# Changelog — SolidPrivacy Scrub

## WP42D-VERIFY — Static highlight preview UI verification closeout

Status: verification attempted; blocked pending Actions/HF/app evidence.

Files added:

- `WP42D_VERIFY_STATUS.md`
- `workpackage_claims/WP42D_VERIFY_static_highlight_preview_ui_closeout.md`
- `handover/workpackages/20260612_1945_static_highlight_preview_ui_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_VERIFY_static_highlight_preview_ui_closeout.md`

Summary:

- Checked for an existing WP42D-VERIFY claim before starting; none existed.
- Created a WP42D-VERIFY claim before changing shared docs.
- Confirmed connector-visible WP42D files exist: `fix_streamlit_static_highlight_preview.py`, `tests/test_static_highlight_preview_ui_integration_patch.py` and `Dockerfile`.
- Confirmed connector-visible patch boundaries: read-only, non-authoritative, helper-gated rendering, escaped text rendering and no export/Scrub Key/reinsert mutation in the patch text.
- Confirmed connector-visible Dockerfile patch order: existing patches run before `fix_streamlit_static_highlight_preview.py`, which runs before `streamlit run`.
- GitHub combined status returned no statuses.
- Workflow run lookup returned no workflow runs.
- App verification remains required because WP42D changed UI behavior.

Validation status:

- Verification artifact added.
- Actions/HF/app status not confirmed by connector.
- No code, UI, tests, runtime behavior, export/download behavior, Scrub Key behavior, reinsert behavior, cloud processing or real data changed.

Next recommended step:

- Coordinator/user evidence needed for WP42D Actions/HF sync and app verification.

## WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration

Status: completed tests/documentation-only.

Files added:

- `tests/test_replace_logic_ui_contract.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_TESTS_replacement_decision_integration.md`
- `handover/workpackages/20260612_2145_replace_logic_ui_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_TESTS_replacement_decision_integration.md`

Summary:

- Checked for an existing claim before starting; none existed.
- Added contract tests mapping planned Dutch UI actions to supported `replacement_decision.py` review states.
- Added contract tests mapping planned scope labels to supported helper scopes.
- Tested exact and normalized affected-occurrence behavior through `matching_occurrence_ids(...)`.
- Tested `build_replacement_audit(...)` report-only/export-readiness behavior.
- Locked boundaries from `REPLACE_LOGIC_UI_PLAN.md`: no UI implementation, no export blocking, no Scrub Key behavior change, no click-to-mark implementation, existing table remains fallback/control surface.
- Used synthetic values only.
- No Streamlit UI, review table behavior, export/download behavior, Scrub Key behavior, reinsert behavior, helper runtime behavior, dependency, cloud processing or real data changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added contract tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Next recommended step:

- `WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout` for the already implemented static highlight preview UI.
- Alternative after verification: `WP43 — Frontend architecture decision`.

## WP42D — Static highlight preview UI integration

Status: implemented UI patch/tests; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `workpackage_claims/WP42D_static_highlight_preview_ui_integration.md`
- `handover/workpackages/20260612_2130_static_highlight_preview_ui_integration.md`

Files changed:

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP42D_static_highlight_preview_ui_integration.md`

Summary:

- Added a new post-patch script that injects an experimental read-only static highlight preview panel before the authoritative replacement table.
- The panel uses `build_static_highlight_preview(...)` and renders only helper-provided `escaped_text` inside trusted markup.
- The panel is gated by helper safety flags and is explicitly non-authoritative.
- The existing review table remains authoritative for include/exclude/replacement decisions, Scrub Key and export.
- Added static tests for patch boundaries and Docker startup order.
- No export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real data changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py`.
- App verification required after Actions and Hugging Face sync because UI behavior changed.

Next recommended step:

- `WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
- WP42C — Static highlight preview UI planning.
- WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests.
- WP42B — Static highlight preview helper and tests.
- WP42 — Streamlit feasibility boundary review.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
