# SolidPrivacy Scrub — Project Governance Bootstrap

```text
standard_id=CROSS_PROJECT_TWO_ROLE_GOVERNANCE_V1
canonical_standard_location=https://github.com/market-predictions/control-plane/blob/main/control/CROSS_PROJECT_TWO_ROLE_GOVERNANCE_STANDARD_V1.md
canonical_location_status=CANONICAL_ACTIVE
project_repository=solidprivacy-nl/scrub
project_risk_class=privacy_sensitive_document_scrubbing_and_reidentification
adoption_status=enforced_for_consequential_work
enforcement_maturity=LEVEL_1_CHECKLIST
target_enforcement_maturity=LEVEL_2_MACHINE_EVIDENCE
implementation_role=implementation_operations
assurance_role=governance_release_assurance
project_specific_assurance_contract=control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md
project_specific_assurance_contract_status=ENFORCED
production_action=merge_to_main_and_github_to_huggingface_deployment
post_action_confirmation=github_actions_plus_exact_huggingface_sync_plus_app_verification_when_ui_changed
blind_review_mode=source_acceptance_criteria_and_machine_evidence_only_before_initial_decision
implementation_handover_visibility=after_initial_assurance_decision
```

## User interface

The user gives one Scrub instruction and receives one consolidated project status. The user does not separately coordinate implementation and assurance.

## Role boundary

`implementation_operations` prepares an identifiable release candidate and implementation evidence. It may report only:

```text
IMPLEMENTATION_IN_PROGRESS
IMPLEMENTATION_BLOCKED
RELEASE_CANDIDATE_READY
```

`governance_release_assurance` independently reconstructs the candidate from authoritative source, acceptance criteria and machine evidence. It may report only:

```text
PASS
FAIL
INDETERMINATE
```

Implementation may not certify its own candidate. Assurance may not silently repair the candidate it reviews. Any repair returns to implementation and requires a new assurance pass.

## Blind-review boundary

Before recording its initial `PASS`, `FAIL` or `INDETERMINATE`, the assurance worker must not read or rely on:

- the implementation handover;
- implementation self-assessment or completion claim;
- implementation conclusions;
- a narrative summary of what the implementation worker believes it changed.

The assurance worker may and must read:

- the user's requested outcome;
- `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `RISK_REGISTER.md`, `DECISION_LOG.md` and this bootstrap;
- the candidate source and diff;
- acceptance criteria and explicit exclusions;
- test code, workflow definitions and raw machine results;
- deployment/sync evidence and target-system evidence where applicable.

After the initial assurance decision is recorded, the implementation handover may be opened only to compare administrative completeness, identify undisclosed scope or prepare the consolidated closeout.

## Trigger rule

Use the two-role cycle for:

- privacy, Scrub Key, reinsert, export, audit, recognizer or document-hygiene changes;
- production-facing UI or runtime changes;
- merges to `main`, releases and Hugging Face deployment claims;
- any claim that work is complete, verified, deployed, synchronized or ready for release.

Low-risk exploration and disposable planning may use a lighter review only when explicitly recorded.

## Session read rule

For consequential work, read this file after the mandatory first sequence:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Then read `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md` and the minimum relevant execution files.

## Prompt invocation

Operational workpackage prompts should invoke this rule rather than copy it:

```text
Apply the project's implementation-versus-release-assurance separation and blind-review boundary. Treat all generated output as a release candidate until independent assurance passes. Do not let implementation certify its own completion. Report action execution separately from independently confirmed outcome.
```
