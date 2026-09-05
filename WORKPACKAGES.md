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

Issue: #113  
PR: #114  
Reviewed frozen head: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Merge/main SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Status: **PASS → MERGED → exact-main verified**.

Evidence:

- fresh blind `governance_release_assurance`: PASS on exact reviewed head;
- exact-main `Tests` run `33925330688`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33925330710`: SUCCESS;
- issue #113 closed;
- no product/runtime semantics changed.

---

## WP-CONVERGENCE-02 — Startup invocation retirement — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT
```

Issue: #115  
PR: #116  
Reviewed frozen head: `cbaaa1e4560670116c41ca788786d80d670dcf34`  
Merge/main SHA: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`  
Status: **PASS → MERGED → exact-main verified**.

Outcome:

- Docker starts `presidio_streamlit.py` directly;
- runtime startup no longer invokes `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py`;
- dormant historical patch scripts remain separate later RETIRE candidates;
- no user-visible product semantics changed.

Evidence:

- fresh blind `governance_release_assurance`: PASS;
- exact-main `Tests` run `33929193443`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33929193466`: SUCCESS;
- deployed Space health confirmed Running/serving;
- issue #115 closed.

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
- recognizer-backed recall reporting remains supplemental diagnostic evidence;
- WP22/WP23/WP24 remain supplemental/historical diagnostics rather than release authority;
- no new Evidence Framework, production score threshold or product/runtime behavior was introduced.

Evidence:

- fresh blind `governance_release_assurance`: PASS on exact reviewed head;
- exact-main `Tests` run `33930953130`: SUCCESS, `1268 passed in 11.68s`;
- GitHub→Hugging Face sync run `33930953103`: SUCCESS on exact merge SHA;
- app verification: N/A because no application/runtime/UI behavior changed;
- issue #117 closed.

---

## WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION
```

Role: `implementation_operations`  
Issue: #119  
Branch: `wp/repository-convergence-issue-state-reconciliation`  
Base: `268d967db95d923a73a3979ffce2d0cab586e499`  
Status: **IMPLEMENTATION IN PROGRESS**.

### Proven current-truth defect

GitHub still exposes 18 historical/current Premium/governance issues as open even though their candidate PRs and assurance cycles are mostly superseded or completed. That stale state competes with `main` and the current convergence queue.

Evidence reconstruction shows:

- PR #73 recovery ultimately received exact-head independent PASS and merged; its earlier failed/repaired dispatch tickets are historical;
- Premium contract/state/staged-workspace packages represented by #79/#81/#84/#86/#88/#89 are implemented or superseded by later repaired runtime state;
- PR #104 V2 independently PASSed and merged, resolving the old #93 PASS / #92 FAIL source-state conflict at the repaired candidate level;
- PR #108 marker/compact-placeholder repair independently PASSed and merged;
- PR #111 Dutch-address precision repair independently PASSed and merged;
- the one still-unproven requirement is the **consolidated deployed live-app retest after both PR #108 and PR #111 repairs**.

### Reviewed target disposition

Subject to fresh independent assurance before issue mutation:

```text
KEEP OPEN
#96 — single residual Premium/App-Shell deployed live-verification gate

CLOSE AS COMPLETED / HISTORICAL-SUPERSEDED
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

Issue #96 must be rewritten/updated to current truth: the old source-state assurance conflict is technically superseded by independently PASSed/merged PR #104; marker/compact-display and address findings were repaired by independently PASSed/merged PR #108 and PR #111; only the final consolidated post-repair live retest remains open.

### Safety boundary

- do not close #96 without actual live post-repair evidence;
- issue closure does not erase historical FAIL/INDETERMINATE/PASS provenance;
- no product/runtime/UI/recognizer/review/export/Scrub Key/reinsert semantics change;
- no Stage-2 persistence/egress work;
- no new permanent issue ledger or tracking framework.

### Acceptance

- exact current issue inventory is independently reconstructed;
- all proposed closures are supported by candidate/assurance/merge evidence, not age alone;
- exactly one residual Premium gate remains open: #96;
- repository controls reflect PR #118 as completed and WP-CONVERGENCE-04 as the only current executable package;
- full exact-head `Tests` workflow is green;
- fresh blind `governance_release_assurance` PASSes the exact candidate before merge and issue-state mutation;
- post-merge exact-main evidence is verified.

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
