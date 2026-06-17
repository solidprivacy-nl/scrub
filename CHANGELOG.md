# Changelog — SolidPrivacy Scrub

## WP_RECALL_PERSON_NAME_COVERAGE_REVIEW — Review remaining PERSON-name recall gaps

Status: completed as review/planning/documentation-only.

Files added:

- `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`
- `handover/workpackages/20260617_2223_recall_person_name_coverage_review.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md`

Summary:

- Reviewed and classified the 14 remaining missed `PERSON` labels from the cleaned diagnostic benchmark artifact.
- Added inventory table with document, source, missed name, context, likely pattern, likely cause, risk and follow-up.
- Classified name types: Dutch names with tussenvoegsel, Arabic/Moroccan-style multi-token names, first-name/surname patterns, single surnames, professional-title context, care-role context, legal-role context, names near contact data and names near care/legal references.
- Concluded that remaining PERSON gaps now look mostly like recognizer/candidate-design coverage issues, not benchmark mapping noise.
- Recommended tests/contracts before any recognizer implementation.

Intentionally not changed:

- No product code.
- No recognizer changes.
- No candidate scanner changes.
- No runner/report behavior changes.
- No workflow changes.
- No tests enforcing thresholds.
- No UI/export/Scrub Key/reinsert behavior changes.
- No thresholds.
- No gate.
- No product claim.

Tests/checks:

- Local tests were not run because this package is review/planning/documentation-only and only markdown/governance files changed.
- `git diff --check` was not runnable in this connector-only environment.

Next recommended step:

- Recommended next after separate approval: `WP_RECALL_PERSON_NAME_COVERAGE_TESTS`.
- Alternative if design should come first: `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN`.
- Do not start follow-up work automatically.

## WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — Plan diagnostic recall/precision thresholds without enforcement

Status: completed as planning/documentation-only.

Summary:

- Added a planning-only threshold policy document for the diagnostic recall/precision benchmark.
- Recorded the cleaned artifact baseline.
- Defined metric meanings and which metrics are hard, soft or diagnostic-only.
- Defined planning categories: planning baseline, warning threshold, release review threshold and future blocking threshold.
- Added class-specific planning and mandatory conditions before any real gate.
- No product code, tests, workflow, CI gate, production blocking, threshold enforcement or product claim was added.

## WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — Review cleaned diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Main findings:

- Cleaned artifact summary: 7 documents, 75 gold labels, 60 predictions, 56 exact matches, 57 text-normalized matches, 57 overlap matches, 18 missed required, 1 wrong-type, 1 false-positive candidate, 0 preserve-term hits and 1 known-trap hit.
- Cleanup materially reduced noise versus the first artifact.
- Remaining misses are concentrated in person names, care room/location references and one client-number example.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping/counting

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Summary:

- Cleaned diagnostic runner/report mapping and counting noise found in the first artifact review.
- Added benchmark/report mappings for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, `NL_LEGAL_PARTY_NAME` and `EMAIL_ADDRESS`.
- Added benchmark-only email predictions with source `benchmark_builtin`.
- Added prediction deduplication for report accounting by text/entity/start/end/source.
- Coordinator evidence showed Tests, HF sync and Diagnostic recall benchmark report workflow green for the cleanup commits.

## Previous benchmark entries

- WP_RECALL_BENCHMARK_REPORT_REVIEW — completed first diagnostic artifact review.
- WP_RECALL_BENCHMARK_REPORT_ARTIFACT — completed and coordinator-verified diagnostic artifact workflow.
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
