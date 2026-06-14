# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — Detailed plan for unified source/processed review surface

Status: completed planning/design/documentation-only; no UI or product code changed.

Files added:

- `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `handover/workpackages/20260614_2205_side_by_side_review_redesign_plan.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`

Summary:

- Added a detailed plan for the unified side-by-side review surface.
- Planned the main layout: brontekst/source text left and verwerkte/gecontroleerde text right.
- Placed optional highlights in the right processed pane instead of a separate long-term highlight-only duplicate preview.
- Confirmed the review table remains source of truth and fallback.
- Defined how serial review should remain a guided layer connected to the side-by-side surface.
- Defined how replacement review should plug into the main surface through simple user-task choices, not raw helper/audit internals.
- Documented desired and unwanted Dutch UI copy.
- Defined the smallest safe first implementation as read-only side-by-side source/processed view without synchronized scrolling.
- Listed contract-test requirements before implementation.

Validation status:

- Documentation/design-only; no app rebuild was run.
- No product tests required because no product code, UI code or runtime behavior changed.
- No shell/git diff execution was available through the ChatGPT GitHub connector.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No changes to `review_highlight_toggle_panel_ui.py`.
- No custom HTML/component implementation.
- No synchronized scroll implementation.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key change.
- No export/download change.
- No reinsert change.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- `WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS`.
- If already completed by another worker: `WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER`.

## WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — Contract tests for intuitive replacement review redesign

Status: completed tests/documentation-only; no UI or product code changed.

Files added:

- `tests/test_replace_logic_ui_redesign_plan.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS.md`
- `handover/workpackages/20260614_2205_replace_logic_ui_redesign_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS.md`

Summary:

- Added contract tests for `REPLACE_LOGIC_UI_REDESIGN_PLAN.md` and `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`.
- Locked the product-rejected old helper panel out of the normal user-facing replacement flow.
- Locked the simple replacement flow: found value, context, suggested replacement, simple choice, optional scope.
- Locked the four first visible choices: `Vervangen`, `Zichtbaar houden`, `Aanpassen`, `Later controleren`.
- Locked first-phase scope to `Alleen deze plek` and `Alle exact dezelfde waarden`.
- Locked technical internals out of the main UI, including `all_normalized`, `creates_mapping`, `mapping_candidates`, `export_readiness`, raw decision states and raw audit fields.
- Locked safety boundaries: no fuzzy matching, guessed intent, automatic replacement, Scrub Key writes, export blocking, reinsert behavior change, click-to-mark, advanced editor or full-document marking.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected check: `pytest tests/test_replace_logic_ui_redesign_plan.py`.
- Optional combined check: `pytest tests/test_replace_logic_ui_redesign_plan.py tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py`.
- No app rebuild was run.
- No app verification is required because no UI/runtime behavior changed.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No changes to `replacement_decision_panel_ui.py`.
- No product code changes.
- No review table behavior change.
- No mutating replacement decisions.
- No automatic replacement.
- No Scrub Key writes.
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

- `WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS`.
- If already completed: `WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER`.

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

## Recent previous entries

Detailed recent history remains available in Git history and includes:

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
