# SolidPrivacy Scrub — Risk-driven Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-facing product changes;
- `RISK_REGISTER.md` for trust, privacy and product risks;
- `DECISION_LOG.md` for accepted strategic and architecture decisions;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap strategy update: 2026-06-12 — local installer deferred to final phase.

---

## 1. Product vision

Scrub is evolving from a technical Presidio demo into a trustworthy Dutch professional document scrubber for confidential legal and care documents.

The long-term product should help professionals safely prepare documents for:

- AI use;
- external sharing;
- internal analysis;
- training examples;
- reporting;
- controlled publication.

The key promise remains:

```text
Sensitive information stays local in the final trust environment.
The user remains in control.
The document stays readable.
Residual risk is visible.
```

Important sequencing decision:

```text
Do not spend major effort on a local installer until logic, interface, security and trustworthiness have been validated as far as practical through the online/web prototype and GitHub test workflow.
```

The Hugging Face app remains the fastest validation surface for synthetic and approved non-confidential testing. The local installer is deliberately moved to the end of the roadmap because installable-app testing is more labor-intensive than web-interface testing.

---

## 2. Core product principle

The product is not just a generic anonymizer.

The real problem is:

```text
How can a professional safely use or share confidential documents without losing context, legal meaning, control or auditability?
```

Scrub must optimize for:

1. high recall for sensitive data;
2. context preservation;
3. human review;
4. consistent placeholders;
5. secure Scrub Key lifecycle;
6. auditability and residual-risk reporting;
7. domain-specific recognition;
8. safe export and reinsert;
9. clear online validation of logic/interface/security/trust;
10. local desktop/offline deployment after the above is credible.

Legal and professional context must be preserved. Scrub should replace sensitive values, not legal meaning.

---

## 3. Strategic workflow

The product workflow direction remains:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The roadmap is risk-driven rather than feature-driven.

The highest priority risks are:

1. false negatives: sensitive values missed by the scrubber;
2. Scrub Key leakage or accidental sharing;
3. hidden document content and metadata leakage;
4. placeholder corruption during AI roundtrip;
5. table-centric review that does not match how professionals review documents;
6. cloud-demo trust gap versus final local-first promise;
7. unsupported PDF/scanned content being misunderstood as safely processed;
8. installer/distribution risk, deliberately deferred until the product is otherwise credible.

The product should not sell only detection. It should sell a trustworthy workflow with:

- measurable recall;
- human-in-the-loop review;
- reversible pseudonymization under user control;
- secure Scrub Key handling;
- visible limitations;
- residual-risk/audit reporting;
- extensive online/web validation first;
- a later path to local desktop/offline use.

---

## 4. Current implementation status

The current app remains a GitHub-synced Hugging Face/Streamlit prototype plus local runtime experiments. Recent work completed the recall/trust foundation, Scrub Key security planning/tests, placeholder robustness helpers/tests, DOCX hygiene triage and local runtime decision line.

Current important open status:

```text
WP28C — Scrub Key warning/acknowledgement UI implementation: implemented; awaiting Actions/HF sync evidence and app verification.
WP36A — DOCX residual placeholder and comments risk triage: completed; next DOCX hygiene step is extraction/audit work.
WP49 — Desktop packaging decision: completed; installer remains deferred.
```

---

## 5. Validation-first roadmap rule

This is now an explicit roadmap rule:

```text
Validate logic, interface, security and trustworthiness online first. Delay local installer/MSI work until the core product behavior is acceptable.
```

Reason:

- Web-interface testing is faster than installable-app testing.
- The current Hugging Face app is sufficient for synthetic and non-confidential workflow validation.
- Installer testing introduces OS, antivirus, signing, dependency, update and support complexity.
- Packaging too early risks wasting effort on distributing behavior that may still change.
- For a privacy product, trust depends first on detection quality, review flow, Scrub Key safety, document hygiene and auditability.

Implication:

```text
Local installer work is a final-phase investment, not the next product track.
```

Allowed before final installer phase:

