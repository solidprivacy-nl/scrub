# Handover — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_PLAN

Repository: solidprivacy-nl/scrub  
Status: completed planning/design-only / PR validation pending

## Summary

Defined the Basiscontrole / Expertcontrole review-mode direction. The plan sets Basiscontrole as the default lower-cognitive-load MVP path and Expertcontrole as the full inspection, tuning, audit and troubleshooting path. It explicitly states that mode switching is visibility/grouping only and must not change recognizer behavior, replacement logic, export output, Scrub Key JSON, reinsert behavior or audit generation.

## Files added

- `BASIC_EXPERT_REVIEW_MODE_PLAN.md`
- `handover/workpackages/20260703_0000_basic_expert_review_mode_plan.md`

## Files changed

- `DECISION_LOG.md`
- `workpackage_claims/scrub_wp_basic_expert_review_mode_plan.md`

## Tests / checks

- Manual review of `BASIC_EXPERT_REVIEW_MODE_PLAN.md` against the workpackage instructions.
- Verified by file scope that no product code or UI implementation files were intentionally changed.
- No product tests were run because this is planning/design-only.
- No full-suite run was performed.
- No GitHub Actions run was manually triggered.

## Validation

- GitHub Actions: pending after PR if repository automation runs.
- Hugging Face sync: not applicable until merge.
- App verification: not applicable because no UI behavior changed.

## Documentation sync note

Updates to `CHANGELOG.md` and `WORKPACKAGES.md` were attempted but blocked by the connector safety layer during full-file replacement. The workpackage status and next step are recorded in this handover and in the claim file. A later small documentation-sync package can update those central files if desired.

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

- Contract tests are still needed before any implementation starts.
- The central `WORKPACKAGES.md` and `CHANGELOG.md` files still need a small sync update if the coordinator wants them updated on `main` before the next package.
- Implementation must avoid changing semantics or resetting session state when the future mode switch is added.

## Next recommended step

Start:

```text
SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS
```

Do not implement the mode switch until contract tests are merged.
