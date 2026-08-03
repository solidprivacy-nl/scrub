from care_profile_gap_triage import (
    ROUTE_CARE_RECLASSIFICATION,
    ROUTE_CARE_REFERENCE,
    ROUTE_COLLISION_GUARD,
    ROUTE_CONTEXTUAL_REVIEW,
    ROUTE_GENERIC_PROFILE,
    ROUTE_REUSE_CURRENT,
    build_care_profile_gap_triage,
)


def test_gap_triage_classifies_every_baseline_expectation():
    report = build_care_profile_gap_triage()

    assert report["schema_version"] == "1.0"
    assert report["expectation_count"] == 81
    assert report["classified_count"] == 81
    assert report["unclassified_count"] == 0
    assert len(report["items"]) == 81
    assert report["production_ready"] is False
    assert report["human_review_required"] is True


def test_gap_triage_preserves_corrected_baseline_status_counts():
    report = build_care_profile_gap_triage()

    assert report["status_counts"] == {
        "correct_entity": 14,
        "misclassified": 11,
        "missed": 56,
    }


def test_gap_triage_routes_are_complete_and_evidence_driven():
    report = build_care_profile_gap_triage()

    assert report["route_counts"] == {
        ROUTE_CARE_RECLASSIFICATION: 10,
        ROUTE_CARE_REFERENCE: 5,
        ROUTE_COLLISION_GUARD: 3,
        ROUTE_CONTEXTUAL_REVIEW: 36,
        ROUTE_GENERIC_PROFILE: 13,
        ROUTE_REUSE_CURRENT: 14,
    }


def test_agb_values_always_route_to_collision_guard():
    report = build_care_profile_gap_triage()
    agb_items = [
        item for item in report["items"]
        if item["expected_entity_type"] == "NL_AGB_CODE"
    ]

    assert len(agb_items) == 3
    assert {item["primary_route"] for item in agb_items} == {
        ROUTE_COLLISION_GUARD
    }
    assert all("bsn_agb_collision_guard" in item["required_contracts"] for item in agb_items)


def test_broad_healthcare_matches_route_to_specific_reclassification():
    report = build_care_profile_gap_triage()
    patient_items = [
        item for item in report["items"]
        if item["expected_entity_type"] == "NL_PATIENT_NUMBER"
    ]

    assert len(patient_items) == 3
    assert all(item["baseline_status"] == "misclassified" for item in patient_items)
    assert all(
        item["primary_route"] == ROUTE_CARE_RECLASSIFICATION
        for item in patient_items
    )
    assert all(
        "NL_HEALTHCARE_REFERENCE" in item["detected_entity_types"]
        for item in patient_items
    )


def test_generic_ner_exclusions_do_not_open_numeric_care_regexes():
    report = build_care_profile_gap_triage()
    generic_items = [
        item for item in report["items"]
        if item["expected_entity_type"] in {"PERSON", "EMAIL_ADDRESS"}
    ]

    assert len(generic_items) == 13
    assert all(item["primary_route"] == ROUTE_GENERIC_PROFILE for item in generic_items)


def test_contextual_review_layer_is_largest_gap_family():
    report = build_care_profile_gap_triage()
    contextual = [
        item for item in report["items"]
        if item["primary_route"] == ROUTE_CONTEXTUAL_REVIEW
    ]

    assert len(contextual) == 36
    assert {item["policy_bucket"] for item in contextual} == {"review_selected"}


def test_contract_families_include_clinical_preservation_guards():
    report = build_care_profile_gap_triage()
    families = {family["id"]: family for family in report["contract_families"]}

    assert "care_reference_identifiers" in families
    assert "care_contextual_review" in families
    assert "care_collision_prevention" in families
    assert "clinical_preservation_guards" in families
    assert any(
        "medication" in requirement.lower() or "medicatie" in requirement.lower()
        for requirement in families["clinical_preservation_guards"]["requirements"]
    )
    assert report["next_workpackage"] == "SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS"
