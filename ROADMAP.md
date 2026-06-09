# SolidPrivacy Scrub — Risk-driven Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-facing product changes;
- `RISK_REGISTER.md` for trust, privacy and product risks;
- `DECISION_LOG.md` for accepted strategic and architecture decisions;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap status reconciliation: 2026-06-09 — WP18R.

---

## 1. Product vision

Scrub is evolving from a technical Presidio demo into a local-first professional document scrubber for confidential Dutch documents.

The first product wedge is confidential Dutch professional documents, with two early validation markets:

```text
Scrub Legal — Dutch legal process documents, case files and AI use.
Scrub Zorg  — Dutch care/healthcare operational documents and AI use.
```

The broader product direction is:

```text
A Dutch local-first privacy scrubber for professional confidential documents.
```

The long-term product should help professionals safely prepare documents for:

- AI use;
- external sharing;
- internal analysis;
- training examples;
- reporting;
- controlled publication.

The key promise remains:

```text
Sensitive information stays local.
The user remains in control.
The document stays readable.
Residual risk is visible.
```

---

## 2. Core product principle

The product is not just a generic anonymizer.

The real problem is:

```text
How can a professional safely use or share confidential documents without losing context, legal meaning, control or auditability?
```

Scrub must optimize for:

1. local processing;
2. high recall for sensitive data;
3. context preservation;
4. human review;
5. consistent placeholders;
6. secure Scrub Key lifecycle;
7. auditability and residual-risk reporting;
8. domain-specific recognition;
9. safe export;
10. desktop/offline deployment.

Legal and professional context must be preserved. Scrub should replace sensitive values, not legal meaning.

Examples of context that must remain readable:

- slachtoffer;
- minderjarige;
- verzoeker;
- verweerder;
- eiser;
- gemachtigde;
- rechtbank;
- zaaknummer label;
- claim context;
- incident context;
- zorgrelatie context;
- functionele rolbenamingen.

---

## 3. Strategic workflow

The product workflow direction remains:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The roadmap is now risk-driven rather than feature-driven.

The highest priority risks are:

1. false negatives: sensitive values missed by the scrubber;
2. Scrub Key leakage or accidental sharing;
3. hidden document content and metadata leakage;
4. cloud-demo trust gap versus local-first promise;
5. placeholder corruption during AI roundtrip;
6. table-centric review that does not match how professionals review documents;
7. unsupported PDF/scanned content being misunderstood as safely processed.

The product should not sell only detection. It should sell a trustworthy local workflow with:

- measurable recall;
- human-in-the-loop review;
- reversible pseudonymization under user control;
- secure Scrub Key handling;
- visible limitations;
- residual-risk/audit reporting;
- a clear future path to local desktop/offline use.

---

## 4. Current implementation status

Current implementation status after WP18 implementation and WP18R roadmap reset:

```text
v9       Dutch Legal UI Layer                                      completed
v9.1     UI polish                                                 completed
v10      Regression test foundation                                completed
v11.1    Legal reference hardening / audit layer                   completed
v11.2    Dutch recognizer integration tests                        completed
v12      Review UX line                                            completed
v13.1    Scrub Key JSON export                                     completed
v13.2    Scrub Key import/reload                                   completed
v13.3    Deterministic pasted-text reinsert                        completed/app-verified
v13.6    Two-mode UI: Anonimiseren / Originele waarden terugzetten completed/app-verified
v13.7    TXT reinsert upload/download UI                           completed/app-verified
v13.8    DOCX reinsert upload/download UI                          completed/app-verified
WP15     PDF text extraction reliability review                    completed review/specification only
WP16     Text-based PDF extraction helper spike                    completed after Actions/sync verification
WP16-FIX PDF helper test fix                                       completed after Actions/sync verification
WP16B    PDF helper verification closeout                          completed closeout-only
WP17     PDF text extraction reinsert UI planning                  completed planning/specification-only
WP17B    Roadmap current-status reconciliation after WP17           completed documentation-only
WP18     PDF text extraction to restored TXT UI implementation      implemented; tests failing; fix required
WP18R    Risk-driven roadmap and operating model reset              completed documentation/governance-only
```

