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
WP40-WP42 — review UX line completed through Streamlit feasibility boundary review.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
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
```

WP42 artifacts:

```text
STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md
tests/test_streamlit_feasibility_boundary_review.py
DECISION_LOG.md
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP42_streamlit_feasibility_boundary_review.md
handover/workpackages/20260612_2030_streamlit_feasibility_boundary_review.md
```

WP42 summary:

- Decided Streamlit is feasible only for a small static/read-only highlight review preview using synthetic text or extracted main text.
- Decided Streamlit is not yet feasible as the long-term professional document-centric review interface.
- Blocked broad document UI rewrite, click-to-mark sensitive text, synchronized editing, Word/PDF layout rendering, review-decision mutation from highlights, Scrub Key mutation and export blocking based on highlight state.
- Required escaped rendering, non-authoritative state, color-plus-label accessibility and bounded performance scope.
- Recorded D017 in `DECISION_LOG.md`.
- Added static tests for the boundary document.
- No Streamlit UI, review table, export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real-data change was made.

Next review UX step:

```text
WP42B — Static highlight preview helper and tests
```

Alternative:

```text
WP43 — Frontend architecture decision
```

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
```

Summary:

- Checked for existing claim before starting.
- No in-progress claim existed.
- Standalone spec file creation was blocked by platform safety checks.
- The completed summary is recorded in the claim and handover.
- Recommended next step is helper/data-model tests before UI implementation.
- No code, UI, tests, export behavior, schema, runtime behavior, cloud processing or real data changed.

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests
```

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP42B — Static highlight preview helper and tests.
3. WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests.
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
