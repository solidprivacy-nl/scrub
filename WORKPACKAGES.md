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
WP28C — implemented; partial app evidence recorded for Scrub Key/reinsert warning UI; full closeout still needs Actions/HF/app coverage.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D — experimental static highlight preview attempted but fully rolled back/parked after repeated runtime failures.
WP_CONTEXT_CARD_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line; no UI implementation.
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — completed helper/tests-only; combines serial queue and context-card data before UI.
WP_REPLACE_LOGIC_HELPER / UI_PLAN / UI_CONTRACT_TESTS — completed helper/planning/tests line.
WP_SERIAL_REVIEW_HELPER — completed helper/tests-only.
WP_SERIAL_REVIEW_UI_CONTRACT_TESTS — completed; coordinator screenshot showed Tests #715 green and Sync #727 green.
WP_SERIAL_REVIEW_UI — implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.
WP50-WP51 — pilot/ICP thinking artifacts completed, but Phase 7 is parked.
```

## Active product line

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
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

## WP_SERIAL_REVIEW_UI implementation note

Coordinator approval: explicit.

Implemented:

- `serial_review_panel_ui.py` renders a small helper-driven Streamlit panel.
- `presidio_streamlit.py` calls `render_serial_review_panel(...)` after the existing replacement table editor.
- `tests/test_serial_review_ui_patch.py` adds static guards for UI text, navigation, safety boundaries and no static-highlight startup mutation.

The panel is intentionally:

- table-first baseline;
- non-destructive;
- report-only;
- no Scrub Key mutation;
- no export blocking;
- no reinsert behavior change.

The panel may use only view state:

```text
serial_review_current_index
serial_review_current_occurrence_id
serial_review_filter_mode
```

Not changed:

- no review table mutation;
- no automatic replacement;
- no Scrub Key writes;
- no export/download behavior change;
- no reinsert behavior change;
- no dependency change;
- no cloud processing;
- no real data.

## Verification required

Because WP_SERIAL_REVIEW_UI changes UI/runtime behavior, it is not fully closed out yet.

Required next evidence:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

App verification should confirm:

- app starts without Script execution error;
- normal table-first Scrub interface remains visible;
- serial review panel is visible;
- existing review table remains present;
- no static highlight preview startup error;
- no full-document marking/editor.

## Active / next recommended execution queue

```text
1. WP_SERIAL_REVIEW_UI_VERIFY — closeout/app verification after Actions and Hugging Face sync are green.
2. WP28C-CLOSEOUT — only after full Actions/HF/app verification evidence is available.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — replacement decision UI implementation
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
- Click-to-mark sensitive text implementation.
- Authoritative highlight-based review mutation.
- Static highlight preview startup source mutation.
- Startup source mutation of `presidio_streamlit.py` for preview/marking/editor work.
