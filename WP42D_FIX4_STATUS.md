# WP42D-FIX4 — Static highlight preview stale-block cleanup repair

Status: implemented; awaiting Actions/HF sync/app verification.

## Runtime evidence

The deployed Space kept showing the old indentation error after WP42D-FIX3. This suggests the running container had already been patched with the stale broken preview block, and the newer patch skipped reinsertion because the preview title was already present.

## Fix

`fix_streamlit_static_highlight_preview.py` now always removes any previously inserted static highlight preview block before inserting the current safe no-expander block.

Cleanup behavior:

```text
find preview title
remove from the preview-title line up to the replacement editor anchor
insert current no-expander preview before the replacement editor
```

## Boundaries preserved

- Read-only preview.
- Non-authoritative preview.
- Helper-gated rendering.
- Escaped text only.
- No export behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

## Expected validation

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

After sync/restart, app verification should confirm the app starts and shows:

```text
Documentvoorbeeld met markeringen — experimenteel
```
