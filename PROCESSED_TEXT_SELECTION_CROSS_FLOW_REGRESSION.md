# Processed-text selection — Cross-flow regression contract

Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`  
Role: `implementation_operations`  
Candidate status: test/documentation release candidate; independent assurance required.

## Purpose

Freeze machine evidence that a masking row created from a processed-text selection enters the same document-scoped, review-table-authoritative path as every other reviewed replacement row.

## Acceptance matrix

| Flow | Required evidence |
|---|---|
| Selection commit | One normal included row, document-bound placeholder, `manual_selection` provenance, `all_exact` scope and exact occurrence count. |
| Processed text / TXT export | Every exact occurrence is replaced by the row's full bound placeholder. |
| DOCX export | The same reviewed mapping is applied to the original DOCX path without changing document-export semantics. |
| Scrub Key | The row becomes one valid schema-1.1 mapping item with the same original value, placeholder, source and document binding. |
| TXT reinsert | The bound key restores all occurrences and reports a verified document match. |
| DOCX reinsert | The bound key restores supported DOCX text and reports a verified document match. |
| CSV audit | The row's original value, placeholder, entity type and `manual_selection` source remain visible in the replacement report. |
| Scrub report | The row contributes to the existing entity-count evidence without changing report semantics. |
| Review exclusion | `include=false` prevents document replacement and omits the row from the Scrub Key. |
| Custom replacement | Free replacement text remains allowed in document export, while verified bound-key generation fails closed. |

## Safety boundaries

- synthetic data only;
- no production code or Streamlit changes;
- no recognizer, replacement, export, filename, MIME, Scrub Key, reinsert or audit semantic changes;
- the full bound placeholder remains the exported value; display compaction is not exercised as storage grammar;
- human review remains authoritative and mandatory;
- no cloud, AI, telemetry, persistence or external document processing is introduced.

## Verification separation

The implementation worker may provide only `RELEASE_CANDIDATE_READY`.

`SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY` must be claimed by `governance_release_assurance`. Before its initial decision, that worker reconstructs the candidate from the requested outcome, authoritative control files, source/diff, this acceptance matrix and raw machine evidence. It must not read the implementation handover or implementation conclusions first.
