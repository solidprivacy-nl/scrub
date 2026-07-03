# Workpackage Claim — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: implemented / PR validation pending

Start timestamp: 2026-07-03 00:00 UTC
Update timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Implement calmer MVP review surface

## Scope

Implementation of the review-surface simplification only. Make the normal anonymization review surface calmer and less form-like while preserving review, export, Scrub Key, reinsert, audit and privacy controls.

## Files changed

- side_by_side_review_panel_ui.py
- tests/test_review_copy_polish_ui.py
- WORKPACKAGES.md
- RELEASE_NOTES.md
- workpackage_claims/scrub_wp_review_surface_simplification_implementation.md

## Files added

- tests/test_review_surface_simplification_implementation.py
- handover/workpackages/20260703_0000_review_surface_simplification_implementation.md

## Validation policy

Visible UI behavior changes require targeted tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Use source-level tests first and do not use Actions as a debugging loop.

## Validation status

- Source-level implementation tests added.
- Related copy-polish tests updated.
- GitHub Actions: pending after PR.
- Hugging Face sync: pending after merge.
- App verification: pending after Actions and sync are green.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_review_surface_simplification_implementation.md

## Next recommended step

Open PR, review GitHub Actions, merge if green, verify Hugging Face sync, then request coordinator live app verification.
