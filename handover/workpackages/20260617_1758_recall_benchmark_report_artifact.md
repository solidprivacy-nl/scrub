# Handover — WP_RECALL_BENCHMARK_REPORT_ARTIFACT

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_REPORT_ARTIFACT — Generate diagnostic recall benchmark report artifact`

Status: completed as benchmark/tooling/tests/documentation-only.

## Summary

Added a diagnostic recall benchmark report helper, tests, documentation and a GitHub Actions workflow that generates and uploads the existing recall benchmark runner output as JSON and Markdown artifacts.

This package does not change product UI, recognizers, candidate scanner logic, export/download behavior, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup or dependencies. It does not enforce thresholds and does not create a production gate.

## Files added

- `recall_benchmark_report.py`
- `tests/test_recall_benchmark_report_artifact.py`
- `.github/workflows/recall-benchmark-report.yml`
- `RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `handover/workpackages/20260617_1758_recall_benchmark_report_artifact.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT.md` pending final closeout update after this handover file

## Product-code changes

None to the app/product flow.

The new files are benchmark/report tooling and tests only. They do not import or start Streamlit, do not change recognizers, do not change the candidate scanner, and do not change export, Scrub Key or reinsert behavior.

## Report artifact summary

Added `recall_benchmark_report.py`.

The helper:

- calls `recall_benchmark_runner.run_benchmark("corpus")`;
- wraps the runner output with diagnostic metadata;
- writes `recall_benchmark_report.json`;
- writes `recall_benchmark_summary.md`;
- validates schema/integrity in strict mode only;
- does not fail on low recall/precision;
- does not enforce thresholds;
- does not create a production gate.

Metadata:

```text
status: diagnostic_only
synthetic_corpus: true
production_gate: false
thresholds_enforced: false
```

Default output directory:

```text
output/recall_benchmark/
```

## Workflow summary

Added workflow:

```text
.github/workflows/recall-benchmark-report.yml
```

Workflow name:

```text
Diagnostic recall benchmark report
```

Artifact name:

```text
diagnostic-recall-benchmark-report
```

Artifact files:

```text
output/recall_benchmark/recall_benchmark_report.json
output/recall_benchmark/recall_benchmark_summary.md
```

The workflow:

1. checks out the repository;
2. sets up Python 3.10;
3. installs test dependencies using the existing Tests workflow style;
4. runs corpus, runner and report tests;
5. compiles runner/report files;
6. generates the report;
7. uploads the diagnostic artifact.

The workflow may fail on broken tests or broken report generation. It must not fail on low recall/precision because no thresholds are enforced.

## Tests/checks run

Required local commands:

```text
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
python -m pytest -q tests/test_recall_benchmark_runner_minimal.py
python -m pytest -q tests/test_recall_benchmark_report_artifact.py
python -m py_compile recall_benchmark_runner.py
python -m py_compile recall_benchmark_report.py
python -m py_compile presidio_streamlit.py
python recall_benchmark_report.py --corpus corpus --output output/recall_benchmark
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests
```

Result: not runnable locally in this environment because no local GitHub working tree is available.

Static checks completed:

- Confirmed no prior `WP_RECALL_BENCHMARK_REPORT_ARTIFACT` claim existed before starting.
- Created claim file before report changes.
- Read required control files and relevant recall/scorecard/corpus/risk/decision/claim/handover files.
- Read existing GitHub workflows: `.github/workflows/tests.yml` and `.github/workflows/sync-to-huggingface.yml`.
- Added report tests for metadata, Markdown summary, file writing, no-threshold behavior and CLI smoke output.
- Added a separate report workflow with `actions/upload-artifact@v4`.

## GitHub Actions status

Unknown at handover time. Connector status visibility for direct-push commits can be incomplete in this repo.

## Diagnostic report workflow status

Pending at handover time. The new workflow should be checked for:

- successful run;
- artifact named `diagnostic-recall-benchmark-report`;
- JSON file present;
- Markdown file present.

## Hugging Face sync status

Unknown at handover time. This package is benchmark/tooling/tests/documentation-only.

## App verification status

Not required. No app behavior changed.

## Updated risks

Updated `RISK_REGISTER.md` for:

- false negatives / missed sensitive data;
- corpus/threshold gap;
- Dutch legal reference under-detection;
- role-word over-masking;
- workflow status/evidence visibility.

The artifact reduces evidence visibility risk, but recall/precision risk remains open until thresholds and gates are separately planned and approved.

## Remaining gaps

- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Report output is diagnostic only.
- First artifact output still needs review.
- Corpus coverage is improved but still synthetic and not exhaustive.

## Remaining risks

- Diagnostic report output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.
- The new artifact workflow needs Actions confirmation.

## Next recommended step

Do not automatically start another pattern-fix round.

First verify:

```text
Tests workflow
Sync to Hugging Face Space
Diagnostic recall benchmark report workflow
Artifact availability
```

Likely next options after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_REPORT_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
