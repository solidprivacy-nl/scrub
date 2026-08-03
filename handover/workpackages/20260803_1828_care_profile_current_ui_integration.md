# Handover — SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Zorgfilter v1 current Streamlit integration  
Status: implemented and regression-tested; final governance run, merge, sync and app verification pending

## Summary

Integrated the approved Zorgfilter v1 profile into the current Streamlit/analyzer flow. The fourth profile is visible in configuration, sixteen dedicated care recognizers are registered, central profile composition and exact-span collision precedence are used, and eight synthetic care examples are available. Review-selected care detections remain selected but show `Controle nodig`; unresolved strongly labelled administrative references are unchecked candidates. Clinical meaning remains a preservation target.

## Files added

- `care_candidate_scanner.py`
- `profile_ui_support.py`
- `CARE_PROFILE_CURRENT_UI_INTEGRATION.md`
- `output/validation/care_profile_current_ui_integration.json`
- `tests/test_care_candidate_scanner.py`
- `tests/test_profile_ui_support.py`
- `tests/test_presidio_helpers_care_registration.py`
- `tests/test_care_profile_current_ui_integration_snapshot.py`
- `workpackage_claims/scrub_wp_care_profile_current_ui_integration.md`
- `handover/workpackages/20260803_1828_care_profile_current_ui_integration.md`

## Files changed

- `presidio_helpers.py`
- `presidio_streamlit.py`
- `document_tools.py`
- `display_labels_nl.py`
- `ui_texts_nl.py`
- `ROADMAP.md` — pending finalizer
- `WORKPACKAGES.md` — pending finalizer
- `CHANGELOG.md` — pending finalizer
- `RELEASE_NOTES.md` — pending finalizer
- `RISK_REGISTER.md` — pending finalizer

## Tests

- Four visible profile labels and stable order.
- Legal remains the initial default selection.
- Care threshold and default entity composition.
- Care/Legal/General profile isolation.
- AGB-over-BSN and dedicated-care-over-legacy exact-span precedence.
- Review-selected reason and `Controle nodig` status while selected by default.
- Patient identity remains selected for replacement.
- Eight synthetic care examples.
- Conservative care candidate positive, overlap and clinical-negative cases.
- Care recognizer registration and supported-entity exposure.
- Static workflow-boundary checks for export, Scrub Key and reinsert imports/sections.
- Full repository regression suite.

## Validation status

- Initial PR run #1876 failed during test collection because the new registration test imported optional Streamlit UI dependencies that are intentionally absent from the lean CI environment.
- The test was isolated with temporary minimal dependency stubs; runtime code and CI dependencies remained unchanged.
- Corrected GitHub Actions run #1877: **983 tests passed in 9.69s**.
- Final clean run after governance finalization: pending.

## GitHub Actions status

- PR #53 is open.
- Latest validated run: #1877, green, 983 tests.

## Hugging Face sync status

Pending merge. The product change is not yet claimed as deployed.

## App verification status

Pending merge and sync. Required because the visible profile selector, profile copy and care examples changed.

## Remaining risks

- Cross-profile regression across complete legal, care and general corpora is still pending.
- Generic NER behavior must be assessed in the cross-profile matrix and deployed app.
- Synthetic evidence does not establish production recall or precision.
- Rare-case indirect identification remains a residual-risk/audit problem, not a blind-masking rule.
- Human review remains mandatory.

## Next recommended step

Finalize governance and release notes, run a clean full regression, merge PR #53, verify GitHub-to-Hugging-Face sync, then start `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX` before the formal deployed app-verification closeout.
