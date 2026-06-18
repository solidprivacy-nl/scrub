status: completed_pending_verification
repository: solidprivacy-nl/scrub
workpackage title: WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — Add contract tests for professional export/download UX redesign
started timestamp: 2026-06-18 22:39 Europe/Amsterdam
completed timestamp: 2026-06-18 22:39 Europe/Amsterdam
wording-fix timestamp: 2026-06-18 23:23 Europe/Amsterdam
scope: tests/documentation-only contract tests for export/download UX redesign
boundaries: no product UI implementation, no Streamlit code changes, no export semantics changes, no Scrub Key changes, no reinsert changes, no recognizer changes, no benchmark gates, no product claim

final commit SHA or PR link: d069f9af9ade880e363094c31bfdaf0d187976bc
handover path: handover/workpackages/20260618_2239_export_download_ux_contract_tests.md

files added:
- EXPORT_DOWNLOAD_UX_CONTRACTS.md
- tests/test_export_download_ux_contracts.py
- handover/workpackages/20260618_2239_export_download_ux_contract_tests.md
- workpackage_claims/WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- tests/test_export_download_ux_contracts.py
- handover/workpackages/20260618_2239_export_download_ux_contract_tests.md
- workpackage_claims/WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS.md

product-code changes: none
Streamlit code changes: none
export semantics changes: none
Scrub Key/reinsert changes: none
recognizer/benchmark changes: none
thresholds/gates/product claims: none

effects:
- Added contract tests and documentation for the professional export/download UX redesign.
- Locked grouping direction: Document downloaden, Scrub Key, Audit en technische bestanden.
- Protected Scrub Key separation and warning concepts.
- Protected audit/technical details availability as secondary layers.
- Protected no export semantics change boundary.
- Protected implementation route.
- Fixed brittle wording assertion by accepting both no benchmark gate and no benchmark gates wording.

tests/checks:
- Added tests/test_export_download_ux_contracts.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Coordinator screenshot showed first attempt failed on exact singular wording No benchmark gate while docs used plural/equivalent wording.
- Required checks after fix: python -m pytest -q tests/test_export_download_ux_contracts.py; python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py; python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py; python -m py_compile presidio_streamlit.py; git diff --check.
- Recommended broader check: python -m pytest -q.

GitHub Actions status: pending/unknown after wording fix.
Hugging Face sync status: pending/unknown after wording fix.
app verification status: not required; no app behavior changed.

remaining risks:
- Export/download UX is contract-protected but not implemented yet.
- Current app still has loose download buttons until implementation.
- Audit/technical details still need professional grouping in a later package.
- Scrub Key must remain visibly sensitive in implementation.
- Export semantics must remain unchanged in implementation.
- Human review remains necessary.

next recommended step after green tests and sync: WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION. Do not start follow-up work automatically.
