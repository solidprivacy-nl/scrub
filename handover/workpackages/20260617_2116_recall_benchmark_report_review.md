# Handover — WP_RECALL_BENCHMARK_REPORT_REVIEW

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_REPORT_REVIEW — Review first diagnostic recall benchmark artifact output`

Status: completed as review/documentation-only.

## Artifact reviewed

Artifact:

```text
diagnostic-recall-benchmark-report
```

Files reviewed:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

Source workflow/commit evidence:

```text
a3df5c7 — Diagnostic recall benchmark report #1 — green by coordinator screenshot evidence
31ee53b — Tests #1193 — green by coordinator screenshot evidence
31ee53b — Sync to Hugging Face Space #1204 — green by coordinator screenshot evidence
```

The GitHub connector could not retrieve the artifact directly, so the coordinator uploaded the JSON and Markdown files. The review uses those uploaded artifact files.

## Files added

- `RECALL_BENCHMARK_REPORT_REVIEW.md`
- `handover/workpackages/20260617_2116_recall_benchmark_report_review.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW.md` pending final closeout update after this handover file

## Product-code changes

None.

No app/product flow was changed. No UI, recognizer, candidate scanner, runner, report helper, export, Scrub Key, reinsert, workflow, threshold or production gate was changed.

## Main findings

Artifact integrity passed:

```text
metadata.status = diagnostic_only
metadata.synthetic_corpus = true
metadata.production_gate = false
metadata.thresholds_enforced = false
report.summary exists
report.documents exists
document_count = 7
gold_label_count = 75
```

Summary values:

```text
document_count = 7
gold_label_count = 75
prediction_count = 61
required_label_count = 75
matched_required_exact_count = 41
matched_required_text_normalized_count = 41
matched_required_overlap_count = 41
missed_required_count = 34
wrong_type_count = 11
false_positive_candidate_count = 8
preserve_term_hit_count = 0
known_trap_hit_count = 1
```

Interpretation:

- Artifact is structurally valid and useful for engineering review.
- Raw counts are not yet suitable for threshold planning.
- Several missed/wrong-type findings appear to be caused by runner mapping, acceptable-entity taxonomy or duplicate prediction reporting.
- Preserve-term hits are currently 0, which is positive for the reviewed synthetic corpus but not production proof.
- The only known-trap hit is a care-location review signal, not a hard product precision failure.

Likely follow-up areas:

- `NL_ADDRESS` mapping/acceptable types for address/location labels.
- `NL_IBAN` mapping/acceptable types for IBAN labels.
- `NL_CASE_REFERENCE` mapping/acceptable types for case-number labels.
- Decision whether `NL_LEGAL_PARTY_NAME` should count as `PERSON` in benchmark review.
- Care `ZORG-CL-*` taxonomy/acceptable types.
- Email prediction absence in the current artifact.
- Duplicate prediction accounting before wrong-type/false-positive reporting.

## Tests/checks run

Local tests were not run. This package is review/documentation-only and no product code was changed.

Existing prior execution proof remains:

```text
a3df5c7 — Diagnostic recall benchmark report #1 — green
31ee53b — Tests #1193 — green
31ee53b — Sync to Hugging Face Space #1204 — green
```

## GitHub Actions status

Previously verified green by coordinator screenshot evidence for the report artifact package.

No new product/test code was added in this review package.

## Diagnostic report workflow status

Previously verified green by coordinator screenshot evidence:

```text
a3df5c7 — Diagnostic recall benchmark report #1 — green
```

## Artifact status

Artifact was available through coordinator upload and reviewed:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

## Hugging Face sync status

Previously verified green by coordinator screenshot evidence for the report artifact package:

```text
31ee53b — Sync to Hugging Face Space #1204 — green
```

## App verification status

Not required. This package is review/documentation-only and does not affect app behavior.

Existing coordinator screenshot evidence showed the Space running without Script execution error after the report artifact package.

## Updated risks

Updated:

- `RECALL_PRECISION_SCORECARD.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Risk interpretation updated:

- Artifact review lowers uncertainty about benchmark output shape.
- Artifact review increases confidence that the artifact is useful.
- Artifact review also shows the metrics are currently too noisy for threshold planning.
- Recall/precision risk remains open until mapping/taxonomy/dedup cleanup and later threshold governance.

## Remaining gaps

- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Report output is diagnostic only.
- Raw counts are noisy due to mapping/taxonomy/deduplication issues.
- Corpus is synthetic and not exhaustive.

## Remaining risks

- Diagnostic report output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.
- A pattern-fix round should not start until the report mapping/dedup/taxonomy issues are cleaned up.

## Next recommended step

Do not start threshold planning yet.

Recommended next package after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX
```

Focus:

- runner/report mapping cleanup;
- dedupe repeated predictions;
- care reference taxonomy/acceptable-type cleanup;
- investigate absent email predictions;
- keep diagnostic-only status;
- no product UI, recognizer/pattern product changes, thresholds or gates.
