from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"
RENDERER = REPO_ROOT / "replacement_decision_panel_ui.py"
HELPER = REPO_ROOT / "replacement_decision.py"
PLAN = REPO_ROOT / "REPLACE_LOGIC_UI_PLAN.md"
CONTRACT_TEST = REPO_ROOT / "tests" / "test_replace_logic_ui_contract.py"
STARTUP_PATCH = REPO_ROOT / "fix_streamlit_nested_expanders.py"


def _normal_flow_text() -> str:
    return APP.read_text(encoding="utf-8") + "\n" + SERIAL_PANEL.read_text(encoding="utf-8")


def _renderer_text() -> str:
    return RENDERER.read_text(encoding="utf-8")


def test_replacement_helper_and_contract_assets_are_preserved_for_redesign():
    assert HELPER.exists()
    assert PLAN.exists()
    assert CONTRACT_TEST.exists()
    assert RENDERER.exists()

    helper_text = HELPER.read_text(encoding="utf-8")
    plan_text = PLAN.read_text(encoding="utf-8")
    contract_text = CONTRACT_TEST.read_text(encoding="utf-8")

    assert "build_replacement_decision" in helper_text
    assert "build_replacement_audit" in helper_text
    assert "matching_occurrence_ids" in helper_text
    assert "staged decision preview only" in plan_text
    assert "existing review table remains source of truth and fallback" in plan_text
    assert "test_staged_vs_applied_state_contract_is_explicit_and_non_mutating" in contract_text


def test_replacement_helper_panel_is_not_rendered_in_normal_scrub_flow():
    app_text = APP.read_text(encoding="utf-8")
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")
    normal_flow = _normal_flow_text()

    assert "render_serial_review_panel(" in app_text
    assert "from replacement_decision_panel_ui import" not in app_text
    assert "from replacement_decision_panel_ui import" not in serial_text
    assert "render_replacement_decision_panel(" not in normal_flow
    assert "Replacement decision helper" not in normal_flow
    assert "replacement_decision_preview" not in normal_flow


def test_serial_review_panel_remains_available_and_table_first():
    normal_flow = _normal_flow_text()
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    assert "Stap voor stap controleren" in serial_text
    assert "expanded=False" in serial_text
    assert "Controleer gevonden gegevens één voor één" in serial_text
    assert "De vervangtabel blijft leidend voor beslissingen en export" in serial_text
    assert "Filter voor stap-voor-stap controle" in serial_text

    assert "Serial review — experimentele reviewhulp" not in serial_text
    assert "table-first baseline" not in serial_text
    assert "no Scrub Key mutation" not in serial_text
    assert "no export blocking" not in serial_text
    assert "no reinsert behavior change" not in serial_text

    assert "render_serial_review_panel(" in normal_flow
    assert "include_side_by_side=False" in normal_flow
    assert "render_side_by_side_review_panel(" in normal_flow
    assert "replacement_editor" in normal_flow

def test_parked_replacement_panel_still_documents_non_mutating_boundaries():
    renderer_text = _renderer_text()

    for phrase in [
        "staged decision preview only",
        "staged decision state is not applied state",
        "existing review table remains source of truth and fallback",
        "does not mutate review rows",
        "does not write edited_replacements_df",
        "does not apply replacements",
        "does not write Scrub Key mappings",
        "does not block export",
        "does not call export/download",
        "does not change reinsert behavior",
        "does not use fuzzy matching",
        "does not use real data",
    ]:
        assert phrase in renderer_text


def test_normal_flow_does_not_call_export_download_scrub_key_or_reinsert_from_replacement_panel():
    normal_flow = _normal_flow_text().lower()

    forbidden_calls = [
        "render_replacement_decision_panel(",
        "replacement_decision_panel_ui",
        "scrub_key_to_json(",
        "build_scrub_key(",
        "validate_scrub_key(",
        "reinsert_from_scrub_key(",
        "reinsert_docx_bytes(",
        "reinsert_txt_bytes(",
        "replacement_decision_preview",
    ]
    for marker in forbidden_calls:
        assert marker.lower() not in normal_flow


def test_no_automatic_replacement_or_editor_marking_features_were_added():
    normal_flow = _normal_flow_text().lower()
    renderer_text = _renderer_text().lower()

    forbidden_normal_flow_markers = [
        "automatic_replacement = true",
        "review_table_mutation = true",
        "st.session_state[\"replacement_editor",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "unsafe_allow_html",
    ]
    for marker in forbidden_normal_flow_markers:
        assert marker not in normal_flow

    assert "automatic_replacement" in renderer_text
    assert "scrub_key_writes" in renderer_text
    assert "export_blocking" in renderer_text
    assert "reinsert_behavior_change" in renderer_text


def test_no_startup_source_mutation_or_cloud_real_data_fixture_added():
    rendered = _normal_flow_text() + "\n" + _renderer_text()
    startup_text = STARTUP_PATCH.read_text(encoding="utf-8")

    app_file_write_marker = "APP_FILE" + ".write_text"
    replace_once_marker = "replace" + "_once("

    assert "replacement_decision_panel_ui" not in startup_text
    assert app_file_write_marker not in rendered
    assert replace_once_marker not in rendered
    assert "cloud services" in rendered.lower()
    assert "real data" in rendered.lower()

    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
