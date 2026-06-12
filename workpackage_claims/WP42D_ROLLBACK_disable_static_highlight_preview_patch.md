# WP42D rollback claim

Workpackage: `WP42D-ROLLBACK — Restore stable Scrub Legal startup`

Status: `completed_awaiting_verification`

Repository: `solidprivacy-nl/scrub`

Files added:

```text
handover/workpackages/20260613_0005_static_highlight_preview_rollback.md
```

Files changed:

```text
Dockerfile
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
WORKPACKAGES.md
```

Expected check:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py
```

Next step:

```text
Verify that the normal Scrub Legal interface loads again after Hugging Face rebuild.
```
