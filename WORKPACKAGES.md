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
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP39D — completed after Actions/HF/app verification; DOCX hygiene audit UI is report-only and app-verified.
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D — experimental static highlight preview attempted but fully rolled back/parked after repeated runtime failures.
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — completed after Actions/HF/app verification.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — completed after Actions/HF/app verification; hidden replacement helper panel closeout completed.
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — completed planning/design/documentation-only; old helper panel must not return as normal user-facing panel.
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — completed tests/documentation-only; intuitive replacement review redesign is contract-locked.
WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — completed roadmap/specification/documentation-only; unified side-by-side review UX direction is now anchored.
WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — completed planning/design/documentation-only; detailed side-by-side source/processed review plan is now available.
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — completed tests/documentation-only; side-by-side review plan is contract-locked before implementation.
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — completed documentation-only wording repair for highlight safety contract phrases.
WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — completed helper/tests-only; pure source/processed pane model, highlight metadata, legend and scroll-sync feasibility fields added.
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — implemented with explicit coordinator approval; follow-up Actions fixes completed; awaiting final GitHub Actions/HF/app closeout.
WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — implemented; equal-height side-by-side panes with local pane scrolling added; awaiting GitHub Actions, Hugging Face sync and app verification.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — completed documentation-only feasibility review; recommendation is not to implement synchronized scroll in the current Streamlit MVP.
WP_SERIAL_REVIEW_UI — completed and app-verified after Actions/sync verification.
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

The side-by-side review target is now implemented as a first bounded Streamlit surface:

```text
brontekst links | verwerkte/gecontroleerde tekst rechts
                | optionele markeringen geïntegreerd in de verwerkte tekst
```

`WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX` improves the first implementation by making the source and processed panes visually equal-height. The processed highlight pane now uses a fixed pane height and its own local vertical scroll.

`WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY` records the current scroll decision:

```text
Keep equal-height independent panes as the MVP baseline.
Do not implement synchronized scrolling in the current Streamlit MVP flow.
```

Reason:

```text
Source and processed text are not guaranteed to align line-by-line or by scroll percentage after masking/replacement, so naive synchronized scrolling can create false visual alignment.
```

This is explicitly not approved:

```text
synchronized scroll implementation
custom Streamlit component rendering
JavaScript injection
```

Required verification for current UI closeout:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app screenshot.
```

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- `Controleer de tekst` side-by-side surface is visible;
- brontekst appears on the left;
- verwerkte tekst appears on the right;
- left and right panes are visually equal height;
- the processed/highlighted pane scrolls locally when content is long;
- `Markeringen tonen in verwerkte tekst` is visible in/near the right pane;
- serial review remains visible;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no replacement decision helper panel returns;
- no static-highlight startup error.

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX.
2. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — after green Actions/sync and app screenshot.
```

Only if the coordinator still wants sync-scroll after current closeout:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS — documentation/tests-only, before any spike.
```

## Blocked work

Do not start yet without separate approval:

```text
synchronized scroll implementation
custom Streamlit component rendering implementation
JavaScript injection for scroll sync
new replacement UI implementation
mutating replacement decision implementation
automatic replacement
Scrub Key writes
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
- DOCX comment/tracked-change removal.
- Restored PDF output.
- OCR.
- Cloud document processing.
- MSI implementation.
- Broad document-centric Streamlit UI rewrite.
- Separate frontend migration.
- Professional document editor implementation.
- Static highlight preview startup source mutation.
