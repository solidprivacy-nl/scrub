## 2026-07-27 19:18 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: completed; targeted validation passed; PR verification pending.

Purpose:
- Determine the smallest safe cross-format mitigation for the critical document/Scrub-Key binding gap before changing schema, placeholders, export or reinsert behavior.

Files added:
- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`
- `tests/test_mvp_scrub_key_document_binding_gap_triage.py`
- `tests/test_mvp_scrub_key_document_binding_gap_triage_validation.py`
- `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Triage result:
- Primary MVP threat: accidental wrong-document/key pairing.
- Secondary MVP threat: accidental key corruption.
- Deferred threat: malicious tampering requiring protected signing-key infrastructure.
- Recommended primary control: document-specific non-sensitive binding ID in all placeholders and the key.
- Recommended complementary control: canonical SHA-256 mapping digest.
- Explicitly not sufficient: document labels, filenames, content hashes, placeholder-list hashes or metadata-only binding.
- Legacy v1.0 keys require explicit unbound status and warning; they must not be silently treated as bound.
- Bound-key mismatch, mixed IDs and digest mismatch must fail closed with zero replacements.
- Human review remains required; production readiness remains false.

Intentionally not changed:
- product code or UI;
- Scrub Key schema/version or serialization;
- placeholder generation or grammar;
- export/download or reinsert semantics;
- document processing;
- cloud, AI, OCR or secret storage.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` before implementation.

---

## 2026-07-27 18:55 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Status: completed; deterministic validation passed; PR verification pending.

Purpose:
- Validate Scrub Key import/reinsert and placeholder roundtrip behavior against adversarial synthetic mutations.
- Record evidence before authorizing any schema, export or reinsert changes.

Files added:
- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `mvp_scrub_key_roundtrip_validation.py`
- `scripts/run_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_report_contract.py`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_roundtrip_validation.md`

Validation result:
- 15 synthetic cases; 0 failed cases.
- 1 critical finding: no reliable document/key binding when a wrong valid key reuses the same placeholder namespace.
- 1 medium finding: malformed placeholder mutations outside the grammar are signalled indirectly.
- Existing duplicate, incomplete, invalid, unknown and translated cases fail closed or remain visibly auditable as expected.
- Local-only: true; external AI: false; cloud processing: false.
- Production ready: false; human review required: true.

Intentionally not changed:
- product code or UI;
- Scrub Key schema, mappings, export, storage or lifecycle;
- placeholder grammar or automatic repair;
- reinsert helper semantics;
- filenames, MIME types or audit fields;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE` before implementing a fix.

---

## 2026-07-27 18:28 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:
- Record successful live verification of the document-first automatic reinsert workflow.
- Close the evidence-driven UI blocker before continuing Scrub Key roundtrip validation.

Validation result:
- PR #38 merge commit: `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678: passed.
- Full repository suite before merge: 797 passed.
- Hugging Face deployment: confirmed by live testing of the merged three-step workflow.
- App verification: passed; coordinator reported `getest en werkend`.

Verified product boundaries:
- Document/text remains step 1, Scrub Key step 2 and restored download step 3.
- Automatic source recognition, key validation and local deterministic reinsert work as intended.
- One final confidential-output acknowledgement remains at download.
- No Scrub Key schema, helper semantics, export filenames/MIME types, cloud, AI, OCR or restored-PDF behavior changed.
- Human review remains required; no production-readiness claim is made.

Files added:
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`
- `handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

## 2026-07-27 — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; full suite passed; final PR validation pending.

Purpose:

- Remove redundant source- and Scrub-Key confirmation steps from the local reinsert workflow after live Phase 6 evidence showed that uploaded inputs looked complete while hidden action gates remained.
- Present the workflow in the user’s natural order: source document/text, corresponding Scrub Key, restored result.
- Preserve a clear confidentiality decision at the final restored-output download boundary.

Files added:

- `reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`
- `output/validation/mvp_reinsert_auto_flow_validation.json`

Files changed:

