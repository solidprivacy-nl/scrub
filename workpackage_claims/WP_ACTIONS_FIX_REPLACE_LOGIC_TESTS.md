# Workpackage claim — WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS

Status: completed
Repository: solidprivacy-nl/scrub
Workpackage: WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — Repair failing replacement logic and DOCX triage tests
Started: 2026-06-13
Completed: 2026-06-13

## Scope completed

Fixed the two reported pytest failures:

- `tests/test_docx_residual_placeholder_comments_risk.py::test_triage_document_records_high_risk_and_no_fix_boundary`
- `tests/test_replace_logic_ui_contract.py::test_contract_tests_use_synthetic_values_only`

## Commits

- `880bf8d` — DOCX triage wording repair.
- `30ba196` — self-referential synthetic-only contract test repair.
- `3fe5fa1` — WORKPACKAGES update.
- `c86d016` — CHANGELOG update.
- `4da23bc` — handover file.

## Handover

`handover/workpackages/20260613_0015_actions_fix_replace_logic_tests.md`

## Validation

- Local pytest execution via the ChatGPT GitHub connector was not available.
- Expected targeted check: `pytest tests/test_docx_residual_placeholder_comments_risk.py tests/test_replace_logic_ui_contract.py`.
- GitHub Actions: pending/unknown after final commit.
- Hugging Face sync: not applicable for this non-runtime fix.
- App verification: not applicable because no UI behavior changed.

## Boundaries preserved

No UI, startup, export, Scrub Key, reinsert, dependency, cloud-processing or real-data changes.

## Next recommended step

Verify GitHub Actions. If green, continue with WP42D-ROLLBACK Hugging Face sync/app-start verification.
