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

## WP13B — v13.7 TXT reinsert upload/download UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Administratively close WP13 after technical verification and Hugging Face app verification.
- Record that TXT upload/download reinsert works inside `Originele waarden terugzetten`.
- Confirm that no code, tests, UI behavior, export behavior or Scrub Key behavior was changed in this closeout.

Technical verification evidence:

```text
Tests #164 green — commit e442d28
Sync to Hugging Face Space #178 green — commit e442d28

Tests #165 green — commit ce7721d
Sync to Hugging Face Space #179 green — commit ce7721d

Tests #166 green — commit 6bf359f
Sync to Hugging Face Space #180 green — commit 6bf359f

Tests #167 green — commit 443d6af
Sync to Hugging Face Space #181 green — commit 443d6af
```

Latest WP13 implementation commit:

```text
443d6af99cfac47ed007d0d1cd666d1549e855d5
```

App verification evidence:

- `Originele waarden terugzetten` mode is active.
- `Scrub Key laden` is visible.
- Scrub Key JSON is loaded.
- Pasted-text reinsert remains available.
- `TXT-bestand terugzetten` is visible.
- TXT file upload works.
- `Zet TXT-bestand lokaal terug` works with a valid Scrub Key.
- Result message appears: `37 waarde(n) lokaal teruggezet in het TXT-bestand.`
- `Herstelde TXT-tekst` appears.
- `Download hersteld TXT-bestand (.txt)` is visible.
- `Controleverslag TXT terugzetten` appears.
- Audit shows document type `txt`.
- Audit shows mapping counts, restored value count, not-found placeholders, unknown placeholders and validation issues.
- Audit shows `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Closeout result:

- WP13 is now recorded as completed and app-verified after Actions/sync verification.
- TXT upload/download reinsert is available inside `Originele waarden terugzetten`.
- Pasted-text reinsert remains available as fallback.
- Existing anonymization flow remains under `Anonimiseren`.
- Existing Scrub Key import/export remains available.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior remains unchanged.

Files added or changed in WP13B:

- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0015_v13_7_txt_reinsert_upload_download_ui_app_closeout.md`.

Tests:

- No new tests were added because WP13B is closeout-only.
- Existing validation is based on coordinator evidence:
  - GitHub Actions green;
  - GitHub to Hugging Face sync green;
  - Hugging Face app verification confirmed.

Intentionally not changed:

- No code files were changed in WP13B.
- `fix_streamlit_nested_expanders.py` was not changed in WP13B.
- `presidio_streamlit.py` was not changed.
- `scrub_key_document_reinsert.py` was not changed.
- `scrub_key_reinsert.py` was not changed.
- `scrub_key.py` was not changed.
- `scrub_key_import.py` was not changed.
- No test files were changed in WP13B.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior intentionally changed.
- No Scrub Key JSON export/import behavior intentionally changed.
- No Scrub Key storage, secrets, tokens or real personal data added.

Outcome:

- Next recommended step is `WP14 — v13.8 DOCX reinsert upload/download UI`.
- PDF remains out of implementation scope until a separate reliability review.

---

## WP13 — v13.7 TXT reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Add controlled TXT upload/download support inside `Originele waarden terugzetten`.
- Keep the existing pasted-text reinsert flow available as fallback.
- Reuse the existing deterministic local TXT helper.
- Keep DOCX upload reinsert UI, PDF reinsert, AI and cloud behavior out of scope.

Files added or changed:

- Changed `fix_streamlit_nested_expanders.py`.
- Changed `tests/test_two_mode_ui_patch.py`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `tests/test_txt_reinsert_ui_patch.py`.
- Added `handover/workpackages/20260608_0000_v13_7_txt_reinsert_upload_download_ui.md`.

Main change:

- Added section `TXT-bestand terugzetten` inside the `Originele waarden terugzetten` mode.
- Added TXT upload label `Upload een TXT-bestand met placeholders`.
- Added action button `Zet TXT-bestand lokaal terug`.
- Added output label `Herstelde TXT-tekst`.
- Added download label `Download hersteld TXT-bestand (.txt)`.
- The UI calls:
  - `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")`.
- TXT reinsert requires a loaded Scrub Key before running.
- The restored TXT result shows text output and an audit summary.
- The existing pasted-text reinsert flow remains available.
- The existing anonymization workflow remains in `Anonimiseren`.

Safety/warnings:

- The TXT reinsert UI warns that restored output may contain personal/confidential data again.
- The UI states that reinsert is local-only and uses no AI/cloud processing.
- The Scrub Key warning remains present and keeps the pseudonymization/reversibility context.

Tests added/updated:

- Added `tests/test_txt_reinsert_ui_patch.py`.
- Updated `tests/test_two_mode_ui_patch.py`.

The tests check:

- `reinsert_txt_bytes` is imported and used;
- TXT UI labels are present;
- TXT upload accepts `.txt` only;
- TXT reinsert requires a loaded Scrub Key;
- TXT reinsert is injected only in the `Originele waarden terugzetten` mode;
- pasted-text reinsert labels remain present;
- `Scrub Key laden` remains present;
- `Anonimiseren` remains present;
- existing anonymization/export markers remain present;
- existing Scrub Key export remains present;
- no DOCX upload reinsert UI is added;
- no PDF reinsert is added;
- no AI/cloud behavior is added;
- `apply_replacements_to_text` is not altered;
- existing scrubbed download markers are not rewired.

Validation:

- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: confirmed by coordinator/user in WP13B.

Intentionally not changed:

- `presidio_streamlit.py` was not directly edited.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration beyond TXT local reinsert added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior intentionally changed.
- No Scrub Key JSON export behavior intentionally changed.
- No Scrub Key import/reload behavior intentionally changed except reusing the loaded key for TXT reinsert.
- No Scrub Key storage, secrets, tokens or real personal data added.

---

## WP12B — v13.6 Two-mode UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.6 two-mode UI is closed as completed and app-verified.
- Next implementation workpackage was `WP13 — v13.7 TXT reinsert upload/download UI`.

---

## Earlier completed work

- v13.6 two-mode UI implementation and app verification closeout.
- v13.3 deterministic reinsert UI implementation.
- v13.3 deterministic reinsert UI planning.
- v13.3 deterministic reinsert helper verification reconciliation.
- v13.2 Scrub Key import/reload UI app verification closeout.
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

- WP14 — v13.8 DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
