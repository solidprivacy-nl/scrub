# Changelog — SolidPrivacy Scrub

## WP_RECALL_BENCHMARK_REPORT_REVIEW — Review first diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Files added:

- `RECALL_BENCHMARK_REPORT_REVIEW.md`
- `handover/workpackages/20260617_2116_recall_benchmark_report_review.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW.md`

Artifact reviewed:

- `diagnostic-recall-benchmark-report`
- `recall_benchmark_report.json`
- `recall_benchmark_summary.md`

Main findings:

- Artifact integrity passed: `diagnostic_only`, synthetic corpus, no production gate and no enforced thresholds.
- Summary: 7 documents, 75 gold labels, 61 predictions, 41 matched required labels, 34 missed required labels, 11 wrong-type findings, 8 false-positive candidates, 0 preserve-term hits and 1 known-trap hit.
- The artifact is useful for engineering review, but not ready for threshold planning.
- Raw metrics are likely inflated by runner mapping, acceptable-type taxonomy and duplicate prediction accounting issues.
- Likely mapping/taxonomy follow-ups include `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, `NL_LEGAL_PARTY_NAME`, care `ZORG-CL-*` values and absent email predictions.

Tests/checks:

- Local tests were not runnable in this environment because there is no local GitHub working tree available.
- This package is review/documentation-only.
- Previous coordinator evidence remains the execution proof for the artifact workflow:
  - `a3df5c7` — `Diagnostic recall benchmark report #1` green.
  - `31ee53b` — `Tests #1193` green.
  - `31ee53b` — `Sync to Hugging Face Space #1204` green.

Intentionally not changed:

- No product code change.
- No `presidio_streamlit.py` change.
- No `candidate_scanner.py` change.
- No `dutch_recognizers.py` change.
- No `recall_benchmark_runner.py` change.
- No `recall_benchmark_report.py` change.
- No workflow change.
- No recognizer/pattern fix.
- No UI/export/Scrub Key/reinsert behavior change.
- No thresholds.
- No production gate.
- No product accuracy claim.

Next recommended step:

- Do not start threshold planning yet.
- Recommended next after separate approval: `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX`.
- Only after mapping/dedup/taxonomy cleanup, consider `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN`.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT — Add diagnostic recall benchmark report artifact

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Files added:

- `recall_benchmark_report.py`
- `tests/test_recall_benchmark_report_artifact.py`
- `.github/workflows/recall-benchmark-report.yml`
- `RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_ARTIFACT.md`
- `handover/workpackages/20260617_1758_recall_benchmark_report_artifact.md`

Summary:

- Added `recall_benchmark_report.py` to wrap the existing diagnostic runner output with metadata and write JSON/Markdown report files.
- Added tests for JSON metadata, Markdown summary, file writing, no-threshold behavior and CLI smoke output.
- Added workflow `Diagnostic recall benchmark report` to generate and upload `diagnostic-recall-benchmark-report`.
- Coordinator evidence shows the report workflow, Tests and HF sync were green.
- No product UI, recognizer, export, Scrub Key, reinsert, threshold or production-gate behavior was changed.

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
