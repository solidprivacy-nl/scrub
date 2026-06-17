# Minimal diagnostic recall/precision runner

Workpackage: `WP_RECALL_BENCHMARK_RUNNER_MINIMAL`

Repository: `solidprivacy-nl/scrub`

Scope: benchmark/tooling/tests/documentation-only.

This runner is an internal diagnostic tool. It is not a product claim, not a production quality gate and not a release threshold.

---

## Goal

The runner compares the synthetic gold-label corpus sidecars with analyzer/helper predictions and reports:

- which gold labels exist;
- which predictions were produced;
- which labels matched exactly;
- which labels matched by text-normalized value;
- which labels only overlapped diagnostically;
- which required labels were missed;
- which labels were hit with the wrong entity type;
- which predictions look like false-positive candidates;
- which preserve terms were hit;
- which known traps were hit.

---

## Inputs

The runner reads:

```text
corpus/**/*.gold.json
```

Each sidecar points to a plain-text source file through `source_file`.

Required sidecar assumptions:

- `synthetic` is `true`;
- every label has exact offsets;
- every preserve term has exact offsets;
- known traps can be found by trap text in the source.

---

## Output

The main API is:

```python
from recall_benchmark_runner import run_benchmark

report = run_benchmark("corpus")
```

The report is a JSON-serializable Python dict with:

```text
documents
summary
```

Each document report includes:

```text
document_id
source_file
domain
gold_label_count
prediction_count
matched_exact
matched_text_normalized
matched_overlap
missed_required
wrong_type
false_positive_candidates
preserve_term_hits
known_trap_hits
```

The summary includes:

```text
document_count
gold_label_count
prediction_count
required_label_count
matched_required_exact_count
matched_required_text_normalized_count
matched_required_overlap_count
missed_required_count
wrong_type_count
false_positive_candidate_count
preserve_term_hit_count
known_trap_hit_count
```

---

## Matching rules

### Exact span match

```text
prediction.start == label.start
prediction.end == label.end
```

### Text-normalized match

The runner normalizes values by:

```text
lowercase
strip
remove non-alphanumeric characters
```

Example:

```text
CLM-2026-112233 -> clm2026112233
```

### Overlap diagnostic

```text
prediction.start < label.end
prediction.end > label.start
```

Overlap is diagnostic only. It must not hide missed sensitive values in future threshold work.

---

## Entity mapping

The runner maps known implementation entity names to benchmark classes through `ENTITY_TYPE_TO_BENCHMARK_CLASS`.

A prediction is accepted for a gold label when either:

1. the prediction entity type is listed in the label's `acceptable_entity_types`; or
2. the mapped benchmark class equals the gold label's `entity_class`.

Important caveat:

```text
NL_SUSPICIOUS_REFERENCE_CANDIDATE is ambiguous.
```

Candidate scanner output may count diagnostically when a gold label explicitly accepts it, but it must not be interpreted as a hard automatic masking guarantee.

---

## Analyzer/helper output

The runner tries to collect predictions from:

```text
dutch_recognizers.get_dutch_recognizers(...)
dutch_recognizers.get_dutch_entity_names(...)
candidate_scanner.scan_unmasked_candidates(...)
```

If optional analyzer dependencies are unavailable in a minimal environment, the runner still loads the corpus and produces a report. This avoids coupling corpus diagnostics to Streamlit or full app startup.

Prediction source is recorded as:

```text
recognizer
candidate_scanner
```

---

## CLI

Optional CLI usage:

```bash
python recall_benchmark_runner.py --corpus corpus --json
```

Without `--json`, the CLI prints a short text summary.

The CLI:

- prints to stdout;
- does not start Streamlit;
- does not write output files unless future work explicitly adds an output option;
- does not make cloud calls.

---

## Limitations

- The runner is diagnostic only.
- No recall/precision threshold is enforced.
- No CI production gate is created.
- No product UI is changed.
- No recognizer or candidate-scanner logic is changed.
- No export, Scrub Key or reinsert behavior is changed.
- Current metrics are only as representative as the synthetic corpus.
- A future thresholds plan is required before any pass/fail language can be used.

---

## Why this is not a product claim

The runner measures synthetic benchmark fixtures. It does not prove that all real-world legal or care documents are safe.

Allowed internal wording:

```text
The diagnostic runner compares current analyzer/helper output with the synthetic gold-label corpus.
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
WP_RECALL_BENCHMARK_REPORT_ARTIFACT
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
