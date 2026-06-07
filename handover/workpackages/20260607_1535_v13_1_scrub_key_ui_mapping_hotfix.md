# Handover — WP4B-FIX — Scrub Key UI row mapping hotfix

Repository: solidprivacy-nl/scrub  
Workpackage title: WP4B-FIX — Scrub Key UI row mapping hotfix  
Status: implemented; pending GitHub Actions, Hugging Face sync and app verification

## Summary

Fixed the Scrub Key JSON export mapping bug reported in the Hugging Face app.

The app was showing the Scrub Key JSON section, but export validation failed with messages like:

```text
Item 0 has empty required field: original_value
```

Root cause: the UI passed Streamlit replacement-table rows directly into `build_scrub_key(...)`. Those rows use app/UI column names such as `find` and `replace_with`, while the Scrub Key model expects `original_value` and `placeholder`.

The fix adds an explicit UI mapping layer before `build_scrub_key(scrub_key_rows)`.

## Files added

- `handover/workpackages/20260607_1535_v13_1_scrub_key_ui_mapping_hotfix.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `scrub_key.py`
- `presidio_streamlit.py`
- TXT/CSV/DOCX/PDF export logic

## Implementation details

Added mapping before Scrub Key build:

```text
find -> original_value
replace_with -> placeholder
entity_type -> entity_type
type_label -> type_label
source -> source
review_status -> review_status
include -> include
```

The UI still adds timestamps in the export layer, preserving the pure-model decision that `scrub_key.py` does not create timestamps itself.

The Scrub Key export still follows the v13.0 excluded-row policy:

```text
excluded_rows_policy = omitted
```

This means only selected rows are included in the key.

## Tests

Updated:

- `tests/test_scrub_key_ui_patch.py`

The tests now verify:

- `find` maps to `original_value` before `build_scrub_key(...)`;
- `replace_with` maps to `placeholder` before `build_scrub_key(...)`;
- required review fields are mapped;
- Scrub Key warning text remains present;
- `Download Scrub Key (.json)` remains present;
- no import/reload, reinsert or AI-output behavior is introduced;
- existing export/download markers remain present;
- no `st.stop()` or blocking behavior is added.

## Validation status

Local pytest was not run from this connector environment.

Required validation commands:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py
PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py
PYTHONPATH=. pytest -q
```

## GitHub Actions status

Pending / not yet verified for this hotfix.

Commits created in this hotfix:

- `8321fef67f3649c5b64d0963033ed6676aea2134` — Fix Scrub Key UI row mapping.
- `da3c47e58d353c8423aaeff37438b6016a76f63c` — Add Scrub Key UI mapping regression tests.
- `05a172a143ba45e8678b4234567de2cf4fa75b33` — Record Scrub Key UI mapping hotfix status.
- `17e79ecbbff65aa6df6b6942f0f841c02855f844` — Log Scrub Key UI mapping hotfix.

## Hugging Face sync status

Pending / not yet verified for this hotfix.

## App verification status

Pending.

Need to verify in the Hugging Face app that:

- the Scrub Key JSON download no longer shows `Item has empty required field: original_value`;
- `Download Scrub Key (.json)` works;
- TXT, CSV, DOCX and PDF downloads still work;
- the pseudonymization warning remains visible.

## Remaining risks

- The hotfix is in `fix_streamlit_nested_expanders.py`, which already carries several sequential UI patches. Future UI work should remain sequential and careful.
- The actual Hugging Face runtime still needs app-level verification after sync.
- GitHub Actions and sync still need to be checked for the latest hotfix commits.

## Next recommended step

Verify GitHub Actions and Hugging Face sync for the latest hotfix commit, then test the Hugging Face app with reviewed replacement rows and download the Scrub Key JSON.
