# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Status: in_progress

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 19:56 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-model-implementation

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB_KEY_BINDING_CONTRACT.md` and its fixed fixture are green.

Scope:
- Implement pure, Streamlit-free binding-ID generation/validation.
- Implement bound automatic/manual placeholder build/parse helpers.
- Implement canonical mapping-digest payload and SHA-256 digest helpers.
- Implement bound Scrub Key validation.
- Implement document/key binding validation with explicit bound and legacy statuses.
- Preserve immutable inputs and stable result fields.

Boundaries:
- Pure model/helper implementation only.
- No changes to current automatic/manual placeholder generation paths.
- No Scrub Key export integration.
- No reinsert helper or UI integration.
- No automatic legacy migration.
- No signing/HMAC, secret storage, cloud, AI or OCR.
- Synthetic data only.
- Human review remains required; no production-readiness claim.

Next step:
- Add the pure binding model and implementation tests against the frozen contract, then hand over to `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after green validation.
