# Handover — WP12-FIX — v13.6 Two-mode UI content separation cleanup

Repository: `solidprivacy-nl/scrub`  
Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification

## Summary

WP12-FIX addresses the app-verification issue found after WP12.

WP12 added visible two-mode navigation, but app verification showed that selecting/viewing `Originele waarden terugzetten` still showed much of the anonymization workflow above the reinsert flow.

This cleanup changes the startup patch so the two modes are meaningfully separated:

```text
Anonimiseren
Originele waarden terugzetten
```

The patch now uses a real work-mode selector with conditional rendering:

```text
solidprivacy_work_mode = st.radio(...)
```

When `Originele waarden terugzetten` is selected, the app renders only Scrub Key load + local pasted-text reinsert content. The full anonymization/review/export workflow is rendered under the `Anonimiseren` branch.

## Files added

- `handover/workpackages/20260608_0000_v13_6_two_mode_content_separation_cleanup.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Updated:

```text
tests/test_two_mode_ui_patch.py
```

The updated tests check:

- both mode labels exist;
- conditional work-mode rendering exists;
- reinsert markers are associated with `Originele waarden terugzetten`;
- anonymization markers are associated with the `Anonimiseren` branch;
- reinsert flow is not embedded in the anonymization review/export summary block;
- existing Scrub Key export/import labels remain;
- existing scrubbed download markers remain;
- no TXT upload reinsert UI was added;
- no DOCX upload reinsert UI was added;
- no PDF reinsert was added;
- no AI/cloud/rehydration behavior was added;
- `apply_replacements_to_text` was not altered.

## Validation

Coordinator evidence for prior WP12 showed green Actions/sync:

```text
Tests #145 green — commit 5d879cc
Sync #159 green — commit 5d879cc
Tests #146 green — commit 79d771e
Sync #160 green — commit 79d771e
Tests #147 green — commit e106f7c
Sync #161 green — commit e106f7c
```

However, WP12 app verification found insufficient content separation. WP12-FIX was implemented to address that.

Local clone/test run for WP12-FIX could not be performed in the container because outbound GitHub DNS failed:

```text
Could not resolve host: github.com
```

No local passing test result is claimed.

## GitHub Actions status

Awaiting verification for WP12-FIX commits.

## Hugging Face sync status

Awaiting verification for WP12-FIX commits.

## App verification status

Required because UI behavior changed. Pending coordinator/user verification.

App verification should confirm:

### In `Anonimiseren`

- anonymization workflow is visible;
- source text/file input is visible;
- review table still appears;
- Scrub Key JSON export still appears;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- pasted-text reinsert is not presented as part of the anonymization workflow.

### In `Originele waarden terugzetten`

- anonymization source input is not shown as the main workflow;
- review table is not shown;
- scrubbed export section is not shown;
- `Scrub Key laden` is visible;
- Scrub Key upload/paste validation is visible;
- pasted-text reinsert is visible;
- `Zet originele waarden lokaal terug` works;
- `Herstelde tekst` appears after reinsert;
- `Download herstelde tekst (.txt)` works;
- audit summary / `Controleverslag terugzetten` appears;
- warning about restored sensitive/confidential data is visible;
- local-only/no-AI/no-cloud text is visible.

Also confirm:

- no TXT upload reinsert UI appears yet;
- no DOCX upload reinsert UI appears yet;
- no PDF reinsert appears;
- no AI/cloud behavior appears.

## Boundaries preserved

- `presidio_streamlit.py` was not directly edited.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download semantics intentionally changed inside `Anonimiseren`.
- No Scrub Key JSON export behavior intentionally changed inside `Anonimiseren`.
- No Scrub Key storage, secrets, tokens or real personal data added.

## Remaining risks

- This remains a startup-patch based UI modification, so parallel edits to `fix_streamlit_nested_expanders.py` remain risky.
- The work-mode selector uses `st.radio` rather than full tab body refactoring, because the priority is safe content separation with minimal change.
- App verification is essential to confirm the patch applies cleanly on Hugging Face and that the user-visible flow matches the intended separation.

## Next recommended step

Start closeout after coordinator evidence:

```text
WP12-FIX-CLOSEOUT — v13.6 Two-mode content separation app verification closeout
```

Only after WP12-FIX is verified should the project continue to:

```text
WP13 — v13.7 TXT reinsert upload/download UI
```
