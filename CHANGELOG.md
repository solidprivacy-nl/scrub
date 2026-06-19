# Changelog — SolidPrivacy Scrub

## WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — Collapse step-by-step review UI

Status: completed pending verification.

Summary:

- Made the existing step-by-step review panel collapsed by default under `Stap voor stap controleren`.
- Replaced prototype wording with shorter Dutch user-facing copy.
- Removed the governance/debug caption from the primary UI.
- Renamed the serial review filter to `Filter voor stap-voor-stap controle`.
- Did not change review logic, review table data, export/download behavior, Scrub Key behavior, reinsert behavior, recognizers, benchmark logic, Dockerfile or runtime setup.

Tests:

- Coordinator-side test run required.
- Recommended focused tests are listed in the workpackage handover.

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
