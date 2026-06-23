# Workpackage claim — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

repo=solidprivacy-nl/scrub
workpackage=SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION
status=in_progress
branch=scrub-reinsert-interface-simplification

Approved scope decision:
- Coordinator approved route A on 2026-06-23.
- Existing reinsert UI may be migrated out of `fix_streamlit_nested_expanders.py` into direct `presidio_streamlit.py` source.
- `fix_streamlit_nested_expanders.py` may be touched only to prevent duplicate startup injection / retire the migrated reinsert UI injection.
- The visible reinsert flow may then be simplified.

Scope:
- simplify visible reinsert UI flow
- migrate existing reinsert UI to direct `presidio_streamlit.py` source
- prevent duplicate startup injection after migration
- no reinsert helper logic change
- no Scrub Key JSON semantics change
- no warning or acknowledgement weakening
- no export filename/content/mime changes
- no cloud, AI, OCR or PDF reconstruction changes
- no recognizer/benchmark behavior change
