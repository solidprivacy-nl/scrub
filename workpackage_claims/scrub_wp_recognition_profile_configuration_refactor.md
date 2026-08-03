# Workpackage claim — SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR

Repository: `solidprivacy-nl/scrub`  
Claimed at: 2026-08-03 17:04 Europe/Amsterdam  
Status: completed

## Scope

- Add a pure central `recognition_profiles.py` configuration model for General Dutch, Care, Legal and International profiles.
- Freeze profile order, labels, thresholds, entity composition, candidate/example behavior and care policy actions.
- Add deterministic exact-span precedence rules for care-specific entities versus broad legacy entities and AGB versus BSN.
- Preserve the currently visible three-profile UI until the later integration package.
- Do not edit `presidio_streamlit.py` or register care recognizers in this package.

## Boundaries

- Synthetic data only.
- No current UI, threshold or analyzer behavior change.
- No export, Scrub Key or reinsert semantic change.
- No cloud processing or new dependency.
- Human review remains required and production readiness remains false.
