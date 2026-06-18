from __future__ import annotations

import ast
from pathlib import Path

from fix_streamlit_export_download_ux import apply_export_download_ux_patch


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
PATCH_PATH = REPO_ROOT / "fix_streamlit_export_download_ux.py"
DOCKERFILE_PATH = REPO_ROOT / "Dockerfile"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_export_download_ux_implementation.py"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalise(text: str) -> str:
    return " ".join(text.lower().split())


def patched_app_source() -> str:
    return apply_export_download_ux_patch(read_text(APP_PATH))


def assert_contains(text: str, term: str) -> None:
    assert normalise(term) in normalise(text), f"Expected to find {term!r}"


def test_export_section_title_is_product_like_after_startup_patch():
    source = patched_app_source()

    assert_contains(source, "5. Exporteer resultaat")
    assert "st.subheader(\"5. Download opgeschoonde bestanden\")" not in source


def test_export_groups_are_visible_after_startup_patch():
    source = patched_app_source()

    for term in [
        "Document downloaden",
        "Scrub Key",
        "Audit en technische bestanden",
    ]:
        assert_contains(source, term)


def test_scrub_key_warning_is_present_after_startup_patch():
    source = patched_app_source()

    assert_contains(source, "De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.")
    assert_contains(source, "Download Scrub Key (.json)")


def test_existing_download_concepts_remain_available_after_startup_patch():
    source = patched_app_source()

    for term in [
        "Download opgeschoonde tekst",
        "Download opgeschoond Word-bestand",
        "Download opgeschoonde PDF",
        "Vervangtabel downloaden",
        "Scrubrapport downloaden",
    ]:
        assert_contains(source, term)


def test_export_payload_filenames_and_mime_types_remain_unchanged_after_startup_patch():
    source = patched_app_source()

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


def test_no_new_bundle_or_zip_export_wording_is_introduced():
    source = normalise(patched_app_source())

    for forbidden_term in [
        "exportpakket.zip",
        "download alles",
        "download gekozen bestanden",
        "bundled package",
        "combined export",
    ]:
        assert forbidden_term not in source


def test_docx_hygiene_audit_remains_available_outside_nested_audit_expander():
    source = patched_app_source()

    assert "render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)" in source
    assert_contains(source, "Audit en technische bestanden")


def test_startup_patch_is_part_of_hugging_face_start_command():
    dockerfile = read_text(DOCKERFILE_PATH)

    assert "python fix_streamlit_export_download_ux.py" in dockerfile
    assert dockerfile.index("python fix_streamlit_nested_expanders.py") < dockerfile.index(
        "python fix_streamlit_export_download_ux.py"
    )
    assert dockerfile.index("python fix_streamlit_export_download_ux.py") < dockerfile.index(
        "streamlit run presidio_streamlit.py"
    )


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


def test_patch_module_does_not_import_streamlit_or_change_runtime_state_directly():
    tree = ast.parse(read_text(PATCH_PATH))
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
