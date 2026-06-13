# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — Fix failing review highlight toggle planning tests/status contracts`

Status: completed narrow documentation repair; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Coordinator screenshot showed `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN` had green Hugging Face sync but red Tests on the claim-close commit.

The GitHub connector could not list push-triggered workflow runs for the failing commit (`fetch_commit_workflow_runs` returned `workflow_runs: []`), and direct run-number lookup is not available because the screenshot shows workflow run numbers, not REST run IDs.

The most likely stale documentation contract was in `RISK_REGISTER.md` R8. It still said there was no formal monitoring runbook and no standard status states, while `STATUS_MONITORING_RUNBOOK.md` already exists and defines standard status states.

This package corrected R8 to:

- mark the workflow-status risk as `mitigating`;
- record `STATUS_MONITORING_RUNBOOK.md` as an active mitigation;
- keep the real remaining gap: connector workflow-run lookup can still be incomplete for some push-triggered runs;
- avoid claiming there is no runbook or no standard status states.

## Files added

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX.md`
- `handover/workpackages/20260613_1634_review_highlight_toggle_plan_actions_fix.md`

## Files changed

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX.md`

## Tests/checks run

Documentation/status checks only.

Read:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RISK_REGISTER.md`
- `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `handover/workpackages/20260613_1605_review_highlight_toggle_plan.md`

Attempted workflow status check:

```text
fetch_commit_workflow_runs(3b4f92b6afa4159294839aee976cbcfbeddd9719) -> workflow_runs: []
```

Could not fetch failing job logs through the connector because the available screenshot exposes workflow run numbers, not REST workflow run IDs/job IDs.

## Validation status

- Minimal documentation repair completed.
- No product code changed.
- No tests changed.
- GitHub Actions verification is still required for the final fix commit.

## GitHub Actions status

Unknown at handover time. A new run is expected after the final fix commits.

## Hugging Face sync status

Unknown at handover time. This package does not change app/runtime behavior.

## App verification status

Not applicable. No Streamlit UI/runtime behavior changed.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No product runtime changes.
- No startup source mutation.
- No static-highlight startup patch.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No replacement table mutation.
- No automatic replacement.
- No Scrub Key writes.
- No export/download behavior changes.
- No export blocking.
- No reinsert behavior changes.
- No dependency changes.
- No cloud processing.
- No real data.

## Remaining risks

- The exact failing assertion from `Tests #838` could not be fetched through the connector.
- This repair addresses the most likely stale status-contract issue from `RISK_REGISTER.md`.
- GitHub Actions must confirm whether this was the only failing test.

## Next recommended step

Verify:

```text
Tests — green
Sync to Hugging Face Space — green
```

for the final fix commit.

Only after green evidence should the next package proceed:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS
```

Do not start `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION` without separate coordinator approval.
