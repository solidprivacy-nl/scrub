from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
POLICY_DOC = REPO_ROOT / "CLEAN_DOCX_EXPORT_POLICY.md"


def _policy_text() -> str:
    return POLICY_DOC.read_text(encoding="utf-8")


def test_policy_forbids_clean_docx_claim_for_current_exports():
    text = _policy_text()
    lowered = text.lower()

    assert "current docx output must not be described as a clean docx export" in lowered
    assert "not allowed yet" in lowered
    assert "clean docx" in lowered
    assert "fully cleaned docx" in lowered
    assert "metadata-free docx" in lowered
    assert "comments removed" in lowered
    assert "tracked changes removed" in lowered


def test_policy_preserves_current_export_semantics_and_no_blocking():
    text = _policy_text()
    lowered = text.lower()

    assert "current export behavior remains unchanged" in lowered
    assert "no export is blocked by wp39" in lowered
    assert "no content is removed by wp39" in lowered
    assert "no export file bytes are changed by wp39" in lowered
    assert "blocking must not be silently added" in lowered
    assert "without a separate workpackage" in lowered


def test_policy_defines_warning_report_rules_for_docx_hygiene_findings():
    text = _policy_text()
    lowered = text.lower()

    assert "no supported hidden-content findings were detected" in lowered
    assert "not a clean-docx guarantee" in lowered
    assert "headers or footers" in lowered
    assert "comments or margin notes" in lowered
    assert "tracked changes can preserve" in lowered
    assert "docx hygiene risk could not be fully assessed" in lowered
    assert "high-risk warning + audit finding" in lowered


def test_policy_sets_minimum_requirements_before_clean_export_claim():
    text = _policy_text()
    lowered = text.lower()

    assert "minimum requirements before a clean-docx claim" in lowered
    assert "explicit clean-export mode" in lowered
    assert "comments, tracked changes, headers and footers" in lowered
    assert "metadata" in lowered
    assert "footnotes" in lowered
    assert "endnotes" in lowered
    assert "custom xml" in lowered
    assert "residual placeholders" in lowered
    assert "no hidden recovery" in lowered
    assert "must not claim a docx export is clean" in lowered


def test_policy_explicitly_does_not_implement_cleaner_or_ui_behavior():
    text = _policy_text()
    lowered = text.lower()

    for required in [
        "does not:",
        "implement a docx cleaner",
        "remove comments",
        "accept or remove tracked changes",
        "remove metadata",
        "block export",
        "change export semantics",
        "change docx reinsert behavior",
        "change streamlit ui",
        "change scrub key schema",
        "add dependencies",
        "add real data",
        "add cloud processing",
    ]:
        assert required in lowered


def test_policy_uses_no_real_personal_data_examples():
    text = _policy_text()

    assert "Jan Jansen" not in text
    assert "Piet de Vries" not in text
    assert "123456782" not in text
    assert "BSN 123" not in text
