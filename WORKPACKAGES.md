## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

Status: in_progress / implementation complete / full-suite validation pending

Scope completed:
- migrated reinsert UI to direct source via `reinsert_mode_ui.py`;
- simplified visible reinsert flow into four user-facing steps;
- kept `presidio_streamlit.py` change minimal;
- added startup no-op guard for direct-source reinsert UI;
- added source-level UI contract tests.

Validation so far:
- targeted reinsert simplification test passed;
- existing reinsert UI patch tests passed;
- warning/two-mode UI tests passed.

Remaining:
- run full test suite;
- commit and open PR;
- verify GitHub Actions;
- verify GitHub to Hugging Face sync;
- request live app verification.


# SolidPrivacy Scrub — Workpackages

Repository: `solidprivacy-nl/scrub`.

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

## Claim rule

Before starting a package, check `workpackage_claims/`. If a claim for the same workpackage is already `in_progress`, stop and report the collision. If no claim exists, create one before changing files. When done, update the claim with status, final commit, handover path, validation and next step.

## Current status

```text
SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — completed and verified; default UI flow simplified toward execution interface, secondary controls collapsed, no export/Scrub Key/reinsert/recognizer/benchmark/startup semantics changed.
SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION — completed; small visible Dutch copy polish for side-by-side review and serial review labels, no product behavior or export semantics changed.
SCRUB-WP_MAIN_NOOP_CLEANUP — completed; accidental noop files and accidental copy-polish claim were removed from main.
SCRUB-WP_MVP_UI_APP_VERIFICATION_CLOSEOUT — completed; verification/closeout-only status recorded for the current MVP UI baseline, no product code or export semantics changed.
WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — completed; MVP UI cleanup and export/download redesign route planned.
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — completed and verified; contract tests added for professional export/download UX redesign.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — superseded by direct repair after startup-patch app verification failed.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — completed and verified; export/download UX implemented directly in presidio_streamlit.py.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN — completed; sharp interface cleanup plan added without adding a new review loop.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — completed and verified; step-by-step review collapsed by default, debug governance captions removed from primary UI, Actions/HF/app verified.
WP_MVP_FAST_MANUAL_MASK_ENTRY — completed and verified; simple manual entry for missed values is implemented in the existing review flow and live app verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — completed and verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — completed and verified.
WP_RECALL_PERSON_NAME_COVERAGE_TESTS — completed and verified.
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — completed.
WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — completed.
WP_SERIAL_REVIEW_UI — completed and app-verified.
```

Earlier completed workpackages remain available in Git history and handover files.

## Active product line

```text
Import -> Scrub -> Review -> Handmatig aanvullen -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend baseline

The review table remains source of truth and fallback. The normal app keeps one central side-by-side review surface, visible markers, a simple manual missed-value entry, the collapsible replacement table, optional step-by-step review, export/download and DOCX hygiene audit.

Current product direction remains MVP interface cleanup and fast anonymization workflow before more recall/benchmark follow-up.

## MVP UI/export redesign status

Planning, contract and implementation files:

```text
MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
MVP_UI_APP_VERIFICATION_CLOSEOUT.md
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
tests/test_export_download_ux_implementation.py
REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md
manual_mask_entry.py
presidio_streamlit.py
serial_review_panel_ui.py
side_by_side_review_panel_ui.py
tests/test_review_copy_polish_ui.py
```

The failed startup-patch route was removed after live app verification showed the old export section. Direct implementation now lives in `presidio_streamlit.py` and is verified in the live app.

The review debug collapse implementation keeps the change interface-focused: the existing serial review renderer is collapsed by default and no new review/benchmark/safeguard loop is introduced. Verification shows the primary review UI no longer displays old debug/governance captions.

The fast manual mask entry implementation adds a simple MVP control near `2. Controleer resultaat` so a user can add a missed value to the existing replacement table. It does not add right-click, context menu, custom editor, export semantics, Scrub Key semantics, reinsert semantics or recognizer changes. Actions, Hugging Face sync and live app verification are complete.

The MVP UI app verification closeout records the current verified MVP UI baseline as an administrative checkpoint only. It does not change product code, UI behavior, export semantics, Scrub Key semantics, reinsert semantics, recognizer logic, benchmark logic or local packaging.

The review copy polish implementation improves visible Dutch helper text in the side-by-side review and serial review panel only. It does not change the review table, export construction, Scrub Key, reinsert, recognizers, benchmarks or local packaging.

Contract and implementation protection covers:

```text
export/download grouping
Scrub Key separation and warning
primary document downloads vs audit downloads
no export semantics change
audit/technical details remain available
copy-cleanup direction
implementation route
manual missed-value entry through the existing replacement table
MVP UI verification closeout without product behavior change
copy polish without product behavior change
```

## Recall/benchmark status

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

## Active / next recommended execution queue

```text
1. Do not start a new feature automatically.
2. Current copy polish is recorded: SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION.
3. SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART is completed and verified on `main`.
4. Do not start a new feature automatically; create a new dedicated workpackage if further UI polish is desired.
```

## Boundaries

Do not start further UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.

## SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE — completed

Status: completed / ready for PR verification.

Summary:
- Reproduced DOCX side-by-side preview order issue with synthetic paragraph/table markers.
- Fixed DOCX plain-text extraction to preserve interleaved paragraph/table body order.
- No export, Scrub Key or reinsert semantics changed.

Validation:
- Targeted DOCX/reinsert/hygiene tests: 40 passed.
- Full suite: 649 passed in 102.51s.

## SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN — completed

Status: completed as planning/design-only; ready for PR review.

Summary:
- Added `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` for the next premium MVP review-surface simplification line.
- Target flow: `1. Voeg document toe` -> `2. Controleer resultaat` -> `3. Download veilig`.
- Keeps side-by-side review central, review table available as source of truth/fallback, and safety/audit controls available through calmer secondary layers.
- Defines `SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS` as the recommended next package before implementation touches `presidio_streamlit.py` or review flow.

Validation:
- Planning/design-only package; no product tests required.
- No app verification required because no UI behavior changed.
