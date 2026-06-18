status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_COVERAGE_TESTS — Add diagnostic tests for remaining PERSON-name recall gaps
started timestamp: 2026-06-18 08:22 Europe/Amsterdam
completed timestamp: 2026-06-18 08:22 Europe/Amsterdam
scope: tests/documentation-only PERSON-name coverage diagnostics
boundaries: no product code, no recognizer changes, no candidate scanner changes, no runner/report changes, no UI, no export, no Scrub Key, no reinsert, no thresholds, no gate, no product claim

final commit SHA or PR link: 83eec5a0784413a9161211c9d530d4ea931aad51
handover path: handover/workpackages/20260618_0822_recall_person_name_coverage_tests.md

files added:
- tests/test_recall_person_name_coverage_diagnostics.py
- handover/workpackages/20260618_0822_recall_person_name_coverage_tests.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md

files changed:
- RECALL_PERSON_NAME_COVERAGE_REVIEW.md
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md

product-code changes: none
recognizer changes: none
candidate scanner changes: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Added diagnostic tests for the PERSON-name gap inventory.
- Tests keep the known gap inventory visible without requiring current recognizers to pass all PERSON examples.
- Tests verify corpus/source grounding, required PERSON labels, context category examples, non-claim boundaries and no enforcement/gate boundary.

tests/checks:
- Added tests/test_recall_person_name_coverage_diagnostics.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Required verification command: python -m pytest -q tests/test_recall_person_name_coverage_diagnostics.py
- Recommended additional checks: python -m pytest -q tests/test_recall_gold_label_corpus_seed.py; python -m pytest -q tests/test_recall_benchmark_runner_minimal.py; git diff --check.

GitHub Actions status: pending/unknown at closeout time.
Hugging Face sync status: pending/unknown at closeout time.
app verification status: not required; no app behavior changed.

remaining risks:
- PERSON-name false-negative risk now has diagnostic test coverage but remains unfixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step: WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN after separate coordinator approval. Then consider WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS. Do not start follow-up work automatically.
