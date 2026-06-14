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
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — completed tests/documentation-only; intuitive replacement review redesign is contract-locked.
WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — completed roadmap/specification/documentation-only; unified side-by-side review UX direction is now anchored.
WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — completed planning/design/documentation-only; detailed side-by-side source/processed review plan is now available.
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — completed tests/documentation-only; side-by-side review plan is contract-locked before implementation.
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — completed documentation-only wording repair for highlight safety contract phrases.
WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — completed helper/tests-only; pure source/processed pane model, highlight metadata, legend and scroll-sync feasibility fields added.
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

This is now anchored, planned, contract-locked and helper-modeled in:

```text
DECISION_LOG.md — D021
SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md
SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md
tests/test_side_by_side_review_contract.py
side_by_side_review.py
tests/test_side_by_side_review_prototype.py
ROADMAP.md
```

The side-by-side prototype helper adds a pure non-UI model for:

- source pane left;
- processed pane right;
- optional processed-pane highlight spans;
- compact single legend;
- review table source-of-truth/fallback fields;
- serial review guided-layer relationship;
- replacement review future task-oriented relationship;
- synchronized scroll desired-later but not implemented;
- explicit no-mutation/no-export/no-Scrub-Key/no-reinsert boundaries.

The detailed side-by-side redesign plan states:

- one main review surface before more helper panels;
- source/brontekst on the left;
- processed/checked text on the right;
- optional highlights integrated into the right processed pane;
- highlight toggle is an only visual aid;
- highlight toggle must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior;
- the separate highlight-only duplicate preview is not the long-term target;
- repeated per-highlight labels such as `Gemarkeerd` are not the long-term design;
- at most one compact legend should explain highlights;
- synchronized scrolling is desirable but must be separately planned/tested;
- no custom component, synchronized scroll, click-to-mark, advanced editor or full-document marking without separate approval.

The replacement decision helper internals are not a user-facing feature:

```text
Do not expose replacement_decision helper internals as a user-facing panel.
```

The redesigned replacement review direction is now locked by contract tests:

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

### Planning / contract/helper line

```text
1. WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — completed.
2. WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — completed.
3. WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — completed.
4. WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — completed.
5. WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — completed.
```

### Implementation line — gated

```text
6. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — only after separate explicit coordinator approval.
7. WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION — only after separate explicit coordinator approval.
```

Implementation packages must be sequential if they touch any shared UI files.

## Active / next recommended execution queue

```text
1. Verify GitHub Actions for WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.
2. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — only after separate explicit coordinator approval.
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
