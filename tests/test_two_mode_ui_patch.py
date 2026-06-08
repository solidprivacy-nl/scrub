from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def _extract_triple_quoted_assignment(name: str) -> str:
    marker = f"{name} = '''"
    start = PATCH_TEXT.index(marker) + len(marker)
    end = PATCH_TEXT.index("'''", start)
    return PATCH_TEXT[start:end]


def _generated_two_mode_source_snippet() -> str:
    scrub_key_import_ui_block = _extract_triple_quoted_assignment("scrub_key_import_ui_block")
    reinsert_ui_block = _extract_triple_quoted_assignment("reinsert_ui_block")
    txt_reinsert_ui_block = _extract_triple_quoted_assignment("txt_reinsert_ui_block")
    anonymization_flow = "    with st.expander(\"Over deze app\", expanded=False):\n        st.write(\"anonimiseren\")\n"
    return (
        "st.markdown(\"**Kies werkmodus**\")\n"
        "solidprivacy_work_mode = st.radio(\n"
        "    \"Werkmodus\",\n"
        "    [\"Anonimiseren\", \"Originele waarden terugzetten\"],\n"
        "    horizontal=True,\n"
        "    key=\"solidprivacy_work_mode\",\n"
        "    help=\"Kies Anonimiseren voor opschonen en export. Kies Originele waarden terugzetten voor lokaal terugzetten met een Scrub Key.\",\n"
        ")\n"
        "if solidprivacy_work_mode == \"Originele waarden terugzetten\":\n"
        "    st.caption(\"Originele waarden terugzetten: laad een Scrub Key en herstel placeholders lokaal in geplakte tekst.\")\n"
        + scrub_key_import_ui_block
        + reinsert_ui_block
        + txt_reinsert_ui_block
        + "else:\n"
        + anonymization_flow
    )


def test_two_mode_labels_are_present_in_patch():
    assert "Anonimiseren" in PATCH_TEXT
    assert "Originele waarden terugzetten" in PATCH_TEXT
    assert "Kies werkmodus" in PATCH_TEXT


def test_two_mode_patch_uses_conditional_work_mode_rendering():
    assert "solidprivacy_work_mode = st.radio(" in PATCH_TEXT
    assert '["Anonimiseren", "Originele waarden terugzetten"]' in PATCH_TEXT
    assert 'if solidprivacy_work_mode == "Originele waarden terugzetten":' in PATCH_TEXT
    assert "else:" in PATCH_TEXT
    assert "indent_block(anonymization_flow)" in PATCH_TEXT


def test_generated_two_mode_source_compiles_without_indentation_or_syntax_error():
    # Guards runtime failures in the generated mode branch.
    compile(_generated_two_mode_source_snippet(), "generated_two_mode_source.py", "exec")


def test_reinsert_blocks_start_at_single_branch_indent():
    scrub_key_import_ui_block = _extract_triple_quoted_assignment("scrub_key_import_ui_block")
    reinsert_ui_block = _extract_triple_quoted_assignment("reinsert_ui_block")
    txt_reinsert_ui_block = _extract_triple_quoted_assignment("txt_reinsert_ui_block")
    assert scrub_key_import_ui_block.startswith('    st.markdown("**Scrub Key laden**")')
    assert reinsert_ui_block.startswith('    st.markdown("**Originele waarden terugzetten**")')
    assert txt_reinsert_ui_block.startswith('    st.markdown("**TXT-bestand terugzetten**")')
    assert not scrub_key_import_ui_block.startswith('        st.markdown("**Scrub Key laden**")')
    assert not reinsert_ui_block.startswith('        st.markdown("**Originele waarden terugzetten**")')
    assert not txt_reinsert_ui_block.startswith('        st.markdown("**TXT-bestand terugzetten**")')


def test_reinsert_mode_gets_own_scrub_key_reinsert_and_txt_content():
    mode_index = PATCH_TEXT.index('if solidprivacy_work_mode == "Originele waarden terugzetten":')
    import_index = PATCH_TEXT.index("scrub_key_import_ui_block + reinsert_ui_block + txt_reinsert_ui_block")
    assert mode_index < import_index
    assert "Scrub Key laden" in PATCH_TEXT
    assert "Upload Scrub Key JSON (.json)" in PATCH_TEXT
    assert "Of plak Scrub Key JSON" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT
    assert "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten" in PATCH_TEXT
    assert "Zet originele waarden lokaal terug" in PATCH_TEXT
    assert "Herstelde tekst" in PATCH_TEXT
    assert "Download herstelde tekst (.txt)" in PATCH_TEXT
    assert "Controleverslag terugzetten" in PATCH_TEXT
    assert "TXT-bestand terugzetten" in PATCH_TEXT
    assert "Upload een TXT-bestand met placeholders" in PATCH_TEXT
    assert "Zet TXT-bestand lokaal terug" in PATCH_TEXT
    assert "Herstelde TXT-tekst" in PATCH_TEXT
    assert "Download hersteld TXT-bestand (.txt)" in PATCH_TEXT


def test_anonymization_flow_is_under_else_branch():
    mode_index = PATCH_TEXT.index('if solidprivacy_work_mode == "Originele waarden terugzetten":')
    else_index = PATCH_TEXT.index("'''else:\n'''")
    indent_index = PATCH_TEXT.index("anonymization_flow =")
    assert mode_index < else_index < indent_index
    assert "with st.expander(\"Over deze app\", expanded=False):" in PATCH_TEXT
    assert "st.subheader(\"4. Download opgeschoonde bestanden\")" in PATCH_TEXT
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT


def test_reinsert_flow_is_not_embedded_in_anonymization_review_summary_block():
    review_summary_start = PATCH_TEXT.index("review_summary_block =")
    review_summary_end = PATCH_TEXT.index("text = replace_once(\n    text,\n    '''        st.subheader(\"4. Download opgeschoonde bestanden\")", review_summary_start)
    review_summary_block = PATCH_TEXT[review_summary_start:review_summary_end]
    assert "Scrub Key (JSON)" in review_summary_block
    assert "Download Scrub Key (.json)" in review_summary_block
    assert "scrub_key_import_ui_block" not in review_summary_block
    assert "reinsert_ui_block" not in review_summary_block
    assert "txt_reinsert_ui_block" not in review_summary_block
    assert "Download herstelde tekst (.txt)" not in review_summary_block
    assert "Download hersteld TXT-bestand (.txt)" not in review_summary_block


def test_existing_scrub_key_export_and_import_labels_remain_present():
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "Scrub Key laden" in PATCH_TEXT
    assert "Upload Scrub Key JSON (.json)" in PATCH_TEXT
    assert "Of plak Scrub Key JSON" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT


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


def test_two_mode_patch_does_not_add_docx_or_pdf_reinsert_upload_ui():
    forbidden_markers = [
        "reinsert_docx_bytes",
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
