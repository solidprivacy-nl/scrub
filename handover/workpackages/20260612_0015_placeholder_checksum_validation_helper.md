# Handover — WP32 Placeholder checksum/validation helper

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP32 — Placeholder checksum/validation helper`

Status: completed helper/tests-only, with central documentation update limitation.

## Summary

Implemented an additive placeholder validation helper for the future robust placeholder shape:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

The helper:

- recognizes and validates robust placeholders;
- parses entity type, four-digit counter and four-hex integrity token;
- computes deterministic four-hex integrity tokens from non-sensitive placeholder metadata only: validation version, `SP`, entity type and counter;
- rejects malformed, truncated, invalid-prefix, invalid-entity, invalid-counter, invalid-integrity and integrity-mismatch robust placeholder candidates;
- detects legacy placeholders separately as compatibility mode;
- classifies other placeholder-like strings without repair or migration.

The integrity helper deliberately does not accept or hash original sensitive values. It is a lightweight corruption-detection helper, not cryptographic authenticity or Scrub Key tamper protection.

## Files added

- `placeholder_validation.py`
- `tests/test_placeholder_validation.py`
- `handover/workpackages/20260612_0015_placeholder_checksum_validation_helper.md`

## Files changed

- None safely updated after the helper/test/handover commits.

## Documentation update limitation

The workpackage asked to update `WORKPACKAGES.md` and `CHANGELOG.md`. Those files are long shared coordination documents and must be updated via full-file replacement through the available GitHub connector. During this run, the full current contents could not be safely reconstructed from the connector output without risking a partial overwrite of parallel worker changes. I therefore did not overwrite them.

Required central documentation still to record in a follow-up closeout:

- WP32 completed helper/tests-only.
- Files added: `placeholder_validation.py`, `tests/test_placeholder_validation.py`, this handover.
- No placeholder migration.
- No robust placeholder generation in product flow.
- No Scrub Key schema change.
- No reinsert behavior change.
- No UI/export/dependency/AI/cloud change.
- Next recommended step: `WP33 — Unknown/changed placeholder audit hardening`.

## Tests/checks run

Run in a local ChatGPT runtime copy of the WP32 helper and test files:

```text
python -m py_compile placeholder_validation.py tests/test_placeholder_validation.py
PYTHONPATH=. pytest tests/test_placeholder_validation.py -q
```

Result:

```text
12 passed
```

The broader requested command was not run:

```text
pytest tests -k "placeholder or scrub_key or reinsert"
```

Reason: a full repository checkout was not available in the ChatGPT runtime, and network cloning from GitHub failed in the container environment. The focused WP32 helper tests were run successfully.

## Validation status

- Required start sequence read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Additional context read: `AGENTS.md`, `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, `PLACEHOLDER_FORMAT_PROPOSAL.md`, `SCRUB_KEY_SPEC.md`, `PARALLEL_SPEC_CONSOLIDATION_WP58.md`, `scrub_key.py`, `scrub_key_reinsert.py`, `RISK_REGISTER.md`, `DECISION_LOG.md`.
- Confirmed no edit to `scrub_key.py`.
- Confirmed no edit to `scrub_key_reinsert.py`.
- Confirmed no Streamlit UI change.
- Confirmed no Scrub Key schema change.
- Confirmed no placeholder generation change.
- Confirmed no placeholder migration.
- Confirmed no export/reinsert behavior change.
- Synthetic placeholder test values only; no real personal, legal, care, customer or confidential data.
- No AI/cloud integration and no dependency change.

## GitHub Actions status

- Unknown at handover creation time.
- Status lookup should be performed against the final handover commit.

## Hugging Face sync status

- Unknown at handover creation time.
- No app/runtime behavior changed.

## App verification status

- Not applicable.
- No UI behavior changed.

## Remaining risks

- Central `WORKPACKAGES.md` and `CHANGELOG.md` closeout entries still need to be added safely.
- The helper is not integrated into reinsert/audit flows yet.
- No near-miss audit/reporting integration yet.
- No synthetic AI-output corruption test package yet.
- The four-hex metadata checksum detects simple corruption but does not provide cryptographic authenticity or Scrub Key tamper protection.
- Stronger authenticity must remain coordinated with Scrub Key integrity/security work.
- Placeholder generation and migration remain gated future work.

## Next recommended step

`WP32-CLOSEOUT — Placeholder validation helper central docs repair`, then `WP33 — Unknown/changed placeholder audit hardening`.
