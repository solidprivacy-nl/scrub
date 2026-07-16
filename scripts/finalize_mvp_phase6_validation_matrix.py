from __future__ import annotations

import json
from pathlib import Path


REPORT = Path("output/validation/mvp_phase6_synthetic_validation_report.json")
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
RISK_REGISTER = Path("RISK_REGISTER.md")
CLAIM = Path("workpackage_claims/scrub_wp_mvp_e2e_synthetic_validation_matrix.md")
HANDOVER = Path("handover/workpackages/20260717_2020_mvp_e2e_synthetic_validation_matrix.md")

STAMP = "2026-07-17 20:20 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def prepend_once(path: Path, marker: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(entry + text, encoding="utf-8")


def _report() -> dict:
    if not REPORT.exists():
        raise FileNotFoundError(REPORT)
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    if report.get("schema") != "solidprivacy.mvp_phase6_validation_report":
        raise RuntimeError("Unexpected validation report schema")
    return report


def _gap_categories(report: dict) -> list[str]:
    return sorted(
        {
            str(item.get("category"))
            for item in report.get("evidence_gaps", [])
            if item.get("category")
        }
    )


def update_changelog(report: dict) -> None:
    categories = ", ".join(_gap_categories(report)) or "none"
    entry = f'''## 2026-07-17 — {PACKAGE}

Status: completed / ready for PR verification.

Purpose:

- Establish a repeatable synthetic evidence baseline for the supported MVP workflow.
- Exercise TXT, DOCX and text-based PDF paths across import, review-row replacement, manual addition, Scrub Key creation/validation, deterministic reinsert, export representations and audit evidence.
- Record known limitations and reproducible gaps without weakening tests or making production-readiness claims.

Files added:

- `test_cases/mvp_phase6/validation_manifest.json`
- `mvp_phase6_validation_manifest.py`
- `mvp_phase6_detection_matrix.py`
- `mvp_phase6_workflow_core.py`
- `mvp_phase6_document_cases.py`
- `mvp_phase6_validation_report.py`
- `scripts/run_mvp_phase6_validation_matrix.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `{REPORT}`
- `{HANDOVER}`

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

Validation result:

- Synthetic cases: {report['case_count']}.
- Failing cases: {report['failing_case_count']}.
- Evidence gaps/known limitations: {report['evidence_gap_count']}.
- Gap categories: {categories}.
- Human review required: `{str(report['human_review_required']).lower()}`.
- Production ready: `{str(report['production_ready']).lower()}`.
- Local-only validation: `{str(report['local_only']).lower()}`.
- External AI/cloud/OCR processing: none.

Intentionally not changed:

- Streamlit UI or review controls;
- recognizers or detection thresholds;
- replacement semantics;
- export payload, filename or MIME semantics;
- Scrub Key schema or lifecycle behavior;
- reinsert semantics;
- document-processing implementation;
- runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE` and classify the report evidence before implementing any fix.

---

'''
    prepend_once(CHANGELOG, PACKAGE, entry)


def update_workpackages(report: dict) -> None:
    categories = ", ".join(_gap_categories(report)) or "none"
    entry = f'''## {STAMP} — {PACKAGE}

Status: completed / ready for PR verification.

Summary:
- Added a versioned synthetic validation manifest with TXT, DOCX and text-based PDF cases.
- Added pure helper-driven validation for import, review rows, manual additions, replacements, Scrub Key, reinsert, export representation and DOCX hygiene evidence.
- Generated `{REPORT}` as the machine-readable Phase 6 baseline.
- Recorded existing DOCX header/footer reinsert and PDF TXT-only limitations as evidence rather than silently accepting or changing them.
- No UI, recognizer, export, Scrub Key, reinsert or document-processing semantics changed.

Validation:
- Cases: {report['case_count']}.
- Failing cases: {report['failing_case_count']}.
- Evidence gaps: {report['evidence_gap_count']}.
- Categories: {categories}.
- Production-readiness claim: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`.

'''
    prepend_once(WORKPACKAGES, f"{STAMP} — {PACKAGE}", entry)


