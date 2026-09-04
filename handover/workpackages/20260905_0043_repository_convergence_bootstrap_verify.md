# Assurance handover — Repository Convergence Bootstrap fresh re-verification

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
PR: #114 — `SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP`  
Issue: #113  
Exact frozen candidate head reviewed: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Expected/actual base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Actual merge-base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Verdict: `PASS`  
Review time: 2026-09-05 00:43 Europe/Amsterdam

## Blind-first boundary

This review was reconstructed fresh from GitHub and the canonical Execution & Engineering Constitution. Prior assurance verdicts, PR implementation claims, implementation handover and PR comments were not used as correctness evidence before the initial verdict.

The initial blind-first reading order was:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`
5. `AGENTS.md`
6. `DECISION_LOG.md`
7. `RISK_REGISTER.md`
8. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
9. canonical `Execution & Engineering Constitution`

The review then independently inspected exact Git identity, full 17-file PR scope/diff, the remediation delta, relevant governance/product contracts, changed regression tests, historical provenance and raw GitHub Actions.

Only after the initial `PASS` was reached were PR comments, implementation claim and implementation handover opened as administrative cross-checks.

## Candidate identity

Frozen head:

```text
8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

Base and merge-base:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

The base-to-head comparison is 26 commits ahead, 0 behind, with exactly 17 changed files.

## Full changed-file scope

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

No `presidio_streamlit.py`, recognizer, profile, threshold, review runtime, export runtime, Scrub Key runtime, reinsert runtime, document transformation, replacement-memory runtime, Azure/OpenAI runtime, Docker, dependency or Hugging Face runtime file changed.

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

No runtime, product, test or canonical-document file was modified by this final remediation.

## Primary ledger remediation finding

Resolved.

The ledger now explicitly distinguishes pre-bootstrap findings from the current candidate state. The rows for `PROJECT_PROMPT.md`, `AGENTS.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`, `DECISION_LOG.md`, `RISK_REGISTER.md`, Hugging Face role and Local/offline installer routing no longer present already-fixed bootstrap debt as current future work.

Already resolved documentary rows are marked `RECONCILE — RESOLVED IN BOOTSTRAP CANDIDATE` or, for the Local installer, `VARIANT-SPECIFIC — DEFERRED / BOOTSTRAP ROUTING RESOLVED`.

Genuine unresolved findings remain visible, including persistent replacement memory, Azure AI Language, OpenAI/Azure synthesis, content-bearing prompt logging, legacy startup patch invocation, issue-state reconciliation and validation/evidence hierarchy.

The ledger remains explicitly `TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE` and does not become a competing permanent source of truth.

## Full candidate governance review

The candidate creates one current repository truth and exactly five strategic stages:

1. Repository Convergence
2. Scrub Private Application
3. Private Service
4. External Product & Service Assurance
5. Pilot

`WORKPACKAGES.md` exposes one current executable queue and requires later convergence work to be evidence-derived rather than pre-invented.

Historical provenance remains separated from current execution authority. D044 is present and still-binding product decisions are retained. Critical false-negative, Scrub Key, Zorg and Private trust-boundary risks remain explicit.

No new Evidence Framework, source-tree clone, Local-installer critical path, confidential-production claim for Hugging Face, or premature platform/multitenancy/API/billing/dashboard architecture was introduced.

## Still-binding product semantics

Verified preserved:

- mandatory human review;
- Legal and Zorg;
- preservation of legal/clinical meaning;
- side-by-side/current review authority;
- Standard and Expert over the same authoritative state;
- staged single-workspace Standard flow;
- document-bound Scrub Key and mapping digest;
- wrong/mixed document-key binding fails closed;
- document-first reinsert;
- supported DOCX body/tables/headers/footers with explicit unsupported boundaries for comments, tracked-change-only content, footnotes/endnotes, text boxes, metadata and split placeholders where applicable;
- pseudonymisation/privacy-processing claim boundary rather than guaranteed irreversible anonymisation.

Relevant current source confirms generation-bound Standard/Expert state and fail-closed Scrub Key/document binding. No product runtime source was changed in this PR.

## Regression/test review

The changed tests protect current semantic invariants rather than restoring obsolete document placement as release authority.

