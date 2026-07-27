# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 19:27 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-contract-tests

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE` — merged as PR #41.
- Decision D033 defines the bound-placeholder plus mapping-digest direction.

Scope:
- Lock the bound placeholder and binding-ID grammar.
- Lock the new bound-key metadata contract and explicit legacy-v1.0 compatibility status.
- Lock canonical mapping-digest input and expected digest fixtures.
- Lock fail-closed mismatch, mixed-ID, missing-binding and invalid-digest behavior.
- Lock the document-first three-step UX boundary without new confirmation gates.
- Define pure helper API expectations for the subsequent model implementation.

Boundaries:
- Specification, fixtures and contract tests only.
- No product helper, UI, placeholder generation, Scrub Key schema implementation, export or reinsert behavior change.
- No cloud, AI, OCR, server secret or signing-key storage.
- Synthetic data only.
- Human review remains required; no production-readiness claim.

Next step:
- Add the versioned contract/specification and green source/fixture-level tests, then hand over to `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.
