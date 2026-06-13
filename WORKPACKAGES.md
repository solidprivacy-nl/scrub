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
WP42D — experimental static highlight preview attempted but fully rolled back/parked after repeated runtime failures.
WP42D-ROLLBACK — completed rollback path; startup mutation disabled and table-first baseline restored.
WP42D-ROLLBACK-REPAIR — completed repair/guard path; stale static-preview source/runtime risk recorded and parked.
WP42D-ROLLBACK-CLOSEOUT — completed documentation-only closeout; working table-first interface is the current baseline.
WP_CONTEXT_CARD_HELPER — completed helper/tests-only context-card foundation; remote Actions/HF status unknown at helper handover; app verification not applicable.
WP_CONTEXT_CARD_STATUS_RECONCILE — completed documentation/status reconciliation for WP_CONTEXT_CARD_HELPER.
WP_CONTEXT_CARD_UI_PLAN — completed planning/contract-only; no UI implementation.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests implemented.
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration completed.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration completed.
WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — completed; GitHub Actions and Hugging Face sync were green for commit b869688.
WP_SERIAL_REVIEW_HELPER — completed after Actions/sync verification for commit a8182cd; app verification not applicable.
WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — completed after Actions/sync verification for commit a8182cd; app verification not applicable.
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
WP42D — Static highlight preview UI integration: fully rolled back/parked after repeated runtime failures.
WP43 — Frontend architecture decision: completed; historical WP43/WP42D contract wording restored for regression tests.
WP42D-ROLLBACK — disabled startup mutation patch and restored the working table-first interface.
WP42D-ROLLBACK-REPAIR — cache-busted HF runtime image and added app-source guard against stale static preview block.
WP42D-ROLLBACK-CLOSEOUT — recorded working table-first baseline and parked static-highlight startup mutation route.
WP_CONTEXT_CARD_HELPER — completed helper/tests-only; adds safe report-only context cards with escaped prefix/match/suffix snippets and synthetic-only tests.
WP_CONTEXT_CARD_STATUS_RECONCILE — reconciled completed context-card helper into central project status.
WP_CONTEXT_CARD_UI_PLAN — completed planning/contract-only for a non-authoritative context-card panel near the review table.
WP_SERIAL_REVIEW_HELPER — completed helper/tests-only serial review queue foundation; Actions/sync green for commit a8182cd; no UI changes.
```

WP42D rollback closeout summary:

- Coordinator/user evidence confirms the Hugging Face app is again usable on the normal table-first Scrub interface.
- The table-first review workflow is the current working baseline and fallback.
- The failed static-highlight/marking attempt is fully rolled back and parked.
- Do not restart the old static highlight preview route.
- Do not patch `presidio_streamlit.py` through startup source mutation.
- Do not reintroduce `python fix_streamlit_static_highlight_preview.py` into container startup.
- Future document-first review, marking and editor improvements must be redesigned through helper/model first, contract tests first and only then small approved UI panels.
- No product code, runtime code, UI behavior, export/download behavior, Scrub Key behavior, reinsert behavior, dependencies, cloud processing or real-data fixtures changed in the closeout.

Completed context-card helper step:

```text
WP_CONTEXT_CARD_HELPER — pure helper/tests for report-only context cards around detected values.
```

Completed context-card UI planning step:

```text
WP_CONTEXT_CARD_UI_PLAN — planning/contract-only; no Streamlit UI implementation.
```

Recorded context-card UI plan boundaries:

- The plan uses `context_cards.py` as an existing report-only helper.
- The context-card panel is non-authoritative and near the existing review table.
- The table-first baseline remains the authoritative control/fallback surface.
- The plan explicitly blocks startup source mutation, click-to-mark, advanced editor behavior, export blocking, Scrub Key mutation and reinsert behavior changes.

Next context-card step:

```text
WP_CONTEXT_CARD_UI_CONTRACT_TESTS — optional next package to harden labels, fields and boundaries.
```

Alternative helper-first next step:

```text
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — combine serial review queue + context-card data into a pure view model before any UI.
```

After context-card UI planning and explicit coordinator approval, a later UI step may combine context cards with serial review:

```text
WP_SERIAL_REVIEW_UI — small non-destructive serial review panel.
```

Do not restart static highlight preview UI work until it is redesigned without startup source mutation and without changing the table-first workflow as baseline/fallback.

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
WP_REPLACE_LOGIC_UI_PLAN — completed planning/tests/documentation-only.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — completed tests/documentation-only.
WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — completed after Actions/HF sync evidence.
WP_CONTEXT_CARD_HELPER — completed helper/tests-only report-only context-card foundation for exact-offset local context review.
WP_CONTEXT_CARD_UI_PLAN — completed planning/contract-only for a non-authoritative context-card panel near the table-first review baseline.
WP_SERIAL_REVIEW_HELPER — completed after Actions/sync verification; implemented helper/tests-only serial queue for one-by-one review navigation and report-only audit summary.
```

Next replace/review logic step:

```text
WP_CONTEXT_CARD_UI_CONTRACT_TESTS — optional next contract-test package for the context-card UI plan.
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — optional helper-first package before UI.
WP_SERIAL_REVIEW_UI — only after coordinator explicitly approves UI work.
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — only after coordinator explicitly approves UI work and after relevant contract tests are green.
```

Do not start replacement UI implementation or serial review UI implementation until coordinator approves UI work.

## Active / next recommended execution queue

```text
1. WP_CONTEXT_CARD_UI_CONTRACT_TESTS — optional next contract-test package for context-card plan labels/fields/boundaries.
2. WP_REVIEW_PANEL_VIEW_MODEL_HELPER — optional pure helper combining serial queue + context-card view data before any UI.
3. WP_SERIAL_REVIEW_UI — small non-destructive serial review panel, only after explicit coordinator approval.
4. WP28C-CLOSEOUT — only after full Actions/HF/app verification evidence is available.
5. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
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
- Startup source mutation of `presidio_streamlit.py` for preview/marking/editor work.
