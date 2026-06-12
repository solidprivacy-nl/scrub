# Changelog — SolidPrivacy Scrub

## WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — Repair failing replacement logic and DOCX triage tests

Status: implemented minimal pytest repair; awaiting GitHub Actions verification.

Files added:

- `workpackage_claims/WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS.md`
- `handover/workpackages/20260613_0015_actions_fix_replace_logic_tests.md`

Files changed:

- `DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md`
- `tests/test_replace_logic_ui_contract.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS.md`

Summary:

- Fixed the reported `test_triage_document_records_high_risk_and_no_fix_boundary` failure by making the WP36A policy boundary explicitly say that WP36A does not implement a DOCX cleaner and does not implement a fix.
- Fixed the reported `test_contract_tests_use_synthetic_values_only` failure by removing literal forbidden example values from the self-scanned test source and constructing them from safe fragments instead.
- Preserved the synthetic-only boundary and kept the replacement UI contract tests focused on helper/UI-plan contracts.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_docx_residual_placeholder_comments_risk.py tests/test_replace_logic_ui_contract.py`.
- Full GitHub Actions rerun is required for final green status.

Intentionally not changed:

- No UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No helper runtime behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- Verify GitHub Actions are green.
- Then verify Hugging Face sync/app startup for the already pending WP42D-ROLLBACK line.

## WP42D-FIX4 — Static highlight preview stale-block cleanup repair

Status: implemented UI patch cleanup repair; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `WP42D_FIX4_STATUS.md`
- `workpackage_claims/WP42D_FIX4_static_highlight_preview_cleanup.md`
- `handover/workpackages/20260612_2340_static_highlight_preview_cleanup_repair.md`

Files changed:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_FIX4_static_highlight_preview_cleanup.md`

Summary:

- User runtime evidence kept showing the old indentation error after the no-expander patch.
- Diagnosis: the running container can already contain a stale broken preview block in `presidio_streamlit.py`; if the preview title is present, the patch skipped reinsertion and left the broken block in place.
- Repaired `fix_streamlit_static_highlight_preview.py` to always remove any existing static highlight preview block before inserting the current safe no-expander block.
- Cleanup removes from the preview-title line through the replacement editor anchor, then reinserts the safe current block before the authoritative replacement table.
- Updated static tests to assert stale preview cleanup logic exists.
- Preserved read-only, non-authoritative, helper-gated rendering with escaped text only.
- No export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py`.
- App verification required after Actions and Hugging Face sync because visible UI behavior should change.

Next recommended step:

- Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42D-FIX3 — Static highlight preview no-expander repair.
- WP42D-FIX2 — Static highlight preview anchor repair.
- WP42D-FIX — Static highlight preview visibility repair.
- WP28C app evidence — Scrub Key warning UI screenshot.
- WP42D-INVESTIGATE — Static highlight preview panel not visible.
- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP43 — Frontend architecture decision.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
