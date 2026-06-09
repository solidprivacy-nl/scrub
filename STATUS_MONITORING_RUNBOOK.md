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
blocked; awaiting coordinator/user evidence
```

---

## 2. Standard verification order

After any implementation commit:

1. Identify the latest relevant commit SHA.
2. Check GitHub Actions for that commit.
3. Check GitHub to Hugging Face sync for that commit.
4. If Actions are red, fetch failing job logs before proposing a fix.
5. If Actions and sync are green and UI changed, ask for app verification.
6. If no UI changed, close with verification status `app verification not applicable`.

---

## 3. GitHub connector procedure

Where connector permissions allow, use GitHub tools to check status directly.

Recommended flow:

```text
1. Fetch current control files if needed:
   - PROJECT_PROMPT.md
   - ROADMAP.md
   - WORKPACKAGES.md
   - CHANGELOG.md

2. Determine the commit SHA from the handover or latest update.

3. Use commit/status tools if available:
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

## 4. Hugging Face sync status

The GitHub-to-Hugging-Face sync is represented by GitHub workflow/check results in this project.

Workers should look for workflow/check names like:

```text
Sync to Hugging Face Space
```

A green sync only means the repo synchronized/deployed. It does not mean app behavior is correct.

---

## 5. When to request app verification

Request app verification only after:

```text
GitHub Actions: green
Hugging Face sync: green
UI behavior changed: yes
```

Do not ask the coordinator to app-test a known failing build.

For UI work, app verification must confirm the exact user-visible behavior listed in the workpackage.

---

## 6. When to create a FIX workpackage

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

## 7. When to close out

Closeout workpackages are allowed only after evidence is clear.

For helper/spec/doc-only work:

```text
Actions/sync green or not applicable
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

## 8. Coordinator dependency boundary

Workers should not depend on the coordinator for routine status checks when connector access is sufficient.

Workers still need coordinator/user input for:

- explicit approval of gated workpackages;
- app verification after UI changes;
- screenshots when connector permissions fail;
- product/UX judgment;
- real-world pilot confirmation.
