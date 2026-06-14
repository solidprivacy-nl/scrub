# Handover — WP_REVIEW_SURFACE_CONTROL_CLEANUP_ACTIONS_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_SURFACE_CONTROL_CLEANUP_ACTIONS_FIX`

Status: completed; verification note only.

## Summary

A failing Actions screenshot showed two stale expectations:

- `tests/test_review_highlight_toggle_ui_patch.py` still expecting `Markeringen tonen in verwerkte tekst`;
- `tests/test_side_by_side_sync_scroll_prototype.py` still expecting `syncToggle` in the production renderer.

On current `main`, both files already contain the updated expectations:

- central renderer expects `Markeringen tonen` and not the old longer label;
- production renderer is expected not to contain `syncToggle`;
- production renderer is expected to contain `sync_scroll_always_on` and `sync_scroll_visible_checkbox` metadata.

The screenshot therefore represents an older failing run, not the current test state.

## Files added

- `handover/workpackages/20260615_0215_review_surface_control_cleanup_actions_fix.md`

## Files changed

- `workpackage_claims/WP_REVIEW_SURFACE_CONTROL_CLEANUP_ACTIONS_FIX.md`

No product code was changed in this repair package.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected verification:

```text
pytest tests/test_review_highlight_toggle_ui_patch.py
pytest tests/test_side_by_side_sync_scroll_prototype.py
pytest tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests
```

## Validation status

Current repository file inspection confirms the stale expectations are no longer present on `main`.

## GitHub Actions status

Pending / unknown for this handover commit.

## Hugging Face sync status

Pending / unknown for this handover commit.

## App verification status

No app behavior changed in this repair package.

## Remaining risks

If Actions are still red after this handover, inspect the latest failing run rather than the older screenshot.

## Next recommended step

Wait for the new Actions run triggered by this handover/claim update and verify that tests are green.
