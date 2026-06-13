# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Required workpackage claim check

Before starting implementation or documentation changes, check:

```text
workpackage_claims/
```

If a claim file for the same workpackage exists with status `in_progress`, stop and report that another worker has already claimed the package.

If no claim exists, create a new claim file before changing code, tests, UI, export, schema or shared documentation. Use `GitHub.create_file` so a duplicate claim fails instead of silently overwriting another worker.

When done, update the same claim file to `completed` and include the final commit/PR, handover path, tests/checks and next step.

## Current status

```text
WP28C — completed after Actions/HF/app verification for Scrub Key warning/reinsert acknowledgement UI.
WP28C-CLOSEOUT — completed verification/documentation-only closeout.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP39B — completed planning/documentation-only for DOCX hygiene audit UI; no UI implementation.
WP39C — completed tests/documentation-only for DOCX hygiene audit UI plan contracts.
WP39D — completed after Actions/HF/app verification; DOCX hygiene audit UI is report-only and app-verified.
WP39D-ACTIONS-FIX — completed wording-only repair.
WP39D-VERIFY — completed verification/documentation-only closeout.
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D — experimental static highlight preview attempted but fully rolled back/parked after repeated runtime failures.
WP_CONTEXT_CARD_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — completed helper/tests-only; combines serial queue and context-card data before UI.
WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — completed planning/specification-only for a simple masked-text highlight toggle; no UI implementation.
WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — completed narrow documentation repair for stale workflow-status risk wording; awaiting Actions/HF verification.
WP_REPLACE_LOGIC_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — completed readiness/specification-only.
WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — completed tests/documentation-only.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — technically implemented, but product validation failed; user-facing panel is not accepted as a successful feature.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — completed product rollback/hide; replacement helper panel is removed from the normal Scrub Legal UI flow while helper/contracts are preserved for redesign.
WP_SERIAL_REVIEW_HELPER — completed helper/tests-only.
WP_SERIAL_REVIEW_UI_CONTRACT_TESTS — completed; coordinator screenshot showed Tests #715 green and Sync #727 green.
WP_SERIAL_REVIEW_UI — completed and app-verified after Actions/sync verification.
WP_SERIAL_REVIEW_UI_VERIFY — completed verification/documentation-only closeout.
WP50-WP51 — pilot/ICP thinking artifacts completed, but Phase 7 is parked.
```

## Active product line

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## DOCX hygiene status

WP39B added:

```text
DOCX_HYGIENE_AUDIT_UI_PLAN.md
```

WP39C added:

```text
tests/test_docx_hygiene_audit_ui_plan.py
```

WP39D added:

```text
docx_hygiene_audit_panel_ui.py
tests/test_docx_hygiene_audit_ui_patch.py
```

WP39D is closed out after green Actions, green sync and app verification. The DOCX hygiene audit UI is report-only and remains visible near DOCX export. It does not clean files, block export, claim clean DOCX, change Scrub Key or change reinsert behavior.

## Scrub Key / reinsert warning closeout

WP28C is closed out.

Important boundary:

```text
UI acknowledgements are safety prompts only. They are not encryption, protected storage, automatic deletion, expiry enforcement, key recovery or a managed vault.
```

## Review UX / frontend status

The working baseline remains:

```text
table-first review table = source of truth and fallback
```

The serial review panel remains visible as a small non-destructive review aid.

The failed static-highlight startup mutation route remains parked. Do not restart:

- startup source mutation;
- `fix_streamlit_static_highlight_preview.py`;
- full-document marking;
- click-to-mark;
- advanced editor;
- Word/PDF layout rendering.

Simple masked-text highlight toggle planning:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — completed planning/specification-only.
```

The planned future toggle is intentionally small and optional:

```text
[ ] Markeringen tonen
[ ] Markeringen tonen in voorbeeldtekst
```

It may later show subtle visual markers for already masked/replaced values in the preview text. It must remain visual-only, read-only, non-authoritative and non-mutating. The review table remains the source of truth and fallback. The plan explicitly blocks startup source mutation, static-highlight startup patching, click-to-mark, advanced editor behavior, full-document marking, raw unsafe HTML, Scrub Key writes, export/download changes and reinsert changes.

Actions repair note:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX repaired stale workflow-status risk wording in RISK_REGISTER.md. R8 now recognizes STATUS_MONITORING_RUNBOOK.md and standard status states instead of claiming they do not exist.
```

Replacement-decision helper status:

```text
replacement_decision.py, REPLACE_LOGIC_UI_PLAN.md and tests/test_replace_logic_ui_contract.py remain valuable helper/contract assets.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION technically added a staged/read-only helper panel, but coordinator product feedback rejected it as not intuitive and too complex for the normal user flow.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK removed the panel from the normal Scrub Legal UI flow.
```

Coordinator feedback:

```text
Replacement decision helper works technically, but is not an intuitive user-friendly functionality. It makes the workflow less clear and more complex instead of more intuitive.
```

Decision boundary:

```text
Do not expose replacement_decision helper internals as a user-facing panel.
Future replacement UX should be redesigned around a genuinely intuitive review flow, not around raw helper/audit internals.
```

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX.
2. Verify GitHub Actions and Hugging Face sync for WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.
3. Request app verification screenshot for WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK because UI/runtime behavior changed.
4. WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — planning test package for the simple visual toggle, only after Actions/sync are green.
5. WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — only after separate coordinator approval.
```

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- serial review panel remains visible;
- replacement decision helper panel is not visible in the normal flow;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no static-highlight startup error.

## Blocked work

Do not start yet without separate approval:

```text
new replacement UI implementation
mutating replacement decision implementation
automatic replacement
Scrub Key write behavior
export blocking
click-to-mark
advanced editor
full-document marking
clean DOCX export blocking
DOCX cleaner/removal
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION
```

Also blocked until separate approval or later specs:

- Scrub Key encryption implementation.
- Scrub Key JSON schema migration.
- Placeholder migration.
- Robust placeholder generation in product flow.
- Placeholder auto-repair or guessed placeholder intent.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking implementation.
- Restored PDF output.
- OCR.
- Cloud document processing.
- MSI implementation.
- PyInstaller/Tauri/Electron implementation.
- Broad document-centric Streamlit UI rewrite.
- Separate frontend migration.
- Professional document editor implementation.
- Authoritative highlight-based review mutation.
- Static highlight preview startup source mutation.
- Startup source mutation of `presidio_streamlit.py` for preview/marking/editor work.
