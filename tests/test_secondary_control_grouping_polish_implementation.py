from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE_TEXT = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
SERIAL_REVIEW_TEXT = (REPO_ROOT / "serial_review_panel_ui.py").read_text(encoding="utf-8")
PLAN_TEXT = (REPO_ROOT / "SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md").read_text(encoding="utf-8")


def test_secondary_controls_have_a_visible_grouping_label_without_parent_expander() -> None:
    assert 'st.markdown("#### Meer controleopties")' in SIDE_BY_SIDE_TEXT
    assert "Aanvullen, detailcontrole en stap-voor-stap controle staan hieronder compact bij elkaar." in SIDE_BY_SIDE_TEXT
    assert "Alles staat standaard ingeklapt." in SIDE_BY_SIDE_TEXT
    assert 'st.expander("Meer controleopties"' not in SIDE_BY_SIDE_TEXT
    assert 'with st.expander("Meer controleopties"' not in APP_TEXT


def test_primary_review_surface_stays_above_secondary_grouping_hint() -> None:
    assert SIDE_BY_SIDE_TEXT.index("components.html(") < SIDE_BY_SIDE_TEXT.index('st.markdown("#### Meer controleopties")')
    assert "Markeringen tonen" in SIDE_BY_SIDE_TEXT
    assert "Brontekst" in SIDE_BY_SIDE_TEXT
    assert "Verwerkte tekst" in SIDE_BY_SIDE_TEXT


def test_existing_secondary_controls_remain_reachable_in_app_source() -> None:
    for marker in [
        "Waarom controleren?",
        "Gemiste waarde toevoegen",
        "Extra controlehulpen",
        "Mogelijk extra te controleren waarden",
        "Vervangtabel controleren",
        "Geavanceerde details bij de vervangtabel",
        "Herbruikbare vervangingen",
    ]:
        assert marker in APP_TEXT
    assert "Stap voor stap controleren" in SERIAL_REVIEW_TEXT


def test_review_table_and_manual_entry_stay_source_of_truth_paths() -> None:
    for marker in [
        "De vervangtabel blijft leidend",
        "replacement_editor",
        "edited_replacements_df",
        "build_manual_mask_row",
        "validate_manual_mask_input",
        "manual_mask_document_key",
    ]:
        assert marker in APP_TEXT


def test_no_nested_expander_implementation_is_added_for_grouping() -> None:
    lowered = SIDE_BY_SIDE_TEXT.lower() + "\n" + APP_TEXT.lower()
    assert "nested streamlit expanders" not in lowered
    assert "st.expander(\"meer controleopties\"" not in lowered
    assert "with st.expander(\"meer controleopties\"" not in lowered
    assert "do not use nested streamlit expanders" in PLAN_TEXT.lower()


def test_export_scrub_key_reinsert_and_audit_controls_stay_visible() -> None:
    for marker in [
        "Document downloaden",
        "Download opgeschoonde tekst (.txt)",
        "Download opgeschoond Word-bestand (.docx)",
        "Download opgeschoonde PDF (.pdf)",
        "Scrub Key downloaden",
        "Download Scrub Key (.json)",
        "Audit en technische bestanden",
        "render_docx_hygiene_audit_panel",
        "Technische informatie",
        "Geavanceerde herkenningsdetails",
    ]:
        assert marker in APP_TEXT


def test_no_prohibited_behavior_is_added_by_grouping_polish() -> None:
    changed_surface = SIDE_BY_SIDE_TEXT + "\n" + SERIAL_REVIEW_TEXT
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
        assert forbidden not in changed_surface
