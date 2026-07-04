# Workpackage Claim — SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS — Contract tests for materially cleaner Basiscontrole

## Scope

Contract tests only. Protect the intended Basiscontrole declutter implementation before product/UI code changes. No product code, Streamlit UI, export/download, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency changes.

## Allowed files

- tests/test_basic_mode_declutter_contracts.py
- workpackage_claims/scrub_wp_basic_mode_declutter_contract_tests.md
- handover/workpackages/YYYYMMDD_HHMM_basic_mode_declutter_contract_tests.md
- CHANGELOG.md / WORKPACKAGES.md if connector permits safe documentation sync

## Validation policy

Source-level contract tests. GitHub Actions/PR validation are appropriate because this package adds tests. No Hugging Face app verification is required because no UI behavior changes.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.
