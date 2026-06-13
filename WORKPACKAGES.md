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
WP42D — experimental static highlight preview attempted but rolled back after repeated runtime failures.
WP42D-ROLLBACK — static highlight preview startup patch disabled to restore working interface; awaiting HF sync/app verification.
WP42D-ROLLBACK-REPAIR — implemented HF runtime cache-bust and source guard for stale static preview code; awaiting Actions/HF/app verification.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests implemented.
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration completed.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration completed.
WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — completed; GitHub Actions and Hugging Face sync were green for commit b869688.
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
WP42D — Static highlight preview UI integration: rolled back after repeated runtime failures.
WP43 — Frontend architecture decision: completed.
WP42D-ROLLBACK — disabled startup mutation patch; awaiting verification that the app starts again.
WP42D-ROLLBACK-REPAIR — cache-busted HF runtime image and added app-source guard against stale static preview block.
```

WP42D-ROLLBACK summary:

- Coordinator/user correctly identified that repeated quick fixes were not resolving the same startup error and that the safest move was to backtrack.
- `Dockerfile` no longer runs `python fix_streamlit_static_highlight_preview.py` before Streamlit startup.
- `fix_streamlit_static_highlight_preview.py` is now a harmless no-op if called manually or by a stale command.
- Static tests now assert the Dockerfile does not run the experimental preview patch and that the patch file does not mutate `presidio_streamlit.py`.
- The experimental static highlight preview is parked.
- Goal is to restore the last working table-first interface.
- No export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

WP42D-ROLLBACK-REPAIR summary:

- Coordinator/user evidence after green Actions/HF sync still showed Hugging Face stuck on Restarting with a script execution error pointing to a stale static highlight preview caption in `presidio_streamlit.py` line 1081.
- GitHub `main` no longer contains that stale preview text, so the repair adds a Dockerfile cache-bust marker before `COPY --chown=user . $HOME/app` to force a clean Hugging Face runtime image.
- The static highlight preview remains parked; the startup patch remains disabled.
- Tests now assert that `presidio_streamlit.py` does not contain the stale preview title/caption/helper import text.

Next review/frontend step:

```text
Verify GitHub Actions, Hugging Face sync and app screenshot showing the normal Scrub Legal interface starts again without the script execution error.
```

Do not restart static highlight preview UI work until it is redesigned without startup source mutation.

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
WP_REPLACE_LOGIC_UI_PLAN — completed planning/tests/documentation-only.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — completed tests/documentation-only.
WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — completed after Actions/HF sync evidence.
```

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — only after coordinator explicitly approves UI work and after relevant contract tests are green.
```

Do not start replacement UI implementation until coordinator approves UI work.

## Active / next recommended execution queue

```text
1. WP42D-ROLLBACK-REPAIR verification — GitHub Actions, Hugging Face sync and app screenshot showing the normal app starts again.
2. WP28C-CLOSEOUT — only after full Actions/HF/app verification evidence is available.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
4. Redesign highlight preview without startup source mutation before any new UI attempt.
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
- Static highlight preview startup source mutation.
