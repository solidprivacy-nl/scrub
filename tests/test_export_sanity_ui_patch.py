from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_export_sanity_helper_is_imported_by_streamlit_patch():
    assert "from export_sanity import build_export_sanity_checks, export_sanity_warnings" in PATCH_TEXT


def test_export_sanity_block_is_inserted_near_final_review_summary():
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT
    assert "export_sanity_checks = build_export_sanity_checks(edited_replacements_df)" in PATCH_TEXT
    assert "export_sanity_warnings(export_sanity_checks)" in PATCH_TEXT


def test_export_sanity_patch_keeps_download_section_marker_and_export_guidance():
    assert 'st.subheader("4. Download opgeschoonde bestanden")' in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT


def test_export_sanity_patch_does_not_alter_replacement_application():
    assert "apply_replacements_to_text =" not in PATCH_TEXT
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" not in PATCH_TEXT


def test_export_sanity_patch_does_not_remove_download_buttons():
    assert "Download opgeschoonde tekst (.txt)" not in PATCH_TEXT
    assert "Download vervangtabel (.csv)" not in PATCH_TEXT
    assert "Download opgeschoond Word-document (.docx)" not in PATCH_TEXT
    assert "Download opgeschoonde PDF (.pdf)" not in PATCH_TEXT


def test_export_sanity_warning_behavior_is_advisory_and_non_blocking():
    assert "Deze exportcontrole is adviserend" in PATCH_TEXT
    assert "downloads blijven beschikbaar" in PATCH_TEXT
    assert "exportinstellingen blijven ongewijzigd" in PATCH_TEXT
    assert "st.stop(" not in PATCH_TEXT
    assert "raise " not in PATCH_TEXT
    assert "blocks_export" not in PATCH_TEXT
    assert "changes_export_semantics" not in PATCH_TEXT
