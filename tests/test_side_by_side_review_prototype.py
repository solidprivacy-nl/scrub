from __future__ import annotations

from pathlib import Path

from side_by_side_review import (
    build_side_by_side_review_model,
    summarize_side_by_side_review_model,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER = REPO_ROOT / "side_by_side_review.py"


def _synthetic_rows() -> list[dict[str, object]]:
    return [
        {"include": True, "find": "SYNTHETIC_NAME_A", "replace_with": "[PERSON_1]"},
        {"include": True, "find": "SYNTHETIC_CASE_A", "replace_with": "[CASE_1]"},
        {"include": False, "find": "SYNTHETIC_IGNORE_A", "replace_with": "[IGNORE_1]"},
    ]


def test_side_by_side_model_places_source_left_and_processed_right():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source text",
        processed_text="SYNTHETIC processed text",
        review_rows=_synthetic_rows(),
    )

    assert model["layout"]["mode"] == "side_by_side"
    assert model["layout"]["source_position"] == "left"
    assert model["layout"]["processed_position"] == "right"
    assert model["source_pane"]["label"] == "Brontekst"
    assert model["processed_pane"]["label"] == "Verwerkte tekst"
    assert model["source_pane"]["editable"] is False


def test_highlights_are_integrated_in_processed_pane_only_when_enabled():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC [PERSON_1] source stays unmarked",
        processed_text="SYNTHETIC [PERSON_1] and [CASE_1] processed",
        review_rows=_synthetic_rows(),
        highlights_enabled=True,
    )

    assert model["source_pane"]["highlight_spans"] == []
    assert model["processed_pane"]["highlights_enabled"] is True
    assert model["processed_pane"]["highlight_scope"] == "processed_pane_only"
    assert model["processed_pane"]["highlight_terms"] == ["[PERSON_1]", "[CASE_1]"]
    assert model["processed_pane"]["highlight_spans"] == [(10, 20), (25, 33)]
    assert model["compact_legend"]["enabled_when_highlights_visible"] is True
    assert model["compact_legend"]["single_legend_only"] is True
    assert model["compact_legend"]["repeated_inline_gemarkeerd_labels"] is False


def test_highlights_disabled_keeps_terms_but_no_visual_spans():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC [PERSON_1] processed",
        review_rows=_synthetic_rows(),
        highlights_enabled=False,
    )

    assert model["processed_pane"]["highlight_terms"] == ["[PERSON_1]", "[CASE_1]"]
    assert model["processed_pane"]["highlight_spans"] == []
    assert model["highlight_toggle"]["enabled"] is False
    assert model["compact_legend"]["enabled_when_highlights_visible"] is False


def test_highlight_toggle_contract_is_visual_only_and_non_mutating():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC [PERSON_1] processed",
        review_rows=_synthetic_rows(),
        highlights_enabled=True,
    )
    toggle = model["highlight_toggle"]

    assert toggle["label"] == "Markeringen tonen"
    assert toggle["explicit_label"] == "Markeringen tonen in verwerkte tekst"
    assert toggle["visual_only"] is True
    assert toggle["only_visual_aid"] is True
    assert toggle["must_not_change_source_text"] is True
    assert toggle["must_not_change_review_table_state"] is True
    assert toggle["must_not_change_export_payloads"] is True
    assert toggle["must_not_change_scrub_key_state"] is True
    assert toggle["must_not_change_reinsert_behavior"] is True


def test_review_table_serial_review_and_replacement_relationships_are_safe():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC processed",
        review_rows=_synthetic_rows(),
        selected_occurrence_id="synthetic-occurrence-1",
    )

    assert model["review_table"]["source_of_truth"] is True
    assert model["review_table"]["fallback"] is True
    assert "De vervangtabel blijft leidend" in model["review_table"]["copy"]
    assert model["review_table"]["included_review_count"] == 2
    assert model["serial_review"]["relationship"] == "guided_layer"
    assert model["serial_review"]["not_table_replacement"] is True
    assert model["serial_review"]["selected_occurrence_id"] == "synthetic-occurrence-1"
    assert model["replacement_review"]["relationship"] == "task_oriented_future_layer"
    assert model["replacement_review"]["allowed_first_actions"] == [
        "Vervangen",
        "Zichtbaar houden",
        "Aanpassen",
        "Later controleren",
    ]
    assert model["replacement_review"]["helper_internals_visible"] is False
    assert "all_normalized" in model["replacement_review"]["blocked_user_facing_internals"]


def test_scroll_sync_is_desired_but_not_implemented_by_helper():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC processed",
    )

    assert model["scroll_sync"]["desired_later"] is True
    assert model["scroll_sync"]["implemented"] is False
    assert model["scroll_sync"]["requires_separate_package"] is True
    assert model["scroll_sync"]["requires_separate_tests"] is True
    assert model["scroll_sync"]["custom_component_required_here"] is False


def test_boundary_flags_block_product_state_changes():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC processed",
    )
    boundaries = model["boundaries"]

    assert boundaries["report_only"] is True
    assert boundaries["mutation_allowed"] is False
    assert boundaries["review_table_mutation"] is False
    assert boundaries["replacement_mutation"] is False
    assert boundaries["automatic_replacement"] is False
    assert boundaries["scrub_key_writes"] is False
    assert boundaries["scrub_key_schema_change"] is False
    assert boundaries["export_blocking"] is False
    assert boundaries["export_download_behavior_change"] is False
    assert boundaries["reinsert_behavior_change"] is False
    assert boundaries["click_to_mark"] is False
    assert boundaries["advanced_editor"] is False
    assert boundaries["full_document_marking"] is False
    assert boundaries["synchronized_scroll_implementation"] is False
    assert boundaries["custom_html_component_implementation"] is False
    assert boundaries["cloud_processing"] is False
    assert boundaries["real_data"] is False


def test_summary_exposes_only_compact_audit_fields():
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text="SYNTHETIC [PERSON_1] processed",
        review_rows=_synthetic_rows(),
        highlights_enabled=True,
    )
    summary = summarize_side_by_side_review_model(model)

    assert summary == {
        "model_type": "side_by_side_review_prototype_helper",
        "source_position": "left",
        "processed_position": "right",
        "highlights_enabled": True,
        "highlight_count": 1,
        "review_table_source_of_truth": True,
        "review_table_fallback": True,
        "synchronized_scroll_implemented": False,
        "mutation_allowed": False,
        "scrub_key_writes": False,
        "export_download_behavior_change": False,
        "reinsert_behavior_change": False,
    }


def test_helper_source_does_not_import_streamlit_or_call_blocked_flows():
    helper_text = HELPER.read_text(encoding="utf-8")
    lowered = helper_text.lower()

    assert "import streamlit" not in lowered
    assert "st." not in helper_text
    assert "download_button" not in lowered
    assert "scrub_key_to_json" not in lowered
    assert "reinsert_from_scrub_key" not in lowered
    assert "reinsert_docx_bytes" not in lowered
    assert "reinsert_txt_bytes" not in lowered
    assert "apply_replacements_to_text" not in lowered
    assert "unsafe_allow_html" not in lowered


def test_tests_use_synthetic_values_only():
    rendered = Path(__file__).read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
        "Fatima " + "El " + "Amrani",
        "Peter " + "Bakker",
    ]

    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
