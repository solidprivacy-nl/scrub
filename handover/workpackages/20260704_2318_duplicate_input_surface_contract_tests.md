# Handover — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — Lock single input-surface contract before implementation

## Status

Completed; PR validation pending.

## Files added

- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_contract_tests.md`
- `handover/workpackages/20260704_2318_duplicate_input_surface_contract_tests.md`

## Files changed

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_contract_tests.md`

## Tests/checks

Intended validation commands:

```bash
python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py
```

```bash
python -m pytest -q \
  tests/test_duplicate_input_surface_simplification_contracts.py \
  tests/test_execution_interface_simplification_ui.py \
  tests/test_basic_mode_declutter_implementation.py \
  tests/test_review_surface_simplification_implementation.py \
  tests/test_export_download_ux_contracts.py \
  tests/test_export_download_ux_implementation.py
```

```bash
git diff --check
git status --short
```

Connector/local limitation: the execution sandbox could not clone GitHub (`Could not resolve host: github.com`), so local pytest execution in this chat environment was not possible. Validation is expected through PR/GitHub Actions.

## Validation status

Source-level contract tests were added. No product implementation files were changed.

The contract tests assert:

- the duplicate-input simplification plan exists and locks the target flow;
- direct app source has one `1. Voeg document of tekst toe` heading;
- step order remains `1 -> 2 -> 3`;
- TXT/DOCX/PDF upload support remains present;
- synthetic Dutch legal example support remains present;
- pasted/extracted text area remains present;
- existing input precedence markers remain present;
- review/export/Scrub Key/audit/DOCX hygiene surfaces remain present;
- no duplicate-input startup/runtime mutation is introduced;
- prohibited scope expansion markers are absent from the direct runtime surface;
- the new tests do not import Streamlit or `presidio_streamlit`.

## GitHub Actions status

Pending after PR creation.

## Hugging Face sync status

Not applicable until merge. No UI or product behavior changed in this contract-test-only package.

## App verification status

Not applicable. This package changed tests/docs only and did not change UI behavior.

## Remaining risks

- Local pytest could not be executed in the chat sandbox because GitHub cloning failed due DNS/network restrictions.
- PR validation must confirm the new contract tests pass with the full repository context.
- The duplicate visible input surface may still be caused by stale/runtime-mutated Space state; the implementation package must verify the live app after merge/sync.

## Next recommended step

Review PR validation. If green, merge this contract-test package and start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow package.
