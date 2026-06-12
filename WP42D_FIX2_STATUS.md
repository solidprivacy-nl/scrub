# WP42D-FIX2 — Static highlight preview anchor repair

Status: implemented; awaiting Actions/HF sync/app verification.

## Runtime evidence

The deployed Space failed fast with:

```text
RuntimeError: Could not insert static highlight preview block before replacement editor.
```

This means the fail-fast guard worked, but the WP42D-FIX insertion anchor was still too strict after the startup patch chain.

## Fix

The patch now anchors on the single replacement-editor line:

```text
edited_replacements_df = st.data_editor(
```

This is less fragile than matching the preceding dataframe line plus editor line together.

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

After sync, app verification should confirm that the app starts and the anonymization review flow shows:

```text
Documentvoorbeeld met markeringen — experimenteel
```
