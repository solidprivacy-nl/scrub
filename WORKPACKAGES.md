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

## WP-CONVERGENCE-04R — Governance sequencing recovery — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY
```

Role: `implementation_operations`  
Issue: #121  
Branch: `wp/repository-convergence-issue-state-reconciliation-governance-recovery`  
Base/current main at start: `fd69294c67a59bb150f5d4a637daad2607c14077`  
Status: **IMPLEMENTATION IN PROGRESS**.

### Proven governance defect

PR #120 contained the intended WP04 issue-state reconciliation candidate, but the required release order was violated:

```text
candidate 1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a
→ merged prematurely as fd69294c67a59bb150f5d4a637daad2607c14077
→ issue #74 closed prematurely
→ fresh blind assurance later returned FAIL
```

The assurance finding is about the missing **pre-merge/pre-mutation independent PASS**. Green PR/main CI and technically correct merge parents cannot retroactively satisfy that ordering control.

### Recovery already applied outside the candidate

Issue #74 has been reopened with explicit governance-recovery provenance. This only restores truthful pre-reconciliation administrative state; it does not rewrite the historical PR #73 assurance evidence or declare #74 substantively current work.

### Smallest complete repository recovery

- preserve Git history; no force reset/force push;
- preserve accepted PR #118/D045 facts;
- remove the prematurely adopted WP04-specific claim/test/handover from the active tree while Git retains provenance;
- remove the failed PR #120 issue-disposition model as current executable authority;
- record the sequencing FAIL and this recovery in current-control docs;
- keep #96 open as the residual unproven live-app gate;
- run full exact-head Tests;
- require fresh blind independent PASS **before** merging this recovery candidate.

### Acceptance

- exactly one current executable workpackage is this recovery package;
- issue #74 remains open until a later properly assured reconciliation acts on it;
- no other historical issue is mutated by recovery;
- D045 remains accepted/independently assured/merged;
- #96 remains open and the consolidated deployed live-app retest remains unproven;
- no product/runtime/UI behavior changes;
- full exact-head `Tests` is green;
- fresh blind `governance_release_assurance` PASS precedes recovery merge;
- post-merge exact-main evidence is verified before any new WP04 candidate is created.

---

## WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — BLOCKED ON 04R

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION
```

Issue: #119 — open.

The substantive reconstruction remains a useful finding, not current action authority:

```text
KEEP OPEN
#96 — residual Premium/App-Shell deployed live-verification gate

POTENTIAL FUTURE CLOSE SET
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

A **new** WP04 candidate must be created from the post-recovery exact `main` after WP-CONVERGENCE-04R receives independent PASS, merges normally and is exact-main verified. PR #120 and its post-merge CI may remain provenance but may not be reused as the pre-action assurance decision for that future candidate.

Safety boundary:

- do not close #96 without actual consolidated post-repair live-app evidence;
- do not close any of the 17 issues before a future fresh WP04 PASS;
- issue closure never erases historical FAIL/INDETERMINATE/PASS provenance.

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
