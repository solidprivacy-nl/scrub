# Workpackage claim — WP42D-ROLLBACK-CLOSEOUT

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP42D-ROLLBACK-CLOSEOUT — Working table-first interface restored after failed static highlight preview
started timestamp: 2026-06-13 11:16 Europe/Amsterdam
completed timestamp: 2026-06-13 11:16 Europe/Amsterdam
scope: Documentation-only closeout to record that the Hugging Face app is back on the stable table-first Scrub interface and that the failed static-highlight/marking attempt is rolled back/parked.
boundaries: No product code changes; no changes to presidio_streamlit.py, fix_streamlit_nested_expanders.py, Dockerfile, dependencies, UI implementation, replacement decision UI, export/download, Scrub Key, reinsert, cloud processing, or real data.
final commit SHA or PR link: 7a3118c7da360b9b011f2d5ea2c84ff2e2d3395e
handover path: handover/workpackages/20260613_1116_wp42d_rollback_closeout.md
tests/checks: Documentation/textual checks only. Required files read; claim created via GitHub.create_file; central planning checked and updated so it no longer points to restarting the old static-highlight startup mutation route. No shell/pytest execution available through ChatGPT GitHub connector.
GitHub Actions status: Unknown / not required for runtime validation in this documentation-only closeout. Workflow tools returned no runs for the initial claim commit at check time; doc commits may still trigger later workflows.
Hugging Face sync status: Unknown / not required for app verification in this documentation-only closeout because no runtime/UI code changed.
app verification status: Not applicable for this closeout commit; coordinator/user-provided instruction supplied working table-first app evidence being recorded.
next recommended step: WP_SERIAL_REVIEW_HELPER — pure helper/tests for serial review queue; then WP_SERIAL_REVIEW_UI only after helper/tests and explicit approval.
