# Handover — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN

Repository: solidprivacy-nl/scrub  
Status: completed as planning/design-only; ready for PR review

## Summary

Created a concrete UX/product plan for the next premium MVP review-surface simplification line.

The plan responds to coordinator feedback that the current interface still feels too much like a technical form: too many expanders, too many vertical button stacks and too little obvious primary flow.

The proposed target is a calmer primary workflow:

```text
1. Voeg document toe
2. Controleer resultaat
3. Download veilig
```

The plan keeps the side-by-side review as the central surface, keeps the review table as source of truth/fallback, keeps manual missed-value entry available, and moves secondary/debug/audit controls into clearer grouped layers.

## Files added

- `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_plan.md`
- `handover/workpackages/20260623_2320_review_surface_simplification_plan.md`

## Files changed

- None in product code.

## Tests

- No product tests required because this is a planning/design-only package.
- No local tests run.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: not applicable until merge; no app behavior changed.
- App verification: not applicable for this planning-only package.

## Notes / risks

- The next implementation line will likely touch `presidio_streamlit.py` and review flow, so it must be preceded by contract tests.
- Do not implement this plan directly without a dedicated contract-test workpackage.
- Preserve export/download, Scrub Key, reinsert, recognizer, benchmark, Docker/runtime and local packaging semantics.
- The parked DOCX first-page footer preview issue remains out of scope.

## Next recommended step

Start:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS
```

Purpose:

- Add source-level UI contract tests to protect the primary review simplification boundary before implementation.
