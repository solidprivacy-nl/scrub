# Workpackage Claim — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: ready_for_pr / implementation complete, app verification pending

Workpackage title: SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

Files changed:
- presidio_streamlit.py
- tests/test_basic_mode_declutter_implementation.py
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md
- handover/workpackages/20260704_1905_basic_mode_declutter_implementation.md

Validation:
- python -m py_compile presidio_streamlit.py: passed
- git diff --check: passed
- targeted pytest set: 74 passed

GitHub Actions: pending PR
Hugging Face sync: pending merge to main
App verification: pending after sync

Boundaries:
No replacement, export, Scrub Key, reinsert, recognizer, benchmark, runtime or dependency semantics changed.
