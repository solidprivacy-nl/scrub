from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
HELPER = REPO_ROOT / "manual_mask_entry.py"
THIS_TEST = REPO_ROOT / "tests" / "test_mvp_fast_manual_mask_entry_ui.py"


def _app_text() -> str:
    return APP.read_text(encoding="utf-8")


def _helper_text() -> str:
    return HELPER.read_text(encoding="utf-8")


def test_manual_mask_helper_exists_and_is_streamlit_free():
    assert HELPER.exists()
    helper_text = _helper_text()
    tree = ast.parse(helper_text)
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "build_manual_mask_row" in helper_text
    assert "build_manual_placeholder" in helper_text
    assert "validate_manual_mask_input" in helper_text


def test_app_imports_manual_mask_entry_helper():
    app_text = _app_text()

    assert "from manual_mask_entry import" in app_text
    assert "build_manual_mask_row" in app_text
    assert "build_manual_placeholder" in app_text
    assert "validate_manual_mask_input" in app_text
    assert "manual_mask_document_key" in app_text


def test_manual_mask_entry_ui_is_visible_and_simple():
    app_text = _app_text()

    for phrase in [
        "Gemiste waarde toevoegen",
        "Waarde die alsnog gemaskeerd moet worden",
        "Type gegeven",
        "Vervangen door",
        "Toevoegen aan vervangtabel",
        "Toegevoegd aan de vervangtabel",
    ]:
        assert phrase in app_text


def test_manual_mask_entry_ui_is_near_review_table_before_data_editor():
    app_text = _app_text()

    assert app_text.index('st.subheader("2. Controleer resultaat")') < app_text.index("Gemiste waarde toevoegen")
    assert app_text.index("Gemiste waarde toevoegen") < app_text.index("st.data_editor(")
    assert app_text.index("build_manual_mask_row(") < app_text.index("st.data_editor(")


def test_manual_mask_rows_are_added_to_existing_replacement_table_source_of_truth():
    app_text = _app_text()

    assert "manual_mask_rows" in app_text
    assert "default_editor_rows.append(manual_row)" in app_text
    assert "replacement_editor_df = pd.DataFrame(default_editor_rows)" in app_text
    assert "edited_replacements_df = st.data_editor(" in app_text
    assert "apply_replacements_to_text(st_text, edited_replacements)" in app_text


def test_manual_mask_entry_keeps_export_scrub_key_and_reinsert_semantics_unchanged():
    app_text = _app_text()

    assert "scrub_key_rows = edited_replacements_df.copy()" in app_text
    assert "build_export_scrub_key(scrub_key_rows)" in app_text
    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" in app_text
    assert "reinsert_from_scrub_key" in app_text
    assert "reinsert_docx_bytes" in app_text
    assert "reinsert_txt_bytes" in app_text


def test_manual_mask_entry_does_not_add_blocked_editor_features():
    combined = (_app_text() + "\n" + _helper_text()).lower()

    for forbidden in [
        "rechter muisklik",
        "contextmenu",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "javascript-mutatie",
        "custom document editor",
        "document editor",
        "cloud document processing",
    ]:
        assert forbidden not in combined


def test_manual_mask_entry_tests_use_synthetic_values_only():
    rendered = THIS_TEST.read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "synthetic" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
