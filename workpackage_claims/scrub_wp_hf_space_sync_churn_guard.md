# Workpackage claim — SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

Status: completed and verified

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 11:36 Europe/Amsterdam

Completed at: 2026-07-17 11:45 Europe/Amsterdam

Branch: scrub-hf-space-sync-churn-guard

Dependency:
- SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY — completed and app-verified.

Evidence:
- The live Space entered an error/rebuild state during a sequence with many non-runtime-only commits.
- A sanitized runtime probe observed stage `BUILDING` on a non-product commit.
- The previous sync workflow force-pushed after every `main` commit, including governance, tests, handovers, claims and temporary operator triggers.

Scope completed:
- Added conservative `paths-ignore` filters for clearly non-runtime repository surfaces.
- Preserved synchronization for README/Hugging Face metadata, Dockerfile, dependency manifests, product Python files, startup scripts and runtime assets.
- Preserved manual workflow dispatch and existing force-push deployment semantics.
- Added source-level contract tests for included and excluded paths.

Validation:
- PR #35 merged successfully.
- A post-guard probe observed the Space at stage `RUNNING`.
- The coordinator confirmed that the application opens again.
- No product code, privacy behavior, hardware or Hugging Face configuration changed.

Handover:
- `handover/workpackages/20260717_1145_hf_space_sync_churn_guard.md`

Next step:
- Resume the Phase 6 document-fidelity package after incident closeout.