- `reinsert_mode_ui.py`
- `tests/test_reinsert_interface_simplification_ui.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `ROADMAP.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`

Implementation result:

- Step 1 is now the source document or pasted text.
- One uploader recognises TXT, DOCX and text-based PDF by extension.
- Step 2 automatically parses and validates the uploaded or pasted Scrub Key.
- Local deterministic reinsert runs automatically once one valid source and one valid key are present.
- Separate source/key acknowledgement checkboxes and execution buttons were removed.
- One final confidentiality acknowledgement remains directly before restored-output download.
- Existing output filenames, MIME types, reinsert helpers, audit fields and explicit DOCX/PDF boundaries are preserved.

Validation:

- Full repository suite: 797 passed.
- Helper dispatch, deterministic request signatures and input precedence are covered.
- Source-level UI contracts verify document-first order, automatic key validation, automatic local reinsert and removal of redundant gates.
- Prior DOCX live verification passed for body, table, header and footer restoration.
- Final GitHub Actions, merge, Hugging Face sync and live app verification remain pending.

Intentionally not changed:

- Scrub Key schema, mappings, lifecycle or storage;
- document replacement or reinsert helper semantics;
- recognizers or thresholds;
- export filenames, MIME types or audit semantics;
- cloud, AI or OCR processing;
- restored-PDF support;
- unsupported DOCX-part boundaries;
- the requirement for human review and a final confidential-output warning.

Next recommended step:

- Complete final PR validation, merge and sync, then live-verify the three-step automatic flow.
- Continue with `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` after app verification.

---

## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Purpose:

- Resolve the reproducible DOCX header/footer reinsert fidelity gap from the Phase 6 matrix.
- Preserve DOCX hygiene visibility and explicit unsupported-part boundaries.
- Keep the PDF restored-TXT-only/no-OCR boundary unchanged.

Files added:

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

Files changed:

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

Implementation result:

- DOCX body paragraphs and tables remain supported.
- `word/header*.xml` and `word/footer*.xml` text nodes are restored deterministically.
- The DOCX reinsert capability copy matches the supported body/table/header/footer scope.
- The synthetic header/footer residual-placeholder finding is resolved: `true`.
- Resolved findings: 1.
- Remaining findings: 1.
- The remaining finding is the explicit PDF restored-TXT-only/no-OCR product boundary.

Intentionally not changed:

- recognizers, thresholds or replacement semantics;
- Scrub Key schema or lifecycle;
- DOCX comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata;
- split-placeholder support across Word text nodes;
- export filenames or MIME types;
- restored PDF or OCR support;
- Streamlit controls/flow, runtime or dependencies; only capability copy was aligned.

Next recommended step:

- After Actions, sync and app verification, start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

## 2026-07-17 — Hugging Face Space runtime incident recovery and sync-churn guard

Status: completed and app-verified.

Purpose:

- Restore the Hugging Face Space after it entered an error/rebuild state.
- Diagnose the incident without exposing secrets or changing product behavior.
- Prevent clearly non-runtime-only commits from repeatedly rebuilding the live Space.

Result:

- Sanitized runtime evidence observed the Space first at `BUILDING` and subsequently at `RUNNING`.
- Streamlit started on port 7860 and the Flair model loaded.
- The coordinator confirmed that the application opens again.
- PR #35 added a conservative deployment `paths-ignore` guard while preserving runtime-relevant deployments and manual dispatch.
- Temporary incident recovery/probe workflows and triggers were removed after verification.

Intentionally not changed:

- product code or UI;
- recognizers, thresholds or replacement semantics;
- export, Scrub Key or reinsert semantics;
- dependencies, Dockerfile, hardware or Hugging Face configuration;
- privacy and human-review controls.

Next recommended step:

- Resume PR #33 and the Phase 6 document-fidelity sequence.

---

## 2026-07-17 — SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Status: completed / ready for PR verification.

Purpose:

- Classify every evidence gap from the first Phase 6 synthetic validation report.
- Decide whether the evidence justifies recognizer or threshold changes.
- Route document-fidelity and product-boundary findings to the correct next package.

Files added:

- `MVP_PHASE6_FALSE_NEGATIVE_GAP_TRIAGE.md`
- `output/validation/mvp_phase6_false_negative_gap_triage.json`
- `tests/test_mvp_phase6_false_negative_gap_triage.py`
- `handover/workpackages/20260717_2208_mvp_false_negative_gap_triage.md`

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_false_negative_gap_triage.md`

Triage result:

