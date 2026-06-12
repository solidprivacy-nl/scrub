# WP42D-FIX3 — Static highlight preview no-expander repair

Status: implemented; awaiting Actions/HF sync/app verification.

## Runtime evidence

The deployed Space showed:

```text
IndentationError: expected an indented block after 'with' statement
```

around the inserted static highlight preview `with st.expander(...)` block.

## Fix

The patch no longer injects a new `with st.expander(...)` wrapper for the preview. It now injects a simple read-only section before the replacement table using:

```text
st.markdown("#### Documentvoorbeeld met markeringen — experimenteel")
st.caption(...)
```

The preview remains directly before the authoritative replacement table.

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

After sync, app verification should confirm the app starts and shows:

```text
Documentvoorbeeld met markeringen — experimenteel
```
