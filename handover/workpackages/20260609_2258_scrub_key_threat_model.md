# Handover — WP25 Scrub Key threat model

Repository: `solidprivacy-nl/scrub`  
Workpackage title: `WP25 — Scrub Key threat model`  
Status: completed security/specification-only

## Summary

WP25 created a formal Scrub Key threat model. The Scrub Key is treated as sensitive re-identification data because it maps placeholders back to real confidential values. The threat model explains why Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists, and defines key handling risks and minimum future warning/lifecycle requirements.

## Files added

- `SCRUB_KEY_THREAT_MODEL.md`
- `handover/workpackages/20260609_2258_scrub_key_threat_model.md`

## Files changed

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added or changed.
- No tests run because this was documentation/security review only.
- No code, helper logic, UI, dependencies or behavior changed.

## Validation status

- Documentation/specification review completed.
- Required start sequence read: `AGENTS.md`, `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Additional context read: `RISK_REGISTER.md`, `DECISION_LOG.md`, `STATUS_MONITORING_RUNBOOK.md`, `RELEASE_NOTES.md`, `SCRUB_KEY_SPEC.md`, `scrub_key.py`, `scrub_key_import.py`, `scrub_key_reinsert.py`.
- `scrub_key_export.py` was requested for context but was not present at the expected repository path; no code changes were made.

## GitHub Actions status

- Not checked before handover creation; documentation/security-specification-only change.

## Hugging Face sync status

- Not checked before handover creation; documentation/security-specification-only change.

## App verification status

- Not applicable. No UI behavior changed.

## Remaining risks

- Scrub Key leakage remains critical until lifecycle, encryption/protection and deletion policy are specified and implemented.
- No encrypted/protected Scrub Key format exists yet.
- No expiry/delete policy is implemented.
- No dedicated warning UX plan covers all Scrub Key touchpoints yet.
- No secure import/export regression test package exists yet.
- Download-folder retention, email/AI upload and shared-computer risks remain user-process risks until future work addresses them.

## Next recommended step

- `WP26 — Scrub Key encryption/lifecycle specification`.

## Explicitly not changed

- No helper logic changed.
- No Scrub Key JSON schema migration.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No encryption implemented.
- No dependencies changed.
- No tests added or changed.
- No secrets or real data stored.
