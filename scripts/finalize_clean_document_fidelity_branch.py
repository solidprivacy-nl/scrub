from __future__ import annotations

from pathlib import Path


SELF = Path(__file__)

CHANGELOG_ENTRY = '''## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Purpose:

- Resolve the reproducible DOCX header/footer reinsert fidelity gap from the Phase 6 matrix.
- Preserve DOCX hygiene visibility and explicit unsupported-part boundaries.
- Keep the PDF restored-TXT-only/no-OCR boundary unchanged.

Files added:

- `mvp_document_fidelity_report.py`
- `scripts/run_mvp_document_hygiene_fidelity_report.py`
- `tests/test_mvp_document_hygiene_fidelity_hardening.py`
- `tests/test_mvp_document_fidelity_report.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json`
- `output/validation/mvp_document_fidelity_pr_validation.json`
- `output/validation/mvp_document_fidelity_pr_validation.log`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`

Files changed:

- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `mvp_phase6_document_cases.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`

Implementation result:

- DOCX body paragraphs and tables remain supported.
- `word/header*.xml` and `word/footer*.xml` text nodes are restored deterministically.
- The DOCX reinsert capability copy matches the supported body/table/header/footer scope.
- The synthetic header/footer residual-placeholder finding is resolved: `true`.
- Resolved findings: 1.
- Remaining findings: 1.
- The remaining finding is the explicit PDF restored-TXT-only/no-OCR product boundary.

Intentionally not changed:

- recognizers, thresholds or replacement semantics;
- Scrub Key schema or lifecycle;
- DOCX comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata;
- split-placeholder support across Word text nodes;
- export filenames or MIME types;
- restored PDF or OCR support;
- Streamlit controls/flow, runtime or dependencies; only capability copy was aligned.

Next recommended step:

- After Actions, sync and app verification, start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

'''

WORKPACKAGES_ENTRY = '''## 2026-07-17 22:30 Europe/Amsterdam — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Summary:
- Extended deterministic DOCX reinsert from `word/document.xml` to existing `word/header*.xml` and `word/footer*.xml` text nodes.
- Preserved body/table behavior and unrelated OOXML package parts.
- Aligned existing DOCX reinsert copy with the supported body/table/header/footer scope without adding controls.
- Kept comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata and split placeholders explicitly unsupported.
- Resolved the DOCX header/footer finding and retained the PDF TXT-only/no-OCR boundary.

Validation:
- DOCX header/footer resolution: true.
- Resolved findings: 1.
- Remaining findings: 1.
- Production readiness: false.
- Human review remains required.
- Final clean-branch GitHub Actions validation required before merge.
- Hugging Face sync and live app verification required after merge.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

'''


def prepend_once(path: Path, marker: str, entry: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker not in current:
        path.write_text(entry + current, encoding="utf-8")


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    prepend_once(
        Path("CHANGELOG.md"),
        "## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING",
        CHANGELOG_ENTRY,
    )
    prepend_once(
        Path("WORKPACKAGES.md"),
        "## 2026-07-17 22:30 Europe/Amsterdam — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING",
        WORKPACKAGES_ENTRY,
    )
    claim = Path(
        "workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md"
    )
    replace_once(
        claim,
        "Status: completed / ready for app verification",
        "Status: completed / ready for PR verification",
    )
    replace_once(
        claim,
        "Branch: scrub-mvp-document-hygiene-fidelity-hardening",
        "Branch: scrub-mvp-document-hygiene-fidelity-hardening-clean",
    )
    text = claim.read_text(encoding="utf-8")
    if "Clean branch rebuild:" not in text:
        text += '''\n\nClean branch rebuild:\n- Rebuilt from current `main` after the Hugging Face incident closeout.\n- Historical temporary operator commits are excluded.\n- Final clean-branch validation is required before merge.\n'''
    claim.write_text(text, encoding="utf-8")
    SELF.unlink()


if __name__ == "__main__":
    main()
