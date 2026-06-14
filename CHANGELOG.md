# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — Unified side-by-side review UX direction

Status: completed roadmap/specification/documentation-only; no UI or product code changed.

Files added:

- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR.md`
- `handover/workpackages/20260614_2130_side_by_side_review_roadmap_anchor.md`

Files changed:

- `DECISION_LOG.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR.md`

Summary:

- Anchored the new review UX direction: one unified side-by-side main review surface rather than another separate helper/expander per function.
- Added `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md` as central direction document.
- Added D021 to `DECISION_LOG.md`: source text left, processed/checked text right, optional highlights integrated in the processed pane.
- Recorded that the long-term UX should not rely on a separate highlight-only duplicate preview.
- Recorded that repeated per-highlight labels such as `Gemarkeerd` are not the long-term design when the highlight color already communicates the marker.
- Structured follow-up workpackages for planning, contract tests, helper/prototype and gated implementation.

Validation status:

- Documentation/roadmap-only; no app rebuild was run.
- No product tests required because no product code, UI code or runtime behavior changed.
- GitHub connector combined-status lookup returned no visible statuses for the latest documentation commit.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No changes to `review_highlight_toggle_panel_ui.py`.
- No changes to `replacement_decision_panel_ui.py`.
- No review table behavior change.
- No synchronized scroll implementation.
- No highlight implementation change.
- No removal of existing UI code.
- No mutation behavior.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- `WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN`.
- In parallel, if desired and carefully coordinated: `WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS`.

## WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — Intuitive replacement review flow redesign

Status: completed planning/design/documentation-only; no UI or product code changed.

Files added:

- `REPLACE_LOGIC_UI_REDESIGN_PLAN.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_REDESIGN_PLAN.md`
- `handover/workpackages/20260614_0230_replace_logic_ui_redesign_plan.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_REDESIGN_PLAN.md`

Summary:

- Designed a new replacement review direction after the helper panel was product-rejected.
- Recorded that the old replacement decision helper panel must not return as the normal user-facing panel.
- Reframed replacement logic around the user task: found value, context, suggested replacement, simple choice, optional exact-same scope.
- Proposed four main actions: `Vervangen`, `Zichtbaar houden`, `Aanpassen`, `Later controleren`.
- Proposed first-phase scopes: `Alleen deze plek`, `Alle exact dezelfde waarden`.
- Explicitly kept `all_normalized`, helper/audit internals, `creates_mapping`, `mapping_candidates` and `export_readiness` out of the main user-facing flow.
- Confirmed D020 already records the product decision, so `DECISION_LOG.md` was not changed.

Validation status:

- Documentation/design-only; no app rebuild was run.
- No product tests required because no product code, UI code or runtime behavior changed.
- No shell/git diff execution was available through the ChatGPT GitHub connector.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No changes to `replacement_decision_panel_ui.py`.
- No review table behavior change.
- No mutating replacement decisions.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS`.
- Later, only with separate explicit coordinator approval: `WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION`.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

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