### 4.1 v12 Review UX line

The v12 line is no longer the active line. It delivered the safer review workflow foundation:

- review status model;
- review focus filters;
- simplified review table;
- review guidance text;
- final review summary;
- export sanity checks.

Export semantics were intentionally preserved: warnings and summaries advise the user but do not silently block or alter exports unless a later workpackage explicitly changes that policy.

### 4.2 v13 Scrub Key / Reinsert line

The v13 line delivered the core reversible pseudonymization workflow:

- Scrub Key JSON export;
- Scrub Key import/reload;
- deterministic local pasted-text reinsert;
- two-mode UI separation between `Anonimiseren` and `Originele waarden terugzetten`;
- TXT upload/download reinsert;
- DOCX upload/download reinsert;
- clear warnings that Scrub Key-based reinsert restores sensitive/confidential values;
- audit output for reinsert flows;
- local-only / no-AI / no-cloud positioning.

Current document-level reinsert support:

```text
Pasted text → restored text
TXT upload  → restored TXT
DOCX upload → restored DOCX, within documented helper limits
```

Known DOCX limitations remain:

- normal `word/document.xml` text and tables are supported;
- headers, footers, comments, tracked changes and metadata are not fully processed;
- placeholders split across Word runs may not be restored;
- no perfect formatting guarantee is made.

### 4.3 PDF review, helper and UI line

WP15 concluded:

- do not implement full PDF reinsert now;
- do not implement OCR now;
- restored PDF output remains out of scope;
- PDF-to-DOCX reconstruction remains out of scope;
- DOCX remains the preferred document-level reinsert path;
- a helper-only text-based PDF extraction route to restored TXT output may be evaluated.

WP16 implemented that helper-only spike:

```text
PDF bytes → local selectable-text extraction → existing Scrub Key reinsert → restored TXT/text output only
```

WP17 specified that any future PDF UI must be limited to:

```text
PDF upload → local text extraction → restored TXT preview/download only
```

WP18 implemented the UI but currently has failing GitHub Actions tests. WP18 must be fixed and verified before app verification or closeout.

The PDF boundaries remain:

- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no cloud PDF conversion;
- no AI-based extraction;
- no layout preservation promises;
- no batch PDF processing;
- no real-data PDF test cases;
- no automatic PDF rehydration.

---

## 5. Active next workpackage

The active next workpackage is:

```text
WP18-FIX — Fix failing PDF text to TXT UI tests
```

Do not start WP18B until:

- GitHub Actions tests are green after WP18-FIX;
- Hugging Face sync is green after WP18-FIX;
- the coordinator/user has verified the Hugging Face app behavior.

WP18 app verification must confirm:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section;
- `Anonimiseren` does not show the PDF reinsert section;
- a valid Scrub Key can be loaded;
- a text-based PDF with placeholders can be uploaded;
- PDF text can be restored locally to TXT;
- restored TXT preview appears;
- restored TXT download appears;
- audit report appears;
- UI clearly says no OCR, no AI, no cloud and no PDF output;
- scanned/image-only PDFs are rejected or clearly marked unsupported;
- existing pasted-text, TXT and DOCX reinsert still work;
- existing anonymization/export behavior is unchanged.

---

## 6. New risk-driven phase order

After WP18-FIX, WP18 app verification and WP18B closeout, do not continue with batch, CLI or more PDF features first.

The next development phases are:

```text
Phase 1 — Trust & recall foundation
Phase 2 — Scrub Key security and lifecycle
Phase 3 — Placeholder robustness for AI roundtrip
Phase 4 — Hidden content and document hygiene
Phase 5 — Document-centric review UX
Phase 6 — Local-first runtime
Phase 7 — Pilot validation: Legal vs Zorg
Phase 8 — Scale features: profiles, batch, CLI, enterprise
```

### Phase 1 — Trust & recall foundation

