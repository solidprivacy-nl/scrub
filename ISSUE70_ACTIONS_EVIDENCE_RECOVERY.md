# Issue #70 — GitHub Actions exact-main evidence recovery

Status: `IMPLEMENTATION_REPAIR_ACTIVE`  
Role: `implementation_operations`  
Repository: `solidprivacy-nl/scrub`

## Problem

Issue #70 has independent PASS decisions for governance adoption and processed-text selection cross-flow regression, but closeout remains `ACTION_EXECUTED_UNVERIFIED` because the connected post-merge path did not create a `Tests` run on the exact current `main` SHA.

The original PR #73 candidate was rejected by independent assurance because its named carrier run from 2026-06-17 had exceeded GitHub's supported 30-day rerun window.

## Structural repair

The repaired candidate no longer depends on a historical carrier.

It adds a purpose-built workflow:

```text
Issue70 exact-main evidence carrier
```

The carrier:
- runs on `pull_request` and `push` to `main`;
- has `contents: read` only;
- checks out no repository code;
- executes one inert `printf` step;
- has no secrets, deployment, repository mutation, artifact mutation or external side effect.

`tests.yml` retains its normal `push` on `main`, `pull_request`, `workflow_dispatch`, no path filters, `contents: read`, checkout without a ref override, and the unchanged full command:

```text
python -m pytest -q tests
```

It adds a narrow `workflow_run` recovery trigger for `Issue70 exact-main evidence carrier`. The regression job accepts that event only when the carrier completed successfully and `run_attempt > 1`.

## Live executable evidence

Repaired candidate head validated in GitHub:

```text
candidate head: 5a415059d879f556fddc5618ed5cf2f9ea4766cd
carrier workflow run: 31216068355 / run #3
initial carrier conclusion: success
initial carrier job: 92989771464
connector rerun invocation: success
rerun attempt: 2
rerun carrier job: 92989859101
rerun carrier conclusion: success
```

This demonstrates that the chosen recovery handle is executable now through the connected GitHub job-rerun operation; no coordinator/manual GitHub step is required.

The full PR regression workflow also passed on the repaired candidate merge context:

```text
Tests run: 31216068325 / run #2115
Python regression job: 92989771650
command: python -m pytest -q tests
result: 1170 passed in 11.00s
conclusion: success
```

## Post-merge execution contract

After a fresh independent PASS and authorized merge:

1. `implementation_operations` identifies the carrier run/job created for the approved merge/main state.
2. Control invokes the connector-authenticated job-rerun operation; no coordinator click is permitted.
3. The successful rerun emits `workflow_run` with `run_attempt > 1`.
4. GitHub executes `Tests` from the default-branch workflow; checkout has no `ref` override, so the resulting run targets then-current `main`.
5. `governance_release_assurance` independently verifies the exact-main SHA, success conclusion and raw `python -m pytest -q tests` result before issue #70 may close.

## Contract coverage

`tests/test_issue70_actions_evidence_recovery_workflow.py` freezes:
- normal push/PR/manual Tests triggers;
- narrow carrier workflow identity;
- successful rerun-only condition;
- read-only permissions;
- default-branch checkout without ref override;
- unchanged full regression command;
- absence of schedule/comment recovery triggers;
- carrier no-op/read-only safety characteristics.

## Exclusions

No changes to product runtime, Streamlit UI, recognizers, replacement/review semantics, exports, Scrub Key, reinsert, dependencies, document processing, or Hugging Face behavior.

## Governance boundary

Implementation does not self-certify, self-merge, close issue #70 or start Premium Core Flow UI. Any final candidate-head change requires fresh exact-head blind `governance_release_assurance`. The remaining implementation closeout is administrative: central `WORKPACKAGES.md` and `CHANGELOG.md` candidate-status entries plus updated handoff/claim must be complete before fresh assurance dispatch.
