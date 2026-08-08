# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`  
Issue: #84  
PR: #85  
Branch: `wp/premium-app-shell-implementation`  
Claimed: 2026-08-08 14:47 Europe/Amsterdam  
Candidate prepared: 2026-08-08 15:28 Europe/Amsterdam

## Dependency check

The upstream staged-workspace architecture gate is satisfied:

- `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE_VERIFY: PASS` was recorded independently for PR #87 exact head `4d99430225f5086a84f2db33089e19688ca7793f`;
- PR #87 merged unchanged as `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`;
- the binding Standard model is therefore `One document. One workspace. Three stages. One active task.`

## Implemented scope

The production Streamlit candidate now implements the shared Premium App Shell:

- top-level `Anonimiseren | Terugzetten`;
- global `Standaard | Expert`;
- persistent `Toevoegen → Controleren → Downloaden` stage presentation;
- exactly one dominant Standard stage;
- explicit active/completed/future stage states;
- compact completed-stage summaries and passive future stages;
- successful processing auto-advances to Review;
- explicit review completion auto-advances to Download;
- explicit return/edit affordance;
- deterministic processing lineage and fail-closed downstream invalidation;
- current-generation analysis cache so stage navigation does not silently re-run recognition;
- cached review rows with fail-closed Download invalidation when Review is reopened;
- Standard without a permanent configuration sidebar;
- Expert retains the existing advanced configuration surface;
- Expert-only `highlight` and `synthesize` choices are never silently rewritten by Standard: Standard asks the user to return to Expert;
- legacy runtime patching is bypassed for the direct Premium source so the retired long-form/two-mode UI cannot be re-injected at container startup.

## Safety boundary preserved

No intended semantic changes to:

- recognizers or profile rules;
- recognition thresholds as processing semantics;
- replacement-table/include authority;
- direct masking semantics;
- export bytes, filenames or MIME types;
- Scrub Key schema, document binding or lifecycle;
- reinsert behavior;
- audit semantics;
- dependencies;
- cloud/local-processing boundary;
- mandatory human review.

The App Shell is presentation/state orchestration only. Subsequent Input, Review and Export simplification remain separate sequential workpackages.

## Regression evidence

Normal PR-triggered GitHub Actions on clean product head `0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d`:

```text
Tests run #2200 / ID 31259576962
job 93108182555
python -m pytest -q tests
1225 passed in 12.55s
conclusion: success
```

Earlier red runs were used as implementation feedback. A temporary diagnostic workflow confirmed an intermediate repaired head at `1223 passed`; that diagnostic workflow was removed from the candidate before clean-head validation.

## Finalization boundary

Administrative closeout files are added after the clean product regression. Those administrative commits change candidate identity but not runtime product behavior, therefore a fresh full exact-head GitHub Actions run is still required before assurance. The exact final assurance head and run evidence must be recorded in PR #85 / issue #84 metadata without further repository changes.

### Execution-continuity note — 2026-08-08 15:32 Europe/Amsterdam

The administrative-finalization commit `d7f57ff59fc50edcc1c78fcf61090df33f4107ce` was authored by GitHub Actions and therefore its follow-up PR checks were `action_required` with no executable jobs. This note is semantics-neutral and exists only to create a repository-user PR synchronize event so the final post-administration head receives executable exact-head regression evidence. No runtime/product file or behavior is changed by this note.

## Coordination and governance

Exclusive ownership of the shared Streamlit shell remains claimed until this candidate leaves implementation. Do not run another package that edits `presidio_streamlit.py`, `fix_streamlit_nested_expanders.py`, review-table flow, export/download flow, or shared workflow state in parallel.

Implementation does not self-certify or self-merge. Fresh independent `governance_release_assurance` must issue `PASS | FAIL | INDETERMINATE` on the final exact head before merge.

After PASS/merge:

1. verify exact-main GitHub Actions;
2. verify GitHub → Hugging Face synchronization for the exact runtime candidate;
3. request live app verification because UI behavior changed;
4. only then release `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`.
