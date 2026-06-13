# Changelog — SolidPrivacy Scrub

## WP_REPLACE_LOGIC_UI_IMPLEMENTATION — Small staged/read-only replacement decision companion panel

Status: implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `replacement_decision_panel_ui.py`
- `tests/test_replace_logic_ui_patch.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION.md`
- `handover/workpackages/20260613_1505_replace_logic_ui_implementation.md`

Files changed:

- `serial_review_panel_ui.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION.md`

Summary:

- Added a small staged/read-only replacement decision companion panel.
- The panel uses `replacement_decision.py` helper functions for preview/audit output only.
- The panel is rendered from the existing serial review area, so the existing review table remains source of truth and fallback.
- Added static patch tests for visible boundary text, helper usage, allowed view-only session keys, no review-table/editor mutation, no Scrub Key writes, no export/download calls, no reinsert calls, no fuzzy matching/guessed intent, no startup source mutation and no real-data fixtures.

Validation status:

- No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.
- Expected checks: `python -m py_compile serial_review_panel_ui.py`; `python -m py_compile replacement_decision_panel_ui.py`; `pytest tests/test_replace_logic_ui_patch.py`; `pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py`; then full `pytest`.
- This changes UI/runtime behavior, so Actions, Hugging Face sync and coordinator app verification are required before closeout.

Intentionally not changed:

- No review table mutation.
- No `edited_replacements_df` mutation.
- No Streamlit data-editor mutation.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No mapping persistence.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No fuzzy matching or guessed intent.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_VERIFY — closeout/app verification for replacement decision helper panel` after green Actions and Hugging Face sync.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
- WP28C-CLOSEOUT — Scrub Key warning/reinsert evidence closeout.
- WP_SERIAL_REVIEW_UI_VERIFY — closeout/app verification for non-destructive serial review panel.
- WP_SERIAL_REVIEW_UI — small non-destructive serial review panel in Streamlit.
- WP_SERIAL_REVIEW_UI_CONTRACT_STATUS_RECONCILE — central status reconciliation for serial review UI contract tests.
- WP_CONTEXT_CARD_STATUS_RECONCILE — central status reconciliation for the context-card helper.
- WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — restored WP43/WP42D contract phrase.
- WP_SERIAL_REVIEW_HELPER — serial review queue helper and tests.
- WP42D-ROLLBACK-CLOSEOUT — working table-first interface restored after failed static highlight preview.
- WP42D-ROLLBACK-REPAIR — static preview source cleanup / HF startup repair.
- WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — repair failing replacement logic and DOCX triage tests.
- WP42D-FIX4 — static highlight preview stale-block cleanup repair.
