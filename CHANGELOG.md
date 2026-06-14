# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — Equal-height side-by-side review panes

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.md`
- `handover/workpackages/20260614_2355_side_by_side_review_height_fix.md`

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.md`

Summary:

- Added a shared pane-height constant for the side-by-side review panes.
- The source text area and processed text area now use the same height value.
- The highlighted processed pane now has fixed height, max-height, min-height and local `overflow-y: auto` scrolling.
- This is not synchronized scrolling.
- No custom Streamlit component was added.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected focused check: `pytest tests/test_side_by_side_review_ui_patch.py`.
- Expected combined check: `pytest tests/test_side_by_side_review_ui_patch.py tests/test_review_highlight_toggle_ui_patch.py`.
- UI changed, so Actions, sync and app verification are required.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No `serial_review_panel_ui.py` change.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
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

Next recommended step:

- Verify GitHub Actions and Hugging Face sync.
- Then `WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY` with coordinator app screenshot.

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX — Repair side-by-side UI patch wording failure

Status: completed narrow Actions repair; no runtime behavior changed.

Summary:

- Removed the exact `Gemarkeerd` wording from a side-by-side panel docstring so the UI patch test can correctly guard against repeated visible per-highlight labels in the new panel.
- Kept the actual UI behavior unchanged.
- Kept the compact legend and visual-only highlight behavior unchanged.

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — Small unified source/processed review surface

Status: implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.

Summary:

- Added a bounded Streamlit side-by-side review surface in the existing review flow.
- The new visible section is `Controleer de tekst`.
- The left pane shows `Brontekst`.
- The right pane shows `Verwerkte tekst`.
- The `Markeringen tonen in verwerkte tekst` toggle is integrated into the right processed pane.
- Markers remain visual-only and do not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.
- The review table remains source of truth and fallback.
- Serial review remains visible below the side-by-side surface.
- The old separate highlight-preview call was removed from `serial_review_panel_ui.py`; legacy highlight helper assets remain available for compatibility.
- The new panel avoids repeated visible per-highlight labels and uses one compact legend instead.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — contract wording repair.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — detailed plan for unified source/processed review surface.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — closeout/app verification for hidden replacement helper panel.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — product rollback/hide of the non-intuitive helper panel.
- WP39D — DOCX hygiene audit UI implementation.
