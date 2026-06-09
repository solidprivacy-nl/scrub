# Handover — WP31 LLM-resistant placeholder format proposal

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP31 — LLM-resistant placeholder format proposal`

Status: completed architecture/proposal-only, with partial documentation-update limitation noted below.

## Summary

WP31 created `PLACEHOLDER_FORMAT_PROPOSAL.md` as an architecture/proposal-only document. It compares the required placeholder styles and recommends the future direction:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

Example:

```text
[[SP_PERSON_0001_A7F3]]
```

The proposal keeps legacy placeholders such as `[PERSOON_1]` as backward-compatible legacy format and explicitly states that robust support must be additive first. It also warns that visible checksum/integrity values must not be derived directly from original sensitive data.

## Files added

- `PLACEHOLDER_FORMAT_PROPOSAL.md`
- `handover/workpackages/20260610_0035_placeholder_format_proposal.md`

## Files changed

- None successfully changed after the proposal file.

## Documentation update limitation

The workpackage required updates to `DECISION_LOG.md`, `RISK_REGISTER.md`, `WORKPACKAGES.md` and `CHANGELOG.md` where applicable.

The following update attempts were made but blocked by the GitHub connector/tool safety checks:

- `DECISION_LOG.md` — attempted to record the recommended architecture direction.
- `RISK_REGISTER.md` — attempted to update placeholder-corruption mitigation and remaining gaps.
- `WORKPACKAGES.md` — attempted to record WP31 completion and next queue.

Because these writes were blocked by the tool, they were not committed. No overwrite or unsafe workaround was performed.

## Tests

- No tests were added.
- No tests were changed.
- No test suite was run because WP31 is architecture/proposal-only and did not change code.

## Validation status

- Required start sequence was read.
- Relevant risk, decision, monitoring, release notes and specification files were read.
- Existing reinsert helpers and tests were inspected for context only.
- Verified that no reinsert logic was changed.
- Verified that no placeholder migration was implemented.

## GitHub Actions status

- Unknown at handover creation time.
- This was documentation/proposal-only and no code or test files were changed.

## Hugging Face sync status

- Unknown at handover creation time.
- No app/runtime behavior changed.

## App verification status

- Not applicable.
- No UI behavior changed.

## Remaining risks

- The proposed robust format is not implemented.
- No checksum/validation helper exists yet.
- No near-miss placeholder detection exists yet.
- No synthetic AI-output corruption tests exist yet.
- No migration or backward-compatibility implementation exists yet.
- Shared documentation files still need to be updated once the tool update block is resolved.

## Next recommended step

- Resolve the documentation-update block, then proceed to `WP32 — Placeholder checksum/validation helper`.
