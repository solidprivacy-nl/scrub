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
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration completed.
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
WP_REPLACE_LOGIC_UI_PLAN — completed planning/tests/documentation-only.
```

WP_REPLACE_LOGIC_UI_PLAN artifacts:

```text
REPLACE_LOGIC_UI_PLAN.md
tests/test_replace_logic_ui_plan.py
workpackage_claims/WP_REPLACE_LOGIC_UI_PLAN_helper_integration.md
handover/workpackages/20260612_1925_replace_logic_ui_plan.md
```

WP_REPLACE_LOGIC_UI_PLAN summary:

- Planned how `replacement_decision.py` can later be integrated into the review UI.
- Mapped simple Dutch UI actions to helper states.
- Defined conservative scope controls.
- Preserved the current table/review flow as fallback.
- Kept export readiness advisory only.
- Kept Scrub Key schema and behavior unchanged.
- Added static tests for plan boundaries.
- No Streamlit UI, review table behavior, export/download behavior, Scrub Key behavior, reinsert behavior, helper runtime behavior, dependency, cloud processing or real data changed.

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration
```

Do not start UI implementation until the UI contract tests are completed and coordinator approves UI work.

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
4. WP43 — Frontend architecture decision, if coordinator wants architecture before UI implementation.
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
