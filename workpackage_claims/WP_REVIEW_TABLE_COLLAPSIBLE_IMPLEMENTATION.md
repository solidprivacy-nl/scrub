# Workpackage claim — WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION

status: blocked/released
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION
started timestamp: 2026-06-15T03:05:00+02:00
restarted timestamp: 2026-06-15T04:05:00+02:00
blocked timestamp: 2026-06-15T11:15:00+02:00
scope: implement collapsible `Controleer gevonden gegevens` review table section after green contract tests and coordinator approval
boundaries: keep review table as source of truth/fallback; preserve `replacement_editor`, include, remember, find, replace_with; no export/download, Scrub Key, reinsert, replacement behavior, dependency, cloud processing or real-data changes.
coordinator approval: explicitly provided by user.
previous status: blocked/released because a prior worker did not safely apply the central UI patch through the connector.
current status note: coordinator-approved takeover attempted, but safe production implementation could not be completed through the ChatGPT GitHub connector without risking an unsafe full-file overwrite or hidden startup/monkeypatch behavior.

handover path: handover/workpackages/20260615_1115_review_table_collapsible_implementation_takeover_blocked.md
partial artifact: `review_table_collapsible_ui.py` added as a non-runtime helper; it is not wired into production UI.
tests/checks: no shell/pytest execution available through the ChatGPT GitHub connector; no completed runtime UI implementation.
GitHub Actions status: not applicable for a completed implementation because implementation is blocked.
Hugging Face sync status: not applicable for a completed implementation because implementation is blocked.
app verification status: not applicable; no completed runtime UI change available to verify.
next recommended step: use a worker/environment that can safely edit `presidio_streamlit.py` as a complete file and run tests; do not use startup source mutation, global monkeypatching or hidden side effects for this UI change.
