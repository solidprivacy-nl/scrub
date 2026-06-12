# Handover — WP34 Synthetic AI-output placeholder corruption tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP34 — Synthetic AI-output placeholder corruption tests`

Status: completed synthetic fixtures/tests-only.

## Summary

Added synthetic AI-output-style placeholder corruption fixtures and tests after WP33. The work stays report/audit focused and does not change product behavior.

The new tests cover:

- exact legacy placeholder preservation with punctuation;
- translated legacy placeholder labels;
- summarization/deletion of placeholders;
- markdown/HTML wrapping around exact tokens;
- HTML split tokens;
- spacing mutation;
- robust placeholder truncation;
- robust integrity mismatch;
- placeholder merge/deletion;
- invented curly placeholder-like tokens.

The tests assert that unknown, malformed, truncated and failed-integrity tokens are not repaired or guessed, and that missing expected placeholders remain visible through helper audit output.

## Files added

- `tests/fixtures/placeholder_corruption/ai_output_corruption_cases.json`
- `tests/test_placeholder_corruption_scenarios.py`
- `handover/workpackages/20260612_0140_synthetic_ai_placeholder_corruption_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

Run in a local ChatGPT runtime copy of the relevant helper/test files:

```text
python -m py_compile placeholder_validation.py placeholder_audit.py scrub_key.py scrub_key_reinsert.py tests/test_placeholder_corruption_scenarios.py
PYTHONPATH=. pytest -q tests/test_placeholder_corruption_scenarios.py
```

Result:

```text
11 passed
```

## Validation status

- Required start sequence read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Additional context read: `AGENTS.md`, placeholder specs/reviews, Scrub Key/reinsert helpers, WP32/WP33 helper/test files and relevant handovers.
- Confirmed no helper logic change.
- Confirmed no Streamlit UI change.
- Confirmed no export behavior change.
- Confirmed no reinsert behavior change.
- Confirmed no Scrub Key schema migration.
- Confirmed no placeholder migration.
- Confirmed no robust placeholder generation in product flow.
- Confirmed no dependency change.
- Synthetic test values only; no real personal, legal, care, customer or confidential data.
- No AI/cloud integration.

## GitHub Actions status

- To be checked after final handover commit.

## Hugging Face sync status

- To be checked after final handover commit.

## App verification status

- Not applicable.
- No UI behavior changed.

## Remaining risks

- `placeholder_audit.py` is not wired into product UI/export/reinsert flows yet.
- Robust placeholder generation remains blocked/gated until schema/format policy is explicitly approved.
- Placeholder migration remains blocked/gated.
- User-visible placeholder corruption warnings remain future audit/UI work.

## Next recommended step

- Placeholder line: later gated robust placeholder generation and compatibility implementation only after schema/format policy approval.
- Active non-placeholder queue: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation` or `WP47 — Local file handling/privacy test`, depending on coordinator priority.
