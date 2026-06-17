status: completed_verified
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping and counting noise
started timestamp: 2026-06-17 21:41 Europe/Amsterdam
completed timestamp: 2026-06-17 21:41 Europe/Amsterdam
verified timestamp: 2026-06-17 22:06 Europe/Amsterdam
scope: benchmark/tooling/tests/documentation-only diagnostic runner/report cleanup
boundaries: no product UI, no product recognizer changes, no app pattern fixes, no export, no Scrub Key, no reinsert changes, no thresholds, no production gate

final commit SHA or PR link: 59473fb47fda6b6c6ac71d1fef0e4369a2be72f2
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
- Coordinator screenshot evidence shows green Tests runs for the cleanup commits, including Tests #1218 for commit 59473fb.
- Updated tests/test_recall_benchmark_runner_minimal.py for mapping, care acceptable types, deduplication, matched-not-false-positive, and benchmark-only email behavior.
- Local tests were not runnable because no local GitHub working tree is available in this environment.

GitHub Actions status: verified green by coordinator screenshot evidence. Tests #1218 for commit 59473fb green.
diagnostic workflow/artifact status: verified green by coordinator screenshot evidence. Diagnostic recall benchmark report ran green for the relevant benchmark cleanup commits, including the mapping/dedup and care-taxonomy commits.
Hugging Face sync status: verified green by coordinator screenshot evidence. Sync to Hugging Face Space #1228 for commit 59473fb green.
app verification status: verified healthy by coordinator screenshot evidence. Hugging Face Space running without Script execution error; no app behavior change was expected.

remaining gaps:
- Cleaned artifact output still needs content review.
- No accepted recall/precision thresholds.
- No production benchmark gate.
- Corpus is synthetic and not exhaustive.

remaining risks:
- Diagnostic report output must not be interpreted as a product accuracy claim.
- Future thresholds/gates require separate approval.
- A product pattern-fix round should not start from raw artifact metrics without cleaned artifact review.

next recommended step: WP_RECALL_BENCHMARK_REPORT_REVIEW_2 after separate coordinator approval to review the cleaned artifact output. Only after cleaned artifact review should WP_RECALL_BENCHMARK_THRESHOLDS_PLAN be considered.
