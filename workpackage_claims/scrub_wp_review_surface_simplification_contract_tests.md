# Workpackage Claim — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-02 00:00 UTC

## Workpackage title

SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — Contract tests for review surface simplification

## Scope

Contract tests only. No product code, Streamlit UI, export/download, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency changes.

## Base branch decision

`REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` is not present on `main`. The plan exists on open planning PR #9 / branch `scrub-review-surface-simplification-plan`, so this package is based on that planning branch to avoid inventing a plan from memory.

## Allowed files

- REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md
- tests/test_review_surface_simplification_contracts.py
- WORKPACKAGES.md
- CHANGELOG.md
- workpackage_claims/scrub_wp_review_surface_simplification_contract_tests.md
- handover/workpackages/YYYYMMDD_HHMM_review_surface_simplification_contract_tests.md

Optional only if directly needed:

- RELEASE_NOTES.md

## Validation policy

Use budget-aware validation. Do not trigger GitHub Actions manually. Do not run full suite by default. Required targeted check is `python -m pytest -q tests/test_review_surface_simplification_contracts.py` if an execution environment is available.
