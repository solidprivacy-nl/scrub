# Workpackage Claim — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: completed / merged / app-verified

Workpackage title: SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

## Merge

- PR: #19 — SCRUB-WP basic mode declutter implementation
- Merge SHA: c68129b3b179fb2f4e0284a57678b96f9fa64ed7

## Files changed

- presidio_streamlit.py
- tests/test_basic_mode_declutter_implementation.py
- tests/test_execution_interface_simplification_ui.py
- tests/test_review_table_collapsible_contract.py
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md
- handover/workpackages/20260704_1905_basic_mode_declutter_implementation.md

## Validation

- python -m py_compile presidio_streamlit.py: passed locally
- git diff --check: passed locally
- targeted pytest set: 74 passed locally
- PR GitHub Actions Tests: passed after stale test expectation updates

## GitHub Actions / sync / app verification

- GitHub Actions: PR Tests passed and PR #19 merged
- Hugging Face sync: live Space running updated app
- App verification: completed by coordinator screenshots on 2026-07-04

## App verification evidence

Coordinator screenshots confirm:

- app starts without Script execution error;
- Basiscontrole is selected by default;
- side-by-side review remains visible;
- Markeringen tonen remains visible;
- Basiscontrole is visibly cleaner with `Gemiste waarde toevoegen` and `Details aanpassen — vervangtabel` as compact correction paths;
- Expertcontrole exposes the full detailed review/audit stack;
- primary downloads, Scrub Key download, audit downloads and DOCX hygiene audit remain available.

## Boundaries

No replacement, export, Scrub Key, reinsert, recognizer, benchmark, runtime or dependency semantics changed.
