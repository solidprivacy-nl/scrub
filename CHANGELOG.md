# Changelog — SolidPrivacy Scrub

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

## WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — Closeout/app verification for hidden replacement helper panel

Status: completed after Actions/HF/app verification.

Files added:

- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY.md`
- `handover/workpackages/20260614_0220_replace_logic_ui_product_rollback_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY.md`

Summary:

- Formally closed out the product rollback/hide of the replacement decision helper panel.
- Verified from source that helper/contract assets remain available for redesign.
- Verified from source that `serial_review_panel_ui.py` does not import or call `replacement_decision_panel_ui.py`.
- Used coordinator screenshot evidence showing current post-rollback Actions/Sync green and app verification positive.
- App screenshot shows review table, serial review, highlight toggle, export/download and DOCX hygiene audit visible, while the replacement decision helper panel is not visible.

Validation status:

- Coordinator screenshot evidence showed current post-rollback Tests and Sync to Hugging Face Space green on current main.
- GitHub connector status/check calls returned no statuses/workflow-runs, so coordinator screenshot evidence was used.
- App verification was positive by coordinator screenshot.

Intentionally not changed:

- No product code.
- No tests.
- No Streamlit UI.
- No `presidio_streamlit.py`.
- No `serial_review_panel_ui.py`.
- No new replacement UI.
- No replacement helper panel re-exposure.
- No mutating replacement behavior.
- No automatic replacement.
- No Scrub Key behavior.
- No export/download behavior.
- No reinsert behavior.
- No dependencies.
- No real data.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_REDESIGN_PLAN` only after separate coordinator approval.

## WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — Simple masked-text highlight toggle implementation

Status: completed after Actions/HF/app verification.

Files added:

- `review_highlight_toggle.py`
- `review_highlight_toggle_panel_ui.py`
- `tests/test_review_highlight_toggle.py`
- `tests/test_review_highlight_toggle_ui_patch.py`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION.md`
- `handover/workpackages/20260613_1805_review_highlight_toggle_implementation.md`

Files changed:

- `serial_review_panel_ui.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION.md`
- `handover/workpackages/20260613_1805_review_highlight_toggle_implementation.md`

Summary:

- Added a small optional `Markeringen tonen in voorbeeldtekst` toggle in the review area through a separate renderer called from the serial review panel.
- Added safe helper functions that escape document text before wrapping exact already-applied replacement values in static marker HTML.
- Added tests for exact matching, escaping, include-only replacement terms, no fuzzy matching, visible UI copy, no table/export/Scrub Key/reinsert side effects and synthetic-only values.
- No startup source mutation, no click-to-mark, no advanced editor, no full-document marking, no export/download behavior change, no Scrub Key behavior change, no reinsert behavior change, no dependency change, no cloud processing and no real data.

Validation status:

- Coordinator screenshot evidence confirmed latest shown `Tests #880` green for commit `83556af`.
- Coordinator screenshot evidence confirmed latest shown `Sync to Hugging Face Space #892` green for commit `83556af`.
- Earlier `Sync #890` failed with external `429`, but it is superseded by later green sync evidence.
- App verification was positive by coordinator screenshot: app starts, review table and serial review remain visible, the optional highlight toggle is visible, and subtle markers are shown.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

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
