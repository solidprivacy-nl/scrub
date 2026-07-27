# Handover — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

## Status

Completed; targeted and full PR validation passed; merge pending.

## Summary

The critical same-placeholder wrong-key finding was classified and routed to a test-first implementation line. The recommended MVP contract adds one non-sensitive document binding ID to every automatic/manual placeholder and the corresponding Scrub Key, plus a canonical mapping digest for accidental corruption. No product behavior was changed.

## Files added

- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`
- `tests/test_mvp_scrub_key_document_binding_gap_triage.py`
- `tests/test_mvp_scrub_key_document_binding_gap_triage_validation.py`
- `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Source critical finding must be consumed by triage.
- Accidental mismatch, accidental corruption and malicious tampering must remain distinct.
- Weak binding options must remain rejected.
- Recommended binding must be cross-format and preserve the three-step UX.
- Mapping digest must not be represented as authenticity.
- Bound mismatch/mixed IDs/invalid digest must be fail-closed requirements.
- Approved sequence must remain test-first.
- Validation evidence and temporary-workflow cleanup are contract-tested.

## Validation

- Targeted triage and source-evidence tests: passed.
- Critical findings triaged: 1.
- Medium findings triaged: 1.
- Implementation authorized: false.
- GitHub Actions run #1695: passed.
- Hugging Face sync: not functionally applicable; no runtime/app code changed.
- App verification: not applicable; no visible behavior changed.

## Notes / risks

- Binding IDs mitigate accidental wrong-key pairing but are not secret and do not stop a fully malicious editor who changes both document and key.
- An unkeyed mapping digest detects accidental edits but is not a signature.
- Strong malicious-tampering protection requires protected local signing-key management.
- Legacy keys remain unbound and require explicit status/warning.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Merge PR #41 and start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.
