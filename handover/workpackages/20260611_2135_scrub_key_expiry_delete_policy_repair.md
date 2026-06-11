# Handover — WP28-REPAIR Scrub Key expiry/delete policy artifact repair

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP28-REPAIR — Scrub Key expiry/delete policy artifact repair`

Status: completed documentation-repair-only.

## Summary

WP28-REPAIR verified that the WP28 policy artifact is present at the expected repository path:

```text
SCRUB_KEY_EXPIRY_DELETE_POLICY.md
```

The artifact covers the required Scrub Key expiry/delete policy topics:

- Scrub Key retention principles;
- user-controlled deletion;
- matter/project retention guidance;
- download-folder risk;
- shared-computer risk;
- expiry guidance;
- manual deletion guidance;
- loss-of-key consequences;
- tampering/mismatch consequences;
- audit/logging expectations;
- what MVP should warn about;
- what later secure/local desktop versions may enforce;
- what must never be deleted silently;
- recommended next implementation phases;
- Dutch user-facing policy copy examples.

No policy rewrite was needed in this repair run because the artifact was already present locally and aligned with WP25, WP26, WP27, `SCRUB_KEY_SPEC.md`, WP58, `RISK_REGISTER.md` and `DECISION_LOG.md`.

## Files added

- `handover/workpackages/20260611_2135_scrub_key_expiry_delete_policy_repair.md`

## Files changed

- `CHANGELOG.md`

## Files verified

- `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests/checks

- `test -f SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `rg -n "retention|User-controlled|Matter|Download|Shared|Expiry|Manual deletion|Loss-of-key|Tampering|Audit|MVP|Later|never be deleted|implementation phases|Bewaar|Verwijder" SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `git diff --check`

No tests were run because this was documentation/artifact repair only and no code or test files were changed.

## Validation status

- Required start files read: `AGENTS.md`, `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Required context read: `SCRUB_KEY_THREAT_MODEL.md`, `SCRUB_KEY_LIFECYCLE_SPEC.md`, `SCRUB_KEY_WARNING_UX_PLAN.md`, `SCRUB_KEY_SPEC.md`, `PARALLEL_SPEC_CONSOLIDATION_WP58.md`, `RISK_REGISTER.md`, `DECISION_LOG.md`.
- Policy artifact verified at `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`.
- Central docs already record WP28 as completed and point to the policy artifact.
- `RISK_REGISTER.md` already records WP28 as a mitigation under R2.
- `DECISION_LOG.md` already records the accepted user-controlled deletion decision in D013.

## GitHub Actions status

- Not checked for a remote run at handover time.

## Hugging Face sync status

- Not applicable. This repair changed documentation only and no app/runtime behavior.

## App verification status

- Not applicable. No UI changed.

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
- No secrets or real data added.
- No cloud processing added.

## Remaining risks

- Warning UX is still not implemented.
- Secure import/export regression tests are still not implemented.
- No protected local storage, encrypted key container, integrity protection, local vault or recovery model exists yet.
- Browser Downloads, shared-computer use, cloud sync and backups remain user-managed risks.

## Next recommended step

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if warning implementation planning should precede tests: `WP28B — Scrub Key warning implementation planning`.
