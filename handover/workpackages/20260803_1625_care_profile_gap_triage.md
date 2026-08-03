# Handover — SCRUB-WP_CARE_PROFILE_GAP_TRIAGE

Repository: solidprivacy-nl/scrub  
Workpackage title: Zorgfilter v1 gap triage  
Status: implemented; validation pending

## Summary

Classified all 81 current-engine care-corpus expectations into explicit follow-up routes. The triage separates existing recognizer reuse, generic profile dependencies, dedicated care references, care-specific reclassification, contextual review recognition and AGB/numeric collision safeguards. No recognizer or UI behavior changed.

## Files added

- `CARE_PROFILE_GAP_TRIAGE.md`
- `care_profile_gap_triage.py`
- `care_profile_gap_triage_summary.py`
- `tests/test_care_profile_gap_triage.py`
- `scripts/generate_care_profile_gap_triage.py`
- `output/validation/care_profile_v1_gap_triage.json`
- `workpackage_claims/scrub_wp_care_profile_gap_triage.md`
- `handover/workpackages/20260803_1625_care_profile_gap_triage.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests

- All 81 expectations classified with no unclassified items.
- Baseline status counts preserved.
- Route counts frozen.
- AGB/BSN collision route required for every AGB expectation.
- Broad healthcare-reference matches routed to care-specific reclassification.
- Generic PERSON/e-mail exclusions not converted into unsafe numeric/name regex work.
- Committed triage summary reproducible from the pure helper.

## Validation

- GitHub Actions: pending.
- Hugging Face sync: not functionally relevant; no runtime/UI behavior changed.
- App verification: not applicable.

## Remaining risks

- Triage routes are contract direction, not recognizer implementation.
- Generic NER behavior remains to be measured in the later cross-profile matrix.
- Contextual provider/organization/date recognition is the largest gap family and carries over-masking risk.
- AGB/BSN precedence must be resolved in tests before implementation.
- Clinical preservation and human review remain mandatory.

## Next recommended step

Start `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS` and freeze positive, value-only, collision and clinical-preservation fixtures before writing care recognizers.
