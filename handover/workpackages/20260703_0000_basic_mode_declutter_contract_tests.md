# Handover — SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub  
Status: implemented / PR validation pending

## Summary

Added a contract-tests-only package for the next Basiscontrole declutter implementation. The package defines the expected behavior before product/UI code changes: Basiscontrole must become materially cleaner, Expertcontrole must preserve the full review/audit machinery, and all export, Scrub Key, reinsert, recognizer, benchmark, runtime and dependency semantics must remain unchanged.

## Files added

- `BASIC_MODE_DECLUTTER_CONTRACTS.md`
- `tests/test_basic_mode_declutter_contracts.py`
- `handover/workpackages/20260703_0000_basic_mode_declutter_contract_tests.md`

## Files changed

- `workpackage_claims/scrub_wp_basic_mode_declutter_contract_tests.md`

## Tests / checks

Added source-level contract tests covering:

- contract document existence and next implementation package name;
- Basiscontrole default and `solidprivacy_review_mode` mode-state key;
- target Basiscontrole visible surface;
- requirement that Basiscontrole does not show the full expert expander stack as the primary path;
- Expertcontrole preservation of full controls;
- mode switch must not reset active document/session state;
- future implementation route through `side_by_side_review_state` and `is_expert_review` or equivalent;
- current source paths required for implementation remain present;
- nested expander pattern is not approved;
- semantic boundaries for replacement/export/Scrub Key/reinsert/recognizer/benchmark/runtime behavior;
- live app verification checklist for the later UI implementation;
- contract tests do not import Streamlit or the runtime app.

Targeted validation command:

```text
python -m pytest -q tests/test_basic_mode_declutter_contracts.py
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
- DOCX hygiene panel;
- export/download behavior;
- Scrub Key behavior or schema;
- reinsert behavior;
- recognizer or benchmark behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- PR validation still needs to complete.
- The actual Basiscontrole declutter is not implemented yet.
- Future implementation must verify that mode switching does not reset session state and that Expertcontrole still exposes the full controls.

## Next recommended step

Open PR and validate. If green, merge this contract-test package. Then start:

```text
SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION
```