- Input evidence gaps: 2.
- Reproducible detection false negatives: 0.
- Misclassifications: 0.
- Legal-role over-masking findings: 0.
- Recognizer fix required: `false`.
- Next package: `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

Decision:

- The DOCX finding is a header/footer reinsert and fidelity-scope issue, not a detection failure.
- The PDF finding is the approved restored-TXT-only/no-OCR product boundary, not a detection failure.
- No recognizer implementation package is opened from this evidence.

Intentionally not changed:

- product recognizers or thresholds;
- replacement semantics;
- document processing or reinsert behavior;
- export, Scrub Key or audit semantics;
- UI, runtime or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

---

## 2026-07-17 — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: completed / ready for PR verification.

Purpose:

- Establish a repeatable synthetic evidence baseline for the supported MVP workflow.
- Exercise TXT, DOCX and text-based PDF paths across import, review-row replacement, manual addition, Scrub Key creation/validation, deterministic reinsert, export representations and audit evidence.
- Record known limitations and reproducible gaps without weakening tests or making production-readiness claims.

Files added:

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

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_e2e_synthetic_validation_matrix.md`

Validation result:

- Synthetic cases: 3.
- Failing cases: 0.
- Evidence gaps/known limitations: 2.
- Gap categories: known_docx_reinsert_limitation, known_pdf_reinsert_limitation.
- Human review required: `true`.
- Production ready: `false`.
- Local-only validation: `true`.
- External AI/cloud/OCR processing: none.

Methodology correction:

- Standard deterministic Presidio email recognition is included alongside the Dutch recognizer pack, preventing a standard e-mail value from being misclassified as a Dutch-pack false negative.

Intentionally not changed:

- Streamlit UI or review controls;
- recognizers or detection thresholds in product code;
- replacement semantics;
- export payload, filename or MIME semantics;
- Scrub Key schema or lifecycle behavior;
- reinsert semantics;
- document-processing implementation;
- runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE` and classify the report evidence before implementing any fix.

---

## 2026-07-17 — SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT

Status: completed / ready for PR verification.

Purpose:

- Realign the central roadmap after completion and live verification of the MVP UI simplification line.
- Make Phase 6 end-to-end workflow validation and trust hardening the active development line.
- Define an ordered evidence-driven workpackage queue before pilot or packaging work resumes.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_phase6_roadmap_realignment.md`

Files added:

- `MVP_PHASE6_EXECUTION_PLAN.md`
- `handover/workpackages/20260717_2012_mvp_phase6_roadmap_realignment.md`

Main changes:

- The verified UI baseline is no longer the active development focus.
- Phase 6 starts with a synthetic end-to-end validation matrix.
- False-negative, document-hygiene, Scrub Key/roundtrip and audit work must be driven by reproducible evidence.
- Phase 7 pilots and local packaging remain gated.

Validation status:

- Documentation-only package.
- GitHub Actions pending after PR.
- Hugging Face functional sync not applicable.
- App verification not applicable.

Intentionally not changed:

- product code or tests;
- UI behavior;
- recognizers or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX` after this realignment is merged.

---

## 2026-07-16 — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:

- Record live Hugging Face app verification after PR #28 merged.
- Close the manual correction panel density simplification line.
- Confirm the compact layout preserves the existing manual correction workflow.

Verification evidence:

- Coordinator live app screenshot reviewed at 2026-07-16 23:43 Europe/Amsterdam.
- `Gemiste waarde toevoegen` remains collapsed by default and opens without a duplicate internal heading.
- The value, type and replacement controls appear in one compact row.
- The full-width `Toevoegen aan vervangtabel` action remains visible.
- Synthetic value `lantaarnbloem` was added successfully.
- The replacement table shows `lantaarnbloem` with `[WAARDE_HANDMATIG_01]` and status `Handmatig toegevoegd`.
- No Script execution error is visible.
- The live screenshot confirms GitHub-to-Hugging-Face deployment of the merged UI.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Files added:

- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260716_2343_manual_correction_panel_density_app_verify_closeout.md`

Intentionally not changed:

- product code or tests;
- recognizer or replacement semantics;
- validation or session-state behavior;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, startup/runtime or dependencies.

Next recommended step:

- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

---

## 2026-07-16 — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; local validation passed.

Purpose:

- Make the existing `Gemiste waarde toevoegen` panel materially shorter and less form-like.
- Remove the duplicate internal heading and group value, type and replacement controls in one compact row.
- Preserve the existing validation, session-state and replacement-table workflow.

Files changed:

- `presidio_streamlit.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`

Files added:

- `tests/test_manual_correction_panel_density_implementation.py`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Validation status:

- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- Live app verification required because visible UI behavior changed.

Intentionally not changed:

- validation rules or duplicate detection;
- placeholder generation or entity types;
- replacement-row structure or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or warning behavior;
- reinsert behavior;
- recognizers, thresholds, document processing, runtime/startup or dependencies.

Next recommended step:

- Verify PR Actions, merge when green, verify Hugging Face sync and request live app verification.

