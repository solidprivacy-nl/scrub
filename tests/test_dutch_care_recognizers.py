import ast
import inspect
from pathlib import Path

from care_recognizer_contracts import (
    ALL_POSITIVE_CASES,
    CARE_RECOGNIZER_ENTITY_NAMES,
    NEGATIVE_CASES,
)
from care_test_examples import TEST_CASES
from dutch_care_recognizers import (
    CareRegexCaptureRecognizer,
    get_dutch_care_entity_names,
    get_dutch_care_recognizers,
)


def _detect(text):
    entities = get_dutch_care_entity_names()
    rows = []
    for recognizer in get_dutch_care_recognizers(supported_language="en"):
        for result in recognizer.analyze(text, entities=entities, nlp_artifacts=None):
            rows.append(
                {
                    "entity_type": result.entity_type,
                    "start": result.start,
                    "end": result.end,
                    "text": text[result.start:result.end],
                    "score": result.score,
                    "recognizer": recognizer.name,
                }
            )
    return sorted(rows, key=lambda row: (row["start"], row["end"], row["entity_type"]))


def _exact(rows, entity_type, value):
    return [
        row for row in rows
        if row["entity_type"] == entity_type and row["text"] == value
    ]


def test_public_api_matches_frozen_contract():
    assert get_dutch_care_entity_names() == list(CARE_RECOGNIZER_ENTITY_NAMES)
    recognizers = get_dutch_care_recognizers()
    assert len(recognizers) == len(CARE_RECOGNIZER_ENTITY_NAMES)
    assert {entity for recognizer in recognizers for entity in recognizer.supported_entities} == set(
        CARE_RECOGNIZER_ENTITY_NAMES
    )
    assert all(recognizer.supported_language == "en" for recognizer in recognizers)


def test_all_positive_contracts_return_the_exact_value_span():
    for case in ALL_POSITIVE_CASES:
        rows = _detect(case["text"])
        matches = _exact(rows, case["entity_type"], case["expected_value"])
        assert len(matches) == 1, (case["id"], rows)

        expected_start = case["text"].index(case["expected_value"])
        assert matches[0]["start"] == expected_start
        assert matches[0]["end"] == expected_start + len(case["expected_value"])

        for forbidden_entity in case["forbidden_entities"]:
            assert not _exact(rows, forbidden_entity, case["expected_value"]), (
                case["id"],
                forbidden_entity,
                rows,
            )


def test_all_negative_contracts_avoid_forbidden_care_entities():
    for case in NEGATIVE_CASES:
        rows = _detect(case["text"])
        forbidden = set(case["forbidden_entities"])
        violations = [row for row in rows if row["entity_type"] in forbidden]
        assert violations == [], (case["id"], violations)


def test_capture_results_have_explanations_and_stable_metadata():
    text = "Patiëntnummer: PAT-2026-1148."
    recognizer = next(
        recognizer for recognizer in get_dutch_care_recognizers()
        if recognizer.supported_entities == ["NL_PATIENT_NUMBER"]
    )
    results = recognizer.analyze(
        text,
        entities=get_dutch_care_entity_names(),
        nlp_artifacts=None,
    )

    assert len(results) == 1
    result = results[0]
    assert result.entity_type == "NL_PATIENT_NUMBER"
    assert text[result.start:result.end] == "PAT-2026-1148"
    assert result.analysis_explanation is not None
    assert result.recognition_metadata


def test_care_module_has_no_streamlit_network_cloud_or_file_write_imports():
    source_path = Path(inspect.getsourcefile(CareRegexCaptureRecognizer))
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert imported_roots.isdisjoint(
        {
            "streamlit",
            "requests",
            "httpx",
            "urllib",
            "openai",
            "azure",
            "boto3",
            "pathlib",
            "os",
            "subprocess",
        }
    )


def test_dedicated_care_expectations_in_full_corpus_are_detected_exactly():
    dedicated_entities = set(get_dutch_care_entity_names())
    checked = 0
    missing = []

    for case in TEST_CASES:
        rows = _detect(case["text"])
        for bucket in ("replace", "review_selected"):
            for expectation in case[bucket]:
                if expectation["entity_type"] not in dedicated_entities:
                    continue
                checked += 1
                if not _exact(rows, expectation["entity_type"], expectation["value"]):
                    missing.append(
                        {
                            "case_id": case["id"],
                            "entity_type": expectation["entity_type"],
                            "value": expectation["value"],
                            "detected": rows,
                        }
                    )

    assert checked > 0
    assert missing == []


def test_full_corpus_clinical_preserve_phrases_do_not_overlap_care_results():
    overlaps = []
    for case in TEST_CASES:
        rows = _detect(case["text"])
        for phrase in case["preserve"]:
            phrase_start = case["text"].index(phrase)
            phrase_end = phrase_start + len(phrase)
            for row in rows:
                if phrase_start < row["end"] and row["start"] < phrase_end:
                    overlaps.append(
                        {
                            "case_id": case["id"],
                            "phrase": phrase,
                            "row": row,
                        }
                    )

    assert overlaps == []
