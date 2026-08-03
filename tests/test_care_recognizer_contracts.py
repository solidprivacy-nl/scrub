import json
from pathlib import Path

from care_profile_policy import ACTION_REPLACE, ACTION_REVIEW_SELECTED, policy_for_entity
from care_recognizer_contract_summary import build_care_recognizer_contract_summary
from care_recognizer_contracts import (
    ALL_POSITIVE_CASES,
    CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION,
    CARE_RECOGNIZER_ENTITY_NAMES,
    CARE_RECOGNIZER_MODULE,
    CARE_RECOGNIZER_PUBLIC_API,
    CARE_RECOGNIZER_SUPPORTED_LANGUAGE,
    CONTEXTUAL_REVIEW_POSITIVE_CASES,
    NEGATIVE_CASES,
    REFERENCE_POSITIVE_CASES,
    contract_snapshot,
)


CONTRACT_SUMMARY_PATH = Path("output/validation/care_recognizer_contract_v1_summary.json")


def test_contract_schema_and_future_public_api_are_frozen():
    assert CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION == "1.0"
    assert CARE_RECOGNIZER_MODULE == "dutch_care_recognizers"
    assert CARE_RECOGNIZER_PUBLIC_API == (
        "get_dutch_care_entity_names",
        "get_dutch_care_recognizers",
    )
    assert CARE_RECOGNIZER_SUPPORTED_LANGUAGE == "en"


def test_contract_covers_all_sixteen_dedicated_care_entities():
    assert len(CARE_RECOGNIZER_ENTITY_NAMES) == 16
    assert len(set(CARE_RECOGNIZER_ENTITY_NAMES)) == 16
    assert {case["entity_type"] for case in ALL_POSITIVE_CASES} == set(
        CARE_RECOGNIZER_ENTITY_NAMES
    )


def test_contract_contains_broad_positive_and_negative_evidence():
    assert len(REFERENCE_POSITIVE_CASES) == 17
    assert len(CONTEXTUAL_REVIEW_POSITIVE_CASES) == 20
    assert len(ALL_POSITIVE_CASES) == 37
    assert len(NEGATIVE_CASES) == 16
    assert len({case["id"] for case in ALL_POSITIVE_CASES}) == 37
    assert len({case["id"] for case in NEGATIVE_CASES}) == 16


def test_every_positive_value_occurs_exactly_once_and_context_is_preserved():
    for case in ALL_POSITIVE_CASES:
        text = case["text"]
        value = case["expected_value"]
        assert text.count(value) == 1, case["id"]
        for preserved in case["preserved_text"]:
            assert preserved in text, f"{case['id']}: missing preserved text {preserved}"
        assert value not in case["preserved_text"], case["id"]


def test_reference_and_contextual_policy_actions_match_approved_care_policy():
    for case in REFERENCE_POSITIVE_CASES:
        expected_action = (
            ACTION_REVIEW_SELECTED
            if case["entity_type"] == "NL_AGB_CODE"
            else ACTION_REPLACE
        )
        assert case["policy_action"] == expected_action, case["id"]
        assert policy_for_entity(case["entity_type"]).action == expected_action

    for case in CONTEXTUAL_REVIEW_POSITIVE_CASES:
        assert case["policy_action"] == ACTION_REVIEW_SELECTED, case["id"]
        assert policy_for_entity(case["entity_type"]).action == ACTION_REVIEW_SELECTED


def test_provider_contracts_preserve_professional_role_words():
    provider_cases = [
        case for case in CONTEXTUAL_REVIEW_POSITIVE_CASES
        if case["entity_type"] == "NL_CARE_PROVIDER_NAME"
    ]

    assert len(provider_cases) == 4
    for case in provider_cases:
        assert case["expected_value"] not in case["preserved_text"]
        assert any(
            role in case["text"].lower()
            for role in (
                "verpleegkundige",
                "internist",
                "huisarts",
                "begeleider",
            )
        )


def test_care_event_dates_forbid_birth_date_classification():
    date_cases = [
        case for case in CONTEXTUAL_REVIEW_POSITIVE_CASES
        if case["entity_type"] == "NL_CARE_EVENT_DATE"
    ]

    assert len(date_cases) == 5
    assert all("NL_DATE_OF_BIRTH" in case["forbidden_entities"] for case in date_cases)


def test_agb_contract_freezes_bsn_collision_precedence():
    agb_case = next(
        case for case in REFERENCE_POSITIVE_CASES
        if case["entity_type"] == "NL_AGB_CODE"
    )
    bsn_negative = next(case for case in NEGATIVE_CASES if case["id"] == "bsn_is_not_agb")
    big_negative = next(case for case in NEGATIVE_CASES if case["id"] == "big_is_not_agb")

    assert agb_case["expected_value"] == "01020304"
    assert "NL_BSN" in agb_case["forbidden_entities"]
    assert "NL_AGB_CODE" in bsn_negative["forbidden_entities"]
    assert "NL_AGB_CODE" in big_negative["forbidden_entities"]


def test_negative_contracts_preserve_clinical_content():
    required_negative_ids = {
        "blood_pressure",
        "temperature",
        "medication_dosage",
        "administration_time",
        "laboratory_result",
        "glucose_result",
        "pain_score",
        "clinical_dbc_code",
        "clinical_icd_code",
        "relative_time_is_not_event_date",
        "professional_role_without_name",
    }
    negative_by_id = {case["id"]: case for case in NEGATIVE_CASES}

    assert required_negative_ids <= set(negative_by_id)
    for case_id in required_negative_ids:
        case = negative_by_id[case_id]
        assert case["forbidden_entities"], case_id
        for preserved in case["preserved_text"]:
            assert preserved in case["text"], f"{case_id}: {preserved}"


def test_contract_snapshot_is_serializable_and_not_a_readiness_claim():
    snapshot = contract_snapshot()

    assert snapshot["schema_version"] == "1.0"
    assert snapshot["module"] == "dutch_care_recognizers"
    assert snapshot["public_api"] == list(CARE_RECOGNIZER_PUBLIC_API)
    assert snapshot["supported_language"] == "en"
    assert snapshot["entity_names"] == list(CARE_RECOGNIZER_ENTITY_NAMES)
    assert len(snapshot["positive_cases"]) == 37
    assert len(snapshot["negative_cases"]) == 16
    assert snapshot["production_ready"] is False
    assert snapshot["human_review_required"] is True


def test_committed_contract_summary_is_reproducible():
    committed = json.loads(CONTRACT_SUMMARY_PATH.read_text(encoding="utf-8"))
    assert committed == build_care_recognizer_contract_summary()
