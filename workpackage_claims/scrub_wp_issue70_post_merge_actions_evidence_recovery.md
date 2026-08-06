# Workpackage claim — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Status: in_progress  
Role: `implementation_operations`  
Claimed: 2026-08-06 23:15 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Issue: `#70`  
Starting main SHA: `aa8a383554645bae0d14bad528d1e56729bea0c3`

## Goal

Recover valid GitHub Actions post-merge evidence for the exact current `main` commit without coordinator-side clicking or manual workflow execution.

## Scope

- attempt direct workflow dispatch through available authenticated mechanisms;
- diagnose the exact blocker where direct dispatch is unavailable;
- use only narrowly necessary governance/status administration when an authenticated push is required to obtain an exact-main run;
- preserve production code, UI, recognizers, replacement, export, Scrub Key, reinsert and Hugging Face behavior.

## Current diagnosis

- `.github/workflows/tests.yml` is active and already declares `push` on `main`, `pull_request` and `workflow_dispatch`;
- local `gh` is unavailable;
- no local GitHub token or checkout is available;
- the connected GitHub App has Actions/workflow write permissions, but the connector exposes no workflow-dispatch operation;
- direct repository Actions-permission inspection is denied to the integration (`403 Resource not accessible by integration`).

## Execution boundary

This worker does not issue an assurance verdict and does not close issue #70. Successful evidence is handed back to `governance_release_assurance` for independent confirmation.
