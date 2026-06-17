status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — Plan diagnostic recall/precision thresholds without enforcement
started timestamp: 2026-06-17 22:18 Europe/Amsterdam
completed timestamp: 2026-06-17 22:18 Europe/Amsterdam
scope: planning/documentation-only threshold policy design
boundaries: no product code, no recognizer changes, no runner/report behavior changes, no CI gate, no production blocking, no threshold enforcement, no product claim

final commit SHA or PR link: 321c82a4f202998d3d38ecaabc06deffa0aee396
handover path: handover/workpackages/20260617_2218_recall_benchmark_thresholds_plan.md

files added:
- RECALL_BENCHMARK_THRESHOLDS_PLAN.md
- handover/workpackages/20260617_2218_recall_benchmark_thresholds_plan.md
- workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md

files changed:
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md

product-code changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Added planning-only diagnostic recall/precision threshold policy.
- Recorded cleaned artifact baseline values.
- Defined metric categories and class-specific planning.
- Defined required preconditions before any future gate.
- Documented product-claim boundaries.

tests/checks:
- Local tests were not run because this package is planning/documentation-only and only markdown/governance files changed.
- git diff --check was not runnable in this connector-only environment.

GitHub Actions status: not applicable for functional validation; documentation-only.
Hugging Face sync status: unknown at closeout time.
app verification status: not required; no app behavior changed.

remaining gaps:
- No accepted recall/precision thresholds.
- No production benchmark gate.
- Corpus is synthetic and small.
- Remaining gaps: 14 missed PERSON labels, 3 care room/location labels, 1 client-number issue, 1 nested false-positive BSN-like hit inside a phone-like value, 1 care-location known-trap signal.

remaining risks:
- Diagnostic benchmark output must not be interpreted as product safety proof.
- Future thresholds/gates require separate approval.
- Product claims remain blocked.

next recommended step: WP_RECALL_PERSON_NAME_COVERAGE_REVIEW after separate coordinator approval. Alternatives: WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN, WP_CLIENT_REFERENCE_COVERAGE_REVIEW, WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS. Do not start follow-up work automatically.
