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
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — completed after Actions/HF/app verification.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — completed after Actions/HF/app verification; hidden replacement helper panel closeout completed.
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — completed after Actions/HF/app verification; first bounded source/processed side-by-side review surface is live.
WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — completed after Actions/HF/app verification; equal-height side-by-side panes with local processed-pane scrolling are live.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — completed isolated prototype-only concept and visually approved by coordinator.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — implemented with explicit coordinator approval; awaiting Actions, Hugging Face sync and app verification.
WP_SERIAL_REVIEW_UI — completed and app-verified after Actions/sync verification.
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

The normal app now targets:

```text
brontekst links | verwerkte/gecontroleerde tekst rechts
equal-height panes
optional visual highlights in processed pane
optional synchronized scrolling with sync-off fallback
```

`WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION` integrates the visually approved prototype concept into `side_by_side_review_panel_ui.py` using Streamlit's built-in local HTML component.

Boundaries preserved:

- review table remains source of truth and fallback;
- no replacement behavior change;
- no Scrub Key change;
- no export/download change;
- no reinsert change;
- no dependency change;
- no cloud processing;
- no real data.

## Active / next recommended execution queue

```text
1. Verify GitHub Actions and Hugging Face sync for WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION.
2. Ask coordinator for app verification screenshot.
3. Close out with WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION_VERIFY.
```

## Blocked work

Do not start yet without separate approval:

```text
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
