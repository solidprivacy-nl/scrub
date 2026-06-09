# Handover — WP30 Placeholder robustness review

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP30 — Placeholder robustness review`

Status: completed architecture/specification-only.

## Summary

WP30 reviewed how current Scrub placeholders survive AI rewriting, translation, summarization, punctuation/spacing changes, markdown/HTML formatting and document conversion. The work documents the current exact-match reinsert assumptions, placeholder corruption examples, candidate robust placeholder directions, checksum ideas, validation/audit ideas, migration risks and backward compatibility concerns.

This workpackage did not implement or mandate a new placeholder format.

## Files added

- `PLACEHOLDER_ROBUSTNESS_REVIEW.md`
- `handover/workpackages/20260609_2310_placeholder_robustness_review.md`

## Files changed

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests run.
- No test files added or changed.
- Reason: WP30 is architecture/specification-only and did not change code, helper logic, UI, dependencies or export behavior.

## Validation status

- Documentation review completed against the required WP30 content list.
- Context inspected: `SCRUB_KEY_SPEC.md`, `scrub_key_reinsert.py`, `scrub_key_document_reinsert.py`, `scrub_key_pdf_text_reinsert.py`, `tests/test_scrub_key_reinsert.py`, `tests/test_scrub_key_document_reinsert.py`.
- Verified that WP30 stayed inside allowed files and did not change reinsert logic.

## GitHub Actions status

- Unknown at handover creation time.
- Documentation/specification-only change; no code or tests changed.
- A connector status lookup can be performed after the final handover commit exists.

## Hugging Face sync status

- Unknown at handover creation time.
- No UI or runtime behavior changed.
- A connector status lookup can be performed after the final handover commit exists.

## App verification status

- Not applicable.
- No UI behavior changed.

## Main architecture findings

- Current placeholders such as `[PERSOON_1]`, `[ZAAKNUMMER_1]`, `[ADRES_1]` and `[ORGANISATIE_01]` are readable and deterministic but fragile under AI translation, summarization, punctuation/spacing changes, markdown/HTML formatting and document conversion.
- Current reinsert depends on exact placeholder strings from the Scrub Key mapping.
- Existing audit fields for unknown, duplicate and not-found placeholders are a useful foundation but do not yet detect checksum failures, near-misses, placeholder deletion or semantic placeholder merges.
- Candidate robust formats such as `[[SP_PERSON_0001_A7F3]]`, `[[SP_BSN_0002_C91B]]` and `[[SP_ADDRESS_0003_D41A]]` should remain proposals only until WP31.
- Checksum design must avoid deriving visible values directly from original sensitive data.
- Backward compatibility with legacy placeholders is mandatory.

## Intentionally not changed

- No code changed.
- No placeholder migration.
- No placeholder format changed.
- No Scrub Key schema change.
- No reinsert helper change.
- No UI change.
- No AI/cloud integration.
- No tests added or changed.
- No export behavior change.
- No final placeholder format mandated.

## Remaining risks

- No LLM-resistant placeholder format has been accepted or implemented.
- No checksum/validation helper exists yet.
- No near-miss placeholder detection exists yet.
- No synthetic AI-output corruption tests exist yet.
- No migration or backward-compatibility implementation exists yet.
- Silent placeholder deletion or merge during summarization remains a high-risk AI-roundtrip failure mode.

## Next recommended step

- `WP31 — LLM-resistant placeholder format proposal`.
