from types import SimpleNamespace

import presidio_helpers


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


def test_registration_tolerates_one_duplicate_or_registry_failure(monkeypatch):
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
