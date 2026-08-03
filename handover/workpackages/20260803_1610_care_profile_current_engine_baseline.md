# Handover — SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE

Repository: solidprivacy-nl/scrub  
Workpackage title: Current-engine Zorgfilter baseline  
Status: completed; final clean PR validation initiated

## Summary

Measured the unchanged deterministic Dutch custom recognizers against the approved eight-document synthetic care corpus. The corrected exact-span baseline contains 81 replace/review expectations: 25 values were found as exact normalized spans, 14 under the correct entity type, 11 were misclassified and 56 were missed. No designated clinical preserve passage was overlapped by the bounded current custom recognizers.

## Files added

- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `care_profile_baseline_summary.py`
- `tests/test_care_profile_baseline_summary.py`
- `output/validation/care_profile_v1_current_engine_baseline.json`
- `workpackage_claims/scrub_wp_care_profile_current_engine_baseline.md`
- `handover/workpackages/20260803_1610_care_profile_current_engine_baseline.md`

## Files changed

- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `ROADMAP.md`

## Tests

- Exact normalized span-matching contract, including the AGB/BIG numeric-prefix collision.
- Compact baseline summary count and policy contracts.
- Reproducibility test comparing the committed JSON artifact with freshly generated output.
- Existing full repository regression suite.

## Validation

- Diagnostic run #1825: 918 existing/new non-diagnostic tests passed and one intentional diagnostic emission failed after producing the first report.
- Initial substring result was rejected because it incorrectly counted an AGB prefix inside a BIG number.
- Corrected baseline result: 25/81 spans, 14/81 correct entities, 11 misclassified, 56 missed, 0 protected clinical overlaps.
- All temporary workflow and diagnostic files are removed.
- Final clean GitHub Actions status: initiated on the cleaned branch head.
- Hugging Face sync: not functionally relevant; no runtime or UI behavior changed.
- App verification: not applicable.

## Remaining risks

- Generic NER is excluded, so PERSON and e-mail misses are not full-app measurements.
- Review-selected care entities are severely underdetected: 4/42 spans found and 3/42 correctly classified.
- An eight-digit AGB value can collide with BSN recognition without care context.
- Current broad healthcare/legal reference entities find several spans but do not express the approved care policy.
- Production readiness remains false and human review remains required.

## Next recommended step

Run `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE` and classify each missed or misclassified expectation before freezing dedicated care-recognizer contracts.
