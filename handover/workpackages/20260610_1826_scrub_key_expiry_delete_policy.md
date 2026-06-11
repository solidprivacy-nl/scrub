# Handover — WP28 Scrub Key expiry/delete policy

Repository: `solidprivacy-nl/scrub`
Status: completed security/lifecycle-policy-only

## Summary

WP28 defines the Scrub Key expiry, retention and deletion policy after WP25-WP27. The policy keeps deletion explicit and user-controlled, treats expiry as MVP guidance-only, and makes clear that Scrub must not silently delete keys or keep hidden recovery copies.

The policy covers retention principles, matter/project retention guidance, Downloads risk, shared-computer risk, expiry guidance, manual deletion guidance, loss-of-key consequences, tampering/mismatch consequences, audit/logging expectations, MVP warnings, later secure/local desktop enforcement candidates and items that must never be deleted silently.

## Files added

- `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `handover/workpackages/20260610_1826_scrub_key_expiry_delete_policy.md`

## Files changed

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added.
- No tests changed.
- No tests run, because WP28 is documentation/security lifecycle-policy-only and no code or test files were changed.

## Validation

- Required start files read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Required context read: `SCRUB_KEY_THREAT_MODEL.md`, `SCRUB_KEY_LIFECYCLE_SPEC.md`, `SCRUB_KEY_WARNING_UX_PLAN.md`, `SCRUB_KEY_SPEC.md`, `PARALLEL_SPEC_CONSOLIDATION_WP58.md`.
- Context-only files inspected without changes: `scrub_key.py`, `scrub_key_import.py`, `scrub_key_reinsert.py`, `fix_streamlit_nested_expanders.py`.
- GitHub Actions: to be checked after final commit.
- Hugging Face sync: to be checked after final commit.
- App verification: not applicable because no UI changed.

## Main policy outcomes

- Scrub Keys should be retained only as long as needed for a specific matter, project, AI roundtrip, review or reinsert purpose.
- MVP expiry is guidance-only.
- Deletion must remain explicit and user-controlled.
- Scrub must not silently delete Scrub Keys, mappings, restored output, audit context, external copies, browser Downloads files, synced copies, backups or future app-managed vault entries.
- Scrub must not keep hidden recovery copies.
- Deleting or losing a key prevents deterministic reinsert.
- Wrong, tampered or mismatched keys can restore values incorrectly or incompletely.
- Future app-managed deletion, expiry metadata, reminders, encrypted containers, local vault behavior and recovery/escrow require separate approved implementation workpackages.

## Intentionally not changed

- No UI implementation.
- No Streamlit patch changed.
- No helper logic changed.
- No automatic deletion.
- No Scrub Key schema migration.
- No encryption implementation.
- No import/export behavior changed.
- No reinsert behavior changed.
- No tests added or changed.
- No dependencies changed.
- No secrets or real data added.
- No cloud processing added.

## Remaining risks

- Warning UX has not yet been implemented.
- No secure import/export regression tests exist yet for the Scrub Key safety expectations.
- No automatic or app-managed lifecycle tooling exists.
- No protected local storage, encrypted key container, integrity protection, vault integration or approved recovery model exists.
- Browser Downloads, shared-computer use, cloud sync and backups remain user-managed risks.

## Next recommended step

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if UI planning should precede tests: `WP28B — Scrub Key warning implementation planning`.
