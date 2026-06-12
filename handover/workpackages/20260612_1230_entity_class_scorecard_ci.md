# Handover — WP23 Entity-class scorecard in CI

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP23 — Entity-class scorecard in CI`

Status: completed report-only CI/entity-class scorecard foundation.

## Summary

WP23 adds a CI-friendly, report-only entity-class scorecard wrapper around the WP22 recall/precision runner.

The helper can write structured JSON and Markdown scorecard artifacts under `benchmark/reports/`. It preserves the benchmark boundary: synthetic data only, no recognizer logic changes, no Streamlit UI changes, no dependency changes, no export/reinsert behavior changes, no cloud processing and no production-blocking threshold.

## Files added

- `benchmark/build_entity_scorecard.py`
- `benchmark/reports/README.md`
- `tests/test_entity_scorecard.py`
- `handover/workpackages/20260612_1230_entity_class_scorecard_ci.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

- `python -m py_compile benchmark/build_entity_scorecard.py` — passed in the ChatGPT execution sandbox against the authored helper. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_entity_scorecard.py` — passed in the ChatGPT execution sandbox against the authored tests; 4 passed. The sandbox emitted the same unrelated spreadsheet runtime warmup warning, but pytest returned success.
- `pytest tests/test_recall_precision_runner.py` — requested, but not run in a live GitHub repository checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository. WP22 previously recorded the targeted runner tests as passed in its implementation sandbox.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` — requested, but not run in a live GitHub repository checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository. The schema was fetched and inspected through GitHub.

## Validation status

- Scorecard JSON includes overall metrics, per-domain metrics, per-entity-class metrics, gold count, prediction count, exact and normalized true positives, false-negative count, false-positive count, preserve-term failures, known-trap failures and partial-overlap diagnostic count.
- Scorecard JSON explicitly records `synthetic_only: true`, `report_only: true`, `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- Markdown output includes the same report-only policy and no-production-safety-claim warning.
- CI may publish the scorecard and may fail on technical errors such as malformed JSON, bad offsets or runner exceptions.
- CI must not fail on recall/precision scores yet.
- No workflow threshold or production gate was added.
- No recognizer logic changed.
- No Streamlit UI changed.
- No dependency changes.
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

- Existing gold sidecars are still schema examples only, not complete gold labels for the full corpus.
- The scorecard wraps the WP22 runner, which scores supplied prediction JSON only; it does not invoke recognizers or establish baselines.
- No recall/precision threshold or production-blocking gate exists.
- No false-negative residual-risk report exists yet.
- No production safety claim is supported.

## Next recommended step

- `WP24 — False-negative residual-risk report`.
