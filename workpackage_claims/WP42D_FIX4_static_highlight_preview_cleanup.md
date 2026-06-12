# WP42D-FIX4 claim

Workpackage: `WP42D-FIX4 — Static highlight preview stale-block cleanup repair`

Status: `completed_awaiting_verification`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Reason: runtime still showed the old broken preview block, likely because a previous startup patch already modified `presidio_streamlit.py` in the running container and the new patch skipped reinsertion when the title was present.

Scope completed: minimal startup patch cleanup repair. Removes stale inserted preview blocks before inserting the safe no-expander preview. No export, reinsert, Scrub Key, dependency, cloud processing or real-data changes.

Files added:

```text
WP42D_FIX4_STATUS.md
handover/workpackages/20260612_2340_static_highlight_preview_cleanup_repair.md
```

Files changed:

```text
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
WORKPACKAGES.md
CHANGELOG.md
workpackage_claims/WP42D_FIX4_static_highlight_preview_cleanup.md
```

Expected checks:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

Next recommended step:

```text
Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.
```
