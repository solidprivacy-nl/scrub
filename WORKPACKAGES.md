# SolidPrivacy Scrub — Current Workpackages

**Current execution line:** Repository Convergence  
**Updated:** 2026-09-05 Europe/Amsterdam

This file contains the **current executable queue only**. Historical package status belongs in `CHANGELOG.md`, `handover/workpackages/`, `workpackage_claims/` and Git history.

For strategy, read `ROADMAP.md`.

---

## Operating rules

Consequential work follows:

```text
implementation_operations
→ exact release candidate
→ governance_release_assurance blind reconstruction
→ PASS | FAIL | INDETERMINATE
→ authorized action
→ exact-main confirmation
```

Implementation cannot certify its own candidate. Governance cannot silently repair what it reviews. Workpackages should represent one coherent root-cause cluster that can be independently understood, tested and rolled back.

Shared Streamlit/review/export/runtime surfaces remain sequential when a package touches them.

---

# Stage 1 — Repository Convergence — ACTIVE

Normal feature development remains paused until:

```text
SCRUB_REPOSITORY_CONVERGED
```

## WP-CONVERGENCE-00 — Preserve exact starting state — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_BASELINE_PRESERVATION
```

Authoritative pre-convergence baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

The exact SHA is the recovery authority. No duplicate source tree was created.

---

## WP-CONVERGENCE-01 — Bootstrap/current-truth audit — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP
```

Issue: #113 — closed  
PR: #114 — merged  
Reviewed frozen head: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Merge/main SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Status: **PASS → MERGED → exact-main verified**.

---

## WP-CONVERGENCE-02 — Startup invocation retirement — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT
```

Issue: #115 — closed  
PR: #116 — merged  
Reviewed frozen head: `cbaaa1e4560670116c41ca788786d80d670dcf34`  
Merge/main SHA: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`  
Status: **PASS → MERGED → exact-main verified**.

Outcome: Docker starts `presidio_streamlit.py` directly; the historical patch scripts remain dormant separate RETIRE candidates.

---

## WP-CONVERGENCE-03 — Validation hierarchy clarification — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION
```

Issue: #117 — closed  
PR: #118 — merged  
Reviewed frozen head: `37de6859ed5b17f4767c463f6db73085ce0d4b56`  
Merge/main SHA: `268d967db95d923a73a3979ffce2d0cab586e499`  
Status: **PASS → MERGED → exact-main verified**.

Outcome:

- D045 establishes one exact-SHA release regression gate: `.github/workflows/tests.yml` → `python -m pytest -q tests`;
- focused product/domain suites remain capability regression evidence within the full suite;
- recognizer-backed recall reporting and WP22/WP23/WP24 remain supplemental diagnostics;
- no new Evidence Framework, production score threshold or product/runtime behavior was introduced.

---

## WP-CONVERGENCE-04R — Governance sequencing recovery — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY
```

Issue: #121 — closed  
Assurance issue: #123 — PASS recorded; intentionally left open by its stop rule and now classified as completed historical administration for WP04 reconciliation  
PR: #122 — merged  
Reviewed frozen head: `8565af4e9f579b3a975c6122668f6511a9df627a`  
Merge/main SHA: `14baceb97b274de6ef35c42ce48441c4e74c5f08`  
Status: **PASS → MERGED → exact-main verified**.

Outcome:

- the premature PR #120 merge remains preserved in Git history rather than force-reset;
- issue #74 was restored to OPEN before recovery assurance;
- failed PR #120 candidate-specific active authority was removed while history was preserved;
- accepted PR #118/D045 truth was retained;
- #96 remained OPEN and its consolidated deployed live-app retest remained unproven;
- no WP04 issue reconciliation was executed during recovery.

Exact-main recovery evidence:

```text
Tests run 33966351441 / job 101307057966
1272 passed in 14.44s
SUCCESS

GitHub → Hugging Face sync run 33966351286 / job 101307057815
SUCCESS on exact main 14baceb97b274de6ef35c42ce48441c4e74c5f08
```

---

## WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION
```

Role: `implementation_operations`  
Issue: #119 — open  
Branch: `wp/repository-convergence-issue-state-reconciliation-v2`  
Exact starting main/base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`  
Status: **IMPLEMENTATION IN PROGRESS — current open-issue inventory corrected before assurance**.

### Proven current-truth defect

After the governed recovery, GitHub still exposes historical Premium/governance worker/candidate issues as open. The substantive evidence reconstruction from the failed PR #120 cycle remains useful evidence, but PR #120 has no pre-action assurance authority and cannot be reused as the release decision for this retry.

A fresh current-issue inventory also shows recovery-assurance issue #123 still OPEN. That is factually consistent with #123's explicit PASS stop rule, but once recovery is complete it is no longer current executable work. Because WP04 exists specifically to reconcile current GitHub issue state, #123 belongs in the evidence-backed historical closure set rather than being left as stale open governance state.

Current reviewed target:

```text
KEEP OPEN
#96 — residual Premium/App-Shell deployed live-verification gate

CLOSE AS COMPLETED / HISTORICAL-SUPERSEDED AFTER NEW WP04 PASS + MERGE + EXACT-MAIN VERIFICATION
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
#123
```

#96 must remain open. Its description may be reconciled to current truth only after the new WP04 candidate has independently PASSed, merged, and exact-main verification succeeds. Current technical truth remains:

