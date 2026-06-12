# Handover — WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS

Repository: `solidprivacy-nl/scrub`

Workpackage title: `WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — Repair failing replacement logic and DOCX triage tests`

Status: implemented minimal pytest repair; awaiting GitHub Actions verification.

## Summary

Fixed the two failing pytest assertions reported by the coordinator/user:

1. `tests/test_docx_residual_placeholder_comments_risk.py::test_triage_document_records_high_risk_and_no_fix_boundary`
2. `tests/test_replace_logic_ui_contract.py::test_contract_tests_use_synthetic_values_only`

The first failure was a wording mismatch: the WP36A triage document said `implement a DOCX cleaner` under an explicit non-change list, but the regression test required an explicit `does not implement a DOCX cleaner` or `no docx cleaner` phrase.

The second failure was self-referential: the synthetic-only contract test scanned its own test source and contained the forbidden example strings literally inside the assert statements.

## Files added

- `workpackage_claims/WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS.md`
- `handover/workpackages/20260613_0015_actions_fix_replace_logic_tests.md`

## Files changed

- `DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md`
- `tests/test_replace_logic_ui_contract.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS.md`

## Tests added/updated

- Updated `tests/test_replace_logic_ui_contract.py` so forbidden example values are constructed from safe fragments before checking the combined test/plan text.
- No product tests were added.

## Tests/checks run

The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.

Expected targeted command:

```text
pytest tests/test_docx_residual_placeholder_comments_risk.py tests/test_replace_logic_ui_contract.py
```

Expected broader command after targeted pass:

```text
pytest
```

## Validation status

- Static review completed against the two reported failure messages.
- The DOCX triage document now explicitly includes `does not implement a DOCX cleaner` and `does not implement a fix` in the MVP policy boundary.
- The replacement UI contract test no longer embeds the forbidden real-data examples as contiguous strings while still checking that those examples are absent from the test/plan text.
- Full validation depends on the next GitHub Actions run.

## GitHub Actions status

Unknown at handover time. A new Actions run is required after the fix commits.

## Hugging Face sync status

Not checked. This package does not change app runtime, UI startup, dependencies, Streamlit patch order, export/download behavior, Scrub Key behavior or reinsert behavior.

## App verification status

Not applicable for this fix package. No UI behavior changed.

## Intentionally not changed

- No UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No review table behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No helper runtime behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

## Remaining risks

- GitHub Actions still needs to confirm the full test suite is green.
- WP42D-ROLLBACK still needs Hugging Face sync/app verification showing the normal table-first app starts again.
- Replacement decision UI implementation remains blocked until coordinator approval and green contract tests.

## Next recommended step

1. Verify GitHub Actions after these commits.
2. If Actions are green, verify Hugging Face sync/app startup for WP42D-ROLLBACK.
3. Do not start `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` unless the coordinator explicitly approves UI work.
