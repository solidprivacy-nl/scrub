# Workpackage claim — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-11 12:24 Europe/Amsterdam

Branch: scrub-manual-correction-panel-density-implementation

Scope:
- Make the existing collapsed `Gemiste waarde toevoegen` panel materially shorter, calmer and less form-like.
- Remove the duplicate internal heading.
- Group the existing value, type and replacement controls in one compact row.
- Preserve all validation, session-state, replacement-table, export, Scrub Key and reinsert behavior.

Primary implementation file:
- `presidio_streamlit.py`

Explicit boundaries:
- No recognizer changes.
- No replacement semantics changes.
- No export payload, filename or MIME changes.
- No Scrub Key JSON changes.
- No reinsert changes.
- No document-processing changes.
- No runtime/startup patches.
- No dependency changes.

Next step:
- Implement the compact panel layout and run the required narrow guardrails.
