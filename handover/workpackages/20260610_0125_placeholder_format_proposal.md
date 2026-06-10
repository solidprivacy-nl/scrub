# Handover — WP31 LLM-resistant placeholder format proposal

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP31 — LLM-resistant placeholder format proposal`

Status: completed architecture/proposal-only.

## Summary

WP31 created and verified `PLACEHOLDER_FORMAT_PROPOSAL.md`.

The proposal compares these required styles:

```text
[PERSOON_1]
[[SP_PERSON_0001_A7F3]]
{{SP:PERSON:0001:A7F3}}
⟦SP_PERSON_0001_A7F3⟧
```

Recommended future architecture direction:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

Primary example:

```text
[[SP_PERSON_0001_A7F3]]
```

The proposal defines current placeholder limitations, candidate formats, recommended format, entity naming convention, counter format, integrity-token direction, readability, LLM robustness, copy/paste robustness, TXT/DOCX/PDF compatibility, Scrub Key compatibility, backward compatibility, migration risks, audit/validation requirements, implementation phases and next workpackages.

The proposal includes the required rule:

```text
Do not derive visible checksum/integrity values directly from original sensitive data.
```

## Files added

- `PLACEHOLDER_FORMAT_PROPOSAL.md`
- `handover/workpackages/20260610_0035_placeholder_format_proposal.md`
- `handover/workpackages/20260610_0125_placeholder_format_proposal.md`

## Files changed

- None in this completion pass.

## Documentation note

Earlier WP31 attempts to update shared documentation files were blocked by the GitHub connector/tool safety layer:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

The proposal and handover files were committed successfully. No unsafe overwrite or workaround was used.

## Tests

- No tests run.
- No tests added or changed.
- Reason: WP31 is architecture/proposal-only.

## Validation status

- Required context was read.
- `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, `SCRUB_KEY_SPEC.md` and `PARALLEL_SPEC_CONSOLIDATION_WP58.md` were read.
- Existing reinsert helpers and tests were inspected for context only.
- Verified that no reinsert logic was changed.
- Verified that no placeholder migration was implemented.
- Verified that no Scrub Key schema change was implemented.

## GitHub Actions status

- Unknown at handover creation time.
- No code or test files changed.

## Hugging Face sync status

- Unknown at handover creation time.
- No app/runtime behavior changed.

## App verification status

- Not applicable.
- No UI behavior changed.

## Remaining risks

- Recommended robust placeholder format is not implemented.
- No checksum/validation helper exists yet.
- No near-miss placeholder detection exists yet.
- No synthetic AI-output corruption tests exist yet.
- No robust placeholder generation or migration exists yet.
- Shared status/risk/decision/changelog documentation still needs update once the connector block is resolved.

## Next recommended step

`WP32 — Placeholder checksum/validation helper`.
