# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

## Status

Implemented; targeted validation passed; PR verification pending.

## Summary

The frozen binding contract is implemented as a pure helper module. Binding IDs, bound placeholders, canonical mapping digests, bound-key validation and all eight document/key statuses are available without integrating current export, reinsert or UI paths.

## Files added

- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `tests/test_scrub_key_binding_model_validation.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`
- `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_model_implementation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Deterministic injected and normal local binding-ID generation.
- Binding-ID validation.
- Automatic/manual bound placeholder build/parse and strict rejection.
- Document binding-ID extraction.
- Exact canonical payload/digest, metadata exclusions and semantic sensitivity.
- Bound-key schema/policy/item/duplicate/digest validation.
- All eight frozen document/key status cases.
- Six fail-closed paths and explicit legacy-unbound compatibility.
- Input immutability.
- No Streamlit, network, AI, file-writing or integration side effects.
- Existing contract, secure import/export and roundtrip tests included in targeted validation.

## Validation

- Targeted model/contract/legacy/roundtrip tests: passed.
- Contract fixture digest: matched exactly.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally applicable; no runtime/app code changed.
- App verification: not applicable; no visible behavior changed.

## Notes / risks

- Current exports remain legacy/unbound until the next package.
- Current reinsert does not yet enforce binding.
- Mapping digest is not cryptographic authenticity.
- Legacy keys remain explicitly unbound.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after merge.
