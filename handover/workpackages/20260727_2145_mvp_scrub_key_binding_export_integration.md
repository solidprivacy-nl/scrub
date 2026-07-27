# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

## Status

Completed; final GitHub Actions passed; ready to merge.

## Files added

- `scrub_key_bound_export.py`
- `tests/test_scrub_key_bound_export.py`
- `tests/test_mvp_scrub_key_binding_export_integration.py`
- `output/validation/mvp_scrub_key_binding_export_validation.json`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_export_integration.md`
- `handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md`

## Files changed

- `document_tools.py`
- `manual_mask_entry.py`
- `presidio_streamlit.py`
- `tests/test_basic_expert_review_mode_implementation.py`
- `tests/test_basic_mode_declutter_implementation.py`
- `tests/test_execution_interface_simplification_ui.py`
- `tests/test_mvp_fast_manual_mask_entry_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Stable per-scope binding ID.
- Automatic, candidate, remembered and manual bound placeholders.
- Schema-1.1 key and canonical digest validation.
- Custom replacement preservation and verified-key blocking.
- Stable document filenames/MIME types and no new confirmation gates.
- Targeted helper/model/contract/manual/UI/roundtrip validation: 103 passed.
- Full repository regression: 881 passed.

## Validation

- Targeted validation: passed.
- Final normal GitHub Actions run #1757: passed on `cae60425894c23c05dd5705b41304ed0c32ee274`.
- Temporary operator, diagnostic workflow, trigger and logs: removed before final validation.
- Hugging Face sync: pending after merge.
- App verification: required after export and reinsert integration are both deployed.

## Notes / risks

- Reinsert does not yet enforce binding; that remains the immediate next package.
- Legacy v1.0 keys remain supported only as explicit unbound compatibility after reinsert integration.
- Mapping digest is not malicious-tampering authenticity.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Merge PR #44, verify GitHub-to-Hugging-Face sync, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.
