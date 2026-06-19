status: in_progress
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION
started timestamp: 2026-06-19 10:05 Europe/Amsterdam
scope: small UI implementation to collapse/rename debug-like review elements
boundaries: no new review layer, no benchmark, no export changes, no Scrub Key changes, no reinsert changes, no recognizer changes, no Docker/runtime changes

planned files:
- presidio_streamlit.py
- serial_review_panel_ui.py
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- handover/workpackages/20260619_1005_review_debug_elements_collapse_implementation.md

status notes:
- Keep this package interface-focused.
- Do not add a new plan/review/safeguard loop.
- Serial review may be collapsed by wrapping the existing renderer in an expander; behavior must stay unchanged.
