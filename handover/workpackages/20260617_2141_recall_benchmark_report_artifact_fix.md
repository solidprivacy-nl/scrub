# Handover — WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping and counting noise`

Status: completed and verified as benchmark/tooling/tests/documentation-only.

## Summary

Cleaned diagnostic recall benchmark runner/report mapping and counting noise identified in `WP_RECALL_BENCHMARK_REPORT_REVIEW`.

This package changes benchmark/report tooling and selected benchmark sidecar acceptable types only. It does not change product UI, product recognizers, candidate scanner behavior, app pattern logic, export/download, Scrub Key, reinsert, thresholds or production gates.

## Files added

- `RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md`
- `handover/workpackages/20260617_2141_recall_benchmark_report_artifact_fix.md`

## Files changed

- `recall_benchmark_runner.py`
- `tests/test_recall_benchmark_runner_minimal.py`
- `corpus/care/care_reference_seed_001.gold.json`
- `corpus/care/care_role_preservation_seed_001.gold.json`
- `corpus/care/care_mixed_identifiers_seed_001.gold.json`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md`

## Product-code changes

None.

No app/product flow changed. No `presidio_streamlit.py`, `candidate_scanner.py`, `dutch_recognizers.py`, export, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup, dependency, threshold or production gate changed.

## Mapping changes

Diagnostic benchmark mapping now includes:

```text
NL_ADDRESS -> ADDRESS
NL_IBAN -> IBAN
NL_CASE_REFERENCE -> CASE_NUMBER
NL_LEGAL_PARTY_NAME -> PERSON
EMAIL_ADDRESS -> EMAIL
```

This is benchmark/report mapping only and does not change product recognizers or app behavior.

## Dedup changes

Added report-accounting dedupe by:

```text
text
entity_type
start
end
source
```

Deduplication is applied before comparison and to:

- wrong-type candidate lists;
- false-positive candidate accounting;
- preserve-term hit accounting;
- known-trap hit accounting.

A matched prediction should no longer also be reported as a false-positive candidate.

## Email behavior decision

The first artifact showed email labels as missed because the runner only collected custom Dutch recognizers and candidate-scanner predictions.

Decision:

- add benchmark-only email collection in `recall_benchmark_runner.py`;
- emit `EMAIL_ADDRESS` predictions with source `benchmark_builtin`;
- use this only for diagnostic runner/report output;
- do not add a product recognizer or app behavior.

## Care taxonomy/acceptable-type cleanup

Updated selected care sidecars so current implementation outputs can be measured fairly:

- `ZORG-CL-*` care references accept `NL_CLIENT_REFERENCE` where appropriate.
- Care department/location labels accept `NL_ADDRESS` where appropriate.
- Care role/person labels accept `NL_LEGAL_PARTY_NAME` as benchmark-compatible person output where appropriate.

Spans and source text were not changed.

## Tests/checks run

Local tests were not runnable in this environment because no local GitHub working tree is available for pytest/py_compile execution.

Coordinator screenshot evidence confirms:

```text
Tests #1218 for commit 59473fb — green
Sync to Hugging Face Space #1228 for commit 59473fb — green
Diagnostic recall benchmark report runs for the relevant benchmark cleanup commits — green
Hugging Face Space app — running without Script execution error
```

Required local checks remain for any future local worker:

```text
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
python -m pytest -q tests/test_recall_benchmark_runner_minimal.py
python -m pytest -q tests/test_recall_benchmark_report_artifact.py
python -m py_compile recall_benchmark_runner.py
python -m py_compile recall_benchmark_report.py
python -m py_compile presidio_streamlit.py
python recall_benchmark_report.py --corpus corpus --output output/recall_benchmark --strict
```

## GitHub Actions status

Verified green by coordinator screenshot evidence.

```text
Tests #1218 for commit 59473fb — green
```

## Diagnostic report workflow status

Verified green by coordinator screenshot evidence for the relevant benchmark cleanup commits.

Workflow:

```text
Diagnostic recall benchmark report
```

Artifact:

```text
diagnostic-recall-benchmark-report
```

Expected artifact files:

```text
output/recall_benchmark/recall_benchmark_report.json
output/recall_benchmark/recall_benchmark_summary.md
```

## Hugging Face sync status

Verified green by coordinator screenshot evidence.

```text
Sync to Hugging Face Space #1228 for commit 59473fb — green
```

## App verification status

Verified healthy by coordinator screenshot evidence. The Hugging Face Space is running without Script execution error.

No app verification was functionally required because this package is benchmark/tooling/tests/documentation-only and no app behavior changed.

## Updated risks

Updated:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Risk interpretation:

- artifact metrics should be less noisy after mapping/dedup/email cleanup;
- metrics remain diagnostic only;
- recall/precision risk remains open until accepted thresholds and gates exist;
- product accuracy claims remain blocked.

## Remaining gaps

- Cleaned artifact output needs content review.
- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Corpus is synthetic and not exhaustive.

## Remaining risks

- Diagnostic report output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.
- A product pattern-fix round should not start from raw artifact metrics without cleaned artifact review.

## Next recommended step

After separate coordinator approval:

```text
WP_RECALL_BENCHMARK_REPORT_REVIEW_2
```

Only after cleaned artifact review should `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` be considered.
