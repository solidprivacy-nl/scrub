# Workpackage claim — WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE
started timestamp: 2026-06-15T11:35:00+02:00
completed timestamp: 2026-06-15T11:35:00+02:00
reason: coordinator requested a manually renameable candidate file after the direct runtime implementation retry was blocked by safe full-file edit constraints.
scope: create a candidate copy file for manual replacement testing without changing active `presidio_streamlit.py` or runtime startup behavior.
boundaries: active app file remains unchanged; no Docker CMD change; no startup patch; no Streamlit monkeypatch; no export/download, Scrub Key, reinsert, replacement behavior, dependency, cloud processing or real-data changes.

final commit SHA or PR link: 3322cd62489bd6ccb5ac750210ee228e2458d28c
handover path: handover/workpackages/20260615_1135_review_table_collapsible_candidate_file.md

files added:
- presidio_streamlit_collapsible_candidate.py
- tests/test_review_table_collapsible_candidate_file.py
- workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md
- handover/workpackages/20260615_1135_review_table_collapsible_candidate_file.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md

tests/checks: no shell/pytest execution available through ChatGPT GitHub connector. Static candidate tests added. Expected: python -m py_compile presidio_streamlit_collapsible_candidate.py; pytest tests/test_review_table_collapsible_candidate_file.py; pytest tests/test_review_table_collapsible_contract.py; pytest tests/test_side_by_side_review_ui_patch.py; pytest tests/test_side_by_side_review_consolidation_dutch_sample.py; python -m pytest -q tests.
GitHub Actions status: pending / unknown at claim completion time.
Hugging Face sync status: pending / unknown at claim completion time.
app verification status: not applicable until candidate is manually promoted to active presidio_streamlit.py on a branch/local clone.
remaining risks: candidate file has not been executed; active app is unchanged; startup compatibility patches must be checked after manual promotion.
next recommended step: wait for Actions, then manually promote candidate on a branch/local clone, run py_compile/pytest, and verify app screenshot before replacing active app in main.
