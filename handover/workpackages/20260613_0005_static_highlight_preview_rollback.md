# Handover — WP42D rollback

Repository: `solidprivacy-nl/scrub`

Workpackage: `WP42D-ROLLBACK — Restore stable Scrub Legal startup`

Status: implemented; app verification pending.

Summary: the experimental static highlight preview startup step was removed from normal app startup. The regular table-first review interface is the target state again.

Files changed:

- `Dockerfile`
- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`

Tests: not run through connector.

Expected check: `pytest tests/test_static_highlight_preview_ui_integration_patch.py`.

Validation: Hugging Face rebuild and app screenshot still needed.

GitHub Actions: not visible through connector.

Hugging Face sync: pending.

App verification: pending.

Remaining risk: the optional highlight preview is no longer active.

Next step: verify that the normal Scrub Legal interface loads again.
