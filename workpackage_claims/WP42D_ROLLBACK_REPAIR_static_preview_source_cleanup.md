# Workpackage claim — WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup

Status: completed
Repository: solidprivacy-nl/scrub
Workpackage: WP42D-ROLLBACK-REPAIR — Static preview source cleanup / HF startup repair
Started: 2026-06-13
Completed: 2026-06-13

## Scope completed

Repaired the continuing Hugging Face startup problem where the Space still showed a stale static highlight preview script error in `presidio_streamlit.py` after the rollback line.

## Evidence

Coordinator/user screenshot showed Hugging Face stuck on Restarting with a script execution error pointing to:

```text
/home/user/app/presidio_streamlit.py line 1081
st.caption("Alleen-lezen voorbeeld. De vervangtabel blijft leidend voor beslissingen, Scrub Key en export.")
```

GitHub `main` no longer contains that stale block, so the repair focused on forcing Hugging Face to rebuild a clean runtime image and guarding against stale preview text returning to the app source.

## Commits

- `9ffa350` — Force HF rebuild after static preview rollback.
- `063ad91` — Guard against stale static preview app source.
- `a3f43b2` — Record WP42D rollback source cleanup repair.
- `f73abd2` — Document WP42D rollback source cleanup repair.
- `2d0a574` — Add handover.

## Handover

`handover/workpackages/20260613_0030_wp42d_rollback_source_cleanup_repair.md`

## Tests/checks

Local pytest execution via the ChatGPT GitHub connector was not available.

Expected targeted check:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py
```

Expected broader check:

```text
pytest
```

## Validation status

- Static review completed against the coordinator-provided HF error evidence.
- GitHub Actions: pending/unknown after final commit.
- Hugging Face sync: pending/unknown after final commit.
- App verification: pending.

## Boundaries preserved

No new highlight preview UI, replacement UI implementation, export/download change, Scrub Key change, reinsert change, dependency change, cloud processing or real-data fixture.

## Next recommended step

Verify GitHub Actions and Hugging Face sync. Then hard refresh the Space and confirm the normal Scrub Legal interface starts without the script execution error.
