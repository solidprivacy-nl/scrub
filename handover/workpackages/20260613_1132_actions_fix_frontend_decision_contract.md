# Handover — WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — Restore WP43/WP42D documentation contract phrase for regression tests`

Status: completed after Actions/sync verification; app verification not applicable.

## Summary

Coordinator/user screenshots showed repeated GitHub Actions failures in:

```text
tests/test_frontend_architecture_decision.py::test_wp43_does_not_close_wp42d_verification_or_change_ui
```

The failing assertion expected the historical WP43 contract phrase:

```text
wp43 does not validate or close wp42d
wp42d remains pending
```

The later rollback/closeout wording in `FRONTEND_ARCHITECTURE_DECISION.md` had removed that exact phrase. The repair restores it under a `Historical WP43 contract` subsection while preserving the later rollback/parked status as a later explicit decision.

Coordinator/user later provided green evidence for commit `a8182cd`:

```text
Tests #691 — green
Sync to Hugging Face Space #703 — green
```

## Files added

- `workpackage_claims/WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT.md`
- `handover/workpackages/20260613_1132_actions_fix_frontend_decision_contract.md`

## Files changed

- `FRONTEND_ARCHITECTURE_DECISION.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT.md`

## Tests added/updated

No tests were changed.

This package repairs the documentation text to satisfy the existing regression contract in `tests/test_frontend_architecture_decision.py`.

## Tests/checks run

Static verification against repository content:

- `FRONTEND_ARCHITECTURE_DECISION.md` now contains `WP43 does not validate or close WP42D.`
- `FRONTEND_ARCHITECTURE_DECISION.md` now contains `WP42D remains pending until its own Actions/Hugging Face/app evidence or a later explicit rollback/closeout decision.`

Coordinator/user CI evidence:

```text
Tests #691 — green for commit a8182cd
Sync to Hugging Face Space #703 — green for commit a8182cd
```

## Validation status

- Static content repair completed.
- GitHub Actions verified green by coordinator/user evidence.
- Hugging Face sync verified green by coordinator/user evidence.

## GitHub Actions status

Green for commit `a8182cd` based on coordinator/user evidence: `Tests #691`.

## Hugging Face sync status

Green for commit `a8182cd` based on coordinator/user evidence: `Sync to Hugging Face Space #703`.

## App verification status

Not applicable. No Streamlit UI behavior changed.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No product code changes.
- No helper logic changes.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

## Commit evidence

- Claim created: `48ecd0fdd1c86cb8459287a2ac224e45ff6d2c28`
- Contract phrase restored: `359af141080ba225b88e2e69e8b78fedf87d5c0c`
- Workpackages updated: `b6926226112c8b6951af092b602ea3fe9743b5d5`
- Changelog updated: `4c18f3ad9488e1ba4de2f8180eed2c401cb1ce95`
- Claim close before verification evidence: `a8182cd146deb9bb3200b333187c5a3b2cdec7d7`

## Remaining risks

- This repair preserves the test contract rather than changing test semantics.
- Next UI work still requires explicit coordinator approval.

## Next recommended step

Resume the planned sequence only after coordinator approval:

```text
WP_SERIAL_REVIEW_UI — non-destructive serial review panel in Streamlit.
```
