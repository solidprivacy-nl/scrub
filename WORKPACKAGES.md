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
WP28C — implemented; partial app evidence recorded for Scrub Key/reinsert warning UI; full closeout still needs Actions/HF/app coverage.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP40-WP43 — review UX/frontend line completed through frontend architecture decision.
WP42D-VERIFY — app verification not passed; expected preview panel not visible in provided screenshot.
WP42D-FIX — first visibility repair created fail-fast behavior but still used an overly strict anchor.
WP42D-FIX2 — anchor repair implemented, but runtime showed indentation error around inserted expander wrapper.
WP42D-FIX3 — no-expander repair implemented, but stale broken block could remain in already-patched running container.
WP42D-FIX4 — stale-block cleanup repair implemented; awaiting Actions/HF sync/app verification.
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

## Scrub Key / reinsert warning evidence

```text
WP28C app evidence — partial evidence recorded.
```

A coordinator-provided screenshot of the running app in mode `Originele waarden terugzetten` shows Scrub Key and reinsert warning/acknowledgement surfaces. Full closeout still needs complete Actions/HF/app evidence.

## Review UX / frontend line

```text
WP40 — Document-centric review UX specification: completed.
WP41 — Highlight-based review prototype decision: completed.
WP42 — Streamlit feasibility boundary review: completed.
WP42B — Static highlight preview helper and tests: completed.
WP42C — Static highlight preview UI planning: completed.
WP42D — Static highlight preview UI integration: implemented.
WP42D-VERIFY — app verification not passed; expected preview panel not visible in provided screenshot.
WP42D-FIX — first visibility repair implemented fail-fast behavior but failed runtime verification.
WP42D-FIX2 — single-line editor anchor repair implemented but failed with inserted expander indentation error.
WP42D-FIX3 — no-expander repair implemented but did not clean stale already-inserted block.
WP42D-FIX4 — stale-block cleanup repair implemented; awaiting verification.
WP43 — Frontend architecture decision: completed.
```

WP42D-FIX4 summary:

- User runtime evidence kept showing the old indentation error even after the no-expander patch.
- Diagnosis: a running container can already contain a stale broken preview block in `presidio_streamlit.py`; a title-present check then skips reinsertion and leaves the broken block in place.
- `fix_streamlit_static_highlight_preview.py` now first removes any existing preview block from the preview-title line through the replacement editor anchor.
- It then inserts the current safe no-expander preview before the authoritative replacement table.
- Tests now assert stale preview cleanup logic exists.
- Read-only, non-authoritative, escaped-rendering, no export, no Scrub Key and no reinsert boundaries remain unchanged.

Next review/frontend step:

```text
Verify WP42D-FIX4 with GitHub Actions, Hugging Face sync and app screenshot showing the app starts and the preview panel is visible.
```

Do not start further review UI implementation until WP42D-FIX4 visibility is verified or coordinator explicitly approves another path.

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
1. WP42D-FIX4 verification — GitHub Actions, Hugging Face sync and app screenshot showing preview panel.
2. WP28C-CLOSEOUT — only after full Actions/HF/app verification evidence is available.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
4. No further review UI implementation until WP42D-FIX4 visibility is verified or explicitly approved.
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
