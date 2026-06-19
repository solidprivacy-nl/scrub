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
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend baseline

The review table remains source of truth and fallback. The normal app keeps one central side-by-side review surface, visible markers, the collapsible replacement table, Serial review, export/download and DOCX hygiene audit.

Current product direction remains MVP interface cleanup and professional export/download flow before more recall/benchmark follow-up.

## MVP UI/export redesign status

Planning, contract and implementation files:

```text
MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
tests/test_export_download_ux_implementation.py
REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md
presidio_streamlit.py
```

The failed startup-patch route was removed after live app verification showed the old export section. Direct implementation now lives in `presidio_streamlit.py` and is verified in the live app.

The review debug collapse plan is intentionally interface-focused: it narrows the next implementation to renaming/collapsing existing prototype-like UI elements, not creating a new review/benchmark/safeguard loop.

Contract and implementation protection covers:

```text
export/download grouping
Scrub Key separation and warning
primary document downloads vs audit downloads
no export semantics change
audit/technical details remain available
copy-cleanup direction
implementation route
```

## Recall/benchmark status

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

## Active / next recommended execution queue

```text
1. Do not start a new feature automatically.
2. Recommended next: WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION.
3. Then: WP_REVIEW_COPY_POLISH_IMPLEMENTATION.
4. Then: WP_MVP_UI_APP_VERIFICATION_CLOSEOUT.
```

## Boundaries

Do not start UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.
