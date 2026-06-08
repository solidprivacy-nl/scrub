from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def _slice_between(start_marker: str, end_marker: str) -> str:
    start = PATCH_TEXT.index(start_marker)
    end = PATCH_TEXT.index(end_marker, start)
    return PATCH_TEXT[start:end]


def _txt_reinsert_block() -> str:
    return _slice_between("txt_reinsert_ui_block = '''", "'''\n\nreview_summary_block =")


def test_txt_reinsert_helper_is_imported_and_used():
    assert "from scrub_key_document_reinsert import reinsert_txt_bytes" in PATCH_TEXT
    assert "reinsert_txt_bytes(" in PATCH_TEXT
    assert "txt_reinsert_file.getvalue()" in PATCH_TEXT
    assert 'encoding="utf-8"' in PATCH_TEXT


def test_txt_reinsert_ui_labels_are_present():
    for marker in [
        "TXT-bestand terugzetten",
        "Upload een TXT-bestand met placeholders",
        "Zet TXT-bestand lokaal terug",
        "Herstelde TXT-tekst",
        "Download hersteld TXT-bestand (.txt)",
        "Controleverslag TXT terugzetten",
    ]:
        assert marker in PATCH_TEXT


def test_txt_reinsert_accepts_txt_only_and_requires_key():
    txt_block = _txt_reinsert_block()
    assert 'type=["txt"]' in txt_block
    assert "Laad eerst een geldige Scrub Key" in txt_block
    assert "Upload eerst een TXT-bestand met placeholders" in txt_block
    assert "active_txt_reinsert_scrub_key" in txt_block
    assert 'st.session_state.get("active_scrub_key", {})' in txt_block


def test_txt_reinsert_is_inside_reinsert_mode_only():
    mode_index = PATCH_TEXT.index('if solidprivacy_work_mode == "Originele waarden terugzetten":')
    txt_block_index = PATCH_TEXT.index("txt_reinsert_ui_block")
    else_index = PATCH_TEXT.index("'''else:\n'''")
    assert mode_index < txt_block_index < else_index
    review_summary_start = PATCH_TEXT.index("review_summary_block =")
    review_summary_end = PATCH_TEXT.index("text = replace_once(\n    text,\n    '''        st.subheader", review_summary_start)
    review_summary_block = PATCH_TEXT[review_summary_start:review_summary_end]
    assert "TXT-bestand terugzetten" not in review_summary_block
    assert "Download hersteld TXT-bestand (.txt)" not in review_summary_block


def test_pasted_text_reinsert_and_scrub_key_load_remain_present():
    for marker in [
        "Scrub Key laden",
        "Upload Scrub Key JSON (.json)",
        "Of plak Scrub Key JSON",
        "Valideer en laad Scrub Key",
        "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten",
        "Zet originele waarden lokaal terug",
        "Herstelde tekst",
        "Download herstelde tekst (.txt)",
        "Controleverslag terugzetten",
    ]:
        assert marker in PATCH_TEXT


def test_anonymization_mode_and_existing_exports_remain_present():
    for marker in [
        "Anonimiseren",
        "Originele waarden terugzetten",
        "Kies werkmodus",
        'st.subheader("4. Download opgeschoonde bestanden")',
        "Download opgeschoonde bestanden",
        "Eindcontrole vóór download",
        "Extra exportcontrole",
        "Scrub Key (JSON)",
        "Download Scrub Key (.json)",
        "st.warning(EXPORT_GUIDANCE)",
    ]:
        assert marker in PATCH_TEXT


def test_txt_reinsert_audit_summary_fields_are_present():
    txt_block = _txt_reinsert_block()
    for marker in [
        "Documenttype",
        "Mappingregels totaal",
        "Actieve mappingregels",
        "Uitgesloten mappingregels",
        "Aantal teruggezette waarden",
        "Niet gevonden placeholders",
        "Onbekende placeholders in tekst",
        "Dubbele placeholders in sleutel",
        "Validatieproblemen",
        "Lokaal uitgevoerd",
        "AI-verwerking",
        "Cloudverwerking",
        "document_type",
        "item_count",
        "active_item_count",
        "excluded_item_count",
        "replacement_count",
        "placeholders_not_found",
        "unknown_placeholders",
        "duplicate_placeholders",
        "validation_issues",
        "local_only",
        "ai_processing",
        "cloud_processing",
    ]:
        assert marker in txt_block


def test_txt_reinsert_warnings_are_present():
    txt_block = _txt_reinsert_block()
    assert "terugzetten herstelt originele gevoelige waarden" in txt_block
    assert "persoonsgegevens of vertrouwelijke informatie" in txt_block
    assert "Controleer het resultaat zorgvuldig voordat u het deelt" in txt_block
    assert "lokaal uitgevoerd" in txt_block.lower()
    assert "geen AI- of cloudverwerking" in txt_block
    assert "Scrub Key" in txt_block


def test_no_docx_pdf_ai_cloud_or_export_rewire_added():
    lower_patch = PATCH_TEXT.lower()
    for marker in [
        "reinsert_docx_bytes",
        "Upload DOCX",
        "Upload .docx",
        "hersteld DOCX",
        "Download hersteld DOCX",
        "download_docx_reinserted",
        "download_pdf_reinserted",
        "PDF reinsert",
        "pdf reinsert",
        "requests.post",
        "httpx.post",
        "cloud processing call",
        "rehydrat",
        "restore_original_document",
        "server-side key storage",
        "durable key vault",
        "openai",
        "anthropic",
    ]:
        assert marker.lower() not in lower_patch
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT
    assert "changes_export_semantics = True" not in PATCH_TEXT
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "apply_replacements_to_text =" not in PATCH_TEXT
    assert "export_text = apply_replacements_to_text" not in PATCH_TEXT
    assert "download_txt" not in PATCH_TEXT
    assert "download_csv" not in PATCH_TEXT
    assert "download_docx" not in PATCH_TEXT
    assert "download_pdf" not in PATCH_TEXT
