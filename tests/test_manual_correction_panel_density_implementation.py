from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_manual_correction_panel_density_implementation.py"


def app_source() -> str:
    return APP_PATH.read_text(encoding="utf-8")


def test_manual_correction_expander_stays_collapsed_and_has_compact_copy() -> None:
    source = app_source()
    assert 'with st.expander("Gemiste waarde toevoegen", expanded=False):' in source
    assert 'st.caption("Voeg een gemiste waarde rechtstreeks toe aan de vervangtabel.")' in source
    assert 'st.markdown("**Gemiste waarde toevoegen**")' not in source


def test_manual_correction_inputs_are_grouped_in_one_compact_row() -> None:
    source = app_source()
    assert "value_col, type_col, replacement_col = st.columns([2.0, 1.1, 1.6])" in source
    for marker in ["with value_col:", "with type_col:", "with replacement_col:"]:
        assert marker in source
    for label in ["Waarde die alsnog gemaskeerd moet worden", "Type gegeven", "Vervangen door"]:
        assert label in source


def test_existing_form_identity_and_action_are_preserved() -> None:
    source = app_source()
    assert 'with st.form("manual_mask_entry_form", clear_on_submit=True):' in source
    assert "manual_submit = st.form_submit_button(" in source
    assert '"Toevoegen aan vervangtabel"' in source
    assert "use_container_width=True" in source


def test_existing_manual_mask_behavior_markers_are_preserved() -> None:
    source = app_source()
    for marker in [
        "manual_value",
        "manual_type_label",
        "manual_placeholder",
        "manual_replace_with",
        "manual_submit",
        "build_manual_placeholder(",
        "validate_manual_mask_input(",
        "build_manual_mask_row(",
        "manual_mask_document_key(",
        'st.session_state["manual_mask_rows"]',
        "st.rerun()",
    ]:
        assert marker in source


def test_validation_block_stays_after_manual_submit() -> None:
    source = app_source()
    submit_index = source.index("if manual_submit:")
    validation_index = source.index("validate_manual_mask_input(", submit_index)
    row_index = source.index("build_manual_mask_row(", validation_index)
    rerun_index = source.index("st.rerun()", row_index)
    assert submit_index < validation_index < row_index < rerun_index


def test_implementation_test_is_source_level_only() -> None:
    tree = ast.parse(THIS_TEST_PATH.read_text(encoding="utf-8"))
    imported_roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])
    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
