# Changelog — SolidPrivacy Scrub

## WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — Add contract tests for safe future PERSON-name recognition

Status: completed as tests/specification-only.

Files added:

- `tests/fixtures/person_name_recognizer_contract_cases.json`
- `tests/test_recall_person_name_recognizer_contracts.py`
- `PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md`
- `handover/workpackages/20260618_1852_recall_person_name_recognizer_contract_tests.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md`

Summary:

- Added contract fixture and tests for future safe PERSON-name recognition behavior.
- Contract cases cover future value-only hard recognizer cases, candidate-only weak-context cases, negative cases, single-surname policy and preserve terms.
- Tests validate fixture metadata, group completeness, value-only behavior, candidate-only review boundaries, negative-case boundaries, single-surname policy, preserve terms, non-claim boundaries and no enforcement/gate status.
- Added `PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md` to document the contract-only scope and next implementation route.

Intentionally not changed:

- No product code.
- No recognizer implementation.
- No candidate scanner implementation.
- No runner/report behavior changes.
- No workflow changes.
- No threshold enforcement.
- No gate.
- No product claim.
- No UI/export/Scrub Key/reinsert behavior changes.

Tests/checks:

- Added `tests/test_recall_person_name_recognizer_contracts.py`.
- Local tests were not run because this environment is connector-only and has no local Git working tree for pytest execution.
- Required check: `python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py`.

Next recommended step:

- Recommended next after separate approval: `WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY`.
- Then consider `WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW`.
- Do not start follow-up work automatically.

## WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN — Plan safe PERSON-name recognition improvements

Status: completed as planning/specification-only.

Summary:

- Added a planning/specification-only document for safe future PERSON-name recognition improvements.
- Planned a test-first route for PERSON-name coverage work.
- Recorded role/context preservation requirements and single-surname ambiguity.
- Defined that contract tests are required before any future implementation.

## WP_RECALL_PERSON_NAME_COVERAGE_TESTS — Add diagnostic tests for PERSON-name coverage gaps

Status: completed and verified as tests/documentation-only.

Summary:

- Added diagnostic tests for the PERSON-name gap inventory.
- Tests verify that the reviewed PERSON names remain documented, grounded in the synthetic corpus and represented as required direct-identifier PERSON gold labels.
- Tests verify context categories such as Arabic/Moroccan-style multi-token names, Dutch tussenvoegsel names, single surnames, professional-title contexts, care/legal role contexts and names near contact/reference data.
- Tests intentionally do not require current recognizers to pass all PERSON examples.
- Coordinator evidence showed Tests #1253 and Sync to Hugging Face Space #1264 green for commit `0927bec`.

## WP_RECALL_PERSON_NAME_COVERAGE_REVIEW — Review remaining PERSON-name recall gaps

Status: completed as review/planning/documentation-only.

Summary:

- Reviewed and classified the remaining missed `PERSON` labels from the cleaned diagnostic benchmark artifact.
- Classified name types and recommended tests/contracts before any recognizer implementation.

## WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — Plan diagnostic recall/precision thresholds without enforcement

Status: completed as planning/documentation-only.

Summary:

- Added a planning-only threshold policy document for the diagnostic recall/precision benchmark.
- Recorded the cleaned artifact baseline.
- No product code, tests, workflow, CI gate, production blocking, threshold enforcement or product claim was added.

## WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — Review cleaned diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Main findings:

- Cleaned artifact summary: 7 documents, 75 gold labels, 60 predictions, 56 exact matches, 57 text-normalized matches, 57 overlap matches, 18 missed required, 1 wrong-type, 1 false-positive candidate, 0 preserve-term hits and 1 known-trap hit.
- Cleanup materially reduced noise versus the first artifact.
- Remaining misses are concentrated in person names, care room/location references and one client-number example.

## Previous benchmark entries

- WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — completed and coordinator-verified mapping/counting cleanup.
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
