# Handover — WP4B — v13.1 Scrub Key JSON export UI integration

Repository: solidprivacy-nl/scrub  
Workpackage title: WP4B — v13.1 Scrub Key JSON export UI integration  
Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification

## Summary

Integrated the existing pure Scrub Key model into the Streamlit startup patch flow as a local JSON download option. The app should now show a `Scrub Key (JSON)` section near the final review/download area and offer `Download Scrub Key (.json)`. The UI includes explicit pseudonymization warnings and does not add import, reload, reinsert or AI-output behavior.

## Files added

- `tests/test_scrub_key_ui_patch.py`
- `handover/workpackages/20260607_1535_v13_1_scrub_key_json_export_ui.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Added patch-level test coverage in `tests/test_scrub_key_ui_patch.py`.

The tests check that:

- Scrub Key helpers are imported by the startup patch.
- `Scrub Key (JSON)` and `Download Scrub Key (.json)` are present.
- the UI uses `edited_replacements_df.copy()` as the source for Scrub Key export.
- timestamp creation happens in the UI/export layer.
- `build_scrub_key`, `scrub_key_to_json` and `validate_scrub_key` are used.
- pseudonymization and non-sharing warnings are present.
- import/reload/reinsert/AI-output flow is not introduced.
- existing final review and export sanity markers remain present.
- existing text export application is not changed by the patch.

## Validation

Local pytest was not run from this connector environment.

Recommended validation commands:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py
PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py
PYTHONPATH=. pytest -q tests/test_export_sanity_ui_patch.py
PYTHONPATH=. pytest -q
```

## GitHub Actions status

Pending / not verified by this worker.

Relevant commits:

- `a9011ccc3fdb981c3101490fdc8b8996696f75e3` — Integrate Scrub Key JSON export into UI patch.
- `adb676000d07e6f00b39a378da40adfa9701e0d1` — Add Scrub Key UI patch tests.
- `7a682b23c2a69a406f93fdf45235e8cde4509a35` — Update workpackage status for Scrub Key UI export.
- `4a2ed4e40083e330372de7b5366f2fb336ba2916` — Record Scrub Key JSON export UI integration.

## Hugging Face sync status

Pending / not verified by this worker.

## App verification status

Pending. Because UI behavior changed, the app should be visually checked in Hugging Face.

Verify that:

- `Scrub Key (JSON)` appears near the final review/download area.
- the pseudonymization warning is visible.
- `Download Scrub Key (.json)` appears.
- existing TXT, CSV, DOCX and PDF downloads still work.

## Notes / risks

- `presidio_streamlit.py` was not directly edited.
- `scrub_key.py` was not changed.
- The pure Scrub Key model remains deterministic and side-effect free.
- Timestamp creation was added in the UI/export layer to satisfy the model validation requirement.
- No Scrub Key import/reload was added.
- No reinsert UI was added.
- No AI-output flow was added.
- No cloud processing was introduced.
- No secrets or real personal data were stored.
- Existing TXT/CSV/DOCX/PDF export/download behavior was not directly changed.

## Next recommended step

Verify GitHub Actions and Hugging Face sync. Then verify the Hugging Face app visually. After v13.1 is confirmed, plan v13.2 Scrub Key import/reload as a separate sequential UI workpackage.
