# Handover — WP29 Scrub Key secure import/export edge-case hardening

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP29 — Scrub Key secure import/export tests`

Status: completed as helper/tests-only edge-case hardening on top of the already-merged WP29 test package.

## Summary

Remote `main` already contained a completed WP29 closeout for Scrub Key secure import/export tests. This run therefore added additional WP29B-style edge-case hardening while preserving the original WP29 scope and safety boundaries.

The only helper behavior changed is conservative validation: unsupported Scrub Key `schema_version` values are now reported as validation issues instead of being accepted as long as the field is non-empty.

No encryption, automatic deletion, expiry enforcement, Scrub Key schema migration, Streamlit UI change, import/export semantic change, reinsert semantic change, dependency change, real data or cloud processing was added.

## Files added

- `handover/workpackages/20260612_1330_scrub_key_secure_import_export_edge_case_hardening.md`

## Files changed

- `scrub_key.py`
- `tests/test_scrub_key_secure_import_export.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

- `python -m py_compile scrub_key.py scrub_key_import.py scrub_key_reinsert.py tests/test_scrub_key_secure_import_export.py` — passed in the ChatGPT execution sandbox against the authored helper/test draft. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_scrub_key_secure_import_export.py` — passed in the ChatGPT execution sandbox against the authored WP29 edge-case test draft; 10 passed. The sandbox emitted the same unrelated spreadsheet runtime warmup warning, but pytest returned success.
- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Related commands `pytest tests/test_scrub_key.py`, `pytest tests/test_scrub_key_import.py` and `pytest tests/test_scrub_key_reinsert.py` were requested by the workpackage as relevant if executable, but were not run in a live GitHub checkout through the connector.

## Validation status

- Existing WP29 remote closeout already recorded PR #2 merged and GitHub Actions green for the original WP29 tests.
- This run expands the existing secure import/export test file with edge-case coverage for missing schema marker, unsupported schema version, empty/no-usable mappings, tampered item count, unknown placeholder and not-found placeholder audit behavior, validation error non-leakage and valid synthetic roundtrip.
- `validate_scrub_key` now rejects unsupported schema versions while preserving the existing schema value `1.0`.
- Invalid keys still fail closed: import returns no mapping rows and reinsert leaves text unchanged.
- Validation/audit errors avoid exposing original sensitive values.
- Duplicate placeholders remain excluded from reinsert.
- Old timestamps remain guidance-only and are not expiry-blocked or deleted.
- Helpers still report local-only/no-AI/no-cloud behavior for deterministic reinsert.
- No UI behavior changed.

## GitHub Actions status

To be checked after final handover commit.

## Hugging Face sync status

To be checked after final handover commit. No app behavior changed.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- No encryption/protected Scrub Key container is implemented.
- No automatic deletion or expiry enforcement is implemented.
- No document/key fingerprint or wrong-document mismatch detection is implemented.
- No warning/acknowledgement UI implementation is added yet.
- The exact final updated GitHub checkout still needs normal GitHub Actions validation.

## Next recommended step

- `WP28B — Scrub Key warning implementation planning`.
