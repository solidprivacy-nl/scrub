from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
RENDERER = REPO_ROOT / "docx_hygiene_audit_panel_ui.py"
STARTUP_PATCH = REPO_ROOT / "fix_streamlit_nested_expanders.py"


def _combined_text() -> str:
    return APP.read_text(encoding="utf-8") + "\n" + RENDERER.read_text(encoding="utf-8")


def test_presidio_imports_and_uses_docx_hygiene_audit_panel():
    app_text = APP.read_text(encoding="utf-8")

    assert "from docx_hygiene_audit_panel_ui import render_docx_hygiene_audit_panel" in app_text
    assert "render_docx_hygiene_audit_panel(" in app_text


def test_docx_hygiene_audit_panel_uses_existing_helper():
    renderer_text = RENDERER.read_text(encoding="utf-8")

    assert "from docx_hygiene_audit import build_docx_hygiene_audit_report" in renderer_text
    assert "build_docx_hygiene_audit_report(" in renderer_text
    assert "docx_hygiene_audit.py" in renderer_text


def test_docx_hygiene_audit_ui_visible_safety_copy_exists():
    text = _combined_text()

    assert "DOCX hygiene audit" in text
    assert "Alleen rapportage" in text
    assert "Geen clean-DOCX garantie" in text
    assert "Export wordt niet geblokkeerd" in text
    assert "Bestaande export blijft ongewijzigd" in text
    assert "audit/waarschuwing" in text
    assert "geen automatische opschoning" in text
    assert "gebruiker blijft zelf verantwoordelijk" in text.lower()


def test_docx_hygiene_audit_ui_mentions_required_risk_areas():
    text = _combined_text()

    assert "metadata" in text
    assert "opmerkingen" in text
    assert "revisies" in text
    assert "verborgen inhoud" in text
    assert "kopteksten" in text.lower()
    assert "voetteksten" in text.lower()
    assert "bijgehouden wijzigingen" in text.lower()


def test_docx_hygiene_audit_ui_remains_report_only_and_non_mutating():
    renderer_text = RENDERER.read_text(encoding="utf-8")

    assert "does not clean DOCX content" in renderer_text
    assert "remove comments" in renderer_text
    assert "remove tracked changes" in renderer_text
    assert "remove metadata" in renderer_text
    assert "block export" in renderer_text
    assert "write Scrub Key data" in renderer_text
    assert "change reinsert behavior" in renderer_text
    assert "Export blocking: false" in renderer_text


def test_docx_hygiene_audit_ui_does_not_add_export_blocking_or_cleaner_behavior():
    text = _combined_text().lower()

    forbidden_implementation_markers = [
        "export_blocking = true",
        "export_blocking_applied = true",
        "cleaning_applied = true",
        "safe_to_claim_clean = true",
        "remove_comments(",
        "remove_tracked_changes(",
        "remove_metadata(",
        "clean_docx(",
        "block_export = true",
        "download_schone_docx",
    ]
    for marker in forbidden_implementation_markers:
        assert marker not in text


def test_docx_hygiene_audit_ui_does_not_change_scrub_key_or_reinsert_behavior():
    renderer_text = RENDERER.read_text(encoding="utf-8").lower()

    forbidden_implementation_markers = [
        "scrub_key_to_json(",
        "build_scrub_key(",
        "validate_scrub_key(",
        "reinsert_from_scrub_key(",
        "reinsert_docx_bytes(",
        "reinsert_txt_bytes(",
        "st.session_state[\"scrub_key",
    ]
    for marker in forbidden_implementation_markers:
        assert marker not in renderer_text


def test_docx_hygiene_audit_ui_does_not_use_cloud_or_real_data():
    rendered = _combined_text() + "\n" + Path(__file__).read_text(encoding="utf-8")
    lowered = rendered.lower()

    assert "no cloud processing" in lowered or "cloud services" in lowered
    assert "real data" in lowered
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered


def test_docx_hygiene_audit_ui_does_not_use_startup_source_mutation():
    renderer_text = RENDERER.read_text(encoding="utf-8")
    startup_text = STARTUP_PATCH.read_text(encoding="utf-8")

    assert "docx_hygiene_audit_panel_ui" not in startup_text
    assert "DOCX hygiene audit" not in startup_text
    assert "APP_FILE.write_text" not in renderer_text
    assert "replace_once(" not in renderer_text


def test_docx_hygiene_audit_ui_does_not_implement_blocked_review_features():
    renderer_text = RENDERER.read_text(encoding="utf-8").lower()

    assert "click-to-mark" not in renderer_text
    assert "advanced editor" not in renderer_text
    assert "full-document marking" not in renderer_text
    assert "unsafe_allow_html" not in renderer_text
