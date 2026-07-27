# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Status: implemented; targeted validation pending

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 21:29 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-export-integration

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` — merged as PR #43 (`07766c8a0407ce2da68af7082799cb6f6ef48953`).

Scope:
- Allocate one locally generated, non-sensitive document binding ID per active source-text scope.
- Generate bound automatic, candidate and manual placeholders by default in the anonymization flow.
- Rebind remembered legacy placeholder tokens when this is lossless; preserve custom replacement text unchanged.
- Export schema-1.1 Scrub Keys with binding metadata and canonical mapping digest when every included mapping is document-bound.
- Fail the Scrub Key export visibly when an included custom/unbound replacement prevents verified binding.
- Preserve document export filenames, MIME types, review controls, legal meaning and the existing three-step reinsert UX.

Boundaries:
- No reinsert enforcement in this package.
- No automatic migration or rewriting of arbitrary custom replacement values.
- No signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.
- No recognizer or threshold changes.
- Human review remains required; no production-readiness claim.

Next step:
- Implement helper-first export integration and tests, then hand over to `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION` after merge.

Implementation result:
- Bound placeholder defaults and schema-1.1 key export integrated.
- Custom replacement text remains unchanged and blocks verified key export.
- Reinsert enforcement remains out of scope.
- Handover: `handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md`.
