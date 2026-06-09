# Handover — WP18C Add Codex worker governance instructions

Repository: solidprivacy-nl/scrub  
Status: completed documentation/governance-only

## Summary

Added repository-level `AGENTS.md` instructions for Codex/agent workers and updated the active workpackage process so Codex workers write full handovers to the repository while the coordinator chat only receives the handover path, commit/PR, status and short summary.

This prepares safe parallel execution of WP19, WP25, WP30 and WP35.

## Files added

- `AGENTS.md`
- `handover/workpackages/20260609_1330_codex_worker_governance.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Not run; documentation/governance-only change.
- No tests were added or changed.

## Validation

- GitHub Actions: not checked; documentation/governance-only change.
- Hugging Face sync: not checked; documentation/governance-only change.
- App verification: not applicable.

## Notes / risks

- No code, UI, tests, dependencies, Docker/runtime behavior or product behavior were changed.
- Parallel Codex workers may still conflict on shared documentation files. `AGENTS.md` now instructs workers to fetch latest files before editing and stop on conflict.
- Full handover copy-paste into the coordinator chat is no longer required when the handover is committed to GitHub.

## Next recommended step

- Start four safe parallel Codex workpackages: WP19, WP25, WP30 and WP35.
- After those complete, run `WP58 — Parallel specification consolidation and next execution queue`.
