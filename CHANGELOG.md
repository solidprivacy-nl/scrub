# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — Small unified source/processed review surface

Status: implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION.md`
- `handover/workpackages/20260614_2305_side_by_side_review_implementation.md`

Files changed:

- `serial_review_panel_ui.py`
- `tests/test_review_highlight_toggle_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION.md`

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
- The new panel avoids repeated visible per-highlight `Gemarkeerd` labels and uses one compact legend instead.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected checks: `python -m py_compile side_by_side_review_panel_ui.py`; `python -m py_compile serial_review_panel_ui.py`; `pytest tests/test_side_by_side_review_ui_patch.py`; `pytest tests/test_review_highlight_toggle_ui_patch.py`; `pytest tests/test_side_by_side_review_prototype.py tests/test_side_by_side_review_contract.py tests/test_review_highlight_toggle.py`; full `pytest`.
- UI/runtime changed, so Actions, Hugging Face sync and coordinator app verification are required before closeout.

Intentionally not changed:

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

Next recommended step:

- Verify GitHub Actions and Hugging Face sync.
- Then `WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY` with coordinator app screenshot.

## WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — Helper-only model for source/processed review panes

Status: completed helper/tests-only; no Streamlit UI or product flow changed.

Summary:

- Added a pure helper model for the future side-by-side review surface.
- The helper models source text left and processed/checked text right.
- The helper integrates optional processed-pane highlight terms/spans using the existing exact-match highlight helper.
- The helper provides a compact legend data shape and avoids repeated inline `Gemarkeerd` labels.
- The helper records review table source-of-truth/fallback fields.
- The helper records serial review as a guided layer, not a table replacement.
- The helper records replacement review as a future task-oriented layer with simple first actions/scopes, while blocking helper/audit internals as user-facing UI.
- The helper records synchronized scrolling as desired later but not implemented.

## WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — Repair side-by-side review contract wording failure

Status: completed documentation-only Actions repair; no UI or product code changed.

Summary:

- Added the exact compact contract/safety wording expected by `tests/test_side_by_side_review_contract.py`.
- Added `only visual aid` to the highlight toggle safety note.
- Added `Must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.` to the same safety note.
- No new UX direction was introduced.

## WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — Contract tests for unified side-by-side review UX

Status: completed tests/documentation-only; no UI or product code changed.

Summary:

- Added contract tests for `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`, `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md` and replacement-review alignment.
- Locked the side-by-side target: source/brontekst left, processed/checked text right, optional highlights integrated in the processed pane.
- Locked `Markeringen tonen` placement near the processed pane.
- Locked the long-term rejection of separate highlight-only duplicate preview as the main review pattern.
- Locked the long-term rejection of repeated per-highlight `Gemarkeerd` labels, allowing at most one compact legend.
- Locked review table source-of-truth/fallback and serial-review guided-layer boundaries.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — detailed plan for unified source/processed review surface.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction.
- WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — intuitive replacement review flow redesign.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — closeout/app verification for hidden replacement helper panel.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — contract tests for simple masked-text highlight toggle plan.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — product rollback/hide of the non-intuitive helper panel.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP39D — DOCX hygiene audit UI implementation.
