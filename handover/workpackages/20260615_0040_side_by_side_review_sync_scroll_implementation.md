# Handover — WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — Production integration of synchronized side-by-side scrolling`

Coordinator approval: explicit after isolated prototype review.

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Integrated the approved synchronized-scroll concept into the existing production side-by-side review surface.

The implementation uses the existing `side_by_side_review_panel_ui.py` renderer and Streamlit's built-in local HTML component. The isolated prototype HTML file is not loaded by the production app.

Visible behavior expected in the app:

- source/brontekst pane left;
- processed/verwerkte pane right;
- equal-height panes;
- processed-pane highlights remain available;
- `Synchroon scrollen` checkbox inside the side-by-side surface;
- scrolling left moves right when sync is enabled;
- scrolling right moves left when sync is enabled;
- sync off restores independent scrolling;
- warning/copy notes that percentage-based sync can be imperfect.

## Files added

- `handover/workpackages/20260615_0040_side_by_side_review_sync_scroll_implementation.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `tests/test_side_by_side_sync_scroll_prototype.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION.md`

## Tests added/updated

Updated `tests/test_side_by_side_review_ui_patch.py` to cover:

- Streamlit local HTML component usage;
- sync toggle copy;
- bidirectional scroll listeners;
- percentage-based scroll syncing;
- sync-off fallback;
- source/processed text escaping before HTML rendering;
- no export, Scrub Key, reinsert or replacement mutation calls.

Updated `tests/test_side_by_side_sync_scroll_prototype.py` so it now reflects that the concept is integrated through the safe renderer, while the prototype HTML file itself remains isolated and not loaded by production code.

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
python -m py_compile side_by_side_review_panel_ui.py
pytest tests/test_side_by_side_review_ui_patch.py
pytest tests/test_side_by_side_sync_scroll_prototype.py
pytest tests/test_review_highlight_toggle_ui_patch.py
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

Unknown at handover time. Verify Actions for the final sync-scroll implementation commit.

## Hugging Face sync status

Unknown at handover time. Verify sync after Actions.

## App verification status

Pending and required.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- `Controleer de tekst` side-by-side surface is visible;
- `Synchroon scrollen` checkbox is visible;
- source pane is left;
- processed pane is right;
- highlights still work;
- scrolling left moves right when sync is on;
- scrolling right moves left when sync is on;
- turning sync off makes panes scroll independently;
- serial review remains visible;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no replacement decision helper panel returns;
- no static-highlight startup error is visible.

## Boundaries preserved

- No `presidio_streamlit.py` change.
- No `serial_review_panel_ui.py` change.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- Percentage-based sync can be visually imperfect if source and processed text diverge structurally after masking/replacement.
- The review table remains source of truth and fallback.
- App verification is still required before closeout.
- If runtime issues appear in the Hugging Face app, use a narrow repair package and preserve fallback behavior.

## Next recommended step

```text
Verify GitHub Actions and Hugging Face sync.
```

Then:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION_VERIFY
```

Do not start without separate coordinator approval:

```text
replacement UI implementation
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```
