# Handover — SCRUB-WP_ACTIONS_BUDGET_VALIDATION_POLICY

Repository: solidprivacy-nl/scrub  
Status: completed governance/docs-only

## Summary

Recorded budget-aware validation as the default governance rule for future SolidPrivacy Scrub workpackages. The update makes clear that GitHub Actions should be deliberate validation, not the first debugging loop, and that the coordinator is not expected to run local tests, Codespaces or Codex validation as a fallback.

The package was performed on branch `scrub-wp-actions-budget-validation-policy-clean` rather than directly on `main` to avoid triggering the `push: main` test and Hugging Face sync workflows unnecessarily.

## Files added

- `handover/workpackages/20260702_0000_actions_budget_validation_policy.md`

## Files changed

- `AGENTS.md`
- `PROJECT_PROMPT.md`
- `WORKPACKAGES.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_actions_budget_validation_policy.md`

## Tests / checks

- No pytest run: not required for documentation/governance-only work.
- No full-suite run: intentionally not run to preserve credits.
- Repository/content review performed for changed governance files.
- Scope review performed: no product code, Streamlit UI, export/download behavior, Scrub Key behavior, reinsert behavior, recognizer logic, benchmark logic, runtime/startup behavior or dependency files were intentionally changed.

## Validation

- GitHub Actions: not required / not manually triggered to preserve credits.
- Hugging Face sync: not applicable / not triggered because there was no push to `main`.
- App verification: not applicable because no app behavior changed.

## Notes / risks

- This package changes governance documentation only; it does not weaken testing expectations for sensitive product behavior changes.
- Future UI/export/reinsert/Scrub Key/runtime/recognizer/document-processing changes should still use targeted checks first and one deliberate CI validation when ready for merge/release.
- A first abandoned branch named `scrub-wp-actions-budget-validation-policy` was created during execution and should not be used for PR/merge. The clean branch for this package is `scrub-wp-actions-budget-validation-policy-clean`.

## Next recommended step

Use budget-aware validation wording in all future workpackage instructions. Do not open a PR solely to consume CI for this docs-only policy; merge or PR only when the coordinator wants the governance change incorporated into `main`.
