# Handover — WP20 Synthetic messy Dutch legal/zorg benchmark corpus

Repository: solidprivacy-nl/scrub  
Workpackage title: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus  
Status: completed benchmark-corpus-only

## Summary

Created a first synthetic messy Dutch benchmark corpus foundation under `benchmark/corpus/`, with separate legal, zorg and mixed professional fixtures. Added corpus documentation and a gold-label README that explains the future zero-based offset direction without implementing a full schema, runner or CI gate.

This work intentionally did not change recognizer logic, tests, UI, dependencies, export/reinsert behavior, real data handling or cloud processing.

## Files added

- `benchmark/corpus/README.md`
- `benchmark/corpus/legal/legal_process_messy_001.txt`
- `benchmark/corpus/zorg/care_operations_messy_001.txt`
- `benchmark/corpus/mixed/legal_care_mixed_messy_001.txt`
- `benchmark/gold/README.md`
- `handover/workpackages/20260610_0045_synthetic_messy_benchmark_corpus.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests were added.
- No tests were changed.
- No test suite was run because this was a benchmark-corpus-only workpackage with no code changes.

## Validation status

- Required start files were read.
- `RECALL_BENCHMARK_SPEC.md` and `PARALLEL_SPEC_CONSOLIDATION_WP58.md` were read and used as the source for scope and sequencing.
- `legal_test_examples.py`, `dutch_recognizers.py` and test context were inspected for context only.
- Corpus fixtures were reviewed for synthetic-only markings and coverage of requested entity categories.
- `RISK_REGISTER.md` optional update was attempted after a SHA conflict was resolved, but the full-file update was blocked by the tool safety layer. The file was therefore intentionally left unchanged rather than risk overwriting parallel WP26 updates.

## GitHub Actions status

- To be checked after the final handover commit.

## Hugging Face sync status

- To be checked after the final handover commit.

## App verification status

- Not applicable. No UI behavior changed.

## Remaining risks

- R1 false negatives / missed sensitive data remains critical and only partially mitigated.
- The corpus is source-text only; there is no full gold-label schema yet.
- No zero-based offset sidecars exist yet.
- No benchmark runner exists yet.
- No CI scorecard or residual-risk report exists yet.
- Synthetic fixtures do not prove real-world safety on confidential documents.

## Next recommended step

- WP21 — Gold-label entity schema.
