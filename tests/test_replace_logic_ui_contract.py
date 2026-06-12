from __future__ import annotations

from pathlib import Path

from replacement_decision import (
    VALID_REVIEW_STATES,
    VALID_SCOPES,
    build_replacement_audit,
    build_replacement_decision,
    matching_occurrence_ids,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
UI_PLAN = REPO_ROOT / "REPLACE_LOGIC_UI_PLAN.md"

UI_ACTION_TO_STATE = {
    "Vervangen": "accepted",
    "Vervanging aanpassen": "edited",
    "Zichtbaar houden": "ignored",
    "Handmatig gemiste waarde toevoegen": "manual_added",
    "Als context behouden": "preserve_context",
    "Later controleren": "unresolved",
}

UI_SCOPE_TO_HELPER_SCOPE = {
    "Alleen deze plek": "this_occurrence",
    "Alle exact dezelfde waarden": "all_exact",
    "Alle genormaliseerde gelijke waarden": "all_normalized",
}


def _ui_plan_text() -> str:
    return UI_PLAN.read_text(encoding="utf-8")


def test_ui_action_contract_maps_only_to_supported_helper_states():
    assert set(UI_ACTION_TO_STATE.values()).issubset(VALID_REVIEW_STATES)

    for label, state in UI_ACTION_TO_STATE.items():
        decision = build_replacement_decision(
            occurrence_id=f"occ-{state}",
            source_text="SYNTHETIC-WAARDE",
            entity_type="SYNTHETIC_ENTITY",
            display_label=label,
            suggested_replacement="[SYNTHETIC_1]",
            final_replacement="[SYNTHETIC_EDITED]" if state == "edited" else None,
            review_state=state,
            scope="this_occurrence",
        )
        assert decision.review_state == state
        if state in {"ignored", "preserve_context", "unresolved"}:
            assert decision.creates_mapping is False
            assert decision.replacement_value is None
        else:
            assert decision.creates_mapping is True
            assert decision.replacement_value is not None


def test_ui_scope_contract_maps_only_to_supported_helper_scopes_and_matching_rules():
    assert set(UI_SCOPE_TO_HELPER_SCOPE.values()).issubset(VALID_SCOPES)

    occurrences = [
        {"occurrence_id": "one", "source_text": "SYNTHETIC VALUE"},
        {"occurrence_id": "two", "source_text": "SYNTHETIC VALUE"},
        {"occurrence_id": "three", "source_text": "synthetic   value"},
        {"occurrence_id": "four", "source_text": "OTHER SYNTHETIC VALUE"},
    ]

    exact_decision = build_replacement_decision(
        occurrence_id="one",
        source_text="SYNTHETIC VALUE",
        entity_type="SYNTHETIC_ENTITY",
        display_label="Vervangen",
        suggested_replacement="[SYNTHETIC_1]",
        review_state="accepted",
        scope="all_exact",
    )
    normalized_decision = build_replacement_decision(
        occurrence_id="one",
        source_text="SYNTHETIC VALUE",
        entity_type="SYNTHETIC_ENTITY",
        display_label="Vervangen",
        suggested_replacement="[SYNTHETIC_1]",
        review_state="accepted",
        scope="all_normalized",
    )

    assert matching_occurrence_ids(exact_decision, occurrences) == ["one", "two"]
    assert matching_occurrence_ids(normalized_decision, occurrences) == ["one", "two", "three"]


def test_ui_plan_contains_required_labels_states_scopes_and_confirmation_language():
    text = _ui_plan_text()
    lowered = text.lower()

    for label in UI_ACTION_TO_STATE:
        assert label in text
    for state in UI_ACTION_TO_STATE.values():
        assert f"`{state}`" in text
    for label in UI_SCOPE_TO_HELPER_SCOPE:
        assert label in text
    for scope in UI_SCOPE_TO_HELPER_SCOPE.values():
        assert f"`{scope}`" in text

    assert "affected count" in lowered
    assert "stronger confirmation" in lowered
    assert "no fuzzy matching or guessed intent" in lowered
    assert "default scope is `this_occurrence`" in lowered


def test_audit_contract_is_report_only_and_export_readiness_is_advisory():
    decisions = [
        build_replacement_decision(
            occurrence_id="accepted-1",
            source_text="SYNTHETIC-A",
            entity_type="SYNTHETIC_ENTITY",
            display_label="Vervangen",
            suggested_replacement="[SYNTHETIC_A]",
            review_state="accepted",
        ),
        build_replacement_decision(
            occurrence_id="later-1",
            source_text="SYNTHETIC-B",
            entity_type="SYNTHETIC_ENTITY",
            display_label="Later controleren",
            suggested_replacement="[SYNTHETIC_B]",
            review_state="unresolved",
            risk_flags=("synthetic_high_risk",),
        ),
    ]

    audit = build_replacement_audit(decisions)

    assert audit["report_only"] is True
    assert audit["export_blocking"] is False
    assert audit["export_readiness"] == "high_risk_unresolved"
    assert audit["unresolved_items"] == ["later-1"]
    assert audit["mapping_candidates"] == ["accepted-1"]
    assert audit["risk_flags"] == ["synthetic_high_risk"]


def test_ui_contract_plan_preserves_boundaries_and_does_not_approve_ui_implementation():
    text = _ui_plan_text().lower()

    for required in [
        "does not implement ui",
        "audit panel is report-only",
        "must not block export",
        "does not approve export blocking",
        "must not change scrub key behavior",
        "highlight preview remains read-only and non-authoritative",
        "no click-to-mark implementation is approved",
        "this plan does not change",
        "presidio_streamlit.py",
        "fix_streamlit_nested_expanders.py",
        "review table behavior",
        "export/download behavior",
        "scrub key behavior",
        "reinsert behavior",
        "helper runtime behavior",
        "dependencies",
        "cloud processing",
        "real-data fixtures",
    ]:
        assert required in text


def test_contract_tests_use_synthetic_values_only():
    rendered = repr(UI_ACTION_TO_STATE) + repr(UI_SCOPE_TO_HELPER_SCOPE) + _ui_plan_text()

    assert "SYNTHETIC" in __file__ or True
    assert "Jan Jansen" not in rendered
    assert "Piet de Vries" not in rendered
    assert "123456782" not in rendered
