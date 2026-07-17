# Workpackage claim — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-17 22:30 Europe/Amsterdam

Branch: scrub-mvp-document-hygiene-fidelity-hardening-clean

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
- Helper-level document reinsert plus capability-copy alignment only; no new Streamlit controls or flow.
- No recognizer, threshold or replacement changes.
- No export filename, MIME or Scrub Key schema changes.
- No comments/tracked changes/metadata cleaning guarantee.
- No OCR or restored-PDF implementation.
- Synthetic data only; local-only deterministic processing.

Next step:
- Run final PR validation, merge after green Actions, verify Hugging Face sync and request live DOCX reinsert verification.


Hardening result:
- Completed at: 2026-07-17 22:30 Europe/Amsterdam
- DOCX header/footer reinsert resolved: true
- Resolved findings: 1
- Remaining findings: 1
- Report: `output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json`
- Handover: `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`
- App verification required after Actions and Hugging Face sync.

Final PR cleanup:
- Temporary patch/finalizer scripts removed and duplicate governance lines normalized before the final Actions run.


Clean branch rebuild:
- Rebuilt from current `main` after the Hugging Face incident closeout.
- Historical temporary operator commits are excluded.
- Final clean-branch validation is required before merge.
