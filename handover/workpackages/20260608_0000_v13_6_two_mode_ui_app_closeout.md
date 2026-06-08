# Handover — WP12B — v13.6 Two-mode UI app verification closeout

Repository: `solidprivacy-nl/scrub`  
Status: completed and app-verified after Actions/sync verification

## Summary

WP12B administratively closes the v13.6 two-mode UI line.

Closed sequence:

- WP12 introduced the two-mode UI skeleton.
- WP12-FIX cleaned up content separation.
- WP12-FIX2 fixed the generated indentation/runtime error around `Scrub Key laden`.
- WP12B records successful GitHub Actions, Hugging Face sync and app verification.

The previous blocking runtime error was:

```text
IndentationError: unexpected indent
File "/home/user/app/presidio_streamlit.py", line 380
    st.markdown("**Scrub Key laden**")
```

This is now verified fixed in the app.

## Files added

- `handover/workpackages/20260608_0000_v13_6_two_mode_ui_app_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Code files changed

None.

This was a closeout-only workpackage.

## Tests

No new tests were added or changed in WP12B.

Existing technical verification evidence from the coordinator:

```text
Tests #155 green — commit b27d115
Sync to Hugging Face Space #169 green — commit b27d115

Tests #156 green — commit 0e357bb
Sync to Hugging Face Space #170 green — commit 0e357bb

Tests #157 green — commit 268234d
Sync to Hugging Face Space #171 green — commit 268234d
```

Latest verified WP12-FIX2 commit:

```text
268234d9d1aeb9c82658c4c30702f51cfdd58c96
```

## Validation status

GitHub Actions: green based on coordinator evidence.  
Hugging Face sync: green based on coordinator evidence.  
App verification: confirmed by coordinator/user.

## App verification status

Confirmed.

Coordinator/user verified:

- The app starts without Script execution error.
- No `IndentationError` appears.
- `Originele waarden terugzetten` mode is visible and selectable.
- In `Originele waarden terugzetten`, the full anonymization workflow is no longer shown above the reinsert flow.
- `Scrub Key laden` is visible.
- Scrub Key upload/paste is visible.
- `Valideer en laad Scrub Key` is visible.
- Local pasted-text reinsert section is visible.
- Warning about restored sensitive/confidential values is visible.
- Local-only / no-AI / no-cloud text is visible.
- Text field for reinsert is visible.
- Button `Zet originele waarden lokaal terug` is visible.
- No TXT upload reinsert UI appears.
- No DOCX upload reinsert UI appears.
- No PDF reinsert appears.
- No AI/cloud behavior appears.

Also recorded:

- `Anonimiseren` mode remains available.
- Existing anonymization workflow remains available in `Anonimiseren`.
- Existing Scrub Key export/import remains available.
- Existing pasted-text reinsert remains available.

## Boundaries preserved

- No code files changed.
- `fix_streamlit_nested_expanders.py` was not changed in WP12B.
- `presidio_streamlit.py` was not changed.
- `scrub_key_document_reinsert.py` was not changed.
- `scrub_key_reinsert.py` was not changed.
- `scrub_key.py` was not changed.
- `scrub_key_import.py` was not changed.
- No test files were changed.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior intentionally changed.
- No Scrub Key export/import behavior intentionally changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- None for the WP12B closeout itself.
- Future UI work should remain sequential because `fix_streamlit_nested_expanders.py` and Streamlit workflow state are still sensitive patch areas.
- WP13 should be started only as a separate workpackage.

## Next recommended step

```text
WP13 — v13.7 TXT reinsert upload/download UI
```

WP13 should remain limited to TXT reinsert upload/download UI and must not introduce DOCX upload reinsert UI, PDF reinsert, AI/cloud behavior or export semantic changes.
