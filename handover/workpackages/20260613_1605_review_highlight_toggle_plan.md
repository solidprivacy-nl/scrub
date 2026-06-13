# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning`

Status: completed planning/specification-only.

## Summary

Added a plan for a simple optional masked-text highlight toggle in the review preview:

```text
Markeringen tonen
Markeringen tonen in voorbeeldtekst
```

The planned feature is a calm visual aid only. When off, the preview remains normally readable. When on, already masked/replaced values may get subtle visual markers in the preview text.

The plan explicitly avoids the old WP42D route. It does not approve startup source mutation, static-highlight startup patching, click-to-mark, advanced editor behavior, full-document marking or raw unsafe HTML with document text.

## Files added

- `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `handover/workpackages/20260613_1605_review_highlight_toggle_plan.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`

## Tests/checks run

Documentation/status checks only.

Read the required start files:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Read relevant review/UI/risk files:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `presidio_streamlit.py`
- `serial_review_panel_ui.py`
- `review_panel_view_model.py`
- `replacement_decision.py`
- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_patch.py`
- `FRONTEND_ARCHITECTURE_DECISION.md`

Read relevant handovers:

- `handover/workpackages/20260613_1116_wp42d_rollback_closeout.md`
- `handover/workpackages/20260613_0030_wp42d_rollback_source_cleanup_repair.md`
- `handover/workpackages/20260613_1200_serial_review_ui_contract_tests.md`
- `handover/workpackages/20260613_1525_replace_logic_ui_product_rollback.md`

No pytest was run because this package is planning/specification-only and added no product code or tests.

## Validation status

- Plan added.
- `WORKPACKAGES.md` updated.
- `CHANGELOG.md` updated.
- `RISK_REGISTER.md` updated.
- No UI/runtime behavior changed.
- No product code changed.

## GitHub Actions status

Unknown at handover time. A workflow may run for the documentation commits.

## Hugging Face sync status

Unknown at handover time. This package does not change app/runtime behavior.

## App verification status

Not applicable. No Streamlit UI/runtime behavior changed.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No startup source mutation.
- No static-highlight startup patch.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No raw HTML with unsafe document text.
- No replacement table mutation.
- No automatic replacement.
- No Scrub Key writes.
- No export/download behavior change.
- No export blocking.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- The toggle is only planned; it is not visible in the app.
- A later implementation must avoid repeating the old WP42D startup-mutation route.
- A later implementation needs contract tests first.
- UI implementation must receive separate coordinator approval.

## Next recommended step

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS
```

Only after that, and only after separate coordinator approval:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION
```
