# Handover — WP29 Scrub Key secure import/export tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP29 — Scrub Key secure import/export tests`

Status: implemented as helper/test-only branch; pending GitHub Actions validation.

## Summary

WP29 adds focused regression tests for Scrub Key secure import/export expectations from WP25-WP28. The tests exercise the existing pure Scrub Key helpers and do not change Scrub Key schema, export/import behavior, reinsert behavior, UI, encryption, expiry/deletion behavior, dependencies or product placeholder behavior.

The test coverage verifies:

- deterministic Scrub Key JSON export;
- required policy markers such as `privacy_model`, `reversible`, `storage_policy`, `external_ai_policy` and `excluded_rows_policy`;
- valid import/reload result shape and privacy warning;
- malformed JSON handling;
- non-object JSON handling;
- missing required item fields;
- invalid `items` structure;
- wrong privacy/reversible/excluded-row policy markers;
- duplicate placeholder tampering is reported and not reinserted;
- unknown placeholder mismatch is visible and not guessed;
- old timestamps are not expiry-blocked or deleted by helpers;
- helpers do not add hidden recovery, automatic deletion or expiry state;
- import/reinsert helpers do not mutate the supplied Scrub Key;
- reinsert remains local, deterministic, no-AI and no-cloud;
- examples use synthetic values only.

## Files added

- `tests/test_scrub_key_secure_import_export.py`
- `handover/workpackages/20260612_0000_scrub_key_secure_import_export_tests.md`

## Files changed

- None yet in this branch beyond new files.

Intended central documentation updates after/with merge:

- `WORKPACKAGES.md` should mark WP29 as completed helper/tests-only and point the Scrub Key line to `WP28B — Scrub Key warning implementation planning` or `WP29B — Scrub Key import/export edge-case hardening` depending on coordinator sequencing.
- `CHANGELOG.md` should record WP29 status, files added, tests/checks, intentionally not changed, remaining risks and next step.

## Tests/checks

Expected targeted validation:

```text
pytest tests/test_scrub_key_secure_import_export.py
```

Expected related regression validation:

```text
pytest tests -k "scrub_key"
```

ChatGPT web interface validation status:

- Tests were not run locally in ChatGPT web interface.
- No local shell/pytest execution was available through the GitHub connector workflow.
- GitHub Actions on the PR should validate the new test file.

## Validation status

- Required project/control files were read from GitHub `main`.
- WP25-WP28 Scrub Key security/lifecycle/warning/expiry specs were read.
- `SCRUB_KEY_SPEC.md`, `scrub_key.py`, `scrub_key_import.py`, `scrub_key_reinsert.py`, `scrub_key_document_reinsert.py`, `scrub_key_pdf_text_reinsert.py` and relevant existing tests were inspected for context.
- Implementation is tests-only and uses synthetic values.

## GitHub Actions status

- Pending. This branch requires PR/Actions validation.

## Hugging Face sync status

- Not applicable for app behavior. This workpackage adds tests only and does not change UI or runtime behavior.
- Repository sync status should be checked after merge if normal workflow requires it.

## App verification status

- Not applicable. No UI changed.

## Remaining risks

- The new tests validate current helper behavior but do not implement encryption, tamper-proof key containers, automatic deletion, expiry blocking or warning UI.
- Import/export edge cases beyond the current helper surface may still require WP29B.
- Central documentation still needs to record WP29 completion once the PR is merged and tests pass.

## Next recommended step

- `WP28B — Scrub Key warning implementation planning`.
- Alternative if the security-test line should continue first: `WP29B — Scrub Key import/export edge-case hardening`.

## Intentionally not changed

- No encryption implemented.
- No automatic deletion implemented.
- No expiry blocking implemented.
- No new UI warnings implemented.
- No Scrub Key schema migration.
- No import/export behavior change.
- No reinsert behavior change.
- No dependencies changed.
- No secrets or real data added.
- No cloud processing added.
