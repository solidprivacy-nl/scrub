# Workpackage claim — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Status: active repair closeout  
Implementation status: `IMPLEMENTATION_REPAIR_ACTIVE`  
Role: `implementation_operations`  
Claimed: 2026-08-06 23:15 Europe/Amsterdam  
Initial candidate completed: 2026-08-07 11:21 Europe/Amsterdam  
Independent initial assurance: `FAIL` on rejected head `087379f83d8731692c96a472e5f9782fc7dabb4f`  
Repair resumed: 2026-08-07 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Parent issue: `#70`  
Assurance issue: `#74`  
Repair issue: `#75`  
Starting main SHA: `aa8a383554645bae0d14bad528d1e56729bea0c3`  
PR base/main SHA: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`  
Candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`

## Goal

Recover valid GitHub Actions post-merge evidence for exact then-current `main` without coordinator-side clicking or manual workflow execution, while preserving the Scrub implementation/assurance boundary.

## Independent FAIL and repair

The first candidate used a successful `Diagnostic recall benchmark report` job from 2026-06-17 as its rerun carrier. Independent assurance correctly rejected that design because GitHub's supported rerun window is 30 days and the handle had expired by 2026-08-07.

The repair removes dependence on historical workflow runs and adds a purpose-built read-only, no-op carrier workflow named:

```text
Issue70 exact-main evidence carrier
```

The carrier has no checkout, secrets, repository write, artifact write, deployment or product side effect. `Tests` listens narrowly for a successful carrier completion with `run_attempt > 1`, while retaining ordinary `push` on `main`, `pull_request`, `workflow_dispatch`, read-only permissions, default checkout and the exact full regression command.

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

Full regression evidence on the repaired candidate merge context:

```text
Tests run: 31216068325 / run #2115
Python regression job: 92989771650
command: python -m pytest -q tests
result: 1170 passed in 11.00s
conclusion: success
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

## Scope exclusions

No changes to recognizers, thresholds, replacement/review semantics, exports, Scrub Key, reinsert, Streamlit UI, runtime document processing, dependencies or Hugging Face product behavior.

## Remaining implementation closeout

Before fresh assurance dispatch:
- central `WORKPACKAGES.md` candidate-status entry must be present;
- central `CHANGELOG.md` candidate-status entry must be present;
- handover and implementation evidence must reflect the repaired carrier and raw current-executability proof;
- freeze the resulting exact PR #73 head.

## Execution boundary

Implementation does not issue its own assurance verdict, self-merge, claim `OUTCOME_CONFIRMED`, close #70 or start Premium Core Flow UI.

After central administration is complete, a fresh blind `governance_release_assurance` review must decide the exact final head. Only PASS authorizes merge; after merge implementation reruns the approved fresh carrier and assurance independently verifies exact-current-main `Tests` evidence before #70 may close.
