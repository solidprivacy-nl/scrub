from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def _slice_between(start_marker: str, end_marker: str) -> str:
    start = PATCH_TEXT.index(start_marker)
    end = PATCH_TEXT.index(end_marker, start)
    return PATCH_TEXT[start:end]


def _docx_reinsert_block() -> str:
    return _slice_between("docx_reinsert_ui_block = '''", "'''\n\nreview_summary_block =")


def test_docx_reinsert_helper_is_imported_and_used():
    assert "from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes" in PATCH_TEXT
    assert "reinsert_docx_bytes(" in PATCH_TEXT
    assert "docx_reinsert_file.getvalue()" in PATCH_TEXT


def test_docx_reinsert_ui_labels_are_present():
    for marker in [
        "DOCX-bestand terugzetten",
        "Upload een DOCX-bestand met placeholders",
        "Zet DOCX-bestand lokaal terug",
        "DOCX-bestand lokaal teruggezet",
        "Download hersteld DOCX-bestand (.docx)",
        "Controleverslag DOCX terugzetten",
    ]:
        assert marker in PATCH_TEXT


def test_docx_reinsert_accepts_docx_only_and_requires_key():
    docx_block = _docx_reinsert_block()
    assert 'type=["docx"]' in docx_block
    assert "Laad eerst een geldige Scrub Key" in docx_block
    assert "Upload eerst een DOCX-bestand met placeholders" in docx_block
    assert "active_docx_reinsert_scrub_key" in docx_block
    assert 'st.session_state.get("active_scrub_key", {})' in docx_block


def test_docx_reinsert_is_injected_inside_reinsert_mode_only():
    mode_start = PATCH_TEXT.index("two_mode_selection_block = '''")
    mode_end = PATCH_TEXT.index("mode_marker =", mode_start)
    mode_block = PATCH_TEXT[mode_start:mode_end]
    mode_index = mode_block.index('if solidprivacy_work_mode == "Originele waarden terugzetten":')
    docx_injection_index = mode_block.index("scrub_key_import_ui_block + reinsert_ui_block + txt_reinsert_ui_block + docx_reinsert_ui_block")
    else_index = mode_block.index("'''else:\n'''")
    assert mode_index < docx_injection_index < else_index
    review_summary_start = PATCH_TEXT.index("review_summary_block =")
    review_summary_end = PATCH_TEXT.index("text = replace_once(\n    text,\n    '''        st.subheader", review_summary_start)
    review_summary_block = PATCH_TEXT[review_summary_start:review_summary_end]
    assert "DOCX-bestand terugzetten" not in review_summary_block
    assert "Download hersteld DOCX-bestand (.docx)" not in review_summary_block


def test_docx_limitations_warning_is_present():
    docx_block = _docx_reinsert_block()
    assert "DOCX-terugzetten ondersteunt in deze versie normale documenttekst en tabellen" in docx_block
    assert "Headers, footers, opmerkingen, bijgehouden wijzigingen" in docx_block
    assert "meerdere tekstfragmenten" in docx_block
    assert "DOCX-beperkingen" in docx_block
    assert "limitations" in docx_block


def test_docx_reinsert_audit_summary_fields_are_present():
    docx_block = _docx_reinsert_block()
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
        "DOCX-beperkingen",
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
        "limitations",
    ]:
        assert marker in docx_block


def test_pasted_text_txt_reinsert_and_scrub_key_load_remain_present():
    for marker in [
        "Scrub Key laden",
        "Upload Scrub Key JSON (.json)",
        "Of plak Scrub Key JSON",
        "Valideer en laad Scrub Key",
        "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten",
        "Zet originele waarden lokaal terug",
        "Herstelde tekst",
        "Download herstelde tekst (.txt)",
        "TXT-bestand terugzetten",
        "Upload een TXT-bestand met placeholders",
        "Zet TXT-bestand lokaal terug",
        "Herstelde TXT-tekst",
        "Download hersteld TXT-bestand (.txt)",
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


def test_no_pdf_ai_cloud_or_export_rewire_added():
    lower_patch = PATCH_TEXT.lower()
    for marker in [
        "download_pdf_reinserted",
        "PDF reinsert",
        "pdf reinsert",
        "requests.post",
        "httpx.post",
        "cloud processing call",
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
