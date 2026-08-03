"""Pure validation report for the Zorgfilter v1 recognizer implementation."""

from __future__ import annotations

from typing import Any, Dict

from care_recognizer_contracts import ALL_POSITIVE_CASES, NEGATIVE_CASES
from care_test_examples import TEST_CASES
from dutch_care_recognizers import (
    get_dutch_care_entity_names,
    get_dutch_care_recognizers,
)


def _detect(text: str) -> list[dict[str, Any]]:
    entities = get_dutch_care_entity_names()
    rows: list[dict[str, Any]] = []
    for recognizer in get_dutch_care_recognizers(supported_language="en"):
        for result in recognizer.analyze(text, entities=entities, nlp_artifacts=None):
            rows.append(
                {
                    "entity_type": result.entity_type,
                    "start": int(result.start),
                    "end": int(result.end),
                    "text": text[result.start:result.end],
                    "score": float(result.score),
                    "recognizer": recognizer.name,
                }
            )
    return sorted(rows, key=lambda row: (row["start"], row["end"], row["entity_type"]))


def _has_exact(rows: list[dict[str, Any]], entity_type: str, value: str) -> bool:
    return any(
        row["entity_type"] == entity_type and row["text"] == value
        for row in rows
    )


def build_care_recognizer_validation() -> Dict[str, Any]:
    """Return deterministic contract and corpus implementation evidence."""

    positive_failures: list[dict[str, Any]] = []
    forbidden_positive_failures: list[dict[str, Any]] = []
    for case in ALL_POSITIVE_CASES:
        rows = _detect(case["text"])
        if not _has_exact(rows, case["entity_type"], case["expected_value"]):
            positive_failures.append(
                {
                    "id": case["id"],
                    "entity_type": case["entity_type"],
                    "expected_value": case["expected_value"],
                    "detected": rows,
                }
            )
        for forbidden_entity in case["forbidden_entities"]:
            if _has_exact(rows, forbidden_entity, case["expected_value"]):
                forbidden_positive_failures.append(
                    {
                        "id": case["id"],
                        "forbidden_entity": forbidden_entity,
                        "value": case["expected_value"],
                    }
                )

    negative_failures: list[dict[str, Any]] = []
    for case in NEGATIVE_CASES:
        rows = _detect(case["text"])
        violations = [
            row for row in rows
            if row["entity_type"] in set(case["forbidden_entities"])
        ]
        if violations:
            negative_failures.append(
                {
                    "id": case["id"],
                    "violations": violations,
                }
            )

    dedicated_entities = set(get_dutch_care_entity_names())
    corpus_expected = 0
    corpus_found = 0
    corpus_failures: list[dict[str, Any]] = []
    preserve_overlaps: list[dict[str, Any]] = []
    for case in TEST_CASES:
        rows = _detect(case["text"])
        for bucket in ("replace", "review_selected"):
            for expectation in case[bucket]:
                if expectation["entity_type"] not in dedicated_entities:
                    continue
                corpus_expected += 1
                if _has_exact(rows, expectation["entity_type"], expectation["value"]):
                    corpus_found += 1
                else:
                    corpus_failures.append(
                        {
                            "case_id": case["id"],
                            "entity_type": expectation["entity_type"],
                            "value": expectation["value"],
                        }
                    )
        for phrase in case["preserve"]:
            phrase_start = case["text"].index(phrase)
            phrase_end = phrase_start + len(phrase)
            for row in rows:
                if phrase_start < row["end"] and row["start"] < phrase_end:
                    preserve_overlaps.append(
                        {
                            "case_id": case["id"],
                            "phrase": phrase,
                            "entity_type": row["entity_type"],
                            "detected_text": row["text"],
                        }
                    )

    return {
        "schema_version": "1.0",
        "module": "dutch_care_recognizers",
        "synthetic_data_only": True,
        "production_ready": False,
        "human_review_required": True,
        "entity_count": len(dedicated_entities),
        "positive_contract_count": len(ALL_POSITIVE_CASES),
        "positive_contract_passed": len(ALL_POSITIVE_CASES) - len(positive_failures),
        "positive_contract_failures": positive_failures,
        "forbidden_positive_failure_count": len(forbidden_positive_failures),
        "forbidden_positive_failures": forbidden_positive_failures,
        "negative_contract_count": len(NEGATIVE_CASES),
        "negative_contract_passed": len(NEGATIVE_CASES) - len(negative_failures),
        "negative_contract_failures": negative_failures,
        "corpus_dedicated_expectation_count": corpus_expected,
        "corpus_dedicated_found_count": corpus_found,
        "corpus_dedicated_failures": corpus_failures,
        "clinical_preserve_overlap_count": len(preserve_overlaps),
        "clinical_preserve_overlaps": preserve_overlaps,
        "app_registered": False,
        "next_workpackage": "SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR",
    }
