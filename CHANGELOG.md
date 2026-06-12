# Changelog — SolidPrivacy Scrub

## WP42D-FIX2 — Static highlight preview anchor repair

Status: implemented UI patch anchor repair; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `WP42D_FIX2_STATUS.md`
- `workpackage_claims/WP42D_FIX2_static_highlight_preview_anchor.md`
- `handover/workpackages/20260612_2310_static_highlight_preview_anchor_repair.md`

Files changed:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_FIX2_static_highlight_preview_anchor.md`

Summary:

- User runtime evidence showed the first fix now fails fast with `RuntimeError: Could not insert static highlight preview block before replacement editor.`
- This confirms the fail-fast guard worked, but the two-line insertion anchor was still too strict after the startup patch chain.
- Repaired `fix_streamlit_static_highlight_preview.py` to anchor on only the replacement editor line: `edited_replacements_df = st.data_editor(`.
- This keeps the preview directly before the authoritative replacement table while avoiding dependency on the preceding dataframe line.
- Updated static tests to assert the single-line editor anchor and fail-fast guards.
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

- WP42D-FIX — Static highlight preview visibility repair.
- WP28C app evidence — Scrub Key warning UI screenshot.
- WP42D-INVESTIGATE — Static highlight preview panel not visible.
- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP43 — Frontend architecture decision.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
