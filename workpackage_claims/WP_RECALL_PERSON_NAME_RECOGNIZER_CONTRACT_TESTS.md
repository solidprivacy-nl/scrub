status: completed_pending_verification
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — Add contract tests for safe future PERSON-name recognition
started timestamp: 2026-06-18 18:52 Europe/Amsterdam
completed timestamp: 2026-06-18 18:52 Europe/Amsterdam
wording-fix timestamp: 2026-06-18 18:59 Europe/Amsterdam
scope: tests/specification-only PERSON-name recognizer contract tests
boundaries: no product code, no recognizer implementation, no candidate scanner implementation, no runner/report changes, no UI, no export, no Scrub Key, no reinsert, no thresholds, no gate, no product claim

final commit SHA or PR link: 8b68dd885abba4a7a8bc50b50874c1d511b31d2e
handover path: handover/workpackages/20260618_1852_recall_person_name_recognizer_contract_tests.md

files added:
- tests/fixtures/person_name_recognizer_contract_cases.json
- tests/test_recall_person_name_recognizer_contracts.py
- PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md
- handover/workpackages/20260618_1852_recall_person_name_recognizer_contract_tests.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md

files changed:
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- DECISION_LOG.md
- handover/workpackages/20260618_1852_recall_person_name_recognizer_contract_tests.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md

product-code changes: none
recognizer implementation: none
candidate scanner implementation: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Added contract fixture and tests for safe future PERSON-name recognition behavior.
- Added contract documentation and decision log update.
- Contract tests define value-only behavior, preserve terms, single-surname policy, candidate-only weak contexts, negative cases, and no threshold/gate/product-claim boundaries.
- Fixed docs-only wording after coordinator screenshot showed existing regression test expected exact phrase: no recognizer changes.

tests/checks:
- Added tests/test_recall_person_name_recognizer_contracts.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Required verification command: python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py
- Recommended additional checks: python -m pytest -q tests/test_recall_person_name_coverage_diagnostics.py; python -m pytest -q tests/test_recall_gold_label_corpus_seed.py; git diff --check.
- Coordinator screenshot before wording fix showed failing test_recall_person_name_coverage_diagnostics due missing exact phrase no recognizer changes in scorecard. Wording fix restored that phrase.

GitHub Actions status: pending/unknown after wording fix.
Hugging Face sync status: pending/unknown after wording fix; earlier screenshot showed HF HTTP 429, likely transient/rate-limit.
app verification status: not required; no app behavior changed.

remaining risks:
- PERSON-name false-negative risk now has diagnostic and contract test coverage but remains unfixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step after green verification: WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY after separate coordinator approval. Then consider WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW. Do not start follow-up work automatically.
