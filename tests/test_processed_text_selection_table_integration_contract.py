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
    render_call = source.index("side_by_side_review_state = render_side_by_side_review_panel(")
    handler_call = source.index("selection_outcome = handle_selection_component_event(")
    fragment = source[render_call:handler_call]
    assert "document_scope_key=document_scope_key" in fragment
    assert "inspection_result=selection_inspection" in fragment
    assert "restore_source_scroll_ratio=restore_source_scroll" in fragment
    assert "restore_processed_scroll_ratio=restore_processed_scroll" in fragment


def test_component_event_is_server_validated_and_rerun_before_exports():
    source = APP.read_text(encoding="utf-8")
    handler_index = source.index("selection_outcome = handle_selection_component_event(")
    first_download_index = source.index("st.download_button", handler_index)
    fragment = source[handler_index:first_download_index]

    assert "source_text=st_text" in fragment
    assert 'processed_text=side_by_side_review_state.get("processed_text", "")' in fragment
    assert "document_scope_key=document_scope_key" in fragment
    assert "document_binding_id=document_binding_id" in fragment
    assert "existing_rows=replacement_editor_df" in fragment
    assert 'marked_ranges=side_by_side_review_state.get("highlight_spans", ())' in fragment
    assert "if selection_outcome.rerun_required:" in fragment
    assert "st.rerun()" in fragment
    assert handler_index < first_download_index


def test_undo_is_document_scoped_and_requires_latest_action():
    source = APP.read_text(encoding="utf-8")
    assert "latest_selection_action(st.session_state, document_scope_key)" in source
    assert "undo_latest_selection_action(" in source
    assert "document_scope_key=document_scope_key" in source
    assert "if undo_outcome.rerun_required:" in source
    assert "st.rerun()" in source


def test_existing_manual_form_and_authoritative_review_table_remain_present():
    source = APP.read_text(encoding="utf-8")
    assert "Gemiste waarde toevoegen" in source
    assert "build_manual_mask_row(" in source
    assert "edited_replacements_df = st.data_editor(" in source
    assert "De vervangtabel blijft leidend" in source
    assert "apply_replacements_to_text(st_text, edited_replacements)" in source


def test_side_panel_has_interactive_default_and_environment_rollback():
    source = SIDE_PANEL.read_text(encoding="utf-8")
    assert 'INTERACTIVE_COMPONENT_ENV = "PROCESSED_TEXT_SELECTION_COMPONENT_ENABLED"' in source
    assert 'os.environ.get(INTERACTIVE_COMPONENT_ENV, "true")' in source
    assert "render_processed_text_selection_component(" in source
    assert "except Exception as exc:" in source
    assert "_render_static_fallback(" in source
    assert '"static_fallback_available": True' in source
    assert '"component_environment_switch": INTERACTIVE_COMPONENT_ENV' in source


def test_selection_of_existing_marked_content_is_protected_server_side():
    side_source = SIDE_PANEL.read_text(encoding="utf-8")
    app_source = APP.read_text(encoding="utf-8")
    action_source = (ROOT / "selection_mask_action.py").read_text(encoding="utf-8")
    assert "highlight_spans = list(model[\"processed_pane\"][\"highlight_spans\"])" in side_source
    assert '"highlight_spans": highlight_spans' in side_source
    assert 'marked_ranges=side_by_side_review_state.get("highlight_spans", ())' in app_source
    assert "def ranges_overlap(" in action_source
    assert "frontend_intersects_marked_content or any(" in action_source
    assert "ranges_overlap((start_index, end_index), marked_range)" in action_source
    assert "marked_content" in action_source
    assert "STRICT_PLACEHOLDER_SEARCH_RE" in action_source


def test_component_wrapper_remains_transport_only():
    source = COMPONENT.read_text(encoding="utf-8")
    assert "def render_processed_text_selection_component(" in source
    assert "build_manual_mask_row" not in source
    assert "from selection_mask_action import" not in source
    assert "st.session_state" not in source
    assert "download_button" not in source
    assert '"commit_action": "commit_manual_mask"' in source


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
