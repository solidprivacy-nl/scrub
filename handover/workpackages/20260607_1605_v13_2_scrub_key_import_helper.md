# Handover — WP5 v13.2 Scrub Key import/reload helper and tests

Repository: solidprivacy-nl/scrub  
Status: helper and tests implemented; awaiting GitHub Actions and Hugging Face sync confirmation

## Summary

This workpackage implemented the first v13.2 Scrub Key import/reload layer as pure helper/test work.

No UI files were changed. No reinsert behavior was added. No AI-output flow was added.

## Repository worked in

- `solidprivacy-nl/scrub`

## Workpackage title

- `WP5 — v13.2 Scrub Key import/reload helper and tests`

## Status

- Helper implemented.
- Tests implemented.
- Project control files updated.
- Local pytest was not run from this connector environment.
- GitHub Actions and Hugging Face sync need confirmation.

## Files added

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`
- `handover/workpackages/20260607_1605_v13_2_scrub_key_import_helper.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Main changes

### `scrub_key_import.py`

Added pure helper functions for loading a previously downloaded Scrub Key JSON string:

- `validate_scrub_key_import_text(json_text) -> list[str]`
- `normalise_scrub_key_items(scrub_key) -> list[dict]`
- `build_scrub_key_import_result(json_text) -> dict`

The helper:

- parses Scrub Key JSON text;
- validates the structure using existing `scrub_key.validate_scrub_key(...)`;
- returns safe Dutch user-facing errors for:
  - empty JSON text;
  - invalid JSON syntax;
  - invalid top-level format;
  - invalid Scrub Key content;
- normalizes imported items into review-table-like mapping rows containing both model fields and app-style fields:
  - `original_value` and `find`;
  - `placeholder` and `replace_with`;
  - `entity_type`;
  - `type_label`;
  - `source`;
  - `review_status`;
  - `include` and `include_state`;
  - `timestamp`;
  - `document_label`;
- returns a UI-friendly result shape with:
  - `ok`;
  - `errors`;
  - `warnings`;
  - `scrub_key`;
  - `mapping_rows`;
  - `item_count`;
  - `reversible`;
  - `privacy_model`;
  - `document_label`.

### `tests/test_scrub_key_import.py`

Added tests for:

- valid Scrub Key JSON import;
- normalized row mapping;
- local-key privacy warning;
- empty JSON text;
- invalid JSON syntax;
- invalid top-level format;
- structural validation errors;
- no input mutation;
- synthetic Dutch legal values only.

### `WORKPACKAGES.md`

Updated WP5 from planned to:

```text
helper and tests implemented; awaiting GitHub Actions and Hugging Face sync confirmation
```

Also added the next planned UI workpackage:

```text
WP5B — v13.2 Scrub Key import/reload UI integration
```

### `CHANGELOG.md`

Added the v13.2 helper/test entry and recorded boundaries.

## Tests

Not run locally in this connector environment.

Required validation:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py
PYTHONPATH=. pytest -q tests/test_scrub_key_import.py
```

Preferred validation:

```bash
PYTHONPATH=. pytest -q
```

## GitHub Actions status

Pending / not checked at handover time.

## Hugging Face sync status

Pending / not checked at handover time.

## App verification status

Not required for this helper-only workpackage because no UI behavior changed.

## Boundaries preserved

- No UI changes.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No edit to existing Scrub Key export UI.
- No reinsert behavior.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.
- No real personal data in tests.
- No change to TXT, CSV, DOCX or PDF download behavior.

## Remaining risks

- GitHub Actions must validate the new tests.
- Hugging Face sync should still be checked even though no UI behavior changed.
- Future UI import/reload must keep the Scrub Key warning visible and must not store keys server-side.
- Deterministic reinsert should remain a separate later workpackage.

## Next recommended step

1. Confirm GitHub Actions tests for the latest commit.
2. Confirm Hugging Face sync for the latest commit.
3. If green, close out WP5 helper if desired.
4. Then start `WP5B — v13.2 Scrub Key import/reload UI integration` as a separate sequential UI workpackage.
