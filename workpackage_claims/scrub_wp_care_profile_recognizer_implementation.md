# Workpackage claim — SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION

Repository: `solidprivacy-nl/scrub`  
Claimed at: 2026-08-03 16:42 Europe/Amsterdam  
Status: completed

## Scope

- Implement the frozen pure `dutch_care_recognizers.py` module.
- Implement exactly the sixteen dedicated care entities and two public helper functions.
- Pass the 37 positive exact-span and 16 negative/collision/clinical-preservation contracts.
- Add implementation validation and a machine-readable result artifact.
- Do not register the recognizers in the current app yet.

## Boundaries

- Synthetic data only.
- No Streamlit, network, AI, cloud or file-write behavior in the recognizer module.
- No current profile selector, threshold or entity-default change.
- No export, Scrub Key or reinsert semantic change.
- Generic PERSON and e-mail remain generic-profile responsibilities.
- Human review remains required and production readiness remains false.
