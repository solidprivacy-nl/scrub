# Handover — WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — Small unified source/processed review surface`

Coordinator approval: explicit.

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented the first bounded side-by-side review surface in the existing review flow.

The new UI section is called:

```text
Controleer de tekst
```

It shows:

```text
Brontekst links | Verwerkte tekst rechts
                | Markeringen tonen in verwerkte tekst
```

The implementation is connected through the existing `serial_review_panel_ui.py` route, so `presidio_streamlit.py` was not changed. The review table remains the source of truth and fallback. Serial review remains visible below the side-by-side surface.

The previous separate highlight-preview call was removed from `serial_review_panel_ui.py`; highlight helper assets remain for compatibility. Markers are now integrated into the right-side processed pane.

## Files added

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION.md`
- `handover/workpackages/20260614_2305_side_by_side_review_implementation.md`

## Files changed

- `serial_review_panel_ui.py`
- `tests/test_review_highlight_toggle_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION.md`

## Tests added/updated

Added `tests/test_side_by_side_review_ui_patch.py` covering:

- side-by-side panel is reached through the existing serial review route;
- side-by-side panel uses `side_by_side_review.py` helper model;
- user-facing copy exists: `Controleer de tekst`, `Brontekst`, `Verwerkte tekst`, `Markeringen tonen in verwerkte tekst`;
- highlights are integrated into the side-by-side right pane rather than rendered as the old separate duplicate preview;
- no repeated visible per-highlight `Gemarkeerd` labels in the new panel;
- review table and serial review boundaries remain visible;
- no Scrub Key, export/download or reinsert calls are introduced;
- no synchronized scroll implementation, click-to-mark, advanced editor or full-document marking is introduced;
- report-only return contract remains explicit;
- old highlight helper assets are preserved;
- synthetic-only test values.

Updated `tests/test_review_highlight_toggle_ui_patch.py` so it now expects the highlight toggle to be reached through the side-by-side panel while preserving legacy helper assets.

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
python -m py_compile side_by_side_review_panel_ui.py
python -m py_compile serial_review_panel_ui.py
pytest tests/test_side_by_side_review_ui_patch.py
pytest tests/test_review_highlight_toggle_ui_patch.py
pytest tests/test_side_by_side_review_prototype.py tests/test_side_by_side_review_contract.py tests/test_review_highlight_toggle.py
pytest
```

## Validation status

Implementation committed. Runtime validation pending.

Because UI/runtime behavior changed, closeout requires:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

## GitHub Actions status

Unknown at handover time. Verify Actions for the final implementation/claim commit.

## Hugging Face sync status

Unknown at handover time. Verify sync after Actions.

## App verification status

Pending and required.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- new `Controleer de tekst` side-by-side surface is visible;
- brontekst is visible on the left;
- verwerkte tekst is visible on the right;
- `Markeringen tonen in verwerkte tekst` is visible in/near the right pane;
- markers are visual-only;
- serial review remains visible;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- replacement decision helper panel does not return;
- no static-highlight startup error is visible.

## Boundaries preserved

- No `presidio_streamlit.py` change.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key writes or schema change.
- No export/download behavior change.
- No reinsert behavior change.
- No synchronized scroll implementation.
- No custom Streamlit component.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- The side-by-side UI is a first bounded implementation and still needs app verification.
- Synchronized scrolling remains desirable but unimplemented and requires separate approval/planning/testing.
- The current layout may still need UX refinement after coordinator review.
- Replacement review remains redesigned/planned but not re-implemented.

## Next recommended step

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY
```

Only after green Actions, green Hugging Face sync and coordinator app screenshot.

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
