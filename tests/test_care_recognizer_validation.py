import json
from pathlib import Path

from care_recognizer_validation import build_care_recognizer_validation


VALIDATION_PATH = Path("output/validation/care_recognizer_implementation_validation.json")


def test_care_recognizer_implementation_passes_frozen_contracts():
    report = build_care_recognizer_validation()

    assert report["schema_version"] == "1.0"
    assert report["entity_count"] == 16
    assert report["positive_contract_count"] == 37
    assert report["positive_contract_passed"] == 37
    assert report["positive_contract_failures"] == []
    assert report["forbidden_positive_failure_count"] == 0
    assert report["forbidden_positive_failures"] == []
    assert report["negative_contract_count"] == 16
    assert report["negative_contract_passed"] == 16
    assert report["negative_contract_failures"] == []


def test_care_recognizers_cover_all_dedicated_corpus_expectations():
    report = build_care_recognizer_validation()

    assert report["corpus_dedicated_expectation_count"] == 54
    assert report["corpus_dedicated_found_count"] == 54
    assert report["corpus_dedicated_failures"] == []
    assert report["clinical_preserve_overlap_count"] == 0
    assert report["clinical_preserve_overlaps"] == []


def test_care_recognizer_validation_keeps_integration_gates_closed():
    report = build_care_recognizer_validation()

    assert report["synthetic_data_only"] is True
    assert report["production_ready"] is False
    assert report["human_review_required"] is True
    assert report["app_registered"] is False
    assert report["next_workpackage"] == "SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR"


def test_committed_care_recognizer_validation_is_reproducible():
    committed = json.loads(VALIDATION_PATH.read_text(encoding="utf-8"))
    assert committed == build_care_recognizer_validation()
