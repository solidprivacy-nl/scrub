# SolidPrivacy Scrub — Product & Development Roadmap

This document is the strategic roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` — current executable queue, dependencies and verification gates;
- `RISK_REGISTER.md` — current privacy, security and product risks;
- `DECISION_LOG.md` — accepted architecture/product decisions;
- `CHANGELOG.md` — historical implementation record;
- `PROJECT_PROMPT.md` — worker/governance rules.

Last strategy reset: 2026-09-04 — Repository Convergence becomes the immediate execution priority before further normal feature development. After convergence, `main` becomes the active Scrub Private development line. Local/offline functionality remains recoverable and may become a separate active product only if a later business requirement justifies it.

---

## 1. Product objective

Scrub helps professionals create reviewed pseudonymised working copies of confidential documents while preserving useful legal and clinical meaning.

The product must:

- detect and pseudonymise sensitive values;
- preserve professional context;
- keep meaningful human review mandatory where required;
- allow users to correct missed values;
- support controlled re-identification through a sensitive Scrub Key;
- preserve supported document structure and expose hygiene limitations;
- make residual risk visible rather than imply perfect automatic detection;
- ultimately run as a managed private service with a defensible content-handling boundary.

Core workflow:

```text
Scrub → Review → Scrub Key → AI / external use → Reinsert → Export → Audit
```

Scrub is primarily a pseudonymisation/privacy-processing product. A re-linkable Scrub Key means the output remains re-identifiable and must not be marketed as guaranteed irreversible anonymisation.

---

## 2. Existing risk priorities remain binding

Repository Convergence does not demote the existing privacy/product risks.

Highest priorities remain:

1. false negatives / missed sensitive data;
2. Scrub Key leakage, mismatch or misuse;
3. hidden document content and metadata leakage;
4. placeholder corruption during external/AI roundtrip;
5. review/state defects that can expose stale or insufficiently reviewed output;
6. domain-specific under-detection or harmful over-masking, especially Legal and Zorg;
7. service trust-boundary failures such as content persistence or unintended external processing.

Human review remains a required control. Synthetic benchmarks and tests do not by themselves establish production safety.

---

## 3. Existing architecture to reuse

The current repository already contains substantial product architecture and validation capability. The default is reuse, not reinvention.

Preserve unless current evidence proves a defect:

- layered Dutch/Legal/Zorg recognition and profile policy;
- clinical/legal context preservation;
- side-by-side human review and authoritative replacement decisions;
- direct/manual missed-value correction;
- generation-bound Standard/Expert workflow state and fail-closed export gating;
- bound Scrub Key, mapping digest and controlled reinsert;
- TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity reporting;
- synthetic Legal/Zorg corpora, gold expectations, benchmark/gap-triage and E2E evidence.

No separate Evidence Framework, workflow engine, mapping service or replacement database is authorized merely by this roadmap.

---

# 4. Strategic stages

The strategic roadmap has five macro stages. Detailed implementation packages belong in `WORKPACKAGES.md`.

## Stage 1 — Repository Convergence — CURRENT

Goal:

> Establish one accurate current repository truth before further normal feature development.

Sequence:

```text
Preserve exact state
→ reconstruct active/reachable behavior
→ classify capabilities and debt
→ reconcile known current issues
→ remove only proven obsolete/contradictory paths
→ identify canonical validation hierarchy
→ align canonical documentation
→ verify
→ freeze clean baseline
```

Rules:

- no source-tree clone (`app_v2`, `scrub-new`, duplicate main Streamlit implementation);
- exact Git SHA is the preservation authority;
- classification is capability-level: `CANONICAL | RECONCILE | RETIRE | VARIANT-SPECIFIC`;
- no refactor for aesthetics alone;
- no new product feature work by default;
- privacy/security defects discovered during convergence may be fixed as narrow root-cause packages;
- existing `implementation_operations` / blind `governance_release_assurance` separation remains mandatory for consequential changes;
- the temporary debt ledger is execution evidence, not a new permanent source of product truth.

Exit milestone:

```text
SCRUB_REPOSITORY_CONVERGED
```

Exit requires one exact clean-baseline SHA, aligned current docs/issues, green relevant regression/evidence, and no known material contradiction knowingly left active.

---

## Stage 2 — Scrub Private Application

Starts only after `SCRUB_REPOSITORY_CONVERGED`.

Goal:

> Reuse the existing Scrub product core while adapting only the application trust boundary required for managed private hosting.

### Content-plane target

The following are customer document content:

```text
uploaded document
extracted text
detected values
review/replacement mappings
processed document
Scrub Key
restored document
```

Private application policy:

- no intentional persistent server-side storage of this content;
- no document-content logs;
- no document-content backup;
- no third-party document-processing egress;
- application-controlled session state is cleared when the processing interaction ends/reset occurs where the application controls that lifecycle.

### Variant-specific capability

Current functionality such as persistent remembered replacements or external Azure/OpenAI document processing may remain recoverable through Git/possible future Local product, but is excluded from Scrub Private unless explicitly re-approved.

### Hugging Face role

Hugging Face remains a synthetic/approved-test **application validation environment**, not the final confidential-production trust environment.

HF may prove application behavior under our control, such as:

- end-to-end Legal/Zorg flows;
- state integrity and stale-export blocking;
- no intentional application-level content persistence;
- no enabled third-party document-processing route;
- no content-bearing application logging.

HF does not prove provider-level snapshot, swap, backup, host-log or forensic-retention properties.

Exit milestone:

```text
SCRUB_HF_APPLICATION_COMPLETE
```

This is functional application evidence with synthetic data, not production-security certification.

---

## Stage 3 — Private Service

Starts only after `SCRUB_HF_APPLICATION_COMPLETE`.

Goal:

> Add the smallest production service layer needed for a real managed private deployment.

Initial architecture:

```text
Browser
  ↓ HTTPS
