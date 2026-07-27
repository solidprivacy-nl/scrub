# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Status: implemented; targeted validation passed; PR verification pending

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
- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`.


Implementation result:
- Pure module: `scrub_key_binding.py`.
- Frozen binding ID, placeholder, digest and status contracts implemented.
- Eight statuses and six fail-closed paths implemented.
- Explicit legacy-v1.0 unbound compatibility implemented.
- Targeted model/contract/legacy/roundtrip validation passed.
- Current export integrated: false.
- Current reinsert integrated: false.
- Product UI changed: false.
- Production ready: false; human review required: true.
- Evidence: `output/validation/mvp_scrub_key_binding_model_validation.json`.
- Handover: `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`.
