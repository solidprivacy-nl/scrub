# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_VERIFY

Repository: `solidprivacy-nl/scrub`  
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

## Independent decision

`SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR_VERIFY: FAIL`

The exact candidate is not authorized for merge or deployment.

## Independent evidence

- `refs/pull/99/head` independently confirmed exact head `55682db371d5547b85f84798cec49a1cdbe6ee73`.
- Exact merge candidate `3717c0d726b6038a15484887550edd12fc7c4fee` independently confirmed with parents base `4130976b7d9489de148dd17234faff4a18fad2f0` and head `55682db371d5547b85f84798cec49a1cdbe6ee73`.
- Persistent changed-file list contains exactly 10 paths and no temporary workflow/executor.
- Raw GitHub Actions Tests #2256 / run `31272580967`, job `93140921643`, checked out exact merge candidate `3717c0d726b6038a15484887550edd12fc7c4fee`.
- Command: `python -m pytest -q tests`.
- Result: `1240 passed in 15.23s`.
- Conclusion: success.

## Blocking findings

### 1. Real Expert review edits do not fail closed at the actual export surface

The candidate detects a changed authoritative review working set, persists it, and invalidates completed reviewed/export lineage by reopening Review. However, the Expert render path then continues to active TXT/DOCX/PDF download controls without requiring current `export_is_current` lineage or a new explicit review completion.

Therefore Download remains functionally usable immediately after a real Expert review edit even though the core state marks review/export stale. This violates issue #101 mandatory B4/B6 and the binding stale-output fail-closed invariant.

### 2. Mandatory executable integrated Streamlit evidence is missing

The cross-mode runtime test exercises state helpers and source-text assertions. The App Shell integration test is AST/source-string based. No `streamlit.testing` / AppTest-style executable product transition is present, and the exact Actions environment does not install Streamlit.

The green suite therefore does not execute the mandatory real transition `Standard completed Download → Expert edit → Download blocked → explicit review re-completion → Standard`, which issue #101 explicitly requires to be executable rather than merely inferred from helper/source assertions.

## Blind-boundary disclosure

A PR metadata connector response unexpectedly included PR #99's implementation narrative before the initial decision. That narrative was immediately excluded from the evidence basis. No implementation handover/claim/status file was intentionally opened before the initial FAIL. No bulk PR patch was used. The verdict was independently derived from issue #101 criteria, authoritative product/governance sources, exact source/tests, file identities, merge-parent identity and raw Actions logs.

Implementation handover/claim/CHANGELOG/WORKPACKAGES were opened only after the initial FAIL for administrative comparison.

## Authorization boundary

- PR #99 head `55682db371d5547b85f84798cec49a1cdbe6ee73`: **DO NOT MERGE**.
- Hugging Face deployment: not authorized/not applicable.
- Live app verification: not requested for this failed undeployed candidate.
- Parent issue #96 remains blocking.
- `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` remains blocked.

## Required next cycle

Return to `implementation_operations` to:
1. gate Expert document downloads on current completed review/export lineage;
2. require explicit review re-completion after a real Expert review edit;
3. preserve the edited authoritative rows across Standard/Expert;
4. add executable integrated Streamlit regression coverage for the full transition and processing-change safety;
5. freeze a new head SHA;
6. run full exact-head Actions;
7. route the new head to a completely fresh blind `governance_release_assurance` reviewer/session.

This verification claim records only the FAIL for the exact candidate above and cannot authorize any repaired future head.