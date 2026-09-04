# Assurance handover — Repository Convergence Bootstrap verify

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
PR: #114 — `SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP`  
Issue: #113  
Exact frozen candidate head: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Expected/actual base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Merge-base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Verdict: `PASS`  
Review time: 2026-09-05 00:26 Europe/Amsterdam

## Blind-first boundary

The initial verdict was reached before the PR body, implementation handover, implementation comments, or prior assurance conclusions were used as correctness evidence.

The review first reconstructed, on the exact frozen SHA, the canonical project instructions and current truth from:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`
5. `AGENTS.md`
6. `DECISION_LOG.md`
7. `RISK_REGISTER.md`
8. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
9. the canonical Execution & Engineering Constitution

It then independently inspected exact PR identity, full diff, remediation delta, relevant governance/product contracts, runtime reference sources, contract tests and raw GitHub Actions evidence.

Prior FAIL verdicts on `ea203abb04f008a7e583387242a6f4917c72e591` and `503a15c8e087840cc004c03d4fbf8ff48cb9f066` were treated only as non-transferable historical administration after the initial verdict.

## Candidate identity

Frozen candidate reviewed:

```text
8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

Base and merge-base independently verified:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Before merge the PR was 26 commits ahead, 0 behind, with exactly 17 changed files and no runtime/product source files.

## Full changed-file scope

Exactly 17 files:

1. `AGENTS.md`
2. `CHANGELOG.md`
3. `DECISION_LOG.md`
4. `PROJECT_PROMPT.md`
5. `PROJECT_PROMPT_SHORT.md`
6. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
7. `RISK_REGISTER.md`
8. `ROADMAP.md`
9. `WORKPACKAGES.md`
10. `handover/workpackages/20260904_2315_repository_convergence_bootstrap.md`
11. `history/CHANGELOG_PRE_CONVERGENCE_20260904.md`
12. `tests/test_mvp_document_fidelity_pr_final_contracts.py`
13. `tests/test_premium_core_flow_ui_realignment_plan.py`
14. `tests/test_premium_staged_workspace_decision.py`
15. `tests/test_reinsert_auto_flow_app_verify_closeout.py`
16. `tests/test_repository_convergence_bootstrap_contracts.py`
17. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP.md`

Scope conclusion: documentation/governance/tests/history/claim/handover only. No changes to `presidio_streamlit.py`, recognizers, profiles, thresholds, review runtime, export runtime, Scrub Key runtime, reinsert runtime, document transformations, replacement-memory runtime, Azure/OpenAI runtime, Docker, dependencies or HF runtime/workflow.

## Remediation delta

Independent compare:

```text
503a15c8e087840cc004c03d4fbf8ff48cb9f066
→
8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

Result:

```text
1 commit
1 changed file
REPOSITORY_CONVERGENCE_DEBT_LEDGER.md
11 additions
9 deletions
```

No runtime, product, test or canonical-document file changed in this remediation.

The ledger remediation is correct:

- documentary rows now explicitly distinguish `Pre-bootstrap finding` from the current candidate state;
- `PROJECT_PROMPT.md`, `AGENTS.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`, `DECISION_LOG.md` and `RISK_REGISTER.md` are marked `RECONCILE — RESOLVED IN BOOTSTRAP CANDIDATE` and describe their current candidate state accurately;
- the Hugging Face role and Local/offline installer routing rows are likewise aligned with the current candidate;
- already-resolved bootstrap debt is not offered as future cleanup;
- genuine unresolved technical, issue-state and validation-hierarchy findings remain unresolved;
- the ledger remains explicitly `TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE` and points permanent authority to the canonical decision/risk/workpackage/changelog sources.

## Full candidate findings

No material finding remains.

The reviewed candidate establishes a coherent current truth:

- exactly five strategic ROADMAP stages: Repository Convergence, Scrub Private Application, Private Service, External Product & Service Assurance, Pilot;
- one current executable WORKPACKAGES queue;
- no new Evidence Framework;
- no source-tree/application clone;
- Local/offline installer preserved/deferred rather than returned to the critical path;
- Hugging Face defined as a synthetic/approved-test application-validation environment, not confidential-production infrastructure assurance;
- no premature platform, generalized multitenancy, billing, dashboard, API-product, Kubernetes/service-mesh or similar architecture was introduced.

Still-binding product semantics remain materially represented:

- mandatory human review;
- Legal and Zorg profiles/policies;
- preservation of legal and clinical meaning;
- side-by-side review and authoritative replacement state;
- Standard/Expert over the same authoritative processing lineage;
- single-workspace staged Standard flow;
- document-bound Scrub Key plus canonical mapping digest;
- wrong/mixed/missing binding fails closed before replacement;
- document-first reinsert;
- DOCX body/tables/headers/footers supported scope with unsupported comments/tracked-change-only/footnotes/endnotes/text-box/metadata boundaries explicit;
- privacy claim remains pseudonymisation/reversible processing, not guaranteed irreversible anonymisation or perfect recall.

## Historical provenance

`history/CHANGELOG_PRE_CONVERGENCE_20260904.md` on the frozen candidate has Git blob SHA:

```text
e5a5dbff25bdacdfa4ed96da4ab6372feb1e7a3b
```

