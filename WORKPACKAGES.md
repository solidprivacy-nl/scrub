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
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D-VERIFY — app verification not passed; expected preview panel not visible in provided screenshot.
WP42D-INVESTIGATE — diagnosis completed; likely running app is not using WP42D-patched runtime or patch-chain diagnostics are insufficient.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests implemented.
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration completed.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration completed.
WP50-WP51 — pilot/ICP thinking artifacts completed, but Phase 7 is parked.
WP51B — MVP product quality gate recorded.
```

## MVP product quality gate

The active product priority is:

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

WP52 is parked until the MVP product quality gate is passed.

## Review UX / frontend line

```text
WP40 — Document-centric review UX specification: completed.
WP41 — Highlight-based review prototype decision: completed.
WP42 — Streamlit feasibility boundary review: completed.
WP42B — Static highlight preview helper and tests: completed.
WP42C — Static highlight preview UI planning: completed.
WP42D — Static highlight preview UI integration: implemented.
WP42D-VERIFY — app verification not passed; expected preview panel not visible in provided screenshot.
WP42D-INVESTIGATE — diagnosis completed.
WP43 — Frontend architecture decision: completed.
```

WP42D-INVESTIGATE summary:

- Checked for an existing claim before starting; none existed.
- Added `WP42D_INVESTIGATION_REPORT.md`.
- Confirmed `fix_streamlit_static_highlight_preview.py` exists and contains the expected preview label and safety gates.
- Confirmed repository `Dockerfile` includes the static highlight patch command before `streamlit run`.
- Confirmed raw `presidio_streamlit.py` does not contain the panel because WP42D is a startup patch, not a direct source edit.
- Confirmed `fix_streamlit_nested_expanders.py` creates the upstream review-table anchor used by the WP42D patch.
- Most likely diagnosis: the running Hugging Face app is not using the WP42D-patched runtime yet, or the patch-chain needs stronger diagnostics/fail-fast checks.
- No UI, code behavior, tests, runtime behavior, export/download behavior, Scrub Key behavior, reinsert behavior, cloud processing or real data changed.

Next review/frontend step:

```text
WP42D-FIX — Static highlight preview deployment/patch-chain hardening
```

Do not start further review UI implementation until WP42D visibility is fixed or coordinator explicitly approves another path.

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
WP_REPLACE_LOGIC_UI_PLAN — completed planning/tests/documentation-only.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — completed tests/documentation-only.
```

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — only after coordinator explicitly approves UI work and after relevant contract tests are green.
```

Do not start replacement UI implementation until coordinator approves UI work.

## Active / next recommended execution queue

```text
1. WP42D-FIX — Static highlight preview deployment/patch-chain hardening.
2. Coordinator/user evidence still needed for WP28C Actions/HF sync and app verification if not already available.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
4. No further review UI implementation until WP42D visibility is fixed or explicitly approved.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — replacement decision UI implementation
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
- Separate frontend migration.
- Professional document editor implementation.
- Click-to-mark sensitive text implementation.
- Authoritative highlight-based review mutation.