- lightweight local runtime documentation;
- minimal local launcher validation;
- architecture/decision documents;
- small packaging proofs only if explicitly approved by the coordinator.

Blocked before final installer phase unless explicitly approved:

- MSI implementation;
- production installer claim;
- signed desktop package;
- auto-updater;
- broad enterprise deployment work;
- major PyInstaller/Tauri/Electron implementation.

---

## 6. New risk-driven phase order

The current phase order is:

```text
Phase 1 — Trust & recall foundation
Phase 2 — Scrub Key security and lifecycle
Phase 3 — Placeholder robustness for AI roundtrip
Phase 4 — Hidden content and document hygiene
Phase 5 — Document-centric review UX
Phase 6 — Online workflow validation and trust hardening
Phase 7 — Pilot validation: Legal vs Zorg
Phase 8 — Scale features: profiles, batch, CLI, enterprise
Phase 9 — Final local desktop/offline installer path
```

### Phase 1 — Trust & recall foundation

Goal:

```text
Make detection quality measurable and treat false negatives as a product-critical risk.
```

Outputs:

- per-entity recall/precision metrics;
- known failure classes;
- residual-risk summary;
- CI guard for benchmark regressions.

### Phase 2 — Scrub Key security and lifecycle

Goal:

```text
Treat the Scrub Key as sensitive re-identification data and make key-handling risk visible.
```

Do not implement encryption, vaulting or schema migration without separate approved lifecycle/security packages.

### Phase 3 — Placeholder robustness for AI roundtrip

Goal:

```text
Ensure placeholders survive AI rewriting, translation and summarization well enough for deterministic reinsert.
```

Robust placeholder generation, migration and Scrub Key schema changes remain gated future work.

### Phase 4 — Hidden content and document hygiene

Goal:

```text
Prevent hidden document content, comments, tracked changes and metadata from leaking sensitive information.
```

This phase must address DOCX residual placeholders and comments/kantlijncommentaren before broad trust claims or scale features.

### Phase 5 — Document-centric review UX

Goal:

```text
Move review from table-first to document-first, because professionals review documents, not only rows of detected spans.
```

Streamlit may remain the prototype UI. A final professional review UI may need a separate frontend decision later.

### Phase 6 — Online workflow validation and trust hardening

Goal:

```text
Use the online/web prototype and GitHub workflow to validate as much product behavior as possible before installer investment.
```

This phase should focus on:

- end-to-end web workflow testing with synthetic and approved non-confidential documents;
- UI behavior verification;
- Scrub Key warning/acknowledgement verification;
- document hygiene warnings and audit output;
- recall and residual-risk reporting;
- security/trust copy;
- regression tests;
- Hugging Face app verification after GitHub Actions/sync.

The Hugging Face demo remains unsuitable for confidential production documents, but it is the preferred validation surface for product behavior until the workflow is credible.

### Phase 7 — Pilot validation: Legal vs Zorg

Goal:

```text
Test whether real users trust, use and pay for the workflow.
```

Pilot validation should happen with careful data rules:

- synthetic documents where possible;
- approved non-confidential examples where needed;
- no uncontrolled confidential production documents in the cloud demo;
- clear distinction between demo validation and final local trust environment.

### Phase 8 — Scale features

Only after single-document trust, security, review and online workflow validation are credible:

- vertical profiles;
- batch / dossiermap;
- CLI / automation;
- enterprise workflow options;
- broader markets.

Batch should not come before single-document flow is reliable.

### Phase 9 — Final local desktop/offline installer path

Goal:

```text
Invest in local installer/desktop packaging only after logic, interface, security and trustworthiness are acceptable.
```

This phase may include:

- hardened portable Python folder;
- PyInstaller one-folder proof;
- Tauri/Electron shell decision if document-centric frontend requires it;
- code signing;
- update and rollback policy;
- offline dependency/model asset strategy;
- temp-file and network-traffic validation;
- managed deployment decision;
- MSI/MSIX or other installer only after prior evidence is strong.

