# Handover — WP28B Scrub Key warning implementation planning

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP28B — Scrub Key warning implementation planning`

Status: completed UI/security implementation-planning-only.

## Summary

WP28B created a planning document that translates the WP27 Scrub Key warning UX plan and WP28 expiry/delete policy into exact future implementation locations, acknowledgement states and Dutch copy inventory. The plan maps warning placement to the current Streamlit patch surface without changing UI behavior.

The plan covers Scrub Key creation, Scrub Key download/export, local storage/Downloads guidance, import/reload, reinsert mode, pasted-text reinsert, TXT reinsert, DOCX reinsert, future PDF-to-TXT scope, restored output downloads, expiry/delete guidance, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch warnings.

## Files added

- `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`
- `handover/workpackages/20260612_1415_scrub_key_warning_implementation_planning.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

No tests were run. This was documentation/planning-only.

No local pytest was run through the ChatGPT GitHub connector environment.

## Validation status

- Required start sequence was followed from GitHub `main`.
- Relevant Scrub Key specs and policies were read.
- Current helper/UI context was inspected:
  - `SCRUB_KEY_THREAT_MODEL.md`
  - `SCRUB_KEY_LIFECYCLE_SPEC.md`
  - `SCRUB_KEY_WARNING_UX_PLAN.md`
  - `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
  - `SCRUB_KEY_SPEC.md`
  - `PARALLEL_SPEC_CONSOLIDATION_WP58.md`
  - `scrub_key.py`
  - `scrub_key_import.py`
  - `scrub_key_reinsert.py`
  - `fix_streamlit_nested_expanders.py`
  - `presidio_streamlit.py`
  - `RISK_REGISTER.md`
  - `DECISION_LOG.md`
- No code, test, UI, dependency, helper, schema, import/export, reinsert, encryption, deletion or expiry behavior was changed.

## GitHub Actions status

- Not applicable for behavior validation; documentation/planning-only.
- No workflow runs were expected for this planning-only change through the connector workflow.

## Hugging Face sync status

- Not applicable for app behavior. No UI/runtime behavior changed.

## App verification status

- Not applicable; no UI changed.

## Remaining risks

- The warning and acknowledgement UI is still not implemented.
- WP28B does not add encryption, automatic deletion, expiry blocking, protected storage, tamper-proof key containers or local vault behavior.
- The next UI implementation package must avoid silently changing export/reinsert semantics.
- The current Streamlit warning implementation surface is patch-based and therefore fragile; tests should cover warning placement and acknowledgement gating.

## Next recommended step

- `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
- Alternative if the coordinator wants tests before UI edits: `WP29C — Scrub Key warning UI regression test scaffolding`.
