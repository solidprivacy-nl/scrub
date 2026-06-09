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

Gaps:

- No synthetic gold-label corpus yet.
- No implemented benchmark runner yet.
- No CI scorecard yet.
- No explicit false-negative residual-risk report yet.

Recommended workpackages:

- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
- WP21 — Gold-label entity schema.
- WP22 — Recall/precision test runner.
- WP23 — Entity-class scorecard in CI.
- WP24 — False-negative residual-risk report.

---

## R2 — Scrub Key leakage or accidental sharing

Status: open  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long or mishandled, allowing full re-identification of scrubbed content.
```

Why it matters:

The Scrub Key maps placeholders to real sensitive values. It is therefore concentrated sensitive data.

Current mitigations:

- UI warnings around Scrub Key reinsert.
- Local-only/no-AI/no-cloud positioning for reinsert.

Gaps:

- No formal Scrub Key threat model.
- No lifecycle/expiry/delete policy.
- No encryption/protection strategy.
- No user-facing release/security notes focused on Scrub Key handling.

Recommended workpackages:

- WP25 — Scrub Key threat model.
- WP26 — Scrub Key encryption/lifecycle specification.
- WP27 — Scrub Key warning UX plan.
- WP28 — Scrub Key expiry/delete policy.
- WP29 — Scrub Key secure import/export tests.

---

## R3 — Placeholder corruption during AI roundtrip

Status: open  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current mitigations:

- Unknown placeholders and not-found placeholders are reported in reinsert audit flows.

Gaps:

- No LLM-resistant placeholder format.
- No checksum/validation helper for placeholder integrity.
- No synthetic AI-output corruption tests.

Recommended workpackages:

- WP30 — Placeholder robustness review.
- WP31 — LLM-resistant placeholder format proposal.
- WP32 — Placeholder checksum/validation helper.
- WP33 — Unknown/changed placeholder audit hardening.
- WP34 — Synthetic AI-output placeholder corruption tests.

---

## R4 — Hidden document content and metadata leakage

Status: open  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

Current mitigations:

- DOCX reinsert limitations are documented.
- Roadmap already recognizes document hygiene and metadata-clean export as important.

Gaps:

- No complete hidden-content extraction policy.
- No metadata cleaner helper.
- No tracked-changes/comments policy.
- No DOCX hygiene audit report.

Recommended workpackages:

- WP35 — DOCX hidden content risk review.
- WP36 — DOCX metadata cleaner helper.
- WP37 — Headers/footers/comments/tracked-changes extraction helper.
- WP38 — DOCX hygiene audit report.
- WP39 — Clean DOCX export policy.

---

## R5 — Cloud-demo trust gap

Status: open  
Impact: high

Risk:

```text
The product promise is local-first, but the current demo runs in a Hugging Face cloud container. Confidential real documents should not be processed there.
```

Current mitigations:

- Roadmap includes local desktop/offline direction.
- UI messaging emphasizes local/no-AI/no-cloud for helper operations where applicable.

Gaps:

- No local runtime proof of concept yet.
- No offline mode demonstration.
- No network-traffic validation.
- No local file handling/privacy test.

Recommended workpackages:

- WP45 — Local runtime architecture plan.
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
