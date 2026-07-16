# Handover — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

## Status

Completed / ready for PR verification.

## Files added

- `test_cases/mvp_phase6/validation_manifest.json`
- `mvp_phase6_validation_manifest.py`
- `mvp_phase6_detection_matrix.py`
- `mvp_phase6_workflow_core.py`
- `mvp_phase6_document_cases.py`
- `mvp_phase6_validation_report.py`
- `scripts/run_mvp_phase6_validation_matrix.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `output/validation/mvp_phase6_synthetic_validation_report.json`
- `handover/workpackages/20260717_2020_mvp_e2e_synthetic_validation_matrix.md`

## Files changed

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_e2e_synthetic_validation_matrix.md`

## Tests

- New focused Phase 6 matrix tests.
- Existing Dutch legal recall-gap tests.
- Existing Scrub Key model, reinsert and document-reinsert tests.
- Existing DOCX hygiene and document-tool guardrails selected by CI.
- Python compilation and `git diff --check`.

## Validation status

- Synthetic cases: 3.
- Failing cases: 0.
- Evidence gaps/known limitations: 3.
- Categories: ['false_negative_or_detection_gap', 'known_docx_reinsert_limitation', 'known_pdf_reinsert_limitation'].
- Report schema is machine-readable and deterministic.
- Human review remains required.
- Production readiness is explicitly false.

## GitHub Actions status

Pending final PR validation.

## Hugging Face sync status

Not functionally relevant; no app code or UI changed.

## App verification status

Not applicable.

## Remaining risks

- Detection evidence is a bounded synthetic baseline, not a production recall/precision benchmark.
- DOCX header/footer reinsert remains outside the current document-reinsert helper scope.
- PDF reinsert remains restored TXT only; no restored PDF and no OCR.
- Evidence gaps require classification before any implementation package is opened.

## Next recommended step

Start `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE` using `output/validation/mvp_phase6_synthetic_validation_report.json` as the source evidence.
