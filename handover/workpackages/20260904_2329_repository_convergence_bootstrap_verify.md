# Assurance handover — Repository Convergence Bootstrap verify

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Pull request: #114 — `SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP`  
Reviewed exact PR head: `ea203abb04f008a7e583387242a6f4917c72e591`  
Expected/actual base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Merge-base: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Review mode: fresh blind-first  
Verdict: `FAIL`

## Candidate shape

PR #114 is open, draft, unmerged and mergeable at the reviewed identity. The reviewed head is 16 commits ahead, 0 behind the expected base. The changed-file set is exactly 13 files:

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
12. `tests/test_repository_convergence_bootstrap_contracts.py`
13. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP.md`

No product/runtime source file is changed by the candidate.

## Blind-first source review

Before consulting the implementation handover or implementation conclusions, reviewed in required order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`
5. `AGENTS.md`
6. `DECISION_LOG.md`
7. `RISK_REGISTER.md`
8. canonical SolidPrivacy Execution & Engineering Constitution from the configured Google Doc

Then inspected PR/base/head/merge-base, changed set/diff, governance contracts, relevant existing tests, the new convergence tests and raw exact-head GitHub Actions evidence. The implementation handover was read only after the initial FAIL decision had already been formed.

## Scope and current-truth assessment

The candidate is repository-convergence/governance/documentation/contract-test scoped. No recognizer, review-runtime, Scrub Key, reinsert, export, document transformation, persistence, external-AI, Docker, Streamlit runtime or Hugging Face runtime file is modified.

The five-stage strategic direction is internally coherent:

1. Repository Convergence
2. Scrub Private Application
3. Private Service
4. External Product & Service Assurance
5. Pilot

It does not restore local installer work as the critical path, does not introduce a new Evidence Framework, and does not prematurely introduce platform/multitenancy/API/billing/dashboard architecture or force VPS infrastructure before application completion.

Still-binding product constraints remain materially represented across the current canonical governance set, including mandatory human review; document-first/document-bound Scrub Key and fail-closed wrong-document/key handling; DOCX supported body/table/header/footer and unsupported-content boundaries; side-by-side/review authority; Legal and Zorg profiles; pseudonymisation versus anonymisation claim limits; and preservation of legal/clinical meaning.

The exact pre-convergence `CHANGELOG.md` is preserved as `history/CHANGELOG_PRE_CONVERGENCE_20260904.md` with the same Git blob identity as the baseline changelog. Historical provenance is therefore retained while the new canonical documents are rewritten toward current truth.

## Raw exact-head Actions evidence

Exact reviewed head: `ea203abb04f008a7e583387242a6f4917c72e591`.

- `Tests` run `33920335521`: `completed / failure`.
- job `Python regression tests` (`101176946293`): failed at `python -m pytest -q tests`.
- raw result: `8 failed, 1256 passed in 12.64s`, exit code 1.
- `Issue70 exact-main evidence carrier` run `33920335605`: `completed / success`; this does not substitute for the failed full regression suite.

## Blocking findings

### Finding 1 — HIGH — exact-head release regression is red

Location/evidence:

- GitHub Actions `Tests` run `33920335521` on the exact reviewed PR head.
- `WORKPACKAGES.md` acceptance explicitly requires both the new contract tests and the full exact-head repository regression to pass.
- Eight test failures remain.

Why it matters:

The bootstrap's purpose is repository convergence. A candidate that knowingly leaves the canonical regression contract red has not produced a converged source of truth and cannot satisfy its own release gate. The issue is not cured by a separate green evidence-carrier workflow.

Smallest complete remediation:

Reconcile the eight failing tests deliberately, rerun the complete repository suite on a new exact candidate head, and require fresh independent assurance on that repaired head.

### Finding 2 — HIGH — two new convergence contract tests are themselves inconsistent/brittle

Location:

`tests/test_repository_convergence_bootstrap_contracts.py`

- `test_roadmap_has_only_the_five_current_macro_stages`
- `test_bootstrap_does_not_authorize_source_cloning_or_a_new_evidence_framework`

Concrete evidence:

