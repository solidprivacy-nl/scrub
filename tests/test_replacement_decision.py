import pytest

from replacement_decision import (
    ReplacementDecision,
    build_replacement_audit,
    build_replacement_decision,
    matching_occurrence_ids,
    normalize_match_text,
)


def test_build_default_decision_is_review_only_and_not_mapping_candidate():
    decision = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
    )

    assert decision.review_state == "needs_review"
    assert decision.replacement_value is None
    assert decision.creates_mapping is False
    assert decision.as_dict()["report_only"] is None if "report_only" in decision.as_dict() else True


def test_accepted_decision_uses_suggested_replacement():
    decision = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        review_state="accepted",
    )

    assert decision.replacement_value == "[PERSOON_1]"
    assert decision.creates_mapping is True


def test_edited_decision_uses_final_replacement():
    decision = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        final_replacement="[CLIËNT_A]",
        review_state="edited",
    )

    assert decision.replacement_value == "[CLIËNT_A]"
    assert decision.creates_mapping is True


def test_ignored_and_context_decisions_do_not_create_mapping():
    ignored = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="ROL-TERM",
        entity_type="ROLE_LABEL",
        display_label="Rolterm",
        suggested_replacement="[ROL_1]",
        review_state="ignored",
    )
    context = build_replacement_decision(
        occurrence_id="occ-2",
        source_text="GETUIGE",
        entity_type="ROLE_LABEL",
        display_label="Contextterm",
        suggested_replacement="[ROL_2]",
        review_state="preserve_context",
    )

    assert ignored.replacement_value is None
    assert ignored.creates_mapping is False
    assert context.replacement_value is None
    assert context.creates_mapping is False


def test_invalid_state_scope_and_confidence_are_rejected():
    with pytest.raises(ValueError, match="Unsupported review_state"):
        build_replacement_decision(
            occurrence_id="occ-1",
            source_text="SYNTHETISCH",
            entity_type="PERSON",
            display_label="Naam",
            suggested_replacement="[PERSOON_1]",
            review_state="done",
        )

    with pytest.raises(ValueError, match="Unsupported scope"):
        build_replacement_decision(
            occurrence_id="occ-1",
            source_text="SYNTHETISCH",
            entity_type="PERSON",
            display_label="Naam",
            suggested_replacement="[PERSOON_1]",
            scope="fuzzy_all",
        )

    with pytest.raises(ValueError, match="confidence"):
        build_replacement_decision(
            occurrence_id="occ-1",
            source_text="SYNTHETISCH",
            entity_type="PERSON",
            display_label="Naam",
            suggested_replacement="[PERSOON_1]",
            confidence=1.5,
        )


def test_this_occurrence_scope_only_selects_one_item():
    decision = build_replacement_decision(
        occurrence_id="occ-2",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        review_state="accepted",
        scope="this_occurrence",
    )
    occurrences = [
        {"occurrence_id": "occ-1", "source_text": "SYNTHETISCH-PERSOON-A"},
        {"occurrence_id": "occ-2", "source_text": "SYNTHETISCH-PERSOON-A"},
    ]

    assert matching_occurrence_ids(decision, occurrences) == ["occ-2"]


def test_exact_scope_selects_exact_same_text_only():
    decision = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        review_state="accepted",
        scope="all_exact",
    )
    occurrences = [
        {"occurrence_id": "occ-1", "source_text": "SYNTHETISCH-PERSOON-A"},
        {"occurrence_id": "occ-2", "source_text": "SYNTHETISCH-PERSOON-A"},
        {"occurrence_id": "occ-3", "source_text": "synthetisch-persoon-a"},
        {"occurrence_id": "occ-4", "source_text": "SYNTHETISCH-PERSOON-B"},
    ]

    assert matching_occurrence_ids(decision, occurrences) == ["occ-1", "occ-2"]


