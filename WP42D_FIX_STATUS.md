# WP42D-FIX — Static highlight preview visibility repair

Status: implemented; awaiting Actions/HF sync/app verification.

## User verification input

The Hugging Face Space runs and the core Scrub Legal UI is visible, but the experimental static highlight preview panel is not visible in the current app.

Expected visible label:

```text
Documentvoorbeeld met markeringen — experimenteel
```

## Root cause

The WP42D patch inserted the preview by searching for an old/stale anchor around:

```text
Technische details bij de vervangtabel
```

That block no longer exists in the current app flow before the replacement table. Because the patch helper used a no-op replacement when the anchor was missing, the deployed app could continue without the preview being inserted.

## Fix

`fix_streamlit_static_highlight_preview.py` now anchors insertion on the stable current app sequence:

```text
replacement_editor_df = pd.DataFrame(default_editor_rows)
edited_replacements_df = st.data_editor(
```

The patch now raises a `RuntimeError` if it cannot insert the helper import or the preview block. This prevents a silent successful startup without the expected panel.

## Boundaries preserved

The repaired panel remains:

- read-only;
- non-authoritative;
- helper-gated;
- escaped-text only;
- not export-blocking;
- not Scrub Key changing;
- not reinsert changing;
- not cloud-processing;
- not real-data based.

## Expected validation

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

App verification is required after GitHub Actions and Hugging Face sync because this affects visible UI behavior.
