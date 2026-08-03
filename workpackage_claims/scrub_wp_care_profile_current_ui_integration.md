# Workpackage claim — SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION

Repository: `solidprivacy-nl/scrub`  
Claimed at: 2026-08-03 17:18 Europe/Amsterdam  
Status: in_progress

## Scope

- Register the pure Dutch care recognizers in the current local analyzer.
- Use the central recognition-profile configuration in the Streamlit application.
- Add `Zorgcontrole — streng` as the fourth visible profile without changing the existing three labels or order relative to each other.
- Add synthetic care-example loading and care-profile explanation.
- Resolve exact-span care/legacy and AGB/BSN collisions for the Care profile.
- Keep existing review, export, Scrub Key and reinsert semantics unchanged.

## Boundaries

- UI integration is sequential; no parallel worker may edit the same Streamlit/analyzer flow.
- Synthetic data only in the public prototype.
- No broad care candidate scanner or silent profile switching.
- No cloud document processing or new dependency.
- No export filename, MIME type, Scrub Key schema or reinsert behavior change.
- Human review remains required and production readiness remains false.
- Hugging Face sync and live app verification are required after merge.
