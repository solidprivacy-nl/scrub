# Workpackage claim — WP_REVIEW_SURFACE_CONTROL_CLEANUP_ACTIONS_FIX

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_SURFACE_CONTROL_CLEANUP_ACTIONS_FIX
started timestamp: 2026-06-15T02:15:00+02:00
completed timestamp: 2026-06-15T02:15:00+02:00
scope: Repair/verify tests that still appeared to expect the old marker label and visible sync-scroll checkbox after the approved review surface control cleanup.

final commit SHA or PR link: 618afec19ab71446779aca575bd385e421820151
handover path: handover/workpackages/20260615_0215_review_surface_control_cleanup_actions_fix.md

tests/checks: No shell/pytest execution available through ChatGPT GitHub connector. Current main inspection confirms stale expectations from the screenshot are no longer present in tests/test_review_highlight_toggle_ui_patch.py and tests/test_side_by_side_sync_scroll_prototype.py. Expected: pytest tests/test_review_highlight_toggle_ui_patch.py; pytest tests/test_side_by_side_sync_scroll_prototype.py; pytest tests/test_side_by_side_review_ui_patch.py; python -m pytest -q tests.
GitHub Actions status: pending / unknown for this claim completion commit.
Hugging Face sync status: pending / unknown for this claim completion commit.
app verification status: not applicable; no app behavior changed in this repair package.
next recommended step: Wait for the new Actions run and inspect the latest failing run if tests remain red.
