# Handover — Workpackage claim protocol and WP28C claim guard

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `Workpackage claim protocol and WP28C claim guard`

Status: completed governance/coordination-only.

## Summary

Added a lightweight GitHub-based claim protocol to reduce duplicate work by parallel workers. WP28C has been claimed as `in_progress` before implementation starts.

The mechanism is:

- workers check `workpackage_claims/` before starting a package;
- if a claim exists with `in_progress`, the second worker stops and reports it;
- if no claim exists, the worker creates a claim file with `GitHub.create_file` before editing code, tests, UI, export, schema or shared docs;
- when done, the worker updates the same claim file to `completed` with commit/PR, handover path, tests/checks and next step.

## Files added

- `workpackage_claims/README.md`
- `workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md`
- `handover/workpackages/20260612_1515_workpackage_claim_protocol_wp28c_claim.md`

## Files changed

- `AGENTS.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests/checks run

No tests run; governance/documentation-only change.

## Validation status

- Standard control files were read.
- Confirmed no prior `workpackage_claims/` claim protocol existed.
- Added the protocol and active WP28C claim.
- No product code changed.
- No test code changed.
- No UI behavior changed.
- No export/reinsert semantics changed.
- No Scrub Key schema changed.
- No dependency changed.
- No real data added.
- No cloud processing added.

## GitHub Actions status

To be checked after final handover commit.

## Hugging Face sync status

To be checked after final handover commit.

## App verification status

Not applicable; no UI behavior changed.

## Remaining risks

- Claim files are a lightweight process guard, not a hard GitHub branch lock.
- Stale `in_progress` claims still require coordinator judgement before reassignment.
- WP28C implementation still needs to be completed and then update the WP28C claim to `completed`.

## Next recommended step

Continue the claimed `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
