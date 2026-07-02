# Workpackage Claim — SCRUB-WP_ACTIONS_BUDGET_VALIDATION_POLICY

Repository: solidprivacy-nl/scrub

Status: completed

Start timestamp: 2026-07-02 00:00 UTC
Completion timestamp: 2026-07-02 00:00 UTC

## Workpackage title

SCRUB-WP_ACTIONS_BUDGET_VALIDATION_POLICY — Budget-aware validation and GitHub Actions usage policy

## Scope

Governance/documentation only. Record budget-aware validation policy for future workpackages.

## Files changed

- AGENTS.md
- PROJECT_PROMPT.md
- WORKPACKAGES.md
- STATUS_MONITORING_RUNBOOK.md
- CHANGELOG.md
- workpackage_claims/scrub_wp_actions_budget_validation_policy.md

## Files added

- handover/workpackages/20260702_0000_actions_budget_validation_policy.md

## Validation policy recorded

Use budget-aware validation. Do not trigger GitHub Actions manually for documentation-only packages. Use static inspection and targeted checks before CI. Use one deliberate CI run for product behavior changes when ready for merge/release. The coordinator is not expected to run local tests, Codespaces or Codex validation.

## Validation performed

- Repository/content review of changed governance files.
- Confirmed no product code, UI, export, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency files were intentionally changed.
- No full test suite was run because this is documentation/governance-only.
- GitHub Actions were not manually triggered to preserve credits.
- Hugging Face sync was not triggered because the work stayed off `main`.

## Handover path

handover/workpackages/20260702_0000_actions_budget_validation_policy.md

## Next recommended step

Use this policy in future workpackage instructions. Merge only when ready; do not open PR solely to consume CI for this docs-only policy.
