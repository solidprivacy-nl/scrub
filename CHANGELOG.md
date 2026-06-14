# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — Isolated working concept for synchronized side-by-side scrolling

Status: implemented prototype-only; not connected to normal Scrub Legal flow.

Files added:

- `prototypes/side_by_side_sync_scroll_prototype.html`
- `SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`
- `tests/test_side_by_side_sync_scroll_prototype.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`
- `handover/workpackages/20260615_0025_side_by_side_review_sync_scroll_prototype.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md`

Summary:

- Added an isolated browser prototype demonstrating synchronized scrolling between two side-by-side panes.
- Prototype uses synthetic-only content.
- Prototype includes source pane left and processed pane right.
- Prototype includes visual markers in the processed pane.
- Prototype includes `Synchroon scrollen` checkbox.
- Prototype supports bidirectional percentage-based scroll sync.
- Prototype supports sync-off fallback to independent scrolling.
- Added static tests ensuring the prototype remains isolated from production app flow and does not touch review table, replacement, Scrub Key, export/download or reinsert behavior.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected check: `pytest tests/test_side_by_side_sync_scroll_prototype.py`.
- Coordinator can inspect `prototypes/side_by_side_sync_scroll_prototype.html` manually in a browser.

Intentionally not changed:

- No normal Streamlit UI changes.
- No `presidio_streamlit.py` changes.
- No `serial_review_panel_ui.py` changes.
- No `side_by_side_review_panel_ui.py` changes.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- Verify GitHub Actions for this prototype package.
- If useful after visual review, create contract tests/spec before any app implementation spike.

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — Closeout/app verification for side-by-side review implementation

Status: completed verification/documentation-only closeout; no product code or UI code changed.

Summary:

- Closed out the first bounded side-by-side review implementation after coordinator evidence.
- Confirmed app screenshot evidence: side-by-side review visible, highlights visible, equal pane height visible, local processed-pane scrolling visible.
- Recorded that synchronized scroll is intentionally not implemented in the normal app.

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — Feasibility review for synchronized side-by-side scrolling

Status: completed documentation-only feasibility review; no implementation or runtime behavior changed.

Summary:

- Reviewed whether synchronized scrolling should be added to the side-by-side review surface.
- Recommended keeping equal-height independent panes as the MVP baseline.
- Recommended not implementing synchronized scroll in the current Streamlit MVP flow.

## WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — Equal-height side-by-side review panes

Status: completed after Actions/HF/app verification.

Summary:

- Added a shared pane-height constant for the side-by-side review panes.
- The source text area and processed text area now use the same height value.
- The highlighted processed pane now has fixed height, max-height, min-height and local `overflow-y: auto` scrolling.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX — narrow test/wording repair after side-by-side implementation.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — closeout/app verification for hidden replacement helper panel.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
