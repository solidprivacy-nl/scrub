# Changelog — SolidPrivacy Scrub

## WP_MVP_FAST_MANUAL_MASK_ENTRY — Simple manual entry for missed values

Status: completed_pending_verification.

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

- GitHub Actions pending/unknown.
- Hugging Face sync pending/unknown.
- Live app verification pending.

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
