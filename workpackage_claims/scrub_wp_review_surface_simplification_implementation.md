# Workpackage Claim — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: completed and app-verified

Start timestamp: 2026-07-03 00:00 UTC
Completion timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Implement calmer MVP review surface

## Scope

Implementation of the review-surface simplification only. Make the normal anonymization review surface calmer and less form-like while preserving review, export, Scrub Key, reinsert, audit and privacy controls.

## Files changed

- side_by_side_review_panel_ui.py
- tests/test_review_copy_polish_ui.py
- tests/test_side_by_side_review_consolidation_dutch_sample.py
- tests/test_side_by_side_review_ui_patch.py
- WORKPACKAGES.md
- CHANGELOG.md
- RELEASE_NOTES.md
- workpackage_claims/scrub_wp_review_surface_simplification_implementation.md

## Files added

- tests/test_review_surface_simplification_implementation.py
- handover/workpackages/20260703_0000_review_surface_simplification_implementation.md

## Validation policy

Visible UI behavior changes require targeted tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Source-level tests were used first and Actions were not used as a debugging loop.

## Validation status

- Source-level implementation tests added.
- Related copy-polish and side-by-side source tests updated.
- PR #12 Tests failed once on stale copy expectations, then passed after a narrow test-expectation fix.
- PR #12 was merged to `main`.
- Main Tests for commit `41cf304` passed.
- GitHub to Hugging Face sync for commit `41cf304` passed.
- App verification passed by coordinator screenshot.

## App verification evidence

Coordinator screenshot confirmed:

- App starts without Script execution error.
- Normal anonymization flow is visible.
- Side-by-side review remains visible.
- `Markeringen tonen` remains visible.
- The calmer review copy is live.
- Manual missed-value entry remains reachable.
- Replacement table remains reachable and leading.
- Step-by-step review remains reachable as optional secondary aid.
- Scrub Key remains separate and warning-protected.
- Primary document downloads remain visible.
- Audit/technical downloads and DOCX hygiene audit remain available.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_review_surface_simplification_implementation.md

## Next recommended step

Do not start broader UI/reinsert/export work without a dedicated workpackage. Recommended next step: decide whether further secondary-control grouping is desired as a separate small package, or return to recall/benchmark follow-up if product UI is good enough for the current MVP pass.
