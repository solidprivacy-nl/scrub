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
WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — completed planning/specification-only for a simple masked-text highlight toggle.
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — completed after Actions/HF verification by coordinator screenshot evidence.
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — completed after Actions/HF/app verification.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — completed product rollback/hide; replacement helper panel is removed from the normal Scrub Legal UI flow.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — completed after Actions/HF/app verification; hidden replacement helper panel closeout completed.
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — completed planning/design/documentation-only; old helper panel must not return as normal user-facing panel.
WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — completed roadmap/specification/documentation-only; unified side-by-side review UX direction is now anchored.
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

The new review UX target is:

```text
brontekst links | verwerkte/gecontroleerde tekst rechts
                | optionele markeringen geïntegreerd in de verwerkte tekst
```

This is now anchored in:

```text
DECISION_LOG.md — D021
SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md
ROADMAP.md
```

The replacement decision helper internals are not a user-facing feature:

```text
Do not expose replacement_decision helper internals as a user-facing panel.
```

The rollback/hide is verified:

```text
Current post-rollback Actions screenshot evidence shows green Tests and green Sync to Hugging Face Space on current main.
Coordinator app screenshot shows the normal Scrub Legal flow with review table, serial review, highlight toggle, export/download and DOCX hygiene audit visible, while the Replacement decision helper panel is not visible.
```

The redesigned replacement review direction remains:

```text
one found item -> context -> suggested replacement -> one simple choice -> optional exact-same scope -> existing table remains fallback
```

Visible first-choice labels should be user-task labels, not helper/audit internals:

```text
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

First-phase scope should stay simple:

```text
Alleen deze plek
Alle exact dezelfde waarden
```

Do not expose `all_normalized`, `creates_mapping`, `mapping_candidates`, `export_readiness`, raw decision states or audit internals as the main UI.

The highlight direction is now:

```text
Markeringen tonen belongs near/in the main side-by-side review surface.
The separate highlight-only duplicate preview is not the long-term target.
Repeated per-highlight labels such as Gemarkeerd are not the long-term target.
```

Current implementation boundaries remain:

- no startup source mutation;
- no static-highlight startup patch;
- no click-to-mark;
- no advanced editor;
- no full-document marking;
- no replacement table mutation;
- no export/download behavior change;
- no Scrub Key behavior change;
- no reinsert behavior change;
- no dependency change;
- no cloud processing;
- no real data.

## Workpackage sequence from side-by-side insight

### Planning / contract line

```text
1. WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN
2. WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS
3. WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```

These are documentation/tests-only and may be partially parallelized if they do not edit the same files at the same time.

### Helper/prototype line

```text
4. WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER
```

This should be helper-only and should not edit Streamlit UI. It may explore safe data structures for source/processed panes, highlight ranges, optional legend and scroll-sync feasibility.

### Implementation line — gated

```text
5. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — only after separate explicit coordinator approval.
6. WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION — only after separate explicit coordinator approval.
```

Implementation packages must be sequential if they touch any shared UI files.

## Active / next recommended execution queue

```text
1. WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — detailed plan for unified source/processed review surface.
2. WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — lock the side-by-side plan before implementation.
3. WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — lock the simple replacement-choice plan.
```

Safe parallel option:

```text
WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN and WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS can be worked by different workers if both stay documentation/tests-only and avoid central-doc conflicts.
```

## Blocked work

Do not start yet without separate approval:

```text
new side-by-side review UI implementation
synchronized scroll implementation
custom HTML/component rendering implementation
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
