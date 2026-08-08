# Handover — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_VERIFY

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_VERIFY — fresh blind assurance for PR #99`  
Role: `governance_release_assurance`  
Issue: #101  
Implementation issue: #98  
Parent governance gate: #96  
Candidate PR: #99  
Exact candidate head: `55682db371d5547b85f84798cec49a1cdbe6ee73`  
Exact base: `4130976b7d9489de148dd17234faff4a18fad2f0`  
Exact tested merge candidate: `3717c0d726b6038a15484887550edd12fc7c4fee`  
Status: `GOVERNANCE_FAIL`  
Verdict: `FAIL`

## Summary

Fresh release assurance independently reconstructed the exact PR #99 candidate from the binding Premium staged-workspace architecture, authoritative state model, candidate source/tests and raw GitHub Actions evidence.

The repair materially improves presentation-neutral source hydration, current-generation analysis reuse and generation-bound authoritative review-row persistence. However, it does not fail closed at the actual Expert export surface after a genuine review edit: the state model is invalidated back to Review, but the same Expert render path still exposes active TXT/DOCX/PDF download controls without requiring current reviewed/export lineage or a new explicit review completion.

The candidate therefore fails issue #101 mandatory criteria B4/B6 and may not be merged.

A second release blocker is evidence quality: the required executable integrated Streamlit transition is not present. Existing cross-mode tests execute helper/session state and source-text assertions; the App Shell integration tests are AST/source-string assertions. The exact CI job does not install Streamlit, so it cannot execute the production Streamlit UI transition demanded by issue #101.

## Blind-assurance boundary

Before the initial verdict, the reviewer did not intentionally inspect implementation handovers, workpackage claims, implementation conclusions in CHANGELOG/WORKPACKAGES, issue #98 implementation narrative, or issue #96 implementation comments as correctness evidence.

One tooling incident occurred: `get_pr_info` unexpectedly returned the PR #99 description together with neutral PR metadata. The implementation narrative in that response was immediately declared contaminated and excluded from the assurance evidence basis. No bulk PR diff/patch was used. The initial FAIL was derived independently from issue #101 criteria, authoritative project/governance documents, exact candidate source/tests, changed filenames, exact merge-parent identity and raw Actions logs.

Only after the initial FAIL was formally recorded on issue #101 were the implementation handover, claim, CHANGELOG and WORKPACKAGES entries opened for administrative comparison.

## Files inspected before verdict

Authoritative/control:
- `PROJECT_PROMPT.md`
- `ROADMAP.md` for product/architecture direction only
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`
- `premium_core_flow_state.py`
- `recognition_profiles.py`

Exact candidate source:
- `premium_streamlit_state.py`
- `presidio_streamlit.py`
- `premium_app_shell.py`
- `premium_streamlit_shell_ui.py`

Exact candidate tests:
- `tests/test_premium_cross_mode_runtime_state.py`
- `tests/test_premium_app_shell_streamlit_integration.py`
- `tests/test_premium_streamlit_state.py`
- `tests/test_premium_presentation_state_preservation.py`
- `tests/test_duplicate_input_surface_simplification_contracts.py`

Exact changed-file identities were listed separately. The persistent PR diff contains exactly 10 paths and no temporary workflow/executor.

## Files inspected after verdict for administration only

- `handover/workpackages/20260808_2035_premium_app_shell_post_merge_state_repair.md`
- `workpackage_claims/scrub_wp_premium_app_shell_post_merge_state_repair.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Administrative comparison found a disclosure gap: implementation states that real review changes invalidate Review/Download lineage and that tests cover fail-closed invalidation, but does not disclose that the Expert runtime continues to render active document download controls after that lineage invalidation. This mismatch did not create or alter the independent verdict.

## Blocking finding 1 — stale Expert export remains usable

Exact candidate behavior:

1. A completed current-generation review/export state exists.
2. Expert restores the authoritative generation-bound review working set.
3. A genuine editor change is detected using `review_rows_changed`.
4. The edited rows are persisted through `cache_review_rows`.
5. If completed review/export lineage existed, `select_stage(..., Stage.REVIEW)` clears `reviewed_generation` and `export_generation` while preserving current source/processed lineage.
6. The same Expert execution path then continues to the export section and renders active TXT/DOCX/PDF download buttons.
7. Those controls are not gated on `premium_state.export_is_current`, current reviewed/export generation, or a fresh explicit review completion.

Result: the internal state correctly says Download is stale, but the actual Expert product surface still allows document export immediately from an unrecompleted edited review.

This violates:
- issue #101 B4: completed Review/Export lineage must become stale fail-closed after a real Expert review edit;
- issue #101 B6: Download cannot silently remain current/usable until review is explicitly completed again;
- the binding staged-workspace invariant that stale output must not remain presented as current.

## Blocking finding 2 — required executable integrated UI evidence absent

