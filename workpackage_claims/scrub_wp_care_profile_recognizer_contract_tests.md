# Workpackage claim — SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS

Repository: `solidprivacy-nl/scrub`  
Claimed at: 2026-08-03 16:32 Europe/Amsterdam  
Status: in_progress

## Scope

- Freeze versioned positive, value-only, context-preservation, policy and negative fixtures for dedicated Zorgfilter recognizers.
- Freeze the later public helper API without implementing it.
- Cover care-reference entities, contextual review entities, AGB/BSN precedence and clinical-content preservation.
- Add no recognizer implementation or UI integration.

## Boundaries

- Synthetic data only.
- No changes to current recognizer registration or behavior.
- No profile selector, threshold, export, Scrub Key or reinsert change.
- Generic PERSON/e-mail remain generic-profile dependencies.
- Human review remains required and production readiness remains false.
