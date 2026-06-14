# Handover — WP_REPLACE_LOGIC_UI_REDESIGN_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — Design a genuinely intuitive replacement review flow`

Status: completed planning/design/documentation-only.

## Summary

Created `REPLACE_LOGIC_UI_REDESIGN_PLAN.md` after verified rollback of the old replacement decision helper panel.

The plan says the old helper panel must not return as the normal user-facing panel. The new direction is task-oriented:

```text
one found item -> context -> suggested replacement -> one simple choice -> optional exact-same scope -> existing table remains fallback
```

Primary choices: `Vervangen`, `Zichtbaar houden`, `Aanpassen`, `Later controleren`.

First-phase scopes: `Alleen deze plek`, `Alle exact dezelfde waarden`.

## Files added

- `REPLACE_LOGIC_UI_REDESIGN_PLAN.md`
- `handover/workpackages/20260614_0230_replace_logic_ui_redesign_plan.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_REDESIGN_PLAN.md`

## Tests/checks run

No shell tests were run. This is planning/design/documentation-only. No product code, UI code, tests or runtime behavior changed.

Dependency checked: `WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY` is completed.

## Validation status

- Redesign plan added.
- Central status updated.
- No app rebuild required.
- No Hugging Face app verification required.

## GitHub Actions status

Unknown. Connector combined-status lookup returned no visible statuses for the latest documentation commit.

## Hugging Face sync status

Unknown / not verified; not required because no UI/runtime behavior changed.

## App verification status

Not applicable.

## Remaining risks

- Replacement UX is redesigned on paper but not yet contract-tested.
- New implementation remains blocked without separate explicit coordinator approval.
- Mutating replacement behavior remains blocked.

## Next recommended step

```text
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```

Later only with separate coordinator approval:

```text
WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION
```
