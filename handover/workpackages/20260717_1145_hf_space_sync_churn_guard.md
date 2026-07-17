# Handover — SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_HF_SPACE_SYNC_CHURN_GUARD

## Status

Completed and verified.

## Files added

- `tests/test_hf_space_sync_churn_guard.py`
- `workpackage_claims/scrub_wp_hf_space_sync_churn_guard.md`

## Files changed

- `.github/workflows/sync-to-huggingface.yml`

## Tests

- Source-level contracts verify clearly non-runtime ignore paths.
- Contracts verify runtime-critical files are not ignored.
- Existing force-push and manual-dispatch deployment behavior remains present.

## Validation status

The guard is merged. A post-guard runtime probe observed `RUNNING`, and the coordinator confirmed that the app opens.

## GitHub Actions status

PR #35 merged successfully.

## Hugging Face sync status

Running; unnecessary deployments from clearly non-runtime-only commits are suppressed.

## App verification status

Passed at 2026-07-17 11:44 Europe/Amsterdam.

## Remaining risks

- Any commit containing a runtime-relevant file still correctly rebuilds the Space.
- Hugging Face infrastructure and dependency-download failures remain external risks.

## Next recommended step

Resume the Phase 6 document-fidelity package.
