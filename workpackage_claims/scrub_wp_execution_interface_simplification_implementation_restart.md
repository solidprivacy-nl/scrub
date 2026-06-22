# Workpackage claim — SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART

repo=solidprivacy-nl/scrub
workpackage=SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART
status=ready_for_pr
branch=scrub-execution-interface-simplification-restart

Scope:
- direct Streamlit UI simplification in `presidio_streamlit.py`
- no startup/runtime patch
- no Dockerfile change
- no export semantics change
- no Scrub Key behavior change
- no reinsert behavior change
- no recognizer/benchmark behavior change
- review table remains source of truth

Validation:
- `tests/test_execution_interface_simplification_ui.py` — 6 passed
- side-by-side / serial review / replace logic UI tests — 37 passed
- export/download contract and implementation tests — 19 passed

Next:
- commit changes
- open PR to `main`
- verify GitHub Actions and Hugging Face sync
- request live app verification
