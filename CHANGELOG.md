# Changelog — SolidPrivacy Scrub

## WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — Review cleaned diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Files added:

- `RECALL_BENCHMARK_REPORT_REVIEW_2.md`
- `handover/workpackages/20260617_2212_recall_benchmark_report_review_2.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW_2.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_REPORT_REVIEW_2.md`

Artifact reviewed:

- `diagnostic-recall-benchmark-report`
- `recall_benchmark_report.json`
- `recall_benchmark_summary.md`

Main findings:

- Artifact integrity passed: `diagnostic_only`, synthetic corpus, no production gate and no enforced thresholds.
- Cleaned artifact summary: 7 documents, 75 gold labels, 60 predictions, 56 exact matches, 57 text-normalized matches, 57 overlap matches, 18 missed required, 1 wrong-type, 1 false-positive candidate, 0 preserve-term hits and 1 known-trap hit.
- Cleanup materially reduced noise versus the first artifact: missed required 34 -> 18, wrong-type 11 -> 1, false positives 8 -> 1, exact matches 41 -> 56.
- Remaining misses are concentrated in person names, care room/location references and one client-number example.
- Threshold planning is now reasonable as a planning-only package, but no thresholds, gates or product claims are accepted.

Tests/checks:

- Local tests were not run because this is review/documentation-only and no product/test code was changed.
- Previous coordinator evidence remains execution proof for the cleaned artifact package:
  - `59473fb` — `Tests #1218` green.
  - `59473fb` — `Sync to Hugging Face Space #1228` green.
  - Diagnostic recall benchmark report workflow green for relevant cleanup commits.

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

- Recommended next after separate approval: `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN`.
- Scope must be planning-only: no CI gate, no production blocking, no threshold enforcement and no product claim.
- Backlog after threshold planning may include person-name coverage, care-location/reference candidate planning and client-reference coverage review.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — Clean diagnostic recall benchmark report mapping/counting

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

Summary:

- Cleaned diagnostic runner/report mapping and counting noise found in the first artifact review.
- Added benchmark/report mappings for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, `NL_LEGAL_PARTY_NAME` and `EMAIL_ADDRESS`.
- Added benchmark-only email predictions with source `benchmark_builtin` so synthetic `@example.test` email labels are not missed merely because the runner does not instantiate Presidio default recognizers.
- Added prediction deduplication for report accounting by text/entity/start/end/source.
- Deduplication now applies before document comparison and to wrong-type, false-positive, preserve-term and known-trap accounting.
- Clarified selected care corpus acceptable entity types for `ZORG-CL-*`, care department/location values and legal-party-name person-name output.
- Added tests for mapping cleanup, care reference acceptable type handling, deduplication, matched-prediction false-positive prevention and benchmark-only email behavior.
- Coordinator evidence showed Tests, HF sync and Diagnostic recall benchmark report workflow green for the cleanup commits.

## WP_RECALL_BENCHMARK_REPORT_REVIEW — Review first diagnostic recall benchmark artifact

Status: completed as review/documentation-only.

Artifact reviewed:

- `diagnostic-recall-benchmark-report`
- `recall_benchmark_report.json`
- `recall_benchmark_summary.md`

Main findings:

- Artifact integrity passed: `diagnostic_only`, synthetic corpus, no production gate and no enforced thresholds.
- Summary: 7 documents, 75 gold labels, 61 predictions, 41 matched required labels, 34 missed required labels, 11 wrong-type findings, 8 false-positive candidates, 0 preserve-term hits and 1 known-trap hit.
- The artifact was useful for engineering review, but not ready for threshold planning.
- Raw metrics were likely inflated by runner mapping, acceptable-type taxonomy and duplicate prediction accounting issues.

## WP_RECALL_BENCHMARK_REPORT_ARTIFACT — Add diagnostic recall benchmark report artifact

Status: completed and coordinator-verified as benchmark/tooling/tests/documentation-only.

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
