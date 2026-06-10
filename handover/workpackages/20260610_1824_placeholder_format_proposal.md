# Handover — WP31 LLM-resistant placeholder format proposal

Repository: `solidprivacy-nl/scrub`

Workpackage title: `WP31 — LLM-resistant placeholder format proposal`

Status: completed architecture/proposal-only.

## Summary

WP31 is completed as a proposal-only architecture package.

The proposal defines current placeholder limitations, compares required candidate formats, recommends a future robust format direction, and documents naming, counter, integrity-token, readability, LLM robustness, copy/paste, TXT/DOCX/PDF, Scrub Key compatibility, backward compatibility, migration, audit/validation and implementation-phase requirements.

Recommended future placeholder direction:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

Example:

```text
[[SP_PERSON_0001_A7F3]]
```

The proposal explicitly keeps legacy placeholders such as `[PERSOON_1]` backward-compatible and records that visible checksum/integrity values must not be derived directly from original sensitive data.

## Files added

- `PLACEHOLDER_FORMAT_PROPOSAL.md`
- `handover/workpackages/20260610_1824_placeholder_format_proposal.md`

## Files changed

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests were added or changed.
- No tests were run because this workpackage is documentation/proposal-only and changed no code.

## Validation

- Required start sequence was read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Additional context was read: `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, `SCRUB_KEY_SPEC.md`, `PARALLEL_SPEC_CONSOLIDATION_WP58.md`.
- Context-only files were inspected: `scrub_key_reinsert.py`, `scrub_key_document_reinsert.py`, `scrub_key_pdf_text_reinsert.py`, `tests/test_scrub_key_reinsert.py`, `tests/test_scrub_key_document_reinsert.py`.
- Confirmed no reinsert helper logic changed.
- Confirmed no placeholder migration was implemented.
- Confirmed no Scrub Key schema change was made.
- Confirmed no UI, export behavior, dependency, AI/cloud or test changes were made.

## GitHub Actions status

- To be checked after commit/push.

## Hugging Face sync status

- To be checked after commit/push.

## App verification status

- Not applicable. No UI behavior changed.

## Remaining risks

- The robust placeholder format is not implemented.
- No placeholder checksum/validation helper exists yet.
- No near-miss placeholder detection exists yet.
- No synthetic AI-output corruption tests exist yet.
- No robust placeholder generation, migration or Scrub Key schema/version support exists yet.

## Next recommended step

`WP32 — Placeholder checksum/validation helper`.