def update_risk_register(report: dict) -> None:
    text = RISK_REGISTER.read_text(encoding="utf-8")

    r1_old = (
        "Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, "
        "PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple "
        "manual missed-value entry that adds user-supplied values to the existing replacement table. Phase 6 "
        "now starts with a synthetic end-to-end validation matrix so new fixes are driven by reproducible "
        "false-negative, misclassification and over-masking evidence."
    )
    r1_new = r1_old + (
        f" The first machine-readable matrix baseline is stored in `{REPORT}` with "
        f"{report['case_count']} synthetic cases and {report['evidence_gap_count']} recorded evidence gaps or known limitations."
    )
    if r1_new not in text:
        text = replace_once(text, r1_old, r1_new, "R1 validation evidence")

    r4_old = (
        "DOCX hygiene audit remains report-only. Export grouping keeps audit details available and does not imply "
        "a clean-DOCX guarantee. The review debug collapse line explicitly keeps audit details available rather than removing them."
    )
    r4_new = r4_old + (
        " The Phase 6 synthetic DOCX case now records header/footer findings and the existing main-document-only "
        "reinsert boundary as reproducible evidence for the document-hygiene hardening package."
    )
    if r4_new not in text:
        text = replace_once(text, r4_old, r4_new, "R4 validation evidence")

    r7_old = "PDF limitations must remain clear in export/reinsert copy."
    r7_new = (
        r7_old
        + " The Phase 6 text-based PDF case verifies the current restored-TXT-only path and explicitly records that restored PDF and OCR are unsupported."
    )
    if r7_new not in text:
        text = replace_once(text, r7_old, r7_new, "R7 validation evidence")

    r9_old = (
        "Current mitigations include diagnostic benchmark work, preservation guidance, PERSON-name contract/helper work "
        "and a verified manual missed-value entry path. Benchmark follow-up is temporarily parked for UI/export work "
        "unless a concrete blocker appears."
    )
    r9_new = (
        "Current mitigations include diagnostic benchmark work, preservation guidance, PERSON-name contract/helper work "
        "and a verified manual missed-value entry path. The Phase 6 synthetic matrix is now the evidence source for "
        "`SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`; only reproducible under-detection, misclassification or role-over-masking "
        "findings may open a subsequent fix package."
    )
    if r9_new not in text:
        text = replace_once(text, r9_old, r9_new, "R9 active evidence line")

    RISK_REGISTER.write_text(text, encoding="utf-8")


def update_claim(report: dict) -> None:
    claim = CLAIM.read_text(encoding="utf-8")
    claim = claim.replace(
        "Status: in_progress",
        "Status: completed / ready for PR verification",
        1,
    )
    if "Validation result:" not in claim:
        claim += f'''\n\nValidation result:\n- Completed at: {STAMP}\n- Cases: {report['case_count']}\n- Failing cases: {report['failing_case_count']}\n- Evidence gaps/known limitations: {report['evidence_gap_count']}\n- Report: `{REPORT}`\n- Handover: `{HANDOVER}`\n- Next package: `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`\n'''
    CLAIM.write_text(claim, encoding="utf-8")


def write_handover(report: dict) -> None:
    categories = _gap_categories(report)
    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(
        f'''# Handover — {PACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{PACKAGE}

## Status

Completed / ready for PR verification.

## Files added

- `test_cases/mvp_phase6/validation_manifest.json`
- `mvp_phase6_validation_manifest.py`
- `mvp_phase6_detection_matrix.py`
- `mvp_phase6_workflow_core.py`
- `mvp_phase6_document_cases.py`
- `mvp_phase6_validation_report.py`
- `scripts/run_mvp_phase6_validation_matrix.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `{REPORT}`
- `{HANDOVER}`

## Files changed

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

## Tests

- New focused Phase 6 matrix tests.
- Existing Dutch legal recall-gap tests.
- Existing Scrub Key model, reinsert and document-reinsert tests.
- Existing DOCX hygiene and document-tool guardrails selected by CI.
- Python compilation and `git diff --check`.

## Validation status

- Synthetic cases: {report['case_count']}.
- Failing cases: {report['failing_case_count']}.
- Evidence gaps/known limitations: {report['evidence_gap_count']}.
- Categories: {categories}.
- Report schema is machine-readable and deterministic.
- Human review remains required.
- Production readiness is explicitly false.

## GitHub Actions status

Pending final PR validation.

## Hugging Face sync status

Not functionally relevant; no app code or UI changed.

## App verification status

Not applicable.

## Remaining risks

- Detection evidence is a bounded synthetic baseline, not a production recall/precision benchmark.
- DOCX header/footer reinsert remains outside the current document-reinsert helper scope.
- PDF reinsert remains restored TXT only; no restored PDF and no OCR.
- Evidence gaps require classification before any implementation package is opened.

## Next recommended step

Start `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE` using `{REPORT}` as the source evidence.
''',
        encoding="utf-8",
    )


def main() -> None:
    report = _report()
    update_changelog(report)
    update_workpackages(report)
    update_risk_register(report)
    update_claim(report)
    write_handover(report)
    print(
        f"Finalized {PACKAGE}: {report['case_count']} cases, "
        f"{report['failing_case_count']} failing, "
        f"{report['evidence_gap_count']} evidence gaps."
    )


if __name__ == "__main__":
    main()
