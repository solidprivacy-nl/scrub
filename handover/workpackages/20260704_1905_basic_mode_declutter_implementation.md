# Handover — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

Status: implementation complete; ready for PR validation; app verification pending.

Files added:
- tests/test_basic_mode_declutter_implementation.py
- handover/workpackages/20260704_1905_basic_mode_declutter_implementation.md

Files changed:
- presidio_streamlit.py
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md

Tests/checks:
- python -m py_compile presidio_streamlit.py
- git diff --check
- targeted pytest set: 74 passed

Validation status:
Source-level validation passed. PR validation still required.

GitHub Actions status:
Pending PR.

Hugging Face sync status:
Pending merge to main.

App verification status:
Pending after Hugging Face sync.

Remaining risks:
- Requires PR Actions confirmation.
- Requires Hugging Face sync confirmation after merge.
- Requires live app verification that Basiscontrole is visibly cleaner and Expertcontrole still exposes full review/audit controls.

Next recommended step:
Open PR from scrub-basic-mode-declutter-implementation to main with title:
SCRUB-WP basic mode declutter implementation
