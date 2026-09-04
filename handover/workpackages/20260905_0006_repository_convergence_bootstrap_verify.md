# Assurance handover — Repository Convergence Bootstrap verify

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
PR: #114 — `SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP`  
Exact frozen head: `503a15c8e087840cc004c03d4fbf8ff48cb9f066`  
Expected/actual base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Merge-base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Verdict: `FAIL`

## Candidate shape

PR #114 was independently verified open, draft, unmerged and mergeable. Compare status is 25 commits ahead, 0 behind.

Changed files — exactly 17:

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

No runtime/product implementation file changed.

## Blind-first reconstruction

Before using implementation handover/claim/comments as administrative cross-checks, reviewed the exact frozen repository in the required order: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`, then `AGENTS.md`, `DECISION_LOG.md`, `RISK_REGISTER.md`, followed by the canonical Google Drive `Execution & Engineering Constitution`. Then independently inspected PR identity, compare/merge-base, changed-file set, changed governance tests, historical preservation and raw Actions.

## Raw exact-head GitHub Actions

Workflow: `Tests`  
Run: `33923171672` / #2308  
Job: `101185789549` — `Python regression tests`  
Workflow head SHA: `503a15c8e087840cc004c03d4fbf8ff48cb9f066`  
Workflow base SHA: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
PR merge candidate checked out: `a2d8855c15c4eb4d0f63fcf1054e6468471b1bcc`  
Command: `python -m pytest -q tests`  
Result: `1264 passed in 17.98s`  
Conclusion: `success`

The previous regression blocker is resolved on this exact frozen candidate.

## Test-contract review

`tests/test_repository_convergence_bootstrap_contracts.py` now validates the five macro stages via formal `## Stage N — ...` headings and no longer treats arbitrary global string counts as governance authority. The Evidence Framework prohibition is checked semantically without requiring duplicated prose.

The four adjusted legacy governance/document-location tests remove obsolete historical placement/status assertions while preserving current product authority through D030, D031, D037, D041 and D043 and retaining historical evidence in archive/claims/handovers. No material weakening of runtime/product invariants was found.

## Historical preservation

`history/CHANGELOG_PRE_CONVERGENCE_20260904.md` on the frozen head and pre-convergence `CHANGELOG.md` on base have the same Git blob SHA:

`e5a5dbff25bdacdfa4ed96da4ab6372feb1e7a3b`

The pre-convergence changelog is therefore byte-identically preserved.

Current governance still contains mandatory human review, Legal/Zorg, legal/clinical meaning preservation, side-by-side/current review authority, Standard/Expert shared state, staged Standard workspace, document-bound Scrub Key, fail-closed wrong/mixed binding, document-first reinsert, D030 DOCX scope with unsupported boundaries, and the pseudonymisation/not-guaranteed-irreversible-anonymisation claim boundary.

## Roadmap result

The five-stage route remains coherent and minimal:

`Repository Convergence → Scrub Private Application → Private Service → External Product & Service Assurance → Pilot`.

No local-installer critical path, premature VPS build, multitenancy/API/billing/dashboard platform, second Evidence Framework or product-runtime rewrite is introduced.

## Blocking finding

### HIGH — `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` contradicts the already-remediated frozen repository

Exact location: `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`, section `## Current capability/path ledger`, rows for `PROJECT_PROMPT.md`, `AGENTS.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`, `DECISION_LOG.md` and `RISK_REGISTER.md`.

The ledger calls itself a **Current capability/path ledger**, yet on the same frozen SHA it still describes these documents in their pre-bootstrap state and routes them to `Fix in bootstrap`. Examples:

- ROADMAP is said to still mix the old nine-phase/local-installer route, while the exact-head ROADMAP already has the five-stage strategy;
- WORKPACKAGES is said to still contain stacked current-status overrides, while the exact-head file explicitly contains one current executable queue;
- DECISION_LOG is said to still lack the new strategic direction and require D044, while D044 is already present;
- RISK_REGISTER is said to still assume local-first final trust, while exact-head R5 is already the Scrub Private retention/egress risk;
- PROJECT_PROMPT and AGENTS are said to still require local-first routing remediation even though they are already aligned;
- CHANGELOG is described as the large pre-convergence file to prepend, while the exact-head root changelog has already been reset after byte-identical archival.

Why it matters: this workpackage exists specifically to remove source-of-truth drift. The temporary ledger is used to derive subsequent convergence packages. Presenting already-resolved baseline observations as current facts can reopen non-existent work and directly violates the Constitution's one-source-of-truth/documentation-matches-reality rules. Its `TEMPORARY ... NON-AUTHORITATIVE` warning reduces authority but does not make false present-tense execution evidence safe.

Smallest complete remediation: change no runtime/product code. Either (a) explicitly relabel these documentary rows as a **pre-bootstrap baseline audit snapshot** and mark the bootstrap-resolved rows resolved/currently aligned, or (b) update/remove the seven stale rows so the `Current capability/path ledger` matches the actual frozen repository. Keep real unresolved technical/issue/evidence-hierarchy entries and the non-authoritative boundary unchanged. Then run full exact-head CI and dispatch a fresh blind assurance review on the resulting new SHA.

## Governance status

- implementation claim exists and is owned by `implementation_operations`;
- mandatory implementation handover exists;
- prior FAIL is documented as non-transferable history;
- exact-head implementation evidence comment matches independently verified raw Actions;
- issue #113 is open;
- PR #114 is open/draft/unmerged;
- no self-certification or implementation-side merge observed;
- assurance made no change to the implementation candidate.

## Merge / post-action status

Merge status: `NOT MERGED` because verdict is `FAIL`.  
Actual merge SHA: n/a.  
Exact-main Actions after merge: n/a.  
HF sync after merge: n/a.  
App verification: n/a; candidate is docs/governance/tests only and was not merged.

## Remaining risks

- debt-ledger current-state contradiction must be corrected;
- parent Premium deployed closeout #105/#96 remains intentionally unproven for later reconciliation;
- validation-hierarchy work remains later and must not create a new Evidence Framework;
- Stage-2 Private persistence/egress work remains gated after Repository Convergence.

## Next recommended step

Return only this debt-ledger contradiction to `implementation_operations`, produce a new frozen head with no runtime/product change, run full exact-head regression, and perform a completely fresh blind `governance_release_assurance` review. Do not start Stage-1 technical cleanup in this assurance task.
