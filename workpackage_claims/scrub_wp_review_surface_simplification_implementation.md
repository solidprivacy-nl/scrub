# Workpackage Claim — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Implement calmer MVP review surface

## Scope

Implementation of the review-surface simplification only. Make the normal anonymization review surface calmer and less form-like while preserving review, export, Scrub Key, reinsert, audit and privacy controls.

## Allowed files

Implementation:

- presidio_streamlit.py
- side_by_side_review_panel_ui.py
- serial_review_panel_ui.py

Tests:

- tests/test_review_surface_simplification_contracts.py
- tests/test_review_surface_simplification_implementation.py
- tests/test_review_copy_polish_ui.py
- tests/test_mvp_fast_manual_mask_entry_ui.py
- tests/test_review_table_collapsible_contract.py
- tests/test_export_download_ux_contracts.py
- tests/test_export_download_ux_implementation.py

Documentation/status:

- WORKPACKAGES.md
- CHANGELOG.md
- RELEASE_NOTES.md
- workpackage_claims/scrub_wp_review_surface_simplification_implementation.md
- handover/workpackages/YYYYMMDD_HHMM_review_surface_simplification_implementation.md

## Validation policy

Visible UI behavior changes require targeted tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Use source-level tests first and do not use Actions as a debugging loop.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.
