from dataclasses import dataclass

import pytest

from care_profile_policy import ACTION_REPLACE, ACTION_REVIEW_SELECTED
from recognition_profiles import (
    CURRENT_VISIBLE_PROFILE_IDS,
    DESKTOP_PROFILE_IDS,
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_GENERAL,
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_GENERAL_INTERNATIONAL,
    TARGET_STREAMLIT_PROFILE_IDS,
    entity_names_for_profile,
    get_profile,
    policy_action_for_profile_entity,
    profile_id_from_internal_value,
    profile_id_from_label,
    profile_options,
    profile_snapshot,
    resolve_profile_result_collisions,
    short_profile_options,
)


AVAILABLE = [
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "IBAN_CODE",
    "URL",
    "IP_ADDRESS",
    "GENERIC_PII",
    "DATE_TIME",
    "NL_BSN",
    "NL_BIG_NUMBER",
    "NL_LEGAL_CASE_NUMBER",
    "NL_PATIENT_NUMBER",
    "NL_AGB_CODE",
    "US_SSN",
]
GENERAL = ["NL_BSN", "NL_BIG_NUMBER"]
LEGAL = ["NL_LEGAL_CASE_NUMBER"]
CARE = ["NL_PATIENT_NUMBER", "NL_AGB_CODE"]


@dataclass
class FakeResult:
    entity_type: str
    start: int
    end: int
    score: float = 0.8


def test_current_three_profile_options_are_preserved_exactly():
    assert CURRENT_VISIBLE_PROFILE_IDS == (
        PROFILE_DUTCH_LEGAL_STRICT,
        PROFILE_DUTCH_GENERAL,
        PROFILE_GENERAL_INTERNATIONAL,
    )
    assert profile_options() == (
        ("Juridische controle — streng", "Dutch Legal Strict"),
        ("Algemene Nederlandse controle", "Dutch / EU"),
        ("Algemene internationale controle", "General / International"),
    )


def test_future_streamlit_and_desktop_orders_are_explicit():
    assert TARGET_STREAMLIT_PROFILE_IDS == (
        PROFILE_DUTCH_CARE_STRICT,
        PROFILE_DUTCH_LEGAL_STRICT,
        PROFILE_DUTCH_GENERAL,
        PROFILE_GENERAL_INTERNATIONAL,
    )
    assert DESKTOP_PROFILE_IDS == (
        PROFILE_DUTCH_GENERAL,
        PROFILE_DUTCH_CARE_STRICT,
        PROFILE_DUTCH_LEGAL_STRICT,
        PROFILE_GENERAL_INTERNATIONAL,
    )
    assert [label for label, _ in profile_options(include_care=True)] == [
        "Zorgcontrole — streng",
        "Juridische controle — streng",
        "Algemene Nederlandse controle",
        "Algemene internationale controle",
    ]
    assert [label for label, _ in short_profile_options()] == [
        "Algemeen NL",
        "Zorg",
        "Juridisch",
        "Internationaal",
    ]


def test_profile_thresholds_and_behavior_match_current_and_approved_policy():
    care = get_profile(PROFILE_DUTCH_CARE_STRICT)
    legal = get_profile(PROFILE_DUTCH_LEGAL_STRICT)
    general = get_profile(PROFILE_DUTCH_GENERAL)
    international = get_profile(PROFILE_GENERAL_INTERNATIONAL)

    assert care.threshold == 0.30
    assert care.candidate_scanner == "care"
    assert care.example_collection == "care"
    assert legal.threshold == 0.30
    assert legal.candidate_scanner == "legal"
    assert legal.example_collection == "legal"
    assert general.threshold == 0.35
    assert general.candidate_scanner is None
    assert international.threshold == 0.35
    assert international.entity_groups == ("all_supported",)


def test_profile_lookup_accepts_internal_values_and_labels():
    for profile_id in TARGET_STREAMLIT_PROFILE_IDS:
        profile = get_profile(profile_id)
        assert profile_id_from_internal_value(profile.internal_value) == profile_id
        assert profile_id_from_label(profile.label_nl) == profile_id

    with pytest.raises(ValueError):
        get_profile("unknown")
    with pytest.raises(ValueError):
        profile_id_from_internal_value("unknown")
    with pytest.raises(ValueError):
        profile_id_from_label("unknown")


