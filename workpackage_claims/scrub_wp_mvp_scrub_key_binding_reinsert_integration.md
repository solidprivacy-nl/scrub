# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: completed; final GitHub Actions passed; ready to merge and app-verify

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-28 00:10 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-reinsert-integration

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` — merged as PR #43.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` — merged as PR #44 (`2f5085a700ba6ced3f41859b1e702bb2da7cd88c`).

Implementation result:
- Structurally valid legacy v1.0 and bound v1.1 Scrub Keys are read explicitly.
- Document/key binding is validated before text, TXT, DOCX or PDF-to-TXT replacement.
- `bound_match` is a verified match; valid legacy v1.0 remains explicit unverified compatibility.
- Six frozen mismatch/corruption states fail closed with zero replacements.
- DOCX binding failure returns the exact original package bytes without partial output.
- Stable binding status, warnings, IDs and digest state are visible in the existing report/status surfaces.
- The three-step document-first flow and single final confidential-output acknowledgement remain unchanged.

Validation:
- Adversarial synthetic tests cover correct, wrong, mixed, missing, legacy and tampered key/document combinations.
- TXT, DOCX body/header/footer and PDF-to-TXT paths are covered.
- Normal full GitHub Actions run #1789 passed during implementation.
- Final clean PR GitHub Actions run #1797 passed on `9f8eddda04b768e994184badbea3aefe39ce74cc`.
- Temporary operator, diagnostic, validation, finalizer and contract workflows, triggers, scripts and logs were removed.
- Evidence: `output/validation/mvp_scrub_key_binding_reinsert_validation.json`.

Boundaries:
- No filename, MIME type or supported-format change.
- No automatic legacy upgrade or fabricated document code.
- No signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.
- Human review remains required; production readiness remains false.

Next step:
- Merge PR #45 after the final metadata-only Actions run, verify GitHub-to-Hugging-Face sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.
