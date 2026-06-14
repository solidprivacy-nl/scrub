# Handover — WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — Equal-height side-by-side review panes`

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented a small UX fix for the side-by-side review surface after coordinator app feedback.

Problem observed:

```text
The source and processed side-by-side panes were not visually equal height.
The processed highlighted pane could grow much taller than the source pane.
```

Fix:

```text
Both side-by-side panes now use one shared height constant.
The processed highlighted pane has fixed height and local vertical scrolling.
```

This is explicitly not synchronized scrolling.

## Files added

- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.md`
- `handover/workpackages/20260614_2355_side_by_side_review_height_fix.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.md`

## Tests added/updated

Updated `tests/test_side_by_side_review_ui_patch.py` with coverage for:

- shared `SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320`;
- CSS height, max-height and min-height using that shared constant;
- local `overflow-y: auto` on the processed highlight pane;
- both text areas using `height=SIDE_BY_SIDE_REVIEW_PANE_HEIGHT`;
- return metadata for `pane_height` and `processed_pane_scrolls_independently`.

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
python -m py_compile side_by_side_review_panel_ui.py
pytest tests/test_side_by_side_review_ui_patch.py
pytest tests/test_side_by_side_review_ui_patch.py tests/test_review_highlight_toggle_ui_patch.py
pytest
```

## Validation status

Implementation committed. Runtime validation pending.

Because UI behavior changed, closeout requires:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

## GitHub Actions status

Unknown at handover time. Verify Actions for the final height-fix commit.

## Hugging Face sync status

Unknown at handover time. Verify sync after Actions.

## App verification status

Pending and required.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- `Controleer de tekst` side-by-side surface is visible;
- brontekst appears on the left;
- verwerkte tekst appears on the right;
- left and right panes are visually equal height;
- the processed/highlighted pane scrolls locally when content is long;
- `Markeringen tonen in verwerkte tekst` remains visible;
- serial review remains visible;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no synchronized scroll behavior is claimed or introduced;
- no replacement decision helper panel returns;
- no static-highlight startup error is visible.

## Boundaries preserved

- No synchronized scroll implementation.
- No custom Streamlit component rendering.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key change.
- No export/download change.
- No reinsert change.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- Visual pane height should be verified in the Hugging Face app.
- Synchronized scrolling remains unimplemented and should only be considered in a separate feasibility package.
- Further UX tuning may be needed after coordinator review.

## Next recommended step

```text
Verify GitHub Actions and Hugging Face sync for WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.
```

Then:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY
```

Do not start without separate coordinator approval:

```text
synchronized scroll implementation
custom Streamlit component rendering
replacement UI implementation
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```
