# SolidPrivacy Scrub — Current Workpackages

**Current execution line:** Repository Convergence  
**Updated:** 2026-09-04 Europe/Amsterdam

This file contains the **current executable queue only**.

Historical package status belongs in `CHANGELOG.md`, `handover/workpackages/`, `workpackage_claims/` and Git history. Old completed candidate cycles must not remain stacked here as competing “current status override” sections.

For strategy, read `ROADMAP.md`.

---

## Operating rules

Consequential work uses the existing two-role model:

```text
implementation_operations
→ exact release candidate
→ governance_release_assurance blind reconstruction
→ PASS | FAIL | INDETERMINATE
→ authorized action
→ exact-main confirmation
```

Implementation cannot certify its own candidate. Governance cannot silently repair what it reviews.

Work in small coherent root-cause packages. Do not create one giant convergence PR. Also do not split trivial edits into ritual packages with no independent risk boundary.

Shared Streamlit/review/export/runtime surfaces remain sequential when a package touches them.

---

# Stage 1 — Repository Convergence — ACTIVE

Normal new feature development is paused until `SCRUB_REPOSITORY_CONVERGED`.

Privacy/security defects discovered during convergence may interrupt the pause as narrow root-cause repairs.

## WP-CONVERGENCE-00 — Preserve exact starting state

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_BASELINE_PRESERVATION
```

Status: **COMPLETED AS EVIDENCE / NO PRODUCT CHANGE**

Authoritative pre-convergence baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Baseline evidence at package start:

- GitHub `main` = exact SHA above;
- exact-main `Tests` = success;
- exact-main `Sync to Hugging Face Space` = success;
- no in-repository source clone was created;
- exact SHA is the recovery authority.

A human-readable tag may be added later if useful, but a tag name does not replace the SHA as provenance.

---

## WP-CONVERGENCE-01 — Bootstrap, current-truth audit and strategy reset — CURRENT

Canonical title:

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP
```

Role: `implementation_operations`  
Issue: #113  
Branch: `wp/repository-convergence-bootstrap`  
Dependency: WP-CONVERGENCE-00 evidence recorded.

### Goal

Reconstruct the active/reachable current system and replace stale strategic/execution routing with one Repository Convergence line **without changing runtime product semantics**.

### Required outputs

- temporary capability/current-truth ledger using:
  `CANONICAL | RECONCILE | RETIRE | VARIANT-SPECIFIC`;
- concise five-stage `ROADMAP.md`;
- this one-current-queue `WORKPACKAGES.md`;
- product-direction alignment in `PROJECT_PROMPT.md` and `AGENTS.md` while preserving governance/safety rules;
- Repository Convergence / Scrub Private decision record;
- current risk alignment without weakening existing critical risks;
- CHANGELOG entry preserving history;
- contract tests protecting the new source-of-truth model;
- implementation claim and handover.

### Known audit findings — evidence only, not runtime authorization

The ledger currently identifies:

1. Premium staged workspace/state, review authority, Scrub Key/reinsert, Legal/Zorg recognition and document handling as current canonical capability.
2. Persistent remembered replacements as `VARIANT-SPECIFIC`: potentially valid Local behavior but incompatible with the future Private no-content-persistence boundary.
3. Azure AI Language and OpenAI/Azure synthesis as `VARIANT-SPECIFIC`: current Expert functionality but incompatible with the Private no-third-party-document-processing baseline.
4. Content-bearing synthesis prompt logging as a future Private blocker.
5. legacy Streamlit source-patch scripts as `RETIRE` candidates: Docker still invokes them, but current Premium/direct-source markers make them exit without mutating source.
6. multiple benchmark/evidence generations requiring authority clarification, not replacement with a new framework.
7. stale/open historical GitHub issue states requiring reconciliation against current main.

### Safety boundary

This package must not change:

- recognizers/profile semantics;
- thresholds;
- review/include authority;
- export bytes/names/MIME;
- Scrub Key schema/binding/lifecycle;
- reinsert;
- document-processing behavior;
- runtime dependencies;
- Docker/Streamlit runtime behavior;
- Hugging Face product behavior;
- mandatory human review.

### Acceptance

- candidate diff remains documentation/governance/tests/administration only;
- no active product/runtime source changed;
- new contract tests pass;
- full exact-head repository regression passes;
- fresh independent `governance_release_assurance` returns PASS before merge;
- after merge, exact-main Tests are green;
- HF sync behavior is checked according to path-ignore rules; no UI/app verification is required because product behavior is unchanged.

---

## WP-CONVERGENCE-02..N — Evidence-backed technical/current-state cleanup — DERIVED, NOT PRE-INVENTED

Status: **NOT YET AUTHORIZED AS A FIX LIST**

The audit determines which packages actually exist.

