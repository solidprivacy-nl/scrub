# Handover — WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR`

Status: completed tests/documentation-only repair.

## Summary

Repaired two stale test assertions that still expected the pre-cleanup review controls. The production UI now uses the shorter `Markeringen tonen` label, markers default on, synchronized scrolling remains active by default, and the visible sync-scroll checkbox is intentionally removed.

## Files added

- `workpackage_claims/WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR.md`
- `handover/workpackages/20260615_0240_review_surface_control_cleanup_test_repair.md`

## Files changed

- `tests/test_review_highlight_toggle_ui_patch.py`
- `tests/test_side_by_side_sync_scroll_prototype.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR.md`

## Tests added/updated

Updated stale assertions in:

- `tests/test_review_highlight_toggle_ui_patch.py`
- `tests/test_side_by_side_sync_scroll_prototype.py`

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected targeted check:

```text
pytest tests/test_review_highlight_toggle_ui_patch.py tests/test_side_by_side_sync_scroll_prototype.py
```

Expected full check:

```text
python -m pytest -q tests
```

## Validation status

- Screenshot showed failing assertions against old UI labels/control state.
- Test assertions updated to match accepted D023 behavior.
- No app rebuild required for this repair.

## GitHub Actions status

Unknown at handover time. Verify the new repair commit in Actions.

## Hugging Face sync status

Not required for behavior; no runtime/UI code changed.

## App verification status

Not applicable for this repair.

## Remaining risks

- Full suite still needs Actions verification.
- Pending UI work still needs normal Actions -> Hugging Face sync -> coordinator app screenshot flow.

## Next recommended step

Verify GitHub Actions for the repair commit. If green, continue the normal verification queue before starting `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION`.