---

## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:

- Record live app verification for `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION`.
- Close the Review/Export vertical-density implementation line after PR #26 merge and live Hugging Face verification.
- Add concise closeout notes for the related plan and contract-test packages that were previously missing from `CHANGELOG.md`.

Verification evidence:

- Coordinator live Hugging Face screenshot reviewed.
- The app starts without Script execution error.
- The input section remains coherent.
- `2. Controleer resultaat` remains visible.
- Basiscontrole / Expertcontrole remain visible.
- `Markeringen tonen` and side-by-side review remain visible.
- `Gemiste waarde toevoegen` and the vervangtabel remain accessible.
- `3. Exporteer resultaat` remains visible.
- TXT/DOCX/PDF downloads are visible in a compact row.
- Scrub Key, audit/technical files and DOCX hygiene audit remain separate and accessible.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`
- `handover/workpackages/20260705_2242_review_export_vertical_density_app_verify_closeout.md`

Intentionally not changed:

- product code;
- tests;
- recognizer logic;
- replacement logic;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON;
- reinsert behavior;
- startup/runtime behavior.

Related package closeout:

- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN` — completed and merged; planning-only.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS` — completed and merged; source-level guardrails only.

Next recommended step:

- Decide whether the current MVP UI is good enough for this pass, or start a new separately approved small UI package.

---

## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Reduce vertical density in the Review and Export areas after plan and contract-test packages were merged.
- Compress repeated Review helper copy while keeping side-by-side review, marker toggle, manual missed-value entry and replacement table accessible.
- Put the three primary document downloads in a compact three-column layout.
- Keep Scrub Key, audit/technical files and DOCX hygiene audit separate and accessible.

Files changed:

- `presidio_streamlit.py`
- `side_by_side_review_panel_ui.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`

Validation status:

- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after sync because visible UI behavior changed.

Intentionally not changed:

- recognizer logic;
- replacement logic;
- review table semantics;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- DOCX/PDF parsing;
- startup/runtime behavior;
- dependencies;
- benchmark or recall logic.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, then request live app verification.

---

## 2026-07-05 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Resume the duplicate input surface implementation after the connector-only worker was blocked.
- Keep one visible `1. Voeg document of tekst toe` step and group upload, synthetic example selection and pasted/extracted text into one input surface.
- Preserve TXT/DOCX/PDF upload support, synthetic legal examples, pasted/extracted text handling and input precedence.
- Preserve review, export/download, Scrub Key, reinsert, audit and DOCX hygiene behavior.

Files changed:

- `presidio_streamlit.py`
- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_0113_duplicate_input_surface_implementation.md`

Validation status:

- Local validation passed:
  - `python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py`
  - related UI/export guardrail tests
  - `git diff --check`
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI grouping changed.

Intentionally not changed:

- document parsing behavior;
- upload backend;
- recognizer logic;
- replacement logic;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, and request live app verification.

---

## 2026-07-04 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Status: completed / PR validation pending.

Purpose:

- Lock the single-input-surface contract before the duplicate input implementation touches `presidio_streamlit.py`.
- Preserve existing TXT/DOCX/PDF upload support, synthetic legal example support, pasted/extracted text handling and input precedence.
- Preserve review, replacement table, Scrub Key, export/download, audit and DOCX hygiene surfaces.
- Block duplicate-input runtime/startup patching and prohibited scope expansion.

Files added:

- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_contract_tests.md`
- `handover/workpackages/20260704_2318_duplicate_input_surface_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because this package changes no UI behavior.

Intentionally not changed:

- product implementation code;
- Streamlit UI behavior;
- document ingestion behavior;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge this contract-test package.
- Then start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow implementation package.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Status: implemented / PR validation pending.

Purpose:

- Make the secondary review controls under `2. Controleer resultaat` calmer and easier to understand.
- Add a clear `Meer controleopties` grouping cue below the side-by-side review without introducing nested Streamlit expanders.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md`

Files added:

- `tests/test_secondary_control_grouping_polish_implementation.py`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md`

Validation status:

- Source-level implementation tests added.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI behavior changed.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge and verify Hugging Face sync.
- Then request coordinator live app verification for the new `Meer controleopties` grouping cue.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Status: implemented planning/contract-tests-only; PR validation pending.

Purpose:

- Prepare the final small UI-polish step for calmer grouping of secondary review controls.
- Avoid nested Streamlit expanders before touching `presidio_streamlit.py`.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files added:

