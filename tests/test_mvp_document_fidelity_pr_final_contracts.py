from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIDELITY_HEADING = "## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"
D030_HEADING = "## D030 — 2026-07-17 — Supported DOCX reinsert includes body, tables, headers and footers"


def _heading_section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_heading = text.find("\n## ", start + len(heading))
    return text[start:] if next_heading < 0 else text[start:next_heading]


def test_temporary_document_fidelity_patch_scripts_are_absent() -> None:
    assert not (ROOT / "scripts" / "patch_docx_reinsert_capability_copy_only.py").exists()
    assert not (ROOT / "scripts" / "finalize_mvp_document_fidelity_pr_cleanup.py").exists()


def test_document_fidelity_history_is_preserved_and_current_scope_remains_bound() -> None:
    archived_changelog = (
        ROOT / "history" / "CHANGELOG_PRE_CONVERGENCE_20260904.md"
    ).read_text(encoding="utf-8")
    decisions = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    handover = (
        ROOT
        / "handover"
        / "workpackages"
        / "20260717_2230_mvp_document_hygiene_fidelity_hardening.md"
    ).read_text(encoding="utf-8")

    archived_section = _heading_section(archived_changelog, FIDELITY_HEADING)
    d030 = _heading_section(decisions, D030_HEADING)

    assert archived_section.count("- `tests/test_mvp_document_fidelity_ui_copy.py`") == 1
    assert archived_section.count(
        "The DOCX reinsert capability copy matches the supported body/table/header/footer scope."
    ) == 1
    assert handover.count("- `tests/test_mvp_document_fidelity_ui_copy.py`") == 1
    assert handover.count("- Capability-copy contract tests.") == 1

    # Current product authority lives in D030, not in a historical WORKPACKAGES slot.
    assert "body, tables, headers and footers" in d030
    assert "word/document.xml" in d030
    assert "word/header*.xml" in d030
    assert "word/footer*.xml" in d030
    assert "comments" in d030
    assert "footnotes/endnotes" in d030


def test_final_claim_preserves_verification_and_product_boundaries() -> None:
    claim = (
        ROOT
        / "workpackage_claims"
        / "scrub_wp_mvp_document_hygiene_fidelity_hardening.md"
    ).read_text(encoding="utf-8")

    assert "DOCX header/footer reinsert resolved: true" in claim
    assert "No OCR or restored-PDF implementation" in claim
    assert "Status: completed and app-verified" in claim
    assert "App verification passed after Actions and Hugging Face sync" in claim
