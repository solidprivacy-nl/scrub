from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_two_mode_labels_are_present_in_patch():
    assert "Anonimiseren" in PATCH_TEXT
    assert "Originele waarden terugzetten" in PATCH_TEXT
    assert "Kies werkmodus" in PATCH_TEXT


def test_two_mode_patch_uses_streamlit_tabs():
    assert "st.tabs" in PATCH_TEXT
    assert 'two_mode_anon_tab, two_mode_reinsert_tab = st.tabs(["Anonimiseren", "Originele waarden terugzetten"])' in PATCH_TEXT
    assert "with two_mode_anon_tab" in PATCH_TEXT
    assert "with two_mode_reinsert_tab" in PATCH_TEXT


def test_two_mode_captions_explain_privacy_modes():
    assert "Anonimiseren: upload of plak brontekst" in PATCH_TEXT
    assert "download opgeschoonde uitvoer" in PATCH_TEXT
    assert "Originele waarden terugzetten: laad een Scrub Key" in PATCH_TEXT
    assert "lokale tekst-terugzetflow" in PATCH_TEXT


def test_existing_scrub_key_export_and_import_labels_remain_present():
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "Scrub Key laden" in PATCH_TEXT
    assert "Upload Scrub Key JSON (.json)" in PATCH_TEXT
    assert "Of plak Scrub Key JSON" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT


def test_existing_pasted_text_reinsert_labels_remain_present():
    assert "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten" in PATCH_TEXT
    assert "Zet originele waarden lokaal terug" in PATCH_TEXT
    assert "Herstelde tekst" in PATCH_TEXT
    assert "Download herstelde tekst (.txt)" in PATCH_TEXT
    assert "Controleverslag terugzetten" in PATCH_TEXT


def test_existing_anonymization_and_download_markers_remain_present():
    assert 'st.subheader("4. Download opgeschoonde bestanden")' in PATCH_TEXT
    assert "Download opgeschoonde bestanden" in PATCH_TEXT
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT


def test_scrubbed_download_behavior_markers_are_not_removed_or_rewired():
    # The startup patch must not patch existing scrubbed download widgets directly.
    assert "download_txt" not in PATCH_TEXT
    assert "download_csv" not in PATCH_TEXT
    assert "download_docx" not in PATCH_TEXT
    assert "download_pdf" not in PATCH_TEXT
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "apply_replacements_to_text =" not in PATCH_TEXT
    assert "export_text = apply_replacements_to_text" not in PATCH_TEXT


def test_two_mode_patch_does_not_add_txt_docx_or_pdf_reinsert_upload_ui():
    forbidden_markers = [
        "reinsert_txt_bytes",
        "reinsert_docx_bytes",
        "Upload TXT",
        "Upload .txt",
        "Upload DOCX",
        "Upload .docx",
        "hersteld DOCX",
        "Download hersteld DOCX",
        "download_docx_reinserted",
        "download_pdf_reinserted",
        "PDF reinsert",
        "pdf reinsert",
    ]
    for marker in forbidden_markers:
        assert marker not in PATCH_TEXT


def test_two_mode_patch_does_not_add_ai_cloud_or_rehydration_behavior():
    lower_patch = PATCH_TEXT.lower()
    for marker in [
        "requests.post",
        "httpx.post",
        "cloud processing call",
        "rehydrat",
        "restore_original_document",
        "server-side key storage",
        "durable key vault",
    ]:
        assert marker.lower() not in lower_patch
    assert "openai" not in lower_patch
    assert "anthropic" not in lower_patch
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT
    assert "changes_export_semantics = True" not in PATCH_TEXT
