# Handover — WP_CONTEXT_CARD_UI_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_CONTEXT_CARD_UI_CONTRACT_TESTS — Harden context-card UI plan labels, fields and boundaries`

Status: completed planning/tests-only; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Hardened the contract-test layer around `CONTEXT_CARD_UI_PLAN.md` without implementing UI.

The existing plan and test already covered the core context-card plan. This package added only missing/stronger coverage:

- explicit `build_context_card` and `build_context_cards` checks;
- full boundary-list contract check;
- exact `existing review table remains authoritative control/fallback` contract wording;
- stronger review-table control/fallback assertions;
- explicit display-only / no-write / no same-value mutation assertions;
- preservation of the serial-review relationship through `serial_review.py` and `current_item`.

## Files added

- `workpackage_claims/WP_CONTEXT_CARD_UI_CONTRACT_TESTS.md`
- `handover/workpackages/20260613_1205_context_card_ui_contract_tests.md`

## Files changed

- `CONTEXT_CARD_UI_PLAN.md`
- `tests/test_context_card_ui_plan.py`
- `WORKPACKAGES.md`
- `workpackage_claims/WP_CONTEXT_CARD_UI_CONTRACT_TESTS.md`

## Tests added/updated

Updated `tests/test_context_card_ui_plan.py`.

Added/strengthened coverage for:

- `context_cards.py`;
- `build_context_card`;
- `build_context_cards`;
- `prefix_text`;
- `match_text`;
- `suffix_text`;
- `entity_type`;
- `review_state`;
- `replacement_preview`;
- `source`;
- `risk_flags`;
- `offset_valid`;
- `validation_errors`;
- `report-only`;
- `non-authoritative`;
- `table-first baseline`;
- `existing review table remains authoritative control/fallback`;
- `no startup source mutation`;
- `no full-document marking`;
- `no click-to-mark`;
- `no advanced editor`;
- `no inline editing`;
- `no Word/PDF layout rendering`;
- `no export blocking`;
- `no Scrub Key mutation`;
- `no reinsert behavior change`;
- `no review table mutation`;
- `synthetic-only`;
- `current_item` from `serial_review.py` may select a context card;
- next/previous review stays helper-driven;
- context card mutates nothing;
- review table remains source of truth;
- context-card display data does not write decisions, mappings, Scrub Key data, export eligibility or reinsert state.

## Tests/checks run

The exact GitHub checkout could not be executed through the GitHub connector because it does not provide a checked-out repo shell/runtime.

I therefore ran the targeted test in an isolated local reconstruction of the updated plan and test file:

```text
pytest -q tests/test_context_card_ui_plan.py
```

Result:

```text
8 passed
```

Expected checks in a normal repository checkout:

```text
pytest tests/test_context_card_ui_plan.py
pytest tests/test_context_card_ui_plan.py tests/test_context_cards.py
```

## Validation status

- Plan/test contract was statically reviewed.
- Targeted reconstructed pytest passed: `8 passed`.
- `WORKPACKAGES.md` was re-fetched with the current SHA and updated successfully.
- `CHANGELOG.md` was re-fetched in ranges before central update consideration. To avoid unsafe manual reconstruction of a long concurrently updated file, it was not overwritten in this package.

Desired changelog entry:

```text
WP_CONTEXT_CARD_UI_CONTRACT_TESTS — completed planning/tests-only. Hardened tests/test_context_card_ui_plan.py and added exact contract wording to CONTEXT_CARD_UI_PLAN.md for builder functions, required fields, full safety boundaries, review-table authoritative control/fallback, serial_review.py current_item relationship, helper-driven next/previous review and display-only/no-mutation context-card behavior. No Streamlit UI, no presidio_streamlit.py, no fix_streamlit_nested_expanders.py, no startup source mutation, no export/Scrub Key/reinsert/dependency/cloud changes and no real data.
```

## GitHub Actions status

Unknown at handover time. A new run is expected after the final commits.

## Hugging Face sync status

Unknown at handover time. This package does not change app runtime/UI/dependencies, but sync status should still be checked if the workflow runs.

## App verification status

Not applicable. No Streamlit UI behavior changed.

## Intentionally not changed

- No Streamlit UI.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No startup source mutation.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No review table mutation.
- No export/download changes.
- No Scrub Key changes.
- No reinsert changes.
- No dependency changes.
- No cloud processing.
- No real data.

## Commit evidence

- Claim created: `8254decaae1710fb2dda1110c83e305d5a359ec6`
- Plan contract wording added: `77aa1ad3d4481af8760ddaa8acc223b39aa11528`
- Contract tests hardened: `3ee20974806d503beedee1b9a9603b2d303a0d7f`
- Workpackages updated: `ae3a4898d9b548ebc6de401e3be3afc174f38a4a`

## Remaining risks

- GitHub Actions and Hugging Face sync still need verification for the final commits.
- Full repository tests were not run from an exact checkout through this interface.
- `CHANGELOG.md` still needs a safe centralized update if a worker with full checkout/merge tools can patch it without reconstructing the whole file manually.
- This package is not a UI implementation; the context card is still not visible in the app.

## Next recommended step

```text
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — pure helper combining serial queue + context-card data before any UI.
```

Do not start Streamlit UI implementation without explicit coordinator approval.
