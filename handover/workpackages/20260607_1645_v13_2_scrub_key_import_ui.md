# Handover — WP6 — v13.2 Scrub Key import/reload UI integration

Repository: solidprivacy-nl/scrub  
Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification

## Summary

Integrated the existing v13.2 Scrub Key import/reload helper into the Streamlit startup patch flow. The UI now adds a `Scrub Key laden` section near the existing Scrub Key JSON export block.

The user can upload a Scrub Key JSON file or paste JSON text, validate it, see pseudonymization/local-protection warnings, and load validated mapping rows into the current replacement table after a visible button click.

## Files added

- `tests/test_scrub_key_import_ui_patch.py`
- `handover/workpackages/20260607_1645_v13_2_scrub_key_import_ui.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Added patch-level tests for:

- import helper usage;
- `Scrub Key laden` UI label;
- upload and paste input paths;
- pseudonymization/reversibility warning text;
- validation before loading;
- visible user action before mapping rows are loaded;
- preservation of existing Scrub Key JSON export;
- preservation of existing download/export markers;
- no direct change to `apply_replacements_to_text`;
- no TXT/CSV/DOCX/PDF download mutation inside the patch.

## Validation

Local targeted validation on the reconstructed connector subset passed:

- `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_import.py` → 8 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py` → 9 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py` → 12 passed.
- `PYTHONPATH=. pytest -q` on the available subset → 35 passed.

GitHub Actions: pending / unknown after latest commits.  
Hugging Face sync: pending / unknown after latest commits.  
App verification: pending.

## Notes / risks

- `presidio_streamlit.py` was not directly edited.
- The change is implemented through `fix_streamlit_nested_expanders.py`, consistent with the current startup patch flow.
- No AI-output behavior was added.
- No deterministic reinsert behavior was added.
- No automatic document rehydration was added.
- No silent replacement of current review rows occurs; import requires the visible `Valideer en laad Scrub Key` action.
- Existing TXT, CSV, DOCX and PDF download behavior was not changed.
- Existing Scrub Key JSON export behavior was kept.
- No cloud processing, server-side key storage, secrets, tokens or real personal data were introduced.

## Next recommended step

- Verify GitHub Actions and Hugging Face sync for the latest commits.
- Ask the coordinator/user to verify in the Hugging Face app that `Scrub Key laden` is visible and can load a valid previously exported Scrub Key.
- After import/reload is stable, implement the deterministic reinsert helper as a separate non-UI workpackage.
