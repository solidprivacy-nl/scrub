# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Status: completed; final GitHub Actions passed; ready to merge

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

Validation:
- Targeted helper, model, contract, manual-entry, UI-contract and roundtrip suite: 103 passed.
- Full repository suite: 881 passed.
- Final normal GitHub Actions run #1757: passed on `cae60425894c23c05dd5705b41304ed0c32ee274`.
- Temporary operator, diagnostic workflow, trigger and logs removed before final validation.
- Machine-readable evidence: `output/validation/mvp_scrub_key_binding_export_validation.json`.

Next step:
- Merge PR #44, verify GitHub-to-Hugging-Face sync, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.

Implementation result:
- Bound placeholder defaults and schema-1.1 key export integrated.
- Custom replacement text remains unchanged and blocks verified key export.
- Reinsert enforcement remains out of scope.
- Handover: `handover/workpackages/20260727_2145_mvp_scrub_key_binding_export_integration.md`.
