from pathlib import Path

import pytest

from care_profile_cross_profile_matrix import build_cross_profile_matrix
from recognition_profiles import (
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_GENERAL,
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_GENERAL_INTERNATIONAL,
)


@pytest.fixture(scope="module")
def matrix():
    return build_cross_profile_matrix()


def _failure_lines(matrix):
    return "\n".join(
        (
            f"{item['category']} | {item['profile_id']} | "
            f"{item['case_id']} | {item['detail']}"
        )
        for item in matrix["hard_failures"]
    )


def test_cross_profile_matrix_is_synthetic_and_keeps_safety_gates_closed(matrix):
    assert matrix["schema_version"] == "1.0"
    assert matrix["synthetic_data_only"] is True
    assert matrix["generic_ner_evaluated"] is False
    assert matrix["human_review_required"] is True
    assert matrix["production_ready"] is False
    assert matrix["next_workpackage"] == "SCRUB-WP_CARE_PROFILE_APP_VERIFY"


def test_cross_profile_matrix_covers_all_four_profiles_and_document_families(matrix):
    assert matrix["profile_ids"] == [
        PROFILE_DUTCH_CARE_STRICT,
        PROFILE_DUTCH_LEGAL_STRICT,
        PROFILE_DUTCH_GENERAL,
        PROFILE_GENERAL_INTERNATIONAL,
    ]
    assert matrix["care_case_count"] == 8
    assert matrix["legal_case_count"] > 0
    assert matrix["dedicated_care_entity_count"] == 16
    assert matrix["dedicated_legal_entity_count"] > 0
    assert matrix["general_entity_count"] > 0


def test_care_and_international_find_all_dedicated_care_expectations(matrix):
    assert matrix["care_expected_total"] > 0
    assert matrix["care_expected_found"] == matrix["care_expected_total"]


def test_legal_and_international_retain_legal_expectations(matrix):
    assert matrix["legal_expected_total"] > 0
    assert matrix["legal_expected_found"] == matrix["legal_expected_total"], _failure_lines(matrix)


def test_no_profile_overlaps_protected_clinical_phrases(matrix):
    assert matrix["clinical_preserve_overlap_count"] == 0


def test_cross_profile_matrix_has_no_hard_failures(matrix):
    assert matrix["hard_failure_count"] == 0, _failure_lines(matrix)
    assert matrix["hard_failures"] == []


def test_international_keeps_explicit_all_supported_scope(matrix):
    counts = matrix["profile_entity_counts"]
    assert counts[PROFILE_GENERAL_INTERNATIONAL] > counts[PROFILE_DUTCH_CARE_STRICT]
    assert counts[PROFILE_GENERAL_INTERNATIONAL] > counts[PROFILE_DUTCH_LEGAL_STRICT]
    assert counts[PROFILE_GENERAL_INTERNATIONAL] > counts[PROFILE_DUTCH_GENERAL]
    assert counts[PROFILE_DUTCH_CARE_STRICT] != counts[PROFILE_DUTCH_GENERAL]
    assert counts[PROFILE_DUTCH_LEGAL_STRICT] != counts[PROFILE_DUTCH_GENERAL]


def test_matrix_helper_remains_pure_and_ui_independent():
    source = (
        Path(__file__).resolve().parents[1]
        / "care_profile_cross_profile_matrix.py"
    ).read_text(encoding="utf-8")

    forbidden = (
        "import streamlit",
        "presidio_streamlit",
        "requests.",
        "urllib.",
        "socket.",
        "openai",
        "azure",
    )
    assert not any(token in source.lower() for token in forbidden)
