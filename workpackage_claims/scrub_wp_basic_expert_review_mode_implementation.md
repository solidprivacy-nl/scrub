# Workpackage Claim — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: completed and app-verified

Start timestamp: 2026-07-03 00:00 UTC
Completion timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION — Implement Basiscontrole / Expertcontrole visibility split

## Scope

Small visible UI implementation of the Basiscontrole / Expertcontrole review mode split. Basiscontrole becomes the default lower-cognitive-load mode; Expertcontrole exposes the fuller current review/audit machinery. Mode switching changes visibility/grouping only.

## Implementation note

The implementation introduces the mode selector in `side_by_side_review_panel_ui.py`, which is the central review surface. It intentionally avoids a broad `presidio_streamlit.py` restructure in this package. This keeps the first implementation safe and visible while preserving all processing and export semantics.

## Files changed

- side_by_side_review_panel_ui.py
- workpackage_claims/scrub_wp_basic_expert_review_mode_implementation.md

## Files added

- tests/test_basic_expert_review_mode_implementation.py
- handover/workpackages/20260703_0000_basic_expert_review_mode_implementation.md

## Documentation sync note

A release-notes update was attempted but blocked by the connector safety layer during full-file replacement. Status is recorded in this claim and handover.

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Do not change processing, export, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency semantics.

## Validation status

- Source-level implementation tests added.
- PR #17 validation passed.
- PR #17 merged to `main`.
- Hugging Face sync completed sufficiently for live Space verification.
- App verification passed by coordinator screenshots.

## App verification evidence

Coordinator screenshots confirmed:

- App starts without Script execution error.
- `Controleweergave` is visible.
- `Basiscontrole` / `Expertcontrole` selector is visible.
- `Basiscontrole` is selected by default.
- `Expertcontrole` can be selected.
- Side-by-side review remains visible in both modes.
- `Markeringen tonen` remains visible.
- Manual missed-value entry remains reachable.
- Replacement table remains reachable.
- Scrub Key, document downloads, audit files, technical details and DOCX hygiene audit remain available.
- No visible export, Scrub Key, reinsert or recognizer regression observed in the verified path.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_basic_expert_review_mode_implementation.md

## Remaining risk

This first implementation introduces the mode selector and explanatory copy, but does not yet fully restructure every downstream secondary control into separate Basic/Expert layouts. A deeper Basic-mode decluttering package should be separate and contract-tested.

## Next recommended step

Start a follow-up package to make Basiscontrole materially cleaner by moving the lower-priority secondary controls behind a smaller `Details aanpassen` / `Meer bestanden` structure while keeping Expertcontrole fully available.
