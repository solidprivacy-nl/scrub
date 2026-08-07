# Workpackage claim — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Status: completed candidate closeout  
Implementation status: `RELEASE_CANDIDATE_READY`  
Role: `implementation_operations`  
Claimed: 2026-08-06 23:15 Europe/Amsterdam  
Initial candidate completed: 2026-08-07 11:21 Europe/Amsterdam  
Independent initial assurance: `FAIL` on rejected head `087379f83d8731692c96a472e5f9782fc7dabb4f`  
Repaired technical candidate blind assurance: `PASS` on head `c75ea000de938f3a8589e36b0b94795dd7b49c5f`, followed by an administrative-completeness block requiring this disclosure-only correction  
Repository: `solidprivacy-nl/scrub`  
Parent issue: `#70`  
Prior assurance issues: `#74`, `#76`  
Repair issue: `#75`  
Starting main SHA: `aa8a383554645bae0d14bad528d1e56729bea0c3`  
PR base/main SHA: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`  
Candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`  
Technical PASS head before this disclosure correction: `c75ea000de938f3a8589e36b0b94795dd7b49c5f`

## Goal

Recover valid GitHub Actions post-merge evidence for exact then-current `main` without coordinator-side clicking or manual workflow execution, while preserving the Scrub implementation/assurance boundary.

## Independent FAIL and repair

The first candidate used a successful `Diagnostic recall benchmark report` job from 2026-06-17 as its rerun carrier. Independent assurance correctly rejected that design because GitHub's supported rerun window is 30 days and the handle had expired by 2026-08-07.

The repair removes dependence on historical workflow runs and adds a purpose-built read-only, no-op carrier workflow named:

```text
Issue70 exact-main evidence carrier
```

The exact candidate carrier is `pull_request`-triggered and path-scoped, has `contents: read`, no checkout, no secrets, no repository or artifact write, no deployment and no product side effect. `Tests` listens narrowly for a successful carrier completion with `run_attempt > 1`, while retaining ordinary `push` on `main`, `pull_request`, `workflow_dispatch`, read-only permissions, default checkout and the exact full regression command.

## Raw live executability evidence

The repaired mechanism was exercised through the connected GitHub Actions job-rerun capability:

```text
candidate head exercised: 5a415059d879f556fddc5618ed5cf2f9ea4766cd
carrier workflow run: 31216068355 / run #3
initial carrier job: 92989771464
initial conclusion: success
connector job-rerun invocation: success
rerun attempt: 2
rerun carrier job: 92989859101
rerun conclusion: success
```

This is live evidence that the recovery handle is currently executable without coordinator/manual GitHub interaction.

Fresh raw evidence on the technically assured head:

```text
technical PASS head: c75ea000de938f3a8589e36b0b94795dd7b49c5f
carrier run: 31218707774 / run #13 / success
Tests run: 31218707788 / run #2125 / success
command: python -m pytest -q tests
result: 1170 passed in 13.06s
```

## Contract coverage

`tests/test_issue70_actions_evidence_recovery_workflow.py` freezes:
- unchanged normal Tests triggers and absence of path filters;
- narrow carrier workflow identity;
- successful rerun-only condition;
- read-only permissions;
- checkout without a ref override;
- unchanged full regression command;
- absence of schedule/comment recovery triggers;
- no-op/read-only carrier safety properties.

## Administration and current candidate identity

Central `WORKPACKAGES.md` and `CHANGELOG.md` contain the repaired-candidate entries required by issue #75. The recovery specification, this claim and the handover identify the repaired mechanism, raw evidence, exclusions and governance boundary.

Issue #76 independently returned technical `PASS` for exact head `c75ea000de938f3a8589e36b0b94795dd7b49c5f`, then correctly blocked merge because this claim and the handover were stale/contradictory. This commit corrects only that administrative disclosure. Because any candidate-head change invalidates the frozen assurance identity, the PR head after the final handover correction must be re-read and receive a fresh blind exact-head assurance decision before merge.

## Scope exclusions

No changes to recognizers, thresholds, replacement/review semantics, exports, Scrub Key, reinsert, Streamlit UI, runtime document processing, dependencies or Hugging Face product behavior.

## Execution boundary

Implementation does not issue its own assurance verdict, self-merge, claim `OUTCOME_CONFIRMED`, close #70 or start Premium Core Flow UI.

Next step after the final disclosure-only handover correction: freeze the resulting PR #73 head, verify its PR Tests result, and dispatch a fresh blind `governance_release_assurance` review. Only PASS authorizes merge; after merge implementation reruns the approved fresh carrier and assurance independently verifies exact-current-main `Tests` evidence before #70 may close.