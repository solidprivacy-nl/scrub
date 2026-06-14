# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — Consolidate preview surfaces and Dutch legal sample

Status: implemented; awaiting Actions, Hugging Face sync and app verification.

Files changed:

- `demo_text.txt`
- `serial_review_panel_ui.py`
- `presidio_streamlit.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE.md`

Files added:

- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `handover/workpackages/20260615_0130_side_by_side_review_consolidation_dutch_sample.md`

Summary:

- Replaced the English demo/fallback text with a longer Dutch synthetic legal sample.
- Added `include_side_by_side` to `render_serial_review_panel` so the lower duplicate side-by-side review can be suppressed.
- Removed the old upper `Invoer` / `Directe voorbeeldweergave` two-column preview from `presidio_streamlit.py`.
- Added one central side-by-side review surface above the review table.
- Kept synchronized scrolling and optional visual markers through the existing side-by-side renderer.
- Changed the serial review call to `include_side_by_side=False` after central rendering.
- Removed the extra controlled-preview expander based on the review table to avoid a third preview surface.
- Preserved review table, export/download, Scrub Key and reinsert behavior boundaries.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected targeted checks: `pytest tests/test_side_by_side_review_consolidation_dutch_sample.py`; `pytest tests/test_review_highlight_toggle.py tests/test_review_highlight_toggle_ui_patch.py`.
- Expected full check: `python -m pytest -q tests`.
- UI behavior changed, so Actions, Hugging Face sync and coordinator app verification are required.

Intentionally not changed:

- No new full-document editor.
- No click-to-mark.
- No advanced editor.
- No startup source mutation.
- No static-highlight startup patch.
- No export/download behavior change.
- No export blocking.
- No Scrub Key writes or schema changes.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- Verify GitHub Actions and Hugging Face sync.
- Then ask coordinator to verify the app: one central side-by-side review near the top, no duplicate preview blocks, Dutch synthetic legal sample, review table and export still visible.

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — Production integration of synchronized side-by-side scrolling

Status: implemented with explicit coordinator approval after isolated prototype review; awaiting Actions, Hugging Face sync and app verification.

Summary:

- Integrated the approved synchronized scroll concept into the production side-by-side review renderer.
- Uses Streamlit's built-in local HTML component.
- Keeps the source/brontekst pane left and processed/verwerkte pane right.
- Keeps visual highlights in the processed pane.
- Adds `Synchroon scrollen` with a sync-off fallback.
- Uses percentage-based bidirectional scroll sync from the approved prototype.
- Escapes source and processed document text before HTML rendering.
- Does not import the prototype HTML file into production.

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

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — closeout/app verification for side-by-side review implementation.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — feasibility review for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — equal-height side-by-side review panes.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
