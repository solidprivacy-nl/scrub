# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS`

Status: completed tests/documentation-only; awaiting GitHub Actions and Hugging Face sync verification.

## Summary

Added documentation and contract tests for the future UX where `Controleer gevonden gegevens` may become a collapsible section without losing the review table's authority.

The contract preserves the review table as:

```text
source of truth
fallback
de plek waar include/remember/find/replace_with wordt gecontroleerd
```

No production UI was implemented.

## Files added

- `REVIEW_TABLE_COLLAPSIBLE_CONTRACT.md`
- `tests/test_review_table_collapsible_contract.py`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260615_0230_review_table_collapsible_contract_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`

## Tests added/updated

Added:

```text
tests/test_review_table_collapsible_contract.py
```

Covered:

- desired heading contains `Controleer gevonden gegevens`;
- desired heading supports item-count copy, e.g. `Controleer gevonden gegevens — {item_count} items`;
- review table remains source of truth and fallback;
- `replacement_editor` remains the Streamlit data-editor key;
- `include`, `remember`, `find`, `replace_with` remain available;
- current app still contains `De vervangtabel blijft leidend`;
- current app still renders `st.data_editor` for the review table;
- export/download labels remain present;
- contract forbids export/download behavior changes;
- contract forbids export blocking;
- contract forbids Scrub Key writes/schema changes;
- contract forbids reinsert behavior changes;
- contract forbids replacement behavior changes;
- contract forbids click-to-mark, advanced editor and full-document marking;
- future implementation gate is `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION`;
- no real-data fixture is introduced.

## Tests/checks run

No shell/pytest execution was available through the GitHub connector.

Expected targeted check:

```text
pytest tests/test_review_table_collapsible_contract.py
```

Expected full check:

```text
python -m pytest -q tests
```

## Validation status

- Contract document added.
- Contract tests added.
- No production UI implementation was added.
- `presidio_streamlit.py` was not changed.
- Export/download behavior was not changed.
- Scrub Key behavior was not changed.
- Reinsert behavior was not changed.
- Replacement behavior was not changed.
- No dependency/cloud/real-data change.

## GitHub Actions status

Unknown at handover time. A new workflow run is expected after the commits.

## Hugging Face sync status

Unknown at handover time. This package does not change app/runtime behavior, but sync may still run for documentation/test commits.

## App verification status

Not applicable. No Streamlit UI/runtime behavior changed.

## Remaining risks

- The review table is not collapsible yet; this package only locks the contract.
- A later implementation will edit the review-flow area in `presidio_streamlit.py` and must not run in parallel with other `presidio_streamlit.py` review-flow changes.
- Actions/HF verification is still required for this package.

## Next recommended step

Verify:

```text
Tests — green
Sync to Hugging Face Space — green
```

Only after green tests may a separate implementation package start:

```text
WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION
```

That package must not run in parallel with other `presidio_streamlit.py` review-flow work.
