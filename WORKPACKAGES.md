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
WP_REPLACE_LOGIC_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — completed readiness/specification-only; implementation required separate coordinator approval.
WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — completed tests/documentation-only; strengthened staged-vs-applied, mutation, Scrub Key, export and reinsert contracts before implementation.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — implemented with explicit coordinator approval; staged/read-only companion panel added; awaiting GitHub Actions, Hugging Face sync and app verification.
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

WP39D-ACTIONS-FIX repaired the wording-only contract failures. Coordinator screenshot evidence then confirmed:

- latest relevant GitHub Actions Tests are green;
- latest relevant Sync to Hugging Face Space is green;
- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- existing export/download section remains visible;
- DOCX hygiene audit UI is visible;
- the panel says it is report-only;
- no clean-DOCX claim is shown;
- export is not blocked;
- no static-highlight startup error is visible.

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

Replacement-decision contract gap fix:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX strengthened REPLACE_LOGIC_UI_PLAN.md and tests/test_replace_logic_ui_contract.py.
It now locks staged-vs-applied state, no review table mutation, view-only session-state limits, advisory-only mapping/export readiness, no Scrub Key writes, no export/download calls, no reinsert changes, no automatic replacement, no fuzzy matching/guessed intent and explicit approval before implementation.
```

Replacement-decision helper panel implementation:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION added replacement_decision_panel_ui.py and tests/test_replace_logic_ui_patch.py.
The panel is rendered from the serial review area and uses replacement_decision.py for staged/read-only preview only.
It shows selected occurrence, source text, suggested replacement, decision state, scope, affected count, advisory mapping/export/readiness fields, unresolved items and risk flags.
It does not mutate the existing review table, edited_replacements_df, Streamlit data-editor state, Scrub Key, export/download behavior or reinsert behavior.
```

Required next evidence:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- existing review table remains visible;
- serial review panel remains visible;
- Replacement decision helper panel is visible;
- panel clearly says staged/read-only / not applied;
- existing replacement table remains source of truth and fallback;
- no automatic replacement;
- no Scrub Key change;
- no export blocking;
- no reinsert change;
- no static-highlight startup error.

## Active / next recommended execution queue

```text
1. WP_REPLACE_LOGIC_UI_VERIFY — closeout/app verification for replacement decision helper panel after Actions and Hugging Face sync are green.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
mutating replacement decision implementation
automatic replacement
Scrub Key write behavior
export blocking
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
