# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 18:42 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-roundtrip-validation

Dependencies:
- `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX` — completed.
- `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING` — completed and app-verified.
- `SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

Scope:
- Build a reproducible synthetic adversarial matrix for Scrub Key and placeholder roundtrip behavior.
- Cover intact, repeated, missing, unknown, translated, malformed, merged and changed placeholders.
- Cover duplicate, incomplete, malformed, tampered and wrong Scrub Keys.
- Verify partial reinsert, validation failure, audit visibility and no silent placeholder guessing.
- Identify evidence-backed gaps without changing product semantics in this validation package.

Boundaries:
- Validation/reporting only unless a separate evidence-driven fix package is opened.
- No UI changes.
- No Scrub Key schema, export, storage or lifecycle changes.
- No cloud, AI, OCR or external document processing.
- Synthetic data only.
- Preserve deterministic local reinsert and human review.

Next step:
- Add pure matrix/report helpers, manifest, tests and machine-readable evidence; then route any reproducible gap through a separate triage package.
