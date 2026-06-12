# Changelog — SolidPrivacy Scrub

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

The previous changelog history remains available in Git history. This WP29C entry records the latest workpackage status and artifacts.
