# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: completed; targeted validation passed; PR verification pending

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
- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.


Triage result:
- Recommended primary control: non-sensitive document binding ID in every automatic/manual placeholder and the corresponding key.
- Recommended complementary control: canonical SHA-256 mapping digest for accidental key corruption.
- Legacy v1.0 keys remain explicit unbound compatibility, not silently bound.
- Bound mismatch, mixed IDs and invalid digest must fail closed with zero replacements.
- Signatures/HMAC deferred until protected local signing-key lifecycle exists.
- Targeted triage/source-evidence tests passed.
- Implementation authorized in this package: false.
- Production ready: false; human review required: true.
- Triage: `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`.
- Evidence: `output/validation/mvp_scrub_key_document_binding_gap_triage.json`.
- Validation evidence: `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`.
- Handover: `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`.