Notable bindings:

- formal five-stage roadmap headings instead of global prose occurrence counting;
- current DOCX scope bound to D030 while historical completion evidence comes from archived history/handovers;
- document-first reinsert and fail-closed binding bound to D031/D037;
- Standard/Expert and staged-workspace semantics bound to D041/D043;
- historical Premium package names/order are explicitly not required in the current queue;
- the no-new-Evidence-Framework constraint uses one stable semantic prohibition rather than duplicate prose requirements.

## Historical provenance

`history/CHANGELOG_PRE_CONVERGENCE_20260904.md` at the frozen candidate and `CHANGELOG.md` at the exact pre-convergence base have identical Git blob SHA:

```text
e5a5dbff25bdacdfa4ed96da4ab6372feb1e7a3b
```

This proves byte-identical preservation of the pre-convergence changelog.

## Exact-head raw Actions

Workflow: `Tests`  
Run: `33924699630`  
Job: `101190549754`  
Workflow head SHA: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
PR merge candidate checked out by Actions: `de0b79cf7000d695b8c5ea9e079fb973410e527d`

Raw checkout states that merge candidate is:

```text
Merge 8028643ed2f11b9f43bf32854e2d4cf86fb387f0 into 54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Raw pytest result:

```text
1264 passed in 14.03s
```

Conclusion:

```text
SUCCESS
```

## Formal verdict

```text
PASS
```

No material correctness, governance, privacy-boundary, historical-provenance, source-of-truth, scope-integrity or regression defect was found in the frozen candidate.

## Administrative cross-check

After the initial blind-first verdict, implementation claim/handover and PR comments were inspected. They disclose the same one-file final remediation, same 17-file total scope, same exact-head Actions evidence and no undisclosed runtime/product change. Earlier FAIL verdicts were treated as non-transferable historical administration only.

## Merge status

PR #114 had already been merged before this repeated fresh assurance request was completed, so no second merge was attempted.

Actual merge SHA:

```text
255cd619d5cf6eab32f9383940eaa4af362cb68c
```

Fresh GitHub readback confirms `main` is still exactly this SHA and the merge commit parents are exactly:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

## Exact-main Actions

Workflow: `Tests`  
Run: `33925330688`  
Job: `101192486044`  
Head SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Conclusion: `SUCCESS`

Raw pytest result:

```text
1264 passed in 14.09s
```

## Hugging Face sync / path-ignore

Workflow: `Sync to Hugging Face Space`  
Run: `33925330710`  
Job: `101192485863`  
Head SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Conclusion: `SUCCESS`

Raw log confirms the actual push:

```text
54c73e0..255cd61  HEAD -> main
```

Operational observation, non-blocking: `.github/workflows/sync-to-huggingface.yml` ignores many governance/test paths, but not `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` or `history/**`. Therefore this governance/history merge triggered a successful HF sync instead of being completely path-ignored. This is sync-churn, not a runtime/product correctness defect in PR #114.

## App verification status

`N/A` for this bootstrap candidate. The PR changes no UI/runtime/product semantics, so no fresh app-verification claim is appropriate.

## Governance / issue status

Issue #113 is already `closed` with state reason `completed`. This is directly supported by the bootstrap PASS/merge/post-merge evidence. No unrelated Premium or technical issue is closed by this re-verification.

No post-merge edit to canonical `WORKPACKAGES.md` is made from this assurance role, because that would create a new unreviewed `main` SHA after exact-main evidence was established.

## Remaining risks

The bootstrap intentionally does not resolve the genuine convergence debt recorded in the ledger: persistent replacement memory, external Azure/OpenAI paths, synthesis prompt logging, legacy startup patch scripts, issue-state reconciliation and evidence/validation hierarchy. These remain work for separately scoped implementation packages.

The HF path-ignore gap for the ledger/history paths may be cleaned up later if sync churn is considered worth addressing; it is not a bootstrap release blocker.

## Next recommended step

Return to `implementation_operations`. Derive the next smallest technical/current-state convergence workpackage from the accepted ledger/current queue, create a new candidate, run its own evidence, and require a fresh independent assurance cycle. Do not perform that technical implementation from this assurance role.