This phase is deliberately last because installer testing is expensive and should not precede product-behavior validation.

---

## 7. Active next work direction

Current active priorities:

```text
1. Obtain WP28C Actions/HF sync evidence and app verification before more Scrub Key UI work.
2. Continue DOCX hygiene extraction/audit work if coordinator approves: WP37.
3. Continue online/web validation and trust hardening before installer work.
```

Local packaging next steps such as `WP48B` or `WP49B` are not default next work. They require explicit coordinator approval and should remain small proof packages only.

---

## 8. Parallelization strategy

Safe to do in parallel:

- helper modules with separate files;
- tests that do not touch the same UI flow;
- specifications;
- documentation;
- benchmark data design;
- risk reviews;
- non-UI architecture work.

Do not run in parallel:

- multiple changes to `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`;
- multiple changes to the same Streamlit patch file;
- export/download flow changes;
- review table flow changes;
- Docker/runtime startup patch-order changes;
- installer/packaging work unless explicitly approved.

Use `workpackage_claims/` before starting a package.

---

## 9. Documentation model

The documentation model is split:

```text
ROADMAP.md         = strategic risk-driven direction and phase order
WORKPACKAGES.md    = active queue and execution dependencies
CHANGELOG.md       = internal implementation/workpackage log
RELEASE_NOTES.md   = user-facing product capability changes
DECISION_LOG.md    = accepted strategic/architecture/product decisions
RISK_REGISTER.md   = active privacy/product/security risks and mitigations
handover/          = worker handovers
```

---

## 10. Product architecture target

Current prototype architecture:

```text
Hugging Face Space
Streamlit UI
Presidio/spaCy recognizers
Dutch legal recognizers
Candidate scanner
Review table
Scrub Key import/export
Pasted/TXT/DOCX/PDF-to-TXT reinsert
Exports
GitHub Actions tests
GitHub → Hugging Face sync
```

Target architecture remains local-first, but the installer comes late:

```text
Validated online/web workflow first
Reusable Python core
Local recognition engine
Local benchmark/evaluation layer
Local review workflow
Secure Scrub Key handling
Local exports
Residual-risk/audit reports
Final local desktop/offline packaging after validation
```

The Python core should remain reusable. Streamlit can remain the prototype/demo surface while the future document-centric review UI and final installer path are evaluated separately.

---

## 11. Security and trust principles

For the final product:

- no document upload to third-party cloud in the final trust environment;
- no model training on user documents;
- no telemetry containing document content;
- clear warning when using cloud AI outside Scrub;
- local-only processing as final production default;
- metadata-aware exports;
- audit report;
- residual-risk report;
- clear distinction between anonymization, pseudonymization and redaction;
- explicit Scrub Key lifecycle and deletion policy.

Before final installer work, security validation should include:

- recall/residual-risk evidence;
- UI review verification;
- Scrub Key handling verification;
- hidden-content/document-hygiene audit direction;
- online workflow/app verification;
- offline mode demonstration plan;
- network traffic check plan;
- clear file storage location plan;
- local key storage explanation;
- user-controlled deletion model.

---

## 12. Development governance

For implementation work:

1. Add or update benchmark/gold-label cases where relevant.
2. Add or update tests.
3. Change logic/UI only within the approved package scope.
4. Verify GitHub Actions tests when possible.
5. Verify GitHub to Hugging Face sync when relevant.
6. Test the app in Hugging Face when UI behavior changed.
7. Update `CHANGELOG.md`.
8. Update `RELEASE_NOTES.md` for user-facing changes.
9. Update `WORKPACKAGES.md` when status or next steps change.
10. Update `ROADMAP.md` only when strategy, phase status or sequence changes.

For installer/packaging work:

1. Do not start by default.
2. Require explicit coordinator approval.
3. Keep proof packages small and separate.
4. Do not claim production installation before signing, update, rollback, offline, network, temp-file and support boundaries are validated.
5. Prefer web-interface validation of product behavior before packaging investment.
