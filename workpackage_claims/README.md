# Workpackage claim protocol

This directory prevents duplicate parallel work on the same workpackage.

Before starting a workpackage, a worker must check this directory.

If a claim file for the same workpackage exists:

- `in_progress`: stop and report that the package is already claimed.
- `completed`: stop and report that the package is already done.
- `blocked`: stop and read the blocking reason.
- `abandoned`: continue only with coordinator approval.

If no claim exists, create a new claim file before making code, test, UI, export, schema or shared documentation changes.

Create the claim as a new GitHub file. Do not silently overwrite an existing claim. This makes the claim step a lightweight lock: if two workers try to claim the same package, only one new-file creation should succeed.

File format:

```text
workpackage_claims/WPXX_short_slug.md
```

Minimum status values:

```text
in_progress
completed
blocked
abandoned
```

When a worker finishes, update the same claim file to `completed` and add the final commit or PR, handover path, tests/checks, remaining risks and next step.

Do not override stale claims silently. Ask the coordinator to mark stale work as `abandoned` first.
