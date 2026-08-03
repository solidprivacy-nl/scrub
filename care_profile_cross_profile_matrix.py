"""Deterministic cross-profile regression matrix for Zorgfilter v1.

The matrix runs the repository's Dutch custom recognizers without a generic NER
model. It verifies profile composition, dedicated Care/Legal isolation, policy
alignment, exact-span collision handling and clinical-context preservation.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Mapping, Sequence

from care_profile_policy import ACTION_REPLACE, ACTION_REVIEW_SELECTED
from care_test_examples import TEST_CASES as CARE_TEST_CASES
from dutch_care_recognizers import (
    get_dutch_care_entity_names,
    get_dutch_care_recognizers,
)
from dutch_recognizers import (
    get_dutch_entity_names,
    get_dutch_general_entity_names,
    get_dutch_legal_entity_names,
    get_dutch_recognizers,
)
from legal_test_examples import TEST_CASES as LEGAL_TEST_CASES
from recognition_profiles import (
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_GENERAL,
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_GENERAL_INTERNATIONAL,
    TARGET_STREAMLIT_PROFILE_IDS,
    entity_names_for_profile,
    get_profile,
    policy_action_for_profile_entity,
    resolve_profile_result_collisions,
)


PROFILE_IDS = TARGET_STREAMLIT_PROFILE_IDS
PROFILE_LABELS = {
    profile_id: get_profile(profile_id).label_nl for profile_id in PROFILE_IDS
}


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def _all_entity_names() -> List[str]:
    return list(
        dict.fromkeys(
            list(get_dutch_entity_names(include_legal=True))
            + list(get_dutch_care_entity_names())
        )
    )


def _profile_entities(profile_id: str) -> List[str]:
    return entity_names_for_profile(
        profile_id,
        _all_entity_names(),
        dutch_general_entities=get_dutch_general_entity_names(),
        dutch_legal_entities=get_dutch_legal_entity_names(),
        dutch_care_entities=get_dutch_care_entity_names(),
    )


def _row(text: str, result: Any, recognizer_name: str) -> Dict[str, Any]:
    start = int(getattr(result, "start"))
    end = int(getattr(result, "end"))
    return {
        "text": text[start:end],
        "entity_type": str(getattr(result, "entity_type", "")),
        "start": start,
        "end": end,
        "score": float(getattr(result, "score", 0.0) or 0.0),
        "recognizer": recognizer_name,
    }


def detect_custom_profile(text: str, profile_id: str) -> List[Dict[str, Any]]:
    """Run all deterministic custom recognizers for one configured profile."""

    entities = _profile_entities(profile_id)
    recognizers = list(get_dutch_recognizers(supported_language="en")) + list(
        get_dutch_care_recognizers(supported_language="en")
    )
    rows: List[Dict[str, Any]] = []
    for recognizer in recognizers:
        if not set(recognizer.supported_entities) & set(entities):
            continue
        results = recognizer.analyze(text, entities=entities, nlp_artifacts=None)
        rows.extend(_row(text, result, recognizer.name) for result in results)

    rows = resolve_profile_result_collisions(rows, profile_id)
    by_key: Dict[tuple[int, int, str], Dict[str, Any]] = {}
    for row in rows:
        key = (int(row["start"]), int(row["end"]), str(row["entity_type"]))
        previous = by_key.get(key)
        if previous is None or float(row["score"]) > float(previous["score"]):
            by_key[key] = row
    return sorted(
        by_key.values(),
        key=lambda item: (item["start"], item["end"], item["entity_type"]),
    )


def _exact_matches(
    rows: Sequence[Mapping[str, Any]], value: str, entity_type: str | None = None
) -> List[Mapping[str, Any]]:
    normalized = _normalize(value)
    return [
        row
        for row in rows
        if _normalize(str(row.get("text", ""))) == normalized
        and (entity_type is None or row.get("entity_type") == entity_type)
    ]


def _phrase_spans(text: str, phrase: str) -> List[tuple[int, int]]:
    spans: List[tuple[int, int]] = []
    offset = 0
    while True:
        start = text.find(phrase, offset)
        if start < 0:
            return spans
        spans.append((start, start + len(phrase)))
        offset = start + max(1, len(phrase))


def _overlaps(first: tuple[int, int], second: tuple[int, int]) -> bool:
    return first[0] < second[1] and second[0] < first[1]


def _preserve_overlaps(
    text: str,
    preserve_phrases: Iterable[str],
    rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, str]]:
    overlaps: List[Dict[str, str]] = []
    for phrase in preserve_phrases:
        for phrase_span in _phrase_spans(text, phrase):
            for row in rows:
                result_span = (int(row["start"]), int(row["end"]))
                if _overlaps(phrase_span, result_span):
                    overlaps.append(
                        {
                            "preserve_phrase": phrase,
                            "detected_text": str(row["text"]),
                            "entity_type": str(row["entity_type"]),
                        }
                    )
    return overlaps


def _failure(
    category: str,
    profile_id: str,
    case_id: str,
    detail: str,
) -> Dict[str, str]:
    return {
        "category": category,
        "profile_id": profile_id,
        "profile_label": PROFILE_LABELS[profile_id],
        "case_id": case_id,
        "detail": detail,
    }


def build_cross_profile_matrix() -> Dict[str, Any]:
    care_entities = set(get_dutch_care_entity_names())
    legal_entities = set(get_dutch_legal_entity_names())
    general_entities = set(get_dutch_general_entity_names())
    hard_failures: List[Dict[str, str]] = []
    care_case_summaries: List[Dict[str, Any]] = []
    legal_case_summaries: List[Dict[str, Any]] = []
    care_expected_total = 0
    care_expected_found = 0
    legal_expected_total = 0
    legal_expected_found = 0
    preserve_overlap_total = 0

    for case in CARE_TEST_CASES:
        case_id = str(case["id"])
        text = str(case["text"])
        rows_by_profile = {
            profile_id: detect_custom_profile(text, profile_id)
            for profile_id in PROFILE_IDS
        }
        dedicated_expectations = [
            item
            for bucket in ("replace", "review_selected")
            for item in case.get(bucket, [])
            if str(item["entity_type"]) in care_entities
        ]
        case_summary = {
            "case_id": case_id,
            "dedicated_care_expectation_count": len(dedicated_expectations),
            "profile_result_counts": {
                profile_id: len(rows) for profile_id, rows in rows_by_profile.items()
            },
            "preserve_overlap_counts": {},
        }

        for item in dedicated_expectations:
            value = str(item["value"])
            entity_type = str(item["entity_type"])
            for profile_id in (
                PROFILE_DUTCH_CARE_STRICT,
                PROFILE_GENERAL_INTERNATIONAL,
            ):
                care_expected_total += 1
                matches = _exact_matches(rows_by_profile[profile_id], value, entity_type)
                if matches:
                    care_expected_found += 1
                else:
                    hard_failures.append(
                        _failure(
                            "missing_dedicated_care_expectation",
                            profile_id,
                            case_id,
                            f"{entity_type}: {value}",
                        )
                    )

        for profile_id in (PROFILE_DUTCH_GENERAL, PROFILE_DUTCH_LEGAL_STRICT):
            leaked = sorted(
                {
                    str(row["entity_type"])
                    for row in rows_by_profile[profile_id]
                    if str(row["entity_type"]) in care_entities
                }
            )
            if leaked:
                hard_failures.append(
                    _failure(
                        "dedicated_care_entity_leakage",
                        profile_id,
                        case_id,
                        ", ".join(leaked),
                    )
                )

        for bucket, expected_action in (
            ("replace", ACTION_REPLACE),
            ("review_selected", ACTION_REVIEW_SELECTED),
        ):
            for item in case.get(bucket, []):
                entity_type = str(item["entity_type"])
                actual = policy_action_for_profile_entity(
                    PROFILE_DUTCH_CARE_STRICT, entity_type
                )
                if actual != expected_action:
                    hard_failures.append(
                        _failure(
                            "care_policy_mismatch",
                            PROFILE_DUTCH_CARE_STRICT,
                            case_id,
                            f"{entity_type}: expected {expected_action}, got {actual}",
                        )
                    )

        for profile_id, rows in rows_by_profile.items():
            overlaps = _preserve_overlaps(text, case.get("preserve", []), rows)
            case_summary["preserve_overlap_counts"][profile_id] = len(overlaps)
            preserve_overlap_total += len(overlaps)
            for overlap in overlaps:
                hard_failures.append(
                    _failure(
                        "clinical_preserve_overlap",
                        profile_id,
                        case_id,
                        (
                            f"{overlap['entity_type']} matched {overlap['detected_text']!r} "
                            f"inside {overlap['preserve_phrase']!r}"
                        ),
                    )
                )
        care_case_summaries.append(case_summary)

    for index, case in enumerate(LEGAL_TEST_CASES):
        case_id = f"legal_{index + 1:02d}"
        text = str(case["text"])
        rows_by_profile = {
            profile_id: detect_custom_profile(text, profile_id)
            for profile_id in PROFILE_IDS
        }
        expected_legal_types = sorted(
            set(str(value) for value in case.get("should_contain", []))
            & legal_entities
        )
        forbidden_types = sorted(
            set(str(value) for value in case.get("should_not_contain", []))
        )
        for entity_type in expected_legal_types:
            for profile_id in (
                PROFILE_DUTCH_LEGAL_STRICT,
                PROFILE_GENERAL_INTERNATIONAL,
            ):
                legal_expected_total += 1
                if any(
                    row["entity_type"] == entity_type
                    for row in rows_by_profile[profile_id]
                ):
                    legal_expected_found += 1
                else:
                    hard_failures.append(
                        _failure(
                            "missing_legal_expectation",
                            profile_id,
                            case_id,
                            entity_type,
                        )
                    )

        for profile_id in (PROFILE_DUTCH_GENERAL, PROFILE_DUTCH_CARE_STRICT):
            leaked = sorted(
                {
                    str(row["entity_type"])
                    for row in rows_by_profile[profile_id]
                    if str(row["entity_type"]) in legal_entities
                }
            )
            if leaked:
                hard_failures.append(
                    _failure(
                        "dedicated_legal_entity_leakage",
                        profile_id,
                        case_id,
                        ", ".join(leaked),
                    )
                )

        for profile_id in PROFILE_IDS:
            found_forbidden = sorted(
                {
                    entity_type
                    for entity_type in forbidden_types
                    if any(
                        row["entity_type"] == entity_type
                        for row in rows_by_profile[profile_id]
                    )
                }
            )
            if found_forbidden:
                hard_failures.append(
                    _failure(
                        "forbidden_legal_entity",
                        profile_id,
                        case_id,
                        ", ".join(found_forbidden),
                    )
                )

        legal_case_summaries.append(
            {
                "case_id": case_id,
                "name": str(case["name"]),
                "expected_legal_entity_types": expected_legal_types,
                "profile_result_counts": {
                    profile_id: len(rows)
                    for profile_id, rows in rows_by_profile.items()
                },
            }
        )

    profile_entities = {
        profile_id: _profile_entities(profile_id) for profile_id in PROFILE_IDS
    }
    for entity_type in general_entities:
        for profile_id in PROFILE_IDS:
            if entity_type not in profile_entities[profile_id]:
                hard_failures.append(
                    _failure(
                        "shared_general_entity_missing",
                        profile_id,
                        "profile_configuration",
                        entity_type,
                    )
                )
    for entity_type in care_entities:
        for profile_id in (PROFILE_DUTCH_CARE_STRICT, PROFILE_GENERAL_INTERNATIONAL):
            if entity_type not in profile_entities[profile_id]:
                hard_failures.append(
                    _failure(
                        "care_entity_not_enabled",
                        profile_id,
                        "profile_configuration",
                        entity_type,
                    )
                )
        for profile_id in (PROFILE_DUTCH_GENERAL, PROFILE_DUTCH_LEGAL_STRICT):
            if entity_type in profile_entities[profile_id]:
                hard_failures.append(
                    _failure(
                        "care_entity_enabled_in_wrong_profile",
                        profile_id,
                        "profile_configuration",
                        entity_type,
                    )
                )
    for entity_type in legal_entities:
        for profile_id in (PROFILE_DUTCH_LEGAL_STRICT, PROFILE_GENERAL_INTERNATIONAL):
            if entity_type not in profile_entities[profile_id]:
                hard_failures.append(
                    _failure(
                        "legal_entity_not_enabled",
                        profile_id,
                        "profile_configuration",
                        entity_type,
                    )
                )
        for profile_id in (PROFILE_DUTCH_GENERAL, PROFILE_DUTCH_CARE_STRICT):
            if entity_type in profile_entities[profile_id]:
                hard_failures.append(
                    _failure(
                        "legal_entity_enabled_in_wrong_profile",
                        profile_id,
                        "profile_configuration",
                        entity_type,
                    )
                )

    return {
        "schema_version": "1.0",
        "scope": "deterministic Dutch custom recognizers; generic NER excluded",
        "synthetic_data_only": True,
        "production_ready": False,
        "human_review_required": True,
        "profile_ids": list(PROFILE_IDS),
        "profile_labels": PROFILE_LABELS,
        "profile_entity_counts": {
            profile_id: len(entities)
            for profile_id, entities in profile_entities.items()
        },
        "general_entity_count": len(general_entities),
        "dedicated_care_entity_count": len(care_entities),
        "dedicated_legal_entity_count": len(legal_entities),
        "care_case_count": len(care_case_summaries),
        "legal_case_count": len(legal_case_summaries),
        "care_expected_total": care_expected_total,
        "care_expected_found": care_expected_found,
        "legal_expected_total": legal_expected_total,
        "legal_expected_found": legal_expected_found,
        "clinical_preserve_overlap_count": preserve_overlap_total,
        "hard_failure_count": len(hard_failures),
        "hard_failures": hard_failures,
        "care_cases": care_case_summaries,
        "legal_cases": legal_case_summaries,
        "generic_ner_evaluated": False,
        "next_workpackage": "SCRUB-WP_CARE_PROFILE_APP_VERIFY",
    }
