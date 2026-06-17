# Handover — WP_RECALL_BENCHMARK_RUNNER_MINIMAL

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_RUNNER_MINIMAL — Add minimal diagnostic recall/precision runner for gold-label corpus`

Status: completed as benchmark/tooling/tests/documentation-only.

## Summary

Added a minimal diagnostic recall/precision runner for the synthetic gold-label corpus. The runner loads `.gold.json` sidecars, validates offsets, collects recognizer/candidate-scanner predictions when optional dependencies are available, compares predictions against gold labels and returns a JSON-serializable diagnostic report.

No product UI, recognizer logic, pattern logic, export/download, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup or dependency behavior was changed.

## Files added

- `recall_benchmark_runner.py`
- `tests/test_recall_benchmark_runner_minimal.py`
- `RECALL_BENCHMARK_RUNNER_MINIMAL.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md`
- `handover/workpackages/20260617_0912_recall_benchmark_runner_minimal.md`

## Files changed

- `corpus/legal/legal_false_positive_traps_seed_001.gold.json`
- `corpus/legal/legal_mixed_identifiers_seed_001.gold.json`
- `corpus/care/care_role_preservation_seed_001.gold.json`
- `corpus/care/care_mixed_identifiers_seed_001.gold.json`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md` pending final closeout update after this handover file

## Product-code changes

None to the app/product flow.

The new file `recall_benchmark_runner.py` is benchmark tooling only. It does not import or start Streamlit, does not change recognizers, does not change the candidate scanner, and does not change export, Scrub Key or reinsert behavior.

## Benchmark runner summary

The runner:

- loads all `.gold.json` sidecars under `corpus/`;
- reads the corresponding `source_file`;
- validates label and preserve-term offsets;
- normalizes gold labels and predictions into internal dataclasses;
- attempts to collect recognizer predictions from `dutch_recognizers` when available;
- attempts to collect review-candidate predictions from `candidate_scanner` when available;
- gracefully falls back to diagnostic empty prediction sets if optional analyzer dependencies are unavailable;
- compares labels and predictions using exact span, text-normalized and overlap diagnostic matching;
- reports missed required labels, wrong type hits, false-positive candidates, preserve-term hits and known-trap hits;
- returns a JSON-serializable report.

Optional CLI:

```text
python recall_benchmark_runner.py --corpus corpus --json
```

## Report format summary

Top-level report keys:

```text
documents
summary
```

Per document:

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

Summary:

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

## Tests/checks run

Required local commands:

```text
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
python -m pytest -q tests/test_recall_benchmark_runner_minimal.py
python -m py_compile recall_benchmark_runner.py
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

Result: not runnable locally in this environment.

Attempted local clone:

```text
git clone --depth 1 https://github.com/solidprivacy-nl/scrub.git /mnt/data/scrub_runner
```

Failure:

```text
fatal: unable to access 'https://github.com/solidprivacy-nl/scrub.git/': Could not resolve host: github.com
```

Static checks completed:

- Confirmed no prior `WP_RECALL_BENCHMARK_RUNNER_MINIMAL` claim existed before starting.
- Created claim file before runner changes.
- Read required control files and relevant recall/scorecard/corpus/risk/decision/claim/handover files.
- GitHub code search for broad benchmark terms returned no useful results.
- Corrected four expanded-corpus sidecars using recalculated offsets.
- Added runner tests to cover loading, normalization, matching, preserve-term hits, known-trap hits and corpus smoke reporting.

## GitHub Actions status

Unknown at handover time. Connector status visibility for direct-push commits has been incomplete in this repo.

## Hugging Face sync status

Unknown at handover time. This package is benchmark/tooling/tests/documentation-only.

## App verification status

Not required. No app behavior changed.

## Updated risks

Updated `RISK_REGISTER.md` for:

- false negatives / missed sensitive data;
- corpus/threshold gap;
- Dutch legal reference under-detection;
- role-word over-masking.

The runner reduces the measurability gap, but recall/precision risk remains open until thresholds and gate governance are separately planned and approved.

## Remaining gaps

- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Runner output is diagnostic only.
- Corpus coverage is improved but still synthetic and not exhaustive.

## Remaining risks

- Diagnostic runner output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.

## Next recommended step

Do not automatically start another pattern-fix round.

Likely next options after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
WP_RECALL_BENCHMARK_REPORT_ARTIFACT
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
