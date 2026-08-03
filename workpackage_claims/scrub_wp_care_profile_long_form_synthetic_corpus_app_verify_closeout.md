# Workpackage claim — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-care-long-form-app-verify-closeout`  
Claimed: 2026-08-03 23:26 Europe/Amsterdam  
Status: completed; final documentation-only GitHub Actions confirmation pending

## Goal

Record the coordinator/user confirmation that the deployed long-form synthetic Zorgfilter examples work as intended, then close the implementation package without changing product code or UI behavior.

## Evidence available

- PR #56 merged to `main` as `1244663d3e69a56d6efc825a6fc019ba72d3782a`.
- Final clean PR run #1926: 1003 tests passed in 11.51s.
- Deployment verification run #1931:
  - `care_test_examples.py` exact byte match between GitHub and Hugging Face;
  - `care_test_example_expansions.py` exact byte match between GitHub and Hugging Face;
  - Streamlit health HTTP 200 / `ok`;
  - 1003 tests passed in 11.35s.
- Coordinator/user app verification at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

## Scope

- update the original workpackage status and handover;
- update `WORKPACKAGES.md` and `CHANGELOG.md`;
- add a closeout handover;
- run a clean documentation-only regression through GitHub Actions.

## Boundaries

- verification/closeout only;
- no product code, UI, corpus, recognizer, profile, export, Scrub Key or reinsert change;
- no Hugging Face runtime change;
- synthetic data and human-review boundaries remain unchanged.
