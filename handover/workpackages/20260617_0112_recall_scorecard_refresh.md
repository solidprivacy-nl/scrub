# Handover — WP_RECALL_SCORECARD_REFRESH

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_SCORECARD_REFRESH — Refresh recall/precision scorecard after Dutch legal recall fixes`

Status: completed as benchmark/documentation-only.

## Summary

Added `RECALL_PRECISION_SCORECARD.md` because no scorecard file existed at the repository root. The scorecard records the current Dutch legal recall/precision status after the gap tests, first candidate-scanner pattern-fix round and verified closeout.

This package did not change product code, recognizers, UI, export/download, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup or dependencies.

## Files added

- `RECALL_PRECISION_SCORECARD.md`
- `workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md`
- `handover/workpackages/20260617_0112_recall_scorecard_refresh.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md` pending final closeout update after this handover file

## Product-code changes

None.

## Scorecard summary

The scorecard records:

- gap tests were added for known Dutch legal recall gaps;
- the first candidate-scanner pattern fixes were completed and verified;
- coordinator evidence confirmed GitHub Actions, Hugging Face sync and app smoke verification for the verify closeout;
- improvement is primarily review-candidate visibility, not a full automatic-recognition guarantee;
- all listed Dutch legal reference samples are covered by the baseline test;
- `CLM-2026-112233` is explicitly tested as not `PHONE`;
- legal role words are covered by preservation and over-masking guard tests;
- review/export/Scrub Key/reinsert boundaries remain guarded by existing contract tests;
- no immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` is recommended unless concrete new misses are observed.

## Tests/checks run

Required local checks:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

Result: not runnable locally in this environment. The container cannot clone/access GitHub for a local working tree.

Connector/static checks completed:

- Confirmed no prior `WP_RECALL_SCORECARD_REFRESH` claim existed before starting.
- Created claim file.
- Read required control files: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Read `RECALL_BENCHMARK_SPEC.md`, `tests/test_dutch_legal_recall_gap_baseline.py`, `candidate_scanner.py`, `RISK_REGISTER.md`, `RELEASE_NOTES.md`, `DECISION_LOG.md`.
- Read relevant claims and handovers for Dutch legal gap tests, pattern fixes and pattern-fix verification.
- Confirmed `RECALL_PRECISION_SCORECARD.md` did not exist at root before this package and then created it.
- GitHub code search returned no useful results for broad recall/scorecard/corpus terms; this limitation is recorded.

## GitHub Actions status

Unknown at handover time for this documentation package. Connector status visibility for direct-push commits has been incomplete in this repo.

## Hugging Face sync status

Unknown at handover time for this documentation package. No app behavior changed.

## App verification status

Not required. This is benchmark/documentation-only and does not change app behavior.

## Updated risks

Updated `RISK_REGISTER.md` for:

- false negatives / missed sensitive data;
- Dutch legal reference under-detection;
- legal-code misclassification;
- role-word over-masking;
- remaining absence of gold-label corpus sidecars and formal recall/precision thresholds.

## Remaining gaps

- No complete gold-label corpus sidecars.
- No formal recall threshold.
- No formal precision threshold.
- No production-blocking benchmark gate.
- Helper-level candidate surfacing is not automatic recognition.
- Candidate rows require human review.
- DOCX metadata/comments/tracked changes remain a separate document-hygiene risk.
- No strong product claim is supported, such as `alle juridische nummers worden altijd herkend`.

## Remaining risks

- A later app/user test may reveal new Dutch legal reference formats not covered by this baseline.
- Role/name combinations such as `arts Jansen` need broader benchmark sidecar coverage.
- Quantitative recall/precision remains open until a runner and gold labels exist.

## Next recommended step

Do not automatically start another pattern-fix round.

Only after separate coordinator approval:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2
```

if concrete new detection misses are observed.

Alternative approved next options:

```text
benchmark/gold-label corpus package
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
