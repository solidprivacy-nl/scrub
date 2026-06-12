# WP42D-FIX claim

Workpackage: `WP42D-FIX — Static highlight preview visibility repair`

Status: `completed_awaiting_verification`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Reason: user app verification showed the experimental static highlight preview was not visible in the deployed Space.

Scope completed: investigated and repaired the WP42D patch anchor. Preserved read-only/non-authoritative behavior. No export, reinsert, Scrub Key, dependency, cloud processing or real-data changes.

Files added:

```text
WP42D_FIX_STATUS.md
handover/workpackages/20260612_2235_static_highlight_preview_visibility_fix.md
```

Files changed:

```text
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
RELEASE_NOTES.md
workpackage_claims/WP42D_FIX_static_highlight_preview_visibility.md
```

Root cause:

```text
The patch used a stale insertion anchor around `Technische details bij de vervangtabel`; the current app flow anchors the replacement editor directly after `replacement_editor_df = pd.DataFrame(default_editor_rows)`.
```

Expected checks:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

Next recommended step:

```text
Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.
```