A technical package may start only when WP-CONVERGENCE-01 has established evidence that the targeted active path is:

- duplicate;
- contradictory;
- dead/unreachable;
- privacy/security defective;
- obsolete compatibility machinery;
- materially burdensome;
- evidence-authority ambiguous;
- or otherwise a concrete current problem.

Likely candidate root-cause clusters, subject to bootstrap acceptance and fresh current verification:

### Candidate A — legacy startup-patch retirement

Potential scope:

- prove current Premium/direct-source app no longer requires `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py` at startup;
- remove obsolete Docker invocation and dead mutation machinery if safe;
- update/remove tests that protect only retired implementation details while retaining product-behavior contracts.

Do not combine with Private persistence/egress work.

### Candidate B — validation hierarchy clarification

Potential scope:

- determine canonical release role of recognizer-backed recall workflow, Phase-6 E2E, Zorg evidence, Scrub Key/document suites and Premium AppTests;
- classify older scorecard/residual-risk helpers as canonical, supplemental or historical based on current reachability and coverage;
- remove/de-authorize only genuine competing authority;
- build no new Evidence Framework and introduce no arbitrary production threshold.

### Candidate C — current GitHub issue/state reconciliation

Potential scope:

- reconstruct open historical candidate/assurance issues against actual main;
- close stale completed cycles with evidence;
- preserve or consolidate any genuinely outstanding current verification gate;
- do not claim unperformed live verification.

### Explicitly Stage 2, not Stage 1 cleanup by default

The following are product-line trust-boundary adaptations and should normally occur **after** the clean baseline unless current evidence proves they are already harmful to the reference environment:

- removing server-side replacement-memory persistence from Scrub Private;
- removing Azure/OpenAI third-party document processing from Scrub Private;
- removing associated external-only dependencies;
- enforcing Private no-content-log contracts.

This separation preserves useful full-feature functionality while convergence establishes a clean shared baseline.

---

## WP-CONVERGENCE-FINAL — Final canonical documentation and issue alignment

Status: **BLOCKED on evidence-backed technical packages**

Goal:

- perform documentation Pass B after technical convergence;
- make `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `DECISION_LOG.md`, `RISK_REGISTER.md`, `CHANGELOG.md`, release notes where relevant, and active GitHub issue state match the resulting implementation;
- ensure the temporary debt ledger is clearly non-authoritative historical evidence after closeout.

Acceptance:

- no stacked obsolete current queues;
- no old local-first delivery route presented as active;
- all material current architecture decisions recorded once;
- live risks remain visible;
- historical CHANGELOG/handover provenance preserved.

---

## WP-CONVERGENCE-VERIFY — Independent clean-baseline assurance

Status: **BLOCKED on WP-CONVERGENCE-FINAL**

Role: `governance_release_assurance`

Required reconstruction:

- exact candidate SHA/tree;
- current active runtime paths;
- current canonical validation hierarchy;
- relevant full test/evidence output;
- documentation/current issue consistency;
- absence of known contradictory active authority;
- exact-main Actions after authorized merge/action;
- GitHub→HF synchronization evidence where applicable.

Required decision:

```text
SCRUB_REPOSITORY_CONVERGED: PASS | FAIL | INDETERMINATE
```

Only PASS permits Stage 2 to start.

---

# Stage 2 — Scrub Private Application — BLOCKED

Entry gate:

```text
SCRUB_REPOSITORY_CONVERGED
```

Expected outcomes, not pre-authorized implementation packages:

- no intentional persistent server-side customer document content/mappings/Scrub Keys;
- no persistent replacement-memory feature in the Private line;
- no third-party document-processing route in Private;
- no content-bearing application logs;
- existing recognition/review/Scrub Key/document/evidence core retained;
- synthetic deployed Legal/Zorg end-to-end validation on HF.

Exit:

```text
SCRUB_HF_APPLICATION_COMPLETE
```

HF remains a synthetic/approved-test application-validation surface, not a confidential-production infrastructure assurance environment.

---

# Stage 3 — Private Service — BLOCKED

Entry gate:

```text
SCRUB_HF_APPLICATION_COMPLETE
```

Add only required service controls: proven OIDC/customer identity, production runtime hardening, content/control-plane separation, customer isolation, storage/logging/egress controls and minimal operations.

Exit:

```text
SCRUB_PRIVATE_SERVICE_CANDIDATE
```

---

# Stage 4 — External Product & Service Assurance — BLOCKED

Separate from internal `governance_release_assurance`.

Reuse product-effectiveness evidence and independently validate service privacy/security properties.

---

# Stage 5 — Pilot — BLOCKED

Initial bias:

```text
Legal → evidence-backed improvement → Zorg → earned scale
```

Do not open generalized platform/multitenancy/API/batch/dashboard work without pilot/customer evidence.
