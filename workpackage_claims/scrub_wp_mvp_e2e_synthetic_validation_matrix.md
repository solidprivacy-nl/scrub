# Workpackage claim — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: completed / ready for PR verification

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 20:20 Europe/Amsterdam

Branch: scrub-mvp-e2e-synthetic-validation-matrix

Dependencies:
- SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT — merged.

Scope:
- Add a versioned synthetic case manifest and pure validation runner for the supported MVP workflow.
- Exercise import, review-row replacement, manual missed-value entry, Scrub Key build/validation, deterministic reinsert, export representations and DOCX hygiene evidence.
- Produce a machine-readable baseline report for the next evidence-driven gap-triage package.

Boundaries:
- Synthetic data only.
- No Streamlit UI changes.
- No recognizer, replacement, export, Scrub Key, reinsert or document-processing semantics changed.
- No external AI, cloud processing, OCR or real personal data.
- Known limitations must be reported, not hidden or converted into production-readiness claims.

Next step:
- Implement manifest, helper, tests and baseline report; validate in GitHub Actions; update governance files and handover.


Validation result:
- Completed at: 2026-07-17 20:20 Europe/Amsterdam
- Cases: 3
- Failing cases: 0
- Evidence gaps/known limitations: 3
- Report: `output/validation/mvp_phase6_synthetic_validation_report.json`
- Handover: `handover/workpackages/20260717_2020_mvp_e2e_synthetic_validation_matrix.md`
- Next package: `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`
