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
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — implemented; awaiting Actions/HF/app verification.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — completed product rollback/hide; replacement helper panel is removed from the normal Scrub Legal UI flow.
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

The planned and now implemented review highlight toggle is intentionally small and optional:

```text
[ ] Markeringen tonen in voorbeeldtekst
```

It shows subtle visual markers for already masked/replaced values in the checked preview text. It remains visual-only, read-only, non-authoritative and non-mutating. The review table remains the source of truth and fallback.

Implementation boundaries:

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

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION.
2. Request app verification screenshot because UI behavior changed.
3. Verify GitHub Actions and Hugging Face sync for WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.
4. WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — only after separate coordinator approval.
```

## Blocked work

Do not start yet without separate approval:

```text
new replacement UI implementation
mutating replacement decision implementation
automatic replacement
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
