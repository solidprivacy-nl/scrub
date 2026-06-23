from pathlib import Path


APP_TEXT = Path("presidio_streamlit.py").read_text(encoding="utf-8")
REINSERT_UI_TEXT = Path("reinsert_mode_ui.py").read_text(encoding="utf-8")
STARTUP_PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_reinsert_flow_is_direct_source():
    assert "from reinsert_mode_ui import render_reinsert_mode" in APP_TEXT
    assert 'solidprivacy_work_mode = st.radio(' in APP_TEXT
    assert 'if solidprivacy_work_mode == "Originele waarden terugzetten":' in APP_TEXT
    assert "render_reinsert_mode()" in APP_TEXT
    assert "st.stop()" in APP_TEXT


def test_reinsert_flow_has_four_task_headings():
    for marker in [
        'st.subheader("1. Voeg Scrub Key toe")',
        'st.subheader("2. Voeg tekst of document toe")',
        'st.subheader("3. Controleer herstelrapport")',
        'st.subheader("4. Download herstelde output")',
    ]:
        assert marker in REINSERT_UI_TEXT


def test_reinsert_inputs_remain_available():
    for marker in [
        "Upload Scrub Key JSON (.json)",
        "Of plak Scrub Key JSON",
        "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten",
        "TXT-bestand terugzetten",
        "Upload een TXT-bestand met placeholders",
        "DOCX-bestand terugzetten",
        "Upload een DOCX-bestand met placeholders",
        "PDF-tekst terugzetten naar TXT",
        "Upload een PDF-bestand met placeholders",
    ]:
        assert marker in REINSERT_UI_TEXT


def test_acknowledgement_gates_remain_present():
    for marker in [
        "ack_scrub_key_import_risk",
        "ack_reinsert_text_confidential",
        "ack_reinsert_txt_confidential",
        "ack_reinsert_docx_confidential",
        "ack_reinsert_pdf_text_confidential",
        "ack_download_restored_text_confidential",
        "ack_download_restored_txt_confidential",
        "ack_download_restored_docx_confidential",
        "ack_download_restored_pdf_text_confidential",
        "disabled=not",
    ]:
        assert marker in REINSERT_UI_TEXT


def test_restored_download_semantics_are_preserved():
    for marker in [
        'file_name="solidprivacy_herstelde_tekst.txt"',
        'file_name="solidprivacy_hersteld_txt_bestand.txt"',
        'file_name="solidprivacy_hersteld_docx_bestand.docx"',
        'file_name="solidprivacy_herstelde_txt_uit_pdf.txt"',
        'mime="text/plain"',
        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',
    ]:
        assert marker in REINSERT_UI_TEXT


def test_no_ai_cloud_ocr_or_restored_pdf_added():
    lower_text = REINSERT_UI_TEXT.lower()
    for forbidden in [
        "requests.post",
        "httpx.post",
        "openai.chat",
        "anthropic",
        "download herstelde pdf",
        "pdf-output: ja",
        "ocr gebruikt: ja",
        "cloud processing call",
        "server-side key storage",
        "durable key vault",
    ]:
        assert forbidden not in lower_text

    for required in [
        "geen AI- of cloudverwerking",
        "geen AI, geen cloudverwerking en geen OCR",
        "OCR gebruikt: Nee",
        "PDF-output: Nee",
        "Deze functie maakt geen herstelde PDF",
    ]:
        assert required in REINSERT_UI_TEXT


def test_startup_injection_is_guarded_against_duplicate_direct_mode():
    assert "if mode_marker in text and 'solidprivacy_work_mode = st.radio(' not in text:" in STARTUP_PATCH_TEXT


def test_pdf_text_startup_patch_skips_direct_source_reinsert_ui():
    pdf_patch_text = Path("fix_streamlit_pdf_text_reinsert.py").read_text(encoding="utf-8")
    assert "from reinsert_mode_ui import render_reinsert_mode" in pdf_patch_text
    assert "raise SystemExit(0)" in pdf_patch_text
