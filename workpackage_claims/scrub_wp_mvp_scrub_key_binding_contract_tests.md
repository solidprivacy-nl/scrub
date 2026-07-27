# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Status: completed; contract frozen; full suite passed; final clean PR validation pending

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

Validation result:
- Contract specification and versioned fixture added.
- Binding grammar, canonical digest, legacy status, fail-closed status matrix and three-step UX contracts added.
- Canonical synthetic digest independently recomputed.
- Full repository suite: 845 passed.
- GitHub Actions run #1703 passed before temporary diagnostic cleanup.
- Temporary diagnostic workflow and log removed.
- Binding ID: `B[A-Z2-7]{16}` with an 80-bit random payload.
- Bound automatic/manual placeholder grammar frozen.
- Bound-key schema direction `1.1`, binding version `1` and canonical SHA-256 mapping digest frozen.
- Eight binding statuses and six fail-closed states frozen.
- Legacy v1.0 remains explicit unbound compatibility.
- Three-step reinsert UX and final download acknowledgement preserved.
- Implementation authorized in this package: false.
- Product code changed: false.
- Production ready: false; human review required: true.
- Evidence: `output/validation/mvp_scrub_key_binding_contract_validation.json`.
- Handover: `handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md`.

Next step:
- Verify the final clean PR run, merge PR #42 and start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.
