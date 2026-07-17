# Handover — SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_HF_SPACE_RUNTIME_INCIDENT_RECOVERY

## Status

Completed and app-verified.

## Files added

- `workpackage_claims/scrub_wp_hf_space_runtime_incident_recovery.md`

## Files changed

- No product files changed.

## Tests

- Sanitized Hugging Face runtime and log probes.
- Runtime-stage verification.
- Coordinator live application verification.

## Validation status

- Runtime stage: `RUNNING`.
- Hardware: `cpu-basic`.
- Streamlit startup visible in the sanitized run log.
- Flair model load visible in the sanitized run log.
- Coordinator confirmed that the application opens again.

## GitHub Actions status

Temporary recovery/probe workflows executed sufficiently to establish recovery. No product test regression was introduced.

## Hugging Face sync status

Recovered and running.

## App verification status

Passed at 2026-07-17 11:44 Europe/Amsterdam.

## Remaining risks

- Long Docker/model rebuilds can temporarily present as an unavailable Space.
- Hosted infrastructure and dependency downloads remain external risks.

## Next recommended step

Close temporary incident tooling and retain the sync-churn guard.
