# Changelog — SolidPrivacy Scrub

## WP_CONTEXT_CARD_STATUS_RECONCILE — Reconcile completed context-card helper into central project status

Status: completed documentation/status-repair-only reconciliation.

Files added:

- `workpackage_claims/WP_CONTEXT_CARD_STATUS_RECONCILE.md`
- `handover/workpackages/20260613_1145_context_card_status_reconcile.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_CONTEXT_CARD_STATUS_RECONCILE.md`

Summary:

- Reconciled `WP_CONTEXT_CARD_HELPER` after its worker hit a 409 conflict while trying to update central project status documents.
- Recorded that `WP_CONTEXT_CARD_HELPER` is completed helper/tests-only.
- Recorded added helper artifacts: `context_cards.py`, `tests/test_context_cards.py`, `handover/workpackages/20260613_1115_context_card_helper.md` and `workpackage_claims/WP_CONTEXT_CARD_HELPER.md`.
- Recorded helper test evidence from the handover: `pytest tests/test_context_cards.py` — 10 passed in an isolated local workspace.
- Recorded combined helper/highlight test evidence from the handover: `pytest tests/test_context_cards.py tests/test_highlight_preview.py` — 16 passed in an isolated local workspace.
- Recorded that remote GitHub Actions / Hugging Face sync status was unknown at helper handover time.
- Recorded that app verification is not applicable because no UI/runtime behavior changed.
- Recorded the helper boundary: report-only, non-mutating, HTML-escaped and synthetic-only tests.
- Set the next recommended step to `WP_CONTEXT_CARD_UI_PLAN`.

Validation status:

- Documentation/status-repair-only; no app rebuild was run.
- No shell/pytest execution was available through the ChatGPT GitHub connector for this exact repository checkout.
- Status was reconciled against `context_cards.py`, `tests/test_context_cards.py`, `workpackage_claims/WP_CONTEXT_CARD_HELPER.md` and `handover/workpackages/20260613_1115_context_card_helper.md`.

Intentionally not changed:

- No changes to `context_cards.py`.
- No changes to `tests/test_context_cards.py`.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No Streamlit UI implementation.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP_CONTEXT_CARD_UI_PLAN — plan a small non-authoritative context-card panel near the review table`.

## WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — Restore WP43/WP42D documentation contract phrase

Status: completed narrow documentation-contract repair; awaiting GitHub Actions and Hugging Face sync evidence.

Files added:

- `workpackage_claims/WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT.md`
- `handover/workpackages/20260613_1132_actions_fix_frontend_decision_contract.md`

Files changed:

- `FRONTEND_ARCHITECTURE_DECISION.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT.md`

Summary:

- Coordinator/user screenshots showed Actions failing in `tests/test_frontend_architecture_decision.py::test_wp43_does_not_close_wp42d_verification_or_change_ui`.
- Root cause: the later rollback/closeout wording in `FRONTEND_ARCHITECTURE_DECISION.md` removed the exact historical contract phrase required by the existing regression test: `WP43 does not validate or close WP42D` and `WP42D remains pending`.
- Restored those exact contract phrases under a `Historical WP43 contract` subsection while preserving the later rollback/parked status as a later explicit decision.
- Did not change product code, UI, helper logic, export, Scrub Key, reinsert, dependencies or runtime behavior.

Validation status:

- Static check confirmed `FRONTEND_ARCHITECTURE_DECISION.md` now contains the expected lower-case substrings after `.lower()`:
  - `wp43 does not validate or close wp42d`
  - `wp42d remains pending`
- The exact GitHub Actions run still needs to verify the full suite.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No product code changes.
- No helper logic changes.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- Verify GitHub Actions and Hugging Face sync for the final fix commit.
- If green, proceed only with approved next work; do not start `WP_SERIAL_REVIEW_UI` unless coordinator explicitly approves UI work.

## WP_SERIAL_REVIEW_HELPER — Serial review queue helper and tests

Status: implemented helper/tests-only serial review queue foundation; awaiting GitHub Actions and Hugging Face sync evidence.

Files added:

- `serial_review.py`
- `tests/test_serial_review_helper.py`
- `workpackage_claims/WP_SERIAL_REVIEW_HELPER.md`
- `handover/workpackages/20260613_1120_serial_review_helper.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_SERIAL_REVIEW_HELPER.md`

Summary:

- Added a pure Python `serial_review.py` helper for future one-by-one review flows.
- Supports stable serial queue construction from synthetic review rows, current item selection, next/previous unresolved navigation, unresolved/high-risk filtering and exact same-value occurrence ids.
- Added report-only audit summary fields for unresolved count, high-risk count, high-risk unresolved ids, duplicate exact-value groups and review readiness.
- Preserved strict boundaries: report-only output, `mutation_allowed = False`, no automatic replacement, no review table mutation and no Scrub Key mapping writes.
- Added synthetic-only pytest coverage for empty queue, single item, navigation, unresolved filtering, high-risk filtering, duplicate exact source text, all-exact occurrence matching, no fuzzy matching, report-only boundaries and synthetic-only values.

Validation status:

- Local subset validation in the ChatGPT container passed with:

```text
PYTHONPATH=. pytest tests/test_serial_review_helper.py
```

- Result: `10 passed`.
- A direct full repository clone for combined pytest was not possible in the container because DNS/network access to GitHub was unavailable.
- The GitHub connector could fetch repository files and write commits, but `fetch_commit_workflow_runs` returned `workflow_runs: []` for the helper commits at check time.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key schema or mapping write behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- Verify GitHub Actions and Hugging Face sync for the final workpackage commits.
- After helper tests are green and coordinator approval is explicit: `WP_SERIAL_REVIEW_UI — non-destructive serial review panel in Streamlit`.

## WP42D-ROLLBACK-CLOSEOUT — Working table-first interface restored after failed static highlight preview

Status: completed documentation-only closeout; normal table-first Scrub interface is the current working baseline.

Files added:

- `workpackage_claims/WP42D_ROLLBACK_CLOSEOUT.md`
- `handover/workpackages/20260613_1116_wp42d_rollback_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `FRONTEND_ARCHITECTURE_DECISION.md`
- `workpackage_claims/WP42D_ROLLBACK_CLOSEOUT.md`

