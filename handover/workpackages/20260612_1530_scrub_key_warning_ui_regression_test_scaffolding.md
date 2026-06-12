# Handover — WP29C Scrub Key warning UI regression test scaffolding

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP29C — Scrub Key warning UI regression test scaffolding`

Status: completed tests/fixture-only.

## Summary

WP29C adds regression-test scaffolding for the future WP28C Scrub Key warning and acknowledgement UI implementation.

The work adds a JSON contract fixture derived from `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md` and a static test file that validates the contract is grounded in the plan, includes the required warning moments, acknowledgement state keys and audit fields, and points to the existing patch surface.

The package also follows the repository's new `workpackage_claims/` protocol by creating a WP29C claim before implementation. The claim is updated to completed at the end of this workpackage.

## Files added

- `tests/fixtures/scrub_key_warning_ui_contract.json`
- `tests/test_scrub_key_warning_ui_contract.py`
- `workpackage_claims/WP29C_scrub_key_warning_ui_regression_test_scaffolding.md`
- `handover/workpackages/ACTIVE_WP29C_scrub_key_warning_ui_regression_test_scaffolding.md`
- `handover/workpackages/20260612_1530_scrub_key_warning_ui_regression_test_scaffolding.md`

## Files changed

- `CHANGELOG.md`
- `workpackage_claims/WP29C_scrub_key_warning_ui_regression_test_scaffolding.md`
- `handover/workpackages/ACTIVE_WP29C_scrub_key_warning_ui_regression_test_scaffolding.md`

## Tests added/updated

- `tests/test_scrub_key_warning_ui_contract.py`
- `tests/fixtures/scrub_key_warning_ui_contract.json`

Coverage added:

- contract fixture is scaffolding-only and targets the patch layer;
- required UI block names are present;
- required warning moments are present;
- required acknowledgement state keys are present;
- acknowledgement-required moments reference valid state keys;
- planned copy fragments are grounded in `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`;
- audit fields from the plan remain part of the contract;
- the claim protocol is present and WP29C is claimed/completed.

## Validation status

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Tests were not run locally in a live repo checkout.
- The test file is static/contract-oriented and should be validated by GitHub Actions.
- App verification is not applicable because no UI behavior changed.

## GitHub Actions status

To be checked after final claim-update commit.

## Hugging Face sync status

To be checked after final claim-update commit. No app behavior changed.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- WP29C does not implement the warning UI.
- WP28C is still required to add the actual warning/acknowledgement UI behavior.
- Because WP28C is already claimed/in progress, that worker may need to pull/rebase and consume this new contract fixture.
- `WORKPACKAGES.md` update attempts were blocked by the platform filter, so WP29C completion is recorded in `CHANGELOG.md`, the claim file and this handover instead.
- `CHANGELOG.md` was compacted to record the latest WP29C status; older changelog detail remains available through Git history.

## Next recommended step

- Continue with the already-claimed `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
- Alternative non-UI track: `WP48 — Portable Windows proof of concept`.