Proven OIDC / customer identity
  ↓
Scrub service
  ├─ ephemeral content plane
  └─ minimal persistent control plane
  ↓
User download
```

Control-plane data may include only necessary non-document operational information such as customer/service identity, IdP configuration, deployment version, security/login metadata, service configuration and health status.

Principles:

- use proven OIDC/customer IdP rather than custom authentication;
- least privilege and non-root runtime;
- immutable production source/runtime behavior;
- no persistent customer-document store;
- no content backup/logging;
- deny unnecessary outbound network access;
- avoid request-time model/dependency downloads where practical;
- manual provisioning is acceptable until automation materially reduces burden;
- customer-dedicated isolation is the preferred starting hypothesis, but exact VPS/container granularity is decided from real threat/cost/assurance requirements.

Avoid by default:

- Kubernetes;
- service mesh;
- Redis;
- queues;
- custom IAM;
- generalized multitenancy;
- billing/orchestration platforms;
- centralized document storage/processing services.

Exit milestone:

```text
SCRUB_PRIVATE_SERVICE_CANDIDATE
```

---

## Stage 4 — External Product & Service Assurance

This is separate from the internal release-assurance role used throughout development.

### Product-effectiveness evidence

Reuse existing Scrub evidence:

- synthetic Legal/Zorg corpora;
- canonical benchmark outputs;
- false-negative/false-positive and preserve/trap evidence;
- cross-profile regression;
- Scrub Key/reinsert safety;
- document hygiene/fidelity evidence;
- documented limitations and human-review controls.

### Service privacy/security evidence

Independently assess:

- authentication/access control;
- runtime/infrastructure isolation;
- persistence/deletion behavior;
- logs and backups;
- outbound egress;
- secrets;
- update/recovery/incident controls;
- penetration-test findings;
- accuracy of customer-facing privacy/security claims.

Do not create per-document “privacy scores” or false precision.

Exit:

```text
material assurance findings closed or explicitly accepted
```

---

## Stage 5 — Pilot

Initial commercial bias:

```text
Legal first
→ observe real workflow/trust friction
→ fix evidence-backed issues
→ Zorg
→ scale only when justified
```

Pilot evidence may justify targeted recognizer/UX/identity/operations improvements.

Pilot evidence does not automatically justify a platform rewrite, broad multitenancy, batch/API architecture, dashboards or a new AI/model architecture.

---

# 5. Current execution direction

The only active strategic line is **Stage 1 — Repository Convergence**.

The current executable queue is defined in `WORKPACKAGES.md`.

Do not resume historical Premium Input/Review/Export queues, installer work, pilot expansion or service infrastructure work simply because old plans/issues still mention them. Current source and evidence must justify any reopened package.

---

# 6. Validation strategy

Scrub already has multiple evidence generations. Convergence must identify the current release-validation hierarchy rather than create another framework.

A validation path is a candidate for canonical release evidence when it:

1. executes against current supported product code or is intentionally a pure contract test;
2. uses current committed synthetic/gold material where applicable;
3. measures a currently meaningful risk;
4. is reproducibly automated;
5. is part of current CI/release validation or has a clear current role;
6. states its limitations and does not imply unsupported production safety;
7. is not superseded by a later path solving the same responsibility more completely.

Classifications:

```text
CANONICAL RELEASE VALIDATION
SUPPLEMENTAL DIAGNOSTIC
HISTORICAL / SUPERSEDED
```

Likely complementary current evidence includes:

- full Python regression suite;
- recognizer-backed corpus benchmark/report workflow;
- Zorg baseline/recognizer/cross-profile evidence;
- Phase-6 synthetic E2E workflow matrix;
- Scrub Key security/roundtrip suites;
- document hygiene/fidelity suites;
- Premium Streamlit/AppTest state suites.

No new production recall/precision threshold is introduced merely as part of repository cleanup.

---

# 7. Future Local product

Local/offline capability is preserved as a possible future product direction, not an active delivery line.

Do not pre-build a two-edition architecture.

If Local later becomes a real maintained product requirement, determine then the smallest shared-core/product-specific structure. Git history preserves currently variant-specific functionality until that requirement exists.

---

# 8. Governing principle

```text
PRESERVE
→ RECONSTRUCT
→ REMOVE ONLY PROVEN DEBT
→ RECONCILE CURRENT TRUTH
→ PROVE
→ FREEZE
→ ADAPT ONLY WHAT PRIVATE REQUIRES
→ HARDEN
→ ASSURE
→ PILOT
```

For every proposed change:

> What concrete current problem disappears if we make this change, and is this the smallest complete way to remove it?

If there is no strong answer, do not add the change.
