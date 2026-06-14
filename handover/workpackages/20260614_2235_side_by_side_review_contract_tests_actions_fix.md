# Handover — WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — Repair side-by-side review contract wording failure`

Status: completed documentation-only Actions repair.

## Summary

Repaired the narrow contract wording failure in `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`.

The failing test expected exact contract phrases in the highlight/safety section. Added a compact English contract/safety note while preserving the Dutch user-facing copy and without changing the UX direction.

Added exact phrases:

```text
only visual aid
must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior
```

## Files added

- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX.md`
- `handover/workpackages/20260614_2235_side_by_side_review_contract_tests_actions_fix.md`

## Files changed

- `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX.md`

`RISK_REGISTER.md` was read. It was not changed because this was a narrow wording-only repair and did not alter risk status or mitigation strategy.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
pytest tests/test_side_by_side_review_contract.py
pytest tests/test_side_by_side_review_contract.py tests/test_replace_logic_ui_redesign_plan.py
```

Repository source verification performed:

- `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md` now contains the exact phrases expected by the test.
- `tests/test_side_by_side_review_contract.py` was read and the failure scope was confirmed as text-only.

## Validation status

Implemented as documentation-only repair. Awaiting GitHub Actions confirmation.

## GitHub Actions status

Unknown at handover time. This package was created specifically to repair a failing Actions contract test. Verify Actions on the final commit before starting the next helper package.

## Hugging Face sync status

Not required for this package because no UI/runtime behavior changed.

## App verification status

Not applicable.

## Remaining risks

- Future side-by-side implementation remains blocked until green contract tests and separate coordinator approval.
- Synchronized scrolling remains a separate risk and requires separate planning/testing.
- Custom HTML/component rendering remains blocked until separately approved.

## Next recommended step

After green Actions:

```text
WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER
```

Do not start without separate coordinator approval:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION
synchronized scroll implementation
custom HTML/component rendering
replacement UI implementation
click-to-mark
advanced editor
full-document marking
```
