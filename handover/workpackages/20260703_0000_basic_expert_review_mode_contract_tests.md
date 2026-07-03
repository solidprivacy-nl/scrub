# Handover — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub  
Status: implemented / PR validation pending

## Summary

Added source-level contract tests for the Basiscontrole / Expertcontrole review-mode direction. These tests protect the planning boundaries before any mode-switch implementation starts.

The tests verify that Basiscontrole is the default lower-cognitive-load MVP path, Expertcontrole remains the full inspection/audit/troubleshooting path, and switching modes must be visibility/grouping-only with no processing, export, Scrub Key, reinsert, recognizer, benchmark or runtime semantic changes.

## Files added

- `tests/test_basic_expert_review_mode_contracts.py`
- `workpackage_claims/scrub_wp_basic_expert_review_mode_contract_tests.md`
- `handover/workpackages/20260703_0000_basic_expert_review_mode_contract_tests.md`

## Files changed

- None.

## Tests / checks

Added source-level contract tests covering:

- plan existence and `Basiscontrole` / `Expertcontrole` naming;
- Basiscontrole default visible flow;
- Expertcontrole full-control scope;
- visibility-only mode-switch boundary;
- Basic secondary grouping structure;
- conditional disclosure requirements;
- safety boundaries;
- implementation sequencing;
- current UI paths required for future mode split;
- no implementation approval before contract tests are merged.

Targeted validation command:

```text
python -m pytest -q tests/test_basic_expert_review_mode_contracts.py
```

No manual full-suite run was performed in this connector session.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: not applicable until merge.
- App verification: not applicable because no UI behavior changed.

## Intentionally not changed

- product code;
- Streamlit UI;
- `presidio_streamlit.py`;
- side-by-side renderer;
- serial review;
- manual mask helper;
- export/download behavior;
- Scrub Key behavior or schema;
- reinsert behavior;
- recognizer or benchmark behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- PR validation still needs to complete.
- Implementation must not start until these contract tests are merged.
- Future implementation must verify that mode switching does not reset session state.

## Next recommended step

Open PR and validate. If green, merge this contract-test package. Then start:

```text
SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION
```
