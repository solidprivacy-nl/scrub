# Handover — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN — Plan removal of duplicate upload/input presentation

## Status

Completed as planning-only; ready for PR validation.

## Files added

- `DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN.md`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_plan.md`
- `handover/workpackages/20260704_2126_duplicate_input_surface_simplification_plan.md`

## Files changed

None.

Central documentation note: `CHANGELOG.md` / `WORKPACKAGES.md` updates were not included in this clean PR because an earlier connector attempt on PR #20 created an unsafe changelog diff. PR #20 was closed as do-not-merge. The clean PR intentionally contains only new planning/claim/handover files.

## Tests/checks

- Planning-only package.
- No product code changed.
- No tests changed.
- GitHub Actions optional because this is documentation-only.

## Validation status

Plan created after reading the required control files and inspecting the input/review/export source and related source-level tests.

## GitHub Actions status

Pending PR. Optional for documentation-only, but PR validation can run normally.

## Hugging Face sync status

Not applicable; no product code or UI behavior changed.

## App verification status

Not applicable; no app behavior changed.

## Summary

The plan documents the observed duplicate `1. Voeg document of tekst toe` input surface from live screenshots. Current direct `presidio_streamlit.py` source has one main static input heading and one input path, so the next test/implementation line must confirm whether the duplicate comes from stale runtime/source mutation, Streamlit state, or a remaining visible fallback surface before touching product code.

The plan recommends the least risky implementation direction: one unified input section with upload, synthetic example selector and paste/edit text area under a single top-level heading. It rejects tabs/radio for the next step unless later evidence shows they are needed.

## Remaining risks

- The observed duplicate may be caused by runtime mutation or stale Space state rather than current direct source.
- A future implementation must preserve input precedence and downstream variables.
- No automated visual regression exists for duplicate input surfaces.
- Central queue/status docs still need a small update after merge if connector editing permits.

## Next recommended step

Start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS` to lock the single-input target before any `presidio_streamlit.py` implementation.
