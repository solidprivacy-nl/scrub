# Changelog — SolidPrivacy Scrub

This changelog records meaningful product, architecture, workflow and recognizer changes for the Scrub legal document scrubber.

Conventions:

- Keep this file explicit and human-readable.
- Group changes by project phase / version.
- Record what changed, why it changed, and what is intentionally not changed.
- Do not use this as a substitute for tests; every recognizer hardening step should also add or update regression tests.

---

## Current development rule

From v10 onward, recognizer work follows this order:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer / scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face.

For UI/UX-only work, prefer pure helper modules and tests before touching Streamlit UI flow.

---

## WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; GitHub Actions and Hugging Face sync pending coordinator/app-independent verification.

Purpose:

- Prepare document-level reinsert without changing UI first.
- Add pure helper/test foundation for TXT and DOCX reinsert.
- Reuse the existing deterministic Scrub Key reinsert logic.
- Keep PDF, UI, AI calls and cloud processing out of scope.

Files added or changed:

- Added `scrub_key_document_reinsert.py`.
- Added `tests/test_scrub_key_document_reinsert.py`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation.md`.

Main helper behavior:

- Added `reinsert_text_document(text, scrub_key)` for plain text document-level reinsert.
- Added `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")` for TXT bytes input/output.
- Added `reinsert_docx_bytes(content, scrub_key)` for DOCX main-document text-node reinsert.
- Reuses `reinsert_from_scrub_key(...)` from `scrub_key_reinsert.py`.
- Returns restored content and audit summary.
- Reports `document_type`, `replacement_count`, `item_count`, `active_item_count`, `excluded_item_count`, `placeholders_not_found`, `unknown_placeholders`, `duplicate_placeholders`, `validation_issues`, `local_only`, `ai_processing` and `cloud_processing`.
- Remains deterministic and side-effect free.
- Does not mutate the input Scrub Key.

TXT behavior:

- Accepts plain text through `reinsert_text_document(...)`.
- Accepts bytes through `reinsert_txt_bytes(...)`.
- Decodes bytes strictly with UTF-8 by default.
- Returns restored text and restored bytes.
- Reports decode/type issues as validation issues instead of silently changing input.

DOCX behavior and limitations:

- Uses Python standard library only: `zipfile`, `BytesIO` and `xml.etree.ElementTree`.
- Processes only `word/document.xml` text nodes.
- Supports normal body paragraphs and tables in `word/document.xml`.
- Returns restored DOCX bytes.
- Leaves the original uploaded bytes untouched.
- Does not restore placeholders split across multiple Word runs/text nodes.
- Does not process headers, footers, comments, tracked changes or metadata.
- Does not claim perfect formatting preservation.
- Records limitations in returned `limitations` and `unsupported_parts` fields.

Tests added:

- TXT text reinsert with one placeholder.
- TXT bytes reinsert with multiple placeholders.
- TXT unknown placeholder remains unchanged and is reported.
- Invalid Scrub Key returns validation issues.
- DOCX reinsert with one placeholder in a paragraph.
- DOCX reinsert with multiple placeholders.
- DOCX table text replacement in `word/document.xml`.
- DOCX output remains a valid DOCX package.
- DOCX paragraph text is restored correctly.
- DOCX helper returns audit summary.
- DOCX unsupported areas / limitations are documented.
- Helper does not mutate input Scrub Key.
- No AI/cloud behavior.
- Synthetic values only.

Testing and validation:

- Local reconstructed targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py` → 12 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py` → 14 passed.
- Local reconstructed full available subset:
  - `PYTHONPATH=. pytest -q` → 32 passed.
- Repository clone via container was not possible because outbound GitHub DNS was unavailable, so validation was performed on reconstructed files from GitHub-fetched content plus the new helper/tests.

Intentionally not changed:

- No UI files changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No PDF reinsert implementation added.
- No AI calls added.
- No cloud processing added.
- No automatic app document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior changed.
- No Scrub Key JSON export/import behavior changed.
- No secrets, tokens or real personal data stored.

Outcome:

- WP10 helper/test foundation is implemented.
- Next recommended workpackage is WP11 — v13.5 Two-mode reinsert UI planning.

---

## WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Purpose:

- Decide what Scrub should do next for AI-output and document-level reinsert before implementation starts.
- Challenge whether pasted-text reinsert is enough.
- Challenge whether direct DOCX/PDF reinsert should be added immediately.
- Challenge whether anonymization and de-anonymization should remain in one combined long screen.
- Recommend a model architecture, product direction, tactical sequence, operational safety position and visual/UX direction.

Files added or changed:

- Added `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`.

Main recommendation:

- Keep pasted-text reinsert as a safe baseline and fallback, but do not treat it as the final legal-document workflow.
- Move toward a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Add document-level reinsert in phases.
- Prioritize TXT and DOCX before PDF.
- Keep PDF as investigation/reliability-review work only for now.
- Keep all reinsert behavior local-only, deterministic and helper-first.
- Do not add AI calls.
- Do not add cloud processing.

Outcome:

- WP9 is complete.
- Product direction for reinsert is documented before implementation.

---

## v13.3 — Deterministic reinsert UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Administratively close the v13.3 deterministic reinsert UI after technical verification and app verification.
- Record that local deterministic reinsert works in the Hugging Face app.
- Preserve the boundary that no AI calls, cloud processing, automatic document rehydration, DOCX/PDF reinsert or existing scrubbed export/download behavior changes were added.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI implementation

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Add the deterministic local reinsert UI described in `REINSERT_UI_SPEC.md`.
- Let the user paste scrubbed or AI-generated text and locally restore mapped placeholders using a validated Scrub Key.
- Show restored text, an audit summary and a `.txt` download for restored text.
- Keep the step local and deterministic, with no AI calls and no cloud processing.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Purpose:

- Plan deterministic local reinsert UI before changing Streamlit UI code.
- Define where the UI should appear, what labels it should use, what state it should rely on, and which warnings and audit fields it must show.
- Keep AI-output behavior separate unless explicitly approved.

Outcome:

- v13.3 deterministic reinsert UI was planned and then implemented and app-verified.

---

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Purpose:

- Administratively reconcile the v13.3 deterministic reinsert helper after coordinator-provided verification evidence.
- Confirm that the helper remains pure, local and deterministic.
- Preserve the boundary that no UI, AI-output flow, cloud processing or export/download behavior change was added.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Purpose:

- Administratively close the v13.2 Scrub Key import/reload UI after app verification.
- Record that the implemented import/reload flow works in the Hugging Face app.
- Preserve the boundary that this phase is import/reload only and does not add AI-output reinsert.

Outcome:

- v13.2 Scrub Key import/reload UI is completed, app-verified and closed.

---

## Earlier completed work

- v13.2 Scrub Key import/reload UI integration.
- v13.2 Scrub Key import/reload helper and tests.
- v13.1 Scrub Key JSON export UI closeout.
- v12.6 Export sanity checks closeout.
- v13.0 Scrub Key specification and pure model.
- v12.5 Final review summary.
- v12.4 Review guidance text.
- Project governance setup.
- v12.3 Review table simplification.
- v12.2 Review focus filters.
- v12.1 Review table status model.
- v11.2 Dutch recognizer integration tests.
- v11.1 Legal reference recognizer hardening.
- v10 Regression test layer.
- v9.1 UI polish and baseline stabilization.
- v9 Dutch Legal UI Layer.

---

## Planned later phase — v13 and beyond

Possible directions:

- Two-mode UI planning for `Anonimiseren` and `Originele waarden terugzetten`.
- TXT/DOCX reinsert UI integration after helper verification.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
