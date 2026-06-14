# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — Production integration of synchronized side-by-side scrolling

Status: implemented with explicit coordinator approval after isolated prototype review; awaiting Actions, Hugging Face sync and app verification.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `tests/test_side_by_side_sync_scroll_prototype.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION.md`

Files added:

- `handover/workpackages/20260615_0040_side_by_side_review_sync_scroll_implementation.md`

Summary:

- Integrated the approved synchronized scroll concept into the production side-by-side review renderer.
- Uses Streamlit's built-in local HTML component.
- Keeps the source/brontekst pane left and processed/verwerkte pane right.
- Keeps visual highlights in the processed pane.
- Adds `Synchroon scrollen` with a sync-off fallback.
- Uses percentage-based bidirectional scroll sync from the approved prototype.
- Escapes source and processed document text before HTML rendering.
- Does not import the prototype HTML file into production.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected checks: `python -m py_compile side_by_side_review_panel_ui.py`; `pytest tests/test_side_by_side_review_ui_patch.py`; `pytest tests/test_side_by_side_sync_scroll_prototype.py`; full `pytest`.
- UI behavior changed, so Actions, Hugging Face sync and coordinator app verification are required.

Intentionally not changed:

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

Next recommended step:

- Verify GitHub Actions and Hugging Face sync.
- Then app verification screenshot confirming synchronized scrolling works in the normal Scrub Legal side-by-side review.

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — Isolated working concept for synchronized side-by-side scrolling

Status: completed prototype-only and visually approved by coordinator.

Summary:

- Added an isolated browser prototype demonstrating synchronized scrolling between two side-by-side panes.
- Prototype uses synthetic-only content.
- Prototype includes source pane left and processed pane right.
- Prototype includes visual markers in the processed pane.
- Prototype includes `Synchroon scrollen` checkbox.
- Prototype supports bidirectional percentage-based scroll sync.
- Prototype supports sync-off fallback to independent scrolling.

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — Closeout/app verification for side-by-side review implementation

Status: completed verification/documentation-only closeout.

Summary:

- Closed out the first bounded side-by-side review implementation after coordinator evidence.
- Confirmed app screenshot evidence: side-by-side review visible, highlights visible, equal pane height visible, local processed-pane scrolling visible.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — feasibility review for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — equal-height side-by-side review panes.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
