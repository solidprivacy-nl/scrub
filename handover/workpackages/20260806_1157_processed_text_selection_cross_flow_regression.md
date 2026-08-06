# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`; independent assurance pending

## Summary

Added synthetic chain-level regression tests for the existing processed-text selection feature. The candidate exercises the real selection inspect/commit path and then proves that the resulting document-bound `manual_selection` row enters the same review-table-authoritative downstream path as other included rows.

This implementation handover is not assurance evidence. The separate assurance worker must record its initial decision before reading it.

## Files added

- `tests/test_processed_text_selection_cross_flow_regression.py`
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_cross_flow_regression.md`
- `handover/workpackages/20260806_1157_processed_text_selection_cross_flow_regression.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- governance/project instruction files as recorded in the paired governance-adoption handover

## Tests

Five focused synthetic regression tests were added for:

1. one selection-created row as the shared authoritative input for processed-text export, replacement CSV, scrub report and bound Scrub Key;
2. bound TXT export and verified TXT reinsert;
3. original-DOCX replacement and verified DOCX reinsert;
4. authoritative `include=false` behavior across export and Scrub Key omission;
5. free custom replacement remaining in document export while verified bound-key validation fails closed.

The tests also assert selection provenance, all-exact occurrence count, document binding, local-only metadata, no AI/cloud processing and exact restoration of the synthetic source text.

## Validation

- Local tests: unavailable in the connector-only implementation session
- Candidate PR: #69, open as draft and not merged
- GitHub Actions: run #2097 green on the pre-closeout candidate, `1165 passed in 9.62s`; final exact-head run pending after administrative closeout
- Hugging Face sync: not applicable; no runtime files changed
- App verification: not applicable; no UI behavior changed
- Independent governance status: pending; implementation deliberately issued no PASS

## Remaining risks

- The final exact-head PR run must remain green after the administrative closeout commits.
- The regression proves current supported TXT/DOCX surfaces; it does not expand known DOCX reinsert limitations such as split placeholders, comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata.
- No production behavior was changed; a test failure must return to implementation rather than be repaired by the assurance worker.

## Next recommended step

- Confirm the final exact-head PR test run.
- A separate `governance_release_assurance` worker/session claims `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY`, independently reconstructs the tests and candidate diff, and records `PASS`, `FAIL` or `INDETERMINATE` before opening this handover.
- Do not start `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT` until both the governance-adoption and cross-flow verification packages pass.
