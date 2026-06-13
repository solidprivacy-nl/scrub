from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"
RENDERER = REPO_ROOT / "replacement_decision_panel_ui.py"
STARTUP_PATCH = REPO_ROOT / "fix_streamlit_nested_expanders.py"

ALLOWED_VIEW_ONLY_SESSION_KEYS = {
    "replacement_decision_selected_occurrence_id",
    "replacement_decision_preview_state",
    "replacement_decision_preview_scope",
    "replacement_decision_preview_text",
    "replacement_decision_panel_expanded",
}


def _renderer_text() -> str:
    return RENDERER.read_text(encoding="utf-8")


def _combined_ui_text() -> str:
    return "\n".join(
        [
            APP.read_text(encoding="utf-8"),
            SERIAL_PANEL.read_text(encoding="utf-8"),
            RENDERER.read_text(encoding="utf-8"),
        ]
    )


def test_app_reaches_replacement_decision_panel_through_serial_review_panel():
    app_text = APP.read_text(encoding="utf-8")
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    assert "render_serial_review_panel(" in app_text
    assert "from replacement_decision_panel_ui import render_replacement_decision_panel" in serial_text
    assert "render_replacement_decision_panel(" in serial_text


def test_replacement_decision_panel_uses_existing_helper_functions():
    renderer_text = _renderer_text()

    assert "from replacement_decision import" in renderer_text
    assert "build_replacement_decision" in renderer_text
    assert "matching_occurrence_ids" in renderer_text
    assert "build_replacement_audit" in renderer_text


def test_replacement_decision_panel_visible_boundary_copy_exists():
    text = _combined_ui_text()

    required = [
        "Replacement decision helper",
        "staged decision preview only",
        "staged decision state is not applied state",
        "existing review table remains source of truth and fallback",
        "no review table mutation",
        "no automatic replacement",
        "no Scrub Key writes",
        "no export blocking",
        "no reinsert behavior change",
        "Vervanghulp",
        "Alleen voorbeeld / nog niet toegepast",
        "Bestaande vervangtabel blijft leidend",
        "Geen automatische vervanging",
        "Geen Scrub Key wijziging",
        "Export wordt niet geblokkeerd",
        "Terugzetten/originele waarden blijft ongewijzigd",
    ]
    for phrase in required:
        assert phrase in text


def test_replacement_decision_panel_shows_advisory_helper_fields():
    renderer_text = _renderer_text()

    for phrase in [
        "source_text",
        "entity_type",
        "suggested_replacement",
        "Decision state",
        "Scope",
        "Affected count",
        "Creates mapping",
        "mapping_candidates",
        "export_readiness",
        "unresolved_items",
        "risk_flags",
        "advisory only",
        "report-only/not applied",
    ]:
        assert phrase in renderer_text


def test_replacement_decision_panel_uses_only_allowed_view_only_session_keys():
    renderer_text = _renderer_text()
    discovered_session_keys = set(re.findall(r"st\.session_state\.get\(\"(replacement_decision_[A-Za-z0-9_]+)\"", renderer_text))
    discovered_widget_keys = set(re.findall(r"key=\"(replacement_decision_[A-Za-z0-9_]+)\"", renderer_text))
    discovered_keys = discovered_session_keys | discovered_widget_keys

    assert ALLOWED_VIEW_ONLY_SESSION_KEYS.issubset(discovered_keys)
    assert discovered_keys.issubset(ALLOWED_VIEW_ONLY_SESSION_KEYS)


def test_replacement_decision_panel_does_not_mutate_review_table_or_editor_state():
    renderer_text = _renderer_text()
    lowered = renderer_text.lower()

    forbidden = [
        "edited_replacements_df[",
        "edited_replacements_df.loc",
        "edited_replacements_df.iloc",
        "replacement_editor",
        "st.session_state[\"replacement_editor",
        "review_table_mutation = true",
        "review table rows =",
        "automatic_replacement = true",
    ]
    for marker in forbidden:
        assert marker.lower() not in lowered


def test_replacement_decision_panel_does_not_call_export_download_scrub_key_or_reinsert_functions():
    renderer_text = _renderer_text()
    lowered = renderer_text.lower()

    forbidden_calls = [
        "st.download_button",
        "download_button(",
        "apply_replacements_to_text(",
        "docx_from_text(",
        "pdf_from_text(",
        "anonymized_docx_from_original(",
        "replacement_report_csv(",
        "scrub_report_txt(",
        "save_remembered_replacements(",
        "scrub_key_to_json(",
        "build_scrub_key(",
        "validate_scrub_key(",
        "reinsert_from_scrub_key(",
        "reinsert_docx_bytes(",
        "reinsert_txt_bytes(",
    ]
    for marker in forbidden_calls:
        assert marker.lower() not in lowered


def test_replacement_decision_panel_does_not_implement_fuzzy_matching_or_guessed_intent():
    renderer_text = _renderer_text().lower()

    forbidden = [
        "fuzzywuzzy",
        "rapidfuzz",
        "levenshtein",
        "guess_intent",
        "guessed_intent = true",
        "fuzzy_matching = true",
    ]
    for marker in forbidden:
        assert marker not in renderer_text

    assert "all_normalized" in renderer_text
    assert "advisory only" in renderer_text
    assert "not_mutating" in renderer_text


def test_replacement_decision_panel_does_not_use_startup_source_mutation_or_blocked_editor_features():
    renderer_text = _renderer_text()
    startup_text = STARTUP_PATCH.read_text(encoding="utf-8")

    assert "replacement_decision_panel_ui" not in startup_text
    assert "APP_FILE.write_text" not in renderer_text
    assert "replace_once(" not in renderer_text
    assert "click-to-mark" not in renderer_text
    assert "advanced editor" not in renderer_text
    assert "full-document marking" not in renderer_text
    assert "unsafe_allow_html" not in renderer_text


def test_replacement_decision_panel_does_not_use_cloud_or_real_data_fixtures():
    rendered = _combined_ui_text() + "\n" + Path(__file__).read_text(encoding="utf-8")
    lowered = rendered.lower()

    assert "cloud services" in lowered
    assert "real data" in lowered
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
