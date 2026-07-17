# Workpackage claim — SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 11:23 Europe/Amsterdam

Branch: scrub-hf-space-runtime-incident-recovery

Incident:
- The live Hugging Face Space reports: `Your space is in error, check its status on hf.co`.
- The latest merged Phase 6 packages did not change deployed app code; current suspicion is a failed rebuild or runtime startup rather than a confirmed product regression.

Scope:
- Query Hugging Face Space runtime stage and build/run logs using the existing `HF_TOKEN` secret.
- Attempt one normal restart and, only if still not running, one factory reboot.
- Capture before/after runtime state and logs as GitHub evidence.
- Restore the live Space without changing privacy, recognizer, replacement, Scrub Key, export or reinsert semantics.

Boundaries:
- No product feature work.
- No real personal data.
- No secret values written to logs or repository files.
- No rollback of GitHub source unless the logs prove a source regression.
- No destructive changes to Space data or configuration beyond restart/factory reboot.

Next step:
- Add a temporary, self-contained incident workflow, merge it, trigger recovery, inspect evidence and apply only the narrow fix supported by logs.
