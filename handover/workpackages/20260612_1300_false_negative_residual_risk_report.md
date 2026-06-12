# Handover — WP24 False-negative residual-risk report

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP24 — False-negative residual-risk report`

Status: completed report-only false-negative residual-risk report foundation.

## Summary

WP24 adds a report-only false-negative residual-risk report helper on top of the WP22/WP23 benchmark foundation.

The helper consumes a WP23 entity-class scorecard or builds one through the WP22/WP23 helper chain, then writes JSON and Markdown residual-risk artifacts under `benchmark/reports/`. It makes remaining coverage and false-negative risk explicit, without changing recognizer logic, UI, dependencies, export/reinsert behavior or cloud-processing boundaries.

## Files added

- `benchmark/build_residual_risk_report.py`
- `tests/test_residual_risk_report.py`
- `handover/workpackages/20260612_1300_false_negative_residual_risk_report.md`

## Files changed

- `benchmark/reports/README.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests/checks run

- `python -m py_compile benchmark/build_residual_risk_report.py` — passed in the ChatGPT execution sandbox against the authored helper. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_residual_risk_report.py` — passed in the ChatGPT execution sandbox against the authored tests; 4 passed. The sandbox emitted the same unrelated spreadsheet runtime warmup warning, but pytest returned success.
- `pytest tests/test_recall_precision_runner.py` — requested, but not run in a live GitHub repository checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository. WP22 previously recorded the targeted runner tests as passed in its implementation sandbox.
- `pytest tests/test_entity_scorecard.py` — requested, but not run in a live GitHub repository checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository. WP23 previously recorded the targeted scorecard tests as passed in its implementation sandbox.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` — requested, but not run in a live GitHub repository checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository. The schema was fetched and inspected through GitHub.

## Validation status

- Residual-risk JSON includes synthetic-only warning, report-only policy, current benchmark coverage status, known limitation that current gold sidecars are schema examples only, known limitation that the runner scores supplied prediction JSON only, overall false-negative risk summary, per-domain residual-risk summary, per-entity-class residual-risk summary, preserve-term risk summary, known-trap/false-positive risk summary, partial-overlap/near-miss diagnostic summary, unsupported/not-yet-baselined classes, recommended next benchmark/data work and recommended next product-risk mitigations.
- Residual-risk Markdown contains the same no-production-safety-claim and no-threshold guidance.
- The report explicitly records `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- Technical errors may still fail, but low scores do not fail CI or create a production gate.
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
- The runner/scorecard/residual-risk report still score supplied prediction JSON only; they do not invoke recognizers or establish accepted baselines.
- No recall/precision threshold or production-blocking gate exists.
- No production safety claim is supported.
- No user-facing residual-risk/audit integration exists yet.

## Next recommended step

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if the coordinator wants to continue the placeholder line first: `WP33 — Unknown/changed placeholder audit hardening`.
