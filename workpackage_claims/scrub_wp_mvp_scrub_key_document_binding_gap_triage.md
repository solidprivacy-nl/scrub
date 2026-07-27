# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 19:12 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-document-binding-gap-triage

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` — merged as PR #40.
- Critical evidence `scrub_key_document_binding_missing` is recorded in `output/validation/mvp_scrub_key_roundtrip_validation_report.json`.

Scope:
- Classify the wrong-key/tampered-key threat by accidental mismatch, accidental corruption and malicious tampering.
- Compare candidate document/key binding mechanisms against TXT, DOCX, PDF-to-TXT and pasted-text workflows.
- Define compatibility, migration, privacy, legal-context and UX boundaries.
- Recommend the smallest safe implementation sequence.
- Produce machine-readable triage evidence and implementation workpackages.

Boundaries:
- Planning/triage only.
- No product code, UI, schema, placeholder, export, reinsert or document-processing change.
- Do not weaken current validation or add guessing/automatic repair.
- Synthetic evidence only.
- Human review remains required; no production-readiness claim.

Next step:
- Inspect current placeholder/key architecture, evaluate binding options and record a decision-backed implementation sequence.
