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

## WP-CONVERGENCE-02..N — Evidence-backed technical/current-state cleanup — DERIVED, NOT PRE-INVENTED

Only audit-proven root-cause clusters may become implementation packages.

### WP-CONVERGENCE-02 — Startup invocation retirement — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT
```

Role: `implementation_operations`  
Issue: #115  
PR: #116  
Branch: `wp/repository-convergence-startup-invocation-retirement`  
Base: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Status: **IMPLEMENTATION IN PROGRESS**.

#### Proven root cause

The current direct-source app already contains the Premium shell and reinsert UI. The two historical startup patch scripts exit without mutation when they encounter those direct-source markers, yet Docker still invoked both before every Streamlit start.

#### Smallest complete fix

- remove only the Docker pre-start invocation of `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py`;
- start Streamlit directly with the existing port/address/XSRF/CORS flags unchanged;
- rebind Docker-specific tests from historical patch ordering to the current no-runtime-mutation invariant;
- keep both historical patch scripts and their broader historical tests for a later evidence-based retirement decision.

#### Explicit non-scope

No change to:

- `presidio_streamlit.py` user-visible behavior;
- recognizers/profiles/thresholds;
- review/export semantics;
- Scrub Key/reinsert semantics;
- persistence/external AI paths;
- dependencies or unrelated Docker hardening;
- historical patch-script deletion.

#### Acceptance

- neither patch script is invoked at runtime startup;
- direct Streamlit command retains existing server flags;
- focused/current startup contracts are green;
- full exact-head `python -m pytest -q tests` is green;
- changed-file scope remains root-cause narrow;
- fresh independent `governance_release_assurance` returns PASS before merge;
- post-merge exact-main Tests and GitHub→HF sync are verified.

### Candidate next package — validation hierarchy clarification

After WP-CONVERGENCE-02, verify and document which existing validation paths are:

```text
CANONICAL RELEASE VALIDATION
SUPPLEMENTAL DIAGNOSTIC
HISTORICAL / SUPERSEDED
```

Expected scope includes recognizer-backed recall workflow, Phase-6 E2E, Zorg evidence, Scrub Key/document suites, Premium AppTests and older scorecard/residual-risk helpers. Build **no new Evidence Framework** and invent no arbitrary production threshold.

### Candidate next package — current GitHub issue/state reconciliation

Reconstruct stale open Premium/governance issues against actual `main`; close only what current machine/assurance evidence proves complete. Preserve the residual consolidated deployed verification gate for #105/#96 unless actual evidence proves it was performed.

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
