# Handover — WP6C — v13.2 Scrub Key import UI verification and closeout

Repository: solidprivacy-nl/scrub  
Workpackage title: WP6C — v13.2 Scrub Key import UI verification and closeout  
Status: completed and formally closed after Actions/sync verification; app verification pending user/coordinator confirmation

## Summary

This was a closeout-only workpackage. No code files were changed.

The v13.2 Scrub Key import/reload UI workpackage is administratively closed based on coordinator evidence that GitHub Actions tests and GitHub to Hugging Face sync are green.

## Files added

- `handover/workpackages/20260607_1715_v13_2_scrub_key_import_ui_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

No new tests were run or added because this was closeout-only.

Existing coordinator evidence recorded:

- Tests #89 green — commit `83353e4`.
- Tests #90 green — commit `4a1ef55`.
- Sync to Hugging Face Space #104 green — commit `4a1ef55`.
- Tests #91 green — commit `4d8bfe9`.
- Sync to Hugging Face Space #105 green — commit `4d8bfe9`.
- Tests #92 green — commit `ff8321f`.
- Sync to Hugging Face Space #106 green — commit `ff8321f`.

## Validation

GitHub Actions: green based on coordinator evidence.  
Hugging Face sync: green based on coordinator evidence.  
App verification: pending user/coordinator confirmation.

## Closeout notes

- Scrub Key import/reload UI was implemented.
- Existing Scrub Key JSON export remains in place.
- Import/reload remains local and uses existing helper logic.
- The key remains pseudonymization/reversible and must be protected.
- No AI-output reinsert behavior was added.
- No automatic document rehydration was added.
- Existing TXT, CSV, DOCX and PDF downloads were not intentionally changed.

## Boundaries preserved

No changes were made to:

- `fix_streamlit_nested_expanders.py`
- `presidio_streamlit.py`
- `scrub_key.py`
- `scrub_key_import.py`
- `tests/*`

No reinsert behavior was added.  
No AI-output flow was added.  
No export/download behavior was changed.  
No cloud processing was introduced.  
No secrets, tokens or real personal data were stored.

## Remaining risks

- App verification is still pending unless the coordinator/user separately confirms the visual state in Hugging Face.
- The next phase should not jump directly to AI-output UI. Deterministic reinsert helper work should come first.

## Next recommended step

Ask the coordinator/user to visually confirm in Hugging Face:

- `Scrub Key laden` is visible;
- import/reload warning is visible;
- existing Scrub Key export is still visible;
- existing TXT, CSV, DOCX and PDF downloads remain available.

After visual verification, start a separate deterministic reinsert helper workpackage.
