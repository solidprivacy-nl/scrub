# Handover — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub  
Status: implemented / targeted pytest pending

## Summary

Added review-surface simplification contract documentation and source-level contract tests. This protects the calmer three-step MVP direction before any implementation touches `presidio_streamlit.py` or the review flow.

The package is based on `scrub-review-surface-simplification-plan` because `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` is not present on `main` yet. This avoids inventing a plan from memory and keeps the contract tests aligned with open planning PR #9.

## Files added

- `REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md`
- `tests/test_review_surface_simplification_contracts.py`
- `workpackage_claims/scrub_wp_review_surface_simplification_contract_tests.md`
- `handover/workpackages/20260702_0000_review_surface_simplification_contract_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_contract_tests.md`

`CHANGELOG.md` update was attempted but blocked by the connector safety layer during full-file replacement. It remains a documentation-sync item for the next branch/PR update.

## Contract coverage

The contract and tests cover:

- three-step target: `Voeg document toe`, `Controleer resultaat`, `Download veilig`;
- review table remains source of truth and fallback;
- side-by-side review remains primary/central review surface;
- manual missed-value entry remains available;
- export/download semantics must not change;
- download filenames and MIME types must not change;
- Scrub Key JSON semantics must not change;
- audit downloads and technical details remain available;
- Scrub Key remains separated and warning-protected;
- no cloud, AI, OCR, restored-PDF or PDF-to-DOCX behavior;
- old replacement decision helper panel must not return as normal user-facing UI;
- future implementation requires a separate workpackage.

## Tests / checks

- Targeted pytest command required: `python -m pytest -q tests/test_review_surface_simplification_contracts.py`.
- Targeted pytest was not run in this connector session because the GitHub connector can edit repository files but cannot execute repository tests.
- Full suite was not run.
- GitHub Actions were not manually triggered to preserve credits.

## Validation

- GitHub Actions: not manually triggered / not required at this stage to preserve credits.
- Hugging Face sync: not triggered because this branch was not merged to `main`.
- App verification: not applicable because no UI behavior changed.
- Targeted pytest: pending.

## Intentionally not changed

- product code;
- Streamlit UI;
- `presidio_streamlit.py`;
- `side_by_side_review_panel_ui.py`;
- `serial_review_panel_ui.py`;
- `manual_mask_entry.py`;
- export/download behavior;
- Scrub Key behavior or schema;
- reinsert behavior;
- recognizer or benchmark behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` remains on open planning PR #9 / branch `scrub-review-surface-simplification-plan`, not on `main`.
- Targeted pytest still needs to run in an execution environment.
- `CHANGELOG.md` still needs a small documentation-sync update because the connector blocked the full-file replacement.

## Next recommended step

Run the targeted contract test in an execution environment:

```text
python -m pytest -q tests/test_review_surface_simplification_contracts.py
```

After targeted validation passes, proceed only with explicit coordinator approval to:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION
```
