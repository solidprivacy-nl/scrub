# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: completed  
Implementation status: `RELEASE_CANDIDATE_READY`  
Governance status: pending independent assurance

Claimed: 2026-08-06 11:38 Europe/Amsterdam  
Implementation completed: 2026-08-06 12:00 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Branch: `wp/processed-text-selection-cross-flow-regression`  
Role: `implementation_operations`

## Scope

Add regression evidence proving that a row created through processed-text selection remains a normal authoritative replacement-table row across:

- processed text export;
- TXT and DOCX export paths;
- Scrub Key generation and validation;
- TXT and DOCX reinsert;
- replacement-table CSV and scrub-report audit evidence.

## Boundaries

- tests and supporting documentation only;
- no production UI or product-code changes;
- no change to recognizers, replacement semantics, filenames, MIME types, Scrub Key schema/binding, reinsert behavior or audit semantics;
- synthetic data only;
- human review remains mandatory.

## Candidate evidence

- PR #69, draft and not merged
- `tests/test_processed_text_selection_cross_flow_regression.py`
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`
- `handover/workpackages/20260806_1157_processed_text_selection_cross_flow_regression.md`

## Validation status

- Focused tests added: 5
- Local test execution: unavailable in connector-only implementation session
- GitHub Actions run #2097 on the pre-closeout PR candidate: `1165 passed in 9.62s`
- Final exact-head GitHub Actions run: pending after administrative closeout commits
- Hugging Face sync: not applicable; no runtime files changed
- App verification: not applicable; no UI behavior changed
- Independent governance decision: pending and deliberately not issued by implementation

## Next step

The separate `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY` package must be claimed by `governance_release_assurance`. That worker/session must reconstruct the candidate from source, acceptance criteria and raw machine evidence, record its initial decision before reading the implementation handover, and must not repair the candidate under review.
