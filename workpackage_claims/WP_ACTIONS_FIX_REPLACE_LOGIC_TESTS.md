# Workpackage claim — WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS

Status: in_progress
Repository: solidprivacy-nl/scrub
Workpackage: WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — Repair failing replacement logic and DOCX triage tests
Started: 2026-06-13

## Scope

Fix only the two failing pytest failures reported by GitHub Actions:

- tests/test_docx_residual_placeholder_comments_risk.py::test_triage_document_records_high_risk_and_no_fix_boundary
- tests/test_replace_logic_ui_contract.py::test_contract_tests_use_synthetic_values_only

## Boundaries

- No UI implementation.
- No changes to presidio_streamlit.py.
- No changes to fix_streamlit_nested_expanders.py.
- No export/download behavior changes.
- No Scrub Key behavior changes.
- No reinsert behavior changes.
- No dependency changes.
- No cloud processing.
- No real-data fixtures.
