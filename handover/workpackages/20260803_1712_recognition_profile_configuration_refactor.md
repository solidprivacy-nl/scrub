# Handover — SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR

Repository: solidprivacy-nl/scrub  
Workpackage title: Recognition profile configuration refactor  
Status: completed; final clean PR validation initiated

## Summary

Added a pure central profile model for General Dutch, Care, Legal and International recognition. The current visible three-profile options remain unchanged. The future Streamlit and desktop orders, thresholds, entity groups, care policy actions and exact-span collision precedence are now explicit and testable. No care recognizer is registered and no live UI behavior changed.

## Files added

- `recognition_profiles.py`
- `recognition_profile_validation.py`
- `RECOGNITION_PROFILE_CONFIGURATION.md`
- `tests/test_recognition_profiles.py`
- `tests/test_recognition_profile_validation.py`
- `output/validation/recognition_profile_configuration.json`
- `workpackage_claims/scrub_wp_recognition_profile_configuration_refactor.md`
- `handover/workpackages/20260803_1712_recognition_profile_configuration_refactor.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests

- Current three-profile order and labels remain exact.
- Future four-profile Streamlit and compact desktop orders.
- Threshold, candidate/example and entity-group configuration.
- Profile lookup and isolation between Care and Legal.
- Care replace/review-selected policy composition.
- Exact-span AGB-over-BSN and care-specific-over-legacy precedence.
- Partial overlaps and unrelated entities remain untouched.
- Mapping/object result support and stable input order.
- Reproducibility of the committed configuration artifact.

## Validation

- Initial profile-configuration run #1865: 965 tests passed before documentation/artifact finalization.
- All temporary governance operator and workflow files are removed.
- Final clean GitHub Actions: initiated on this handover commit.
- Hugging Face sync: not functionally relevant; no live runtime/UI integration changed.
- App verification: not applicable.

## Remaining risks

- The central model is not yet imported by the current app.
- Care recognizers remain unregistered.
- Profile-level AGB/BSN precedence must be verified with real Presidio results during integration.
- The Care candidate scanner is configuration direction; no broad candidate scanner is introduced here.
- Human review remains mandatory and production readiness remains false.

## Next recommended step

Start `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION` sequentially. Register care recognizers, use the central configuration, expose the fourth profile, load synthetic care examples, apply exact-span collision resolution and verify the deployed app without altering export, Scrub Key or reinsert semantics.
