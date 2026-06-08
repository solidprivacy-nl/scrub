# Handover — WP13B — v13.7 TXT reinsert upload/download UI app verification closeout

Repository: `solidprivacy-nl/scrub`  
Status: implemented; Actions/sync verified; awaiting app verification

## Summary

WP13B is a closeout-only workpackage for the v13.7 TXT reinsert upload/download UI.

The coordinator supplied technical evidence that GitHub Actions and GitHub to Hugging Face sync are green for the WP13 implementation line.

However, the closeout request did not include confirmed Hugging Face app verification results. Therefore WP13 is not marked as fully completed/app-verified yet.

Recorded status:

```text
implemented; Actions/sync verified; awaiting app verification
```

## Files added

- `handover/workpackages/20260608_0000_v13_7_txt_reinsert_upload_download_ui_app_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Code files changed

None.

This was closeout-only. No code or test files were changed.

## Tests

No new tests were added or changed in WP13B.

Existing technical verification evidence from the coordinator:

```text
Tests #164 green — commit e442d28
Sync to Hugging Face Space #178 green — commit e442d28

Tests #165 green — commit ce7721d
Sync to Hugging Face Space #179 green — commit ce7721d

Tests #166 green — commit 6bf359f
Sync to Hugging Face Space #180 green — commit 6bf359f

Tests #167 green — commit 443d6af
Sync to Hugging Face Space #181 green — commit 443d6af
```

Latest WP13 implementation commit:

```text
443d6af99cfac47ed007d0d1cd666d1549e855d5
```

## Validation status

GitHub Actions: green based on coordinator evidence.  
Hugging Face sync: green based on coordinator evidence.  
App verification: pending.

## App verification status

Pending.

Required app verification before full WP13 closure:

### In `Originele waarden terugzetten`

- `Scrub Key laden` remains visible.
- Scrub Key upload/paste validation remains visible.
- Pasted-text reinsert remains visible.
- `TXT-bestand terugzetten` is visible.
- TXT upload accepts `.txt`.
- `Zet TXT-bestand lokaal terug` works with a valid Scrub Key.
- `Herstelde TXT-tekst` appears.
- `Download hersteld TXT-bestand (.txt)` works.
- `Controleverslag TXT terugzetten` appears.
- Warning about restored sensitive/confidential data is visible.
- Local-only / no-AI / no-cloud text is visible.

### In `Anonimiseren`

- normal anonymization workflow remains available;
- source text/file input remains visible;
- review table appears;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- Scrub Key JSON export remains available;
- TXT reinsert upload UI is not shown as part of the anonymization workflow.

### Also confirm

- no DOCX upload reinsert UI appears yet;
- no PDF reinsert appears;
- no AI/cloud behavior appears;
- existing Scrub Key export/import remains available;
- existing scrubbed export/download semantics are unchanged.

## Boundaries preserved

- No code files changed.
- `fix_streamlit_nested_expanders.py` was not changed in WP13B.
- `presidio_streamlit.py` was not changed.
- `scrub_key_document_reinsert.py` was not changed.
- `scrub_key_reinsert.py` was not changed.
- `scrub_key.py` was not changed.
- `scrub_key_import.py` was not changed.
- No test files were changed in WP13B.
- No UI changes were added in WP13B.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior intentionally changed.
- No Scrub Key export/import behavior intentionally changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- WP13 remains pending app verification.
- Do not start WP14 until TXT reinsert upload/download UI is verified in the Hugging Face app.
- The next action should be app verification only, not new feature development.

## Next recommended step

```text
WP13B-APPVERIFY — v13.7 TXT reinsert upload/download UI app verification completion
```

After app verification is confirmed, WP13 can be closed as:

```text
completed and app-verified after Actions/sync verification
```
