# Handover — WP4C-FIX v13.1 Scrub Key JSON export verification and closeout

Repository: solidprivacy-nl/scrub  
Status: completed and app verified

## Summary

This closeout administratively completed v13.1 Scrub Key JSON export after the mapping hotfix was verified in the Hugging Face app.

No code files were changed in this closeout. Only project control files and this handover were updated.

## Repository worked in

- `solidprivacy-nl/scrub`

## Workpackage title

- `WP4C-FIX — v13.1 Scrub Key JSON export verification and closeout`

## Status

- Completed.
- GitHub Actions evidence was provided by the coordinator.
- Hugging Face sync evidence was provided by the coordinator.
- App verification was provided by the user/coordinator.

## Files added

- `handover/workpackages/20260607_1550_v13_1_scrub_key_json_export_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `fix_streamlit_nested_expanders.py`
- `presidio_streamlit.py`
- `scrub_key.py`
- `tests/test_scrub_key.py`
- `tests/test_scrub_key_ui_patch.py`

## Tests

No new tests were added or run in this administrative closeout.

Relevant prior test evidence:

- Initial v13.1 UI implementation:
  - `Tests #73` green for commit `9d349bb`.
  - `Sync to Hugging Face Space #87` green for commit `9d349bb`.
- Mapping hotfix:
  - `Tests #78` green for commit `8d33941`.
  - `Sync to Hugging Face Space #92` green for commit `8d33941`.

## Validation status

App verification passed.

The user verified in the Hugging Face app that:

- `Scrub Key (JSON)` is visible.
- the pseudonymization / reversibility warning is visible.
- the earlier `Item has empty required field: original_value` error is gone.
- `Download Scrub Key (.json)` is visible.
- Scrub Key JSON download works.

## GitHub Actions status

Green, based on coordinator evidence:

- `Tests #78` green for commit `8d33941`.

## Hugging Face sync status

Green, based on coordinator evidence:

- `Sync to Hugging Face Space #92` green for commit `8d33941`.

## App verification status

Passed.

## Boundaries preserved

- No edit to `scrub_key.py` in the mapping hotfix closeout.
- No direct edit to `presidio_streamlit.py`.
- No Scrub Key import/reload.
- No reinsert UI.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.
- No change to TXT, CSV, DOCX or PDF export/download behavior.
- No change to existing replacement/export semantics.
- No `st.stop()` or export blocking behavior added.

## Remaining risks

- Scrub Key import/reload is not implemented yet.
- Reinsert workflow is not implemented yet.
- The Scrub Key file is sensitive because it makes replacements reversible; user-facing warning exists, but later phases should keep emphasizing local protected handling.
- `fix_streamlit_nested_expanders.py` now carries multiple staged UI patches; future UI work should remain sequential and careful.

## Next recommended step

Start v13.2 as helper/test work first:

```text
WP5 — v13.2 Scrub Key import/reload helper and tests
```

Do not start reinsert UI or AI-output flow yet. First implement reliable Scrub Key import/reload validation and normalization.
