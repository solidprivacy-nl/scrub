# Handover — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`  
Parent assurance: `#74`  
Technical PASS / admin follow-up: `#76`  
Repair issue: `#75`  
Issue to close after post-action confirmation: `#70`

## Candidate identity

- base/main used by PR #73: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`;
- candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`;
- rejected original assurance head: `087379f83d8731692c96a472e5f9782fc7dabb4f`;
- technically assured PASS head before final disclosure corrections: `c75ea000de938f3a8589e36b0b94795dd7b49c5f`;
- this handover correction follows claim correction commit `c3dc0bb1f3c0e6628f1c68f0d660d8c735fa3bb3`;
- the PR head produced by this handover commit is the new candidate identity and must be re-read exactly by fresh blind assurance before merge.

## Independent FAIL addressed

Assurance rejected the earlier candidate because its designated carrier run/job dated 2026-06-17 had exceeded GitHub's supported 30-day rerun window. The repaired design removes that historical dependency entirely.

## Structural repair

Added a purpose-built workflow:

```text
.github/workflows/issue70-exact-main-evidence-carrier.yml
name: Issue70 exact-main evidence carrier
```

Exact carrier safety properties:
- trigger: `pull_request` only, path-scoped to the carrier/Tests/contract/specification files;
- `contents: read` only;
- no checkout;
- no secrets;
- one inert evidence-output step;
- no repository, artifact, deployment, product or external-state mutation.

`.github/workflows/tests.yml` retains:
- `push` on `main`;
- `pull_request`;
- `workflow_dispatch`;
- no `paths` / `paths-ignore` filter;
- `contents: read`;
- `actions/checkout@v4` without `ref` override;
- exact command `python -m pytest -q tests`.

It adds one `workflow_run` source, `Issue70 exact-main evidence carrier`, and the recovery path executes only when the carrier rerun completed successfully with `run_attempt > 1` and `conclusion == success`.

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

Fresh raw CI on the technically assured head:

```text
technical PASS head: c75ea000de938f3a8589e36b0b94795dd7b49c5f
carrier run: 31218707774 / run #13 / success
Tests run: 31218707788 / run #2125 / success
command: python -m pytest -q tests
result: 1170 passed in 13.06s
```

Issue #76 independently returned `PASS` on that exact technical head. Its post-decision administration check then blocked merge solely because the implementation claim and this handover were stale and this handover incorrectly said the carrier also triggered on push to `main`. No product/workflow repair was requested. This disclosure-only correction resolves those findings; because it moves the PR head, fresh exact-head blind assurance remains mandatory.

## Files added or changed

Workflow/contract scope:
- added: `.github/workflows/issue70-exact-main-evidence-carrier.yml`;
- changed: `.github/workflows/tests.yml`;
- changed: `tests/test_issue70_actions_evidence_recovery_workflow.py`;
- changed: `ISSUE70_ACTIONS_EVIDENCE_RECOVERY.md`.

Administration:
- changed: `workpackage_claims/scrub_wp_issue70_post_merge_actions_evidence_recovery.md`;
- changed: this handover;
- changed earlier in candidate: central `WORKPACKAGES.md` and `CHANGELOG.md` repaired-candidate entries.

Temporary administration patch tooling used to add the central records was removed from the candidate after successful use. `ROADMAP.md` remains unchanged because no strategy or phase-order decision changed.

## Validation contract

The focused contract test freezes the Tests YAML shape, no-op/read-only carrier properties, rerun gating, default-branch checkout semantics and unchanged full regression command. Raw GitHub evidence establishes current connector rerun eligibility/execution.

The final disclosure-only head must have fresh PR Tests evidence before assurance. The carrier workflow itself is unchanged by these disclosure corrections; the fresh reviewer must independently compare the final head to the technically passed head and decide the exact candidate rather than inheriting the prior PASS automatically.

## Post-merge execution contract

Only after fresh blind `governance_release_assurance` PASS for the final exact head:

1. merge the exact approved candidate using the expected head identity;
2. identify the approved fresh carrier run/job;
3. `implementation_operations` invokes the connected job-rerun operation; no coordinator click/manual test is permitted;
4. successful attempt >1 emits `workflow_run`;
5. a fresh `governance_release_assurance` session independently verifies the resulting `Tests` run is on exact then-current `main`, has `conclusion=success`, and raw logs contain the complete `python -m pytest -q tests` result;
6. only then promote issue #70 to `OUTCOME_CONFIRMED` and close it;
7. only then release `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`.

## Hugging Face / app verification

`NOT_APPLICABLE`. No runtime/application, dependency, UI, recognizer, review, export, Scrub Key, reinsert, document-processing or Hugging Face behavior changes.

## Governance boundary

Implementation does not self-certify, self-merge, close #70 or start Premium Core Flow UI. Any candidate-head change invalidates a frozen assurance dispatch and requires a fresh exact-head decision.

## Exact next step

Treat the PR head created by this handover commit as the frozen candidate only after its PR Tests complete successfully. Then dispatch a fresh blind `governance_release_assurance` review for that exact head. No further implementation change is authorized unless that reviewer returns `FAIL` or `INDETERMINATE` with a concrete finding.