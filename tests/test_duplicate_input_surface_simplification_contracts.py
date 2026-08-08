from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = REPO_ROOT / "presidio_streamlit.py"
PLAN_PATH = REPO_ROOT / "DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN.md"
DOCKERFILE_PATH = REPO_ROOT / "Dockerfile"
NESTED_PATCH_PATH = REPO_ROOT / "fix_streamlit_nested_expanders.py"
PDF_PATCH_PATH = REPO_ROOT / "fix_streamlit_pdf_text_reinsert.py"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_duplicate_input_surface_simplification_contracts.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def assert_contains(text: str, marker: str) -> None:
    assert marker in text, f"Expected marker missing: {marker!r}"


def assert_ordered(text: str, markers: list[str]) -> None:
    positions = []
    for marker in markers:
        index = text.find(marker)
        assert index >= 0, marker
        positions.append(index)
    assert positions == sorted(positions), markers


def test_plan_exists_and_locks_single_input_surface_target() -> None:
    assert PLAN_PATH.exists(), "Duplicate input surface simplification plan must exist"
    plan_text = read(PLAN_PATH)

    for marker in [
        "single coherent input area",
        "1. Voeg document of tekst toe",
        "2. Controleer resultaat",
        "3. Exporteer resultaat",
        "SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS",
        "SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION",
    ]:
        assert_contains(plan_text, marker)


def test_app_has_one_direct_input_step_heading() -> None:
    app_text = read(APP_PATH)

    assert app_text.count('st.subheader("1. Voeg document of tekst toe")') == 1


def test_step_order_remains_input_review_export() -> None:
    app_text = read(APP_PATH)

    assert_ordered(
        app_text,
        [
            'st.subheader("1. Voeg document of tekst toe")',
            'st.subheader("2. Controleer resultaat")',
            'st.subheader("3. Exporteer resultaat")',
        ],
    )


def test_existing_upload_support_remains_available() -> None:
    app_text = read(APP_PATH)
    app_compact = compact(app_text)

    for marker in [
        "st.file_uploader(",
        "Upload een .txt-, .docx- of tekstgebaseerd .pdf-bestand",
        'type=["txt", "docx", "pdf"]',
        "uploaded_file_to_text(uploaded_file)",
        "uploaded_file_type",
    ]:
        assert_contains(app_text, marker)

    assert_contains(
        app_compact,
        'uploaded_file = st.file_uploader( "Upload een .txt-, .docx- of tekstgebaseerd .pdf-bestand", type=["txt", "docx", "pdf"],',
    )


def test_synthetic_legal_example_support_remains_present() -> None:
    app_text = read(APP_PATH)

    for marker in [
        "Gebruik een synthetisch juridisch testvoorbeeld",
        "get_example_names()",
        "get_example_text(sample_name)",
        "Geen testvoorbeeld laden",
        "EMBEDDED_LEGAL_TEST_CASES",
    ]:
        assert_contains(app_text, marker)


def test_pasted_or_extracted_text_area_remains_present() -> None:
    app_text = read(APP_PATH)

    for marker in [
        "st_text = st.text_area(",
        "Plak tekst of controleer de uit het document gehaalde tekst",
        'key="text_input"',
        "height=240",
    ]:
        assert_contains(app_text, marker)


def test_input_precedence_markers_remain_present() -> None:
    app_text = read(APP_PATH)

    for marker in [
        'st.session_state.get("_premium_cached_text", "".join(demo_text))',
        'else "".join(demo_text)',
        'if sample_name != "Geen testvoorbeeld laden" and uploaded_file is None:',
        "if uploaded_file is not None:",
        "input_text, uploaded_file_type = uploaded_file_to_text(uploaded_file)",
    ]:
        assert_contains(app_text, marker)


def test_review_export_and_scrub_key_surface_remains_present() -> None:
    app_text = read(APP_PATH)

    for marker in [
        "render_side_by_side_review_panel",
        "Basiscontrole",
        "Expertcontrole",
        "Gemiste waarde toevoegen",
        "Details aanpassen — vervangtabel",
        "Document downloaden",
        "Scrub Key downloaden",
        "Audit en technische bestanden",
        "render_docx_hygiene_audit_panel",
    ]:
        assert_contains(app_text, marker)


def test_no_duplicate_input_startup_or_runtime_patch_is_introduced() -> None:
    startup_text = "\n".join(
        [
            read(DOCKERFILE_PATH),
            read(NESTED_PATCH_PATH),
            read(PDF_PATCH_PATH),
        ]
    )
    startup_lower = startup_text.lower()

    for marker in [
        "duplicate_input_surface",
        "single_input_surface_patch",
        "fix_streamlit_duplicate_input",
        "runtime source mutation for duplicate input",
    ]:
        assert marker not in startup_lower

    assert startup_text.count('st.subheader("1. Voeg document of tekst toe")') == 0
    assert startup_text.count("1. Voeg document of tekst toe") == 0


def test_no_prohibited_scope_is_added_to_direct_runtime_surface() -> None:
    direct_runtime_text = "\n".join(
        [
            read(APP_PATH),
            read(DOCKERFILE_PATH),
            read(NESTED_PATCH_PATH),
        ]
    ).lower()

    prohibited_markers = [
        "new ocr",
        "pdf-to-docx reconstruction",
        "cloud processing",
        "ai document processing",
        "new upload backend",
        "new recognizers",
        "new export gates",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
    ]
    for marker in prohibited_markers:
        assert marker not in direct_runtime_text, marker


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


def test_input_controls_are_grouped_under_single_input_surface() -> None:
    app_text = read(APP_PATH)

    input_start = app_text.index('st.subheader("1. Voeg document of tekst toe")')
    review_start = app_text.index('st.subheader("2. Controleer resultaat")')
    input_section = app_text[input_start:review_start]

    assert "with st.container(border=True):" in input_section
    assert input_section.count("st.file_uploader(") == 1
    assert input_section.count("st.text_area(") == 1
    assert "Gebruik een synthetisch juridisch testvoorbeeld" in input_section
    assert "uploaded_file_to_text(uploaded_file)" in input_section
    assert 'type=["txt", "docx", "pdf"]' in input_section
    assert 'key="text_input"' in input_section
