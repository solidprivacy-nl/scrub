from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
DOCKERFILE = REPO_ROOT / "Dockerfile"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"


def _app_text() -> str:
    return APP.read_text(encoding="utf-8")


def test_default_flow_is_shorter_and_execution_oriented() -> None:
    text = _app_text()

    assert 'st.subheader("1. Voeg document of tekst toe")' in text
    assert 'st.subheader("2. Controleer resultaat")' in text
    assert 'st.subheader("3. Exporteer resultaat")' in text

    assert 'st.subheader("2. Controleer de tekst")' not in text
    assert 'st.subheader("3. Controleer gevonden gegevens")' not in text
    assert 'st.subheader("4. Onthoud herbruikbare vervangingen")' not in text
    assert 'st.subheader("5. Exporteer resultaat")' not in text


def test_secondary_controls_are_collapsed_but_available() -> None:
    text = _app_text()
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    for marker in [
        'with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False)',
        'with st.expander("Controle-instellingen en herkenning", expanded=False)',
        'with st.expander("Waarom controleren?", expanded=False)',
        'with st.expander("Gemiste waarde toevoegen", expanded=False)',
        'with st.expander("Extra controlehulpen", expanded=False)',
        'with st.expander("Mogelijk extra te controleren waarden", expanded=False)',
        'with st.expander(f"Vervangtabel controleren — {len(replacement_editor_df.index)} items", expanded=False)',
        'with st.expander("Geavanceerde details bij de vervangtabel", expanded=False)',
        'with st.expander("Herbruikbare vervangingen", expanded=False)',
        'with st.expander("Scrub Key downloaden", expanded=False)',
        'with st.expander("Audit en technische bestanden", expanded=False)',
    ]:
        assert marker in text

    assert 'with st.expander("Stap voor stap controleren", expanded=False)' in serial_text


def test_review_table_manual_entry_and_source_of_truth_remain() -> None:
    text = _app_text()

    assert "manual_mask_entry_form" in text
    assert "Toevoegen aan vervangtabel" in text
    assert "replacement_editor" in text
    assert "st.data_editor(" in text
    assert "De vervangtabel blijft leidend" in text
    assert "edited_replacements_df = st.data_editor(" in text
    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" in text


def test_export_buttons_keys_and_filenames_remain_unchanged() -> None:
    text = _app_text()

    for marker in [
        'label="Download opgeschoonde tekst (.txt)"',
        'file_name="opgeschoonde_tekst.txt"',
        'key="download_txt"',
        'label="Download opgeschoond Word-bestand (.docx)"',
        'key="download_docx"',
        'label="Download opgeschoonde PDF (.pdf)"',
        'file_name="opgeschoonde_tekst.pdf"',
        'key="download_pdf"',
        'label="Download vervangtabel (.csv)"',
        'file_name="vervangtabel.csv"',
        'key="download_csv"',
        'label="Download scrubrapport (.txt)"',
        'file_name="scrubrapport.txt"',
        'key="download_scrub_report"',
    ]:
        assert marker in text


def test_scrub_key_warning_and_semantics_remain_available() -> None:
    text = _app_text()

    assert "De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig." in text
    assert "scrub_key_rows = edited_replacements_df.copy()" in text
    assert '"find": "original_value"' in text
    assert '"replace_with": "placeholder"' in text
    assert "build_export_scrub_key(scrub_key_rows)" in text
    assert "validate_export_scrub_key(scrub_key)" in text
    assert "export_key_json(scrub_key)" in text
    assert '"Download Scrub Key (.json)"' in text
    assert 'file_name="solidprivacy_scrub_key.json"' in text
    assert 'key="download_scrub_key"' in text


def test_no_startup_runtime_patch_or_blocked_ui_features_added() -> None:
    combined = (_app_text() + "\n" + DOCKERFILE.read_text(encoding="utf-8")).lower()

    forbidden = [
        "execution_interface_simplification_patch",
        "fix_streamlit_execution_interface_simplification",
        "sitecustomize",
        "runtime source mutation",
        "right-click",
        "click-to-mark",
        "full-document marking",
        "cloud document processing",
    ]
    for marker in forbidden:
        assert marker not in combined
