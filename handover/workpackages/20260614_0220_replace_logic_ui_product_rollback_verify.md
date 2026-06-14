# Handover — WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — Closeout/app verification for hidden replacement helper panel`

Status: completed after Actions/HF/app verification.

## Summary

Formally closed out the product rollback/hide of the replacement decision helper panel.

The replacement decision helper panel was technically working but product-rejected because it was not intuitive enough and made the review flow more complex. The panel has been removed from the normal Scrub Legal flow. Helper and contract assets remain available for a future redesign.

## Verification recorded

Coordinator Actions screenshot evidence shows current post-rollback main has green recent runs:

```text
Tests — green on current post-rollback main
Sync to Hugging Face Space — green on current post-rollback main
```

The screenshot also shows earlier work after the rollback, including review highlight toggle implementation, running green on top of the rollback state. This confirms current deployed main includes the hidden/parked replacement helper panel state.

Coordinator app screenshot shows:

```text
app starts without visible Script execution error
normal Scrub Legal interface is visible
review table is visible
serial review panel is visible
highlight toggle is visible and active
replacement decision helper panel is not visible in the normal flow
export/download section is visible
DOCX hygiene audit area is visible
no static-highlight startup error is visible
```

Source verification shows:

```text
replacement_decision.py exists
REPLACE_LOGIC_UI_PLAN.md exists
tests/test_replace_logic_ui_contract.py exists
replacement_decision_panel_ui.py exists as parked/unused helper code
serial_review_panel_ui.py does not import replacement_decision_panel_ui.py
serial_review_panel_ui.py does not call render_replacement_decision_panel(...)
presidio_streamlit.py continues to import/render serial_review_panel_ui
```

## Files added

- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY.md`
- `handover/workpackages/20260614_0220_replace_logic_ui_product_rollback_verify.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY.md`

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Checks performed through repository reads and coordinator screenshots:

```text
PROJECT_PROMPT.md read
ROADMAP.md read
WORKPACKAGES.md read
CHANGELOG.md read
workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.md read
handover/workpackages/20260613_1525_replace_logic_ui_product_rollback.md read
serial_review_panel_ui.py read
tests/test_replace_logic_ui_patch.py read
replacement_decision_panel_ui.py read
replacement_decision.py read
REPLACE_LOGIC_UI_PLAN.md read
tests/test_replace_logic_ui_contract.py read
presidio_streamlit.py read
RISK_REGISTER.md read
DECISION_LOG.md read
STATUS_MONITORING_RUNBOOK.md read
```

Expected local checks, not executed here:

```text
python -m py_compile presidio_streamlit.py
python -m py_compile serial_review_panel_ui.py
pytest tests/test_replace_logic_ui_patch.py
pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py
pytest
```

## GitHub Actions status

Completed/green by coordinator screenshot evidence on current post-rollback main.

The GitHub connector status/check calls returned no statuses/workflow-runs, so screenshot evidence was used.

## Hugging Face sync status

Completed/green by coordinator screenshot evidence on current post-rollback main.

## App verification status

Completed by coordinator screenshot.

Verified user-visible state:

- app starts without visible Script execution error;
- normal Scrub Legal interface visible;
- review table visible;
- serial review panel visible;
- highlight toggle visible;
- replacement decision helper panel not visible in normal flow;
- export/download visible;
- DOCX hygiene audit visible;
- no static-highlight startup error visible.

## Remaining risks

- Replacement UX is still not solved.
- The parked replacement helper panel should not be re-exposed as a user-facing feature.
- Future replacement UX needs a design pass focused on intuitive workflow, not helper/audit internals.
- Mutating replacement behavior remains blocked until separate approval and dedicated tests.

## Next recommended step

```text
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — design a genuinely intuitive replacement review flow.
```

Only start after separate coordinator approval.

Do not start without separate coordinator approval:

```text
new replacement UI implementation
mutating replacement decisions
automatic replacement
Scrub Key writes
export blocking
click-to-mark
advanced editor
full-document marking
```
