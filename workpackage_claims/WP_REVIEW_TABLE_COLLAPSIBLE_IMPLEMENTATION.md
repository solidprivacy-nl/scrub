# Workpackage claim — WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION

status: blocked/released
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION
started timestamp: 2026-06-15T03:05:00+02:00
released timestamp: 2026-06-15T03:15:00+02:00
scope: implement collapsible `Controleer gevonden gegevens` review table section after green contract tests and coordinator approval
boundaries: keep review table as source of truth/fallback; preserve `replacement_editor`, include, remember, find, replace_with; no export/download, Scrub Key, reinsert, replacement behavior, dependency, cloud processing or real-data changes.
coordinator approval: explicitly provided by user.

reason: blocked because the available GitHub contents connector only supports whole-file replacement for `presidio_streamlit.py`; a manual whole-file replacement of the large central UI file is too risky without a normal repo checkout/line diff.
handover path: `handover/workpackages/20260615_0315_review_table_collapsible_implementation_repair_blocked.md`
tests/checks: no product code changed; no tests run through connector.
GitHub Actions status: not applicable for implementation; no production-code change made.
Hugging Face sync status: not applicable for implementation; no production-code change made.
app verification status: not applicable; UI not changed.
next recommended step: use a worker with repo checkout/Codespaces to apply the controlled `presidio_streamlit.py` diff from the handover, then run tests and app verification.
