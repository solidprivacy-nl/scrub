# Changelog — SolidPrivacy Scrub

## SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION — Review copy polish

Status: completed as small UI-copy implementation.

Summary:

- Polished visible Dutch helper text in `side_by_side_review_panel_ui.py`.
- Polished visible Dutch labels and helper text in `serial_review_panel_ui.py`.
- Added `tests/test_review_copy_polish_ui.py` to protect the new copy and boundaries.
- Updated `RELEASE_NOTES.md` with the user-facing copy polish.
- Kept the review table as source of truth and fallback.

Tests:

- Added source-level UI copy tests for side-by-side review and serial review.
- Added boundary tests confirming export, Scrub Key and reinsert references remain in the app flow.
- Local tests were not run in this connector session.

Validation status:

- GitHub Actions: pending after PR.
- Hugging Face sync: pending after merge.
- App verification: required after merge because visible UI copy changed.

Intentionally not changed:

- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- review table data flow
- export/download behavior and file semantics
- Scrub Key behavior
- reinsert behavior
- recognizer/benchmark behavior
- local packaging/runtime setup
- cloud document processing

---

## SCRUB-WP_MAIN_NOOP_CLEANUP — Remove accidental files from main

Status: completed as emergency repository cleanup.

Summary:

- Removed accidental `_noop_branch_anchor*.txt` files from `main`.
- Removed the accidental `workpackage_claims/scrub_wp_review_copy_polish_implementation.md` claim from `main`.
- Confirmed the accidental files are no longer returned by repository search.
- No product code, UI behavior, export semantics, Scrub Key behavior, reinsert behavior, recognizer logic, benchmark logic, Dockerfile/runtime setup or local packaging changed.

Tests:

- No local tests were run because this was a repository cleanup only.

Validation status:

- Repository search no longer returns `_noop_branch_anchor` or `scrub_wp_review_copy_polish_implementation`.
- GitHub Actions: not checked for cleanup commits.
- Hugging Face sync: not checked for cleanup commits.
- App verification: not applicable because no app behavior changed.

Next recommended step:

- Restart `SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION` only after the repository is confirmed clean.
- Use a fresh branch and claim; do not reuse the removed accidental claim.

---

## SCRUB-WP_MVP_UI_APP_VERIFICATION_CLOSEOUT — MVP UI app verification closeout

Status: completed as verification/closeout-only.

Summary:

- Added `MVP_UI_APP_VERIFICATION_CLOSEOUT.md` to record the currently verified MVP UI baseline.
- Recorded that the current normal app baseline keeps one central side-by-side review surface, visible markers, simple manual missed-value entry, collapsible replacement table, optional step-by-step review, export/download and DOCX hygiene audit.
- Confirmed this package is administrative only and does not change product code, UI behavior, export semantics, Scrub Key semantics, reinsert semantics, recognition logic, benchmark logic, Dockerfile/runtime setup or local packaging.
- Added a namespaced claim file for `SCRUB-WP_MVP_UI_APP_VERIFICATION_CLOSEOUT`.

Tests:

- No local tests were run in this package because it is documentation/closeout-only.
- Prior verification evidence remains recorded for the underlying product changes in `WORKPACKAGES.md` and earlier changelog entries.

Validation status:

- GitHub Actions: unknown from connector for this closeout branch.
- Hugging Face sync: unknown from connector for this closeout branch.
- App verification: not newly requested because no UI behavior changed in this package; existing verified app baseline remains recorded.

Intentionally not changed:

- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- review table flow
- export/download flow
- Scrub Key behavior
- reinsert behavior
- recognizer/benchmark behavior
- local packaging/runtime setup

Next recommended step:

- Do not start a new feature automatically.
- With explicit coordinator approval only: `SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION` or another very small UI simplification package.

---

## WP_MVP_FAST_MANUAL_MASK_ENTRY — Simple manual entry for missed values

Status: completed and verified.

Summary:

- Added `manual_mask_entry.py` as a Streamlit-free helper for manual replacement rows.
- Added helper tests and UI source tests for the manual missed-value flow.
- Wired a simple `Gemiste waarde toevoegen` form into `presidio_streamlit.py` near `3. Controleer gevonden gegevens`.
- Manual rows are added to the existing replacement table and therefore use the existing replacement/export path.
- Manual rows are scoped to the current text with `manual_mask_document_key`.
- Did not change export/download semantics, Scrub Key semantics, reinsert semantics, recognition logic, benchmark logic, Dockerfile or runtime setup.

Tests:

- `tests/test_manual_mask_entry.py` — 11 passed.
- `tests/test_mvp_fast_manual_mask_entry_ui.py` — 8 passed.
- `tests/test_replace_logic_ui_patch.py` — 7 passed.
- `tests/test_review_table_collapsible_contract.py` — 11 passed.
- `tests/test_side_by_side_review_consolidation_dutch_sample.py` — 8 passed.
- `tests/test_export_download_ux_contracts.py` and `tests/test_export_download_ux_implementation.py` — 19 passed.
- `py_compile` reported no errors for touched UI/helper modules.
- `git diff --check` reported no errors.

Validation status:

- GitHub Actions green by coordinator screenshot.
- Hugging Face sync green by coordinator screenshot.
- Live app verified by coordinator screenshot: app starts, manual missed-value form is visible, handmatige rij appears in replacement table, replacement count increased, export and Scrub Key warning remain visible.

---

## WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — Collapse step-by-step review UI

Status: completed and verified.

Summary:

- Made the existing step-by-step review panel collapsed by default under `Stap voor stap controleren`.
- Replaced prototype wording with shorter Dutch user-facing copy.
- Removed the governance/debug caption from the primary UI.
- Renamed the serial review filter to `Filter voor stap-voor-stap controle`.
- Did not change review logic, review table data, export/download behavior, Scrub Key behavior, reinsert behavior, recognizers, benchmark logic, Dockerfile or runtime setup.

Tests:

- Coordinator full suite: `609 passed`.
- GitHub Actions green.
- Hugging Face sync green.
- Live app verified.

---

## WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN — Plan review debug/prototype UI cleanup

Status: completed as planning/design-only.

Summary:

- Added `REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md`.
- Classified visible review/debug/audit UI elements into keep, collapse, rename, audit-only and do-not-change categories.
- Explicitly constrained the next package to interface cleanup only: no new review layer, benchmark gate or export gate.
- Prepared the next implementation package: `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION`.

Tests:

- No product tests required because only planning/governance markdown was changed.

---

## WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — Directly implement grouped export/download UX

Status: completed and verified.

Summary:

- Removed the unreliable export startup-patch route after live app verification stayed old.
- Implemented the grouped export/download section directly in `presidio_streamlit.py`.
- Dockerfile no longer runs the export startup patch.
- Existing export content and behavior are intended unchanged.

Next recommended step:

- `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN` after green Actions, HF sync and app verification.

---

## WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — Implement grouped export/download UX

Status: superseded by direct repair.

Summary:

- Initial startup-patch route was not reliable in the live app.
- Replaced by `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR`.

---

## WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — Add contract tests for professional export/download UX redesign

Status: completed and verified as tests/documentation-only.

Summary:

- Added contract tests and documentation for the professional export/download UX redesign.
- Protected export grouping, key separation, audit/technical detail availability, copy-cleanup direction and no export semantics change.

---

## WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — Plan MVP interface cleanup and professional export/download flow

Status: completed as planning/design-only.

Summary:

- Planned MVP interface cleanup and export/download redesign.
- Updated the active direction toward UI/export polish before further benchmark follow-up.

---

Historical changelog entries remain available in Git history before this planning note.
