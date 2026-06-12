# Changelog — SolidPrivacy Scrub

## WP42D-FIX — Static highlight preview visibility repair

Status: implemented UI patch repair; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `WP42D_FIX_STATUS.md`
- `workpackage_claims/WP42D_FIX_static_highlight_preview_visibility.md`
- `handover/workpackages/20260612_2235_static_highlight_preview_visibility_fix.md`

Files changed:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP42D_FIX_static_highlight_preview_visibility.md`

Summary:

- User app verification showed the Hugging Face Space runs but the expected experimental static highlight preview panel is not visible.
- Root cause found: the WP42D patch targeted a stale `Technische details bij de vervangtabel` anchor that is no longer present before the replacement editor in the current app flow.
- Repaired `fix_streamlit_static_highlight_preview.py` to insert the panel using the stable current app anchor directly before `edited_replacements_df = st.data_editor(...)`.
- Added fail-fast `RuntimeError` guards if the helper import or preview block cannot be inserted, preventing silent startup without the expected panel.
- Updated static tests to assert the stable anchor exists in `presidio_streamlit.py`, the stale anchor is not used, and fail-fast guards exist.
- Preserved read-only, non-authoritative, helper-gated rendering with escaped text only.
- No export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py`.
- App verification required after Actions and Hugging Face sync because visible UI behavior should change.

Next recommended step:

- Verify GitHub Actions, Hugging Face sync and app screenshot showing `Documentvoorbeeld met markeringen — experimenteel`.

## WP28C app evidence — Scrub Key warning UI screenshot

Status: partial app evidence recorded.

Files added:

- `WP28C_APP_EVIDENCE_SCRUB_KEY_WARNING_UI.md`
- `workpackage_claims/WP28C_app_evidence_scrub_key_warning_ui.md`
- `handover/workpackages/20260612_2025_scrub_key_warning_ui_app_evidence.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP28C_app_evidence_scrub_key_warning_ui.md`

Summary:

- Coordinator provided a screenshot of the running app in mode `Originele waarden terugzetten`.
- The screenshot shows Scrub Key loading, Scrub Key warning text, acknowledgement checkbox before validating/loading the key, original-values reinsert warning and TXT/DOCX/PDF-to-TXT reinsert warning sections.
- DOCX and PDF limitation warnings are visible.
- Buttons are gated by acknowledgement/input state.
- The screenshot itself was not stored in the repository.
- This screenshot is useful partial evidence for WP28C reinsert-warning behavior, but it does not verify WP42D because WP42D belongs to the anonymization review flow.

Remaining verification needs:

- Full GitHub Actions evidence.
- Hugging Face sync evidence.
- App verification coverage for all expected WP28C warning/acknowledgement surfaces.

## WP42D-INVESTIGATE — Static highlight preview panel not visible

Status: diagnosis completed; superseded by WP42D-FIX.

Summary:

- Added an investigation report.
- Confirmed the WP42D patch file exists and contains the expected preview label and safety gates.
- Confirmed repository `Dockerfile` includes the static highlight preview patch command before `streamlit run`.
- Confirmed raw `presidio_streamlit.py` does not contain the panel because WP42D is a startup patch, not a direct source edit.
- Initial diagnosis suggested runtime/sync or insufficient patch-chain diagnostics.
- WP42D-FIX later identified and repaired the stale insertion anchor.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP43 — Frontend architecture decision.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
- WP42C — Static highlight preview UI planning.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
