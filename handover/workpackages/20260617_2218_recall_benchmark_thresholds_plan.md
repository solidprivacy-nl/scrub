# Handover — WP_RECALL_BENCHMARK_THRESHOLDS_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — Plan diagnostic recall/precision thresholds without enforcement`

Status: completed as planning/documentation-only.

## Summary

Added a planning-only threshold policy document for future diagnostic recall/precision threshold design.

This work does not enforce thresholds, does not create a CI gate, does not block production, does not change product behavior and does not support product safety claims.

## Files added

- `RECALL_BENCHMARK_THRESHOLDS_PLAN.md`
- `handover/workpackages/20260617_2218_recall_benchmark_thresholds_plan.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md` pending final closeout update after this handover file

## Product-code changes

None.

No app/product flow was changed. No UI, recognizer, candidate scanner, runner, report helper, workflow, export, Scrub Key, reinsert, dependency, threshold enforcement or production gate was changed.

## Threshold policy summary

The plan defines:

- current cleaned diagnostic baseline;
- metric meanings;
- hard versus soft diagnostic interpretation;
- planning baseline;
- warning threshold;
- release review threshold;
- future blocking threshold;
- class-specific planning;
- mandatory conditions before any future gate;
- product-claim boundaries.

Current status remains:

```text
No accepted production thresholds.
No CI gate.
No production blocking.
No threshold enforcement.
No product claim.
```

## Current baseline values

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

Remaining diagnostic gaps:

```text
14 missed PERSON labels
3 missed MEDICAL_OR_CARE_REFERENCE care room/location labels
1 missed/wrong CLIENT_NUMBER
1 nested false-positive BSN-like hit inside a phone-like value
1 known-trap care-location review signal
```

## Non-goals

- No threshold enforcement.
- No CI gate.
- No release blocking.
- No product safety claim.
- No product code.
- No workflow change.
- No test changes.
- No app behavior change.

## Tests/checks run

Local tests were not run because this package is planning/documentation-only and only markdown/governance files changed.

`git diff --check` was not runnable in this connector-only environment.

Previous execution evidence remains from the cleaned artifact package:

```text
59473fb — Tests #1218 green
59473fb — Sync to Hugging Face Space #1228 green
Diagnostic recall benchmark report workflow green for relevant cleanup commits
```

## GitHub Actions status

Not applicable for functional validation of this package. This package is planning/documentation-only.

Connector status may be incomplete for push-triggered runs.

## Hugging Face sync status

Unknown at handover time for the final documentation commit.

This package contains no app/product changes.

## App verification status

Not required. No app behavior changed.

## Updated risks

Updated:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Risk interpretation:

- Threshold planning exists.
- Recall/precision risk remains open.
- No accepted production thresholds exist.
- No benchmark gate exists.
- Product claims remain blocked.

## Remaining gaps

- No accepted recall threshold exists.
- No accepted precision threshold exists.
- No production benchmark gate exists.
- Corpus is synthetic and small.
- Remaining detection gaps need focused review.

## Remaining risks

- Diagnostic report output must not be interpreted as a product accuracy claim.
- Future thresholds/gates require separate approval.
- A gate may only be considered after larger corpus, stable metric definitions, false-negative/false-positive policy approval and a separate approved gate package.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
```

Alternative next packages:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS
```

Do not start follow-up work automatically.
