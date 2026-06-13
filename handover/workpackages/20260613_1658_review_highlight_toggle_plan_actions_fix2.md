# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — Repair replacement-logic contract text failures after highlight toggle plan`

Status: completed narrow Actions repair; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Coordinator screenshot for `Tests #844` showed two existing replacement-logic contract failures:

1. `tests/test_replace_logic_ui_patch.py::test_parked_replacement_panel_still_documents_non_mutating_boundaries` expected the exact phrase `does not write Scrub Key mappings` in `replacement_decision_panel_ui.py`.
2. `tests/test_replace_logic_ui_plan.py::test_plan_requires_contract_tests_before_ui_implementation` expected the exact package name `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS` in `REPLACE_LOGIC_UI_PLAN.md`.

This repair restores only those contract strings.

## Files added

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2.md`
- `handover/workpackages/20260613_1658_review_highlight_toggle_plan_actions_fix2.md`

## Files changed

- `replacement_decision_panel_ui.py`
- `REPLACE_LOGIC_UI_PLAN.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2.md`

## Tests/checks run

No shell/pytest execution was available through the GitHub connector.

The repair is based on the exact failure lines shown in the coordinator screenshot for `Tests #844`.

Expected targeted checks in a normal checkout:

```text
pytest tests/test_replace_logic_ui_patch.py tests/test_replace_logic_ui_plan.py
python -m pytest -q tests
```

## Validation status

- Exact missing renderer phrase restored: `does not write Scrub Key mappings`.
- Exact missing plan package name restored: `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS`.
- `_safe_text` runtime behavior was preserved after the renderer text patch.
- No normal Scrub Legal flow rendering was re-enabled.

## GitHub Actions status

Unknown at handover time. A new run is expected after the final fix commits.

## Hugging Face sync status

Unknown at handover time. This package does not change normal app runtime behavior.

## App verification status

Not applicable. The normal app UI/runtime behavior was not intentionally changed.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No product runtime behavior changes.
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

- Full suite still needs GitHub Actions verification.
- This fix only addresses the two visible failures from `Tests #844`.
- If another hidden failure remains, inspect the next red test log before making further changes.

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
