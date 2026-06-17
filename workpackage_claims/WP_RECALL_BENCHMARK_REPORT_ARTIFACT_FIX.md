status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping and counting noise
started timestamp: 2026-06-17 21:41 Europe/Amsterdam
completed timestamp: 2026-06-17 21:41 Europe/Amsterdam
scope: benchmark/tooling/tests/documentation-only diagnostic runner/report cleanup
boundaries: no product UI, no product recognizer changes, no app pattern fixes, no export, no Scrub Key, no reinsert changes, no thresholds, no production gate

final commit SHA or PR link: 3fe3b9bd0330b146c64597642f40567e3ae70dff
handover path: handover/workpackages/20260617_2141_recall_benchmark_report_artifact_fix.md

files added:
- RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md
- handover/workpackages/20260617_2141_recall_benchmark_report_artifact_fix.md
- workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md

files changed:
- recall_benchmark_runner.py
- tests/test_recall_benchmark_runner_minimal.py
- corpus/care/care_reference_seed_001.gold.json
- corpus/care/care_role_preservation_seed_001.gold.json
- corpus/care/care_mixed_identifiers_seed_001.gold.json
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md

product-code changes: none

mapping changes:
- NL_ADDRESS -> ADDRESS
- NL_IBAN -> IBAN
- NL_CASE_REFERENCE -> CASE_NUMBER
- NL_LEGAL_PARTY_NAME -> PERSON
- EMAIL_ADDRESS -> EMAIL
- selected care ZORG-CL-* sidecars accept NL_CLIENT_REFERENCE where appropriate
- selected care location sidecars accept NL_ADDRESS where appropriate

dedup changes:
- predictions are deduped by text/entity_type/start/end/source for diagnostic accounting
- duplicate wrong-type candidates are deduped
- duplicate preserve-term hits are deduped
- duplicate known-trap hits are deduped
- matched predictions should not also be false-positive candidates

email behavior decision:
- added benchmark-only email collection in recall_benchmark_runner.py
- EMAIL_ADDRESS predictions use source benchmark_builtin
- this is not a product recognizer and does not change app behavior

tests/checks:
- Local tests were not runnable because no local GitHub working tree is available in this environment.
- Updated tests/test_recall_benchmark_runner_minimal.py for mapping, care acceptable types, deduplication, matched-not-false-positive, and benchmark-only email behavior.
- Required checks remain corpus validator, benchmark runner tests, report artifact tests, py_compile for runner/report/app, and diagnostic report generation.

GitHub Actions status: pending after final commit.
diagnostic workflow/artifact status: pending after final commit.
Hugging Face sync status: pending after final commit.
app verification status: not required; benchmark/tooling/tests/documentation-only and no app behavior changed.

remaining gaps:
- Cleaned artifact needs Actions/report workflow verification.
- Cleaned artifact output needs review.
- No accepted recall/precision thresholds.
- No production benchmark gate.
- Corpus is synthetic and not exhaustive.

remaining risks:
- Diagnostic report output must not be interpreted as a product accuracy claim.
- Future thresholds/gates require separate approval.
- A product pattern-fix round should not start from raw artifact metrics without cleaned artifact review.

next recommended step: first verify Tests, Sync to Hugging Face Space and Diagnostic recall benchmark report workflow/artifact. Then consider WP_RECALL_BENCHMARK_REPORT_REVIEW_2 after separate coordinator approval. Only after cleaned artifact review should WP_RECALL_BENCHMARK_THRESHOLDS_PLAN be considered.
