# Handover — SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Workpackage title: Zorgfilter v1 recognizer implementation  
Status: implemented; final governance and clean validation pending

## Summary

Implemented the pure `dutch_care_recognizers.py` module against the frozen contract. Sixteen dedicated care entities are recognized through bounded labels and professional context. The module is not registered in the app yet. All 37 positive contracts, 16 negative/collision contracts and 54 dedicated expectations in the eight-document synthetic corpus pass, with zero protected clinical phrase overlaps.

## Files added

- `dutch_care_recognizers.py`
- `care_recognizer_validation.py`
- `CARE_RECOGNIZER_IMPLEMENTATION_V1.md`
- `scripts/generate_care_recognizer_validation.py`
- `tests/test_dutch_care_recognizers.py`
- `tests/test_care_recognizer_validation.py`
- `output/validation/care_recognizer_implementation_validation.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_implementation.md`
- `handover/workpackages/20260803_1652_care_profile_recognizer_implementation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests

- Frozen public API and sixteen-entity scope.
- All 37 positive exact-span contracts.
- All 16 negative, collision and clinical-preservation contracts.
- Exact Presidio result spans, explanations and metadata.
- Module-purity import guard.
- All 54 dedicated care expectations in the eight-document synthetic corpus.
- Zero overlap with protected clinical passages.
- Reproducibility of the committed validation artifact.

## Validation

- Initial run #1850 identified five bounded missing context variants; no clinical-overmasking failure.
- Corrected variants: Dutch `cliëntnummer`, `receptnummer`, generic `incidentnummer`, and lowercase `woonzorgcentrum` after a labeled location field.
- GitHub Actions run #1854: 953 tests passed.
- Final clean GitHub Actions: pending after governance finalization.
- Hugging Face sync: not functionally relevant; no current runtime/UI registration changed.
- App verification: not applicable.

## Remaining risks

- The recognizers are not yet composed into a Zorg profile or registered in the app.
- Generic PERSON and e-mail remain generic-profile dependencies.
- Existing BSN and new AGB overlap requires deterministic profile-level precedence validation.
- Synthetic contract success does not establish production precision or recall.
- Human review remains mandatory and production readiness remains false.

## Next recommended step

Start `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR` to centralize the four profile definitions and collision/policy composition before changing the visible Streamlit selector.
