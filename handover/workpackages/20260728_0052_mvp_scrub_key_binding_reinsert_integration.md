# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

## Status

Completed; final GitHub Actions passed; merge, sync and live app verification pending.

## Files added

- `scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_integration.py`
- `tests/test_scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_ui.py`
- `output/validation/mvp_scrub_key_binding_reinsert_validation.json`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_reinsert_integration.md`
- `handover/workpackages/20260728_0052_mvp_scrub_key_binding_reinsert_integration.md`

## Files changed

- `scrub_key_import.py`
- `scrub_key_reinsert.py`
- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `tests/test_scrub_key_binding_model.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Bound key import and metadata.
- Correct bound match and verified status.
- Wrong-key mismatch, mixed document IDs and missing document binding.
- Legacy key for bound document and bound key for legacy document.
- Mapping-digest tampering.
- Explicit legacy unbound compatibility.
- TXT, DOCX body/header/footer and PDF-to-TXT enforcement.
- Exact original DOCX bytes on fail-closed mismatch.
- Input immutability and pure status-model boundaries.
- Existing import, document reinsert, fidelity and automatic-flow regressions.

## Validation

- Normal full GitHub Actions run #1789: passed during implementation.
- Final clean PR GitHub Actions run #1797: passed on `9f8eddda04b768e994184badbea3aefe39ce74cc`.
- Final metadata-only Actions run: pending before merge.
- Hugging Face sync: pending after merge.
- App verification: required for correct bound key, wrong key, tampered key and legacy compatibility.

## Notes / risks

- The accidental wrong-document/key pairing and accidental mapping-corruption path is technically mitigated but remains open until deployed app verification passes.
- Mapping digest is not malicious-tampering authenticity; signing/HMAC remains deferred until protected key management exists.
- Legacy v1.0 compatibility is intentionally unverified and visibly warned.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Merge after the metadata-only Actions run passes, verify sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.
