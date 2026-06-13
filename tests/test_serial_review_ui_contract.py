from __future__ import annotations

from pathlib import Path

from replacement_decision import VALID_REVIEW_STATES, VALID_SCOPES, build_replacement_decision, matching_occurrence_ids
from serial_review import VALID_SERIAL_REVIEW_STATES, build_serial_review_queue


REPO_ROOT = Path(__file__).resolve().parents[1]
UI_PLAN = REPO_ROOT / "SERIAL_REVIEW_UI_PLAN.md"
THIS_TEST = Path(__file__)

REQUIRED_QUEUE_FIELDS = {
    "current_item",
    "previous_item",
    "next_item",
    "unresolved_count",
    "high_risk_count",
    "duplicate_exact_value_count",
    "same_value_occurrence_ids",
    "report_only",
    "mutation_allowed",
}

REQUIRED_ITEM_FIELDS = {
    "context_preview",
    "suggested_replacement",
    "review_state",
    "risk_flags",
    "report_only",
    "mutation_allowed",
}

UI_NAVIGATION_LABELS = {
    "Vorige",
    "Volgende",
    "Volgende onopgeloste",
}

UI_ACTION_TO_STATE = {
    "Later controleren": "unresolved",
    "Vervangen": "accepted",
    "Vervanging aanpassen": "edited",
    "Zichtbaar houden": "ignored",
    "Als context behouden": "preserve_context",
}

UI_SCOPE_TO_HELPER_SCOPE = {
    "Alleen deze plek": "this_occurrence",
    "Alle exact dezelfde waarden": "all_exact",
}


def _ui_plan_text() -> str:
    return UI_PLAN.read_text(encoding="utf-8")


def _row(
    occurrence_id: str,
    source_text: str,
    *,
    review_state: str = "needs_review",
    risk_flags: tuple[str, ...] = (),
) -> dict[str, object]:
    return {
        "occurrence_id": occurrence_id,
        "source_text": source_text,
        "entity_type": "SYNTHETIC_ENTITY",
        "suggested_replacement": "[SYNTHETIC_REPLACEMENT]",
        "review_state": review_state,
        "confidence": 0.88,
        "context_preview": "SYNTHETIC context preview only.",
        "risk_flags": risk_flags,
    }


def test_serial_review_ui_plan_exists_and_names_helpers():
    assert UI_PLAN.exists()
    text = _ui_plan_text()

    assert "serial_review.py" in text
    assert "replacement_decision.py" in text
    assert "context_cards.py" in text
    assert "does not implement UI" in text


def test_plan_lists_current_helper_output_fields_and_queue_exposes_them():
    text = _ui_plan_text()
    rows = [
        _row("syn-1", "SYNTHETIC-DUP", risk_flags=("synthetic_high_risk",)),
        _row("syn-2", "SYNTHETIC-OTHER", review_state="accepted"),
        _row("syn-3", "SYNTHETIC-DUP", review_state="unresolved"),
    ]
    queue = build_serial_review_queue(rows, current_occurrence_id="syn-1")

    for field in REQUIRED_QUEUE_FIELDS:
        assert field in text
        assert field in queue

    for field in REQUIRED_ITEM_FIELDS:
        assert field in text
        assert field in queue["current_item"]

    assert queue["current_item"]["context_preview"] == "SYNTHETIC context preview only."
    assert queue["current_item"]["suggested_replacement"] == "[SYNTHETIC_REPLACEMENT]"
    assert queue["current_item"]["risk_flags"] == ["synthetic_high_risk"]
    assert queue["same_value_occurrence_ids"] == ["syn-1", "syn-3"]
    assert queue["duplicate_exact_value_count"] == 2
    assert queue["report_only"] is True
    assert queue["mutation_allowed"] is False


def test_plan_contains_required_ui_labels():
    text = _ui_plan_text()

    for label in UI_NAVIGATION_LABELS:
        assert label in text
    for label in UI_ACTION_TO_STATE:
        assert label in text
    for label in UI_SCOPE_TO_HELPER_SCOPE:
        assert label in text


def test_review_action_states_align_with_replacement_and_serial_helpers():
    assert set(UI_ACTION_TO_STATE.values()).issubset(VALID_REVIEW_STATES)
    assert set(UI_ACTION_TO_STATE.values()).issubset(VALID_SERIAL_REVIEW_STATES)

    for label, state in UI_ACTION_TO_STATE.items():
        decision = build_replacement_decision(
            occurrence_id=f"syn-{state}",
            source_text="SYNTHETIC-VALUE",
            entity_type="SYNTHETIC_ENTITY",
            display_label=label,
            suggested_replacement="[SYNTHETIC_REPLACEMENT]",
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

    assert "high_risk_unresolved" in VALID_SERIAL_REVIEW_STATES
    assert "manual_added" in VALID_SERIAL_REVIEW_STATES


def test_scope_labels_align_with_replacement_helper_and_exact_matching_only():
    assert set(UI_SCOPE_TO_HELPER_SCOPE.values()).issubset(VALID_SCOPES)

    occurrences = [
        {"occurrence_id": "syn-1", "source_text": "SYNTHETIC VALUE"},
        {"occurrence_id": "syn-2", "source_text": "SYNTHETIC VALUE"},
        {"occurrence_id": "syn-3", "source_text": "synthetic value"},
    ]
    exact_decision = build_replacement_decision(
        occurrence_id="syn-1",
        source_text="SYNTHETIC VALUE",
        entity_type="SYNTHETIC_ENTITY",
        display_label="Alle exact dezelfde waarden",
        suggested_replacement="[SYNTHETIC_REPLACEMENT]",
        review_state="accepted",
        scope="all_exact",
    )

    assert matching_occurrence_ids(exact_decision, occurrences) == ["syn-1", "syn-2"]
    assert "all_normalized" in VALID_SCOPES
    assert "all_normalized" in _ui_plan_text()
    assert "not part of the first serial review panel contract" in _ui_plan_text()


def test_plan_preserves_table_first_non_destructive_report_only_boundaries():
    text = _ui_plan_text().lower()

    for required in [
        "table-first baseline",
        "non-destructive",
        "report-only until approved",
        "review table remains the authoritative control/audit surface",
        "must not hide or replace the existing review table",
    ]:
        assert required in text


def test_plan_forbids_export_scrub_key_reinsert_startup_and_editor_scope():
    text = _ui_plan_text().lower()

    for forbidden_boundary in [
        "no export blocking",
        "must not block export",
        "no scrub key mutation",
        "must not write scrub key mappings",
        "no reinsert behavior change",
        "no startup source mutation",
        "no click-to-mark",
        "no advanced editor",
        "presidio_streamlit.py",
        "fix_streamlit_nested_expanders.py",
    ]:
        assert forbidden_boundary in text


def test_plan_uses_synthetic_only_boundary_and_contract_tests_do_not_contain_real_data_examples():
    rendered = THIS_TEST.read_text(encoding="utf-8") + _ui_plan_text()
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "synthetic-only boundary" in rendered.lower()
    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
