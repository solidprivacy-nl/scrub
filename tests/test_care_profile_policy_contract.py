from care_profile_policy import (
    ACTION_AUDIT_ONLY,
    ACTION_PRESERVE,
    ACTION_REPLACE,
    ACTION_REVIEW_SELECTED,
    entities_for_action,
    policy_for_entity,
    policy_snapshot,
    validate_care_policy_rules,
)


def test_care_policy_contract_is_structurally_valid():
    assert validate_care_policy_rules() == ()


def test_all_four_policy_actions_are_used():
    assert entities_for_action(ACTION_REPLACE)
    assert entities_for_action(ACTION_REVIEW_SELECTED)
    assert entities_for_action(ACTION_PRESERVE)
    assert entities_for_action(ACTION_AUDIT_ONLY)


def test_approved_care_policy_preferences_are_frozen():
    assert policy_for_entity("NL_DATE_OF_BIRTH").action == ACTION_REPLACE
    assert policy_for_entity("NL_PATIENT_NUMBER").action == ACTION_REPLACE
    assert policy_for_entity("NL_CARE_PROVIDER_NAME").action == ACTION_REVIEW_SELECTED
    assert policy_for_entity("NL_BIG_NUMBER").action == ACTION_REVIEW_SELECTED
    assert policy_for_entity("NL_AGB_CODE").action == ACTION_REVIEW_SELECTED
    assert policy_for_entity("CARE_DIAGNOSIS").action == ACTION_PRESERVE
    assert policy_for_entity("CARE_MEDICATION").action == ACTION_PRESERVE
    assert policy_for_entity("CARE_LAB_RESULT").action == ACTION_PRESERVE
    assert policy_for_entity("CARE_OBSERVATION").action == ACTION_PRESERVE
    assert policy_for_entity("CARE_RARE_CASE_COMBINATION").action == ACTION_AUDIT_ONLY


def test_clinical_codes_are_not_blindly_replaced():
    assert policy_for_entity("CARE_CLINICAL_CODE").action == ACTION_PRESERVE
    assert "CARE_CLINICAL_CODE" not in entities_for_action(ACTION_REPLACE)


def test_policy_snapshot_is_stable_and_complete():
    snapshot = policy_snapshot()
    assert snapshot["NL_EPD_ECD_NUMBER"] == ACTION_REPLACE
    assert snapshot["NL_CARE_EVENT_DATE"] == ACTION_REVIEW_SELECTED
    assert snapshot["CARE_DOSAGE"] == ACTION_PRESERVE
    assert len(snapshot) == len(set(snapshot))
