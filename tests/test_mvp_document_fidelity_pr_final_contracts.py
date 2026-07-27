from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIDELITY_HEADING = "## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"
FIDELITY_WORKPACKAGE_HEADING = (
    "## 2026-07-17 22:30 Europe/Amsterdam — "
    "SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"
)


def _heading_section(text: str, heading: str) -> str:
    start = text.index(heading)
    next_heading = text.find("\n## ", start + len(heading))
    return text[start:] if next_heading < 0 else text[start:next_heading]


def test_temporary_document_fidelity_patch_scripts_are_absent() -> None:
    assert not (ROOT / "scripts" / "patch_docx_reinsert_capability_copy_only.py").exists()
    assert not (ROOT / "scripts" / "finalize_mvp_document_fidelity_pr_cleanup.py").exists()


def test_document_fidelity_governance_evidence_has_no_duplicate_lines() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    workpackages = (ROOT / "WORKPACKAGES.md").read_text(encoding="utf-8")
    handover = (
        ROOT
        / "handover"
        / "workpackages"
        / "20260717_2230_mvp_document_hygiene_fidelity_hardening.md"
    ).read_text(encoding="utf-8")

    changelog_section = _heading_section(changelog, FIDELITY_HEADING)
    workpackage_section = _heading_section(
        workpackages,
        FIDELITY_WORKPACKAGE_HEADING,
    )

    assert changelog_section.count("- `tests/test_mvp_document_fidelity_ui_copy.py`") == 1
    assert changelog_section.count(
        "The DOCX reinsert capability copy matches the supported body/table/header/footer scope."
    ) == 1
    assert workpackage_section.count(
        "Aligned existing DOCX reinsert copy with the supported body/table/header/footer scope without adding controls."
    ) == 1
    assert handover.count("- `tests/test_mvp_document_fidelity_ui_copy.py`") == 1
    assert handover.count("- Capability-copy contract tests.") == 1


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
