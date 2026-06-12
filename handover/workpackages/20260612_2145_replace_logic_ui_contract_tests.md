# Handover — WP_REPLACE_LOGIC_UI_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration`

Status: completed tests/documentation-only.

## Summary

Added UI contract tests for future replacement decision integration. The tests lock the planned Dutch UI action labels, helper review states, helper scopes, affected-count behavior, audit/report-only behavior and safety boundaries from `REPLACE_LOGIC_UI_PLAN.md`.

## Files added

- `tests/test_replace_logic_ui_contract.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_TESTS_replacement_decision_integration.md`
- `handover/workpackages/20260612_2145_replace_logic_ui_contract_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_TESTS_replacement_decision_integration.md`

## Tests

Added:

```text
tests/test_replace_logic_ui_contract.py
```

Expected validation:

```text
pytest tests/test_replace_logic_ui_contract.py
```

No tests were run in the live GitHub checkout because the connector does not provide shell execution.

## Validation

- GitHub Actions: pending / not visible through connector at handover time.
- Hugging Face sync: not applicable for app behavior.
- App verification: not applicable because no UI behavior changed.

## Notes / risks

- No replacement-decision UI implementation exists yet.
- WP42D UI integration was already implemented by another worker and still needs verification.
- No export blocking, Scrub Key mutation, reinsert mutation or click-to-mark implementation was added.

## Next recommended step

- `WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.
- Alternative after verification: `WP43 — Frontend architecture decision`.

## Intentionally not changed

- No Streamlit UI changed.
- No review table behavior changed.
- No export/download behavior changed.
- No Scrub Key behavior changed.
- No reinsert behavior changed.
- No helper runtime behavior changed.
- No dependency changed.
- No cloud processing added.
- No real data added.
