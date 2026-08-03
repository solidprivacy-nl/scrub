from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _identity_cache_decorator(func=None, **_kwargs):
    if func is None:
        return lambda wrapped: wrapped
    return func


def _load_presidio_helpers_with_optional_dependency_stubs():
    streamlit = ModuleType("streamlit")
    streamlit.cache_resource = _identity_cache_decorator
    streamlit.cache_data = _identity_cache_decorator

    anonymizer = ModuleType("presidio_anonymizer")
    anonymizer.AnonymizerEngine = type("AnonymizerEngine", (), {})
    anonymizer_entities = ModuleType("presidio_anonymizer.entities")
    anonymizer_entities.OperatorConfig = type("OperatorConfig", (), {})

    fake_data = ModuleType("openai_fake_data_generator")
    fake_data.call_completion_model = lambda *_args, **_kwargs: ""
    fake_data.OpenAIParams = object
    fake_data.create_prompt = lambda text: text

    nlp_config = ModuleType("presidio_nlp_engine_config")
    for name in (
        "create_nlp_engine_with_spacy",
        "create_nlp_engine_with_flair",
        "create_nlp_engine_with_transformers",
        "create_nlp_engine_with_azure_ai_language",
        "create_nlp_engine_with_stanza",
    ):
        setattr(nlp_config, name, lambda *_args, **_kwargs: None)

    stubs = {
        "streamlit": streamlit,
        "presidio_anonymizer": anonymizer,
        "presidio_anonymizer.entities": anonymizer_entities,
        "openai_fake_data_generator": fake_data,
        "presidio_nlp_engine_config": nlp_config,
    }
    previous = {name: sys.modules.get(name) for name in stubs}
    sys.modules.update(stubs)
    try:
        module_path = Path(__file__).resolve().parents[1] / "presidio_helpers.py"
        spec = importlib.util.spec_from_file_location(
            "presidio_helpers_care_registration_test_module", module_path
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        for name, original in previous.items():
            if original is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = original


presidio_helpers = _load_presidio_helpers_with_optional_dependency_stubs()


class Registry:
    def __init__(self):
        self.recognizers = []

    def add_recognizer(self, recognizer):
        self.recognizers.append(recognizer)


class Analyzer:
    def __init__(self):
        self.registry = Registry()


def test_custom_entity_names_include_general_legal_and_dedicated_care_entities():
    names = presidio_helpers.get_custom_entity_names()

    assert "NL_BSN" in names
    assert "NL_LEGAL_CASE_NUMBER" in names
    assert "NL_PATIENT_NUMBER" in names
    assert "NL_AGB_CODE" in names
    assert len(names) == len(set(names))


def test_custom_recognizer_registration_includes_care_without_network_behavior():
    analyzer = Analyzer()
    presidio_helpers.register_custom_recognizers(analyzer)

    supported = {
        entity
        for recognizer in analyzer.registry.recognizers
        for entity in recognizer.supported_entities
    }
    assert "NL_BSN" in supported
    assert "NL_LEGAL_CASE_NUMBER" in supported
    assert "NL_PATIENT_NUMBER" in supported
    assert "NL_AGB_CODE" in supported


def test_registration_tolerates_one_duplicate_or_registry_failure():
    analyzer = Analyzer()
    calls = []

    class FailingRegistry:
        def add_recognizer(self, recognizer):
            calls.append(recognizer)
            if len(calls) == 1:
                raise ValueError("duplicate")

    analyzer.registry = FailingRegistry()
    presidio_helpers.register_custom_recognizers(analyzer)
    assert len(calls) > 1
