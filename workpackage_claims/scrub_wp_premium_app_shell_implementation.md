# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`  
Issue: #84  
PR: #85  
Branch: `wp/premium-app-shell-implementation`  
Original claim: 2026-08-08 14:47 Europe/Amsterdam  
Repair cycle opened: 2026-08-08 16:42 Europe/Amsterdam

## Dependency check

The upstream staged-workspace architecture gate remains satisfied:

- `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE_VERIFY: PASS` was recorded independently for PR #87 exact head `4d99430225f5086a84f2db33089e19688ca7793f`;
- PR #87 merged unchanged as `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`;
- the binding Standard model remains `One document. One workspace. Three stages. One active task.`

## Independent assurance result requiring repair

`SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY` returned `FAIL` on prior exact head:

```text
2b04ca6260bddee07fbcf901239cee2955bd6dc7
```

Blocking finding returned to implementation:

- Standard persisted the selected recognition profile in `_premium_profile_label`;
- Expert initialized `Controlemodus` with hard-coded `index=1`, which can silently change an explicitly selected Standard `Zorg` profile to `Juridisch` merely by switching presentation mode;
- operator/threshold/entity hydration and processing-generation synchronization required the same cross-mode integrity review;
- a repaired head requires fresh exact-head tests and a fresh blind assurance worker.

Issue #90 is closed as FAIL evidence. Governance-only verification administration was merged separately through PR #91; it is not candidate implementation evidence.

## Repair scope

Repair presentation/state integrity only. Preserve the already implemented staged App Shell and protected processing/export semantics.

Required repair behavior:

- Standard and Expert hydrate the same persisted processing-affecting settings;
- Standard → Expert → Standard with no processing-setting change preserves profile, operator, threshold, entity selection, allow/deny lists and analyzer configuration;
- presentation-only switching does not change the deterministic processing generation or invalidate valid downstream state;
- a real processing-setting change in Expert changes the processing generation and invalidates downstream processed/review/export lineage fail-closed;
- Standard never silently rewrites an Expert-only operator;
- regression coverage explicitly includes Standard Zorg → Expert → Standard state preservation.

## Current repair implementation

The branch now includes:

- reusable persisted-setting helpers in `premium_streamlit_state.py`;
- deterministic hydration helpers for profile, operator, threshold, entities, allow/deny lists and analyzer parameters;
- Expert widget hydration on entry and Standard profile-widget rehydration on return;
- processing-generation synchronization in both presentation modes rather than only Standard;
- fail-closed cached-review invalidation only when the deterministic generation actually changes;
- new cross-mode regression tests and source-integration contract tests.

The temporary repair workflow and executor self-deleted after applying the production `presidio_streamlit.py` patch. They are not intended to remain in the final PR diff.

## Safety boundary preserved

Do not change:

- recognizers/profile rules;
- recognition threshold meaning;
- replacement-table/include authority;
- direct masking semantics;
- export bytes, filenames or MIME types;
- Scrub Key schema, document binding or lifecycle;
- reinsert behavior;
- audit semantics;
- dependencies;
- cloud/local-processing boundary;
- mandatory human review.

## Validation boundary

A connector-authored claim update intentionally retriggers normal PR GitHub Actions after the bot-authored self-cleaning repair commit produced `action_required` checks with zero jobs.

Only a new exact repaired head with a real executable full-suite result may become `RELEASE_CANDIDATE_READY`.

Implementation does not self-certify or self-merge. Any repaired release candidate requires a fresh independent `governance_release_assurance` decision.


## Repair validation result — 2026-08-08 16:55 Europe/Amsterdam

The functional repair and new regression contracts are green before final administrative identity:

```text
Tests run #2229 / ID 31263099583
job 93116829430
branch head under test: f6dd1fede240f9cacf29bd5323dec9f182052828
PR merge candidate: bd3c404f7075d86620272bf28c9a5192006e8209
base main in tested merge candidate: 2831da154e6c299b3616d62a37f151ebfa9c45f1
command: python -m pytest -q tests
result: 1235 passed in 14.48s
conclusion: success
```

The final administrative commit changes candidate identity but not runtime behavior. Therefore this claim is not sufficient release evidence by itself: a fresh full exact-head GitHub Actions run on the final candidate is mandatory before handoff to a new blind reviewer.
