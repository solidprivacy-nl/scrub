# Changelog — SolidPrivacy Scrub

## WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — Contract tests for collapsible review table section

Status: completed after Actions/HF verification.

Files added:

- `REVIEW_TABLE_COLLAPSIBLE_CONTRACT.md`
- `tests/test_review_table_collapsible_contract.py`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260615_0230_review_table_collapsible_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260615_0230_review_table_collapsible_contract_tests.md`

Summary:

- Added documentation and contract tests for a future collapsible `Controleer gevonden gegevens` review table section.
- Locked the future heading shape `Controleer gevonden gegevens — {item_count} items`.
- Preserved the review table as source of truth and fallback.
- Contract tests verify that `replacement_editor`, `include`, `remember`, `find` and `replace_with` remain available.
- Contract tests verify that export/download labels remain present.
- Explicitly blocks export/download changes, export blocking, Scrub Key changes, reinsert changes, replacement behavior changes, click-to-mark, advanced editor and full-document marking.
- No production UI implementation was added.

Validation status:

- Earlier `Tests #1031` failed on stale review-surface assertions expecting old highlight label and visible `syncToggle`; this was outside the collapsible-contract package.
- `WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR` repaired those stale assertions.
- Coordinator screenshot evidence confirmed `Tests #1041` green and `Sync to Hugging Face Space #1053` green for commit `143a0fa`.

Next recommended step:

- `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION` may start after coordinator approval.
- The implementation package must not run in parallel with other `presidio_streamlit.py` review-flow changes.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — Repair stale review surface control assertions

Status: completed after Actions/HF verification.

Summary:

- Repaired stale test assertions after the review surface control cleanup.
- Updated highlight-toggle contract expectations from `Markeringen tonen in verwerkte tekst` to the accepted shorter label `Markeringen tonen`.
- Updated sync-scroll production assertions to reflect D023: synchronized scrolling is active by default and no visible `syncToggle` checkbox exists in the production side-by-side renderer.
- Coordinator screenshot evidence confirmed `Tests #1041` green and `Sync to Hugging Face Space #1053` green for commit `143a0fa`.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP — Simplify side-by-side review controls

Status: implemented; awaiting Actions, Hugging Face sync and app verification.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_REVIEW_SURFACE_CONTROL_CLEANUP.md`

Files added:

- `handover/workpackages/20260615_0200_review_surface_control_cleanup.md`

Summary:

- Marker toggle label shortened to `Markeringen tonen`.
- Marker toggle now defaults to on.
- Visible sync-scroll checkbox removed from the central side-by-side component.
- Synchronized scrolling remains active by default.
- A short sync-scroll explanation remains visible below the panes.
- Tests updated for the simplified control model.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected targeted checks: `pytest tests/test_side_by_side_review_ui_patch.py`; `pytest tests/test_side_by_side_review_consolidation_dutch_sample.py`.
- Expected full check: `python -m pytest -q tests`.
- UI behavior changed, so Actions, Hugging Face sync and coordinator app verification are required.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No review table behavior change.
- No replacement behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No click-to-mark.
- No advanced editor.
- No full-document marking.

Next recommended step:

- Verify GitHub Actions and Hugging Face sync.
- Then ask coordinator to verify the app: marker on by default, no visible sync checkbox, synchronized scrolling still works.

## WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — Consolidate preview surfaces and Dutch legal sample

Status: implemented; awaiting Actions, Hugging Face sync and app verification.

Summary:

- Replaced the English demo/fallback text with a longer Dutch synthetic legal sample.
- Added `include_side_by_side` to `render_serial_review_panel` so the lower duplicate side-by-side review can be suppressed.
- Removed the old upper `Invoer` / `Directe voorbeeldweergave` two-column preview from `presidio_streamlit.py`.
- Added one central side-by-side review surface above the review table.
- Kept synchronized scrolling and optional visual markers through the existing side-by-side renderer.
- Changed the serial review call to `include_side_by_side=False` after central rendering.
- Removed the extra controlled-preview expander based on the review table to avoid a third preview surface.
- Preserved review table, export/download, Scrub Key and reinsert behavior boundaries.

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — Production integration of synchronized side-by-side scrolling

Status: implemented with explicit coordinator approval after isolated prototype review; awaiting Actions, Hugging Face sync and app verification.

Summary:

- Integrated the approved synchronized scroll concept into the production side-by-side review renderer.
- Uses Streamlit's built-in local HTML component.
- Keeps the source/brontekst pane left and processed/verwerkte pane right.
- Keeps visual highlights in the processed pane.
- Adds synchronized scrolling behavior.
- Uses percentage-based bidirectional scroll sync from the approved prototype.
- Escapes source and processed document text before HTML rendering.
- Does not import the prototype HTML file into production.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — isolated working concept for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — closeout/app verification for side-by-side review implementation.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — feasibility review for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — equal-height side-by-side review panes.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
