# Handover — WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN`

Status: completed.

## Summary

Added a planning/design-only interface cleanup plan for collapsing, renaming or moving debug-like review UI elements out of the primary user flow.

The plan is intentionally sharp on the review-loop trap: it does not introduce a new review layer, benchmark gate, export gate, status system or safeguard cycle. It prepares one small next implementation package.

## Files added

- `REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md`
- `workpackage_claims/WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md`
- `handover/workpackages/20260619_0946_review_debug_elements_collapse_plan.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Product-code changes

None.

## Tests

No product tests were required because this was planning-only and changed markdown/governance files only.

`git diff --check` was not executed through the GitHub connector. The changed files are markdown only.

## Validation status

Completed as planning/design-only. The plan reviews current UI labels and locations and narrows the next implementation to a small interface cleanup.

## GitHub Actions status

Pending/unknown after final commit.

## Hugging Face sync status

Pending/unknown after final commit. No app behavior changed.

## App verification status

Not required for this planning-only package because no product UI code changed.

## Remaining risks

- The next implementation must avoid becoming another planning/review loop.
- The next implementation must not hide review table controls, audit details, Scrub Key warnings or export controls.
- Human review remains necessary.

## Next recommended step

```text
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION
```

Do not start automatically without coordinator approval.
