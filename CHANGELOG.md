# Changelog — SolidPrivacy Scrub

## WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator punctuation handling

Status: completed as tests-only repair after GitHub Actions failure.

Files added:

- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md`
- `handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md`

Files changed:

- `tests/test_recall_gold_label_corpus_seed.py`
- `CHANGELOG.md`

Summary:

- GitHub Actions screenshots showed `tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only` failing.
- Root cause: the email regex captured sentence-final punctuation, for example `sami.elamrani@example.test.`.
- Fixed the validator regex so email matches end on an alphanumeric domain character.
- This keeps `.example.test` enforcement intact while allowing normal punctuation after synthetic email addresses.

Tests/checks:

- Local tests were not runnable in this environment because no local GitHub working tree is available.
- GitHub Actions should be used as final execution proof for repair commit `151749e4e4f19d3eaeffce52b1b83a807e15df5c`.

Intentionally not changed:

- No product code change.
- No runner logic change.
- No recognizer/pattern fix.
- No UI/export/Scrub Key/reinsert behavior change.

Next recommended step:

- Wait for GitHub Actions Tests and Hugging Face sync for the repair commit before starting a new workpackage.

## WP_RECALL_BENCHMARK_RUNNER_MINIMAL — Add minimal diagnostic recall/precision runner

Status: completed as benchmark/tooling/tests/documentation-only.

Files added:

- `recall_benchmark_runner.py`
- `tests/test_recall_benchmark_runner_minimal.py`
- `RECALL_BENCHMARK_RUNNER_MINIMAL.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md`
- `handover/workpackages/20260617_0912_recall_benchmark_runner_minimal.md`

Files changed:

- `corpus/legal/legal_false_positive_traps_seed_001.gold.json`
- `corpus/legal/legal_mixed_identifiers_seed_001.gold.json`
- `corpus/care/care_role_preservation_seed_001.gold.json`
- `corpus/care/care_mixed_identifiers_seed_001.gold.json`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_MINIMAL.md`

Summary:

- Added a minimal diagnostic recall/precision runner for the synthetic gold-label corpus.
- Runner loads sidecars, validates source offsets and collects recognizer/candidate-scanner predictions when optional dependencies are available.
- Runner compares gold labels and predictions using exact span, text-normalized and overlap diagnostic matching.
- Runner reports missed required labels, wrong-type hits, false-positive candidates, preserve-term hits and known-trap hits.
- Added a JSON-serializable per-document and summary report structure.
- Added optional CLI usage: `python recall_benchmark_runner.py --corpus corpus --json`.
- Added tests for sidecar loading, normalization, matching, preserve-term hits, known-trap hits and corpus smoke reporting.
- Corrected four expanded-corpus sidecars using recalculated offsets so the sidecar validator can check the expanded corpus reliably.
- Added `RECALL_BENCHMARK_RUNNER_MINIMAL.md` documenting purpose, inputs, outputs, matching rules, entity mapping, limitations and non-claim boundaries.

Tests/checks:

- Local tests were not runnable in this environment because there is no local GitHub working tree available for pytest/py_compile execution.
- Required test commands remain:
  - `python -m pytest -q tests/test_recall_gold_label_corpus_seed.py`
  - `python -m pytest -q tests/test_recall_benchmark_runner_minimal.py`
  - `python -m py_compile recall_benchmark_runner.py`
  - `python -m py_compile presidio_streamlit.py`
  - `python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py`
- GitHub Actions and Hugging Face sync should be used as final execution proof for the benchmark/tooling commits.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No `candidate_scanner.py` change.
- No `dutch_recognizers.py` change.
- No recognizer/pattern fix.
- No product UI change.
- No review table change.
- No side-by-side change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No DOCX/PDF flow change.
- No Docker/startup/dependency change.
- No cloud processing.
- No production threshold or blocking gate.

Remaining gaps:

- Runner metrics are diagnostic only.
- No accepted recall/precision thresholds exist yet.
- No production-blocking benchmark gate exists yet.
- Corpus coverage is improved but still synthetic and not exhaustive.
- No product accuracy claim is supported.

Next recommended step:

- Do not automatically start another pattern-fix round.
- Consider `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` after separate approval if benchmark governance is next.
- Consider `WP_RECALL_BENCHMARK_REPORT_ARTIFACT` after separate approval if CI artifacts/diagnostic reports are desired first.
- Consider `WP_DOCX_HYGIENE_RECALL_FOLLOWUP` if document/export risks now dominate.

## WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — Expand synthetic gold-label corpus

Status: completed as benchmark/data/documentation-only.

Summary:

- Expanded the synthetic gold-label corpus from 3 to 7 source documents.
- Added legal false-positive traps for article references, legal subsection references, page/attachment/exhibit labels, dates, times and money amounts.
- Added legal mixed identifiers covering case, role/court reference, dossier, client, claim, invoice, financial, civil-service-like, ECLI, names, phone, email and address values.
- Added care role-preservation corpus covering care role words and role/name combinations.
- Added care mixed identifiers covering room, department, incident, client number, care dossier, medication code, device reference, professional-number-like value, names, phone and email.
- Extended the sidecar validator for the expanded expected sidecars and additional preserve-context terms.

## WP_RECALL_GOLD_LABEL_CORPUS_SEED — Add synthetic gold-label corpus seed

Status: completed as benchmark/data/documentation-only.

Summary:

- Added a first synthetic gold-label corpus seed for future recall/precision benchmarking.
- Added legal reference, legal role-preservation and care reference seed texts.
- Added sidecars with exact offsets, labels, preserve terms and known traps.
- Added tests-only sidecar integrity checks.

## WP_RECALL_SCORECARD_REFRESH — Refresh recall/precision scorecard after Dutch legal fixes

Status: completed as benchmark/documentation-only.

Summary:

- Added `RECALL_PRECISION_SCORECARD.md` because no scorecard file existed at repo root.
- Refreshed Dutch legal recall/precision status after the gap tests, first pattern-fix round and verify closeout.
- Clarified that improvement is review-candidate visibility, not a complete automatic-recognition guarantee.

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
