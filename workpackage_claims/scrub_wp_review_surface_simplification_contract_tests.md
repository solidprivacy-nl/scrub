# Workpackage Claim — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Status: implemented / targeted pytest pending

Start timestamp: 2026-07-02 00:00 UTC
Update timestamp: 2026-07-02 00:00 UTC

## Workpackage title

SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — Contract tests for review surface simplification

## Scope

Contract tests only. No product code, Streamlit UI, export/download, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency changes.

## Base branch decision

`REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` is not present on `main`. The plan exists on open planning PR #9 / branch `scrub-review-surface-simplification-plan`, so this package is based on that planning branch to avoid inventing a plan from memory.

## Files added

- REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md
- tests/test_review_surface_simplification_contracts.py
- handover/workpackages/20260702_0000_review_surface_simplification_contract_tests.md

## Files changed

- WORKPACKAGES.md
- workpackage_claims/scrub_wp_review_surface_simplification_contract_tests.md

`CHANGELOG.md` update was attempted but blocked by the connector safety layer during full-file replacement. It is recorded as a remaining documentation sync item.

## Validation policy

Use budget-aware validation. Do not trigger GitHub Actions manually. Do not run full suite by default. Required targeted check is `python -m pytest -q tests/test_review_surface_simplification_contracts.py` when an execution environment is available.

## Validation status

- GitHub Actions: not manually triggered to preserve credits.
- Hugging Face sync: not triggered because this branch is not merged to `main`.
- App verification: not applicable because no UI behavior changed.
- Targeted pytest: pending; connector session cannot execute repository tests.

## Handover path

handover/workpackages/20260702_0000_review_surface_simplification_contract_tests.md

## Next recommended step

Run targeted validation in an execution environment. After it passes, proceed only with explicit coordinator approval to `SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION`.
