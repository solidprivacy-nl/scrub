# Changelog — SolidPrivacy Scrub

## WP28C — MVP Scrub Key warning/acknowledgement UI implementation

Status: implemented; pending GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Implement MVP Scrub Key warning and acknowledgement gating for high-risk Scrub Key and reinsert actions.
- Make Scrub Key export/import, local reinsert actions and restored-output downloads visibly safer before the user triggers them.
- Preserve Scrub Key JSON content, import behavior, reinsert helper behavior, restored output bytes, filenames and MIME types after acknowledgement.

Files added:

- `tests/test_scrub_key_warning_acknowledgement_ui.py`

Files changed:

- `fix_streamlit_pdf_text_reinsert.py`
- `RELEASE_NOTES.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md`
- `handover/workpackages/20260612_1545_mvp_scrub_key_warning_acknowledgement_ui.md`

Main changes:

- Added acknowledgement gating for Scrub Key JSON download: `ack_scrub_key_export_risk`.
- Added acknowledgement gating for Scrub Key import/load: `ack_scrub_key_import_risk`.
- Added reinsert acknowledgement gating for pasted text, TXT, DOCX and PDF-to-TXT reinsert actions.
- Added restored-output download acknowledgement gating for pasted text, TXT, DOCX and PDF-to-TXT downloads.
- Added extra Dutch warning copy for Scrub Key storage, Downloads, local storage, shared risk, loss-of-key and restored confidential output.
- Strengthened unknown/duplicate placeholder warning copy without changing reinsert helper behavior.
- Kept the implementation in the post-patch layer that runs after the main Streamlit patch, so existing injected UI blocks can be gated without changing helper logic.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added static regression tests in `tests/test_scrub_key_warning_acknowledgement_ui.py`; GitHub Actions should validate them.
- App verification is required after GitHub Actions and Hugging Face sync are green because UI behavior changed.

Intentionally not changed:

- No Scrub Key schema migration.
- No encryption implementation.
- No automatic deletion.
- No expiry blocking.
- No hidden recovery.
- No helper logic change.
- No import/export semantic change after acknowledgement.
- No reinsert semantic change after acknowledgement.
- No output filename or MIME type changes.
- No dependency change.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.

## WP48 — Portable Windows proof of concept

Status: completed Windows portable proof-of-concept launcher/docs/tests.

Purpose:

- Validate a minimal portable Windows/Python direction after WP47 local file-handling/privacy validation.
- Reuse the existing local Streamlit launcher without changing app behavior.
- Keep the work proof-of-concept only with no production packaging claim.

Files added:

- `scripts/run_windows_portable_poc.ps1`
- `WINDOWS_PORTABLE_POC.md`
- `tests/test_windows_portable_poc.py`
- `workpackage_claims/WP48_portable_windows_proof_of_concept.md`
- `handover/workpackages/20260612_1530_portable_windows_proof_of_concept.md`

Files changed:

- `LOCAL_RUN.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Added a small Windows PowerShell proof-of-concept wrapper that delegates to `scripts/run_local_streamlit.py`.
- Added `WINDOWS_PORTABLE_POC.md` documenting the local portable-folder concept, Windows command, privacy boundary, non-goals and validation matrix.
- Added static tests to verify the wrapper delegates to the existing launcher, defaults to `127.0.0.1` and `8501`, does not add cloud/telemetry/packaging behavior, does not accept document/secret arguments, and that documentation records the proof-of-concept boundary.
- Updated `LOCAL_RUN.md` to describe the Windows POC path and keep explicit no-production-installer/no-MSI/no-full-offline-guarantee boundaries.
- Updated `RISK_REGISTER.md` and `WORKPACKAGES.md` so WP48 is recorded as completed and WP49 is the next local-runtime decision step.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- The tests are static proof-of-concept boundary tests and should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No Streamlit UI behavior changed.
- No upload/download/export/reinsert semantics changed.
- No Docker/Hugging Face startup behavior changed.
- No dependency changes.
- No telemetry added.
- No cloud document processing added.
- No real data added.
- No production installer claim.
- No MSI claim.
- No PyInstaller package.
- No signed executable.
- No full offline guarantee or network-traffic certification.

Next recommended step:

- `WP49 — Desktop packaging decision`, only after WP48 CI/status is acceptable and the coordinator confirms the local-runtime line should continue.
- The active Scrub Key UI line remains the already-claimed `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.

## WP29C — Scrub Key warning UI regression test scaffolding

Status: completed tests/fixture-only.

Purpose:

- Add regression-test scaffolding before the WP28C UI implementation.
- Convert `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md` into a reusable contract fixture for future warning and acknowledgement UI tests.
- Keep behavior unchanged.

Files added:

- `tests/fixtures/scrub_key_warning_ui_contract.json`
- `tests/test_scrub_key_warning_ui_contract.py`
- `workpackage_claims/WP29C_scrub_key_warning_ui_regression_test_scaffolding.md`
- `handover/workpackages/20260612_1530_scrub_key_warning_ui_regression_test_scaffolding.md`

Files changed:

- `CHANGELOG.md`

Main changes:

- Added a JSON contract fixture listing the planned warning moments, acknowledgement state keys, warning copy fragments and audit fields from `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`.
- Added tests that verify the fixture is scaffolding-only, grounded in the plan, tied to the existing Streamlit patch surface and connected to the workpackage claim protocol.
- Used the repository's `workpackage_claims/` protocol for the WP29C claim.
- Did not edit `fix_streamlit_nested_expanders.py`, `presidio_streamlit.py` or product helper files.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- The tests are static/contract tests only and should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No UI implementation.
- No Streamlit patch change.
- No helper logic change.
- No schema change.
- No import/export behavior change.
- No reinsert behavior change.
- No dependency change.
- No real data added.
- No cloud processing added.

Next recommended step:

- Continue with the already-claimed `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
- Alternative non-UI track: `WP48 — Portable Windows proof of concept`.

## Earlier entries

The previous changelog history remains available in Git history. This WP28C entry records the latest Scrub Key UI implementation status while preserving the WP48 and WP29C entries below.
