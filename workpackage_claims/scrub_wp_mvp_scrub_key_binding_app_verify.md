# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY

Status: in_progress; technical deployment and synthetic fixtures verified; live app verification pending

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-28 01:13 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-app-verify

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` — merged as PR #43.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` — merged as PR #44.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION` — merged as PR #45 (`4a21c2d93acf3c166534a4a0501e602954c5606d`).

Technical evidence:
- Post-merge GitHub Tests run for `4a21c2d9…`: success.
- GitHub-to-Hugging-Face sync run for `4a21c2d9…`: success.
- Hugging Face mirror SHA: exact match with `4a21c2d9…`.
- Hugging Face runtime stage: `RUNNING`.
- Deployment evidence: `output/validation/mvp_scrub_key_binding_post_merge_probe.json`.
- Synthetic fixture contract validated against deployed product helpers.
- Fixture evidence: `output/validation/mvp_scrub_key_binding_app_fixture_validation.json`.

Live verification scope:
- Correct bound DOCX/key pair restores body, table, header and footer and shows a verified match.
- Structurally valid wrong bound key is blocked before restoration and produces no restored download.
- Correct binding with a tampered mapping digest is rejected before restoration.
- Legacy v1.0 document/key pair remains usable with a visible unverified-match warning.
- Bound text-based PDF follows the existing verified PDF-to-TXT route without OCR or restored PDF.
- New anonymization/export output uses one shared binding ID in default placeholders and schema-1.1 Scrub Key metadata.
- The three-step document-first flow and only one final confidentiality acknowledgement remain.
- No Script execution error is visible.

Boundaries:
- Verification/closeout only; no product code, UI, schema, export or reinsert changes.
- Synthetic data only.
- Human review remains required; production readiness remains false.

Next step:
- Obtain coordinator live-app evidence, then create the docs-only closeout PR and proceed to `SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE`.
