# Workpackage claim — SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 11:36 Europe/Amsterdam

Branch: scrub-hf-space-sync-churn-guard

Dependency:
- SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY — active incident response.

Evidence:
- The live Space was reported in error.
- A sanitized runtime probe observed stage `BUILDING` on GitHub commit `9f72fed7ca6e628ed5160003e0874ffaa7a22c21`.
- The current sync workflow force-pushes to Hugging Face after every `main` commit, including governance, tests, handovers, claims and temporary operator triggers.
- The recent Phase 6 incident sequence generated many non-runtime commits and therefore unnecessary rebuild/restart churn.

Scope:
- Add conservative `paths-ignore` filters to the Hugging Face sync workflow for clearly non-runtime repository surfaces.
- Preserve synchronization whenever product/runtime files are changed in the same commit.
- Add a source-level contract test for the ignore list and its critical exclusions.

Boundaries:
- Do not ignore `README.md`, `Dockerfile`, dependency manifests, Python product files, startup scripts or runtime assets.
- No product code, privacy, recognizer, replacement, export, Scrub Key or reinsert semantic changes.
- No Hugging Face configuration or hardware change.

Next step:
- Implement and test the sync guard, merge it, allow the one final rebuild, then rerun the runtime probe without causing another Space sync.
