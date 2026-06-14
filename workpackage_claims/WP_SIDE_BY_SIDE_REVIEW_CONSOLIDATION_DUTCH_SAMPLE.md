# Workpackage claim — WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE

status: in_progress_partial
repository: solidprivacy-nl/scrub
workpackage title: WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE
started timestamp: 2026-06-15T00:55:00+02:00
scope: Consolidate duplicate preview surfaces into one central side-by-side review surface and replace English fallback demo text with longer Dutch synthetic legal text.

partial progress:
- demo_text.txt was safely updated on main with longer Dutch synthetic legal sample text.
- UI consolidation in presidio_streamlit.py was not completed.
- The old upper Invoer / Directe voorbeeldweergave still exists on main.
- The lower side-by-side review surface still exists through serial_review_panel_ui.py.
- Do not mark this workpackage completed yet.

known issue:
- A previous low-level create_tree/create_commit attempt created detached commit objects, but main was not moved to those commits. They do not affect the app.
- Continue only with small GitHub.update_file commits or a clean local patch workflow.

boundaries:
- no export/download behavior change
- no export blocking
- no Scrub Key writes or schema changes
- no reinsert behavior change
- no dependency change
- no cloud processing
- no real data
- no click-to-mark
- no advanced editor
- no full-document marking
- no startup source mutation

next recommended step:
- Continue with small, testable changes.
- First add tests for the intended consolidation.
- Then modify serial_review_panel_ui.py to allow suppressing its side-by-side block.
- Then carefully modify presidio_streamlit.py so the central side-by-side review appears once above the review table and the old Directe voorbeeldweergave is removed.
