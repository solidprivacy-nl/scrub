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
WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — completed; MVP UI cleanup and export/download redesign route planned.
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — completed and verified; contract tests added for professional export/download UX redesign.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — superseded by direct repair after startup-patch app verification failed.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — completed and verified; export/download UX implemented directly in presidio_streamlit.py.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN — completed; sharp interface cleanup plan added without adding a new review loop.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — completed and verified; step-by-step review collapsed by default, debug governance captions removed from primary UI, Actions/HF/app verified.
WP_MVP_FAST_MANUAL_MASK_ENTRY — completed_pending_verification; simple manual entry for missed values is implemented in the existing review flow and awaits Actions/HF/app verification.
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
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
tests/test_export_download_ux_implementation.py
REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md
manual_mask_entry.py
presidio_streamlit.py
serial_review_panel_ui.py
side_by_side_review_panel_ui.py
```

The failed startup-patch route was removed after live app verification showed the old export section. Direct implementation now lives in `presidio_streamlit.py` and is verified in the live app.

The review debug collapse implementation keeps the change interface-focused: the existing serial review renderer is collapsed by default and no new review/benchmark/safeguard loop is introduced. Verification shows the primary review UI no longer displays old debug/governance captions.

The fast manual mask entry implementation adds a simple MVP control near `3. Controleer gevonden gegevens` so a user can add a missed value to the existing replacement table. It does not add right-click, context menu, custom editor, export semantics, Scrub Key semantics, reinsert semantics or recognizer changes.

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
```

## Recall/benchmark status

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

## Active / next recommended execution queue

```text
1. Verify WP_MVP_FAST_MANUAL_MASK_ENTRY in GitHub Actions, Hugging Face sync and the live app.
2. If verified, mark WP_MVP_FAST_MANUAL_MASK_ENTRY completed_verified.
3. Do not start a new feature automatically.
4. Recommended next after verification: WP_MVP_UI_APP_VERIFICATION_CLOSEOUT or a very small UI simplification package.
```

## Boundaries

Do not start further UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.
