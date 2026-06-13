# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3 — Restore exact replacement UI plan sequencing contract phrase`

Status: completed narrow documentation repair; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Coordinator screenshot for `Tests #851` showed one remaining exact contract failure in `tests/test_replace_logic_ui_plan.py`.

The test expected this exact sentence in `REPLACE_LOGIC_UI_PLAN.md`:

```text
Only after that should a small UI implementation package be considered.
```

This package restored that exact sentence under `## 14. Minimum implementation sequence`, immediately after the `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS` required-package block.

## Files added

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3.md`
- `handover/workpackages/20260613_1718_review_highlight_toggle_plan_actions_fix3.md`

## Files changed

- `REPLACE_LOGIC_UI_PLAN.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3.md`

## Tests/checks run

No shell/pytest execution was available through the GitHub connector.

Repair was based on the exact failure lines shown in coordinator screenshot for `Tests #851`.

Expected targeted check in a normal checkout:

```text
pytest tests/test_replace_logic_ui_plan.py
python -m pytest -q tests
```

## Validation status

- Exact missing sequencing sentence restored.
- No product code changed.
- No UI/runtime behavior changed.

## GitHub Actions status

Unknown at handover time. A new run is expected after the final fix commits.

## Hugging Face sync status

Unknown at handover time. This package does not change normal app runtime behavior.

## App verification status

Not applicable. No app UI/runtime behavior was changed.

## Remaining risks

- Full suite still needs GitHub Actions verification.
- This fix only addresses the remaining visible failure from `Tests #851`.

## Next recommended step

Verify:

```text
Tests — green
Sync to Hugging Face Space — green
```

Only after green evidence should the next planning package proceed:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS
```

Do not start `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION` without separate coordinator approval.
