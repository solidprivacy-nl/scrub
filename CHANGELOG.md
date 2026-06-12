# Changelog — SolidPrivacy Scrub

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

Status: diagnosis completed; no fix implemented.

Files added:

- `WP42D_INVESTIGATION_REPORT.md`
- `workpackage_claims/WP42D_INVESTIGATE_static_highlight_preview_not_visible.md`
- `handover/workpackages/20260612_2010_static_highlight_preview_investigation.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_INVESTIGATE_static_highlight_preview_not_visible.md`

Summary:

- Checked for an existing WP42D-INVESTIGATE claim before starting; none existed.
- Added an investigation report.
- Confirmed the WP42D patch file exists and contains the expected preview label and safety gates.
- Confirmed repository `Dockerfile` includes the static highlight preview patch command before `streamlit run`.
- Confirmed raw `presidio_streamlit.py` does not contain the panel because WP42D is a startup patch, not a direct source edit.
- Confirmed `fix_streamlit_nested_expanders.py` creates the upstream review-table anchor used by the WP42D patch.
- Most likely diagnosis: the running Hugging Face app is not using the WP42D-patched runtime yet, or the patch-chain needs stronger diagnostics/fail-fast checks.
- No UI, code behavior, tests, runtime behavior, export/download behavior, Scrub Key behavior, reinsert behavior, cloud processing or real data changed.

Next recommended step:

- `WP42D-FIX — Static highlight preview deployment/patch-chain hardening`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP43 — Frontend architecture decision.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
- WP42C — Static highlight preview UI planning.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
