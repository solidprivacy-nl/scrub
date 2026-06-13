# Workpackage claim — WP_SERIAL_REVIEW_UI

status: in_progress
repository: solidprivacy-nl/scrub
workpackage title: WP_SERIAL_REVIEW_UI — Small non-destructive serial review panel in Streamlit
started timestamp: 2026-06-13T12:30:00+02:00
coordinator approval: explicit
scope: Small controlled Streamlit UI implementation that shows a non-destructive serial review panel using review_panel_view_model.py while preserving the existing table-first review table as source of truth and fallback.
boundaries:
- No startup source mutation.
- No use of fix_streamlit_static_highlight_preview.py.
- No startup patch that mutates presidio_streamlit.py.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No inline editing.
- No Word/PDF layout rendering.
- No review table mutation.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No export blocking.
- No reinsert behavior change.
- No export/download behavior change.
- No dependency change.
- No cloud processing.
- No real data.
