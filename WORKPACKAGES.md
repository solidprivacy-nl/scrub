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
WP28C — implemented; still needs coordinator evidence/app verification.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP40-WP42C — review UX line completed through static highlight preview UI planning.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests implemented.
WP50-WP51 — pilot/ICP thinking artifacts completed, but Phase 7 is parked.
WP51B — MVP product quality gate recorded.
```

## MVP product quality gate

The active product priority is:

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

WP52 is parked until the MVP product quality gate is passed.

## Review UX line

```text
WP40 — Document-centric review UX specification: completed.
WP41 — Highlight-based review prototype decision: completed.
WP42 — Streamlit feasibility boundary review: completed.
WP42B — Static highlight preview helper and tests: completed.
WP42C — Static highlight preview UI planning: completed.
```

WP42C artifacts:

```text
STATIC_HIGHLIGHT_PREVIEW_UI_PLAN.md
tests/test_static_highlight_preview_ui_plan.py
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP42C_static_highlight_preview_ui_planning.md
handover/workpackages/20260612_2110_static_highlight_preview_ui_planning.md
```

WP42C summary:

- Planned a future experimental read-only Streamlit panel for static highlight preview.
- Required the current replacement table to remain authoritative.
- Required helper gates before rendering: `safe_to_render`, `read_only`, `non_authoritative`, `mutation_allowed=False`, `export_blocking=False` and `scrub_key_changes=False`.
- Required rendering only `escaped_text`, not raw user text as HTML.
- Added static tests for planning boundaries.
- No Streamlit UI, review table, export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real data changed.

Next review UX step:

```text
WP42D — Static highlight preview UI integration
```

Only start WP42D if coordinator explicitly approves UI work, because it changes app behavior and requires app verification.

Alternative:

```text
WP43 — Frontend architecture decision
```

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
```

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration
```

Do not start UI implementation until the helper tests are green and UI plan is separately approved.

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP42D — Static highlight preview UI integration, only if coordinator approves UI work.
3. WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
4. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
WP42D — Static highlight preview UI integration
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
- Click-to-mark sensitive text implementation.
- Authoritative highlight-based review mutation.
