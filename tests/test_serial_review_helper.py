from __future__ import annotations

from pathlib import Path

from serial_review import (
    build_serial_review_audit,
    build_serial_review_item,
    build_serial_review_items,
    build_serial_review_queue,
    matching_exact_source_occurrence_ids,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER = REPO_ROOT / "serial_review.py"
THIS_TEST = Path(__file__)


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
        "confidence": 0.91,
        "context_preview": "Synthetic context only.",
        "risk_flags": risk_flags,
    }


def test_empty_queue_is_report_only_and_non_mutating():
    queue = build_serial_review_queue([])

    assert queue["total_items"] == 0
    assert queue["current_index"] is None
    assert queue["current_item"] is None
    assert queue["next_item"] is None
    assert queue["previous_item"] is None
    assert queue["unresolved_count"] == 0
    assert queue["high_risk_count"] == 0
    assert queue["duplicate_exact_value_count"] == 0
    assert queue["same_value_occurrence_ids"] == []
    assert queue["report_only"] is True
    assert queue["mutation_allowed"] is False


def test_single_item_queue_exposes_current_item_and_same_value_count():
    queue = build_serial_review_queue([_row("syn-1", "SYNTHETIC-ONE")])

    assert queue["total_items"] == 1
    assert queue["current_index"] == 0
    assert queue["current_item"]["occurrence_id"] == "syn-1"
    assert queue["next_item"] is None
    assert queue["previous_item"] is None
    assert queue["duplicate_exact_value_count"] == 1
    assert queue["same_value_occurrence_ids"] == ["syn-1"]


def test_next_and_previous_navigation_targets_unresolved_items_without_wraparound():
    rows = [
        _row("syn-1", "SYNTHETIC-A", review_state="needs_review"),
        _row("syn-2", "SYNTHETIC-B", review_state="accepted"),
        _row("syn-3", "SYNTHETIC-C", review_state="unresolved"),
    ]

    first = build_serial_review_queue(rows, current_occurrence_id="syn-1")
    last = build_serial_review_queue(rows, current_occurrence_id="syn-3")

    assert first["current_item"]["occurrence_id"] == "syn-1"
    assert first["next_item"]["occurrence_id"] == "syn-3"
    assert first["previous_item"] is None
    assert last["current_item"]["occurrence_id"] == "syn-3"
    assert last["previous_item"]["occurrence_id"] == "syn-1"
    assert last["next_item"] is None


def test_unresolved_filter_keeps_needs_review_and_unresolved_only():
    rows = [
        _row("syn-1", "SYNTHETIC-A", review_state="accepted"),
        _row("syn-2", "SYNTHETIC-B", review_state="needs_review"),
        _row("syn-3", "SYNTHETIC-C", review_state="unresolved"),
        _row("syn-4", "SYNTHETIC-D", review_state="ignored"),
    ]

    queue = build_serial_review_queue(rows, filter_mode="unresolved")

    assert queue["total_items"] == 2
    assert [item["occurrence_id"] for item in queue["items"]] == ["syn-2", "syn-3"]
    assert queue["unresolved_count"] == 2


def test_high_risk_filters_surface_risk_flags_and_high_risk_unresolved_state():
    rows = [
        _row("syn-1", "SYNTHETIC-A", review_state="accepted"),
        _row("syn-2", "SYNTHETIC-B", review_state="needs_review", risk_flags=("synthetic_high_risk",)),
        _row("syn-3", "SYNTHETIC-C", review_state="high_risk_unresolved"),
        _row("syn-4", "SYNTHETIC-D", review_state="unresolved"),
    ]

    high_risk = build_serial_review_queue(rows, filter_mode="high_risk")
    high_risk_unresolved = build_serial_review_queue(rows, filter_mode="high_risk_unresolved")

    assert high_risk["high_risk_count"] == 2
    assert [item["occurrence_id"] for item in high_risk["items"]] == ["syn-2", "syn-3"]
    assert [item["occurrence_id"] for item in high_risk_unresolved["items"]] == ["syn-2", "syn-3"]
    assert high_risk_unresolved["audit_summary"]["review_readiness"] == "high_risk_unresolved"


def test_duplicate_exact_source_text_count_is_for_current_item():
    rows = [
        _row("syn-1", "SYNTHETIC-DUP"),
        _row("syn-2", "synthetic-dup"),
        _row("syn-3", "SYNTHETIC-DUP"),
        _row("syn-4", "SYNTHETIC-OTHER"),
    ]

    queue = build_serial_review_queue(rows, current_occurrence_id="syn-1")

    assert queue["duplicate_exact_value_count"] == 2
    assert queue["same_value_occurrence_ids"] == ["syn-1", "syn-3"]


def test_all_exact_occurrence_matching_returns_only_exact_source_text_ids():
    rows = [
        _row("syn-1", "SYNTHETIC VALUE"),
        _row("syn-2", "SYNTHETIC VALUE"),
        _row("syn-3", "synthetic value"),
        _row("syn-4", "SYNTHETIC  VALUE"),
    ]
    items = build_serial_review_items(rows)

    assert matching_exact_source_occurrence_ids(items[0], items) == ["syn-1", "syn-2"]


def test_no_fuzzy_matching_or_guessed_intent_is_used_for_same_value_matching():
    current = build_serial_review_item(_row("syn-1", "SYNTHETIC VALUE"))
    rows = [
        _row("syn-1", "SYNTHETIC VALUE"),
        _row("syn-2", "synthetic value"),
        _row("syn-3", "SYNTHETIC  VALUE"),
        _row("syn-4", "SYNTHETIC-VALUE"),
    ]

    assert matching_exact_source_occurrence_ids(current, rows) == ["syn-1"]


def test_audit_summary_is_report_only_and_does_not_allow_mutation():
    audit = build_serial_review_audit(
        [
            _row("syn-1", "SYNTHETIC-A", review_state="accepted"),
            _row("syn-2", "SYNTHETIC-B", review_state="unresolved"),
        ]
    )

    assert audit["report_only"] is True
    assert audit["mutation_allowed"] is False
    assert audit["export_blocking"] is False
    assert audit["scrub_key_mapping_written"] is False
    assert audit["review_readiness"] == "review_recommended"


def test_contract_tests_use_synthetic_values_only():
    rendered = HELPER.read_text(encoding="utf-8") + THIS_TEST.read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
