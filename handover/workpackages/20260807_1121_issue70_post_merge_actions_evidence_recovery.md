# Handover — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY`  
Role: `implementation_operations`  
Status: `IMPLEMENTATION_REPAIR_ACTIVE`  
Parent assurance: `#74`  
Repair issue: `#75`  
Issue to close after post-action confirmation: `#70`

## Candidate identity

- base/main used by PR #73: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`;
- candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`;
- rejected assurance head: `087379f83d8731692c96a472e5f9782fc7dabb4f`;
- repaired implementation head is moving while administration is completed; assurance must freeze and re-read the final PR head before review.

## Independent FAIL addressed

Assurance rejected the earlier candidate because its designated carrier run/job dated 2026-06-17 had exceeded GitHub's supported 30-day rerun window. The repaired design removes that historical dependency entirely.

## Structural repair

Added a purpose-built workflow:

```text
.github/workflows/issue70-exact-main-evidence-carrier.yml
name: Issue70 exact-main evidence carrier
```

Safety properties:
- triggers only on PR and push to `main`;
- `contents: read` only;
- no checkout;
- no secrets;
- one inert `printf` step;
- no repository, artifact, deployment, product or external-state mutation.

`.github/workflows/tests.yml` retains:
- `push` on `main`;
- `pull_request`;
- `workflow_dispatch`;
- no `paths` / `paths-ignore` filter;
- `contents: read`;
- `actions/checkout@v4` without `ref` override;
- exact command `python -m pytest -q tests`.

It adds one `workflow_run` source, `Issue70 exact-main evidence carrier`, and the recovery path executes only when the carrier rerun completed successfully with `run_attempt > 1`.

## Live executable evidence

The repaired mechanism was exercised through the connected GitHub Actions write surface, without a coordinator/manual GitHub step:

```text
candidate head exercised: 5a415059d879f556fddc5618ed5cf2f9ea4766cd
carrier run: 31216068355 / run #3
initial carrier job: 92989771464
initial conclusion: success
connector job-rerun invocation: success
rerun attempt: 2
rerun carrier job: 92989859101
rerun conclusion: success
```

This closes the implementation defect identified by #74/#75: the selected carrier mechanism is demonstrably rerunnable now, rather than merely encoded in YAML.

Full PR regression evidence on that repaired candidate merge context:

```text
Tests run: 31216068325 / run #2115
job: 92989771650
command: python -m pytest -q tests
result: 1170 passed in 11.00s
conclusion: success
```

Because subsequent documentation/admin commits move the PR head, fresh assurance must use the final exact head and its corresponding current PR checks; the evidence above establishes the live rerun capability and full-suite behavior of the repaired mechanism.

## Files added or changed

Workflow/contract scope:
- added: `.github/workflows/issue70-exact-main-evidence-carrier.yml`;
- changed: `.github/workflows/tests.yml`;
- changed: `tests/test_issue70_actions_evidence_recovery_workflow.py`;
- changed: `ISSUE70_ACTIONS_EVIDENCE_RECOVERY.md`.

Administration:
- changed: `workpackage_claims/scrub_wp_issue70_post_merge_actions_evidence_recovery.md`;
- changed: this handover;
- required before assurance dispatch: central `WORKPACKAGES.md` and `CHANGELOG.md` candidate-status entries.

`ROADMAP.md` remains unchanged because no strategy or phase-order decision changed.

## Validation contract

The focused contract test now freezes not only the Tests YAML shape but the no-op/read-only carrier properties and unchanged full regression command. Raw GitHub evidence above proves current connector rerun eligibility/execution.

## Post-merge execution contract

Only after fresh blind `governance_release_assurance` PASS for the final exact head:

1. merge the exact approved candidate;
2. identify the carrier run/job associated with the approved main state;
3. `implementation_operations` invokes the connected job-rerun operation; no coordinator click/manual test is permitted;
4. successful attempt >1 emits `workflow_run`;
5. `governance_release_assurance` independently verifies the resulting `Tests` run is on exact then-current `main`, has `conclusion=success`, and raw logs contain the complete `python -m pytest -q tests` result;
6. only then promote issue #70 to `OUTCOME_CONFIRMED` and close it;
7. only then release `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`.

## Hugging Face / app verification

`NOT_APPLICABLE`. No runtime/application, dependency, UI, recognizer, review, export, Scrub Key, reinsert, document-processing or Hugging Face behavior changes.

## Governance boundary

Implementation does not self-certify, self-merge, close #70 or start Premium Core Flow UI. Any candidate-head change invalidates a frozen assurance dispatch and requires a fresh exact-head decision.

## Exact next step

Complete the central `WORKPACKAGES.md` and `CHANGELOG.md` candidate-status records, freeze the resulting PR #73 head, then dispatch a fresh blind `governance_release_assurance` review under the #74/#75 boundary using the repaired live evidence above.
