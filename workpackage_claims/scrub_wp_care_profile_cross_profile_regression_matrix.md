# Workpackage claim — SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-care-profile-cross-profile-regression-matrix`  
Claimed: 2026-08-03 18:34 Europe/Amsterdam  
Status: completed

## Scope

Build a deterministic, synthetic cross-profile regression matrix for:

- `Zorgcontrole — streng`;
- `Juridische controle — streng`;
- `Algemene Nederlandse controle`;
- `Algemene internationale controle`.

The matrix must verify profile entity composition, dedicated care/legal isolation, shared Dutch identity coverage, exact-span collision behavior, candidate-scanner dispatch, clinical preservation and unchanged legal context behavior.

## Boundaries

- Pure helpers, tests, evidence and governance only.
- No `presidio_streamlit.py`, review table, export, Scrub Key or reinsert changes.
- Deterministic custom recognizers only; generic NER observations are recorded separately and are not simulated.
- Synthetic data only.
- Human review remains mandatory.
- No production-readiness claim.

## Dependencies

Completed:

- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`
- `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`
- `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`

## Intended outputs

- pure cross-profile matrix helper;
- machine-readable validation artifact;
- targeted and full regression tests;
- `WORKPACKAGES.md`, `CHANGELOG.md`, `RISK_REGISTER.md` updates;
- handover in `handover/workpackages/`.

## Next gate

`SCRUB-WP_CARE_PROFILE_APP_VERIFY` after merge/deployment sync evidence is available.