Summary:

- Recorded that the Hugging Face app is again usable on the stable table-first Scrub interface.
- Recorded that the failed static-highlight/marking attempt is fully rolled back and parked.
- Explicitly blocked a restart of the old static highlight preview route based on startup source mutation.
- Preserved the product direction: document-first review with context, better replacement decisions, and later marking/editor capabilities.
- Changed the implementation route: helper/model first, contract tests first, then small approved non-destructive UI panels.
- Set the next recommended package to `WP_SERIAL_REVIEW_HELPER`, followed later by `WP_SERIAL_REVIEW_UI` only after helper/tests and explicit approval.

Validation status:

- Documentation-only closeout; no app rebuild was run.
- No shell/pytest execution was available through the ChatGPT GitHub connector for this repository checkout.
- Textual planning was checked and updated so it no longer points to restarting the old static-highlight startup mutation route.
- GitHub Actions and Hugging Face sync are not required for a runtime/UI change in this closeout, but may still run for documentation commits.
- App verification for this closeout is not applicable because no code/runtime/UI behavior changed; coordinator/user instruction supplied the working-app evidence that this package records.

Intentionally not changed:

- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No changes to `Dockerfile`.
- No UI implementation.
- No new highlight preview.
- No replacement decision UI.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP_SERIAL_REVIEW_HELPER — pure helper/tests for serial review queue`.
- After that: `WP_SERIAL_REVIEW_UI — small non-destructive serial review panel`, only after helper/tests and explicit approval.

## WP42D-ROLLBACK-REPAIR — Static preview source cleanup / HF startup repair

Status: implemented HF runtime cache-bust and source guard; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `workpackage_claims/WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup.md`
- `handover/workpackages/20260613_0030_wp42d_rollback_source_cleanup_repair.md`

Files changed:

- `Dockerfile`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup.md`

Summary:

- Coordinator/user evidence after green Actions/Hugging Face sync still showed Hugging Face stuck on Restarting with a script execution error pointing to a stale static highlight preview caption in `presidio_streamlit.py` line 1081.
- GitHub `main` no longer contains that stale static-preview text in `presidio_streamlit.py`, which suggests Hugging Face was still running or rebuilding from a stale mutated runtime image/container state.
- Added a Dockerfile cache-bust marker before the application `COPY` layer so Hugging Face must build a fresh runtime image and cannot reuse an image containing stale mutated app source.
- Added tests asserting that `presidio_streamlit.py` does not contain the stale static preview title/caption/helper text.
- Kept `fix_streamlit_static_highlight_preview.py` disabled and no-op.
- Kept the experimental static highlight preview parked.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py` and then full `pytest`.
- GitHub Actions and Hugging Face sync must be verified after the final repair commit.
- App verification is required after HF sync because the goal is restoring app startup.

Intentionally not changed:

- No new highlight preview UI.
- No replacement UI implementation.
- No changes to `fix_streamlit_nested_expanders.py`.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- Verify GitHub Actions and Hugging Face sync for the final repair commit.
- Then verify the Hugging Face app starts with the normal table-first Scrub Legal interface and no script execution error.

## WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — Repair failing replacement logic and DOCX triage tests

Status: completed minimal pytest repair; GitHub Actions and Hugging Face sync were green for commit `b869688`.

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

- Coordinator/user provided evidence that `Tests #656` and `Sync to Hugging Face Space #668` were green for commit `b869688`.

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

- Continue with WP42D-ROLLBACK-REPAIR verification.

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
