# Workpackage Claim — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN

Repository: solidprivacy-nl/scrub

Status: completed / ready_for_pr

Start timestamp: 2026-07-04 21:26 Europe/Amsterdam
Completed timestamp: 2026-07-04 21:33 Europe/Amsterdam

## Workpackage title

SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN — Plan removal of duplicate upload/input presentation

## Scope

Planning-only workpackage. Analyze the duplicate input/upload presentation observed after the basic-mode declutter implementation and document a narrow implementation path.

## Files added

- DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN.md
- workpackage_claims/scrub_wp_duplicate_input_surface_simplification_plan.md
- handover/workpackages/20260704_2126_duplicate_input_surface_simplification_plan.md

## Files changed

None.

## Validation

- Required control files read.
- Relevant source/test files inspected.
- Planning-only; no product code or tests changed.
- App verification not applicable.
- GitHub Actions optional for docs-only PR.

## Boundaries

No product implementation files, tests, runtime/startup files, dependencies, export behavior, Scrub Key semantics, reinsert behavior, recognizer logic or document parsing behavior changed.

## Handover

handover/workpackages/20260704_2126_duplicate_input_surface_simplification_plan.md

## Note

Earlier PR #20 was closed as do-not-merge because a connector update to CHANGELOG.md created an unsafe diff. This clean branch intentionally avoids modifying existing files.

## Next recommended step

Start SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS before touching presidio_streamlit.py.