Goal:

```text
Make detection quality measurable and treat false negatives as a product-critical risk.
```

Recommended workpackages:

- WP19 — Recall benchmark specification.
- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
- WP21 — Gold-label entity schema.
- WP22 — Recall/precision test runner.
- WP23 — Entity-class scorecard in CI.
- WP24 — False-negative residual-risk report.

Outputs:

- per-entity recall/precision metrics;
- known failure classes;
- residual-risk summary;
- CI guard for benchmark regressions.

### Phase 2 — Scrub Key security and lifecycle

Goal:

```text
Treat the Scrub Key as sensitive data because it can re-identify scrubbed content.
```

Recommended workpackages:

- WP25 — Scrub Key threat model.
- WP26 — Scrub Key encryption/lifecycle specification.
- WP27 — Scrub Key warning UX plan.
- WP28 — Scrub Key expiry/delete policy.
- WP29 — Scrub Key secure import/export tests.

Do not implement encryption before the threat model and lifecycle specification are complete.

### Phase 3 — Placeholder robustness for AI roundtrip

Goal:

```text
Ensure placeholders survive AI rewriting, translation and summarization well enough for deterministic reinsert.
```

Recommended workpackages:

- WP30 — Placeholder robustness review.
- WP31 — LLM-resistant placeholder format proposal.
- WP32 — Placeholder checksum/validation helper.
- WP33 — Unknown/changed placeholder audit hardening.
- WP34 — Synthetic AI-output placeholder corruption tests.

Example future direction:

```text
[[SP_NAME_0001_A7F3]]
[[SP_BSN_0002_C91B]]
```

### Phase 4 — Hidden content and document hygiene

Goal:

```text
Prevent hidden document content and metadata from leaking sensitive information.
```

Recommended workpackages:

- WP35 — DOCX hidden content risk review.
- WP36 — DOCX metadata cleaner helper.
- WP37 — Headers/footers/comments/tracked-changes extraction helper.
- WP38 — DOCX hygiene audit report.
- WP39 — Clean DOCX export policy.

This phase must precede batch/CLI scale features.

### Phase 5 — Document-centric review UX

Goal:

```text
Move review from table-first to document-first, because professionals review documents, not only rows of detected spans.
```

Recommended workpackages:

- WP40 — Document-centric review UX specification.
- WP41 — Highlight-based review prototype decision.
- WP42 — Streamlit feasibility boundary review.
- WP43 — Frontend architecture decision: Streamlit vs React/Tauri/Electron.
- WP44 — Click-to-mark sensitive text prototype.

Streamlit may remain the prototype UI, but the final professional review UI may need a separate frontend.

### Phase 6 — Local-first runtime

Goal:

```text
Resolve the trust gap between the local-first promise and the current Hugging Face cloud demo.
```

Recommended workpackages:

- WP45 — Local runtime architecture plan.
- WP46 — Minimal local Streamlit launcher.
- WP47 — Local file handling/privacy test.
- WP48 — Portable Windows proof of concept.
- WP49 — Desktop packaging decision: PyInstaller/Tauri/Electron.

Hugging Face remains useful for demo and development, but should not be the trust environment for confidential real-world documents.

### Phase 7 — Pilot validation: Legal vs Zorg

Goal:

```text
Test whether real users trust, use and pay for the workflow.
```

Recommended workpackages:

- WP50 — Pilot design: Legal vs Zorg.
- WP51 — ICP and pricing hypothesis.
- WP52 — Pilot intake and NDA process.
- WP53 — 10-document controlled pilot protocol.
- WP54 — Missers/false negatives feedback loop.
- WP55 — Residual-risk report as consultancy deliverable.

Because SolidPrivacy already has care-sector context, Scrub Zorg may be the fastest validation wedge even while Scrub Legal remains the initial product concept.

### Phase 8 — Scale features

Only after single-document trust, security, review and local runtime are credible:

- vertical profiles;
- batch / dossiermap;
- CLI / automation;
- enterprise deployment;
- broader markets.

