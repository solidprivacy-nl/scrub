# Workpackage Claim — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: implemented / PR validation pending

Start timestamp: 2026-07-03 00:00 UTC
Update timestamp: 2026-07-03 00:00 UTC

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
- PR validation pending.
- Hugging Face sync pending after merge.
- App verification required after merge/sync.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_basic_expert_review_mode_implementation.md

## Next recommended step

Open PR, validate GitHub Actions, merge if green, verify Hugging Face sync, then request coordinator live app verification.