def test_entity_composition_isolated_by_profile_and_preserves_engine_order():
    general = entity_names_for_profile(
        PROFILE_DUTCH_GENERAL,
        AVAILABLE,
        dutch_general_entities=GENERAL,
        dutch_legal_entities=LEGAL,
        dutch_care_entities=CARE,
    )
    care = entity_names_for_profile(
        PROFILE_DUTCH_CARE_STRICT,
        AVAILABLE,
        dutch_general_entities=GENERAL,
        dutch_legal_entities=LEGAL,
        dutch_care_entities=CARE,
    )
    legal = entity_names_for_profile(
        PROFILE_DUTCH_LEGAL_STRICT,
        AVAILABLE,
        dutch_general_entities=GENERAL,
        dutch_legal_entities=LEGAL,
        dutch_care_entities=CARE,
    )
    international = entity_names_for_profile(
        PROFILE_GENERAL_INTERNATIONAL,
        AVAILABLE,
        dutch_general_entities=GENERAL,
        dutch_legal_entities=LEGAL,
        dutch_care_entities=CARE,
    )

    assert general == [entity for entity in AVAILABLE if entity in set(AVAILABLE[:10] + GENERAL)]
    assert "NL_PATIENT_NUMBER" not in general
    assert "NL_LEGAL_CASE_NUMBER" not in general

    assert "NL_PATIENT_NUMBER" in care
    assert "NL_AGB_CODE" in care
    assert "NL_LEGAL_CASE_NUMBER" not in care

    assert "NL_LEGAL_CASE_NUMBER" in legal
    assert "NL_PATIENT_NUMBER" not in legal
    assert "NL_AGB_CODE" not in legal

    assert international == AVAILABLE


def test_care_policy_actions_are_centralized_without_changing_other_profiles():
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "NL_PATIENT_NUMBER"
    ) == ACTION_REPLACE
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "NL_CARE_PROVIDER_NAME"
    ) == ACTION_REVIEW_SELECTED
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "NL_BIG_NUMBER"
    ) == ACTION_REVIEW_SELECTED
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "ORGANIZATION"
    ) == ACTION_REVIEW_SELECTED
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "LOCATION"
    ) == ACTION_REVIEW_SELECTED
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "DATE_TIME"
    ) == ACTION_REVIEW_SELECTED
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_CARE_STRICT, "PERSON"
    ) == ACTION_REPLACE
    assert policy_action_for_profile_entity(
        PROFILE_DUTCH_LEGAL_STRICT, "NL_BIG_NUMBER"
    ) == ACTION_REPLACE


def test_care_exact_span_precedence_prefers_agb_over_bsn():
    results = [
        FakeResult("NL_BSN", 10, 18, 0.72),
        FakeResult("NL_AGB_CODE", 10, 18, 0.94),
    ]

    resolved = resolve_profile_result_collisions(results, PROFILE_DUTCH_CARE_STRICT)
    assert [result.entity_type for result in resolved] == ["NL_AGB_CODE"]
    assert resolve_profile_result_collisions(results, PROFILE_DUTCH_GENERAL) == results


def test_care_exact_span_precedence_prefers_specific_care_entities():
    results = [
        FakeResult("NL_HEALTHCARE_REFERENCE", 5, 18),
        FakeResult("NL_PATIENT_NUMBER", 5, 18),
        FakeResult("PERSON", 30, 43),
        FakeResult("NL_CARE_PROVIDER_NAME", 30, 43),
        FakeResult("ORGANIZATION", 50, 72),
        FakeResult("NL_CARE_ORGANIZATION", 50, 72),
        FakeResult("DATE_TIME", 80, 90),
        FakeResult("NL_CARE_EVENT_DATE", 80, 90),
    ]

    resolved = resolve_profile_result_collisions(results, PROFILE_DUTCH_CARE_STRICT)
    assert [result.entity_type for result in resolved] == [
        "NL_PATIENT_NUMBER",
        "NL_CARE_PROVIDER_NAME",
        "NL_CARE_ORGANIZATION",
        "NL_CARE_EVENT_DATE",
    ]


def test_partial_overlaps_and_unrelated_exact_entities_are_preserved():
    results = [
        FakeResult("NL_BSN", 10, 18),
        FakeResult("NL_AGB_CODE", 10, 17),
        FakeResult("NL_PHONE_NUMBER", 30, 40),
        FakeResult("PERSON", 30, 40),
    ]

    assert resolve_profile_result_collisions(
        results, PROFILE_DUTCH_CARE_STRICT
    ) == results


def test_collision_resolver_supports_mapping_results_and_preserves_input_order():
    results = [
        {"entity_type": "NL_BSN", "start": 0, "end": 8, "score": 0.72},
        {"entity_type": "NL_AGB_CODE", "start": 0, "end": 8, "score": 0.94},
        {"entity_type": "NL_PHONE_NUMBER", "start": 20, "end": 30, "score": 0.85},
    ]

    resolved = resolve_profile_result_collisions(results, PROFILE_DUTCH_CARE_STRICT)
    assert resolved == [results[1], results[2]]


def test_profile_snapshot_keeps_live_integration_gates_closed():
    snapshot = profile_snapshot()

    assert len(snapshot["profiles"]) == 4
    assert snapshot["current_visible_profile_ids"] == list(CURRENT_VISIBLE_PROFILE_IDS)
    assert snapshot["target_streamlit_profile_ids"] == list(TARGET_STREAMLIT_PROFILE_IDS)
    assert snapshot["desktop_profile_ids"] == list(DESKTOP_PROFILE_IDS)
    assert "NL_BSN" in snapshot["care_exact_span_supersedes"]["NL_AGB_CODE"]
    assert snapshot["live_ui_changed"] is False
    assert snapshot["care_recognizers_registered"] is False
    assert snapshot["production_ready"] is False
    assert snapshot["human_review_required"] is True