Batch should not come before single-document flow is reliable.

---

## 7. Parallelization strategy

After WP18-FIX is resolved, these can run safely in parallel because they do not touch the same UI flow:

```text
WP19 — Recall benchmark specification
WP25 — Scrub Key threat model
WP30 — Placeholder robustness review
WP35 — DOCX hidden content risk review
WP45 — Local runtime architecture plan
WP50 — Pilot design: Legal vs Zorg
WP56 — User-facing release notes split and documentation hygiene
WP57 — Workflow status monitoring runbook and checks
```

Do not run in parallel:

- WP18-FIX and any other UI patch work;
- multiple changes to `Dockerfile` startup patch order;
- multiple changes to `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`;
- export/download flow changes.

---

## 8. Documentation model

The documentation model is now split:

```text
ROADMAP.md         = strategic risk-driven direction and phase order
WORKPACKAGES.md    = active queue and execution dependencies
CHANGELOG.md       = internal implementation/workpackage log
RELEASE_NOTES.md   = user-facing product capability changes
DECISION_LOG.md    = accepted strategic/architecture/product decisions
RISK_REGISTER.md   = active privacy/product/security risks and mitigations
handover/          = worker handovers
```

This avoids mixing user-facing release information with agent/process worklogs.

---

## 9. Product architecture target

Current prototype architecture:

```text
Hugging Face Space
Streamlit UI
Presidio/spaCy recognizers
Dutch legal recognizers
Candidate scanner
Review table
Scrub Key import/export
Pasted/TXT/DOCX reinsert
PDF text extraction helper
PDF-to-restored-TXT UI implementation
Exports
GitHub Actions tests
GitHub → Hugging Face sync
```

Target architecture:

```text
Local desktop app
Local recognition engine
Local benchmark/evaluation layer
Local review workflow
Secure local Scrub Key vault/files
Local exports
Residual-risk/audit reports
Optional CLI
No required cloud processing
```

Layered architecture target:

```text
1. Core detection engine
2. Evaluation and recall layer
3. Review and decision layer
4. Scrub Key security layer
5. Reinsert layer
6. UI layer
7. Runtime/deployment layer
```

The Python core should remain reusable. Streamlit can remain the prototype/demo surface while the future document-centric review UI is evaluated separately.

---

## 10. Security and trust principles

For the final product:

- no document upload to third-party cloud;
- no model training on user documents;
- no telemetry containing document content;
- clear warning when using cloud AI outside Scrub;
- local-only processing as default;
- metadata-aware exports;
- audit report;
- residual-risk report;
- clear distinction between anonymization, pseudonymization and redaction;
- explicit Scrub Key lifecycle and deletion policy.

Future security validation should include:

- offline mode demonstration;
- network traffic check;
- clear file storage locations;
- local key storage explanation;
- user-controlled deletion;
- encrypted or protected Scrub Key strategy.

---

## 11. Development governance

For recognizer work:

1. Add or update benchmark/gold-label cases.
2. Add or update tests.
3. Change recognizer/scanner logic.
4. Verify GitHub Actions tests are green.
5. Verify GitHub to Hugging Face sync when relevant.
6. Test the app in Hugging Face when UI behavior changed.
7. Update `CHANGELOG.md`.
8. Update `RELEASE_NOTES.md` for user-facing changes.
9. Update `WORKPACKAGES.md` when status or next steps change.
10. Update `ROADMAP.md` only when strategy, phase status or sequence changes.

For UI implementation work:

1. Prefer helper modules and tests before UI changes.
2. Keep UI workpackages small and sequential.
3. Do not silently change export/download semantics.
4. Ask for app verification whenever UI behavior changes.
5. Preserve local-only, no-AI and no-cloud boundaries unless explicitly approved otherwise.

For status monitoring:

1. Check GitHub Actions status directly when possible.
2. Check GitHub to Hugging Face sync directly when possible.
3. Fetch failing job logs before proposing a fix.
4. Ask the coordinator only for app verification or permissions gaps.
