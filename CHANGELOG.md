# Changelog — SolidPrivacy Scrub

## WP42D-FIX4 — Static highlight preview stale-block cleanup repair

Status: implemented UI patch cleanup repair; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `WP42D_FIX4_STATUS.md`
- `workpackage_claims/WP42D_FIX4_static_highlight_preview_cleanup.md`
- `handover/workpackages/20260612_2340_static_highlight_preview_cleanup_repair.md`

Files changed:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_FIX4_static_highlight_preview_cleanup.md`

Summary:

- User runtime evidence kept showing the old indentation error after the no-expander patch.
- Diagnosis: the running container can already contain a stale broken preview block in `presidio_streamlit.py`; if the preview title is present, the patch skipped reinsertion and left the broken block in place.
- Repaired `fix_streamlit_static_highlight_preview.py` to always remove any existing static highlight preview block before inserting the current safe no-expander block.
- Cleanup removes from the preview-title line through the replacement editor anchor, then reinserts the safe current block before the authoritative replacement table.
- Updated static tests to assert stale preview cleanup logic exists.
- Preserved read-only, non-authoritative, helper-gated rendering with escaped text only.
- No export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py`.
- App verification required after Actions and Hugging Face sync because visible UI behavior should change.

Next recommended step:

- Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42D-FIX3 — Static highlight preview no-expander repair.
- WP42D-FIX2 — Static highlight preview anchor repair.
- WP42D-FIX — Static highlight preview visibility repair.
- WP28C app evidence — Scrub Key warning UI screenshot.
- WP42D-INVESTIGATE — Static highlight preview panel not visible.
- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP43 — Frontend architecture decision.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
