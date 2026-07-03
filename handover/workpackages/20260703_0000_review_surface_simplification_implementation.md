# Handover — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: completed and app-verified

## Summary

Implemented and verified a restrained review-surface simplification focused on calmer side-by-side review copy. The review surface now gives shorter guidance, keeps the source-vs-processed comparison central, and explicitly points users toward the safe download step without changing review-table, export, Scrub Key or reinsert semantics.

This implementation followed the merged planning and contract-test line and kept the change narrow: no broad `presidio_streamlit.py` rewrite, no startup patch, no second review flow and no export/reinsert behavior change.

## Files added

- `tests/test_review_surface_simplification_implementation.py`
- `handover/workpackages/20260703_0000_review_surface_simplification_implementation.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_implementation.md`

## Tests / checks

Added source-level implementation tests covering:

- three-step flow markers/equivalent safe-download copy;
- side-by-side review visibility;
- review table reachability and source-of-truth wording;
- manual missed-value entry reachability;
- serial review secondary availability;
- Scrub Key separation and warning protection;
- export/download label and MIME/filename markers;
- audit/technical/DOCX hygiene access;
- absence of prohibited new review-surface behavior.

Updated existing side-by-side copy tests to reflect the calmer copy.

Validation evidence:

- PR #12 first run failed on two stale source-level copy expectations.
- Narrow fix updated only stale test expectations.
- PR #12 Tests passed after the narrow fix.
- PR #12 was merged to `main`.
- Main Tests for commit `41cf304` passed.
- GitHub to Hugging Face sync for commit `41cf304` passed.
- Coordinator live app screenshot verified the UI.

No manual full-suite run was performed outside GitHub Actions.

## Validation

- GitHub Actions: green after narrow fix and green on `main` after merge.
- Hugging Face sync: green on `main` after merge.
- App verification: passed by coordinator screenshot.

## App verification evidence

Coordinator screenshot confirmed:

- App starts without Script execution error.
- Normal anonymization flow remains visible and calmer.
- Side-by-side review remains visible.
- `Markeringen tonen` remains visible.
- The updated calmer review copy is live.
- Manual missed-value entry remains reachable.
- Replacement table remains reachable and source of truth.
- Step-by-step review remains reachable as optional secondary aid.
- Scrub Key remains separate and warning-protected.
- Primary document downloads remain visible.
- Audit/technical downloads and DOCX hygiene audit remain available.

## Intentionally not changed

- `presidio_streamlit.py` business logic;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- The implementation is intentionally restrained; broader grouping of all secondary review expanders should be a separate package if desired.
- App verification was screenshot-based and covered the normal anonymization flow. It did not separately retest every download byte or Scrub Key JSON because those semantics were intentionally unchanged and protected by existing tests.

## Next recommended step

Do not start broader UI/reinsert/export work without a dedicated workpackage.

Recommended next step: decide whether further secondary-control grouping is desired as a separate small package, or return to recall/benchmark follow-up if product UI is good enough for the current MVP pass.
