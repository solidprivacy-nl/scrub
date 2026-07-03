# Workpackage Claim — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION — Implement calmer secondary review controls

## Scope

Small visible UI implementation for grouping secondary controls under `2. Controleer resultaat` more calmly. Preserve side-by-side review, `Markeringen tonen`, manual missed-value entry, replacement table/source of truth, step-by-step review, Scrub Key, export/download, audit and DOCX hygiene controls.

## Allowed files

Implementation:

- presidio_streamlit.py

Tests:

- tests/test_secondary_control_grouping_polish_implementation.py
- tests/test_secondary_control_grouping_polish_contracts.py
- tests/test_review_surface_simplification_implementation.py
- tests/test_mvp_fast_manual_mask_entry_ui.py
- tests/test_review_table_collapsible_contract.py
- tests/test_export_download_ux_contracts.py
- tests/test_export_download_ux_implementation.py

Documentation/status:

- WORKPACKAGES.md
- CHANGELOG.md
- RELEASE_NOTES.md
- workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md
- handover/workpackages/YYYYMMDD_HHMM_secondary_control_grouping_polish_implementation.md

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Avoid nested Streamlit expanders. Do not use Actions as a debugging loop.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.
