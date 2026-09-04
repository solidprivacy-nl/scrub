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

Outputs now authoritative on `main` include the five-stage roadmap, one-current-queue workpackage model, D044, current risk alignment and the temporary capability-level convergence ledger.

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

- Docker now starts `presidio_streamlit.py` directly;
- runtime startup no longer invokes `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py`;
- existing port/address/XSRF/CORS flags remain unchanged;
- dormant historical patch scripts remain separate later RETIRE candidates;
- no user-visible product semantics changed.

Evidence:

- fresh blind `governance_release_assurance`: PASS on exact reviewed head;
- exact-main `Tests` run `33929193443`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33929193466`: SUCCESS;
- deployed Space health confirmed Running/serving;
- issue #115 closed.

---

## WP-CONVERGENCE-03 — Validation hierarchy clarification — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION
```

Role: `implementation_operations`  
Issue: #117  
Branch: `wp/repository-convergence-validation-hierarchy`  
Base: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`  
Status: **IMPLEMENTATION IN PROGRESS**.

### Proven ambiguity

Multiple mature evidence generations exist, but their authority differs. Historical language could be read as if diagnostic report workflows were independent release gates.

Source reconstruction shows:

- `.github/workflows/tests.yml` runs the complete committed `tests/` suite and is the current exact-SHA release regression gate;
- focused Phase-6, Scrub Key, document, Zorg, recognizer and Premium/AppTest suites are capability-level product regression evidence within that full gate;
- `recall_benchmark_report.py` explicitly declares `diagnostic_only`, `production_gate=False`, `thresholds_enforced=False`;
- WP22 scores supplied predictions without invoking recognizers;
- WP23/WP24 are report-only/non-gating and carry coverage limitations.

### Smallest complete fix

- record binding validation authority in D045;
- align ROADMAP and the temporary debt ledger;
- add one narrow contract test grounded in actual workflow/source metadata;
- do not change runners, corpus data, thresholds or product/runtime behavior;
- do not delete historical diagnostic helpers merely because they are non-authoritative.

### Acceptance

- one release regression gate is unambiguous: exact-SHA full `Tests` workflow;
- capability suites remain first-class evidence without competing merge authority;
- recall benchmark/report is supplemental diagnostic evidence;
- WP22/WP23/WP24 chain is supplemental/historical diagnostic, not release authority;
- no production threshold or safety claim is introduced;
- full exact-head `python -m pytest -q tests` is green;
- fresh independent `governance_release_assurance` returns PASS before merge;
- post-merge exact-main Tests and GitHub→HF sync are verified.

---

## Candidate next package — current GitHub issue/state reconciliation

After WP-CONVERGENCE-03, reconstruct stale open Premium/governance issues against actual `main`; close only what current machine/assurance evidence proves complete. Preserve the residual consolidated deployed verification gate for #105/#96 unless actual evidence proves it was performed.

## Candidate later package — dormant patch-artifact retirement

`fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` are no longer runtime startup dependencies after WP-CONVERGENCE-02. Their actual files and historical patch-specific tests may be retired only after a separate evidence review proves there is no remaining diagnostic/current-contract value. Do not mass-delete by filename pattern.

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
