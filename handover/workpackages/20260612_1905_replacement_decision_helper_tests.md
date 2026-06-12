# Handover — WP_REPLACE_LOGIC_HELPER replacement decision helper and tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests`

Status: implemented helper/tests-only; awaiting GitHub Actions verification.

## Summary

Added `replacement_decision.py`, a pure helper module for future review/replace flows.

The helper provides:

- `ReplacementDecision` data model;
- validated review states and scopes;
- conservative same-value matching;
- report-only replacement audit summary;
- advisory export-readiness state.

The helper does not apply replacements to documents and does not mutate Scrub Key mappings.

## Files added

- `replacement_decision.py`
- `tests/test_replacement_decision.py`
- `workpackage_claims/WP_REPLACE_LOGIC_HELPER_replacement_decision_helper_tests.md`
- `handover/workpackages/20260612_1905_replacement_decision_helper_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_HELPER_replacement_decision_helper_tests.md`

## Tests/checks run

No local shell tests were run because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Added tests:

- `tests/test_replacement_decision.py`

## Validation status

- Claim checked before start.
- Claim created before changes.
- Helper and tests added.
- Central docs updated.
- Claim completed.

## GitHub Actions status

Pending / unknown for final handover commit.

## Hugging Face sync status

Pending / unknown for final handover commit. No app behavior changed.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- Added tests must be validated by GitHub Actions.
- Helper is not wired into UI or product flow yet.
- Export readiness is advisory/report-only and does not block export.
- UI integration requires a separate approved package.

## Next recommended step

`WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration`.
