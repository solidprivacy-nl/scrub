from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
SIDE_BY_SIDE_PATH = REPO_ROOT / "side_by_side_review_panel_ui.py"
DOCX_HYGIENE_PATH = REPO_ROOT / "docx_hygiene_audit_panel_ui.py"
DOCKERFILE_PATH = REPO_ROOT / "Dockerfile"
NESTED_PATCH_PATH = REPO_ROOT / "fix_streamlit_nested_expanders.py"
PDF_PATCH_PATH = REPO_ROOT / "fix_streamlit_pdf_text_reinsert.py"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_review_export_vertical_density_contracts.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def marker(*parts: str) -> str:
    return " ".join(parts)


def assert_contains(text: str, term: str) -> None:
    assert term in text, f"Expected marker missing: {term!r}"


def assert_ordered(text: str, terms: list[str]) -> None:
    positions = []
    for term in terms:
        index = text.find(term)
        assert index >= 0, term
        positions.append(index)
    assert positions == sorted(positions), terms


def app_source() -> str:
    return read(APP_PATH)


def review_source() -> str:
    return "\n".join([read(APP_PATH), read(SIDE_BY_SIDE_PATH)])


def export_audit_source() -> str:
    return "\n".join([read(APP_PATH), read(DOCX_HYGIENE_PATH)])


def test_primary_step_order_remains_input_review_export() -> None:
    assert_ordered(
        app_source(),
        [
            'st.subheader("1. Voeg document of tekst toe")',
            'st.subheader("2. Controleer resultaat")',
            'st.subheader("3. Exporteer resultaat")',
        ],
    )


def test_review_mode_and_side_by_side_controls_remain_available() -> None:
    source = review_source()

    for term in [
        'st.subheader("2. Controleer resultaat")',
        "Basiscontrole",
        "Expertcontrole",
        "Controleweergave",
        "Markeringen tonen",
        "render_side_by_side_review_panel",
        "Brontekst",
        "Verwerkte tekst",
    ]:
        assert_contains(source, term)


def test_manual_missed_value_entry_remains_wired_to_replacement_table() -> None:
    source = app_source()

    for term in [
        "Gemiste waarde toevoegen",
        "build_manual_mask_row",
        "validate_manual_mask_input",
        "Details aanpassen — vervangtabel",
        'key="replacement_editor"',
    ]:
        assert_contains(source, term)


def test_primary_document_downloads_keep_current_labels_filenames_and_types() -> None:
    source = app_source()

    for term in [
        'st.subheader("3. Exporteer resultaat")',
        "Document downloaden",
        "Download opgeschoonde tekst (.txt)",
        "Download opgeschoond Word-bestand (.docx)",
        "Download opgeschoonde PDF (.pdf)",
        "opgeschoonde_tekst.txt",
        "opgeschoonde_tekst.docx",
        "opgeschoond_",
        "opgeschoonde_tekst.pdf",
        'mime="text/plain"',
        'mime="application/pdf"',
        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',
    ]:
        assert_contains(source, term)


def test_scrub_key_remains_separate_and_warning_protected() -> None:
    source = app_source()

    for term in [
        "Scrub Key downloaden",
        "De Scrub Key kan originele waarden herstellen",
        "Download Scrub Key (.json)",
        "solidprivacy_scrub_key.json",
        'mime="application/json"',
    ]:
        assert_contains(source, term)


def test_audit_downloads_and_docx_hygiene_audit_remain_available() -> None:
    source = export_audit_source()

    for term in [
        "Audit en technische bestanden",
        "Download vervangtabel (.csv)",
        "Download scrubrapport (.txt)",
        "DOCX hygiene audit",
        "render_docx_hygiene_audit_panel",
    ]:
        assert_contains(source, term)


def test_no_new_bundle_runtime_or_scope_markers_are_present() -> None:
    source = "\n".join(
        [read(APP_PATH), read(DOCKERFILE_PATH), read(NESTED_PATCH_PATH), read(PDF_PATCH_PATH)]
    ).lower()

    forbidden_terms = [
        marker("cloud", "processing"),
        marker("ai", "document", "processing"),
        marker("new", "recognizers"),
        marker("new", "export", "gates"),
        marker("runtime", "source", "mutation"),
        marker("custom", "html", "component"),
        "full-document editor",
        marker("combined", "export"),
        "exportpakket.zip",
        marker("download", "alles"),
    ]
    for term in forbidden_terms:
        assert term not in source, term


def test_no_new_user_facing_sync_scroll_control_is_added_to_app_source() -> None:
    source = app_source().lower()

    for term in [
        marker("synchronized", "scroll"),
        marker("sync", "scroll"),
        marker("scroll", "synchronisatie"),
        marker("gesynchroniseerd", "scrollen"),
    ]:
        assert term not in source, term


def test_contract_tests_remain_source_level_only() -> None:
    tree = ast.parse(read(THIS_TEST_PATH))
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
