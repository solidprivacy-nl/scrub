from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACT = (REPO_ROOT / "BASIC_MODE_DECLUTTER_CONTRACTS.md").read_text(encoding="utf-8")
PLAN = (REPO_ROOT / "BASIC_EXPERT_REVIEW_MODE_PLAN.md").read_text(encoding="utf-8")
APP = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
SERIAL = (REPO_ROOT / "serial_review_panel_ui.py").read_text(encoding="utf-8")
DOCX_HYGIENE = (REPO_ROOT / "docx_hygiene_audit_panel_ui.py").read_text(encoding="utf-8")
THIS_TEST = (REPO_ROOT / "tests" / "test_basic_mode_declutter_contracts.py").read_text(encoding="utf-8")


def norm(text: str) -> str:
    return " ".join(text.lower().split())


def contains(text: str, term: str) -> None:
    assert norm(term) in norm(text), f"Expected to find {term!r}"


def test_declutter_contract_document_exists_and_names_next_package() -> None:
    assert "# SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACTS" in CONTRACT
    contains(CONTRACT, "SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION")
    contains(CONTRACT, "Only start implementation after these contract tests are accepted and merged")


def test_basiscontrole_default_and_mode_state_are_protected() -> None:
    combined = CONTRACT + "\n" + PLAN + "\n" + SIDE_BY_SIDE
    for term in [
        "Basiscontrole must remain the default selected review mode",
        "Basiscontrole should become the default user-facing MVP flow",
        "Default: `Basiscontrole`",
        "solidprivacy_review_mode",
    ]:
        contains(combined, term)


def test_basiscontrole_target_surface_is_defined() -> None:
    for term in [
        "1. Voeg document of tekst toe",
        "2. Controleer resultaat",
        "3. Exporteer resultaat / Download veilig",
        "Controleweergave",
        "side-by-side review",
        "Markeringen tonen",
        "replacement count",
        "Gemiste waarde toevoegen",
        "Details aanpassen",
        "primary document downloads",
    ]:
        contains(CONTRACT, term)


def test_basiscontrole_should_not_show_full_expert_stack_as_primary() -> None:
    contains(CONTRACT, "Basiscontrole should avoid showing the full expert expander stack")
    for term in [
        "Waarom controleren?",
        "Extra controlehulpen",
        "Mogelijk extra te controleren waarden",
        "Geavanceerde details bij de vervangtabel",
        "Stap voor stap controleren",
        "Herbruikbare vervangingen",
        "Technische informatie",
        "Geavanceerde herkenningsdetails",
    ]:
        assert term in CONTRACT


def test_expertcontrole_full_controls_remain_available() -> None:
    contains(CONTRACT, "Expertcontrole preservation contract")
    for term in [
        "Waarom controleren?",
        "Gemiste waarde toevoegen",
        "Extra controlehulpen",
        "Mogelijk extra te controleren waarden",
        "Vervangtabel controleren",
        "Geavanceerde details bij de vervangtabel",
        "Stap voor stap controleren",
        "Herbruikbare vervangingen",
        "Scrub Key downloaden",
        "Audit en technische bestanden",
        "DOCX hygiene audit",
        "Technische informatie",
        "Geavanceerde herkenningsdetails",
    ]:
        contains(CONTRACT, term)


def test_mode_switch_must_not_reset_active_document_state() -> None:
    for term in [
        "Switching modes must not reset",
        "uploaded text",
        "uploaded file",
        "recognized replacements",
        "manual additions",
        "replacement decisions",
        "download outputs",
        "session state needed for the active document",
    ]:
        contains(CONTRACT, term)


def test_future_implementation_route_is_defined() -> None:
    for term in [
        "side_by_side_review_state = render_side_by_side_review_panel",
        "review_mode = side_by_side_review_state.get",
        "is_expert_review = review_mode == \"Expertcontrole\"",
        "visibility and grouping only",
    ]:
        contains(CONTRACT, term)


def test_current_source_paths_needed_for_implementation_exist() -> None:
    for term in [
        "render_side_by_side_review_panel",
        "2. Controleer resultaat",
        "Gemiste waarde toevoegen",
        "Vervangtabel controleren",
        "Document downloaden",
        "Scrub Key downloaden",
        "Audit en technische bestanden",
        "render_docx_hygiene_audit_panel",
    ]:
        contains(APP, term)
    for term in ["Basiscontrole", "Expertcontrole", "solidprivacy_review_mode", "Markeringen tonen"]:
        contains(SIDE_BY_SIDE, term)
    contains(SERIAL, "Stap voor stap controleren")
    contains(DOCX_HYGIENE, "DOCX hygiene audit")


def test_nested_expander_pattern_is_not_approved() -> None:
    for term in [
        "Do not introduce nested expanders",
        "must not put existing `st.expander(...)` blocks inside a parent `st.expander(...)`",
        "Do not introduce a parent `Meer controleopties` expander containing other expanders",
    ]:
        contains(CONTRACT, term)


def test_semantic_boundaries_are_locked() -> None:
    for term in [
        "replacement logic",
        "review table data semantics",
        "include/remember/find/replace_with meaning",
        "export content",
        "download filenames",
        "download MIME types",
        "Scrub Key JSON semantics",
        "Scrub Key warning meaning",
        "reinsert behavior",
        "recognizer logic",
        "benchmark logic",
        "DOCX/PDF parsing behavior",
        "runtime/startup behavior",
        "dependencies",
    ]:
        contains(CONTRACT, term)


def test_app_verification_checklist_is_defined_for_later_ui_change() -> None:
    for term in [
        "Basiscontrole is selected by default",
        "Basiscontrole is visibly cleaner than before",
        "Side-by-side review remains visible",
        "Gemiste waarde toevoegen",
        "Expertcontrole exposes the full detailed controls",
        "Primary document downloads remain visible",
        "DOCX hygiene audit remains available when relevant",
        "No visible export, Scrub Key or reinsert regression appears",
    ]:
        contains(CONTRACT, term)


def test_contract_tests_do_not_import_streamlit_or_runtime_app() -> None:
    tree = ast.parse(THIS_TEST)
    imported_roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])
    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
