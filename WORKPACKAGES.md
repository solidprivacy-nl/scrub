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
WP40-WP42B — review UX line completed through static highlight preview helper/tests.
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
```

Next review UX step:

```text
WP42C — Static highlight preview UI planning
```

Alternative:

```text
WP43 — Frontend architecture decision
```

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
```

WP_REPLACE_LOGIC_HELPER artifacts:

```text
replacement_decision.py
tests/test_replacement_decision.py
workpackage_claims/WP_REPLACE_LOGIC_HELPER_replacement_decision_helper_tests.md
handover/workpackages/20260612_1905_replacement_decision_helper_tests.md
```

WP_REPLACE_LOGIC_HELPER summary:

- Added a pure replacement-decision helper and synthetic tests.
- Defines validated review states and scopes.
- Provides conservative same-value matching: this occurrence, exact match and normalized match.
- Builds report-only audit summaries with decision counts, risk flags, mapping candidates and advisory export-readiness state.
- Does not apply replacements to documents and does not mutate Scrub Key mappings.
- No Streamlit UI, review table flow, export/download behavior, Scrub Key schema, recognizer behavior, runtime behavior, cloud processing or real data changed.

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration
```

Do not start UI implementation until the helper tests are green and UI plan is separately approved.

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP42C — Static highlight preview UI planning.
3. WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
4. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
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
