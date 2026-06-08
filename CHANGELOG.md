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

## WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Purpose:

- Verify and formally close, or pending-close, WP10.
- Check GitHub Actions and Hugging Face sync visibility for implementation commit `eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee`.
- Update control files without changing code.

Files added or changed:

- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation_closeout.md`.

Verification result:

- Commit metadata was visible for `eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee`.
- GitHub combined commit status returned an empty status list.
- GitHub workflow-runs query for the commit returned no visible workflow runs.
- GitHub Actions: not visible through connector.
- Hugging Face sync: not visible through connector.
- App verification: not applicable; WP10 was helper/test-only and added no UI behavior.

Recorded existing validation:

- Local reconstructed targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py` → 12 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py` → 14 passed.
- Available reconstructed subset:
  - `PYTHONPATH=. pytest -q` → 32 passed.
- Important nuance preserved:
  - Container clone from GitHub failed because of DNS/outbound GitHub issues.
  - Tests were run on reconstructed files from GitHub-fetched content plus the new helper/tests.

Closeout decision:

- WP10 remains `implemented; awaiting coordinator verification of Actions/sync`.
- WP10 was not marked as formally closed because Actions/sync were not visible through the connector.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI files changed.
- No edit to `scrub_key_document_reinsert.py`.
- No edit to `tests/test_scrub_key_document_reinsert.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior changed.
- No Scrub Key export/import behavior changed.
- No secrets, tokens or real personal data stored.

Outcome:

- WP10B closeout is complete.
- Coordinator should verify Actions/sync externally before marking WP10 formally closed.
- Next recommended workpackage remains WP11 — v13.5 Two-mode reinsert UI planning.

---

## WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

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
- WP10 awaits coordinator verification of GitHub Actions and Hugging Face sync.
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

Outcome:

- WP9 is complete.
- Product direction for reinsert is documented before implementation.

---

## v13.3 — Deterministic reinsert UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI implementation

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Outcome:

- v13.3 deterministic reinsert UI was planned and then implemented and app-verified.

---

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

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

- Coordinator verification of WP10 Actions/sync.
- Two-mode UI planning for `Anonimiseren` and `Originele waarden terugzetten`.
- TXT/DOCX reinsert UI integration after helper verification.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
