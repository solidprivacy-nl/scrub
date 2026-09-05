# SolidPrivacy Scrub — Current Workpackages

**Current execution line:** Repository Convergence  
**Updated:** 2026-09-06 Europe/Amsterdam

This file contains the **current executable queue only**. Historical package detail belongs in `CHANGELOG.md`, `handover/workpackages/`, `workpackage_claims/` and Git history.

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

Implementation cannot certify its own consequential candidate. Governance cannot silently repair what it reviews.

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

The exact SHA remains recovery authority. No duplicate source tree was created.

---

## WP-CONVERGENCE-01 — Bootstrap/current-truth audit — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP
```

Issue #113 closed; PR #114 merged.  
Reviewed head: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Merge/main: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Status: **PASS → MERGED → exact-main verified**.

---

## WP-CONVERGENCE-02 — Startup invocation retirement — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT
```

Issue #115 closed; PR #116 merged.  
Reviewed head: `cbaaa1e4560670116c41ca788786d80d670dcf34`  
Merge/main: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`  
Status: **PASS → MERGED → exact-main verified**.

Docker now starts `presidio_streamlit.py` directly. Historical patch scripts remain dormant separate RETIRE candidates.

---

## WP-CONVERGENCE-03 — Validation hierarchy clarification — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION
```

Issue #117 closed; PR #118 merged.  
Reviewed head: `37de6859ed5b17f4767c463f6db73085ce0d4b56`  
Merge/main: `268d967db95d923a73a3979ffce2d0cab586e499`  
Status: **PASS → MERGED → exact-main verified**.

D045 remains accepted validation authority:

```text
.github/workflows/tests.yml
→ python -m pytest -q tests
→ exact candidate/main SHA evidence
```

Focused capability suites remain evidence inside the full suite; recognizer-backed recall and WP22/WP23/WP24 remain supplemental diagnostics. No new Evidence Framework or score-based production gate exists.

---

## WP-CONVERGENCE-04R — Governance sequencing recovery — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY
```

Issue #121 closed; assurance #123 closed after later WP04 reconciliation; PR #122 merged.  
Reviewed head: `8565af4e9f579b3a975c6122668f6511a9df627a`  
Merge/main: `14baceb97b274de6ef35c42ce48441c4e74c5f08`  
Status: **PASS → MERGED → exact-main verified**.

The premature PR #120 merge remains visible in Git history; no force reset or history rewrite occurred.

---

## WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — COMPLETED

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION
```

Issue #119 closed; assurance #126 closed; PR #124 merged.  
Reviewed head: `ce021443303cfa11de12f3273f872b2d027da5db`  
Merge/main SHA: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`  
Status: **PASS → GUARDED MERGE → exact-main verified → administrative reconciliation confirmed**.

Exact post-merge evidence:

```text
Tests run 33997889522
1279 passed in 14.51s
SUCCESS

GitHub → Hugging Face sync run 33997889554
SUCCESS
14baceb..2d4ab04 HEAD -> main
```

Administrative outcome:

- historical/completed/superseded issues #74 #75 #76 #77 #79 #81 #84 #86 #88 #89 #98 #100 #105 #106 #107 #109 #112 #123 are closed;
- #119 and assurance #126 are closed after readback;
- historical PASS/FAIL/INDETERMINATE provenance remains intact;
- **#96 is the sole remaining open product-facing issue** and remains intentionally open because its consolidated deployed live-app retest is still unproven.

---

## WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_CONSOLIDATED_LIVE_APP_VERIFY_CLOSEOUT
```

Role: `implementation_operations` for current-truth alignment and evidence coordination; live-app outcome must be independently evidenced.  
Issue: #96 — OPEN  
Exact starting main/base: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`  
Alignment branch: `wp/repository-convergence-live-app-gate-alignment`  
Status: **CURRENT — deployed live-app evidence pending; no runtime/product change authorized by this package**.

### Why this is current

The underlying repair chains are already complete:

- PR #104 V2 fixed Standard↔Expert source/analysis/review-state preservation and received fresh independent PASS before merge;
- PR #108 fixed processed-text marker offsets and compact bound-placeholder rendering and received fresh independent PASS before merge;
- PR #111 fixed Dutch address-span overcapture and received fresh independent PASS before merge.

Their exact-main CI and GitHub→Hugging Face synchronization are necessary deployment evidence, but they do not prove the final deployed user-facing behavior as one consolidated flow.

### Required deployed verification

Using only synthetic/approved material, verify the deployed Hugging Face Space and record the exact deployed Git SHA, test date and concrete outcomes for all of the following:

1. staged Standard/Expert core flow remains coherent and operates on current authoritative state;
2. marker/highlight offsets remain exact with leading whitespace/newlines;
3. strict document-bound placeholders render compactly in review without token fragmentation or full binding-token leakage;
4. `Polderweg 8` and representative legitimate Dutch address forms resolve without adjacent ordinary-word overcapture;
5. source/review/export lineage remains fail-closed and explicit human review remains required;
6. no test result is promoted into a claim of perfect anonymisation, perfect recall or production safety.

The coordinator/live test lineage that originally exposed the regressions included the synthetic/professional-style sentence around:

```text
Rapport van het inspectiebezoek aan Stichting Amsta, locatie Polderweg 8 in Amsterdam ...
```

and address contexts including:

```text
Beschrijving Polderweg 8
De inspectie bezoekt Polderweg 8
Nu Polderweg 8 de
Op Polderweg 8
Polderweg 8 een
Polderweg 8 en
Polderweg 8 in
Polderweg 8 is
Polderweg 8 na
Polderweg 8 op
```

The privacy-sensitive address is `Polderweg 8`; surrounding grammar must remain professional context rather than becoming part of the address entity.

### Action boundary

- Do not close #96 from CI/HF sync alone.
- Do not alter runtime/UI/recognizers merely to manufacture a passing verification result.
- If deployed verification finds a defect, create one narrow root-cause repair package and keep #96 open.
- If deployed verification passes all required behavior, record the evidence on #96 and close #96 only after the live outcome is independently confirmed.
- App verification remains a distinct evidence class from repository regression and deployment synchronization.

### Acceptance

- WP04 is represented as completed and no longer current;
- #96 is the sole current product-facing gate;
- the deployed verification covers marker offsets, compact placeholders, address precision, Standard/Expert state, fail-closed review/export lineage and mandatory human review;
- exact deployed SHA/date/results are recorded;
- #96 closes only on actual live PASS;
- no product/runtime semantics change in this alignment package;
- Stage 2 remains blocked until convergence finalization and independent clean-baseline assurance.

---

## Candidate later package — dormant patch-artifact retirement

`fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` are no longer runtime startup dependencies after WP-CONVERGENCE-02. Their files and historical patch-specific tests may be retired only after a separate evidence review proves there is no remaining diagnostic/current-contract value. Do not mass-delete by filename pattern.

This is **not** current work and does not supersede WP-CONVERGENCE-05.

---

## WP-CONVERGENCE-FINAL — Final canonical documentation and issue alignment

Status: **BLOCKED on WP-CONVERGENCE-05 outcome**.

After the residual live gate is resolved, perform documentation Pass B so canonical project files and active GitHub issue state match resulting implementation. The temporary debt ledger then becomes explicitly historical/non-authoritative evidence.

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
