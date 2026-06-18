status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — Plan MVP interface cleanup and professional export/download flow
started timestamp: 2026-06-18 22:34 Europe/Amsterdam
completed timestamp: 2026-06-18 22:34 Europe/Amsterdam
scope: planning/design/specification-only for MVP UI cleanup and export/download redesign
boundaries: no product UI implementation, no Streamlit code changes, no export semantics changes, no Scrub Key changes, no reinsert changes, no recognizer changes, no benchmark gates, no product claim

final commit SHA or PR link: 25116550ace0d90264ae5ba79b16150744147c33
handover path: handover/workpackages/20260618_2234_mvp_ui_cleanup_and_export_redesign_plan.md

files added:
- MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
- handover/workpackages/20260618_2234_mvp_ui_cleanup_and_export_redesign_plan.md
- workpackage_claims/WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md

files changed:
- ROADMAP.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- DECISION_LOG.md
- workpackage_claims/WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md

product-code changes: none
Streamlit code changes: none
export semantics changes: none
Scrub Key/reinsert changes: none
recognizer changes: none
benchmark/gate changes: none
product claim: none

effects:
- Planned MVP interface cleanup and export/download redesign.
- Temporarily parked recall/benchmark follow-up packages unless a concrete blocker appears.
- Defined new active next direction: export/download UX first, then debug/audit collapse, then copy polish.
- Defined target export grouping with document downloads, separate Scrub Key area, and secondary audit/technical downloads.
- Preserved safety boundaries: review table source of truth, Scrub Key sensitivity, audit details remain available, no export semantics change.

tests/checks:
- No pytest required; planning/design-only.
- git diff --check was not runnable in this connector-only environment.

GitHub Actions status: pending/unknown at closeout time.
Hugging Face sync status: pending/unknown at closeout time.
app verification status: not required; no app behavior changed.

remaining risks:
- UI/export redesign is planned but not implemented.
- Current app still contains prototype/debug-like labels until follow-up implementation packages run.
- Export/download buttons are still functionally separate until redesigned.
- Audit details must remain available during cleanup.
- Human review remains necessary.

next recommended step: WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS after separate coordinator approval. Do not start follow-up work automatically.
