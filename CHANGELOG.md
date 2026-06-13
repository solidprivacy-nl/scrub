# Changelog — SolidPrivacy Scrub

## WP_SERIAL_REVIEW_UI — Small non-destructive serial review panel in Streamlit

Status: implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `serial_review_panel_ui.py`
- `tests/test_serial_review_ui_patch.py`
- `workpackage_claims/WP_SERIAL_REVIEW_UI.md`
- `handover/workpackages/20260613_1230_serial_review_ui.md`

Files changed:

- `presidio_streamlit.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SERIAL_REVIEW_UI.md`

Summary:

- Added a small helper-driven Streamlit renderer for a non-destructive serial review panel.
- Integrated the panel into `presidio_streamlit.py` directly after the existing replacement table editor.
- The panel uses `review_panel_view_model.py` and shows current item, context card/fallback, counts, warnings and navigation.
- The panel keeps the existing table-first review table as source of truth and fallback.
- Session state is limited to `serial_review_current_index`, `serial_review_current_occurrence_id` and `serial_review_filter_mode`.
- Added static UI/contract guards in `tests/test_serial_review_ui_patch.py`.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector for the checked-out repository.
- Expected checks: `python -m py_compile presidio_streamlit.py`, `python -m py_compile review_panel_view_model.py`, `pytest tests/test_serial_review_ui_patch.py`, `pytest tests/test_review_panel_view_model.py tests/test_serial_review_helper.py tests/test_context_cards.py`, then full `pytest`.
- This changes UI/runtime behavior, so Actions, Hugging Face sync and app verification are required before closeout.

Intentionally not changed:

- No startup source mutation.
- No use of `fix_streamlit_static_highlight_preview.py`.
- No Dockerfile change.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No inline editing.
- No Word/PDF layout rendering.
- No review table mutation.
- No automatic replacement.
- No Scrub Key writes or schema changes.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP_SERIAL_REVIEW_UI_VERIFY — closeout/app verification for the non-destructive serial review panel after green Actions and Hugging Face sync`.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SERIAL_REVIEW_UI_CONTRACT_STATUS_RECONCILE — central status reconciliation for serial review UI contract tests.
- WP_CONTEXT_CARD_STATUS_RECONCILE — central status reconciliation for the context-card helper.
- WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — restored WP43/WP42D contract phrase.
- WP_SERIAL_REVIEW_HELPER — serial review queue helper and tests.
- WP42D-ROLLBACK-CLOSEOUT — working table-first interface restored after failed static highlight preview.
- WP42D-ROLLBACK-REPAIR — static preview source cleanup / HF startup repair.
- WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — repair failing replacement logic and DOCX triage tests.
- WP42D-FIX4 — static highlight preview stale-block cleanup repair.
