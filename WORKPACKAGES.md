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
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — completed; contract tests added for professional export/download UX redesign.
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

Current product direction shifts visible work toward MVP UI cleanup and professional export/download flow before more recall/benchmark follow-up.

## MVP UI/export redesign status

Planning and contract files:

```text
MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
```

Contract protection covers:

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
2. Recommended next after separate approval: WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION.
3. Then: WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.
4. Then: WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION.
5. Then: WP_REVIEW_COPY_POLISH_IMPLEMENTATION.
6. Then: WP_MVP_UI_APP_VERIFICATION_CLOSEOUT.
```

## Boundaries

Do not start UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.
