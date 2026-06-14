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
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — implemented with explicit coordinator approval; WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX completed narrow wording/test repair; awaiting GitHub Actions, Hugging Face sync and app verification.
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

The new review UX target is now implemented as a first bounded Streamlit surface:

```text
brontekst links | verwerkte/gecontroleerde tekst rechts
                | optionele markeringen geïntegreerd in de verwerkte tekst
```

This line is governed by:

```text
DECISION_LOG.md — D021
SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md
SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md
tests/test_side_by_side_review_contract.py
side_by_side_review.py
tests/test_side_by_side_review_prototype.py
side_by_side_review_panel_ui.py
tests/test_side_by_side_review_ui_patch.py
```

WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION added:

- `side_by_side_review_panel_ui.py`;
- `tests/test_side_by_side_review_ui_patch.py`;
- integration through `serial_review_panel_ui.py`;
- a visible `Controleer de tekst` section;
- source/brontekst left;
- processed/verwerkte text right;
- `Markeringen tonen in verwerkte tekst` toggle in the right processed pane;
- one compact legend when markers are visible;
- no repeated per-highlight `Gemarkeerd` labels in the new panel;
- table-first fallback copy;
- no synchronized scroll implementation;
- no custom Streamlit component;
- no replacement behavior change;
- no review table behavior change;
- no Scrub Key/export/reinsert behavior change.

WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX repaired a narrow test wording issue in a helper docstring. No runtime behavior changed.

The old separate highlight-preview call was removed from `serial_review_panel_ui.py`; its helper assets remain available for compatibility.

Required verification for closeout:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app screenshot.
```

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- the new `Controleer de tekst` side-by-side surface is visible;
- brontekst appears on the left;
- verwerkte tekst appears on the right;
- `Markeringen tonen in verwerkte tekst` is visible in/near the right pane;
- marker toggle is visual-only;
- serial review remains visible;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no replacement decision helper panel returns;
- no static-highlight startup error.

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX.
2. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — after green Actions/sync and app screenshot.
```

## Blocked work

Do not start yet without separate approval:

```text
synchronized scroll implementation
custom Streamlit component rendering implementation
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
