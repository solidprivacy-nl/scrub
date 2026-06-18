status: completed_pending_verification
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — Implement safe helper-level PERSON-name recognition improvements
started timestamp: 2026-06-18 20:48 Europe/Amsterdam
completed timestamp: 2026-06-18 20:48 Europe/Amsterdam
regex-fix timestamp: 2026-06-18 20:58 Europe/Amsterdam
scope: helper/recognizer implementation + tests for contract-backed PERSON-name recognition
boundaries: no UI, no export, no Scrub Key, no reinsert, no threshold enforcement, no production gate, no product claim

final commit SHA or PR link: 88324e49bc3080da95b297ae6638ead394b87009
handover path: handover/workpackages/20260618_2048_recall_person_name_recognizer_implementation_helper_only.md

files added:
- person_name_recognizer_helper.py
- tests/test_recall_person_name_recognizer_implementation.py
- handover/workpackages/20260618_2048_recall_person_name_recognizer_implementation_helper_only.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md

files changed:
- person_name_recognizer_helper.py
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- handover/workpackages/20260618_2048_recall_person_name_recognizer_implementation_helper_only.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md

product-code changes: helper module added and regex casing tightened; no Streamlit/UI/export/Scrub Key/reinsert changes
recognizer implementation summary: contract-backed value-only role/title PERSON-name helper for strong-context examples; role/title cue case-insensitive; name tokens uppercase-sensitive
candidate scanner changes: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Implemented helper-level value-only role/title PERSON-name matching.
- Added implementation tests that load existing contract fixture.
- Positive contract cases must be matched value-only.
- Negative contract cases must not match.
- Candidate-only cases remain not automatic.
- Single-surname matching remains limited to strong role/title context.
- Helper is not registered into the Streamlit app recognizer setup in this package.
- Fixed first failing test attempt by removing global regex IGNORECASE and scoping case-insensitivity to the role/title cue only.

tests/checks:
- Added tests/test_recall_person_name_recognizer_implementation.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Coordinator screenshot showed first implementation attempt had failing Tests on commit fbefcde.
- Required checks after regex fix: python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py; python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py; python -m pytest -q tests/test_recall_person_name_coverage_diagnostics.py; python -m pytest -q tests/test_recall_gold_label_corpus_seed.py.
- Recommended checks: python -m pytest -q tests/test_recall_benchmark_runner_minimal.py; python -m pytest -q; python -m py_compile person_name_recognizer_helper.py; python -m py_compile dutch_recognizers.py; python -m py_compile candidate_scanner.py; python -m py_compile presidio_streamlit.py; git diff --check.

GitHub Actions status: pending/unknown after regex fix.
Hugging Face sync status: pending/unknown after regex fix.
app verification status: pending smoke verification after green Actions/HF sync. No app behavior change is expected because helper is not wired into the Streamlit recognizer setup.

remaining risks:
- PERSON-name false-negative risk is only partially mitigated for contract-backed role/title helper cases.
- Helper is not yet benchmark-reviewed.
- Helper is not registered into app recognizer setup in this package.
- Candidate-only weak contexts remain not automatic.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step after green tests/HF sync/app smoke: WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW. Do not start follow-up work automatically.
