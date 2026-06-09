# Handover — WP26 Scrub Key encryption/lifecycle specification

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP26 — Scrub Key encryption/lifecycle specification`

Status: completed security/lifecycle-specification-only.

## Summary

WP26 created `SCRUB_KEY_LIFECYCLE_SPEC.md` and defined the Scrub Key lifecycle and protection model following WP25. The specification treats the Scrub Key as sensitive re-identification data and defines lifecycle states from creation through deletion, plus loss-of-key, tampering, passphrase, recovery, metadata, audit/logging and UI-warning expectations.

The recommended MVP path is warning-only plus explicit lifecycle guidance and protected-local-file guidance. Encrypted local files, local vault / managed key store, key recovery, authenticated containers and schema/container changes are reserved for later professional/local desktop workpackages.

## Files added

- `SCRUB_KEY_LIFECYCLE_SPEC.md`
- `handover/workpackages/20260610_0015_scrub_key_lifecycle_spec.md`

## Files changed

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added or changed.
- No tests run because this was documentation/security lifecycle specification only.
- No code or test files were changed.

## Validation status

- Required start sequence read:
  - `AGENTS.md`
  - `PROJECT_PROMPT.md`
  - `ROADMAP.md`
  - `WORKPACKAGES.md`
  - `CHANGELOG.md`
- Required context read:
  - `RISK_REGISTER.md`
  - `DECISION_LOG.md`
  - `STATUS_MONITORING_RUNBOOK.md`
  - `RELEASE_NOTES.md`
  - `SCRUB_KEY_THREAT_MODEL.md`
  - `SCRUB_KEY_SPEC.md`
  - `PARALLEL_SPEC_CONSOLIDATION_WP58.md`
- Context-only helpers inspected:
  - `scrub_key.py`
  - `scrub_key_import.py`
  - `scrub_key_reinsert.py`
- Validation type: documentation/security lifecycle review only.

## GitHub Actions status

- To be checked by connector after this handover commit.

## Hugging Face sync status

- To be checked by connector after this handover commit.

## App verification status

- Not applicable. No UI changed.

## Remaining risks

- R2 remains critical/mitigating because lifecycle is now specified but not implemented.
- No encryption/protection implementation exists yet.
- No expiry/delete implementation exists yet.
- No dedicated warning UX plan exists yet.
- No secure import/export regression test package exists yet.
- No tamper-proof/authenticated key format exists yet.
- No local vault / managed key store exists yet.
- No approved key recovery model exists yet.

## Next recommended step

- `WP27 — Scrub Key warning UX plan`.
- Alternative next step depending on consolidation: `WP29 — Scrub Key secure import/export tests`.

## Intentionally not changed

- No encryption implemented.
- No Scrub Key JSON schema migration.
- No helper logic changed.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No dependencies changed.
- No tests added or changed.
- No secrets stored.
- No real data stored.
- No release notes changed, because this workpackage changed internal lifecycle/security documentation only and did not add a user-facing capability.
