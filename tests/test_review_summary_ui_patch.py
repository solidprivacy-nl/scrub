from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_review_summary_helper_is_imported_by_streamlit_patch():
    assert "from review_summary import build_review_summary, review_summary_markdown" in PATCH_TEXT


def test_review_summary_is_inserted_before_download_section():
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "final_review_summary = build_review_summary(edited_replacements_df)" in PATCH_TEXT
    assert "review_summary_markdown(final_review_summary)" in PATCH_TEXT


def test_review_summary_patch_keeps_export_guidance_and_download_marker():
    assert "st.subheader(\"4. Download opgeschoonde bestanden\")" in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT


def test_review_summary_patch_does_not_change_export_replacement_application():
    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" not in PATCH_TEXT
    assert "Download opgeschoonde tekst (.txt)" not in PATCH_TEXT
