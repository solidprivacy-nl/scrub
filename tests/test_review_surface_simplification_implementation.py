from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE_TEXT = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
SERIAL_REVIEW_TEXT = (REPO_ROOT / "serial_review_panel_ui.py").read_text(encoding="utf-8")
MANUAL_MASK_TEXT = (REPO_ROOT / "manual_mask_entry.py").read_text(encoding="utf-8")
CONTRACT_TEXT = (REPO_ROOT / "REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md").read_text(encoding="utf-8")


def test_primary_flow_copy_is_present_and_calmer() -> None:
    combined = APP_TEXT + "\n" + SIDE_BY_SIDE_TEXT + "\n" + CONTRACT_TEXT

    assert "1. Voeg document of tekst toe" in APP_TEXT
    assert "2. Controleer resultaat" in APP_TEXT
    assert "3. Exporteer resultaat" in APP_TEXT
    assert "Download veilig" in combined
    assert "Controleer links de brontekst en rechts de verwerkte tekst." in SIDE_BY_SIDE_TEXT
    assert "Deze vergelijking wijzigt zelf niets." in SIDE_BY_SIDE_TEXT


def test_side_by_side_review_remains_visible_and_primary() -> None:
    assert "render_side_by_side_review_panel" in APP_TEXT
    assert "Brontekst" in SIDE_BY_SIDE_TEXT
    assert "Verwerkte tekst" in SIDE_BY_SIDE_TEXT
    assert "Markeringen tonen" in SIDE_BY_SIDE_TEXT
    assert "side-by-side review remains the primary" in CONTRACT_TEXT.lower()


def test_review_table_remains_reachable_and_source_of_truth() -> None:
    for marker in [
        "Vervangtabel controleren",
        "edited_replacements_df",
        "key=\"replacement_editor\"",
        "De vervangtabel blijft leidend",
    ]:
        assert marker in APP_TEXT
    assert "review table remains source of truth and fallback" in CONTRACT_TEXT.lower()


def test_manual_missed_value_entry_remains_reachable() -> None:
    for marker in [
        "Gemiste waarde toevoegen",
        "from manual_mask_entry import",
        "build_manual_mask_row",
        "validate_manual_mask_input",
        "manual_mask_document_key",
    ]:
        assert marker in APP_TEXT
    assert "build_manual_mask_row" in MANUAL_MASK_TEXT


def test_serial_review_remains_secondary_and_reachable() -> None:
    assert "render_serial_review_panel" in APP_TEXT
    assert "Stap voor stap controleren" in SERIAL_REVIEW_TEXT
    assert "expanded=False" in SERIAL_REVIEW_TEXT
    assert "Deze hulpweergave verandert niets" in SERIAL_REVIEW_TEXT


def test_scrub_key_remains_separate_and_warning_protected() -> None:
    for marker in [
        "Scrub Key downloaden",
        "De Scrub Key kan originele waarden herstellen",
        "Download Scrub Key (.json)",
        "solidprivacy_scrub_key.json",
        "mime=\"application/json\"",
    ]:
        assert marker in APP_TEXT


def test_export_download_semantics_remain_visible() -> None:
    for marker in [
        "Document downloaden",
        "Download opgeschoonde tekst (.txt)",
        "opgeschoonde_tekst.txt",
        "mime=\"text/plain\"",
        "Download opgeschoond Word-bestand (.docx)",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "Download opgeschoonde PDF (.pdf)",
        "mime=\"application/pdf\"",
    ]:
        assert marker in APP_TEXT


def test_audit_and_technical_details_remain_available() -> None:
    for marker in [
        "Audit en technische bestanden",
        "Download vervangtabel (.csv)",
        "Download scrubrapport (.txt)",
        "render_docx_hygiene_audit_panel",
        "Technische informatie",
        "Geavanceerde herkenningsdetails",
    ]:
        assert marker in APP_TEXT


def test_no_new_prohibited_review_surface_behavior_is_introduced() -> None:
    changed_review_surface = SIDE_BY_SIDE_TEXT + "\n" + SERIAL_REVIEW_TEXT

    for forbidden in [
        "cloud processing",
        "AI processing",
        "OCR",
        "restored PDF",
        "PDF-to-DOCX",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "hidden export gate",
    ]:
        assert forbidden not in changed_review_surface


def test_old_replacement_decision_helper_panel_stays_out() -> None:
    combined = APP_TEXT + "\n" + SIDE_BY_SIDE_TEXT + "\n" + SERIAL_REVIEW_TEXT

    assert "replacement decision helper" not in combined.lower()
    assert "Vervangbeslissing" not in combined
