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
WP39D — implemented with explicit coordinator approval; WP39D-ACTIONS-FIX completed wording-only repair; awaiting green Actions, Hugging Face sync and app verification.
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D — experimental static highlight preview attempted but fully rolled back/parked after repeated runtime failures.
WP_CONTEXT_CARD_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — completed helper/tests-only; combines serial queue and context-card data before UI.
WP_REPLACE_LOGIC_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — completed readiness/specification-only; implementation still requires separate coordinator approval.
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

## Scrub Key / reinsert warning closeout

WP28C is now closed out.

Coordinator evidence confirms:

- recent relevant GitHub Actions Tests are green;
- recent relevant Sync to Hugging Face Space runs are green;
- the running app starts without Script execution error;
- mode `Originele waarden terugzetten` is visible;
- Scrub Key loading section is visible;
- Scrub Key warning text is visible;
- Scrub Key acknowledgement checkbox is visible;
- Original-values reinsert section is visible;
- pasted-text, TXT, DOCX and PDF-to-TXT reinsert warning/acknowledgement surfaces are visible;
- DOCX success/download flow is visible after acknowledgement;
- reinsert statistics/audit output is visible;
- no export/download, Scrub Key schema, reinsert semantic, dependency, cloud-processing or real-data change was made in closeout.

Important boundary:

```text
UI acknowledgements are safety prompts only. They are not encryption, protected storage, automatic deletion, expiry enforcement, key recovery or a managed vault.
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

WP39D-ACTIONS-FIX repaired two wording-only contract failures:

```text
remove metadata
no real data
```

The DOCX hygiene audit UI is a small report-only panel shown near the existing DOCX download button. It uses `docx_hygiene_audit.py` and preserves these boundaries:

- no DOCX cleaner/removal;
- no clean-DOCX claim;
- no export blocking;
- no export/download behavior change;
- no Scrub Key change;
- no reinsert behavior change;
- no dependency change;
- no cloud processing;
- no real data.

Because WP39D changes UI/runtime behavior, it is not fully closed out yet.

Required next evidence:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- existing export/download section remains visible;
- DOCX hygiene audit UI is visible;
- text makes clear it is report-only;
- no clean-DOCX claim;
- no export blocking;
- no static-highlight startup error.

## Review UX / frontend status

The working baseline remains:

```text
table-first review table = source of truth and fallback
```

The failed static-highlight startup mutation route remains parked. Do not restart:

- startup source mutation;
- `fix_streamlit_static_highlight_preview.py`;
- full-document marking;
- click-to-mark;
- advanced editor;
- Word/PDF layout rendering.

Replacement-decision readiness conclusion:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS completed a documentation-only check.
Replacement-decision UI must not start automatically.
The smallest safe first UI direction is read-only/staged near the existing review table or serial review panel.
Mutating replacement actions, Scrub Key writes, export blocking and reinsert changes require separate explicit coordinator approval and stronger contract tests.
```

Recommended pre-implementation package if stronger safeguards are desired:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — add contract tests for staged-vs-applied UI, no table/session mutation, no Scrub Key writes, no export/download calls, and no reinsert changes.
```

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP39D-ACTIONS-FIX.
2. WP39D-VERIFY — closeout/app verification for DOCX hygiene audit UI after Actions and Hugging Face sync are green.
3. WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — if coordinator wants stronger contract coverage before replacement UI.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — replacement decision UI implementation
click-to-mark
advanced editor
full-document marking
clean DOCX export blocking
DOCX cleaner/removal
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
