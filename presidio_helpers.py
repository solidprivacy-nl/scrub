"""Helper methods for the Presidio Streamlit app."""

from typing import List, Optional, Tuple
import logging

import streamlit as st
from presidio_analyzer import (
    AnalyzerEngine,
    RecognizerResult,
    RecognizerRegistry,
    PatternRecognizer,
    Pattern,
)
from presidio_analyzer.nlp_engine import NlpEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

from openai_fake_data_generator import (
    call_completion_model,
    OpenAIParams,
    create_prompt,
)
from presidio_nlp_engine_config import (
    create_nlp_engine_with_spacy,
    create_nlp_engine_with_flair,
    create_nlp_engine_with_transformers,
    create_nlp_engine_with_azure_ai_language,
    create_nlp_engine_with_stanza,
)

try:
    from dutch_recognizers import get_dutch_recognizers, get_dutch_entity_names
except Exception:  # pragma: no cover - keeps original demo usable if file is absent
    get_dutch_recognizers = None
    get_dutch_entity_names = None


logger = logging.getLogger("presidio-streamlit")


@st.cache_resource
def nlp_engine_and_registry(
    model_family: str,
    model_path: str,
    ta_key: Optional[str] = None,
    ta_endpoint: Optional[str] = None,
) -> Tuple[NlpEngine, RecognizerRegistry]:
    """Create the NLP engine and recognizer registry for the selected model."""

    if "spacy" in model_family.lower():
        return create_nlp_engine_with_spacy(model_path)

    if "stanza" in model_family.lower():
        return create_nlp_engine_with_stanza(model_path)

    if "flair" in model_family.lower():
        return create_nlp_engine_with_flair(model_path)

    if "huggingface" in model_family.lower():
        return create_nlp_engine_with_transformers(model_path)

    if "azure ai language" in model_family.lower():
        return create_nlp_engine_with_azure_ai_language(ta_key, ta_endpoint)

    raise ValueError(f"Model family {model_family} not supported")


@st.cache_resource
def analyzer_engine(
    model_family: str,
    model_path: str,
    ta_key: Optional[str] = None,
    ta_endpoint: Optional[str] = None,
) -> AnalyzerEngine:
    """Create the AnalyzerEngine and register Dutch/EU recognizers."""

    nlp_engine, registry = nlp_engine_and_registry(
        model_family, model_path, ta_key, ta_endpoint
    )

    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, registry=registry)

    # Register Dutch/EU pattern recognizers. They are registered for language="en"
    # because this demo currently calls analyzer.analyze(language="en") and uses
    # English NER models. This makes Dutch identifiers available without requiring
    # a separate Dutch NLP model.
    if get_dutch_recognizers is not None:
        for recognizer in get_dutch_recognizers(supported_language="en"):
            try:
                analyzer.registry.add_recognizer(recognizer)
            except Exception as exc:  # avoid breaking the demo on duplicate/registry edge cases
                logger.debug("Could not register %s: %s", recognizer, exc)

    return analyzer


@st.cache_resource
def anonymizer_engine():
    """Return AnonymizerEngine."""

    return AnonymizerEngine()


@st.cache_data
def get_supported_entities(
    model_family: str, model_path: str, ta_key: str, ta_endpoint: str
):
    """Return supported entities from the AnalyzerEngine."""

    entities = analyzer_engine(
        model_family, model_path, ta_key, ta_endpoint
    ).get_supported_entities()

    if get_dutch_entity_names is not None:
        for entity in get_dutch_entity_names():
            if entity not in entities:
                entities.append(entity)

    if "GENERIC_PII" not in entities:
        entities.append("GENERIC_PII")

    return entities


@st.cache_data
def analyze(
    model_family: str, model_path: str, ta_key: str, ta_endpoint: str, **kwargs
):
    """Analyze input using AnalyzerEngine and input arguments."""

    if "entities" not in kwargs or "All" in kwargs["entities"]:
        kwargs["entities"] = None

    if "deny_list" in kwargs and kwargs["deny_list"] is not None:
        ad_hoc_recognizer = create_ad_hoc_deny_list_recognizer(kwargs["deny_list"])
        kwargs["ad_hoc_recognizers"] = [ad_hoc_recognizer] if ad_hoc_recognizer else []
        del kwargs["deny_list"]

    if "regex_params" in kwargs and len(kwargs["regex_params"]) > 0:
        ad_hoc_recognizer = create_ad_hoc_regex_recognizer(*kwargs["regex_params"])
        kwargs["ad_hoc_recognizers"] = [ad_hoc_recognizer] if ad_hoc_recognizer else []
        del kwargs["regex_params"]

    return analyzer_engine(model_family, model_path, ta_key, ta_endpoint).analyze(
        **kwargs
    )


def anonymize(
    text: str,
    operator: str,
    analyze_results: List[RecognizerResult],
    mask_char: Optional[str] = None,
    number_of_chars: Optional[str] = None,
    encrypt_key: Optional[str] = None,
):
    """Anonymize identified input using Presidio Anonymizer."""

    if operator == "mask":
        operator_config = {
            "type": "mask",
            "masking_char": mask_char,
            "chars_to_mask": number_of_chars,
            "from_end": False,
        }
    elif operator == "encrypt":
        operator_config = {"key": encrypt_key}
    elif operator == "highlight":
        operator_config = {"lambda": lambda x: x}
    else:
        operator_config = None

    if operator == "highlight":
        operator = "custom"
    elif operator == "synthesize":
        operator = "replace"

    return anonymizer_engine().anonymize(
        text,
        analyze_results,
        operators={"DEFAULT": OperatorConfig(operator, operator_config)},
    )


def annotate(text: str, analyze_results: List[RecognizerResult]):
    """Highlight identified PII entities on the original text."""

    tokens = []
    results = anonymize(
        text=text,
        operator="highlight",
        analyze_results=analyze_results,
    )
    results = sorted(results.items, key=lambda x: x.start)

    for i, res in enumerate(results):
        if i == 0:
            tokens.append(text[: res.start])

        tokens.append((text[res.start : res.end], res.entity_type))

        if i != len(results) - 1:
            tokens.append(text[res.end : results[i + 1].start])
        else:
            tokens.append(text[res.end :])

    return tokens


def create_fake_data(
    text: str,
    analyze_results: List[RecognizerResult],
    openai_params: OpenAIParams,
):
    """Create a synthetic version of the text using OpenAI APIs."""

    if not openai_params.openai_key:
        return "Please provide your OpenAI key"

    results = anonymize(text=text, operator="replace", analyze_results=analyze_results)
    prompt = create_prompt(results.text)
    print(f"Prompt: {prompt}")
    return call_completion_model(prompt=prompt, openai_params=openai_params)


@st.cache_data
def call_openai_api(
    prompt: str, openai_model_name: str, openai_deployment_name: Optional[str] = None
) -> str:
    return call_completion_model(
        prompt, model=openai_model_name, deployment_id=openai_deployment_name
    )


def create_ad_hoc_deny_list_recognizer(
    deny_list=Optional[List[str]],
) -> Optional[PatternRecognizer]:
    if not deny_list:
        return None

    return PatternRecognizer(
        supported_entity="GENERIC_PII", deny_list=deny_list
    )


def create_ad_hoc_regex_recognizer(
    regex: str, entity_type: str, score: float, context: Optional[List[str]] = None
) -> Optional[PatternRecognizer]:
    if not regex:
        return None

    pattern = Pattern(name="Regex pattern", regex=regex, score=score)
    return PatternRecognizer(
        supported_entity=entity_type, patterns=[pattern], context=context
    )
