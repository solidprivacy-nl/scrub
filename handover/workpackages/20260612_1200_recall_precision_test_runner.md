# Handover — WP22 Recall/precision test runner

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP22 — Recall/precision test runner`

Status: completed report-only benchmark runner implementation.

## Summary

WP22 adds the first deterministic local recall/precision runner for the synthetic benchmark foundation created in WP19/WP20/WP21.

The runner reads WP21 gold-label sidecars and optional supplied prediction JSON, validates source-file references and offsets, then emits structured report-only metrics. It does not call recognizers, Presidio, Streamlit, AI, cloud services or CI gates.

## Files added

- `benchmark/run_recall_precision.py`
- `tests/test_recall_precision_runner.py`
- `handover/workpackages/20260612_1200_recall_precision_test_runner.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

- `python -m py_compile benchmark/run_recall_precision.py` — passed in the ChatGPT execution sandbox against the authored runner.
- `pytest -q tests/test_recall_precision_runner.py` — passed in the ChatGPT execution sandbox against the authored tests; 3 passed.
- `benchmark/gold/schema/gold_label_schema.json` was fetched and inspected through the GitHub connector. `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was not run inside a live GitHub checkout because this ChatGPT GitHub connector does not provide shell execution in the repository checkout.

## Validation status

- Runner validates `synthetic: true` sidecars.
- Runner validates `source_file` references.
- Runner validates zero-based inclusive `start` and exclusive `end` semantics by checking `text == source_text[start:end]`.
- Runner reports exact and value-normalized recall/precision separately.
- Runner reports per-domain and per-entity-class metrics.
- Runner reports false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps.
- Runner is report-only and applies no CI threshold.
- No recognizer logic changed.
- No Streamlit UI changed.
- No dependencies changed.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

## GitHub Actions status

To be checked after final handover commit.

## Hugging Face sync status

To be checked after final handover commit.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- Current sidecars are schema examples only, not complete gold-label sidecars for the full corpus.
- The runner scores supplied prediction JSON only; it does not invoke current recognizers or define accepted baselines.
- No CI scorecard exists yet.
- No production-blocking threshold exists.
- No false-negative residual-risk report exists yet.

## Next recommended step

- `WP23 — Entity-class scorecard in CI`.
