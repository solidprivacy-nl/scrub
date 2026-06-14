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
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — completed after Actions/HF/app verification; first bounded source/processed side-by-side review surface is live.
WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — completed after Actions/HF/app verification; equal-height side-by-side panes with local processed-pane scrolling are live.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — completed documentation-only feasibility review; recommendation is not to implement synchronized scroll in the current Streamlit MVP.
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — completed closeout/app verification for implementation, height fix and explicit no-sync-scroll decision.
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

The side-by-side review target is now implemented and app-verified as a first bounded Streamlit surface:

```text
brontekst links | verwerkte/gecontroleerde tekst rechts
                | optionele markeringen geïntegreerd in de verwerkte tekst
```

Verified evidence:

```text
Tests green and Sync to Hugging Face Space green for:
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY

Coordinator app screenshot confirms:
- Scrub Legal starts without Script execution error;
- review table is visible;
- `Controleer de tekst` side-by-side surface is visible;
- brontekst appears on the left;
- verwerkte tekst appears on the right;
- left and right panes are visually equal height;
- processed/highlighted pane scrolls locally;
- `Markeringen tonen in verwerkte tekst` is visible and works;
- serial review remains visible;
- export/download remains visible;
- no replacement decision helper panel is visible;
- no static-highlight startup error is visible.
```

Synchronized scrolling is explicitly not implemented:

```text
Keep equal-height independent panes as the MVP baseline.
Do not implement synchronized scrolling in the current Streamlit MVP flow.
```

Reason:

```text
Source and processed text are not guaranteed to align line-by-line or by scroll percentage after masking/replacement, so naive synchronized scrolling can create false visual alignment.
```

This remains not approved:

```text
synchronized scroll implementation
custom Streamlit component rendering
JavaScript injection
```

## Active / next recommended execution queue

```text
1. Continue MVP workflow simplification and replacement-review redesign only through separately approved packages.
2. If synchronized scroll is still desired later: WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS before any spike.
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
