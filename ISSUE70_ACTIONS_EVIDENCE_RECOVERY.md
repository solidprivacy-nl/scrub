# Issue #70 — GitHub Actions exact-main evidence recovery

Status: `RELEASE_CANDIDATE_READY`  
Role: `implementation_operations`  
Repository: `solidprivacy-nl/scrub`

## Problem

Issue #70 has independent PASS decisions for the governance adoption and processed-text selection cross-flow regression, but closeout remains `ACTION_EXECUTED_UNVERIFIED` because the connected execution path did not create a `Tests` run on the exact post-merge `main` SHA.

The existing workflow already retained `push` on `main`, `pull_request`, `workflow_dispatch`, and the full command `python -m pytest -q tests`.

## Observed execution blocker

- Direct `workflow_dispatch` is not exposed by the connected GitHub connector.
- Local `gh` and a local GitHub token are unavailable.
- The local execution container has no GitHub network resolution.
- A connector-authenticated write to `main` created `a3c7dfe7fe172af5827c3819833bd0c7c43546d0` but no `Tests` run for that exact SHA.
- The connector does expose authenticated Actions job rerun operations.

## Narrow recovery design

`tests.yml` adds a `workflow_run` trigger for the existing artifact-only workflow:

```text
Diagnostic recall benchmark report
```

The regression job accepts that event only when the carrier completed successfully and `run_attempt > 1`. Normal carrier runs therefore do not execute the full regression job.

Known safe carrier handle:

```text
workflow run ID: 27715364089
workflow run number: 6
job ID: 81986778399
job name: Generate diagnostic recall benchmark report
prior conclusion: success
```

After independent approval and merge, `implementation_operations` can invoke the connector's job-rerun operation for job `81986778399`. The completed rerun emits `workflow_run`; GitHub defines the event SHA/ref as the latest default-branch commit/default branch, and the Tests checkout has no `ref` override. The resulting Tests run therefore targets the exact then-current `main` commit.

## Validation

Focused contract test:

```text
python -m pytest -q tests/test_issue70_actions_evidence_recovery_workflow.py
4 passed in 0.03s
```

The full test command remains unchanged:

```text
python -m pytest -q tests
```

## Exclusions

No changes to product runtime, Streamlit UI, recognizers, replacement/review semantics, exports, Scrub Key, reinsert, dependencies, document processing, or Hugging Face behavior.

## Governance boundary

This implementation worker does not self-certify or merge the workflow repair. A fresh `governance_release_assurance` decision is required before merge. After merge, implementation performs the carrier rerun and assurance independently verifies the exact-main Tests evidence before issue #70 can close.
