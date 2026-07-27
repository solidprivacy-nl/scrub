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


def test_reinsert_flow_has_three_task_headings_in_user_order():
    markers = [
        'st.subheader("1. Voeg het bestand toe dat je wilt herstellen")',
        'st.subheader("2. Voeg de bijbehorende Scrub Key toe")',
        'st.subheader("3. Download het herstelde resultaat")',
    ]
    for marker in markers:
        assert marker in REINSERT_UI_TEXT
    assert REINSERT_UI_TEXT.index(markers[0]) < REINSERT_UI_TEXT.index(markers[1])
    assert REINSERT_UI_TEXT.index(markers[1]) < REINSERT_UI_TEXT.index(markers[2])


def test_reinsert_inputs_remain_available_in_compact_form():
    for marker in [
        "Upload het bestand met placeholders",
        'type=["txt", "docx", "pdf"]',
        "Of plak tekst in plaats van een bestand",
        "Plak tekst met placeholders",
        "Upload de Scrub Key (.json)",
        "Of plak Scrub Key JSON",
        "Plak Scrub Key JSON",
    ]:
        assert marker in REINSERT_UI_TEXT


def test_source_and_key_are_processed_automatically():
    for marker in [
        "build_reinsert_source(",
        "build_scrub_key_import_result(scrub_key_text)",
        "build_reinsert_request_signature(source, active_key)",
        "run_reinsert_request(source, active_key)",
        "Scrub Key herkend en geldig",
    ]:
        assert marker in REINSERT_UI_TEXT

    for removed_marker in [
        "ack_scrub_key_import_risk",
        "load_scrub_key_import",
        "Valideer en laad Scrub Key",
        "ack_reinsert_text_confidential",
        "run_local_reinsert",
        "ack_reinsert_txt_confidential",
        "run_txt_file_reinsert",
        "ack_reinsert_docx_confidential",
        "run_docx_file_reinsert",
        "ack_reinsert_pdf_text_confidential",
        "run_pdf_text_file_reinsert",
    ]:
        assert removed_marker not in REINSERT_UI_TEXT


def test_one_final_download_acknowledgement_remains_present():
    assert "ack_auto_reinsert_download_confidential" in REINSERT_UI_TEXT
    assert "disabled=not acknowledged" in REINSERT_UI_TEXT
    assert "CONFIDENTIAL_OUTPUT_WARNING" in REINSERT_UI_TEXT
    assert "RESTORED_DOWNLOAD_WARNING" in REINSERT_UI_TEXT
    assert (
        "Ik begrijp dat het herstelde resultaat weer vertrouwelijke originele waarden bevat"
        in REINSERT_UI_TEXT
    )


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
        "cloud processing call",
        "server-side key storage",
        "durable key vault",
    ]:
        assert forbidden not in lower_text

    for required in [
        "geen herstelde PDF",
        "OCR is niet beschikbaar",
        "AI-verwerking",
        "Cloudverwerking",
    ]:
        assert required in REINSERT_UI_TEXT


def test_startup_injection_is_guarded_against_duplicate_direct_mode():
    assert "if mode_marker in text and 'solidprivacy_work_mode = st.radio(' not in text:" in STARTUP_PATCH_TEXT


def test_pdf_text_startup_patch_skips_direct_source_reinsert_ui():
    pdf_patch_text = Path("fix_streamlit_pdf_text_reinsert.py").read_text(encoding="utf-8")
    assert "from reinsert_mode_ui import render_reinsert_mode" in pdf_patch_text
    assert "raise SystemExit(0)" in pdf_patch_text
