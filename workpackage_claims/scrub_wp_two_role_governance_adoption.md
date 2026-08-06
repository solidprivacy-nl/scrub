# Workpackage claim — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION

Status: in_progress

Claimed: 2026-08-06 11:37 Europe/Amsterdam  
Repository: solidprivacy-nl/scrub  
Branch: wp/processed-text-selection-cross-flow-regression  
Role: implementation_operations

## Scope

Adopt the canonical cross-project implementation-versus-release-assurance model used by `market-predictions/weekly-etf`, with a Scrub-specific blind-review boundary.

The assurance worker must independently reconstruct the candidate from source, acceptance criteria and machine evidence. Before issuing its own decision, it must not read the implementation handover, implementation self-assessment or implementation conclusions.

## Boundaries

- governance and control files only;
- no product behavior, recognizer, export, Scrub Key, reinsert, audit or UI semantic changes;
- no implementation worker may issue the governance PASS for its own candidate;
- governance may not silently repair the candidate it reviews.

## Planned evidence

- project-local governance bootstrap;
- Scrub-specific assurance contract;
- worker/project-prompt invocation rule;
- roadmap, decision-log, workpackage and changelog records;
- separate independent verification workpackage.
