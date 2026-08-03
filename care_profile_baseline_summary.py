"""Compact machine-readable summary for the current Zorgfilter baseline."""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, Mapping

from care_profile_baseline import build_current_care_baseline


STATUS_CORRECT_ENTITY = "correct_entity"
STATUS_MISCLASSIFIED = "misclassified"
STATUS_MISSED = "missed"


def _expectation_status(expectation: Mapping[str, Any]) -> str:
    if not expectation.get("found"):
        return STATUS_MISSED
    if expectation.get("expected_entity_type") in set(
        expectation.get("detected_entity_types", [])
    ):
        return STATUS_CORRECT_ENTITY
    return STATUS_MISCLASSIFIED


def build_current_care_baseline_summary() -> Dict[str, Any]:
    """Return compact evidence derived from the unchanged current recognizers."""

    source = build_current_care_baseline()
    entity_summary: dict[str, dict[str, int]] = defaultdict(
        lambda: {
            "expected": 0,
            "found": 0,
            "correct_entity": 0,
            "misclassified": 0,
            "missed": 0,
        }
    )
    policy_summary: dict[str, dict[str, int]] = defaultdict(
        lambda: {
            "expected": 0,
            "found": 0,
            "correct_entity": 0,
            "misclassified": 0,
            "missed": 0,
        }
    )
    cases = []
    correct_entity_count = 0
    misclassified_count = 0
    missed_count = 0

    for case in source["cases"]:
        case_correct = 0
        case_misclassified = 0
        case_missed = 0
        for expectation in case["expectations"]:
            status = _expectation_status(expectation)
            entity_type = str(expectation["expected_entity_type"])
            policy_bucket = str(expectation["policy_bucket"])

            entity_summary[entity_type]["expected"] += 1
            policy_summary[policy_bucket]["expected"] += 1

            if status == STATUS_MISSED:
                entity_summary[entity_type]["missed"] += 1
                policy_summary[policy_bucket]["missed"] += 1
                case_missed += 1
                missed_count += 1
            else:
                entity_summary[entity_type]["found"] += 1
                policy_summary[policy_bucket]["found"] += 1
                if status == STATUS_CORRECT_ENTITY:
                    entity_summary[entity_type]["correct_entity"] += 1
                    policy_summary[policy_bucket]["correct_entity"] += 1
                    case_correct += 1
                    correct_entity_count += 1
                else:
                    entity_summary[entity_type]["misclassified"] += 1
                    policy_summary[policy_bucket]["misclassified"] += 1
                    case_misclassified += 1
                    misclassified_count += 1

        expected = int(case["expected_value_count"])
        found = int(case["found_value_count"])
        cases.append(
            {
                "id": case["id"],
                "name": case["name"],
                "sector": case["sector"],
                "document_type": case["document_type"],
                "expected": expected,
                "found": found,
                "correct_entity": case_correct,
                "misclassified": case_misclassified,
                "missed": case_missed,
                "span_recall": round(found / expected, 6) if expected else 0.0,
                "preserve_overlap_count": len(case["preserve_overlaps"]),
            }
        )

    def with_rates(bucket: Mapping[str, int]) -> Dict[str, Any]:
        result = dict(bucket)
        expected = int(result["expected"])
        result["span_recall"] = (
            round(int(result["found"]) / expected, 6) if expected else 0.0
        )
        result["correct_entity_recall"] = (
            round(int(result["correct_entity"]) / expected, 6)
            if expected
            else 0.0
        )
        return result

    expected_total = int(source["expected_value_count"])
    return {
        "schema_version": "1.1",
        "profile": source["profile"],
        "scope": source["scope"],
        "synthetic_data_only": True,
        "production_ready": False,
        "human_review_required": True,
        "case_count": int(source["case_count"]),
        "expected_value_count": expected_total,
        "found_value_count": int(source["found_value_count"]),
        "correct_entity_count": correct_entity_count,
        "misclassified_value_count": misclassified_count,
        "missed_value_count": missed_count,
        "indicative_span_recall": float(source["indicative_recall"]),
        "indicative_correct_entity_recall": (
            round(correct_entity_count / expected_total, 6)
            if expected_total
            else 0.0
        ),
        "preserve_overlap_count": int(source["preserve_overlap_count"]),
        "policy_summary": {
            key: with_rates(value)
            for key, value in sorted(policy_summary.items())
        },
        "entity_summary": {
            key: with_rates(value)
            for key, value in sorted(entity_summary.items())
        },
        "cases": cases,
    }
