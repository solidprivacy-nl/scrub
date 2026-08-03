from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "presidio_streamlit.py"
SIDE_PANEL = ROOT / "side_by_side_review_panel_ui.py"
COMPONENT = ROOT / "processed_text_selection_component.py"
INTEGRATION = ROOT / "processed_text_selection_integration.py"


def test_main_app_imports_server_authoritative_selection_adapter():
    source = APP.read_text(encoding="utf-8")
    for name in (
        "handle_selection_component_event",
        "selection_inspection_result",
        "selection_scroll_restore",
        "selection_feedback",
        "latest_selection_action",
        "undo_latest_selection_action",
    ):
        assert name in source
    assert "from processed_text_selection_integration import (" in source


def test_component_render_receives_document_scope_inspection_and_scroll_restore():
    source = APP.read_text(encoding="utf-8")
    render_call = source.index("side_by_side_state = render_side_by_side_review_panel(")
    render_end = source.index(")\n", render_call)
    fragment = source[render_call : render_end + 2]
    assert "document_scope_key=document_scope_key" in fragment
    assert "inspection_result=selection_inspection" in fragment
    assert "restore_source_scroll_ratio=restore_source_scroll" in fragment
    assert "restore_processed_scroll_ratio=restore_processed_scroll" in fragment


def test_events_are_processed_after_editable_table_and_before_serial_review_and_exports():
    source = APP.read_text(encoding="utf-8")
    editor_index = source.index("edited_replacements_df = st.data_editor(")
    save_index = source.index("save_remembered_replacements(edited_replacements_df)")
    handler_index = source.index("selection_outcome = handle_selection_component_event(")
    serial_index = source.index("serial_review_state = render_serial_review_panel(")
    first_download_index = source.index("st.download_button", handler_index)

    assert editor_index < save_index < handler_index < serial_index < first_download_index
    handler_fragment = source[handler_index:serial_index]
    assert "existing_rows=edited_replacements_df" in handler_fragment
    assert 'processed_text=side_by_side_state["processed_text"]' in handler_fragment
    assert '"protected_highlight_spans"' in handler_fragment
    assert "if selection_outcome.rerun_required:" in handler_fragment
    assert "st.rerun()" in handler_fragment


def test_undo_runs_against_current_visible_review_rows_before_component_event():
    source = APP.read_text(encoding="utf-8")
    undo_index = source.index("undo_outcome = undo_latest_selection_action(")
    event_index = source.index("selection_outcome = handle_selection_component_event(")
    fragment = source[undo_index:event_index]
    assert undo_index < event_index
    assert "current_review_rows=edited_replacements_df" in fragment
    assert "if undo_outcome.rerun_required:" in fragment
    assert "st.rerun()" in fragment


def test_existing_manual_form_and_authoritative_review_table_remain_present():
    source = APP.read_text(encoding="utf-8")
    assert "Gemiste waarde toevoegen" in source
    assert "build_manual_mask_row(" in source
    assert "edited_replacements_df = st.data_editor(" in source
    assert "save_remembered_replacements(edited_replacements_df)" in source


def test_side_panel_has_interactive_default_and_environment_rollback():
    source = SIDE_PANEL.read_text(encoding="utf-8")
    assert 'INTERACTIVE_COMPONENT_ENV = "PROCESSED_TEXT_SELECTION_COMPONENT_ENABLED"' in source
    assert 'os.environ.get(INTERACTIVE_COMPONENT_ENV, "true")' in source
    assert "render_processed_text_selection_component(" in source
    assert "except Exception as exc:" in source
    assert "_render_static_fallback(" in source
    assert '"static_fallback_available": True' in source
    assert '"component_environment_switch": INTERACTIVE_COMPONENT_ENV' in source


def test_server_protected_spans_exist_even_when_visual_markers_are_hidden():
    source = SIDE_PANEL.read_text(encoding="utf-8")
    assert "protected_model = (" in source
    assert "if show_markers" in source
    assert "highlights_enabled=True" in source
    assert "protected_highlight_spans = list(" in source
    assert '"protected_highlight_spans": protected_highlight_spans' in source


def test_component_wrapper_remains_transport_only():
    source = COMPONENT.read_text(encoding="utf-8")
    assert "def render_processed_text_selection_component(" in source
    assert "build_manual_mask_row" not in source
    assert "commit_manual_mask" not in source
    assert "session_state" not in source
    assert "download_button" not in source


def test_integration_adapter_is_the_only_layer_appending_document_scoped_manual_rows():
    source = INTEGRATION.read_text(encoding="utf-8")
    assert 'MANUAL_ROWS_KEY = "manual_mask_rows"' in source
    assert "manual_rows.append(dict(result.row))" in source
    assert "manual_bucket[document_scope_key] = manual_rows" in source
    assert "session[MANUAL_ROWS_KEY] = manual_bucket" in source
    assert "commit_manual_mask(" in source
    assert "undo_manual_selection_action(" in source
    assert "import streamlit" not in source


def test_no_export_scrub_key_or_reinsert_semantics_are_implemented_in_new_layers():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (COMPONENT, INTEGRATION, SIDE_PANEL)
    )
    for forbidden in (
        "build_scrub_key",
        "write_scrub_key",
        "reinsert_document",
        "st.download_button",
        "export_filename",
    ):
        assert forbidden not in combined
