from pathlib import Path

STAMP = "2026-08-08 21:50 Europe/Amsterdam"
WP = "SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_V2"


def prepend(path: str, block: str) -> None:
    p = Path(path)
    old = p.read_text(encoding="utf-8") if p.exists() else ""
    p.write_text(block.rstrip() + "\n\n---\n\n" + old, encoding="utf-8")


prepend(
    "CHANGELOG.md",
    f"""## {STAMP} — {WP} — executable fail-closed Expert export repair

Status: `IMPLEMENTATION_IN_PROGRESS` until the post-administration exact-head full-suite run is green; fresh independent assurance remains mandatory.

Reason:
- independent assurance issue #101 correctly returned `FAIL` on PR #99 because a real Expert review edit cleared review/export lineage but the same render still exposed document, Scrub Key and audit downloads;
- the same review also found that prior evidence lacked an executable Streamlit transition test.

Repair:
- all existing export/download controls now sit behind current `CoreFlowState.export_is_current` lineage;
- a real Expert review edit immediately blocks the entire downstream export surface;
- Expert exposes one explicit `Controle opnieuw afronden` action only when current processing is still reviewable;
- review is never silently auto-completed after edits;
- real source/processing-setting changes remain blocked until reprocessing and cannot use the review-recompletion shortcut;
- authoritative edited review rows remain generation-bound and survive Standard/Expert presentation switches;
- product export payload bytes, filenames and MIME semantics are unchanged once eligibility is current.

Executable regression:
- added `streamlit.testing.v1.AppTest` coverage for Standard Download → Expert → review edit → export blocked → explicit review completion → Standard with source/generation/analysis/review state preserved;
- added executable processing-setting invalidation coverage;
- added executable Expert-only `highlight` preservation coverage;
- CI now installs Streamlit for the test environment.

Pre-administration machine evidence:
- PR #104 head `d688cc3b980da63c3c3f0bfb98e990a00b746c4b`;
- base main `2623524c858216318d238213e37445193510fa73`;
- tested merge candidate `abeb56ee683fb4c97e0c2fef7786ed65c825b582`;
- Tests #2261 / run `31275276471`, job `93147717998`;
- raw checkout confirms the exact merge candidate;
- Streamlit `1.61.1` installed in CI;
- `python -m pytest -q tests` → `1244 passed in 13.89s`.

Protected semantics intentionally unchanged:
- recognizers/profile rules and threshold meaning;
- authoritative include/replacement decisions and direct masking;
- eligible export bytes, filenames and MIME types;
- Scrub Key schema/binding/lifecycle;
- reinsert and audit semantics;
- local/cloud processing boundary;
- mandatory human review.

Final exact-head CI is mandatory after this administration. Implementation does not self-certify or self-merge. Parent issue #96 and Premium Input Stage remain blocked pending fresh assurance, merge, deployment evidence and live app verification.""",
)

prepend(
    "RELEASE_NOTES.md",
    """## Unreleased — Premium review/export safety

A pending Premium App Shell correction makes the download boundary stricter after review changes. When an Expert user changes a reviewed replacement, document downloads, the Scrub Key and audit downloads remain unavailable until the current review is explicitly completed again. A change to the source or processing settings requires reprocessing first. No existing export format or Scrub Key content is changed by this correction.

This change is not released until independent assurance, merge, synchronization and required live-app verification are complete.""",
)

prepend(
    "WORKPACKAGES.md",
    f"""# SolidPrivacy Scrub — Current execution status override

> **{STAMP}**  
> This block supersedes lower current-status fields for the Premium UI line. Historical package records remain below.

## Premium UI execution queue

1. `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` — **COMPLETED**.
2. `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION` — **MERGED BUT OUTCOME NOT CONFIRMED**; parent governance conflict issue #96 remains open after contradictory earlier assurance.
3. `{WP}` — **IMPLEMENTATION_IN_PROGRESS / PR #104**. This V2 candidate supersedes failed PR #99 and addresses issue #101's two blockers: actual fail-closed export enforcement and executable Streamlit transition evidence. Final exact-head CI and a completely fresh blind `governance_release_assurance` review are mandatory.
4. `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` — **BLOCKED** until V2 independently PASSes, merges unchanged, exact-main/Hugging Face/runtime evidence is green, issue #96 is independently reconciled, and required live-app verification closes.
5. `SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION` — queued after Input Stage.
6. `SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION` — queued after Review Stage.
7. `SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION` — queued after the three stage packages.
8. `SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT` — final live Premium gate.

### V2 acceptance gate

- no document/Scrub-Key/audit download control may render unless `export_is_current` is true;
- a genuine Expert review-row edit must preserve the edited working set but clear completed review/export lineage and block downloads immediately;
- explicit human re-completion is required before downloads return;
- source/processing changes cannot be bypassed through review re-completion;
- executable `streamlit.testing.v1.AppTest` coverage must run in GitHub Actions;
- Standard/Expert must preserve authoritative source, current analysis and generation-bound review rows on presentation-only switches;
- Expert-only operators must not be silently coerced by Standard;
- protected recognizer, export-payload, Scrub Key, reinsert, audit and mandatory-review semantics remain unchanged.

Do **not** start downstream shared Streamlit work while this gate is open.""",
)

handover_path = Path("handover/workpackages/20260808_2150_premium_app_shell_post_merge_state_repair_v2.md")
handover_path.parent.mkdir(parents=True, exist_ok=True)
handover_path.write_text(
    f"""# Handover — {WP}

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `{WP} — enforce fail-closed Expert export and executable UI evidence`  
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

Run final full exact-head GitHub Actions after the claim/admin commit, freeze the SHA, then route PR #104 to a completely new `governance_release_assurance` session. Do not start Premium Input Stage.""",
    encoding="utf-8",
)

claim_path = Path("workpackage_claims/scrub_wp_premium_app_shell_post_merge_state_repair_v2.md")
claim_path.parent.mkdir(parents=True, exist_ok=True)
claim_path.write_text(
    f"""# Workpackage Claim — {WP}

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Parent issue: #98  
Parent governance conflict: #96  
PR: #104  
Status: `IMPLEMENTATION_IN_PROGRESS` pending final exact-head CI; fresh independent assurance mandatory.

## Claimed implementation scope

- Gate the existing export/download surface on current completed review/export lineage.
- Require explicit Expert review re-completion after a genuine review working-set edit.
- Preserve the authoritative edited generation-bound review rows across presentation switches.
- Keep genuine source/processing changes fail-closed to reprocessing.
- Add executable Streamlit AppTest evidence for the returned assurance blockers.

## Explicit exclusions

No intended recognizer/profile, threshold-meaning, authoritative include/replacement, eligible export-payload, Scrub Key schema/binding, reinsert, audit, local/cloud processing or mandatory-human-review semantic change.

## Evidence before final administration

Tests #2261 / run `31275276471`, job `93147717998`, merge candidate `abeb56ee683fb4c97e0c2fef7786ed65c825b582`, Streamlit `1.61.1`, `1244 passed in 13.89s`.

This claim is administrative evidence only and must not be used as pre-verdict assurance evidence. Final exact-head CI after this administrative commit remains mandatory.""",
    encoding="utf-8",
)
