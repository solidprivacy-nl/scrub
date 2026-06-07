# Handover — WP6D — v13.2 Scrub Key import UI app verification closeout

Repository: solidprivacy-nl/scrub  
Workpackage title: WP6D — v13.2 Scrub Key import UI app verification closeout  
Status: completed and app-verified

## Summary

v13.2 Scrub Key import/reload UI has been administratively closed after app verification.

This was a closeout-only workpackage. No code files and no test files were changed.

The coordinator/user confirmed that the Hugging Face app works with the Scrub Key import/reload UI.

## Files added

- `handover/workpackages/20260607_1730_v13_2_scrub_key_import_ui_app_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `fix_streamlit_nested_expanders.py`
- `presidio_streamlit.py`
- `scrub_key.py`
- `scrub_key_import.py`
- `tests/*`

## Tests

No new tests were required or added because this was closeout-only.

Existing technical evidence recorded:

- Tests #89 green — commit `83353e4`.
- Tests #90 green — commit `4a1ef55`.
- Tests #91 green — commit `4d8bfe9`.
- Tests #92 green — commit `ff8321f`.

Existing local/targeted validation recorded in the implementation handover:

- `PYTHONPATH=. pytest -q tests/test_scrub_key.py` -> 6 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_import.py` -> 8 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py` -> 9 passed.
- `PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py` -> 12 passed.
- `PYTHONPATH=. pytest -q` on the available subset -> 35 passed.

## Validation status

Completed.

App verification: confirmed by coordinator/user.

Confirmed app behavior:

- `Scrub Key laden` works.
- Scrub Key import/reload UI is visible.
- Upload/paste import flow works.
- Pseudonymization/reversibility warning is visible.
- Existing `Download Scrub Key (.json)` remains visible.
- Existing TXT, CSV, DOCX and PDF downloads remain available.

## GitHub Actions status

Green based on coordinator evidence:

- Tests #89 green — commit `83353e4`.
- Tests #90 green — commit `4a1ef55`.
- Tests #91 green — commit `4d8bfe9`.
- Tests #92 green — commit `ff8321f`.

## Hugging Face sync status

Green based on coordinator evidence:

- Sync to Hugging Face Space #104 green — commit `4a1ef55`.
- Sync to Hugging Face Space #105 green — commit `4d8bfe9`.
- Sync to Hugging Face Space #106 green — commit `ff8321f`.

## App verification status

Confirmed.

The coordinator/user confirmed:

- `Scrub Key laden` works.
- Upload/paste import flow works.
- Pseudonymization/reversibility warning is visible.
- Existing Scrub Key JSON export remains visible.
- Existing downloads remain available.

## Boundary confirmation

This closeout did not change code and did not add new behavior.

Recorded boundaries:

- No AI-output reinsert behavior was added.
- No automatic document rehydration was added.
- No export/download behavior was intentionally changed.
- Import/reload remains local and uses the existing helper logic.
- The key remains pseudonymization/reversible and must be protected.
- No cloud processing was introduced.
- No secrets or real personal data were stored.

## Remaining risks

- A loaded Scrub Key is sensitive because it makes scrubbed values reversible.
- Deterministic reinsert is not yet implemented as a separate helper/UI flow.
- AI-output reinsert remains a future phase and should not be mixed into import/reload closeout.

## Next recommended step

Start a separate helper-only workpackage for deterministic reinsert:

- build a pure helper that replaces placeholders with original values using a loaded Scrub Key;
- use synthetic tests only;
- do not add UI until helper tests are stable;
- keep AI-output flow separate and explicitly reviewed before UI integration.
