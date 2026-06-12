# Changelog — SolidPrivacy Scrub

## WP24 — False-negative residual-risk report

Status: completed report-only false-negative residual-risk report foundation.

Purpose:

- Make remaining false-negative and coverage risks explicit after WP19/WP20/WP21/WP22/WP23.
- Provide a report-only residual-risk helper for internal/support risk communication.
- Keep the work synthetic-only and avoid any production safety claim, threshold or gate.

Files added:

- `benchmark/build_residual_risk_report.py`
- `tests/test_residual_risk_report.py`
- `handover/workpackages/20260612_1300_false_negative_residual_risk_report.md`

Files changed:

- `benchmark/reports/README.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `benchmark/build_residual_risk_report.py`, a pure-stdlib report-only helper that consumes a WP23 scorecard or builds one through the existing WP22/WP23 helpers.
- The helper can write `benchmark/reports/false_negative_residual_risk_report.json` and `benchmark/reports/false_negative_residual_risk_report.md`.
- The report includes synthetic-only warning, report-only/no-production-safety policy, current benchmark coverage status, schema-example limitation, supplied-prediction limitation, overall false-negative risk, per-domain residual risk, per-entity-class residual risk, preserve-term risk, known-trap/false-positive risk, partial-overlap/near-miss diagnostics, unsupported/not-yet-baselined classes and recommended next work.
- The report explicitly records `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- Added `tests/test_residual_risk_report.py` for policy fields, coverage limitations, risk summaries, unsupported/not-yet-baselined classes, Markdown rendering and output writing.
- Updated `benchmark/reports/README.md` to document generated residual-risk report artifacts and the no-real-data/no-production-claim boundary.

Validation status:

- `python -m py_compile benchmark/build_residual_risk_report.py` passed in the ChatGPT execution sandbox against the authored helper. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_residual_risk_report.py` passed in the ChatGPT execution sandbox against the authored tests: 4 passed. The sandbox emitted the same unrelated spreadsheet runtime warmup warning, but pytest returned success.
- `pytest tests/test_recall_precision_runner.py` and `pytest tests/test_entity_scorecard.py` were requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector. WP22/WP23 previously recorded their targeted tests as passed in the implementation sandbox.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector. The schema was fetched and inspected through GitHub.
- GitHub Actions: to be checked after final handover commit.
- Hugging Face sync: to be checked after final handover commit.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No Presidio integration changed.
- No Streamlit UI changed.
- No recall/precision threshold added.
- No production-blocking gate added.
- No production safety claim added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if the coordinator wants to continue the placeholder line first: `WP33 — Unknown/changed placeholder audit hardening`.

## WP23 — Entity-class scorecard in CI

Status: completed report-only CI/entity-class scorecard foundation.

Purpose:

- Make the WP22 recall/precision runner visible through CI-friendly entity-class scorecard artifacts.
- Keep benchmark reporting report-only with no production threshold or safety claim.
- Preserve recognizer logic, Streamlit UI, export/reinsert behavior, dependencies and cloud boundaries.

Files added:

- `benchmark/build_entity_scorecard.py`
- `benchmark/reports/README.md`
- `tests/test_entity_scorecard.py`
- `handover/workpackages/20260612_1230_entity_class_scorecard_ci.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `benchmark/build_entity_scorecard.py`, a pure-stdlib wrapper around `benchmark/run_recall_precision.py`.
- The helper can write `benchmark/reports/entity_scorecard.json` and `benchmark/reports/entity_scorecard.md`.
- Scorecard JSON includes `synthetic_only: true`, `report_only: true`, `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- Scorecard policy states that CI may publish the report and may fail on technical errors such as malformed JSON, bad offsets or runner exceptions, but must not fail on recall/precision scores yet.
- Scorecard output includes overall recall/precision, per-domain metrics, per-entity-class metrics, gold/prediction counts, exact and normalized true positives, false-negative and false-positive counts, preserve-term failures, known-trap failures and partial-overlap diagnostic counts.
- Added `benchmark/reports/README.md` to explain generated report artifacts and the no-real-data/no-production-claim boundary.
- Added `tests/test_entity_scorecard.py` for scorecard policy fields, zero rows for entity classes, Markdown rendering and output writing.

Validation status:

- `python -m py_compile benchmark/build_entity_scorecard.py` passed in the ChatGPT execution sandbox against the authored helper.
- `pytest -q tests/test_entity_scorecard.py` passed in the ChatGPT execution sandbox against the authored tests: 4 passed.
- `pytest tests/test_recall_precision_runner.py` was requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector. WP22 already recorded the targeted runner tests as passed in the implementation sandbox.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector. The schema was fetched and inspected through GitHub.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No Presidio integration changed.
- No Streamlit UI changed.
- No CI threshold or production-blocking gate added.
- No production safety claim added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP24 — False-negative residual-risk report`.

