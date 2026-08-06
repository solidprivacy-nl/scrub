# Workpackage claim — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION

Status: completed  
Implementation status: `RELEASE_CANDIDATE_READY`  
Governance status: pending independent assurance

Claimed: 2026-08-06 11:37 Europe/Amsterdam  
Implementation completed: 2026-08-06 11:59 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Branch: `wp/processed-text-selection-cross-flow-regression`  
Role: `implementation_operations`

## Scope

Adopt the canonical cross-project implementation-versus-release-assurance model used by `market-predictions/weekly-etf`, with a Scrub-specific blind-review boundary.

The assurance worker must independently reconstruct the candidate from source, acceptance criteria and machine evidence. Before issuing its own decision, it must not read the implementation handover, implementation self-assessment or implementation conclusions.

## Boundaries

- governance and control files only;
- no product behavior, recognizer, export, Scrub Key, reinsert, audit or UI semantic changes;
- no implementation worker may issue the governance PASS for its own candidate;
- governance may not silently repair the candidate it reviews.

## Candidate evidence

- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
- updated project prompts, roadmap, workpackages, changelog and decision log
- `handover/workpackages/20260806_1156_two_role_governance_adoption.md`

## Validation status

- Candidate PR: pending creation
- GitHub Actions: pending candidate PR
- Hugging Face sync: not applicable; no runtime files changed
- App verification: not applicable; no UI behavior changed
- Independent governance decision: pending and deliberately not issued by implementation

## Next step

A separate `governance_release_assurance` worker/session must claim `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY`, record its initial `PASS`, `FAIL` or `INDETERMINATE` before opening the implementation handover, and must not modify the candidate under review.
