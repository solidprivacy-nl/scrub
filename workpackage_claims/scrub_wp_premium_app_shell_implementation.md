# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `IMPLEMENTATION_IN_PROGRESS`  
Issue: #84  
PR: #85  
Branch: `wp/premium-app-shell-implementation`  
Claimed: 2026-08-08 14:47 Europe/Amsterdam

## Dependency check

The upstream staged-workspace architecture gate is satisfied:

- `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE_VERIFY: PASS` was recorded independently for PR #87 exact head `4d99430225f5086a84f2db33089e19688ca7793f`;
- PR #87 merged unchanged as `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`;
- the binding Standard model is therefore `One document. One workspace. Three stages. One active task.`

## Scope

Implement the shared Premium App Shell only:

- top-level `Anonimiseren | Terugzetten`;
- global `Standaard | Expert`;
- persistent `Toevoegen → Controleren → Downloaden` stage presentation;
- exactly one dominant stage in Standard;
- explicit active/completed/future stage states;
- compact completed-stage summaries and passive future stages;
- explicit return/edit affordance;
- automatic progression hooks tied to current processing/review lineage;
- Standard without a permanent configuration sidebar;
- production integration into `presidio_streamlit.py` without redesigning stage internals beyond shell/grouping needs.

## Safety boundary

Do not change recognizers, thresholds, replacement semantics, review-table/include authority, direct masking semantics, export bytes/names/MIME, Scrub Key schema/binding/lifecycle, reinsert semantics, audit semantics, dependencies, cloud/local-processing boundary, or the mandatory human-review requirement.

## Coordination

Exclusive ownership is claimed for the shared Streamlit shell surface while this package is active. Do not run another package that edits `presidio_streamlit.py`, `fix_streamlit_nested_expanders.py`, review-table flow, export/download flow, or shared workflow state in parallel.

## Validation plan

- focused pure shell/state tests first;
- production integration contract tests;
- full GitHub Actions regression on the exact candidate head;
- fresh independent `governance_release_assurance` before merge;
- after merge, exact-main Actions + GitHub→Hugging Face sync + live app verification because UI behavior changes.

## Execution-continuity note — 2026-08-08 15:08 Europe/Amsterdam

The latest PR event at head `7938b04a122e35d4a7a9fb9a64b0dec564ed8f87` ended as `action_required` before job creation (`0` jobs), so it is an Actions invocation-state problem rather than a regression-test failure. This administrative claim update intentionally creates a normal repository-user synchronize event without changing product semantics, solely to obtain executable exact-head CI on the current implementation candidate. The resulting new head must be treated as the only candidate eligible for later assurance.

Implementation will not self-certify or self-merge.
