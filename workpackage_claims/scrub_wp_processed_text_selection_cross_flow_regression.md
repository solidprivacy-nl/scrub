# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: in_progress

Claimed: 2026-08-06 11:38 Europe/Amsterdam  
Repository: solidprivacy-nl/scrub  
Branch: wp/processed-text-selection-cross-flow-regression  
Role: implementation_operations

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

## Separation of duties

Implementation may prepare only a release candidate. The separate `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY` workpackage must be executed by `governance_release_assurance` from source and machine evidence without reading implementation conclusions first.
