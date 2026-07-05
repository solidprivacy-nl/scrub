# Handover — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS — Lock Review/Export safety controls before UI simplification

## Status

Completed / PR validation pending.

## Files added

- `tests/test_review_export_vertical_density_contracts.py`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_contract_tests.md`
- `handover/workpackages/20260705_1214_review_export_vertical_density_contract_tests.md`

## Files changed

- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_contract_tests.md`

Note: `CHANGELOG.md` and `WORKPACKAGES.md` still need concise updates from Codespaces or a local clone. Previous connector attempts to update those large whole-file documents were blocked, and this package kept the code/test scope minimal rather than risking unsafe documentation overwrites.

## Tests

Source-level tests added:

- `tests/test_review_export_vertical_density_contracts.py`

Expected local commands:

```bash
python -m pytest -q tests/test_review_export_vertical_density_contracts.py
python -m pytest -q \
  tests/test_review_export_vertical_density_contracts.py \
  tests/test_export_download_ux_implementation.py \
  tests/test_review_surface_simplification_implementation.py \
  tests/test_duplicate_input_surface_simplification_contracts.py
git diff --check
git status --short
```

## Validation status

PR validation pending.

The new tests are source-level only and do not import Streamlit or `presidio_streamlit`.

## GitHub Actions status

Pending after PR.

## Hugging Face sync status

Not applicable until merge. No app behavior changes in this contract-test-only package.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- `CHANGELOG.md` and `WORKPACKAGES.md` need a concise follow-up update because connector-safe whole-file updates were not available.
- The next implementation package will touch Review/Export UI density and must remain narrow.
- The implementation must preserve side-by-side review, manual missed-value entry, replacement table, Scrub Key warning/separation, audit files and DOCX hygiene audit.

## Next recommended step

Run PR validation. If green, merge and start `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` as the material UI simplification package.
