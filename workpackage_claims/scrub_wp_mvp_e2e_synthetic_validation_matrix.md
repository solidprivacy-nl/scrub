# Workpackage claim — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: in_progress

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

Methodology correction in progress:
- The initial evidence run omitted Presidio's standard email recognizer and therefore incorrectly classified a standard e-mail value as a Dutch-pack false negative.
- The validation helper is being corrected before merge; product recognizer code remains unchanged.

Next step:
- Rerun the corrected matrix, regenerate the report, reconcile governance evidence and complete final PR validation.
