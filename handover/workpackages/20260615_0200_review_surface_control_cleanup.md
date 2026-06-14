# Handover — WP_REVIEW_SURFACE_CONTROL_CLEANUP

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_SURFACE_CONTROL_CLEANUP`

Status: implemented; awaiting Actions, Hugging Face sync and app verification.

## Files added

- `handover/workpackages/20260615_0200_review_surface_control_cleanup.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_REVIEW_SURFACE_CONTROL_CLEANUP.md`

## What changed

- Marker checkbox label shortened to `Markeringen tonen`.
- Marker checkbox now defaults to on.
- Visible sync-scroll checkbox removed.
- Side-by-side panes still scroll together by default.
- Short sync explanation remains below the panes.
- Side-by-side return metadata now records sync always-on and no visible sync checkbox.

## Tests added/updated

Updated:

- `tests/test_side_by_side_review_ui_patch.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`

The tests now check:

- markers default on;
- marker toggle remains present;
- sync scroll logic remains present;
- visible sync checkbox is absent;
- sync explanation copy remains present;
- review table and download labels remain present;
- no new editor/startup-mutation wording was added.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
pytest tests/test_side_by_side_review_ui_patch.py
pytest tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

## Validation status

Implemented on `main`; runtime validation pending.

## GitHub Actions status

Unknown at handover time. Verify Actions for the final claim commit.

## Hugging Face sync status

Unknown at handover time. Verify sync after Actions.

## App verification status

Pending and required because UI behavior changed.

Expected app verification:

- app starts without Script execution error;
- central side-by-side review is visible;
- markers are on by default;
- marker toggle is visible as `Markeringen tonen`;
- no visible sync-scroll checkbox is shown;
- side-by-side panes still scroll together;
- review table remains visible;
- export/download remains visible.

## Remaining risks

- Percentage-based sync can still be visually imperfect when source and processed text differ structurally.
- App verification is required before closeout.

## Next recommended step

Verify Actions and Hugging Face sync, then perform app verification screenshot.
