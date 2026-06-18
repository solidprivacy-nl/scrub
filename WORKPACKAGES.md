# SolidPrivacy Scrub — Workpackages

Repository: `solidprivacy-nl/scrub`.

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

## Claim rule

Before starting a package, check `workpackage_claims/`. If a claim for the same workpackage is already `in_progress`, stop and report the collision. If no claim exists, create one before changing files. When done, update the claim with status, final commit, handover path, validation and next step.

## Current status

```text
WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — completed and verified.
WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — completed.
WP_DUTCH_LEGAL_RECALL_GAP_TESTS — completed.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — completed.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — completed and verified.
WP_RECALL_SCORECARD_REFRESH — completed.
WP_RECALL_GOLD_LABEL_CORPUS_SEED — completed.
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — completed.
WP_RECALL_BENCHMARK_RUNNER_MINIMAL — completed.
WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — completed and verified.
WP_RECALL_BENCHMARK_REPORT_ARTIFACT — completed and verified.
WP_RECALL_BENCHMARK_REPORT_REVIEW — completed.
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — completed and verified.
WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — completed.
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — completed; planning-only threshold policy design added.
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW — completed; PERSON-name coverage gaps reviewed and follow-up route planned.
WP_RECALL_PERSON_NAME_COVERAGE_TESTS — completed; diagnostic PERSON-name gap inventory tests added.
WP_SERIAL_REVIEW_UI — completed and app-verified.
```

## Active product line

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend baseline

The review table remains source of truth and fallback. The normal app keeps one central side-by-side review surface, visible visual markers, the collapsible replacement table under `Vervangtabel controleren — <items> items`, Serial review, export/download and DOCX hygiene audit.

No current benchmark/planning package changes app behavior.

## Recall/benchmark status

The diagnostic benchmark stack now includes:

```text
corpus/**/*.gold.json
recall_benchmark_runner.py
recall_benchmark_report.py
.github/workflows/recall-benchmark-report.yml
RECALL_BENCHMARK_REPORT_REVIEW_2.md
RECALL_BENCHMARK_THRESHOLDS_PLAN.md
RECALL_PERSON_NAME_COVERAGE_REVIEW.md
tests/test_recall_person_name_coverage_diagnostics.py
```

Cleaned artifact baseline:

```text
document_count = 7
gold_label_count = 75
prediction_count = 60
matched_required_exact_count = 56
matched_required_text_normalized_count = 57
matched_required_overlap_count = 57
missed_required_count = 18
wrong_type_count = 1
false_positive_candidate_count = 1
preserve_term_hit_count = 0
known_trap_hit_count = 1
```

PERSON coverage diagnostic status:

```text
PERSON gap inventory covered by tests
name-type categories covered by tests
no full-recognition requirement yet
no recognizer changes
no candidate scanner changes
no runner/report changes
no thresholds
no gate
no product claim
```

Remaining diagnostic gaps:

```text
14 missed PERSON labels
3 missed MEDICAL_OR_CARE_REFERENCE care room/location labels
1 missed/wrong CLIENT_NUMBER
1 nested false-positive BSN-like hit inside a phone-like value
1 known-trap care-location review signal
```

## Verification evidence

Recent relevant verification evidence:

```text
a3df5c7 — Diagnostic recall benchmark report #1 green
31ee53b — Tests #1193 green
31ee53b — Sync to Hugging Face Space #1204 green
59473fb — Tests #1218 green
59473fb — Sync to Hugging Face Space #1228 green
Diagnostic recall benchmark report workflow green for relevant cleanup commits
Hugging Face app screenshot showed running without Script execution error
```

`WP_RECALL_PERSON_NAME_COVERAGE_TESTS` is tests/documentation-only and does not require app verification.

## Active / next recommended execution queue

```text
1. Do not start a new feature automatically.
2. Recommended next after separate approval: WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN.
3. Then consider: WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.
4. Other backlog candidates: WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN, WP_CLIENT_REFERENCE_COVERAGE_REVIEW, WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS.
5. A future gate route may be planned later as WP_RECALL_BENCHMARK_GATE_PLAN, but that is still planning and not implementation.
```

## Boundaries

Do not start UI, export/download, Scrub Key, reinsert, recognizer, candidate-scanner, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.
