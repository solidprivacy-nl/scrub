# Workpackage Claim — SCRUB-WP_ACTIONS_BUDGET_VALIDATION_POLICY

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-02 00:00 UTC

## Workpackage title

SCRUB-WP_ACTIONS_BUDGET_VALIDATION_POLICY — Budget-aware validation and GitHub Actions usage policy

## Scope

Governance/documentation only. Record budget-aware validation policy for future workpackages.

## Allowed files

- AGENTS.md
- PROJECT_PROMPT.md
- WORKPACKAGES.md
- STATUS_MONITORING_RUNBOOK.md
- CHANGELOG.md
- workpackage_claims/scrub_wp_actions_budget_validation_policy.md
- handover/workpackages/YYYYMMDD_HHMM_actions_budget_validation_policy.md

Optional only if needed:

- DECISION_LOG.md

## Validation policy

Use budget-aware validation. Do not trigger GitHub Actions manually for this documentation-only package. Required checks are repository/content review, confirmation that no product code/UI/export/Scrub Key/reinsert/recognizer/runtime files changed, and documentation consistency review.

## Notes

The coordinator does not run local tests, Codespaces or Codex validation as a fallback. GitHub Actions should be deliberate validation, not a debugging loop.