def test_normalized_scope_is_conservative_not_fuzzy():
    decision = build_replacement_decision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH   PERSOON A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        review_state="accepted",
        scope="all_normalized",
    )
    occurrences = [
        {"occurrence_id": "occ-1", "source_text": "SYNTHETISCH PERSOON A"},
        {"occurrence_id": "occ-2", "source_text": "synthetisch persoon a"},
        {"occurrence_id": "occ-3", "source_text": "SYNTHETISCH PERSOON B"},
    ]

    assert normalize_match_text("SYNTHETISCH   PERSOON A") == "synthetisch persoon a"
    assert matching_occurrence_ids(decision, occurrences) == ["occ-1", "occ-2"]


def test_audit_counts_states_and_is_report_only():
    decisions = [
        build_replacement_decision(
            occurrence_id="occ-1",
            source_text="SYNTHETISCH-PERSOON-A",
            entity_type="PERSON",
            display_label="Naam",
            suggested_replacement="[PERSOON_1]",
            review_state="accepted",
            scope="all_exact",
            risk_flags=["same_value_scope_confirmed"],
        ),
        build_replacement_decision(
            occurrence_id="occ-2",
            source_text="ROL-TERM",
            entity_type="ROLE_LABEL",
            display_label="Contextterm",
            suggested_replacement="[ROL_1]",
            review_state="preserve_context",
        ),
        build_replacement_decision(
            occurrence_id="occ-3",
            source_text="SYNTHETISCH-MISSER",
            entity_type="CUSTOM",
            display_label="Handmatig",
            suggested_replacement="[HANDMATIG_1]",
            review_state="manual_added",
            origin="manual",
        ),
    ]

    audit = build_replacement_audit(decisions)

    assert audit["total_decisions"] == 3
    assert audit["state_counts"]["accepted"] == 1
    assert audit["state_counts"]["preserve_context"] == 1
    assert audit["state_counts"]["manual_added"] == 1
    assert audit["context_preserved"] == ["occ-2"]
    assert audit["manual_additions"] == ["occ-3"]
    assert audit["apply_to_same_value_actions"] == ["occ-1"]
    assert audit["risk_flags"] == ["same_value_scope_confirmed"]
    assert audit["report_only"] is True
    assert audit["export_blocking"] is False


def test_export_readiness_is_advisory_only():
    ready = build_replacement_audit(
        [
            build_replacement_decision(
                occurrence_id="occ-1",
                source_text="SYNTHETISCH-PERSOON-A",
                entity_type="PERSON",
                display_label="Naam",
                suggested_replacement="[PERSOON_1]",
                review_state="accepted",
            )
        ]
    )
    review = build_replacement_audit(
        [
            build_replacement_decision(
                occurrence_id="occ-1",
                source_text="SYNTHETISCH-PERSOON-A",
                entity_type="PERSON",
                display_label="Naam",
                suggested_replacement="[PERSOON_1]",
            )
        ]
    )
    unresolved = build_replacement_audit(
        [
            build_replacement_decision(
                occurrence_id="occ-1",
                source_text="SYNTHETISCH-PERSOON-A",
                entity_type="PERSON",
                display_label="Naam",
                suggested_replacement="[PERSOON_1]",
                review_state="unresolved",
            )
        ]
    )

    assert ready["export_readiness"] == "ready_for_export"
    assert review["export_readiness"] == "review_recommended"
    assert unresolved["export_readiness"] == "high_risk_unresolved"
    assert ready["export_blocking"] is False
    assert review["export_blocking"] is False
    assert unresolved["export_blocking"] is False


def test_helper_signature_does_not_require_streamlit_or_scrub_key_objects():
    decision = ReplacementDecision(
        occurrence_id="occ-1",
        source_text="SYNTHETISCH-PERSOON-A",
        entity_type="PERSON",
        display_label="Naam",
        suggested_replacement="[PERSOON_1]",
        review_state="accepted",
    )

    assert decision.as_dict()["replacement_value"] == "[PERSOON_1]"
    assert decision.as_dict()["creates_mapping"] is True
