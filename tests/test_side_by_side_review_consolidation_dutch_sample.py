from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"
SIDE_BY_SIDE_PANEL = REPO_ROOT / "side_by_side_review_panel_ui.py"
DEMO_TEXT = REPO_ROOT / "demo_text.txt"


def _app_text() -> str:
    return APP.read_text(encoding="utf-8")


def test_dutch_synthetic_legal_demo_text_replaces_english_demo():
    text = DEMO_TEXT.read_text(encoding="utf-8")

    assert "Op 14 maart 2026 ontving mr. Eva de Vries" in text
    assert "Woningstichting Noordrand" in text
    assert "WR-KLANT-2026-7712" in text
    assert "ZK-WOON-55091" in text
    assert "Deze gegevens zijn niet echt" in text
    assert "Here are a few example sentences we currently support" not in text


def test_app_uses_one_central_side_by_side_review_surface_before_review_table():
    text = _app_text()

    assert "from side_by_side_review_panel_ui import render_side_by_side_review_panel" in text
    assert 'st.subheader("2. Controleer resultaat")' in text
    assert "render_side_by_side_review_panel(" in text
    assert 'st.subheader("3. Exporteer resultaat")' in text
    assert text.index("render_side_by_side_review_panel(") < text.index("st.data_editor(")


def test_old_upper_direct_preview_is_removed():
    text = _app_text()

    assert 'st.subheader("Directe voorbeeldweergave")' not in text
    assert 'st.text_area(label="Automatisch resultaat"' not in text
    assert "st_anonymize_results = anonymize(" not in text
    assert "col1, col2 = st.columns(2)" not in text
    assert 'col1.subheader("Invoer")' not in text


def test_lower_duplicate_side_by_side_is_suppressed_in_serial_review_call():
    app_text = _app_text()
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    assert "include_side_by_side: bool = True" in serial_text
    assert "if include_side_by_side:" in serial_text
    assert "side-by-side review already rendered centrally" in serial_text
    assert "include_side_by_side=False" in app_text


def test_sync_scroll_and_highlight_toggle_remain_available_but_sync_control_is_hidden():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "De panelen scrollen samen" in text
    assert "sourcePane.addEventListener('scroll'" in text
    assert "processedPane.addEventListener('scroll'" in text
    assert "side_by_side_review_show_markers" in text
    assert "Markeringen tonen" in text
    assert "value=True" in text
    assert "Geel = vervangen of gemaskeerde waarde" in text
    assert "Synchroon scrollen" not in text
    assert 'id="syncToggle"' not in text


def test_side_by_side_primary_ui_does_not_show_debug_governance_caption():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "table-first baseline" not in text
    assert "visual-only highlights" not in text
    assert "no Scrub Key writes" not in text
    assert "no export/download changes" not in text
    assert "no reinsert behavior change" not in text
    assert "Must not change source text" not in text
    assert "Deze weergave is alleen bedoeld om te vergelijken. Pas beslissingen aan in de vervangtabel hieronder." in text


def test_review_table_and_download_labels_are_preserved():
    text = _app_text()

    assert "replacement_editor" in text
    assert "De vervangtabel blijft leidend" in text
    assert "edited_replacements" in text
    assert "apply_replacements_to_text(st_text, edited_replacements)" in text
    assert "Download opgeschoonde tekst (.txt)" in text
    assert "Download vervangtabel (.csv)" in text
    assert "Download scrubrapport (.txt)" in text
    assert "Download opgeschoond Word-bestand (.docx)" in text
    assert "Download opgeschoonde PDF (.pdf)" in text


def test_no_editor_or_startup_mutation_language_added():
    combined = "\n".join(
        [
            _app_text(),
            SERIAL_PANEL.read_text(encoding="utf-8"),
            SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8"),
        ]
    ).lower()

    assert "click-to-mark" not in combined
    assert "advanced editor" not in combined
    assert "full-document marking" not in combined
    assert "startup source mutation" not in combined
