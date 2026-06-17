# Handover — WP_RECALL_BENCHMARK_REPORT_REVIEW_2

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — Review cleaned diagnostic recall benchmark artifact output`

Status: completed as review/documentation-only.

## Summary

Reviewed the cleaned `diagnostic-recall-benchmark-report` artifact generated after `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX`.

The cleaned artifact is structurally valid and materially less noisy than the first artifact. It is now reasonable to start planning-only threshold work, while keeping all product claims and production gates blocked.

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

## Files added

- `RECALL_BENCHMARK_REPORT_REVIEW_2.md`
- `handover/workpackages/20260617_2212_recall_benchmark_report_review_2.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW_2.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW_2.md` pending final closeout update after this handover file

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

Cleaned artifact summary values:

```text
document_count = 7
gold_label_count = 75
prediction_count = 60
required_label_count = 75
matched_required_exact_count = 56
matched_required_text_normalized_count = 57
matched_required_overlap_count = 57
missed_required_count = 18
wrong_type_count = 1
false_positive_candidate_count = 1
preserve_term_hit_count = 0
known_trap_hit_count = 1
```

Improvement versus the first artifact:

```text
matched_required_exact_count: 41 -> 56
missed_required_count: 34 -> 18
wrong_type_count: 11 -> 1
false_positive_candidate_count: 8 -> 1
preserve_term_hit_count: 0 -> 0
known_trap_hit_count: 1 -> 1
```

Interpretation:

- Mapping/counting cleanup was effective.
- Exact matches increased materially.
- Missed required labels, wrong-type findings and false-positive candidates dropped substantially.
- Preserve-term hits remain 0.
- Remaining misses now look more like real coverage/taxonomy/product-risk questions than benchmark accounting bugs.

## Remaining findings

Remaining missed required labels:

```text
PERSON: 14
MEDICAL_OR_CARE_REFERENCE: 3
CLIENT_NUMBER: 1
```

Remaining wrong-type finding:

```text
CL-HUUR-2026-0009 predicted partially as NL_LEGAL_PARTY_NAME / CL-HUUR-
```

Remaining false-positive candidate:

```text
55667788 predicted as NL_BSN inside a phone-like value
```

Remaining known-trap hit:

```text
afdeling Rozenhof 3 -> Rozenhof 3 / NL_ADDRESS, care_location_context_needs_review
```

## Tests/checks run

Local tests were not run. This package is review/documentation-only and no product/test code was changed.

Existing execution proof for the cleaned artifact package remains:

```text
59473fb — Tests #1218 — green by coordinator screenshot evidence
59473fb — Sync to Hugging Face Space #1228 — green by coordinator screenshot evidence
Diagnostic recall benchmark report workflow — green by coordinator screenshot evidence for relevant cleanup commits
```

## GitHub Actions status

Previously verified green by coordinator screenshot evidence for the cleanup package.

No new product/test code was added in this review package.

## Diagnostic report workflow status

Previously verified green by coordinator screenshot evidence for relevant cleanup commits.

The cleaned artifact files were uploaded by the coordinator and reviewed.

## Artifact status

Reviewed successfully from uploaded files:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

## Hugging Face sync status

Previously verified green by coordinator screenshot evidence for the cleanup package:

```text
59473fb — Sync to Hugging Face Space #1228 — green
```

## App verification status

Not required. This package is review/documentation-only and does not affect app behavior.

Existing coordinator screenshot evidence showed the Space running without Script execution error after the cleanup package.

## Updated risks

Updated:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Risk interpretation updated:

- Benchmark output is substantially less noisy.
- Threshold planning is now reasonable as planning-only work.
- Recall/precision risk remains open until thresholds and gates are separately planned and approved.
- Product claims remain blocked.

## Remaining gaps

- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Report output remains diagnostic only.
- Corpus is synthetic and not exhaustive.
- 14 person labels remain missed.
- 3 care room/location reference labels remain missed.
- 1 client-number label remains missed/wrong-type.
- 1 nested BSN false positive remains.

## Remaining risks

- Diagnostic report output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.
- A product pattern-fix round should not start from artifact metrics without threshold planning and a separate approved workpackage.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
```

Strict boundary:

```text
planning-only
no CI gate
no production blocking
no threshold enforcement
no product claim
```

Potential later backlog after threshold planning:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
```
