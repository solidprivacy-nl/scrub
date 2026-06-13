from __future__ import annotations

from pathlib import Path

from review_panel_view_model import build_review_panel_view_model


REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER = REPO_ROOT / "review_panel_view_model.py"
THIS_TEST = Path(__file__)

SYNTHETIC_TEXT = (
    "Start [SYNTHETIC_A] midden [SYNTHETIC_B] einde "
    "[SYNTHETIC_DUP] en later [SYNTHETIC_DUP]."
)


def _row(
    occurrence_id: str,
    source_text: str,
    *,
    review_state: str = "needs_review",
    risk_flags: tuple[str, ...] = (),
    include_offsets: bool = True,
    context_preview: str = "SYNTHETIC context preview only.",
) -> dict[str, object]:
    row: dict[str, object] = {
        "occurrence_id": occurrence_id,
        "source_text": source_text,
        "entity_type": "SYNTHETIC_ENTITY",
        "suggested_replacement": "[SYNTHETIC_REPLACEMENT]",
        "review_state": review_state,
        "confidence": 0.91,
        "context_preview": context_preview,
        "risk_flags": risk_flags,
        "source": "synthetic_test",
    }
    if include_offsets:
        start = SYNTHETIC_TEXT.index(source_text)
        row["start_offset"] = start
        row["end_offset"] = start + len(source_text)
    return row


def test_empty_rows_build_empty_report_only_panel_without_crash():
    panel = build_review_panel_view_model(displayed_text=SYNTHETIC_TEXT, review_rows=[])

    assert panel["panel_type"] == "review_panel_view_model"
    assert panel["queue"]["total_items"] == 0
    assert panel["current_item"] is None
    assert panel["current_context_card"] is None
    assert panel["next_item"] is None
    assert panel["previous_item"] is None
    assert panel["unresolved_count"] == 0
    assert panel["high_risk_count"] == 0
    assert panel["duplicate_exact_value_count"] == 0
    assert panel["same_value_occurrence_ids"] == []
    assert "no_current_item" in panel["warnings"]
    assert panel["report_only"] is True
    assert panel["mutation_allowed"] is False
    assert panel["table_first_baseline"] is True


def test_valid_current_item_has_valid_context_card_from_exact_offsets():
    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=[_row("syn-a", "[SYNTHETIC_A]")],
        context_window=7,
    )

    assert panel["current_item"]["occurrence_id"] == "syn-a"
    card = panel["current_context_card"]
    assert card["card_type"] == "context_card"
    assert card["occurrence_id"] == "syn-a"
    assert card["match_text"] == "[SYNTHETIC_A]"
    assert card["offset_valid"] is True
    assert card["prefix_text"].endswith("Start ")
    assert card["suffix_text"].startswith(" midden")
    assert card["report_only"] is True
    assert card["mutation_allowed"] is False
    assert panel["warnings"] == []


def test_current_occurrence_id_selection_controls_current_item_and_card():
    rows = [
        _row("syn-a", "[SYNTHETIC_A]"),
        _row("syn-b", "[SYNTHETIC_B]", review_state="unresolved"),
    ]

    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=rows,
        current_occurrence_id="syn-b",
    )

    assert panel["current_item"]["occurrence_id"] == "syn-b"
    assert panel["current_context_card"]["match_text"] == "[SYNTHETIC_B]"


def test_next_and_previous_items_are_propagated_from_serial_queue():
    rows = [
        _row("syn-a", "[SYNTHETIC_A]", review_state="needs_review"),
        _row("syn-b", "[SYNTHETIC_B]", review_state="accepted"),
        _row("syn-c", "[SYNTHETIC_DUP]", review_state="unresolved"),
    ]

    first = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=rows,
        current_occurrence_id="syn-a",
    )
    last = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=rows,
        current_occurrence_id="syn-c",
    )

    assert first["next_item"]["occurrence_id"] == "syn-c"
    assert first["previous_item"] is None
    assert last["previous_item"]["occurrence_id"] == "syn-a"
    assert last["next_item"] is None


def test_unresolved_and_high_risk_counts_are_propagated():
    rows = [
        _row("syn-a", "[SYNTHETIC_A]", review_state="accepted"),
        _row("syn-b", "[SYNTHETIC_B]", review_state="needs_review", risk_flags=("synthetic_high_risk",)),
        _row("syn-c", "[SYNTHETIC_DUP]", review_state="high_risk_unresolved"),
    ]

    panel = build_review_panel_view_model(displayed_text=SYNTHETIC_TEXT, review_rows=rows)

    assert panel["unresolved_count"] == 2
    assert panel["high_risk_count"] == 2
    assert panel["audit_summary"]["review_readiness"] == "high_risk_unresolved"


