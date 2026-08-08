# Handover — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY

Repository: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY — blind assurance for PR #85`  
Role: `governance_release_assurance`  
Status: `GOVERNANCE_FAIL`  
Initial assurance decision: `FAIL`  
Issue: `#90`  
Candidate PR: `#85`  
Candidate head: `2b04ca6260bddee07fbcf901239cee2955bd6dc7`  
Base main: `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`  
Tested merge candidate: `ed7728fc85f22026863faab435a00a31a5aa1438`  
Decision recorded: 2026-08-08 16:17 Europe/Amsterdam

## Summary

Independent release assurance returned `FAIL` for exact PR #85 head `2b04ca6260bddee07fbcf901239cee2955bd6dc7`.

The exact production Streamlit source violates the binding Standard/Expert presentation-only invariant. Standard persists the active recognition profile in `_premium_profile_label`, but the Expert `Controlemodus` widget initializes from a hard-coded `index=1` instead of the persisted profile. In the authoritative profile order, index 0 is Care/Zorg and index 1 is Legal/Juridisch. A user can therefore select Zorg in Standard, switch only the presentation mode to Expert, and silently arrive in the Juridisch processing profile.

This is a processing/state-integrity defect, not a visual-polish issue. It violates the requirement that a presentation-mode change itself must not change or reprocess the current processing model. It also risks inconsistent lineage because candidate generation synchronization is performed on the Standard path while the Expert path can proceed after the silently changed profile.

No candidate repair was made by assurance. PR #85 was not merged.

## Independent evidence

Authoritative inputs reviewed included:

- `PROJECT_PROMPT.md`;
- `ROADMAP.md` for binding direction;
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- merged `premium_core_flow_state.py`;
- exact candidate production/source helper files and tests;
- raw GitHub Actions run/job/log evidence.

Source-level reconstruction established:

1. `current_profile_options_with_care()` uses the authoritative target Streamlit profile order.
2. That order is Care/Zorg first and Legal/Juridisch second.
3. Standard hydrates `profile_label` from `_premium_profile_label` and writes Standard profile changes back to that key.
4. Expert instead creates its profile widget with `index=1`, without hydrating `_premium_profile_label`.
5. The existing integrated tests do not exercise Standard Zorg → Expert profile preservation; the pure `synchronize_shell_choices(...)` test does not cover the Streamlit widget default/reset path.

## Tests and machine evidence

Exact raw GitHub Actions evidence independently inspected:

```text
workflow: Tests
run: #2211 / 31259805641
job: 93108743739
candidate head: 2b04ca6260bddee07fbcf901239cee2955bd6dc7
checked-out PR merge ref: ed7728fc85f22026863faab435a00a31a5aa1438
checkout log: Merge 2b04ca... into d54eb06...
command: python -m pytest -q tests
result: 1225 passed in 10.32s
conclusion: success
```

The green suite is valid machine evidence, but it does not cover the blocking Standard/Expert profile-preservation integration path and therefore cannot support PASS.

A direct container clone was attempted for an additional local run, but the execution container had no external DNS/network access to GitHub. This did not require user action and did not prevent the decision because exact source and decoded raw Actions logs were available through the GitHub connector.

## Files added/changed by this assurance worker

Candidate PR #85: **none**.

Separate assurance administration branch `assurance/issue90-premium-app-shell-fail`:

- added `handover/workpackages/20260808_1618_premium_app_shell_implementation_verify.md`;
- added `workpackage_claims/scrub_wp_premium_app_shell_implementation_verify.md`.

No runtime, test, review, export, Scrub Key, reinsert or deployment file was modified.

## Validation status

- Initial assurance: `FAIL`.
- Candidate identity rechecked immediately before decision: unchanged at `2b04ca6260bddee07fbcf901239cee2955bd6dc7`.
- Candidate merge: `NOT EXECUTED`.
- GitHub Actions candidate evidence: `GREEN BUT INSUFFICIENT FOR PASS` because the blocking transition is untested and source is non-conforming.
- GitHub Actions post-merge: `NOT APPLICABLE — FAIL / no merge`.
- Hugging Face sync: `NOT EXECUTED — FAIL / no merge`.
- Runtime health/smoke: `NOT EXECUTED — FAIL / no deployment action`.
- App verification: `NOT EXECUTED — FAIL / no deployment action`.

## Governance transparency note

The connector's bulk PR-diff response unexpectedly included bodies of paths under `handover/workpackages/` and `workpackage_claims/` before the initial verdict, even though those paths were intended to be excluded from blind review. Those implementation narratives were not used as evidence for the decision. The blocking finding above was independently derived from permitted exact source, authoritative profile ordering, binding contracts and raw machine evidence. Because the decision is `FAIL`, no release authorization resulted from this exposure. Any repaired head already requires a fresh blind reviewer/pass.

## Remaining risks

- The same widget hydration path should be checked for operator, threshold, entity selection and other processing-affecting Expert state; the profile defect alone is sufficient to block this head.
- The current test suite has a coverage gap around integrated Standard ↔ Expert state preservation.
- Until repaired and freshly assured, Expert can potentially operate against processing settings that do not correspond to the lineage previously established in Standard.

## Next recommended step

Return to `implementation_operations` and create a new release candidate that:

1. hydrates Expert processing-affecting controls from the authoritative persisted state when presentation mode changes;
2. preserves Standard → Expert → Standard state unless the user explicitly changes a processing-affecting control;
3. fail-closes and invalidates downstream lineage only when such a control is explicitly changed;
4. adds integrated regression coverage for profile preservation, including Standard Zorg → Expert and return;
5. checks the same preservation/invalidation contract for operator, threshold and entity selection;
6. receives a new head SHA and full exact-head regression;
7. receives a fresh independent blind `governance_release_assurance` decision before any merge.

`SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` remains gated.