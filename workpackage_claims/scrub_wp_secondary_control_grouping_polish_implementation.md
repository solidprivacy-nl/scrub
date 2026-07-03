# Workpackage Claim — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: implemented / PR validation pending

Start timestamp: 2026-07-03 00:00 UTC
Update timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION — Implement calmer secondary review controls

## Scope

Small visible UI implementation for grouping secondary controls under `2. Controleer resultaat` more calmly. Preserve side-by-side review, `Markeringen tonen`, manual missed-value entry, replacement table/source of truth, step-by-step review, Scrub Key, export/download, audit and DOCX hygiene controls.

## Implementation note

The implementation uses a visible `Meer controleopties` grouping cue below the side-by-side review instead of a parent expander. This avoids nested Streamlit expanders while still making the secondary-control stack feel grouped and intentional.

## Files changed

- side_by_side_review_panel_ui.py
- CHANGELOG.md
- RELEASE_NOTES.md
- workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md

## Files added

- tests/test_secondary_control_grouping_polish_implementation.py
- handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Avoid nested Streamlit expanders. Do not use Actions as a debugging loop.

## Validation status

- Source-level implementation tests added.
- PR validation pending.
- Hugging Face sync pending after merge.
- App verification pending after merge/sync.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md

## Next recommended step

Open PR, review GitHub Actions, merge if green, verify Hugging Face sync, then request coordinator live app verification.
