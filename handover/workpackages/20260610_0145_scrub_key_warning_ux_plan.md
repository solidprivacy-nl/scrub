# Handover — WP27 Scrub Key warning UX plan

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP27 — Scrub Key warning UX plan`

Status: completed UX/security specification-only.

## Summary

WP27 created `SCRUB_KEY_WARNING_UX_PLAN.md`, converting WP25/WP26 Scrub Key threat and lifecycle findings into user-facing warning and acknowledgement expectations. The plan defines severity levels, MVP acknowledgement expectations, proposed Dutch UI copy and later secure/local desktop blocking candidates.

The plan covers Scrub Key creation, download/export, local storage, import/reload, reinsert mode, restored output download, deletion/expiry guidance, shared-computer risk, e-mail/AI upload risk, loss-of-key warning and tampering/mismatch warning.

## Files added

- `SCRUB_KEY_WARNING_UX_PLAN.md`
- `handover/workpackages/20260610_0145_scrub_key_warning_ux_plan.md`

## Files changed

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added or changed.
- No tests run because this was documentation/UX-security specification only.
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
  - `SCRUB_KEY_LIFECYCLE_SPEC.md`
  - `SCRUB_KEY_SPEC.md`
  - `PARALLEL_SPEC_CONSOLIDATION_WP58.md`
- Context-only files inspected:
  - `scrub_key.py`
  - `scrub_key_import.py`
  - `scrub_key_reinsert.py`
  - `fix_streamlit_nested_expanders.py`
- Validation type: documentation/UX-security review only.

## GitHub Actions status

- To be checked by connector after this handover commit.

## Hugging Face sync status

- To be checked by connector after this handover commit.

## App verification status

- Not applicable. No UI changed.

## Remaining risks

- R2 remains critical/mitigating because warning UX is specified but not implemented.
- No implemented warning acknowledgement controls exist yet.
- No expiry/delete policy exists yet.
- No secure import/export regression test package exists yet.
- No encryption/protection implementation exists yet.
- No tamper-proof/authenticated Scrub Key format exists yet.
- No local vault / managed key store exists yet.
- No approved key recovery model exists yet.

## Next recommended step

- `WP28 — Scrub Key expiry/delete policy`.

## Intentionally not changed

- No UI implementation.
- No Streamlit patch changed.
- No helper logic changed.
- No Scrub Key JSON schema migration.
- No encryption implementation.
- No import/export behavior changed.
- No reinsert behavior changed.
- No tests added or changed.
- No dependencies changed.
- No secrets stored.
- No real data stored.
- No release notes changed, because this workpackage changed internal UX/security documentation only and did not add a user-facing capability.
