# Workpackage claim — WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup

Status: in_progress
Repository: solidprivacy-nl/scrub
Workpackage: WP42D-ROLLBACK-REPAIR — Static preview source cleanup / HF startup repair
Started: 2026-06-13

## Scope

Repair the continuing Hugging Face startup error that still points to a stale static highlight preview block in `presidio_streamlit.py`.

## Evidence

Coordinator/user screenshot shows Hugging Face stuck on Restarting with a script execution error pointing to:

```text
/home/user/app/presidio_streamlit.py line 1081
st.caption("Alleen-lezen voorbeeld. De vervangtabel blijft leidend voor beslissingen, Scrub Key en export.")
```

## Boundaries

- Remove/guard stale static preview source only.
- Restore normal table-first app startup.
- No new highlight preview UI.
- No replacement UI implementation.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.