- PR #104 V2 independently PASSed and merged, superseding the old PR #85 exact-head source/state conflict at the repaired implementation level;
- PR #108 marker/compact-placeholder repair independently PASSed and merged;
- PR #111 Dutch-address precision repair independently PASSed and merged;
- the consolidated deployed live-app retest after both repairs **remains unproven**.

### Action fence

No target issue mutation is authorized during implementation or pre-verdict assurance.

Required order for this retry:

```text
new exact WP04 candidate on 14baceb...
→ full exact-head Tests
→ fresh blind governance_release_assurance
→ PASS
→ guarded merge of the exact reviewed head
→ exact-main Tests + GitHub→HF sync/path-ignore verification
→ only then execute the reviewed issue disposition
→ read back #74/#75/#76/#77/#79/#81/#84/#86/#88/#89/#98/#100/#105/#106/#107/#109/#112/#123 as closed
→ read back #96 as open with current residual-gate wording
→ close #119 only after administrative outcome confirmation
```

The active assurance-dispatch issue for the final frozen candidate is procedural current work, not part of this pre-verdict historical close set; it closes itself only after its own PASS/post-merge closeout procedure completes.

This sequence deliberately makes post-merge exact-main confirmation a prerequisite for issue mutation, preventing recurrence of the PR #120 ordering defect.

### Safety boundary

- do not close #96 without actual consolidated post-repair live-app evidence;
- do not mutate any of the 18 target issue states before the new exact candidate receives fresh PASS and merges;
- issue closure never erases historical FAIL/INDETERMINATE/PASS provenance;
- no product/runtime/UI/recognizer/review/export/Scrub Key/reinsert semantics change;
- no Stage-2 persistence/egress work;
- no new permanent issue ledger or tracking framework.

### Acceptance

- recovery PR #122 is independently confirmed complete and is not treated as WP04 assurance;
- exactly one current executable workpackage is WP-CONVERGENCE-04;
- exact 18-close/1-keep disposition is contract-checked;
- completed recovery-assurance issue #123 is classified as historical administration, not current release authority;
- #96 remains excluded from the closure set and its consolidated live-app gate remains explicitly unproven;
- full exact-head `Tests` is green;
- a genuinely fresh blind `governance_release_assurance` PASSes the new candidate before merge;
- guarded merge uses the exact reviewed head;
- post-merge exact-main Tests and HF sync/path-ignore behavior are verified before any target issue mutation;
- final issue-state readback matches the reviewed disposition;
- no runtime/product semantics change.

---

## Candidate later package — dormant patch-artifact retirement

`fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` are no longer runtime startup dependencies after WP-CONVERGENCE-02. Their files and historical patch-specific tests may be retired only after a separate evidence review proves there is no remaining diagnostic/current-contract value. Do not mass-delete by filename pattern.

### Stage 2 boundary — not Stage 1 cleanup by default

The following are Scrub Private product-line adaptations and remain deferred until the clean shared baseline unless a present defect independently forces a narrow repair:

- remove server-side replacement-memory persistence from Private;
- remove Azure/OpenAI third-party document processing from Private;
- remove associated external-only dependencies;
- enforce no-content-log contracts.

---

## WP-CONVERGENCE-FINAL — Final canonical documentation and issue alignment

Status: **BLOCKED on evidence-backed Stage 1 packages**.

Perform documentation Pass B only after technical/current-state convergence. Canonical project files and active GitHub issue state must then match the resulting implementation; the temporary debt ledger becomes clearly historical/non-authoritative evidence.

---

## WP-CONVERGENCE-VERIFY — Independent clean-baseline assurance

Status: **BLOCKED on WP-CONVERGENCE-FINAL**.  
Role: `governance_release_assurance`.

Required decision:

```text
SCRUB_REPOSITORY_CONVERGED: PASS | FAIL | INDETERMINATE
```

Only PASS opens Stage 2.

---

# Stage 2 — Scrub Private Application — BLOCKED

Entry gate: `SCRUB_REPOSITORY_CONVERGED`.

Expected outcomes: no intentional persistent server-side document content/mappings/Scrub Keys, no persistent replacement memory in Private, no third-party document-processing route, no content-bearing application logs, existing product core retained, and deployed synthetic Legal/Zorg end-to-end validation on Hugging Face.

Exit: `SCRUB_HF_APPLICATION_COMPLETE`.

Hugging Face remains an application-validation surface for synthetic/approved material, **not the final confidential-production trust environment**.

---

# Stage 3 — Private Service — BLOCKED

Entry gate: `SCRUB_HF_APPLICATION_COMPLETE`.

Add only required service controls: proven OIDC/customer identity, production runtime hardening, content/control-plane separation, customer isolation, storage/logging/egress controls and minimal operations.

Exit: `SCRUB_PRIVATE_SERVICE_CANDIDATE`.

---

# Stage 4 — External Product & Service Assurance — BLOCKED

Separate from internal `governance_release_assurance`. Reuse product-effectiveness evidence and independently validate service privacy/security properties.

---

# Stage 5 — Pilot — BLOCKED

Initial bias:

```text
Legal → evidence-backed improvement → Zorg → earned scale
```

Do not open generalized platform/multitenancy/API/batch/dashboard work without pilot/customer evidence.
