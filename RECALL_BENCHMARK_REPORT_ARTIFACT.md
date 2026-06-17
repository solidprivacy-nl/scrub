# Diagnostic recall benchmark report artifact

Workpackage: `WP_RECALL_BENCHMARK_REPORT_ARTIFACT`

Repository: `solidprivacy-nl/scrub`

Scope: benchmark/tooling/tests/documentation-only.

This report artifact is diagnostic only. It is not a product claim, not a production quality gate and not a release threshold.

---

## Goal

The goal is to make the existing minimal recall benchmark runner output visible in GitHub Actions as downloadable JSON and Markdown artifacts.

The artifact helps answer:

- which synthetic gold labels were loaded;
- which analyzer/helper predictions were produced;
- which required labels were missed;
- which predictions hit preserve terms;
- which predictions hit known traps;
- where wrong-type or false-positive candidates appeared.

---

## Workflow

Workflow file:

```text
.github/workflows/recall-benchmark-report.yml
```

Workflow name:

```text
Diagnostic recall benchmark report
```

The workflow can be started manually with `workflow_dispatch` and also runs on pushes that touch recall benchmark files.

Steps:

1. Checkout repository.
2. Set up Python 3.10.
3. Install test dependencies.
4. Run corpus/runner/report tests.
5. Generate the diagnostic report.
6. Upload report files as a GitHub Actions artifact.

---

## Artifact

Artifact name:

```text
diagnostic-recall-benchmark-report
```

Artifact files:

```text
output/recall_benchmark/recall_benchmark_report.json
output/recall_benchmark/recall_benchmark_summary.md
```

---

## CLI

Generate locally or in CI:

```bash
python recall_benchmark_report.py --corpus corpus --output output/recall_benchmark
```

Strict mode validates report schema/integrity only:

```bash
python recall_benchmark_report.py --corpus corpus --output output/recall_benchmark --strict
```

Strict mode does not enforce recall, precision or quality thresholds.

---

## JSON format

The JSON file has this shape:

```json
{
  "metadata": {
    "status": "diagnostic_only",
    "synthetic_corpus": true,
    "production_gate": false,
    "thresholds_enforced": false
  },
  "report": {
    "documents": [],
    "summary": {}
  }
}
```

The `report` value is the direct diagnostic output from `recall_benchmark_runner.run_benchmark(...)`.

---

## Markdown format

The Markdown file contains:

- diagnostic status;
- synthetic corpus warning;
- no-threshold / no-product-claim warning;
- summary counts;
- per-document counts;
- interpretation notes.

Required warning language includes:

```text
Status: diagnostic only
Generated from synthetic corpus
No production threshold
No product safety claim
```

---

## Interpretation

This artifact is useful for engineering review. It does not prove production safety.

Interpret carefully:

- exact matches are useful diagnostics;
- text-normalized matches are useful diagnostics;
- overlap matches are diagnostic only;
- missed required counts show what should be investigated;
- preserve-term hits can indicate over-masking risk;
- known-trap hits can indicate precision risk;
- candidate-scanner output is review-candidate visibility, not hard automatic masking proof.

---

## Boundaries

This package does not:

- change product UI;
- change recognizers;
- change candidate scanner logic;
- change export/download behavior;
- change Scrub Key behavior;
- change reinsert behavior;
- enforce thresholds;
- create a production gate;
- make a product accuracy claim.

---

## Why this is not a product claim

The artifact is generated from a small synthetic corpus. It is intended to make gaps visible, not to prove that all sensitive data is detected.

Allowed internal wording:

```text
The diagnostic recall benchmark report artifact makes runner output visible in CI.
```

Disallowed product claim:

```text
Alle juridische nummers worden altijd herkend.
```

---

## Likely next work

Possible next packages after separate approval:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
WP_RECALL_BENCHMARK_REPORT_REVIEW
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
