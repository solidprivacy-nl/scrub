# Handover — WP42D-FIX Static highlight preview visibility repair

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP42D-FIX — Static highlight preview visibility repair`

Status: implemented; awaiting Actions/HF sync/app verification.

## Summary

User app verification showed the Hugging Face Space runs, but the expected experimental panel `Documentvoorbeeld met markeringen — experimenteel` was not visible.

Root cause: `fix_streamlit_static_highlight_preview.py` used a stale insertion anchor around `Technische details bij de vervangtabel`. That block no longer exists before the replacement editor in the current app flow, so the patch could silently skip insertion.

Fix: the patch now anchors on the stable current sequence directly before `edited_replacements_df = st.data_editor(...)`. It now raises `RuntimeError` if it cannot insert the helper import or preview block.

## Files added

- `WP42D_FIX_STATUS.md`
- `workpackage_claims/WP42D_FIX_static_highlight_preview_visibility.md`
- `handover/workpackages/20260612_2235_static_highlight_preview_visibility_fix.md`

## Files changed

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`

## Tests

Updated:

```text
tests/test_static_highlight_preview_ui_integration_patch.py
```

Expected validation:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

No tests were run in the live GitHub checkout because the connector does not provide shell execution.

## Validation

- GitHub Actions: pending / not visible through connector at handover time.
- Hugging Face sync: pending / not visible through connector at handover time.
- App verification: pending; requires screenshot showing `Documentvoorbeeld met markeringen — experimenteel` in anonymization mode.

## Notes / risks

- This is a UI patch repair and needs app verification after sync.
- If the patch fails at startup, the Space may show an error instead of silently missing the panel; this is intentional fail-fast behavior.
- No export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior was changed.

## Next recommended step

Verify GitHub Actions, Hugging Face sync and app screenshot showing the experimental preview panel.

## Intentionally not changed

- No review table decision behavior changed.
- No export/download behavior changed.
- No Scrub Key behavior changed.
- No reinsert behavior changed.
- No dependency changed.
- No cloud processing added.
- No real data added.