def test_duplicate_exact_value_metadata_is_propagated_without_fuzzy_matching():
    rows = [
        _row("syn-1", "[SYNTHETIC_DUP]"),
        _row("syn-2", "[synthetic_dup]", include_offsets=False),
        _row("syn-3", "[SYNTHETIC_DUP]", include_offsets=False),
    ]

    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=rows,
        current_occurrence_id="syn-1",
    )

    assert panel["duplicate_exact_value_count"] == 2
    assert panel["same_value_occurrence_ids"] == ["syn-1", "syn-3"]
    assert panel["fuzzy_matching"] is False
    assert panel["guessed_intent"] is False


def test_missing_offsets_degrade_to_escaped_context_preview_fallback():
    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=[
            _row(
                "syn-a",
                "[SYNTHETIC_A]",
                include_offsets=False,
                context_preview="SYNTHETIC <b>preview</b> only.",
            )
        ],
    )

    card = panel["current_context_card"]
    assert card["card_type"] == "context_preview_fallback"
    assert card["offset_valid"] is False
    assert card["escaped_context_preview"] == "SYNTHETIC &lt;b&gt;preview&lt;/b&gt; only."
    assert card["raw_html_allowed"] is False
    assert "missing_offsets_context_preview_fallback" in panel["warnings"]


def test_invalid_offsets_degrade_to_invalid_context_card_with_warnings():
    row = _row("syn-a", "[SYNTHETIC_A]")
    row["start_offset"] = -1
    row["end_offset"] = 9999

    panel = build_review_panel_view_model(displayed_text=SYNTHETIC_TEXT, review_rows=[row])

    card = panel["current_context_card"]
    assert card["card_type"] == "context_card"
    assert card["offset_valid"] is False
    assert "invalid offset range" in card["validation_errors"]
    assert "end_offset outside displayed_text" in card["validation_errors"]
    assert any(warning.startswith("context_card_invalid:") for warning in panel["warnings"])


def test_html_escaping_is_inherited_from_context_cards_helper():
    text = "Waarde <script> blijft synthetisch."
    start = text.index("<script>")
    panel = build_review_panel_view_model(
        displayed_text=text,
        review_rows=[
            {
                "occurrence_id": "html",
                "source_text": "<script>",
                "entity_type": "SYNTHETIC_HTML",
                "suggested_replacement": "<SAFE_PLACEHOLDER>",
                "review_state": "needs_review",
                "confidence": 0.9,
                "context_preview": "Synthetic HTML context.",
                "risk_flags": ["html_escape_check"],
                "start_offset": start,
                "end_offset": start + len("<script>"),
            }
        ],
    )

    card = panel["current_context_card"]
    assert card["match_text"] == "<script>"
    assert card["escaped_match"] == "&lt;script&gt;"
    assert card["replacement_preview"] == "<SAFE_PLACEHOLDER>"
    assert card["escaped_replacement_preview"] == "&lt;SAFE_PLACEHOLDER&gt;"


def test_report_only_mutation_export_scrub_key_reinsert_boundaries_are_locked():
    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=[_row("syn-a", "[SYNTHETIC_A]")],
    )

    assert panel["report_only"] is True
    assert panel["mutation_allowed"] is False
    assert panel["export_blocking"] is False
    assert panel["scrub_key_changes"] is False
    assert panel["scrub_key_mapping_written"] is False
    assert panel["reinsert_changes"] is False
    assert panel["review_table_mutation"] is False
    assert panel["replacement_mutation"] is False
    assert panel["automatic_replacement"] is False
    assert panel["cloud_processing"] is False
    assert panel["table_first_baseline"] is True


def test_no_fuzzy_matching_no_guessed_intent_and_no_automatic_replacement():
    panel = build_review_panel_view_model(
        displayed_text=SYNTHETIC_TEXT,
        review_rows=[_row("syn-a", "[SYNTHETIC_A]")],
    )

    assert panel["fuzzy_matching"] is False
    assert panel["guessed_intent"] is False
    assert panel["automatic_replacement"] is False


def test_synthetic_only_values_are_used_in_helper_and_tests():
    rendered = HELPER.read_text(encoding="utf-8") + THIS_TEST.read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
