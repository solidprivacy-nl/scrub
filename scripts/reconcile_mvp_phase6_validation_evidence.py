from __future__ import annotations

import json
import re
from pathlib import Path


REPORT = Path("output/validation/mvp_phase6_synthetic_validation_report.json")
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
RISK_REGISTER = Path("RISK_REGISTER.md")
CLAIM = Path("workpackage_claims/scrub_wp_mvp_e2e_synthetic_validation_matrix.md")
HANDOVER = Path("handover/workpackages/20260717_2020_mvp_e2e_synthetic_validation_matrix.md")

STAMP = "2026-07-17 20:20 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX"
CHANGELOG_HEADING = f"## 2026-07-17 — {PACKAGE}"
WORKPACKAGES_HEADING = f"## {STAMP} — {PACKAGE}"


def report() -> dict:
    loaded = json.loads(REPORT.read_text(encoding="utf-8"))
    if loaded.get("schema") != "solidprivacy.mvp_phase6_validation_report":
        raise RuntimeError("Unexpected Phase 6 validation report schema")
    return loaded


def categories(data: dict) -> list[str]:
    return sorted(
        {
            str(item.get("category"))
            for item in data.get("evidence_gaps", [])
            if item.get("category")
        }
    )


def prepend_if_heading_missing(path: Path, heading: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if heading not in text:
        path.write_text(entry + text, encoding="utf-8")


def update_changelog(data: dict) -> None:
    gap_categories = ", ".join(categories(data)) or "none"
    entry = f'''{CHANGELOG_HEADING}

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

- Synthetic cases: {data['case_count']}.
- Failing cases: {data['failing_case_count']}.
- Evidence gaps/known limitations: {data['evidence_gap_count']}.
- Gap categories: {gap_categories}.
- Human review required: `{str(data['human_review_required']).lower()}`.
- Production ready: `{str(data['production_ready']).lower()}`.
- Local-only validation: `{str(data['local_only']).lower()}`.
- External AI/cloud/OCR processing: none.

Methodology correction:

- Standard deterministic Presidio email recognition is included alongside the Dutch recognizer pack, preventing a standard e-mail value from being misclassified as a Dutch-pack false negative.

Intentionally not changed:

- Streamlit UI or review controls;
- recognizers or detection thresholds in product code;
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
    prepend_if_heading_missing(CHANGELOG, CHANGELOG_HEADING, entry)


def update_workpackages(data: dict) -> None:
    gap_categories = ", ".join(categories(data)) or "none"
    entry = f'''{WORKPACKAGES_HEADING}

Status: completed / ready for PR verification.

Summary:
- Added a versioned synthetic validation manifest with TXT, DOCX and text-based PDF cases.
- Added pure helper-driven validation for import, review rows, manual additions, replacements, Scrub Key, reinsert, export representation and DOCX hygiene evidence.
- Generated `{REPORT}` as the machine-readable Phase 6 baseline.
- Included deterministic standard email recognition alongside the Dutch pack so evidence categories reflect the supported recognizer surface more accurately.
- Recorded existing DOCX header/footer reinsert and PDF TXT-only limitations as evidence rather than silently accepting or changing them.
- No UI or product recognizer/export/Scrub Key/reinsert/document-processing semantics changed.

Validation:
- Cases: {data['case_count']}.
- Failing cases: {data['failing_case_count']}.
- Evidence gaps: {data['evidence_gap_count']}.
- Categories: {gap_categories}.
- Production-readiness claim: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`.

'''
    prepend_if_heading_missing(WORKPACKAGES, WORKPACKAGES_HEADING, entry)


def update_risk_register(data: dict) -> None:
    text = RISK_REGISTER.read_text(encoding="utf-8")
    pattern = re.compile(
        r"The first machine-readable matrix baseline is stored in "
        r"`output/validation/mvp_phase6_synthetic_validation_report\.json` with "
        r"\d+ synthetic cases and \d+ recorded evidence gaps or known limitations\."
    )
    replacement = (
        "The first machine-readable matrix baseline is stored in "
        "`output/validation/mvp_phase6_synthetic_validation_report.json` with "
        f"{data['case_count']} synthetic cases and {data['evidence_gap_count']} "
        "recorded evidence gaps or known limitations."
    )
    if pattern.search(text):
        text = pattern.sub(replacement, text, count=1)
    else:
        anchor = (
            "Phase 6 now starts with a synthetic end-to-end validation matrix so new fixes are driven by "
            "reproducible false-negative, misclassification and over-masking evidence."
        )
        if anchor not in text:
            raise RuntimeError("R1 Phase 6 evidence anchor not found")
        text = text.replace(anchor, anchor + " " + replacement, 1)
    RISK_REGISTER.write_text(text, encoding="utf-8")


def update_claim(data: dict) -> None:
    claim = CLAIM.read_text(encoding="utf-8")
    claim = re.sub(
        r"^Status: .+$",
        "Status: completed / ready for PR verification",
        claim,
        count=1,
        flags=re.MULTILINE,
    )
    claim = claim.split("\n\nValidation result:", 1)[0].rstrip()
    claim += f'''\n\nValidation result:\n- Completed at: {STAMP}\n- Cases: {data['case_count']}\n- Failing cases: {data['failing_case_count']}\n- Evidence gaps/known limitations: {data['evidence_gap_count']}\n- Report: `{REPORT}`\n- Handover: `{HANDOVER}`\n- Next package: `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`\n'''
    CLAIM.write_text(claim, encoding="utf-8")


def write_handover(data: dict) -> None:
    gap_categories = categories(data)
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
- Python compilation and `git diff --check`.

## Validation status

- Synthetic cases: {data['case_count']}.
- Failing cases: {data['failing_case_count']}.
- Evidence gaps/known limitations: {data['evidence_gap_count']}.
- Categories: {gap_categories}.
- Standard deterministic email recognition is included alongside the Dutch pack.
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
    data = report()
    update_changelog(data)
    update_workpackages(data)
    update_risk_register(data)
    update_claim(data)
    write_handover(data)
    print(
        f"Reconciled {PACKAGE}: {data['case_count']} cases, "
        f"{data['failing_case_count']} failing, "
        f"{data['evidence_gap_count']} evidence gaps."
    )


if __name__ == "__main__":
    main()
