# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — Helper-only model for source/processed review panes

Status: completed helper/tests-only; no Streamlit UI or product flow changed.

Files added:

- `side_by_side_review.py`
- `tests/test_side_by_side_review_prototype.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.md`
- `handover/workpackages/20260614_2250_side_by_side_review_prototype_helper.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.md`

Summary:

- Added a pure helper model for the future side-by-side review surface.
- The helper models source text left and processed/checked text right.
- The helper integrates optional processed-pane highlight terms/spans using the existing exact-match highlight helper.
- The helper provides a compact legend data shape and avoids repeated inline `Gemarkeerd` labels.
- The helper records review table source-of-truth/fallback fields.
- The helper records serial review as a guided layer, not a table replacement.
- The helper records replacement review as a future task-oriented layer with simple first actions/scopes, while blocking helper/audit internals as user-facing UI.
- The helper records synchronized scrolling as desired later but not implemented.
- Added tests for layout, highlight behavior, visual-only toggle contract, review table/serial/replacement relationships, scroll-sync feasibility fields, no product-state changes, compact audit summary, no Streamlit import/calls and synthetic-only values.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected check: `pytest tests/test_side_by_side_review_prototype.py`.
- Optional combined check: `pytest tests/test_side_by_side_review_prototype.py tests/test_side_by_side_review_contract.py tests/test_review_highlight_toggle.py`.
- No app rebuild or app verification required because no UI/runtime behavior changed.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No changes to `review_highlight_toggle_panel_ui.py`.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
- No export/download behavior change.
- No reinsert behavior change.
- No synchronized scroll implementation.
- No custom HTML/component rendering implementation.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- Verify GitHub Actions for this helper package.
- `WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION` only after separate explicit coordinator approval.

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
- Locked blocked behavior: no synchronized scroll implementation, custom HTML/component implementation, UI edits, review table mutation, Scrub Key writes, export/download changes, reinsert changes, click-to-mark, advanced editor or full-document marking.

## WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — Detailed plan for unified source/processed review surface

Status: completed planning/design/documentation-only; no UI or product code changed.

Summary:

- Added a detailed plan for the unified side-by-side review surface.
- Planned the main layout: brontekst/source text left and verwerkte/gecontroleerde text right.
- Placed optional highlights in the right processed pane instead of a separate long-term highlight-only duplicate preview.
- Confirmed the review table remains source of truth and fallback.
- Defined how serial review should remain a guided layer connected to the side-by-side surface.
- Defined how replacement review should plug into the main surface through simple user-task choices, not raw helper/audit internals.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction.
- WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — intuitive replacement review flow redesign.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — closeout/app verification for hidden replacement helper panel.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — contract tests for simple masked-text highlight toggle plan.
- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3 — restored exact replacement UI plan sequencing phrase.
- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — simple masked-text highlight toggle planning.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — product rollback/hide of the non-intuitive helper panel.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
