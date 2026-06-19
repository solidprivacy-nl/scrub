from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
DOCKERFILE_PATH = REPO_ROOT / "Dockerfile"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_export_download_ux_implementation.py"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalise(text: str) -> str:
    return " ".join(text.lower().split())


def assert_contains(text: str, term: str) -> None:
    assert normalise(term) in normalise(text), f"Expected to find {term!r}"


def test_direct_app_source_has_new_export_title():
    source = read_text(APP_PATH)

    assert_contains(source, 'st.subheader("5. Exporteer resultaat")')
    assert 'st.subheader("5. Download opgeschoonde bestanden")' not in source


def test_export_groups_exist_in_direct_app_source():
    source = read_text(APP_PATH)

    for term in [
        "Document downloaden",
        "Scrub Key",
        "Audit en technische bestanden",
    ]:
        assert_contains(source, term)


def test_scrub_key_warning_is_present_in_direct_app_source():
    source = read_text(APP_PATH)

    assert_contains(source, "De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.")
    assert_contains(source, "Download Scrub Key (.json)")


def test_existing_download_concepts_remain_available():
    source = read_text(APP_PATH)

    for term in [
        "Download opgeschoonde tekst",
        "Download opgeschoond Word-bestand",
        "Download opgeschoonde PDF",
        "Vervangtabel downloaden",
        "Scrubrapport downloaden",
        "Download Scrub Key",
    ]:
        assert_contains(source, term)


def test_existing_filenames_and_mime_types_remain_present():
    source = read_text(APP_PATH)

    for term in [
        "opgeschoonde_tekst.txt",
        "opgeschoonde_tekst.docx",
        "opgeschoond_",
        "opgeschoonde_tekst.pdf",
        "vervangtabel.csv",
        "scrubrapport.txt",
        "solidprivacy_scrub_key.json",
        "text/plain",
        "text/csv",
        "application/pdf",
        "application/json",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]:
        assert_contains(source, term)


def test_dockerfile_no_longer_runs_export_startup_patch():
    dockerfile = read_text(DOCKERFILE_PATH)

    assert "fix_streamlit_export_download_ux.py" not in dockerfile
    assert (
        "python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py"
        in dockerfile
    )


def test_no_bundle_or_zip_export_was_introduced():
    source = normalise(read_text(APP_PATH))

    for forbidden_term in [
        "exportpakket.zip",
        "download alles",
        "download gekozen bestanden",
        "bundled package",
        "combined export",
    ]:
        assert forbidden_term not in source


def test_docx_hygiene_audit_remains_available_outside_technical_expander():
    source = read_text(APP_PATH)

    assert "render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)" in source
    assert_contains(source, "Audit en technische bestanden")


def test_implementation_test_does_not_import_streamlit_or_runtime_app():
    tree = ast.parse(read_text(THIS_TEST_PATH))
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
