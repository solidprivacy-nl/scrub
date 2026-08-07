# Handover — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`  
Issue: `#70`

## Current-main identity

- assignment-start main: `aa8a383554645bae0d14bad528d1e56729bea0c3`;
- main after the required implementation claim commit: `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`;
- no later main change was observed before candidate closeout;
- candidate branch: `wp/issue70-post-merge-actions-evidence-recovery`;
- implementation head before this administrative handover commit: `e3f6e102dc5e5e296862986bc0d27813794a26d8`.

The pull-request head is authoritative after this handover commit and must be re-read by assurance.

## Problem diagnosis

The existing `Tests` workflow was already active and declared:

- `push` on `main`;
- `pull_request`;
- `workflow_dispatch`;
- full test command `python -m pytest -q tests`.

Direct dispatch could not be executed because:

- the connected GitHub connector exposes no workflow-dispatch operation;
- local `gh` is unavailable;
- no local GitHub token is available;
- the local execution container cannot resolve `github.com` for a full checkout.

A connector-authenticated write to `main` created commit `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`, but querying `tests.yml` runs for that exact SHA returned zero runs. This reproduces the evidence gap without requiring coordinator action.

## Repair method

Added a narrow `workflow_run` trigger to `.github/workflows/tests.yml` using the existing safe carrier workflow:

```text
Diagnostic recall benchmark report
```

The Tests job accepts that trigger only when:

```text
workflow_run.run_attempt > 1
workflow_run.conclusion == success
```

Normal push, pull-request and workflow-dispatch behavior remains unchanged.

The carrier is artifact-only: it checks out the repository, runs diagnostic corpus/report tests, generates a report and uploads an artifact. It does not modify repository state, product behavior or Hugging Face.

Known carrier execution handle:

- prior successful carrier run ID: `27715364089` (carrier run #6);
- carrier event: `push`;
- carrier head SHA: `732652e66c999d69486c377b1ea2e61707f49b13`;
- carrier job ID: `81986778399`;
- carrier job: `Generate diagnostic recall benchmark report`;
- prior carrier conclusion: `success`.

After this candidate is independently approved and merged, rerunning job `81986778399` through the connected GitHub Actions write operation creates carrier attempt 2. On completion, the new `workflow_run` trigger launches `.github/workflows/tests.yml`. GitHub defines `GITHUB_SHA` for `workflow_run` as the last commit on the default branch, and the Tests checkout has no ref override, so that run targets the exact then-current `main` SHA.

## Files added or changed

Candidate product/workflow scope:

- changed: `.github/workflows/tests.yml`;
- added: `tests/test_issue70_actions_evidence_recovery_workflow.py`.

Administration:

- updated: `workpackage_claims/scrub_wp_issue70_post_merge_actions_evidence_recovery.md`;
- added: `handover/workpackages/20260807_1121_issue70_post_merge_actions_evidence_recovery.md`.

Central `WORKPACKAGES.md` and `CHANGELOG.md` still require the candidate status entry before merge; no strategy/phase-order change exists, so `ROADMAP.md` must remain unchanged.

## Tests

Focused contract validation executed in the available local runtime:

```text
python -m pytest -q tests/test_issue70_actions_evidence_recovery_workflow.py
4 passed in 0.03s
```

Full checkout/full-suite validation could not be executed locally because the execution container has no GitHub network resolution. This is an environment limitation, not hidden as a pass.

The candidate preserves the exact full-suite command:

```text
python -m pytest -q tests
```

## GitHub Actions status

- exact-current-main Tests run: not yet produced; candidate must first receive independent assurance and be merged;
- direct `workflow_dispatch`: unavailable in this connector surface;
- connector-authenticated main push reproduction: no Tests run for `a3c7dfe7fe172af5827c3819833bd0c7c43546d0`;
- recovery mechanism after authorized merge: rerun carrier job `81986778399`, then inspect the resulting `workflow_run`-triggered Tests run;
- required final evidence remains: workflow `.github/workflows/tests.yml`, ref `main`, exact current-main `head_sha`, conclusion `success`, command `python -m pytest -q tests`.

## Hugging Face sync status

`NOT_APPLICABLE` for this candidate. No runtime/application path, dependency, Dockerfile or deployment semantics are changed.

## App verification status

`NOT_APPLICABLE`. No visible UI or runtime Scrub behavior is changed.

## Explicit exclusions

No changes to:

- recognizers;
- replacement logic;
- review semantics;
- export bytes, filenames or MIME types;
- Scrub Key behavior;
- reinsert behavior;
- Streamlit UI;
- runtime document processing;
- Hugging Face application behavior.

## Remaining risks

1. The workflow repair itself has not yet been independently assured; implementation must not self-certify it.
2. The exact-current-main Tests run can only be generated after authorized merge because `workflow_run` workflows must exist on the default branch.
3. Central `WORKPACKAGES.md` and `CHANGELOG.md` candidate-status entries remain to be added before final assurance/merge.
4. `OUTCOME_CONFIRMED` remains prohibited until the separate assurance worker verifies the resulting exact-main run.

## Exact next step for `governance_release_assurance`

1. Re-read the final PR base SHA, head SHA and changed files.
2. Independently inspect the `workflow_run` recovery trigger, its `run_attempt > 1` and `success` gates, the no-ref checkout, and the contract test.
3. Confirm that the carrier workflow is artifact-only and that rerunning job `81986778399` is a safe trigger action.
4. Issue a fresh decision for this repair candidate without changing it.
5. Only on independent PASS may the authorized merge occur.
6. After merge, `implementation_operations` reruns job `81986778399` through the connector; no coordinator click is required.
7. Independently verify the resulting Tests run has exact current-main `head_sha`, ref `main`, conclusion `success`, and raw `python -m pytest -q tests` result.
8. Only then may issue #70 be closed and the premium UI contract gate be released.