Evidence inspected:
- `tests/test_premium_cross_mode_runtime_state.py` contains executable state/helper tests but its production-runtime integration assertion reads `presidio_streamlit.py` as text.
- `tests/test_premium_app_shell_streamlit_integration.py` performs AST/source-string contract assertions.
- repository search found no `AppTest` or `streamlit.testing` use.
- raw Actions dependency installation for the exact candidate installs pytest, Presidio and document dependencies, but not Streamlit.

Therefore the green full suite does not execute the mandatory real UI transition:

`completed Standard Review/Download → Expert → edit reviewed working set → Download blocked → explicit review completion → Standard with identical authoritative rows/state`.

Issue #101 explicitly requires integrated source/state behavior plus executable tests, not merely helper-unit/source assertions.

## Positive independent findings

The candidate does independently demonstrate several repaired invariants:
- source text is hydrated from one presentation-neutral cached source;
- uploaded-file context is reused when no new file is supplied;
- profile/operator/threshold/entity/list/analyzer settings are persisted independently of presentation mode;
- deterministic processing generation includes all documented processing-affecting inputs;
- current-generation analysis cache is reused in both Standard and Expert;
- authoritative review rows are bound to processing generation and restored in both modes;
- real processing-generation changes clear stale analysis/review caches and downstream lineage;
- Standard blocks valid Expert-only `highlight` / `synthesize` rather than silently coercing them;
- staged-workspace shell architecture remains source-consistent with the one-document/one-workspace/three-stage contract;
- no candidate path introduces a temporary workflow/executor.

These positives are insufficient to override the blocking stale-export defect and missing mandatory executable evidence.

## Tests / raw machine evidence

GitHub Actions:
- workflow: Tests #2256
- run: `31272580967`
- job: `93140921643`
- event: pull_request
- exact PR head: `55682db371d5547b85f84798cec49a1cdbe6ee73`
- exact base: `4130976b7d9489de148dd17234faff4a18fad2f0`
- exact checked-out merge candidate: `3717c0d726b6038a15484887550edd12fc7c4fee`
- merge candidate parents independently confirmed as exact base + exact head
- command: `python -m pytest -q tests`
- result: `1240 passed in 15.23s`
- conclusion: success

Machine evidence is valid for the tested suite but insufficient for release PASS because the required integrated Expert edit/export behavior is not executed by that suite and source inspection identifies a blocking defect.

## Validation status

- Candidate identity: confirmed exact.
- Persistent changed paths: 10, confirmed.
- Raw candidate GitHub Actions: green.
- Binding architecture/source-state review: completed.
- Mandatory A no-change cross-mode state preservation: helper/source evidence materially improved, but no executable production Streamlit transition.
- Mandatory B real Expert review edit: FAIL at actual export surface.
- Mandatory C real processing change: source/helper evidence supports fail-closed cache/lineage invalidation.
- Mandatory D Expert-only operator boundary: source evidence supports no silent coercion.
- Mandatory E staged App Shell architecture: no new blocking regression identified in reviewed source.
- Mandatory F protected semantics: no intended protected-semantic diff identified in the two runtime/state files, but release remains blocked by B/evidence failure.

## GitHub Actions status

Candidate PR #99 exact-head Actions: **SUCCESS**, `1240 passed in 15.23s`.

Governance outcome: **FAIL**. Green CI does not authorize merge.

## Hugging Face sync status

Not applicable for candidate release. PR #99 was not merged by this assurance worker and is not authorized for deployment.

## App verification status

Not requested. The failed candidate was not merged/deployed under this assurance decision. Live UI verification must wait for a repaired candidate to PASS, merge and synchronize.

## Files added by this assurance worker

- `handover/workpackages/20260808_2118_premium_app_shell_post_merge_state_repair_verify.md`
- `workpackage_claims/scrub_wp_premium_app_shell_post_merge_state_repair_verify.md`

No runtime/product/test/deployment file in PR #99 was modified.

## Findings returned to implementation

Issue #98 and PR #99 were updated with the exact blockers and required repair boundary:
- gate Expert exports on current completed review/export lineage;
- after a real Expert review edit, keep Download unavailable until an explicit re-completion action establishes current lineage again;
- preserve edited authoritative rows across return to Standard;
- add an executable integrated Streamlit transition test proving the full fail-closed/re-completion path;
- preserve real processing-change invalidation and Expert-only operator safety;
- freeze a new head, run full exact-head CI, then use a fresh blind assurance reviewer/session.

## Remaining risks

- Current PR #99 exposes stale/unrecompleted Expert review output through active document download controls.
- The production Streamlit integration path is not exercised by the exact candidate CI suite.
- Parent issue #96/App Shell outcome conflict remains unresolved.
- `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` remains blocked.
- Any repair changes the candidate identity and invalidates this review for authorization purposes.

## Next recommended step

`implementation_operations` repairs the Expert review-completion/export gate and adds executable integrated Streamlit regression coverage on a new candidate head. The new head receives full exact-head Actions and a completely fresh independent blind assurance issue/session. Do not merge PR #99 head `55682db371d5547b85f84798cec49a1cdbe6ee73`.