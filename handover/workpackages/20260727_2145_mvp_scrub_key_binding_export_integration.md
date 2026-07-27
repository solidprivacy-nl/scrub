# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

## Status

Implemented; targeted validation passed; final PR verification pending.

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
- Full repository regression pending final normal GitHub Actions run.

## Validation

- Targeted validation: passed.
- Temporary operator and diagnostic log: removed before final PR validation.
- GitHub Actions: final clean-branch run pending.
- Hugging Face sync: pending after merge.
- App verification: required after export and reinsert integration are both deployed.

## Notes / risks

- Reinsert does not yet enforce binding; that remains the immediate next package.
- Legacy v1.0 keys remain supported only as explicit unbound compatibility after reinsert integration.
- Mapping digest is not malicious-tampering authenticity.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Merge after the final normal GitHub Actions run passes, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.
