# Workpackage Claim — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS — Contract tests for Basiscontrole / Expertcontrole review modes

## Scope

Contract tests only. Protect the Basiscontrole / Expertcontrole plan before any mode-switch implementation starts. No product code, Streamlit UI, export/download, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency changes.

## Allowed files

- tests/test_basic_expert_review_mode_contracts.py
- workpackage_claims/scrub_wp_basic_expert_review_mode_contract_tests.md
- handover/workpackages/YYYYMMDD_HHMM_basic_expert_review_mode_contract_tests.md
- CHANGELOG.md / WORKPACKAGES.md if connector permits safe documentation sync

## Validation policy

Source-level contract tests. GitHub Actions/PR validation are appropriate because this package adds tests. No app verification is required because no UI behavior changes.
