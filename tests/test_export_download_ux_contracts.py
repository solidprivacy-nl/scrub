from __future__ import annotations

import ast
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = REPO_ROOT / "MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md"
CONTRACT_PATH = REPO_ROOT / "EXPORT_DOWNLOAD_UX_CONTRACTS.md"
THIS_TEST_PATH = REPO_ROOT / "tests" / "test_export_download_ux_contracts.py"


def read_doc(path: str | Path) -> str:
    target = REPO_ROOT / path if isinstance(path, str) else path
    return target.read_text(encoding="utf-8")


def normalise(text: str) -> str:
    return " ".join(text.lower().split())


def assert_contains(text: str, term: str) -> None:
    assert normalise(term) in normalise(text), f"Expected to find {term!r}"


def combined_contract_text() -> str:
    return f"{read_doc(PLAN_PATH)}\n{read_doc(CONTRACT_PATH)}"


def test_plan_exists_and_names_target_export_surface():
    assert PLAN_PATH.exists(), "MVP UI cleanup/export redesign plan must exist"
    plan_text = read_doc(PLAN_PATH)

    for term in [
        "Exporteer resultaat",
        "Document downloaden",
        "Scrub Key",
        "Audit en technische bestanden",
    ]:
        assert_contains(plan_text, term)


def test_export_grouping_separates_scrub_key_from_document_downloads():
    plan_text = read_doc(PLAN_PATH)

    document_index = plan_text.index("Document downloaden")
    scrub_key_index = plan_text.index("Scrub Key")
    audit_index = plan_text.index("Audit en technische bestanden")

    assert document_index < scrub_key_index < audit_index, (
        "Export plan must separate normal document downloads, Scrub Key, and audit/technical downloads"
    )
    assert_contains(plan_text, "Scrub Key clearly separated")


def test_primary_and_secondary_export_outputs_are_contractually_separated():
    text = combined_contract_text()

    for term in [
        "Opgeschoonde tekst (.txt)",
        "Word-document (.docx)",
        "PDF (.pdf)",
    ]:
        assert_contains(text, term)

    for term in [
        "Vervangtabel (.csv)",
        "Scrubrapport (.txt)",
        "DOCX hygiene audit",
        "Geavanceerde technische informatie",
    ]:
        assert_contains(text, term)

    assert_contains(text, "Primary/normal document outputs")
    assert_contains(text, "Secondary/audit outputs")


def test_export_semantics_change_is_explicitly_blocked():
    text = combined_contract_text()

    for term in [
        "No export semantics change",
        "filenames",
        "MIME types",
        "payloads",
        "export eligibility",
        "Scrub Key contents",
        "report contents",
    ]:
        assert_contains(text, term)


def test_scrub_key_safety_remains_visible_and_separate():
    text = combined_contract_text()

    for term in [
        "Scrub Key clearly separated",
        "Scrub Key is sensitive",
        "can restore original values",
        "separate warning",
    ]:
        assert_contains(text, term)


def test_audit_and_technical_details_remain_available_as_secondary_layers():
    text = combined_contract_text()

    for term in [
        "Audit and technical details must not disappear",
        "secondary layers",
        "Audit en risico’s",
        "Geavanceerd",
    ]:
        assert_contains(text, term)


def test_debug_prototype_copy_cleanup_direction_is_locked():
    text = combined_contract_text()

    for term in [
        "Serial review — experimentele reviewhulp",
        "Stap voor stap controleren",
        "Download opgeschoonde bestanden",
        "Exporteer resultaat",
        "Technische details bij de vervangtabel",
        "Geavanceerde details bij de vervangtabel",
        "Technische herkenningen",
        "Geavanceerde herkenningsdetails",
    ]:
        assert_contains(text, term)


def test_follow_up_workpackage_sequence_is_locked():
    text = combined_contract_text()

    for term in [
        "WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS",
        "WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION",
        "WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN",
        "WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION",
        "WP_REVIEW_COPY_POLISH_IMPLEMENTATION",
        "WP_MVP_UI_APP_VERIFICATION_CLOSEOUT",
    ]:
        assert_contains(text, term)


def test_this_package_does_not_approve_implementation_or_semantic_changes():
    text = combined_contract_text()

    for term in [
        "No product UI implementation",
        "No Streamlit code",
        "No export semantics change",
        "No Scrub Key",
        "No reinsert",
        "No recognizer",
        "No benchmark gate",
        "No product claim",
    ]:
        assert_contains(text, term)


def test_contract_tests_do_not_import_streamlit_or_mutate_runtime_app_state():
    tree = ast.parse(read_doc(THIS_TEST_PATH))
    imported_roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "presidio_streamlit" not in imported_roots