`CHANGELOG.md` on pre-convergence base `54c73e0...d3cd` has the exact same Git blob SHA.

Conclusion: pre-convergence changelog history is byte-identically preserved.

## Exact-head machine evidence

Workflow: `Tests`  
Run: `33924699630` (#2310)  
Job: `101190549754`  
Workflow head SHA: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
PR merge candidate checked out by Actions: `de0b79cf7000d695b8c5ea9e079fb973410e527d`  
Base represented by the merge candidate: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Conclusion: `SUCCESS`

Raw pytest result:

```text
1264 passed in 14.03s
```

The previously changed governance/legacy tests were independently inspected. They now protect stable semantic invariants through formal stage parsing and current D030/D031/D037/D041/D043 authority plus archived historical evidence; they do not restore obsolete ROADMAP/WORKPACKAGES prose placement as release authority.

## Verdict

```text
PASS
```

No material correctness, governance, privacy-boundary, source-of-truth, historical-provenance, scope-integrity or regression defect remains in exact frozen candidate `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`.

The independent PASS was registered on PR #114 before administrative implementation claims were used as a cross-check.

## Administrative cross-check

After the initial verdict, the PR body, implementation claim, implementation handover and implementation comments were inspected. They materially matched the independent reconstruction: exact identity, one-file final remediation, 17-file overall scope, machine evidence and no runtime/product change.

## Merge status

PR #114 was draft after PASS. Assurance changed only PR metadata to mark it ready for review; this did not modify the implementation branch or candidate SHA.

Merge was then executed with a hard expected-head guard:

```text
expected_head_sha = 8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

GitHub returned:

```text
merged = true
merge SHA = 255cd619d5cf6eab32f9383940eaa4af362cb68c
```

Post-merge verification confirms:

- PR #114 is closed and merged;
- PR head remains exactly `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`;
- merge commit first parent is exact base `54c73e0...d3cd`;
- merge commit second parent is exact reviewed head `8028643e...87f0`;
- `main` is exactly `255cd619d5cf6eab32f9383940eaa4af362cb68c`.

## Exact-main Actions

Workflow: `Tests`  
Run: `33925330688` (#2312)  
Job: `101192486044`  
Head branch: `main`  
Head SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Event: `push`  
Conclusion: `SUCCESS`

Raw pytest result:

```text
1264 passed in 14.09s
```

The raw Actions log confirms checkout of exact merge SHA `255cd619d5cf6eab32f9383940eaa4af362cb68c`.

## Hugging Face sync / path-ignore status

Workflow: `Sync to Hugging Face Space`  
Run: `33925330710` (#1532)  
Job: `101192485863`  
Head branch: `main`  
Head SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Conclusion: `SUCCESS`

Raw log confirms checkout of exact `main` SHA and successful push:

```text
54c73e0..255cd61  HEAD -> main
```

Therefore HF `main` was synchronized to the exact merged GitHub main commit.

Operational note, non-blocking: the current HF workflow ignores the main canonical docs, tests, claims and handovers, but it does not ignore `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` or `history/**`. Because those paths were present in this bootstrap merge, the docs/governance-only merge triggered a sync rather than being fully path-ignored. The sync succeeded and introduced no reviewed runtime/product source delta. If the intended policy is that all governance/history-only commits avoid HF churn, this can be reconciled later as a narrow workflow-maintenance item; it does not invalidate this candidate.

## App verification status

```text
NOT APPLICABLE
```

PR #114 changes no visible UI, runtime product semantics, document processing, export, Scrub Key, reinsert, recognition or deployed application behavior. No live application verification is required by the assurance contract for this package.

## Issue/workpackage governance status

Issue #113 was still open after the successful merge. Assurance closed only issue #113 with state reason `completed`, because this PASS/merge/post-merge evidence directly proves that bootstrap package complete.

No other stale Premium or technical-convergence issues were closed. In particular, unresolved parent live-verification evidence such as #105/#96 remains unresolved unless separately proven.

`WORKPACKAGES.md` on merged main is not post-merge edited from this assurance role. Creating an extra status-only commit on main after exact-main verification would create a new unreviewed main SHA and invalidate the exact-main evidence just established. This handover records the completed state; any canonical execution-queue advancement should be performed as the next properly scoped governance/implementation state transition, not by silently mutating the reviewed candidate or exact-main proof.

## Remaining risks

No blocker to this bootstrap PASS remains. Existing documented risks deliberately remain for later evidence-backed convergence work, including:

- false negatives / missed sensitive data;
- Scrub Key handling and re-identification risk;
- hidden/unsupported document content;
- Private-line content persistence and third-party processing conflicts;
- current replacement-memory and Azure/OpenAI variant-specific paths;
- content-bearing synthesis prompt logging;
- legacy startup patch-script retirement candidates;
- unresolved issue-state reconciliation beyond #113;
- validation/evidence hierarchy classification;
- final consolidated live verification for historical parent Premium issues where evidence remains incomplete.

## Next recommended step

Return execution to `implementation_operations` / the coordinator.

The next package must be derived from current ledger evidence and the current WORKPACKAGES queue, remain small/root-cause scoped, and receive its own fresh assurance if consequential.

This assurance worker must not implement the next technical-convergence package.
