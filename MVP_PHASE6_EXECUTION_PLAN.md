# SolidPrivacy Scrub — MVP Phase 6 Execution Plan

Status: active after `SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT` merges.

## Objective

Validate the supported MVP workflow with synthetic evidence before pilot expansion, local packaging or stronger trust claims.

```text
Import -> Scrub -> Review -> Handmatig aanvullen -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Package order

### 1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Create a versioned synthetic corpus, a machine-readable case manifest and automated tests covering supported TXT, DOCX and text-based PDF paths. Record expected detections, preserved role/context terms, manual additions, exports, Scrub Key, reinsert and audit outcomes.

### 2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Review only reproducible gaps from the matrix. Classify each as recognizer gap, misclassification, over-masking, document-extraction gap, expected limitation or manual-review dependency. Do not implement broad recognizer changes in the triage package.

### 3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Test and, through separately scoped fixes, harden headers, footers, tables, comments, tracked changes, hidden content, metadata, text order, residual placeholders and export readability. Preserve the report-only boundary until a clean-DOCX policy change is explicitly approved.

### 4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Test correct, missing, duplicate, altered, translated, merged and malformed placeholders; wrong or incomplete Scrub Keys; repeated values; partial restoration; and deterministic recovery reporting.

### 4A. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Classify the critical finding that a structurally valid wrong key can reuse the same placeholder namespace and restore incorrect values without a detectable mismatch. Decide whether document/key binding requires a key identifier, content fingerprint, manifest binding or another explicit contract. Do not change schema, export or reinsert semantics in the triage package.

Triage result: use a non-sensitive document binding ID in every placeholder and the corresponding key, complemented by a canonical mapping digest. Implement sequentially through contract tests, pure model helpers, export integration, reinsert integration and live verification. Legacy unbound keys remain explicit; malicious tampering remains outside the MVP without protected signing-key management.

Contract status: frozen. Binding IDs use `B[A-Z2-7]{16}`; bound keys use an explicit new schema direction with canonical SHA-256 mapping digest, eight statuses and fail-closed mismatch rules. Pure model implementation is complete and isolated; export integration is active next, followed by reinsert enforcement.

### 5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE

Produce a consistent machine-readable and human-readable evidence summary covering automatic findings, manual additions, unresolved candidates, document-hygiene warnings, exports, reinsert completeness and known limitations.

### 6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT

Decide whether the prototype is ready for controlled pilot validation. This gate does not establish production readiness and cannot remove the human-review requirement.

## Validation matrix minimum scope

- synthetic TXT, DOCX and text-based PDF;
- paragraphs, tables, headers and footers;
- names, addresses, email, telephone and dates;
- Dutch legal dossier, case, client, claim and administrative references;
- legal and care role words that must retain meaning;
- manual missed-value addition through the replacement table;
- normal TXT/DOCX/PDF exports within existing semantics;
- Scrub Key export/import and warning boundaries;
- pasted-text, TXT and DOCX reinsert plus PDF-to-TXT limitation;
- DOCX hygiene audit and residual-risk visibility;
- placeholder mutation simulations without external AI or cloud processing.

## Evidence rules

- synthetic data only;
- deterministic fixtures where possible;
- machine-readable case manifest;
- explicit expected and observed outcomes;
- failures become narrow workpackages, not silent test weakening;
- preserve legal meaning;
- no claim that all sensitive data is detected;
- no production-readiness claim;
- no Phase 7 pilot start without explicit quality-gate approval.

## Parallelization

Safe in parallel only when files and flows do not overlap:

- corpus/fixture design;
- helper-level validation utilities;
- audit evidence schema;
- documentation and risk review.

Keep sequential:

- recognizer changes;
- `presidio_streamlit.py` changes;
- document extraction/export changes;
- Scrub Key/reinsert semantics;
- quality-gate decisions.
