# Handover — WP4 — v13.0 Scrub Key specification and pure model

Repository: solidprivacy-nl/scrub  
Status: completed / implemented; pending GitHub Actions and Hugging Face sync confirmation

## Summary

Implemented the v13.0 Scrub Key foundation as a specification plus pure Python model. The work prepares the future Scrub Key / Reinsert phase without touching the active review UI.

The model builds a deterministic local mapping from reviewed rows, serializes/deserializes JSON, and validates the required structure. Excluded rows are omitted according to the v13.0 spec.

## Files added

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`
- `handover/workpackages/20260607_1342_v13_0_scrub_key_spec_model.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Added `tests/test_scrub_key.py`
- Covered valid key creation from reviewed rows.
- Covered excluded-row omission policy.
- Covered required mapping fields.
- Covered JSON roundtrip.
- Covered validation for missing/empty required fields.
- Covered synthetic Dutch legal examples only.

## Validation

- Local targeted test: `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- Full local test run: not run, because the full repository could not be cloned in the local container environment.
- GitHub Actions: pending / unknown after commit.
- Hugging Face sync: pending / unknown after commit.
- App verification: not applicable; no UI files were touched.

## Notes / risks

- `presidio_streamlit.py` was not touched.
- `fix_streamlit_nested_expanders.py` was not touched.
- No export/download button was added.
- No reinsert UI was added.
- No cloud processing was introduced.
- No real personal data or secrets were stored.
- The pure model does not generate timestamps itself; timestamps must be supplied by the caller and validation catches missing timestamps.

## Next recommended step

- Confirm GitHub Actions and Hugging Face sync after the commit.
- Continue with v12.6 export sanity checks if not already completed, or plan the next v13 UI workpackage for Scrub Key JSON export after v12 is stable.
