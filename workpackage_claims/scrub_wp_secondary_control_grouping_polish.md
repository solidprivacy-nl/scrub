# Workpackage Claim — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH — Make secondary review controls calmer

## Scope

Small UI polish for the normal anonymization review surface. Group secondary controls more calmly while preserving side-by-side review, manual missed-value entry, replacement table, step-by-step review, Scrub Key, export/download, audit and DOCX hygiene controls.

## Allowed files

Implementation:

- presidio_streamlit.py

Tests:

- tests/test_secondary_control_grouping_polish.py
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
- workpackage_claims/scrub_wp_secondary_control_grouping_polish.md
- handover/workpackages/YYYYMMDD_HHMM_secondary_control_grouping_polish.md

## Validation policy

Visible UI behavior changes require targeted tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Avoid nested Streamlit expanders. Do not use Actions as a debugging loop.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.
