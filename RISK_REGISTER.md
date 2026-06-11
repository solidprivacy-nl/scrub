# SolidPrivacy Scrub — Risk Register

This register tracks product, privacy, security and trust risks.

Status values:

```text
open
mitigating
accepted
closed
```

Impact values:

```text
critical
high
medium
low
```

---

## R1 — False negatives / missed sensitive data

Status: mitigating  
Impact: critical

Risk:

```text
Sensitive data remains in the scrubbed output and the user wrongly trusts the result.
```

Why it matters:

A scrubber has asymmetric failure costs. A false positive is annoying; a false negative may create the exact privacy incident the user wanted to avoid.

Current mitigations:

- Human review workflow.
- Review guidance and final review summary.
- Synthetic regression tests for selected recognizers.
- WP19 created `RECALL_BENCHMARK_SPEC.md`, defining how Scrub will measure recall, precision, per-entity scorecards, context-term preservation and CI reporting on messy synthetic Dutch legal and care documents.
- WP20 created the first synthetic messy legal, zorg and mixed corpus fixtures.
- WP21 created the gold-label sidecar schema foundation in `benchmark/gold/schema/gold_label_schema.json`, covering canonical entity classes, zero-based inclusive/exclusive offsets, expected text spans, preserve terms, known traps, normalization guidance and future runner expectations.

Gaps:

- No complete gold-label sidecars for the corpus yet.
- No implemented benchmark runner yet.
- No CI scorecard yet.
- No explicit false-negative residual-risk report yet.

Recommended workpackages:

- WP22 — Recall/precision test runner.
- WP23 — Entity-class scorecard in CI.
- WP24 — False-negative residual-risk report.

---

## R2 — Scrub Key leakage or accidental sharing

Status: mitigating  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long, tampered with or mishandled, allowing full re-identification of scrubbed content.
```

Why it matters:

The Scrub Key maps placeholders to real sensitive values. It is therefore concentrated sensitive re-identification data. Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.

Current mitigations:

- UI warnings around Scrub Key reinsert.
- Local-only/no-AI/no-cloud positioning for reinsert.
- `SCRUB_KEY_SPEC.md` states that Scrub Key-based output is pseudonymization, not full anonymization.
- WP25 created `SCRUB_KEY_THREAT_MODEL.md`, defining accidental sharing, local storage, download-folder, e-mail/AI-upload, shared-computer, retention, loss-of-key, tampering, malformed-key and import/export risks.
- WP26 created `SCRUB_KEY_LIFECYCLE_SPEC.md`, defining lifecycle states, retention/deletion expectations, loss-of-key and tampering consequences, audit/logging expectations and protection options.
- WP27 created `SCRUB_KEY_WARNING_UX_PLAN.md`, defining warning severity levels, acknowledgement expectations and proposed Dutch UI copy for Scrub Key creation, export/download, storage, import/reload, reinsert, restored downloads, expiry/delete guidance, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch moments.
- WP28 created `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`, defining user-controlled retention, expiry and deletion policy; Downloads/shared-computer/manual deletion guidance; loss-of-key and tampering consequences; audit/logging expectations; and the rule that Scrub must not silently delete keys or keep hidden recovery copies.

Gaps:

- No implemented warning UX changes yet.
- No encryption/protection implementation.
- No implemented expiry/delete UI or automated lifecycle tooling.
- No tamper-proof or authenticated Scrub Key format.
- No secure import/export regression test package focused on key handling.
- No automatic cleanup for browser Downloads or unmanaged local storage.
- No local vault / managed key store.
- No approved key recovery model.

Recommended workpackages:

- WP29 — Scrub Key secure import/export tests.
- WP28B — Scrub Key warning implementation planning.
- Later implementation package — MVP Scrub Key warning/acknowledgement UI.
- Later implementation package — protected local file handling.
- Later implementation package — encrypted key container.
- Later implementation package — local vault / managed key store.

---

## R3 — Placeholder corruption during AI roundtrip

Status: mitigating  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Why it matters:

The current reinsert path is deterministic and exact-match based. This is safe when placeholders are preserved exactly, but fragile when scrubbed content is rewritten, translated, summarized or moved through markdown, HTML, DOCX or PDF text extraction. The most dangerous failure is silent partial restoration: some placeholders restore while others are missing, merged or changed.

Current mitigations:

- Unknown placeholders and not-found placeholders are reported in reinsert audit flows.
- Duplicate placeholders in the Scrub Key are detected and excluded from deterministic replacement.
- WP30 created `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, documenting current assumptions, corruption examples, translation/summarization/formatting risks, candidate robust formats, checksum ideas, validation/audit direction, migration risks and backward compatibility concerns.
- WP31 created `PLACEHOLDER_FORMAT_PROPOSAL.md`, recommending the future architecture direction `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`, for example `[[SP_PERSON_0001_A7F3]]`, as proposal-only and additive to legacy placeholders.

