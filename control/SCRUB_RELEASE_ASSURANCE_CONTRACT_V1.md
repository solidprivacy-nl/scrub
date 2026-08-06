# SolidPrivacy Scrub — Release Assurance Contract V1

## Status

```text
contract_id=SCRUB_RELEASE_ASSURANCE_CONTRACT_V1
version=1.0.0
standard_id=CROSS_PROJECT_TWO_ROLE_GOVERNANCE_V1
project_repository=solidprivacy-nl/scrub
status=ENFORCED
```

## Purpose

Prevent privacy-sensitive implementation work from certifying its own completion and keep implementation conclusions out of the assurance worker's initial judgment.

## Consequential candidate

A candidate is consequential when it changes or claims completion for any of the following:

- recognizers, thresholds, replacement logic or human-review behavior;
- processed document bytes, filenames, MIME types or export semantics;
- Scrub Key schema, binding, lifecycle, warnings or download behavior;
- TXT/DOCX reinsert behavior;
- document hygiene, audit or residual-risk evidence;
- Streamlit product UI, runtime, dependency or deployment behavior;
- merge to `main`, GitHub Actions completion, Hugging Face synchronization or a release claim.

## Required cycle

```text
user request
→ implementation_operations
→ identifiable release candidate
→ governance_release_assurance blind reconstruction
→ PASS / FAIL / INDETERMINATE
→ authorized merge or production action
→ post-action verification
→ closeout
```

A repaired candidate receives a new candidate identity and a fresh assurance pass.

## Candidate identity

Implementation must provide, without issuing a governance conclusion:

- repository;
- base commit SHA;
- head commit SHA;
- branch and PR number when available;
- workpackage title;
- exact files added/changed;
- explicit exclusions;
- implementation test commands and raw results;
- known blockers and residual risks;
- handover path.

The implementation handover is administrative evidence, not assurance evidence.

## Blind-review input contract

Before its initial decision, assurance reconstructs the candidate without reading the implementation handover or implementation conclusions.

### Permitted initial inputs

- requested outcome and approved workpackage scope;
- authoritative project control files;
- candidate source, base/head diff and file identities;
- acceptance criteria and exclusions recorded before or independently of implementation conclusions;
- test source, workflow source and raw GitHub Actions results;
- exact Hugging Face synchronization evidence and app evidence when applicable;
- risk register and relevant architecture/specification files.

### Prohibited initial inputs

- implementation handover;
- implementation completion statement;
- implementation self-review, confidence assessment or claimed PASS;
- implementation explanation of why tests are sufficient;
- conclusions copied from the candidate PR description.

The reviewer may open the implementation handover only after recording an initial decision. It may then compare disclosure completeness and prepare closeout, but may not retroactively replace the initial independent reasoning.

## Assurance decisions

```text
PASS
FAIL
INDETERMINATE
```

`PASS` requires all applicable acceptance criteria and evidence. Missing, stale or contradictory evidence is `FAIL` or `INDETERMINATE`, never an inferred pass.

Assurance may not modify the candidate under review. A required fix returns to implementation.

## Minimum privacy-sensitive checks

For every applicable candidate, assurance checks independently that:

- no real personal data, secrets or tokens were introduced;
- document processing remains local unless explicitly approved otherwise;
- human review was not weakened;
- export semantics did not change outside scope;
- Scrub Key material is treated as re-identification-sensitive;
- wrong-key and malformed-key behavior remains fail-closed;
- audit evidence does not overstate anonymization or production readiness;
- synthetic fixtures preserve professional/legal meaning without real identifiers.

## Test and deployment evidence

### Before merge

- relevant focused tests;
- full repository test workflow where required by the workpackage;
- frontend/runtime checks when affected;
- exact candidate SHA associated with the evidence.

### After merge

- GitHub Actions on the merged SHA;
- GitHub-to-Hugging-Face sync evidence for the same SHA when runtime files changed;
- app verification when UI behavior changed;
- no app verification claim for test/documentation-only work.

A successful workflow invocation is not itself a confirmed deployment outcome. A sync action and the target-space file identity/health check are separate evidence.

## Status mapping

Implementation statuses:

```text
IMPLEMENTATION_IN_PROGRESS
IMPLEMENTATION_BLOCKED
RELEASE_CANDIDATE_READY
```

Assurance and closeout statuses:

```text
GOVERNANCE_FAIL
GOVERNANCE_INDETERMINATE
GOVERNANCE_PASS_PRE_ACTION
ACTION_EXECUTED_UNVERIFIED
OUTCOME_CONFIRMED
```

## Workpackage pairing

Consequential implementation packages must have a separate verification package. The verification package:

- is claimed by `governance_release_assurance`;
- starts from the requested outcome and candidate identity;
- does not reuse the implementation worker's conclusions;
- records its own evidence and decision in a separate handover;
- cannot silently repair the implementation branch.

## Current enforcement maturity

The repository begins at `LEVEL_1_CHECKLIST`. Existing GitHub Actions and synchronization evidence support later promotion to `LEVEL_2_MACHINE_EVIDENCE`, but that promotion requires a dedicated structured assurance-record package rather than a documentation claim.