- The first asserts `roadmap.count(stage) == 1`; the valid Stage 1 name occurs twice because the roadmap contains both the formal stage heading and a later current-execution reference. This tests global string multiplicity rather than the intended invariant of exactly five formal macro-stage headings.
- The second requires the exact lowercase phrase `new evidence framework` in the debt ledger. The ledger semantically forbids framework proliferation but does not contain that exact phrase, so the new test fails on wording rather than authority semantics.

Why it matters:

These are newly introduced release contracts. They fail on the candidate they are supposed to protect and encode accidental prose placement/literal wording rather than the governance invariant. That makes the bootstrap non-self-consistent and creates future pressure to edit documentation to satisfy brittle strings instead of preserving meaning.

Smallest complete remediation:

Make the stage test parse/count only formal `## Stage N — ...` headings and assert the exact ordered five-stage set. Make the evidence-framework/source-clone test assert stable semantic markers or a specific authoritative prohibition without requiring arbitrary duplicate wording in the ledger. Do not change runtime/product code.

### Finding 3 — MEDIUM, release-blocking through the full-suite gate — six legacy documentation-placement tests were not reconciled

Locations:

- `tests/test_mvp_document_fidelity_pr_final_contracts.py::test_document_fidelity_governance_evidence_has_no_duplicate_lines`
- `tests/test_premium_core_flow_ui_realignment_plan.py::test_roadmap_and_workpackages_route_the_new_ui_line_sequentially`
- `tests/test_premium_core_flow_ui_realignment_plan.py::test_decision_log_records_global_view_and_stage_model`
- `tests/test_premium_staged_workspace_decision.py::test_roadmap_makes_staged_workspace_the_urgent_premium_gate`
- `tests/test_premium_staged_workspace_decision.py::test_workpackages_and_decision_log_bind_the_execution_order`
- `tests/test_reinsert_auto_flow_app_verify_closeout.py::test_reinsert_auto_flow_closeout_is_recorded`

Evidence:

These tests still require historical execution headings/workpackage identifiers or exact old copy to remain in current `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md` or `DECISION_LOG.md`. The new convergence model intentionally moves historical provenance out of current execution authority. Review of the current canonical docs shows that the major still-binding underlying product semantics are preserved elsewhere, so these failures appear primarily to be obsolete document-placement/status assertions rather than demonstrated loss of the protected product behavior.

Why it matters:

Repository convergence must explicitly retire/re-home obsolete tests while preserving any still-binding invariant. Leaving them red is not convergence; deleting them blindly would also be unsafe.

Smallest complete remediation:

For each legacy test, identify the still-binding invariant. Rebind a test to the new canonical location/semantic contract when the invariant remains current; retire only the historical placement/status assertion when the underlying behavior is independently protected. Keep the archived/history provenance. Then rerun the entire suite.

## Governance status

- Independent blind-first separation: satisfied.
- Implementation handover read only after initial verdict: satisfied.
- Implementation candidate modified by assurance: no.
- Assurance verdict registered as: `FAIL`.
- Candidate eligible for merge: no.
- Fresh repaired-head assurance required: yes.

## Merge / deployment status

Merge status: `NOT MERGED` by this assurance review.  
Exact-main Actions after merge: `NOT APPLICABLE — no merge performed`.  
GitHub → Hugging Face sync after merge: `NOT APPLICABLE — no merge performed`.  
App verification: `NOT APPLICABLE` for this docs/governance/test-only candidate and no merge was performed.

## Remaining risks

- The exact candidate does not satisfy its own full-regression acceptance gate.
- Legacy documentation-placement tests need deliberate semantic reconciliation; they must not simply be deleted to make CI green.
- Any repaired candidate receives a new SHA and invalidates this exact-head review.
- The user prompt contained `<FINAL_HEAD_SHA>` rather than a concrete SHA. This review therefore binds only the exact PR head independently read from GitHub: `ea203abb04f008a7e583387242a6f4917c72e591`. No later head inherits this verdict.

## Next recommended step

Return the candidate to `implementation_operations` for the smallest test/governance reconciliation only. Keep runtime/product files untouched. Freeze the repaired exact head only after the complete `Tests` workflow is green, then dispatch a fresh blind `governance_release_assurance` review. Do not merge PR #114 on this reviewed head.
