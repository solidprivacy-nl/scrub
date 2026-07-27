# Workpackage claim — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; full suite passed; final PR validation pending

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-27 16:05 Europe/Amsterdam

Branch: scrub-mvp-reinsert-auto-flow-simplification

Dependencies:
- SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING — merged, Actions/sync verified and live DOCX app verification passed.
- User evidence confirms body, table, header and footer restoration in the downloaded synthetic DOCX.

Evidence / problem:
- The current reinsert UI starts with the Scrub Key instead of the document the user wants to restore.
- Uploading the source document still requires a separate confidentiality checkbox and execution button.
- Uploading the Scrub Key still requires a separate acknowledgement checkbox and validation button.
- These repeated gates make an already explicit two-file operation feel unfinished and form-like.

Scope:
- Reorder the primary reinsert flow to source document/text first, Scrub Key second, result/download third.
- Automatically recognize the uploaded source type.
- Automatically parse and validate an uploaded or pasted Scrub Key.
- Automatically run local deterministic reinsert once one valid source and one valid Scrub Key are present.
- Remove the separate pre-processing acknowledgements and action buttons for source and Scrub Key.
- Preserve one final restored-output confidentiality acknowledgement directly at the download boundary.
- Preserve warnings, validation errors, audit/report details and all current output filenames/MIME types.
- Preserve TXT, DOCX, PDF-to-TXT and pasted-text support.

Boundaries:
- No Scrub Key schema, mapping or lifecycle change.
- No document-processing or replacement-semantics change.
- No recognizer, threshold, export or audit-semantics change.
- No cloud, AI or OCR processing.
- PDF remains restored TXT only.
- Unsupported DOCX parts remain explicitly documented.
- Human review and confidential-output warnings remain required.

Validation note:
- Full repository suite passed: 797 tests before governance finalisation.
- Governance finalisation completed.
- Governance-scoped regression fixed; standard suite passed on the finalised branch.
- Temporary diagnostic and finalizer workflows removed from `main`.
- Clean final standard PR validation triggered at 2026-07-27 17:25 Europe/Amsterdam.

Implementation result:
- Completed at: 2026-07-27 17:06 Europe/Amsterdam.
- Document/text is step 1; Scrub Key is step 2; download is step 3.
- Source type recognition, key validation and local deterministic reinsert are automatic.
- Redundant source/key checkboxes and action buttons are removed.
- One final confidentiality acknowledgement remains before download.
- Full repository suite before governance finalisation: 797 passed.
- Evidence: `output/validation/mvp_reinsert_auto_flow_validation.json`.
- Handover: `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`.

Next step:
- Verify clean final standard Actions, merge, verify Hugging Face sync and request live app verification.
