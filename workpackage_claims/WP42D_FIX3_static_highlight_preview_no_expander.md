# WP42D-FIX3 claim

Workpackage: `WP42D-FIX3 — Static highlight preview no-expander repair`

Status: `completed_awaiting_verification`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Reason: runtime showed IndentationError after inserting the preview as a `with st.expander(...)` block.

Scope completed: minimal UI patch repair. Removed the extra preview expander wrapper and kept the preview read-only/non-authoritative. No export, reinsert, Scrub Key, dependency, cloud processing or real-data changes.

Files added:

```text
WP42D_FIX3_STATUS.md
handover/workpackages/20260612_2325_static_highlight_preview_no_expander_repair.md
```

Files changed:

```text
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
WORKPACKAGES.md
CHANGELOG.md
workpackage_claims/WP42D_FIX3_static_highlight_preview_no_expander.md
```

Expected checks:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

Next recommended step:

```text
Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.
```
