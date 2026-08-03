# Handover — SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub  
Workpackage title: Zorgfilter v1 recognizer contract tests  
Status: implemented; validation pending

## Summary

Frozen the dedicated Zorgfilter v1 recognizer contract before implementation. The contract defines sixteen care-specific entities, the future pure helper API, 37 positive exact-span fixtures and 16 negative/collision/clinical-preservation fixtures. No recognizer or UI behavior changed.

## Files added

- `CARE_RECOGNIZER_CONTRACT_V1.md`
- `care_recognizer_contracts.py`
- `care_recognizer_contract_summary.py`
- `tests/test_care_recognizer_contracts.py`
- `scripts/generate_care_recognizer_contract_summary.py`
- `output/validation/care_recognizer_contract_v1_summary.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_contract_tests.md`
- `handover/workpackages/20260803_1634_care_profile_recognizer_contract_tests.md`

## Tests

- Future public API and supported-language contract.
- Sixteen dedicated care entities fully covered by positive fixtures.
- Exact expected values and context/role preservation.
- Replace versus review-selected policy alignment.
- Care-event date versus date-of-birth separation.
- AGB versus BSN/BIG precedence.
- Clinical preservation for vital signs, medication, dosages, times, lab results, DBC/ICD codes and role words.
- Reproducibility of the committed contract summary.

## Validation

- GitHub Actions: pending.
- Hugging Face sync: not functionally relevant; no runtime/UI behavior changed.
- App verification: not applicable.

## Remaining risks

- The contract is specification data, not a recognizer implementation.
- Generic PERSON and e-mail behavior remains outside the dedicated care module.
- Contextual organization/location recognition may require conservative patterns to avoid broad spans.
- AGB/BSN overlap must be solved deterministically in implementation and later profile integration.
- Human review remains required and production readiness remains false.

## Next recommended step

Implement `dutch_care_recognizers.py` against the frozen 37 positive and 16 negative contracts without registering it in the app yet.
