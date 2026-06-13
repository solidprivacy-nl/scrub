# Handover — WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — Strengthen replacement decision UI contract tests before implementation`

Status: completed tests/documentation-only.

## Summary

Strengthened replacement decision UI contract coverage before any later UI implementation. No UI or product code was changed.

The gap fix strengthened contract language and tests for:

- staged-vs-applied UI state;
- no review table mutation;
- allowed view-only session keys only;
- no Scrub Key writes;
- advisory-only `creates_mapping`, `mapping_candidates` and `export_readiness`;
- no export/download calls;
- no reinsert changes;
- no automatic replacement;
- no fuzzy matching or guessed intent;
- no first mutating `all_normalized` scope without separate explicit coordinator approval;
- existing review table remains source of truth and fallback;
- future UI requires separate explicit coordinator approval.

## Files added

- `handover/workpackages/20260613_1255_replace_logic_ui_contract_gap_fix.md`

## Files changed

- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_contract.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX.md`

## Tests added/updated

- `tests/test_replace_logic_ui_contract.py` strengthened from 6 to 13 tests.

## Tests/checks run

```text
PYTHONPATH=. pytest tests/test_replace_logic_ui_contract.py
```

Result:

```text
13 passed
```

Recommended CI:

```text
pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py
```

## Validation status

- Contract plan strengthened.
- Contract tests strengthened.
- Targeted local pytest passed: `13 passed`.
- No UI/runtime behavior changed.

## GitHub Actions status

Unknown at handover time. `get_commit_combined_status` returned no visible statuses for the latest documentation/test commit checked through the connector.

## Hugging Face sync status

Unknown / not verified. App verification is not required for this package because UI/runtime behavior did not change.

## App verification status

Not applicable.

## Remaining risks

- Future replacement decision UI still needs separate explicit coordinator approval.
- A future mutating UI package needs dedicated implementation tests.

## Next recommended step

Only after separate explicit coordinator approval:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — small staged/read-only companion panel first, unless mutation is separately approved.
```
