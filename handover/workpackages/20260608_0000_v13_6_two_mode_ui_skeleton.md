# Handover — WP12 — v13.6 Two-mode UI skeleton and tab separation

Repository: `solidprivacy-nl/scrub`  
Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification

## Summary

WP12 implemented the first two-mode UI skeleton through the existing startup patch flow.

The app now gets a visible mode-choice skeleton near the top of the UI:

```text
Anonimiseren
Originele waarden terugzetten
```

The implementation is intentionally minimal. It adds visible Streamlit tabs and captions without a full landing-page refactor and without moving all app content into separate tab bodies yet.

Existing anonymization, Scrub Key export/import, pasted-text reinsert and scrubbed export/download behavior were preserved.

## Files added

- `tests/test_two_mode_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_6_two_mode_ui_skeleton.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Added patch-level tests in:

```text
tests/test_two_mode_ui_patch.py
```

The tests check:

- `Anonimiseren` is present;
- `Originele waarden terugzetten` is present;
- `st.tabs` and tab variables are present;
- existing Scrub Key export/import labels remain present;
- existing pasted-text reinsert labels remain present;
- existing anonymization/download markers remain present;
- existing scrubbed download behavior markers are not rewired;
- no TXT upload reinsert UI was added;
- no DOCX upload reinsert UI was added;
- no PDF reinsert was added;
- no AI/cloud/rehydration behavior was added;
- `apply_replacements_to_text` was not altered.

Required local validation was attempted conceptually, but a real repo clone/test run could not be performed in the container because outbound GitHub DNS failed:

```text
Could not resolve host: github.com
```

Therefore no local passing test result is claimed.

## Validation status

- Local tests: not run successfully because repository clone was unavailable due DNS/outbound GitHub resolution failure.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required; pending.

## GitHub Actions status

Awaiting verification.

## Hugging Face sync status

Awaiting verification.

## App verification status

Required because UI behavior changed. Pending coordinator/user verification.

App verification should confirm:

- `Anonimiseren` mode is visible;
- `Originele waarden terugzetten` mode is visible;
- anonymization workflow still works;
- review table still appears;
- Scrub Key JSON export still appears;
- Scrub Key import/reload still appears;
- pasted-text reinsert still works;
- `Download herstelde tekst (.txt)` still works;
- existing scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- no TXT/DOCX upload reinsert UI appears yet;
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
- No existing TXT, CSV, DOCX or PDF scrubbed export/download semantics intentionally changed.
- No Scrub Key export/import behavior intentionally changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- The patch is intentionally skeleton-only: the full existing app content is not yet structurally moved into tab bodies.
- App verification is required to confirm the startup patch applies cleanly on Hugging Face.
- The current patch-based UI remains sensitive to parallel edits in `fix_streamlit_nested_expanders.py`.
- If the tabs create layout confusion in practice, WP12B should record the issue before moving on to TXT/DOCX upload UI.

## Next recommended step

Start closeout after coordinator evidence:

```text
WP12B — v13.6 Two-mode UI skeleton app verification closeout
```

WP12B should verify:

- GitHub Actions tests;
- GitHub to Hugging Face sync;
- Hugging Face app behavior.

Only after WP12 is verified should the project continue to:

```text
WP13 — v13.7 TXT reinsert upload/download UI
```
