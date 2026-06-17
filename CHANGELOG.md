# Changelog — SolidPrivacy Scrub

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT — Add diagnostic recall benchmark report artifact

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Files added:

- `recall_benchmark_report.py`
- `tests/test_recall_benchmark_report_artifact.py`
- `.github/workflows/recall-benchmark-report.yml`
- `RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `handover/workpackages/20260617_1758_recall_benchmark_report_artifact.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT.md`

Summary:

- Added `recall_benchmark_report.py` to wrap the existing diagnostic runner output with metadata and write JSON/Markdown report files.
- Added `tests/test_recall_benchmark_report_artifact.py` for JSON metadata, Markdown summary, file writing, no-threshold behavior and CLI smoke output.
- Added `.github/workflows/recall-benchmark-report.yml` to run corpus/runner/report tests, generate the diagnostic report and upload it as an artifact.
- Added `RECALL_BENCHMARK_REPORT_ARTIFACT.md` documenting the workflow, artifact files, report formats, interpretation and non-claim boundaries.
- Updated the recall/precision scorecard, workpackage status and risk register to record that runner output is now CI-visible as a diagnostic artifact.

Tests/checks:

- Local tests were not runnable in this environment because there is no local GitHub working tree available for pytest/py_compile execution.
- Coordinator evidence shows:
  - `a3df5c7` — `Diagnostic recall benchmark report #1` green.
  - `31ee53b` — `Tests #1193` green.
  - `31ee53b` — `Sync to Hugging Face Space #1204` green.
  - Hugging Face app screenshot shows the Space running without Script execution error.

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
- No product accuracy claim.

Remaining gaps:

- Report metrics are diagnostic only.
- No accepted recall/precision thresholds exist yet.
- No production-blocking benchmark gate exists yet.
- Corpus coverage is improved but still synthetic and not exhaustive.
- First artifact output still needs content review before threshold planning.

Next recommended step:

- Do not automatically start another pattern-fix round.
- Consider `WP_RECALL_BENCHMARK_REPORT_REVIEW` after separate approval if the first artifact output should be reviewed.
- Consider `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` only after artifact review and separate approval.
- Consider `WP_DOCX_HYGIENE_RECALL_FOLLOWUP` if document/export risks now dominate.

## WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator punctuation handling

Status: completed as tests-only repair after GitHub Actions failure.

Summary:

- GitHub Actions screenshots showed `tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only` failing.
- Root cause: the email regex first captured sentence-final punctuation, and the assertion then used the wrong suffix check for `@example.test` domains.
- Final repair checks the email domain after `@` equals `example.test`.
- Coordinator evidence later showed the repair commits green in Tests and HF sync.

## WP_RECALL_BENCHMARK_RUNNER_MINIMAL — Add minimal diagnostic recall/precision runner

Status: completed as benchmark/tooling/tests/documentation-only.

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