## WP32-CLOSEOUT — Placeholder validation helper central docs repair

Status: completed documentation/coordination-only.

Purpose:

- Complete central documentation for WP32 after the helper and tests were added.
- Record the additive placeholder validation helper status without changing code, tests, UI, reinsert, export or Scrub Key schema behavior.
- Move the placeholder robustness line to WP33.

Files added:

- `handover/workpackages/20260612_0030_placeholder_validation_helper_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP32 artifacts recorded:

- `placeholder_validation.py`
- `tests/test_placeholder_validation.py`
- `handover/workpackages/20260612_0015_placeholder_checksum_validation_helper.md`

Main closeout points:

- WP32 is completed helper/tests-only.
- The helper recognizes and validates the future robust placeholder form `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`.
- The helper parses entity type, counter and integrity token.
- The helper generates deterministic integrity tokens from non-sensitive placeholder metadata.
- Integrity tokens are not derived directly from original sensitive values.
- Legacy placeholders remain a separate compatibility mode.
- No placeholder migration, robust placeholder generation, Scrub Key schema change, reinsert behavior change, UI/export/dependency change or AI/cloud processing was added.

Validation status:

- Documentation/coordination repair only.
- Prior WP32 targeted checks were recorded as passed: `python -m py_compile placeholder_validation.py tests/test_placeholder_validation.py` and `PYTHONPATH=. pytest tests/test_placeholder_validation.py -q` with 12 passed.
- The broader command `pytest tests -k "placeholder or scrub_key or reinsert"` was not run in the prior WP32 worker because a full repository checkout was unavailable in the ChatGPT runtime.
- No code or test files were changed in this closeout.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No code changed.
- No tests changed.
- No placeholder migration.
- No robust placeholder generation in product flow.
- No Scrub Key schema migration.
- No reinsert behavior change.
- No Streamlit UI change.
- No export behavior change.
- No dependency change.
- No AI/cloud integration.
- No real data added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP33 — Unknown/changed placeholder audit hardening`.

## WP22 — Recall/precision test runner

Status: completed report-only benchmark runner implementation.

Purpose:

- Make synthetic benchmark detection quality measurable after WP19/WP20/WP21.
- Add a deterministic local runner for WP21 gold-label sidecars and supplied prediction JSON.
- Keep the first runner report-only with no recognizer logic changes, no Streamlit UI changes, no CI gate and no production-blocking threshold.

Files added:

- `benchmark/run_recall_precision.py`
- `tests/test_recall_precision_runner.py`
- `handover/workpackages/20260612_1200_recall_precision_test_runner.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `benchmark/run_recall_precision.py`, a pure-stdlib deterministic runner.
- The runner loads WP21 sidecars, validates `synthetic: true`, verifies source file references and checks `text == source_text[start:end]` for labels, preserve terms and known traps.
- The runner accepts optional prediction JSON and reports exact and value-normalized recall/precision.
- Metrics include overall summary, per-domain metrics, per-entity-class metrics, false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps.
- Partial overlap is explicitly diagnostic-only and does not hide false negatives.
- Schema-example sidecars are included by default with warnings so current examples can be used for runner validation without implying full benchmark coverage.
- Added `tests/test_recall_precision_runner.py` covering exact/normalized scoring, preserve/trap failure reporting, malformed gold-label offset rejection and CLI JSON output.

Validation status:

- `python -m py_compile benchmark/run_recall_precision.py` passed in the ChatGPT execution sandbox against the authored runner.
- `pytest -q tests/test_recall_precision_runner.py` passed in the ChatGPT execution sandbox against the authored tests: 3 passed.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was requested; the schema was fetched and inspected through GitHub, but the GitHub connector does not provide a shell in the repository checkout. The runner itself parses JSON sidecars with Python stdlib.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No Presidio integration changed.
- No Streamlit UI changed.
- No CI scorecard or production test gate added.
- No production-blocking threshold added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP23 — Entity-class scorecard in CI`.

## Earlier completed work

- WP28-REPAIR — Scrub Key expiry/delete policy artifact repair.
- WP21-CLOSEOUT — Gold-label schema handover and central docs repair.
- WP28 — Scrub Key expiry/delete policy.
- WP46 — Minimal local Streamlit launcher.
- WP31 — LLM-resistant placeholder format proposal.
- WP27 — Scrub Key warning UX plan.
- WP45 — Local runtime architecture plan.
- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
- WP26 — Scrub Key encryption/lifecycle specification.
- WP58 — Parallel specification consolidation and next execution queue.
- WP35 — DOCX hidden content risk review.
- WP30 — Placeholder robustness review.
- WP25 — Scrub Key threat model.
- WP19 — Recall benchmark specification.
- WP18C — Add Codex worker governance instructions.
- Earlier UI, PDF helper, Scrub Key, reinsert and Review UX work as recorded in repository history.