Gaps:

- No robust placeholder format has been implemented.
- No checksum/validation helper exists yet.
- No near-miss placeholder detection exists yet.
- No synthetic AI-output corruption tests exist yet.
- No migration or backward-compatibility implementation exists yet.
- No Scrub Key schema/version support for robust placeholder metadata exists yet.

Recommended workpackages:

- WP32 — Placeholder checksum/validation helper.
- WP33 — Unknown/changed placeholder audit hardening.
- WP34 — Synthetic AI-output placeholder corruption tests.
- Later gated package — robust placeholder generation and compatibility implementation, only after validation and schema decisions.

---

## R4 — Hidden document content and metadata leakage

Status: mitigating  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

Current mitigations:

- DOCX reinsert limitations are documented.
- Roadmap already recognizes document hygiene and metadata-clean export as important.
- Current DOCX helper reports limitations and unsupported parts for headers, footers, comments, tracked changes, metadata and split-run placeholders.
- WP35 created `DOCX_HIDDEN_CONTENT_RISK_REVIEW.md`, defining current assumptions, hidden-content leakage risks, audit requirements, safe extraction/cleaning sequence and future warning/blocking policy boundaries.

Gaps:

- No DOCX metadata cleaner helper yet.
- No headers/footers/comments/tracked-changes extraction helper yet.
- No DOCX hygiene audit report yet.
- No clean DOCX export policy yet.
- No implementation for footnotes/endnotes, custom XML, text boxes/shapes or embedded object handling.
- No approved export-blocking policy for high-risk hidden content.

Recommended workpackages:

- WP36 — DOCX metadata cleaner helper.
- WP37 — Headers/footers/comments/tracked-changes extraction helper.
- WP38 — DOCX hygiene audit report.
- WP39 — Clean DOCX export policy.

---

## R5 — Cloud-demo trust gap

Status: mitigating  
Impact: high

Risk:

```text
The product promise is local-first, but the current demo runs in a Hugging Face cloud container. Confidential real documents should not be processed there.
```

Current mitigations:

- Roadmap includes local desktop/offline direction.
- UI messaging emphasizes local/no-AI/no-cloud for helper operations where applicable.
- WP45 created `LOCAL_RUNTIME_ARCHITECTURE_PLAN.md`, defining the Hugging Face demo role, local-first trust requirements and a phased local runtime path.
- WP45 recommends a minimal local Streamlit launcher as MVP path, followed by local file-handling/privacy validation, a PyInstaller/portable Windows proof of concept and a later Tauri/Electron desktop decision.

Gaps:

- No minimal local Streamlit launcher yet.
- No local runtime proof of concept yet.
- No offline mode demonstration.
- No network-traffic validation.
- No local file handling/privacy test.
- No Windows packaging proof of concept.
- No final desktop packaging decision.

Recommended workpackages:

- WP46 — Minimal local Streamlit launcher.
- WP47 — Local file handling/privacy test.
- WP48 — Portable Windows proof of concept.
- WP49 — Desktop packaging decision.

---

## R6 — Streamlit review UX ceiling

Status: open  
Impact: medium

Risk:

```text
A table-first Streamlit interface may not support the document-centric review experience needed for high-trust legal/care workflows.
```

Current mitigations:

- Review table flow exists.
- Review filters and guidance exist.

Gaps:

- No document-centric review specification.
- No click-to-mark sensitive text prototype.
- No frontend architecture decision for professional review UX.

Recommended workpackages:

- WP40 — Document-centric review UX specification.
- WP41 — Highlight-based review prototype decision.
- WP42 — Streamlit feasibility boundary review.
- WP43 — Frontend architecture decision.
- WP44 — Click-to-mark sensitive text prototype.

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

Current mitigations:

- WP15 reliability review.
- WP16 helper-only path.
- WP17 UI planning.
- WP18 UI warnings and audit fields, pending test/app verification.

Boundaries:

- No restored PDF output.
- No OCR.
- No PDF-to-DOCX reconstruction.
- No layout preservation promises.

Recommended workpackages:

- WP18-FIX — fix failing PDF-to-TXT UI tests.
- WP18 app verification.
- WP18B — closeout after app verification.

---

## R8 — Workflow status dependence on coordinator screenshots

Status: open  
Impact: medium

Risk:

```text
Development slows because workers wait for coordinator screenshots instead of self-checking GitHub Actions and Hugging Face sync where connector permissions allow.
```

Current mitigations:

- Coordinator supplies screenshots/evidence.
- Workpackages record Actions/sync status.

Gaps:

- No formal monitoring runbook.
- No standard status states.
- No automated status artifact.

Recommended workpackages:

- WP57 — Workflow status monitoring runbook and checks.
