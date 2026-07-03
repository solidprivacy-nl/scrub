# Workpackage Claim — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Repository: solidprivacy-nl/scrub

Status: implemented planning/contract-tests-only / PR validation pending

Start timestamp: 2026-07-03 00:00 UTC
Update timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH — Make secondary review controls calmer

## Scope

Planning and contract tests for a small UI polish package. The goal is to group secondary controls more calmly while preserving side-by-side review, manual missed-value entry, replacement table, step-by-step review, Scrub Key, export/download, audit and DOCX hygiene controls.

## Files added

- SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md
- tests/test_secondary_control_grouping_polish_contracts.py
- handover/workpackages/20260703_0000_secondary_control_grouping_polish.md

## Files changed

- CHANGELOG.md
- workpackage_claims/scrub_wp_secondary_control_grouping_polish.md

## Validation policy

This package is planning/contract-tests-only. GitHub Actions are appropriate for PR validation because it adds tests. App verification is not applicable because no UI behavior changed in this package. The later implementation package will require Actions, Hugging Face sync and live app verification.

## Boundaries

No product code or Streamlit UI changed in this package. No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.

## Handover path

handover/workpackages/20260703_0000_secondary_control_grouping_polish.md

## Next recommended step

Open PR, validate tests, merge if green. Then start `SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION` for the actual narrow UI implementation.
