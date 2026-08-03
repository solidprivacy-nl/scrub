from dataclasses import dataclass

from care_profile_policy import ACTION_REVIEW_SELECTED
from profile_ui_support import (
    care_example_names,
    care_example_text,
    configured_description,
    configured_entity_names,
    configured_threshold,
    current_profile_options_with_care,
    detected_reason,
    profile_id_for_internal_value,
    resolve_configured_analysis_results,
    scan_configured_candidates,
)
from recognition_profiles import PROFILE_DUTCH_CARE_STRICT


@dataclass
class Result:
    entity_type: str
    start: int
    end: int


def test_current_profile_options_add_care_without_renaming_existing_profiles():
    assert list(current_profile_options_with_care().items()) == [
        ("Zorgcontrole — streng", "Dutch Care Strict"),
        ("Juridische controle — streng", "Dutch Legal Strict"),
        ("Algemene Nederlandse controle", "Dutch / EU"),
        ("Algemene internationale controle", "General / International"),
    ]


def test_care_profile_threshold_description_and_identity_are_available():
    assert profile_id_for_internal_value("Dutch Care Strict") == PROFILE_DUTCH_CARE_STRICT
    assert configured_threshold("Dutch Care Strict") == 0.30
    description = configured_description("Dutch Care Strict")
    assert "patiënt" in description.lower()
    assert "medicatie" in description.lower()


def test_care_profile_entity_defaults_include_general_and_care_but_not_legal():
    available = [
        "PERSON",
        "EMAIL_ADDRESS",
        "NL_BSN",
        "NL_PATIENT_NUMBER",
        "NL_AGB_CODE",
        "NL_LEGAL_CASE_NUMBER",
    ]
    resolved = configured_entity_names(
        "Dutch Care Strict",
        available,
        dutch_general_entities=["NL_BSN"],
        dutch_legal_entities=["NL_LEGAL_CASE_NUMBER"],
        dutch_care_entities=["NL_PATIENT_NUMBER", "NL_AGB_CODE"],
    )

    assert resolved == [
        "PERSON",
        "EMAIL_ADDRESS",
        "NL_BSN",
        "NL_PATIENT_NUMBER",
        "NL_AGB_CODE",
    ]


def test_care_profile_collision_resolution_removes_exact_legacy_duplicates():
    results = [
        Result("NL_BSN", 0, 8),
        Result("NL_AGB_CODE", 0, 8),
        Result("PERSON", 20, 35),
        Result("NL_CARE_PROVIDER_NAME", 20, 35),
    ]

    resolved = resolve_configured_analysis_results("Dutch Care Strict", results)
    assert [item.entity_type for item in resolved] == [
        "NL_AGB_CODE",
        "NL_CARE_PROVIDER_NAME",
    ]


def test_profile_candidate_dispatch_is_care_specific_and_review_only():
    text = "Patiëntnummer: PAT.2026.1148."
    care = scan_configured_candidates("Dutch Care Strict", text)
    general = scan_configured_candidates("Dutch / EU", text)

    assert len(care) == 1
    assert care[0]["entity_type"] == "NL_PATIENT_NUMBER"
    assert care[0]["text"] == "PAT.2026.1148"
    assert general == []


def test_care_review_selected_entities_get_explicit_reason():
    assert detected_reason(
        "Dutch Care Strict", "NL_CARE_PROVIDER_NAME"
    ) == "Automatisch herkend — controleren"
    assert detected_reason(
        "Dutch Care Strict", "NL_PATIENT_NUMBER"
    ) == "Automatisch herkend"
    assert detected_reason(
        "Dutch Legal Strict", "NL_CARE_PROVIDER_NAME"
    ) == "Automatisch herkend"


def test_synthetic_care_examples_are_available_by_stable_name():
    names = care_example_names()
    assert len(names) == 8
    assert len(set(names)) == 8
    assert any("rapportage" in name.lower() for name in names)
    assert any("ontslagbrief" in name.lower() for name in names)

    text = care_example_text(names[0])
    assert text
    assert "synthet" not in text.lower()
    assert care_example_text("bestaat niet") == ""