- `SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md`
- `tests/test_secondary_control_grouping_polish_contracts.py`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish.md`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because no UI behavior changed in this planning/contract step.

Intentionally not changed:

- product code;
- Streamlit UI;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Run PR validation for the contract tests.
- If green, merge this plan/contract package.
- Then start `SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION` as the actual narrow UI implementation.

---

## 2026-07-03 — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: completed and app-verified.

Purpose:

- Make the side-by-side review surface calmer and less form-like.
- Keep the source-vs-processed comparison central while pointing users toward the safe download step.
- Preserve review table, manual missed-value entry, serial review, Scrub Key, export/download and audit controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_implementation.md`

Files added:

- `tests/test_review_surface_simplification_implementation.py`
- `handover/workpackages/20260703_0000_review_surface_simplification_implementation.md`

Validation status:

- Source-level implementation tests added.
- Related copy-polish and side-by-side tests updated.
- PR #12 initially failed on stale copy expectations; a narrow test-expectation fix was applied.
- PR #12 Tests passed after the narrow fix.
- PR #12 merged to `main`.
- Main Tests for commit `41cf304` passed.
- GitHub to Hugging Face sync for commit `41cf304` passed.
- App verification passed by coordinator screenshot.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Do not start broader UI/reinsert/export work without a dedicated workpackage.
- Decide whether further secondary-control grouping is desired as a separate small package, or return to recall/benchmark follow-up if product UI is good enough for the current MVP pass.

---

## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

## 2026-06-23 — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

- Fixed DOCX plain-text extraction order for side-by-side preview.
- DOCX body paragraphs and tables are now read in document XML order instead of all paragraphs first and all tables afterwards.
- Added synthetic regression coverage for interleaved paragraph/table order.
- Preserved DOCX export, Scrub Key and reinsert semantics.
- Validation: `python -m pytest tests -x -vv` → 649 passed in 102.51s.

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## 2026-06-23 20:43 Europe/Amsterdam — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Implemented direct-source reinsert interface simplification.
- Added `reinsert_mode_ui.py` with the visible four-step reinsert flow:
  1. Voeg Scrub Key toe
  2. Voeg tekst of document toe
  3. Controleer herstelrapport
  4. Download herstelde output
- Added a minimal direct hook in `presidio_streamlit.py`.
- Added a no-op guard to `fix_streamlit_pdf_text_reinsert.py` so startup does not mutate the direct-source reinsert UI.
- Preserved Scrub Key warnings, acknowledgement gates, restored download filenames, MIME types and local-only/no-AI/no-cloud/no-OCR/no-restored-PDF boundaries.
- Added `tests/test_reinsert_interface_simplification_ui.py`.

Validation so far:
- `tests/test_reinsert_interface_simplification_ui.py`: 8 passed
- reinsert patch tests: 39 passed
- warning/two-mode UI tests: 23 passed


# Changelog — SolidPrivacy Scrub

## SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — Execution interface simplification

Status: completed and verified on `main` via PR #6 (`a34700c`).

Summary:

- Simplified the default Scrub flow toward `1. Voeg document of tekst toe`, `2. Controleer resultaat`, `3. Exporteer resultaat`.
- Edited `presidio_streamlit.py` directly; no startup patch, runtime hook, sitecustomize hook or Dockerfile startup change was added.
- Collapsed secondary controls by default while keeping them available:
  - control-mode explanation;
  - recognition details;
  - review guidance;
  - manual missed-value entry;
  - focus filter / extra control helpers;
  - candidate audit values;
  - replacement table;
  - technical replacement details;
  - step-by-step review;
  - reusable replacements;
  - Scrub Key download;
  - audit/technical downloads.
- Kept side-by-side review visible as the main review surface.
- Kept the replacement table as source of truth and export input.
- Kept primary document downloads visible.

Tests:

- `tests/test_execution_interface_simplification_ui.py` — 6 passed.
- Side-by-side, serial review and replace logic UI tests — 37 passed.
- Export/download contract and implementation tests — 19 passed.
- `git diff --check` — passed.
- Full local test suite — 639 passed.
- PR #6 checks — green.
- Main Tests — green.
- GitHub to Hugging Face sync — green.
- Live app verification — passed by coordinator screenshot on 2026-06-23.

Intentionally not changed:

- export semantics;
- download file contents;
- download filenames;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark thresholds;
- document processing behavior;
- cloud processing;
- local packaging;
- Dockerfile startup behavior;
- runtime mutation behavior;
