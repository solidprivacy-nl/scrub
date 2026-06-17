# Changelog — SolidPrivacy Scrub

## WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — Plan diagnostic recall/precision thresholds without enforcement

Status: completed as planning/documentation-only.

Files added:

- `RECALL_BENCHMARK_THRESHOLDS_PLAN.md`
- `handover/workpackages/20260617_2218_recall_benchmark_thresholds_plan.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.md`

Summary:

- Added a planning-only threshold policy document for the diagnostic recall/precision benchmark.
- Recorded the cleaned artifact baseline: 7 documents, 75 gold labels, 60 predictions, 56 exact matches, 57 text-normalized matches, 57 overlap matches, 18 missed required, 1 wrong type, 1 false-positive candidate, 0 preserve-term hits and 1 known-trap hit.
- Defined metric meanings and which metrics are hard, soft or diagnostic-only.
- Defined planning categories: planning baseline, warning threshold, release review threshold and future blocking threshold.
- Added class-specific planning for PERSON, legal references/case numbers, client numbers, care references, email, phone, IBAN, BSN, address/location, preserve terms and known traps.
- Documented mandatory conditions before any real gate may be considered.

Intentionally not changed:

- No product code.
- No tests changed to enforce thresholds.
- No runner/report behavior change.
- No workflow change.
- No CI gate.
- No production blocking.
- No threshold enforcement.
- No product claim.
- No UI/export/Scrub Key/reinsert behavior change.

Tests/checks:

- Local tests were not run because this package is planning/documentation-only and only markdown/governance files changed.
- `git diff --check` was not runnable in this connector-only environment.

Next recommended step:

- Recommended next after separate approval: `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW`.
- Alternative next packages: `WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN`, `WP_CLIENT_REFERENCE_COVERAGE_REVIEW`, `WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS`.
- Do not start any follow-up automatically.

## WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — Review cleaned diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Main findings:

- Artifact integrity passed: `diagnostic_only`, synthetic corpus, no production gate and no enforced thresholds.
- Cleaned artifact summary: 7 documents, 75 gold labels, 60 predictions, 56 exact matches, 57 text-normalized matches, 57 overlap matches, 18 missed required, 1 wrong-type, 1 false-positive candidate, 0 preserve-term hits and 1 known-trap hit.
- Cleanup materially reduced noise versus the first artifact: missed required 34 -> 18, wrong-type 11 -> 1, false positives 8 -> 1, exact matches 41 -> 56.
- Remaining misses are concentrated in person names, care room/location references and one client-number example.
- Threshold planning is now reasonable as a planning-only package, but no thresholds, gates or product claims are accepted.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping/counting

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Summary:

- Cleaned diagnostic runner/report mapping and counting noise found in the first artifact review.
- Added benchmark/report mappings for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, `NL_LEGAL_PARTY_NAME` and `EMAIL_ADDRESS`.
- Added benchmark-only email predictions with source `benchmark_builtin`.
- Added prediction deduplication for report accounting by text/entity/start/end/source.
- Clarified selected care corpus acceptable entity types for `ZORG-CL-*`, care department/location values and legal-party-name person-name output.
- Coordinator evidence showed Tests, HF sync and Diagnostic recall benchmark report workflow green for the cleanup commits.

## WP_RECALL_BENCHMARK_REPORT_REVIEW — Review first diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Main findings:

- Artifact integrity passed: `diagnostic_only`, synthetic corpus, no production gate and no enforced thresholds.
- Summary: 7 documents, 75 gold labels, 61 predictions, 41 matched required labels, 34 missed required labels, 11 wrong-type findings, 8 false-positive candidates, 0 preserve-term hits and 1 known-trap hit.
- The artifact was useful for engineering review, but not ready for threshold planning.
- Raw metrics were likely inflated by runner mapping, acceptable-type taxonomy and duplicate prediction accounting issues.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT — Add diagnostic recall benchmark report artifact

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Summary:

- Added `recall_benchmark_report.py` to wrap the existing diagnostic runner output with metadata and write JSON/Markdown report files.
- Added workflow `Diagnostic recall benchmark report` to generate and upload `diagnostic-recall-benchmark-report`.
- Coordinator evidence shows the report workflow, Tests and HF sync were green.
- No product UI, recognizer, export, Scrub Key, reinsert, threshold or production-gate behavior was changed.

## Previous benchmark entries

- WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — completed tests-only repair.
- WP_RECALL_BENCHMARK_RUNNER_MINIMAL — completed diagnostic runner.
- WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — completed expanded synthetic corpus.
- WP_RECALL_GOLD_LABEL_CORPUS_SEED — completed first synthetic corpus seed.
- WP_RECALL_SCORECARD_REFRESH — completed scorecard refresh.

## Recent previous entries

Detailed previous history remains available in Git history and includes:

- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — verified Dutch legal recall pattern fixes.
- WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — targeted helper-level detection improvement.
- WP_DUTCH_LEGAL_RECALL_GAP_TESTS — tests-only baseline for known Dutch legal recall gaps.
- WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — repo-hygiene cleanup after verified promotion.
- WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — verified promoted collapsible review table.
- WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — contract tests for collapsible review table section.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP39D — DOCX hygiene audit UI implementation.
