# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-28 00:10 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-reinsert-integration

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` — merged as PR #43.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` — merged as PR #44 (`2f5085a700ba6ced3f41859b1e702bb2da7cd88c`).

Scope:
- Accept both structurally valid legacy v1.0 and bound v1.1 Scrub Keys during local import.
- Validate document/key binding automatically before any text, TXT, DOCX or PDF-to-TXT replacement.
- Allow replacement for `bound_match` and explicit legacy `legacy_unbound` compatibility only.
- Fail closed with zero replacements for binding mismatch, mixed document bindings, missing document binding, invalid mapping digest, invalid bound key and legacy key for bound document.
- Surface stable binding status, verified-match state, warnings and errors in the existing result/audit model.
- Preserve the document-first three-step reinsert UX and final confidential-output acknowledgement.

Boundaries:
- No new source/key execution buttons or acknowledgement checkboxes.
- No change to restored filenames, MIME types or supported TXT/DOCX/PDF-to-TXT boundaries.
- No automatic legacy-key upgrade or fabricated binding ID.
- No signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.
- No recognizer, threshold or anonymization/export changes.
- Synthetic data only; human review remains required; no production-readiness claim.

Next step:
- Add pure import/orchestration integration and fail-closed tests before the minimal UI status wiring.
