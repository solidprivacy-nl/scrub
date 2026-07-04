# Workpackage Claim — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-04 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

## Scope

Visible UI implementation. Make `Basiscontrole` materially cleaner than the first mode-split implementation while preserving full `Expertcontrole`. Mode switching changes visibility/grouping only.

## Allowed files

Implementation:

- presidio_streamlit.py
- side_by_side_review_panel_ui.py

Tests:

- tests/test_basic_mode_declutter_implementation.py
- tests/test_basic_mode_declutter_contracts.py
- tests/test_basic_expert_review_mode_implementation.py
- tests/test_basic_expert_review_mode_contracts.py
- tests/test_review_surface_simplification_implementation.py
- tests/test_secondary_control_grouping_polish_implementation.py
- tests/test_export_download_ux_contracts.py
- tests/test_export_download_ux_implementation.py

Documentation/status:

- RELEASE_NOTES.md
- CHANGELOG.md
- WORKPACKAGES.md
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md
- handover/workpackages/YYYYMMDD_HHMM_basic_mode_declutter_implementation.md

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking, hidden export gate or old replacement decision helper panel.
