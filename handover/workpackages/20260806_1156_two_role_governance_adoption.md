# Handover — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`; independent assurance pending

## Summary

Adopted the canonical cross-project two-role governance model used by the Weekly ETF donor architecture and added a Scrub-specific blind-review boundary. Implementation and governance/release assurance are now distinct roles and workpackages. Implementation cannot certify its own candidate; assurance cannot silently repair it.

Before its initial `PASS`, `FAIL` or `INDETERMINATE`, the assurance worker may inspect the requested outcome, authoritative project files, candidate source/diff, acceptance criteria and raw machine/deployment evidence, but must not read this handover, implementation self-assessment or implementation conclusions.

## Files added

- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
- `workpackage_claims/scrub_wp_two_role_governance_adoption.md`
- `handover/workpackages/20260806_1156_two_role_governance_adoption.md`

## Files changed

- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`

## Tests

- No product test added specifically for the governance text.
- Existing repository tests must run on the exact PR head.
- Independent governance must inspect control-file consistency without relying on this implementation handover before its initial decision.

## Validation

- GitHub Actions: pending on candidate PR
- Hugging Face sync: not applicable; no runtime or deployment files changed
- App verification: not applicable; no UI behavior changed
- Independent governance status: pending; implementation deliberately issued no PASS

## Remaining risks

- Current enforcement maturity is `LEVEL_1_CHECKLIST`; documentation does not yet provide a hard CI assurance gate.
- True conclusion isolation depends on a separate worker/session respecting the blind-review input contract.
- Promotion to `LEVEL_2_MACHINE_EVIDENCE` needs a later structured assurance-record package.

## Next recommended step

- A separate `governance_release_assurance` worker/session claims `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY`, reconstructs the candidate from source and raw evidence, records its initial decision before opening this handover, and does not modify the candidate under review.
