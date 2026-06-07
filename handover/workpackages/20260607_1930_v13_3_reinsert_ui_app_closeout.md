# Handover — WP8C — v13.3 Deterministic reinsert UI app verification closeout

Repository: solidprivacy-nl/scrub  
Workpackage title: WP8C — v13.3 Deterministic reinsert UI app verification closeout  
Status: completed and app-verified after Actions/sync verification

## Summary

Administratively closed v13.3 deterministic reinsert UI after technical verification and app verification.

This was a closeout-only workpackage. No code files, test files, UI behavior, export/download behavior or Scrub Key import/export behavior were changed in this closeout.

The coordinator/user confirmed that the Hugging Face app shows the deterministic local reinsert UI and that reinsert works with a valid Scrub Key.

## Files added

- `handover/workpackages/20260607_1930_v13_3_reinsert_ui_app_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `fix_streamlit_nested_expanders.py`
- `presidio_streamlit.py`
- `scrub_key_reinsert.py`
- `scrub_key.py`
- `scrub_key_import.py`
- `tests/*`

## Tests

No new tests were required or run because this was closeout-only.

Existing validation recorded from WP8B:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py tests/test_scrub_key_reinsert_ui_patch.py tests/test_scrub_key_import_ui_patch.py tests/test_scrub_key_ui_patch.py
```

Result:

```text
57 passed
```

## Validation status

Completed.

Recorded validation:

- Local validation recorded in WP8B: 57 passed.
- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: confirmed by coordinator/user.

## GitHub Actions status

Green based on coordinator evidence:

- Tests #120 green — commit `7725182`.
- Tests #121 green — commit `84f5312`.
- Tests #122 green — commit `1a8e87e`.

## Hugging Face sync status

Green based on coordinator evidence:

- Sync to Hugging Face Space #134 green — commit `7725182`.
- Sync to Hugging Face Space #135 green — commit `84f5312`.
- Sync to Hugging Face Space #136 green — commit `1a8e87e`.

## App verification status

Confirmed by coordinator/user.

Confirmed app behavior:

- `Originele waarden terugzetten` is visible.
- Warning about sensitive/confidential information is visible.
- Local-only / no-AI / no-cloud text is visible.
- Text input works.
- Button `Zet originele waarden lokaal terug` works.
- Reinsert works with a valid Scrub Key.
- Placeholders are correctly restored.
- Result message appears: `37 waarde(n) lokaal teruggezet.`
- `Herstelde tekst` appears with restored original values.

## Closeout notes

Recorded in `WORKPACKAGES.md` and `CHANGELOG.md`:

- v13.3 deterministic reinsert UI is implemented.
- GitHub Actions tests are green.
- GitHub to Hugging Face sync is green.
- App verification is confirmed.
- Restored output may contain sensitive/confidential information again.
- Existing Scrub Key export remains available.
- Existing Scrub Key import/reload remains available.
- Existing TXT, CSV, DOCX and PDF scrubbed downloads remain available, based on prior verification and no intentional export changes.
- No AI calls were added.
- No cloud processing was added.
- No automatic document rehydration was added.
- No DOCX/PDF reinsert was added.
- No existing scrubbed export/download behavior was intentionally changed.

## Boundary confirmation

This closeout did not change code.

Confirmed boundaries:

- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No UI changes.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No TXT, CSV, DOCX or PDF export/download behavior changes.
- No Scrub Key export/import behavior changes.
- No secrets, tokens or real personal data stored.

## Remaining risks

- Restored text can contain personal or confidential information and must be manually reviewed before sharing.
- Scrub Keys remain sensitive because they make scrubbed values reversible.
- AI-output-specific workflow decisions remain future work and should be explicitly reviewed before adding any AI-specific behavior.

## Next recommended step

Start WP9 — AI-output reinsert workflow review as a planning/review-only workpackage. Keep AI/cloud behavior out unless explicitly approved, and preserve existing export/download and Scrub Key import/export semantics.
