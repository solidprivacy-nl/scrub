status: in_progress
repository: solidprivacy-nl/scrub
workpackage title: WP_MVP_FAST_MANUAL_MASK_ENTRY
started timestamp: 2026-06-21 23:16 Europe/Amsterdam
scope: simple MVP helper and UI for adding a manually supplied replacement row to the existing replacement table
boundaries: keep review table as source of truth; keep export, Scrub Key, reinsert, recognizers, benchmark, Docker and runtime behavior unchanged

planned files:
- manual_mask_entry.py
- tests/test_manual_mask_entry.py
- tests/test_mvp_fast_manual_mask_entry_ui.py
- presidio_streamlit.py
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- handover/workpackages/20260621_2316_mvp_fast_manual_mask_entry.md

status notes:
- Keep this package MVP-focused and interface-light.
- Add a simple manual replacement entry near 3. Controleer gevonden gegevens.
- Do not build a custom editor or context-menu interaction in this package.
