# Workpackage claim — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Status: completed  
Implementation status: `RELEASE_CANDIDATE_READY`  
Role: `implementation_operations`  
Claimed: 2026-08-06 23:15 Europe/Amsterdam  
Completed: 2026-08-07 11:21 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Issue: `#70`  
Starting main SHA: `aa8a383554645bae0d14bad528d1e56729bea0c3`  
Main after required claim commit: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`  
Candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`  
Implementation head before administrative closeout: `2695e5501435f9a457ac6e7d314df7b6669a39eb`

## Goal

Recover valid GitHub Actions post-merge evidence for the exact current `main` commit without coordinator-side clicking or manual workflow execution.

## Diagnosis

- `.github/workflows/tests.yml` is active and retains `push` on `main`, `pull_request` and `workflow_dispatch`.
- Direct dispatch is not exposed by the connected GitHub connector.
- Local `gh`, a local GitHub token and a network-capable checkout are unavailable in this worker environment.
- A connector-authenticated write to `main` created commit `a3c7dfe7fe172af5827c3819833bd0c7c43546d0` but created no `Tests` run, reproducing the post-action evidence gap.
- The connector does expose authenticated Actions job rerun operations.

## Repair candidate

The candidate adds a narrow `workflow_run` recovery trigger to `Tests` for the existing artifact-only workflow `Diagnostic recall benchmark report`.

The `Tests` job runs from that trigger only when:

- the carrier workflow completed successfully; and
- its `run_attempt` is greater than 1, so ordinary carrier runs do not execute the regression job.

GitHub documents `workflow_run` with `GITHUB_SHA` equal to the last commit on the default branch. `actions/checkout@v4` has no ref override, so the recovery run checks out the exact then-current `main` commit.

Known safe carrier evidence:

- workflow: `Diagnostic recall benchmark report`;
- prior successful run ID: `27715364089` (run #6);
- job ID: `81986778399`;
- job: `Generate diagnostic recall benchmark report`;
- carrier is artifact-only and does not modify repository or product state.

After independent assurance and merge, `implementation_operations` can rerun job `81986778399` through the connector. The completed rerun then causes `.github/workflows/tests.yml` to run against exact current `main` without coordinator action.

## Validation

Focused workflow contract test:

```text
python -m pytest -q tests/test_issue70_actions_evidence_recovery_workflow.py
4 passed in 0.03s
```

A full local checkout is unavailable because the execution container cannot resolve `github.com`; this limitation is recorded rather than hidden. The unchanged product test command in the workflow remains:

```text
python -m pytest -q tests
```

## Scope exclusions

No changes to:

- recognizers or thresholds;
- replacement or review semantics;
- export bytes, filenames or MIME types;
- Scrub Key behavior;
- reinsert behavior;
- Streamlit UI;
- runtime document processing;
- Hugging Face application behavior.

## Execution boundary

This worker does not issue an assurance verdict, does not merge its own workflow candidate, does not claim `OUTCOME_CONFIRMED`, and does not close issue #70.

Next step: a fresh `governance_release_assurance` pass must inspect the exact PR candidate. If it passes and is merged, rerun carrier job `81986778399`, then independently verify the resulting exact-current-main `Tests` run and close issue #70.