# Workpackage claim — SCRUB-WP_CARE_PROFILE_APP_VERIFY

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-care-profile-app-verify`  
Claimed: 2026-08-03 19:05 Europe/Amsterdam  
Status: in_progress

## Scope

Verification and closeout only for the deployed Zorgfilter v1 current-UI integration.

Required sequence:

1. independently verify GitHub-to-Hugging-Face file synchronization;
2. verify the Hugging Face Space health endpoint;
3. record technical deployment evidence;
4. request coordinator/user verification of the exact visible profile behavior;
5. close only after that confirmation.

## Technical verification targets

- exact byte equality for the relevant integration files between GitHub `main` and Hugging Face Space `solidprivacy/scrub`;
- `Zorgcontrole — streng` present in deployed `presidio_streamlit.py`;
- profile-aware review status and Care helper imports present;
- Hugging Face Space health endpoint responds successfully.

## User-visible verification targets

- four profile choices are visible;
- `Juridische controle — streng` remains the initial default;
- `Zorgcontrole — streng` shows the care description and eight synthetic examples;
- provider/location/date review-selected rows show `Controle nodig` while remaining selected;
- patient/client identity rows remain selected for replacement;
- candidate care references remain unchecked;
- Legal, General Dutch and International profiles remain selectable;
- export, Scrub Key and reinsert flows remain present and unchanged.

## Boundaries

- verification-only; no product code, recognizer, UI, export, Scrub Key or reinsert changes;
- synthetic examples only;
- no production-readiness claim;
- human review remains mandatory.

## Dependencies

Completed:

- `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`
- `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`

## Closeout gate

Do not mark completed until technical sync/health evidence is green and the coordinator/user confirms the visible app behavior.
