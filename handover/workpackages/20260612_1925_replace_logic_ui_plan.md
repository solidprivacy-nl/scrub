# Handover — WP_REPLACE_LOGIC_UI_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration`

Status: completed planning/tests/documentation-only.

## Summary

Planned how `replacement_decision.py` can later be integrated into the review UI without implementing UI now.

The plan maps simple Dutch actions to helper states, defines conservative scope controls, keeps export readiness advisory only, keeps Scrub Key behavior unchanged and requires contract tests before UI implementation.

## Files added

- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_plan.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PLAN_helper_integration.md`
- `handover/workpackages/20260612_1925_replace_logic_ui_plan.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PLAN_helper_integration.md`

## Tests/checks run

No local shell tests were run because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Added static plan tests:

- `tests/test_replace_logic_ui_plan.py`

## Validation status

- Claim checked before start.
- Claim created before changes.
- Plan and static tests added.
- Central docs updated.
- Claim completed.

## GitHub Actions status

Pending / unknown for final handover commit.

## Hugging Face sync status

Pending / unknown for final handover commit. No app behavior changed.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- Added plan tests must be validated by GitHub Actions.
- No UI implementation exists yet.
- Future UI work will require explicit approval and app verification.

## Next recommended step

`WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration`.
