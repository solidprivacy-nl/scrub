# Handover — WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — Isolated working concept for synchronized side-by-side scrolling`

Coordinator approval: explicit.

Status: implemented prototype-only; awaiting GitHub Actions verification and coordinator visual inspection.

## Summary

Added an isolated working concept for synchronized scrolling between two side-by-side panes.

Prototype file:

```text
prototypes/side_by_side_sync_scroll_prototype.html
```

The prototype demonstrates:

- source/brontekst left;
- processed/verwerkte text right;
- equal-height panes;
- visual markers in the processed pane;
- `Synchroon scrollen` checkbox;
- bidirectional percentage-based scroll sync;
- sync-off fallback to independent scrolling.

The prototype is not connected to the normal Scrub Legal flow.

## Files added

- `prototypes/side_by_side_sync_scroll_prototype.html`
- `SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`
- `tests/test_side_by_side_sync_scroll_prototype.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`
- `handover/workpackages/20260615_0025_side_by_side_review_sync_scroll_prototype.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`

`RISK_REGISTER.md` was not changed because this package adds an isolated prototype only and does not change the production app risk state.

## Tests added/updated

Added `tests/test_side_by_side_sync_scroll_prototype.py`.

The tests check:

- prototype HTML exists;
- two panes and sync toggle exist;
- bidirectional percentage-based scroll logic exists;
- sync-off fallback exists;
- risk warning exists;
- synthetic content only;
- prototype is not connected to `presidio_streamlit.py`, `serial_review_panel_ui.py` or `side_by_side_review_panel_ui.py`;
- no production behavior markers for Scrub Key, export/download, reinsert or replacement application appear in the prototype.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected check:

```text
pytest tests/test_side_by_side_sync_scroll_prototype.py
```

Optional full check:

```text
pytest
```

## Validation status

Implemented and committed. GitHub Actions verification pending.

Manual visual inspection path:

```text
Open prototypes/side_by_side_sync_scroll_prototype.html in a browser.
```

Expected behavior:

- with sync on, scrolling left moves right;
- with sync on, scrolling right moves left;
- with sync off, panes scroll independently.

## GitHub Actions status

Unknown at handover time. Verify Actions for final prototype commit.

## Hugging Face sync status

Not required for app behavior because the prototype is not connected to the normal app. A sync may still run because the repository changed.

## App verification status

Not applicable for normal Scrub Legal app flow.

Prototype visual inspection is recommended.

## Boundaries preserved

- No production Streamlit UI change.
- No `presidio_streamlit.py` change.
- No `serial_review_panel_ui.py` change.
- No `side_by_side_review_panel_ui.py` change.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- The prototype uses percentage-based scroll sync and can still create false visual alignment if source and processed text diverge structurally.
- This prototype is not proof that production synchronized scrolling is safe.
- A production implementation would require separate contract tests, a security review and explicit coordinator approval.

## Next recommended step

Verify GitHub Actions for this package.

Then have the coordinator visually inspect:

```text
prototypes/side_by_side_sync_scroll_prototype.html
```

If the concept is useful, the next safe package is:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS
```

Do not start without separate coordinator approval:

```text
production synchronized scroll implementation
custom Streamlit component rendering
replacement UI implementation
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```
