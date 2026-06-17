status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_RUNNER_MINIMAL
started timestamp: 2026-06-17 09:12 Europe/Amsterdam
completed timestamp: 2026-06-17 09:13 Europe/Amsterdam
scope: benchmark/tooling/tests/documentation-only diagnostic runner
boundaries: no product UI, no recognizer changes, no pattern fixes, no export, no Scrub Key, no reinsert changes, no production gate

final commit SHA or PR link: e56535ec5ff2e86767e81a627df107aa10982613
handover path: handover/workpackages/20260617_0912_recall_benchmark_runner_minimal.md

files added:
- recall_benchmark_runner.py
- tests/test_recall_benchmark_runner_minimal.py
- RECALL_BENCHMARK_RUNNER_MINIMAL.md
- workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md
- handover/workpackages/20260617_0912_recall_benchmark_runner_minimal.md

files changed:
- corpus/legal/legal_false_positive_traps_seed_001.gold.json
- corpus/legal/legal_mixed_identifiers_seed_001.gold.json
- corpus/care/care_role_preservation_seed_001.gold.json
- corpus/care/care_mixed_identifiers_seed_001.gold.json
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md

product-code changes: none to app/product flow

tests/checks:
- Local tests were not runnable because the container could not resolve github.com for a local clone.
- Added tests/test_recall_benchmark_runner_minimal.py.
- Required checks remain pytest for corpus validator and runner tests, py_compile for recall_benchmark_runner.py and presidio_streamlit.py, and the Dutch legal recall baseline.
- GitHub Actions should be used as final execution proof.

GitHub Actions status: unknown through connector at closeout time.
Hugging Face sync status: unknown through connector at closeout time.
app verification status: not required; benchmark/tooling/tests/documentation-only and no app behavior changed.

runner summary:
- Loads synthetic gold sidecars and source files.
- Validates label and preserve-term offsets.
- Collects recognizer and candidate-scanner predictions when available.
- Falls back safely if optional analyzer dependencies are unavailable.
- Reports exact, text-normalized and overlap diagnostic matches.
- Reports missed required labels, wrong types, false-positive candidates, preserve-term hits and known-trap hits.
- Returns JSON-serializable per-document and summary report.

remaining gaps:
- Runner metrics are diagnostic only.
- No accepted recall/precision thresholds.
- No production-blocking benchmark gate.
- Corpus coverage is improved but still synthetic and not exhaustive.

remaining risks:
- Diagnostic runner output must not be interpreted as a product accuracy claim.
- Candidate scanner output is review-candidate surfacing, not hard automatic masking proof.
- Future thresholds/gates require separate approval.

next recommended step: do not automatically start another pattern-fix round. Consider WP_RECALL_BENCHMARK_THRESHOLDS_PLAN, WP_RECALL_BENCHMARK_REPORT_ARTIFACT or WP_DOCX_HYGIENE_RECALL_FOLLOWUP only after separate coordinator approval.
