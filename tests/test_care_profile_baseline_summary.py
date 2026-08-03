import json
from pathlib import Path

from care_profile_baseline_summary import build_current_care_baseline_summary


BASELINE_PATH = Path("output/validation/care_profile_v1_current_engine_baseline.json")


def test_current_care_baseline_summary_freezes_corrected_counts():
    report = build_current_care_baseline_summary()

    assert report["schema_version"] == "1.1"
    assert report["case_count"] == 8
    assert report["expected_value_count"] == 81
    assert report["found_value_count"] == 25
    assert report["correct_entity_count"] == 14
    assert report["misclassified_value_count"] == 11
    assert report["missed_value_count"] == 56
    assert report["indicative_span_recall"] == 0.308642
    assert report["indicative_correct_entity_recall"] == 0.17284
    assert report["preserve_overlap_count"] == 0
    assert report["production_ready"] is False
    assert report["human_review_required"] is True


def test_current_care_baseline_summary_exposes_policy_gap():
    report = build_current_care_baseline_summary()

    replace = report["policy_summary"]["replace"]
    review = report["policy_summary"]["review_selected"]

    assert replace == {
        "expected": 39,
        "found": 21,
        "correct_entity": 11,
        "misclassified": 10,
        "missed": 18,
        "span_recall": 0.538462,
        "correct_entity_recall": 0.282051,
    }
    assert review == {
        "expected": 42,
        "found": 4,
        "correct_entity": 3,
        "misclassified": 1,
        "missed": 38,
        "span_recall": 0.095238,
        "correct_entity_recall": 0.071429,
    }


def test_current_care_baseline_summary_keeps_clinical_preservation_evidence():
    report = build_current_care_baseline_summary()

    assert all(case["preserve_overlap_count"] == 0 for case in report["cases"])
    assert report["entity_summary"]["NL_ADDRESS"]["correct_entity_recall"] == 1.0
    assert report["entity_summary"]["NL_BIG_NUMBER"]["correct_entity_recall"] == 1.0
    assert report["entity_summary"]["PERSON"]["correct_entity_recall"] == 0.0
    assert report["entity_summary"]["NL_CARE_PROVIDER_NAME"]["found"] == 0
    assert report["entity_summary"]["NL_CARE_ORGANIZATION"]["found"] == 0
    assert report["entity_summary"]["NL_CARE_EVENT_DATE"]["found"] == 0


def test_committed_baseline_artifact_is_exactly_reproducible():
    committed = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    assert committed == build_current_care_baseline_summary()
