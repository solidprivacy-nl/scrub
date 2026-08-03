# Handover — SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION

Repository: solidprivacy-nl/scrub  
Workpackage title: Zorgfilter v1 policy and corpus foundation  
Status: completed; final clean PR validation initiated

## Summary

Recorded the approved Zorgfilter v1 policy and workpackage sequence. Added a pure policy contract, eight fully synthetic care-document families, corpus contract tests and a deterministic baseline helper for the current Dutch custom recognizers. No recognizer or UI behavior has changed.

## Files added

- `CARE_PROFILE_V1_PLAN.md`
- `care_profile_policy.py`
- `care_test_examples.py`
- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_policy_contract.py`
- `tests/test_care_profile_corpus_contracts.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `workpackage_claims/scrub_wp_care_profile_v1_policy_and_corpus_foundation.md`
- `handover/workpackages/20260803_1531_care_profile_v1_policy_and_corpus_foundation.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`

## Tests

- Pure policy-contract tests.
- Synthetic corpus structural and policy-alignment tests.
- Current deterministic recognizer baseline-schema tests.

## Validation

- Initial GitHub Actions run: 917 passed, 1 new corpus-contract test failed because a valid discharge-letter preserve phrase lacked one of the test's clinical marker words.
- Corrective action: replaced the brittle marker-word assertion with a contract for multiple protected clinical passages that remain disjoint from replace/review values.
- GitHub Actions run #1818: 918 tests passed on the corrected implementation.
- Final clean PR validation: initiated after all temporary workflow/operator files were removed.
- Hugging Face sync status: not functionally relevant; no runtime/UI change.
- App verification status: not applicable.

## Remaining risks

- The current broad `NL_HEALTHCARE_REFERENCE` behavior remains unchanged and must be split through later evidence-driven recognizer packages.
- The baseline excludes generic NER-model results and is not a production benchmark.
- Exact care-date, provider, organization and location policy requires later recognizer precision testing.
- Human review remains mandatory.

## Next recommended step

Generate and inspect the current-engine baseline report, perform gap triage, then freeze care-recognizer contracts before implementing care-specific recognizers.
