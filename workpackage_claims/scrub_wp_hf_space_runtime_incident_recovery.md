# Workpackage claim — SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

Status: completed and app-verified

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 11:23 Europe/Amsterdam

Completed at: 2026-07-17 11:45 Europe/Amsterdam

Branch: scrub-hf-space-runtime-incident-recovery

Incident:
- The live Hugging Face Space reported: `Your space is in error, check its status on hf.co`.
- The latest merged Phase 6 packages had not changed deployed product code, so the incident was treated as a build/runtime problem rather than an assumed product regression.

Scope:
- Query Hugging Face Space runtime stage and sanitized build/run logs using the existing secret.
- Attempt controlled recovery without changing privacy, recognizer, replacement, Scrub Key, export or reinsert semantics.
- Capture runtime evidence and obtain live application verification.

Recovery result:
- The first short probe observed stage `BUILDING`.
- A subsequent probe observed stage `RUNNING` on `cpu-basic`.
- Sanitized run logs showed Streamlit listening on port 7860 and the Flair model loading.
- The coordinator confirmed that the application opens again.
- No product rollback or product-code change was required.
- No secret value or personal data was stored.

Handover:
- `handover/workpackages/20260717_1145_hf_space_runtime_incident_recovery.md`

Next step:
- Retain the permanent sync-churn guard and remove temporary recovery/probe tooling.
