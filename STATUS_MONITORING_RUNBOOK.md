# SolidPrivacy Scrub — Status Monitoring Runbook

Purpose:

```text
Reduce dependence on coordinator screenshots by making GitHub Actions and Hugging Face sync status checks part of the worker workflow.
```

This runbook does not replace app verification. UI behavior still requires coordinator/user verification in the Hugging Face app after Actions and sync are green.

---

## 1. Status states

Use these status states consistently in `WORKPACKAGES.md`, `CHANGELOG.md` and handovers.

```text
implemented; awaiting GitHub Actions and Hugging Face sync
implemented; GitHub Actions failing; fix required
implemented; Actions/sync verified; awaiting app verification
completed after Actions/sync verification; app verification not applicable
completed and app-verified after Actions/sync verification
completed; Actions not required / not run to preserve credits; app verification not applicable
blocked; awaiting coordinator/user evidence
```

---

## 2. Budget-aware validation

Validation must be risk-driven and mindful of GitHub Actions/Codespaces credit usage.

Use Actions deliberately, not as the first debugging loop.

Prefer this order:

```text
1. Static inspection and scope check.
2. Targeted checks or targeted tests for touched files.
3. Related regression tests when the touched flow is sensitive.
4. One deliberate CI run when the change is ready for merge/release validation.
```

Do not ask the coordinator to run local tests, Codespaces or Codex validation as a fallback.

### When to use Actions

Use Actions when:

```text
product behavior changed
UI/export/reinsert/Scrub Key/runtime/recognizer/document processing changed
full-suite or release-level confidence is needed
PR/merge validation is required
```

### When Actions are not required

Actions are normally not required for:

```text
documentation-only work
specification-only work
closeout-only work with no code/test/runtime changes
repository governance text updates
```

For these packages, report:

```text
GitHub Actions: not required / not run to preserve credits
Hugging Face sync: not applicable unless automation triggers it
App verification: not applicable
```

### Avoiding repeated CI cycles

Workers should avoid repeated push/PR cycles for small iteration fixes. Batch fixes before requesting CI. Do not use red Actions as a routine syntax or documentation checker.

### Targeted checks versus CI

Targeted checks are local or repository-level checks for the files/flow touched by the package. CI is repository-level validation through GitHub Actions. A handover must distinguish clearly between these two.

---

## 3. Standard verification order

After an implementation commit, and only where Actions/sync validation is required or triggered:

1. Identify the latest relevant commit SHA.
2. Check GitHub Actions for that commit.
3. Check GitHub to Hugging Face sync for that commit.
4. If Actions are red, fetch failing job logs before proposing a fix.
5. If Actions and sync are green and UI changed, ask for app verification.
6. If no UI changed, close with verification status `app verification not applicable`.

For documentation-only or governance-only work, record Actions as not required unless repository automation triggered them automatically.

---

## 4. GitHub connector procedure

Where connector permissions allow, use GitHub tools to check status directly.

Recommended flow:

```text
1. Fetch current control files if needed:
   - PROJECT_PROMPT.md
   - ROADMAP.md
   - WORKPACKAGES.md
   - CHANGELOG.md

2. Determine the commit SHA from the handover or latest update.

3. Use commit/status tools if available and proportionate:
   - get_commit_combined_status
   - fetch_commit_workflow_runs
   - fetch_workflow_run_jobs
   - fetch_workflow_job_logs

4. If a workflow run is red:
   - fetch jobs for the workflow run;
   - identify failed job ID;
   - fetch job logs;
   - quote the failing assertion/error in the next workpackage or fix handover.
```

If a connector cannot list the relevant workflow runs, state that clearly and ask the coordinator for the missing run/job link or screenshot.

---

## 5. Hugging Face sync status

The GitHub-to-Hugging-Face sync is represented by GitHub workflow/check results in this project.

Workers should look for workflow/check names like:

```text
Sync to Hugging Face Space
```

A green sync only means the repo synchronized/deployed. It does not mean app behavior is correct.

For branch-only documentation work, Hugging Face sync is not applicable unless the branch is merged to `main` or repository automation triggers sync.

---

## 6. When to request app verification

Request app verification only after:

```text
GitHub Actions: green
Hugging Face sync: green
UI behavior changed: yes
```

Do not ask the coordinator to app-test a known failing build.

For UI work, app verification must confirm the exact user-visible behavior listed in the workpackage.

Documentation-only, governance-only, helper-only without UI and closeout-only packages normally do not require app verification.

---

## 7. When to create a FIX workpackage

Create a FIX workpackage when:

```text
Implementation exists
GitHub Actions are red
The cause is not a transient external outage
```

FIX scope should be narrow:

- read failing logs;
- fix only the failing behavior/tests/config;
- do not add new product scope;
- preserve all original boundaries;
- update `WORKPACKAGES.md`, `CHANGELOG.md` and handover.

---

## 8. When to close out

Closeout workpackages are allowed only after evidence is clear.

For helper/spec/doc-only work:

```text
Actions/sync green or not applicable/not required
App verification not applicable
```

For UI work:

```text
Actions green
Sync green
App verification confirmed by coordinator/user
```

Closeout-only packages must not change code, tests, dependencies or UI.

---

## 9. Coordinator dependency boundary

Workers should not depend on the coordinator for routine status checks when connector access is sufficient.

Workers still need coordinator/user input for:

- explicit approval of gated workpackages;
- app verification after UI changes;
- screenshots when connector permissions fail;
- product/UX judgment;
- real-world pilot confirmation.

The coordinator is not expected to run local validation, Codespaces or Codex as a workaround for routine worker validation.
