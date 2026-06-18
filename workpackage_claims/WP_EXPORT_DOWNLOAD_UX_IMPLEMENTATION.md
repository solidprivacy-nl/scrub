status: completed_pending_verification
repository: solidprivacy-nl/scrub
workpackage title: WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — Implement professional grouped export/download UX without changing export semantics
started timestamp: 2026-06-18 23:41 Europe/Amsterdam
completed timestamp: 2026-06-18 23:41 Europe/Amsterdam
startup-order-fix timestamp: 2026-06-18 23:49 Europe/Amsterdam
scope: small Streamlit UI implementation for grouped export/download UX
boundaries: no export semantics changes, no Scrub Key contents changes, no reinsert changes, no recognizer changes, no benchmark gates, no product claim

final commit SHA or PR link: 0dda1720bdf724aa4767d874280eedd490728dba
handover path: handover/workpackages/20260618_2341_export_download_ux_implementation.md

files added:
- fix_streamlit_export_download_ux.py
- tests/test_export_download_ux_implementation.py
- EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
- handover/workpackages/20260618_2341_export_download_ux_implementation.md
- workpackage_claims/WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md

files changed:
- Dockerfile
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- RELEASE_NOTES.md
- workpackage_claims/WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md

product-code changes: startup patch added for grouped export/download UI
Streamlit code changes: no direct edit to presidio_streamlit.py; runtime startup patch updates the export/download section before Streamlit starts
export semantics changes: none intended
Scrub Key/reinsert changes: none
thresholds/gates/product claims: none

effects:
- Export section title becomes 5. Exporteer resultaat.
- Document downloads are grouped under Document downloaden.
- Scrub Key is visually separated and warned.
- Audit/technical downloads are grouped under Audit en technische bestanden.
- Existing download data, filenames, MIME types and helpers are preserved.
- Docker startup now keeps the legacy expected patch order substring: fix_streamlit_nested_expanders.py && fix_streamlit_pdf_text_reinsert.py.
- The export UX patch now runs after the existing PDF text reinsert startup patch and before streamlit run.

tests/checks:
- Added tests/test_export_download_ux_implementation.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Coordinator screenshot showed two Dockerfile regression tests failed because the new patch was inserted between existing startup patches.
- Fixed by moving fix_streamlit_export_download_ux.py after fix_streamlit_pdf_text_reinsert.py in the Dockerfile command.
- Required checks: python -m pytest -q tests/test_export_download_ux_contracts.py; python -m pytest -q tests/test_export_download_ux_implementation.py; python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py; python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py; python -m py_compile presidio_streamlit.py; python -m py_compile fix_streamlit_export_download_ux.py; git diff --check.
- Recommended broader check: python -m pytest -q.

GitHub Actions status: pending/unknown after Dockerfile startup-order fix.
Hugging Face sync status: pending/unknown after Dockerfile startup-order fix.
app verification status: required and pending because visible UI changed.

remaining risks:
- Runtime startup patch must apply cleanly in Hugging Face.
- Live app must verify grouped export UI.
- Downloads should be checked for availability after grouping.
- Review/debug labels elsewhere are still not cleaned up.
- Human review remains necessary.

next recommended step after green tests/HF sync/app verification: WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN. Do not start follow-up work automatically.
