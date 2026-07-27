# Handover — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

## Status

Completed and app-verified.

## Files added

- `mvp_document_fidelity_report.py`
- `scripts/run_mvp_document_hygiene_fidelity_report.py`
- `tests/test_mvp_document_hygiene_fidelity_hardening.py`
- `tests/test_mvp_document_fidelity_report.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json`
- `output/validation/mvp_document_fidelity_pr_validation.json`
- `output/validation/mvp_document_fidelity_pr_validation.log`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`

## Files changed

- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `mvp_phase6_document_cases.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`

## Tests

- Existing TXT/DOCX Scrub Key document-reinsert suite.
- Body, table, header and footer DOCX tests.
- OOXML preservation and malformed-part fail-safe tests.
- Phase 6 synthetic matrix tests.
- Capability-copy contract tests.
- Fidelity report and document hygiene tests.
- Python compilation and `git diff --check`.
- Focused final suite: 54 passed.

## Validation status

- DOCX header/footer finding resolved: true.
- Resolved findings: 1.
- Remaining findings: 1.
- PDF TXT-only/no-OCR boundary preserved: true.
- Local-only deterministic processing retained.
- Human review remains required.
- Production readiness remains false.
- Clean implementation PR #37 merged.
- Historical PR #33 closed as superseded.

## GitHub Actions status

Passed before and after merge.

## Hugging Face sync status

Passed. The deployed Hugging Face revision matches the PR #37 merge revision and the runtime is RUNNING on cpu-basic.

Sanitized evidence is stored on branch `evidence/pr37-postmerge-verification` in `output/validation/pr37_postmerge_verification.json`.

## App verification status

Passed on 2026-07-27 with the supplied synthetic DOCX and Scrub Key fixture.

The downloaded restored DOCX confirms:

- body: `Mila Voorbeeld`;
- table: `SYN-2026-0042`;
- header: `Stichting Proefdocument`;
- footer: `testpersoon@example.invalid`.

The verification exposed a separate interface-clarity issue: the reinsert flow starts with the Scrub Key and requires redundant source/key acknowledgements and action buttons after upload. That evidence is routed to `SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION`.

## Remaining risks

- Comments, tracked-change-only parts, footnotes/endnotes, text boxes and metadata remain unsupported by reinsert.
- Placeholders split across Word text nodes remain unsupported.
- PDF remains restored TXT only; no OCR or restored PDF output.
- DOCX hygiene audit remains report-only and does not guarantee a clean document.
- The reinsert workflow requires a narrow evidence-driven interface simplification before continuing the general Scrub Key roundtrip line.

## Next recommended step

Complete and app-verify `SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION`, then continue with `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.
