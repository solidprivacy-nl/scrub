# Changelog — SolidPrivacy Scrub

## WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — Directly implement grouped export/download UX

Status: completed, pending verification.

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
