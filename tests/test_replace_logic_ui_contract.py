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
THIS_TEST = Path(__file__)

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

ALLOWED_VIEW_ONLY_SESSION_KEYS = {
    "replacement_decision_selected_occurrence_id",
    "replacement_decision_preview_state",
    "replacement_decision_preview_scope",
    "replacement_decision_preview_text",
    "replacement_decision_panel_expanded",
}

FORBIDDEN_MUTATION_TARGETS = {
    "replacement_editor",
    "edited_replacements_df",
    "review table rows",
    "export state",
    "scrub key state",
    "reinsert state",
}


def _ui_plan_text() -> str:
    return UI_PLAN.read_text(encoding="utf-8")


def _contract_text() -> str:
    return _ui_plan_text().replace("`", "").lower()


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
    text = _contract_text()

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
        "serial_review_panel_ui.py",
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


def test_staged_vs_applied_state_contract_is_explicit_and_non_mutating():
    text = _contract_text()

    for required in [
        "staged decision preview only",
        "staged decision state is not applied state",
        "existing review table remains source of truth and fallback",
        "no review table mutation",
        "no replacement mutation",
        "no automatic replacement",
        "not write those decisions back",
        "separate package with explicit coordinator approval",
    ]:
        assert required in text


def test_session_state_contract_allows_only_view_only_keys_and_blocks_mutation_targets():
    text = _ui_plan_text()
    contract = _contract_text()

    assert "Allowed view-only session keys" in text
    assert "temporary UI selection and preview state" in text
    assert "must not be treated as applied replacement state" in text

    for key in ALLOWED_VIEW_ONLY_SESSION_KEYS:
        assert key in text
    for target in FORBIDDEN_MUTATION_TARGETS:
        assert f"no mutation of {target}" in contract


def test_scrub_key_mapping_indicators_are_advisory_only():
    text = _contract_text()
    decisions = [
        build_replacement_decision(
            occurrence_id="mapping-1",
            source_text="SYNTHETIC-A",
            entity_type="SYNTHETIC_ENTITY",
            display_label="Vervangen",
            suggested_replacement="[SYNTHETIC_A]",
            review_state="accepted",
        )
    ]
    audit = build_replacement_audit(decisions)

    assert decisions[0].creates_mapping is True
    assert audit["mapping_candidates"] == ["mapping-1"]
    assert "creates_mapping is advisory only" in text
    assert "does not authorize a scrub key write" in text
    assert "mapping_candidates are advisory only" in text
    assert "do not authorize scrub key persistence" in text
    assert "writing mappings directly from a new ui panel" in text
    assert "scrub key schema" in text


def test_export_download_and_reinsert_boundaries_are_explicit():
    text = _contract_text()

    for required in [
        "export_readiness is advisory only",
        "must not call export/download functions",
        "change export eligibility",
        "disable export buttons",
        "alter download payloads",
        "no export/download calls",
        "no reinsert behavior change",
        "no scrub key writes",
    ]:
        assert required in text


def test_no_fuzzy_matching_no_guessed_intent_and_no_automatic_replacement_contract():
    text = _contract_text()

    assert "no fuzzy matching or guessed intent is allowed" in text
    assert "no automatic replacement" in text
    assert "auto-repairing duplicate placeholders" in text


def test_all_normalized_not_available_as_first_mutating_scope_without_approval():
    text = _contract_text()

    assert "all_normalized" in text
    assert "not available as a first mutating ui scope without separate explicit coordinator approval" in text
    assert "disabled/advisory only" in text


def test_future_ui_requires_separate_explicit_coordinator_approval():
    text = _contract_text()

    assert "only after separate explicit coordinator approval" in text
    assert "do not start implementation automatically" in text
    assert "small staged/read-only companion panel" in text


def test_contract_tests_use_synthetic_values_only():
    rendered = THIS_TEST.read_text(encoding="utf-8") + _ui_plan_text()
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
