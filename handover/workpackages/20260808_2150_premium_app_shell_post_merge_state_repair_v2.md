# Handover — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_V2

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_V2 — enforce fail-closed Expert export and executable UI evidence`  
Role: `implementation_operations`  
Parent implementation issue: #98  
Parent governance conflict: #96  
Candidate PR: #104  
Status: `IMPLEMENTATION_IN_PROGRESS` pending final post-administration exact-head CI; fresh independent assurance required before merge.

## Files added

- `premium_streamlit_export_gate.py`
- `tests/streamlit_apps/premium_export_gate_flow_app.py`
- `tests/test_premium_streamlit_export_gate_app.py`
- this handover
- `workpackage_claims/scrub_wp_premium_app_shell_post_merge_state_repair_v2.md`

## Files changed

- `presidio_streamlit.py`
- `.github/workflows/tests.yml`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `WORKPACKAGES.md`
- plus the prior PR #99 state-repair files carried forward on the reconciled branch.

Temporary one-shot patch workflow/script were self-deleted and must not appear in the persistent PR diff.

## Implementation summary

The concrete issue #101 FAIL was reproduced from source: Expert review edits invalidated `reviewed_generation` and `export_generation`, but export buttons still rendered later in the same Streamlit execution. V2 adds one narrow export-readiness gate before the first download surface. The gate permits exports only when the core flow reports `export_is_current`. When current processing remains valid but review changed, Expert offers an explicit `Controle opnieuw afronden` action. When source or processing settings changed, the gate does not offer that shortcut and requires reprocessing.

## Tests

Executable AppTest coverage now proves:
- completed Standard state can enter Expert without source/generation/cache drift;
- an Expert review edit preserves the edited row, makes reviewed/export lineage stale and removes export availability;
- explicit re-completion restores current review/export and returning to Standard preserves source/generation/analysis/review rows;
- a real processing-setting change creates a new generation, clears analysis/review caches and blocks export without a review-only shortcut;
- Expert-only `highlight` remains preserved when returning to Standard.

Pre-administration full suite:
- Tests #2261 / run `31275276471`;
- job `93147717998`;
- exact PR merge candidate `abeb56ee683fb4c97e0c2fef7786ed65c825b582` = head `d688cc3b980da63c3c3f0bfb98e990a00b746c4b` into base `2623524c858216318d238213e37445193510fa73`;
- CI installed Streamlit `1.61.1`;
- `python -m pytest -q tests` → `1244 passed in 13.89s`.

Final post-administration exact-head CI: pending at handover-write time and must be recorded in PR/issue metadata without further repository mutation.

## Validation status

- Functional/source validation: candidate behavior implemented; executable pre-admin regression green.
- GitHub Actions status: pre-admin green; final exact-head pending.
- Hugging Face sync status: not applicable before authorized merge; must be verified for exact merge commit after PASS/merge.
- App verification status: pending/blocked until repaired runtime independently PASSes, merges and synchronizes.

## Remaining risks

- Implementation cannot certify that the candidate fully satisfies assurance; a fresh independent blind reviewer must reconstruct the final exact head.
- The already-merged App Shell remains governance-unconfirmed while issue #96 is open.
- Any candidate-head movement after final machine evidence invalidates that assurance identity.

## Next recommended step

Run final full exact-head GitHub Actions after the claim/admin commit, freeze the SHA, then route PR #104 to a completely new `governance_release_assurance` session. Do not start Premium Input Stage.