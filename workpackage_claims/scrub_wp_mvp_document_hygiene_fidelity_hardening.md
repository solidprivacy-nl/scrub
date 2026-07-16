# Workpackage claim — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 22:30 Europe/Amsterdam

Branch: scrub-mvp-document-hygiene-fidelity-hardening

Dependencies:
- SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX — merged.
- SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — merged.

Evidence:
- DOCX body/table reinsert passes, while scrubbed header/footer placeholders remain after reinsert.
- DOCX hygiene audit already reports header/footer presence.
- PDF text roundtrip passes only to restored TXT; restored PDF and OCR remain unsupported product boundaries.

Scope:
- Harden deterministic DOCX reinsert fidelity for existing scrubbed header and footer OOXML parts.
- Add contract and regression tests covering document body, tables, headers and footers.
- Preserve explicit unsupported boundaries for comments, tracked changes, metadata, split placeholders, OCR and restored PDF.
- Update the Phase 6 matrix expectation and evidence after the helper change.

Boundaries:
- Helper-level document reinsert only; no Streamlit UI changes.
- No recognizer, threshold or replacement changes.
- No export filename, MIME or Scrub Key schema changes.
- No comments/tracked changes/metadata cleaning guarantee.
- No OCR or restored-PDF implementation.
- Synthetic data only; local-only deterministic processing.

Next step:
- Add failing contract tests, implement multi-part OOXML reinsert narrowly, rerun the synthetic matrix and related document/Scrub Key/hygiene suites, then update governance evidence and handover.
