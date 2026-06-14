# Workpackage claim — WP_REVIEW_SURFACE_CONTROL_CLEANUP

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_SURFACE_CONTROL_CLEANUP
started timestamp: 2026-06-15T02:00:00+02:00
completed timestamp: 2026-06-15T02:00:00+02:00
scope: Simplify central side-by-side review controls. Default markers on. Remove visible sync control. Keep synchronized scrolling as normal behavior.

final commit SHA or PR link: 97d72d67ae483037698d32a98a69583f4ec9ed22
handover path: handover/workpackages/20260615_0200_review_surface_control_cleanup.md

done commits:
- claim created: 0730c9dceff6d07cb20baf57d48c08e8a4c9017d
- renderer cleanup: 93fa4d8781352bdb523b78eb95a1592fdaa44cab
- UI patch tests: 886c06d33df0a9e0f0d680572d19016983304a81
- consolidation tests: 8a6fb9c3f5c291e08e6140ab486aef991eece822
- workpackages: bd5ffbb10dc34d8fbb117c975b2feb7e2d6a5056
- changelog: aa02d4eb689bd77acac8779e1018db622f52fc83
- decision log: 86d77c57fa25a5e9b447b11d8a05584527fac799
- release notes: 12799644652ce633302951e501fe23d2f1fc46ba
- handover: 97d72d67ae483037698d32a98a69583f4ec9ed22

tests/checks: Updated tests/test_side_by_side_review_ui_patch.py and tests/test_side_by_side_review_consolidation_dutch_sample.py. No shell/pytest execution available through ChatGPT GitHub connector. Expected: pytest tests/test_side_by_side_review_ui_patch.py; pytest tests/test_side_by_side_review_consolidation_dutch_sample.py; python -m pytest -q tests.
GitHub Actions status: pending / unknown at claim completion time.
Hugging Face sync status: pending / unknown at claim completion time.
app verification status: pending and required because UI behavior changed.
next recommended step: Verify Actions and Hugging Face sync, then perform app verification screenshot.
