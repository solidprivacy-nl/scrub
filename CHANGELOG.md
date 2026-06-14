# Changelog — SolidPrivacy Scrub

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

## WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — Contract tests for simple masked-text highlight toggle plan

Status: completed after Actions/HF verification by coordinator screenshot evidence.

Summary:

- Added contract tests for `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`.
- Coordinator screenshot showed `Tests #865` green and `Sync to Hugging Face Space #877` green for commit `07b7581`.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3 — Restore exact replacement UI plan sequencing phrase

Status: completed after Actions/HF verification; app verification not applicable.

Summary:

- Restored: `Only after that should a small UI implementation package be considered.`
- Coordinator screenshot evidence confirmed `Tests #855` green and `Sync to Hugging Face Space #867` green for commit `c9b5201`.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning

Status: completed planning/specification-only; no UI or product code changed.

Summary:

- Planned a simple optional review toggle: `Markeringen tonen` / `Markeringen tonen in voorbeeldtekst`.
- Goal is to show subtle visual markers for values already masked/replaced in the preview text.
- The planned toggle remains visual-only, read-only, non-authoritative and non-mutating.
- The review table remains the source of truth and fallback.
- Explicitly blocks the old WP42D static-highlight startup mutation route, startup patching of `presidio_streamlit.py`, click-to-mark, advanced editor behavior, full-document marking, raw unsafe HTML, Scrub Key writes, export/download changes and reinsert changes.

## WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

Status: completed product rollback/hide.

Summary:

- Product feedback rejected the technically working replacement helper panel as not intuitive enough for the normal user flow.
- The panel is no longer rendered from the normal Scrub Legal flow.
- Helper and contract assets remain available for later redesign.
- No replacement behavior, export behavior, Scrub Key behavior or reinsert behavior changed.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — replacement-logic contract text repair.
- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — workflow-status risk wording repair.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
