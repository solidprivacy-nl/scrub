# Changelog — SolidPrivacy Scrub

## WP14C — v13.8 DOCX reinsert upload/download UI final verification reconciliation

Status: completed.

WP14 DOCX reinsert UI is now completed and app-verified after Actions/sync verification.

Purpose:

- Reconcile WP14 final status after coordinator/user verification evidence was supplied.
- Supersede the cautious WP14B status, which was recorded before evidence was available to that worker.
- Update project status only.

Files changed or added in WP14C:

- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0045_v13_8_docx_reinsert_upload_download_ui_final_reconciliation.md`.

No code files were changed.

Technical verification evidence supplied by coordinator:

```text
Tests #177 green — commit 22b7066
Sync to Hugging Face Space #191 green — commit 22b7066
Tests #178 green — commit 68379c6
Sync to Hugging Face Space #192 green — commit 68379c6
Tests #179 green — commit 03fd2cd
Sync to Hugging Face Space #193 green — commit 03fd2cd
Tests #180 green — commit 8651fc7
Sync to Hugging Face Space #194 green — commit 8651fc7
```

Latest WP14 implementation commit:

```text
8651fc7520cebc321b4b893557fce57afc314fe4
```

App verification supplied by coordinator/user confirms:

- `Originele waarden terugzetten` is active.
- `Scrub Key laden` is visible.
- Scrub Key JSON is loaded.
- Pasted-text reinsert remains available.
- TXT reinsert remains available.
- `DOCX-bestand terugzetten` is visible.
- DOCX limitations warning is visible.
- DOCX file upload works.
- `Zet DOCX-bestand lokaal terug` works with a valid Scrub Key.
- `DOCX-bestand lokaal teruggezet` appears.
- `15 waarde(n) lokaal teruggezet in het DOCX-bestand.` appears.
- `Download hersteld DOCX-bestand (.docx)` is visible.
- `Controleverslag DOCX terugzetten` appears.
- Audit shows document type `docx`, mapping counts, restored value count, placeholder checks, validation issues and DOCX limitations.
- Audit shows `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Also confirmed:

- No PDF reinsert was added.
- No AI/cloud behavior was added.
- Existing pasted-text reinsert remains available.
- Existing TXT reinsert remains available.
- Existing Scrub Key import/export remains available.
- Existing scrubbed export/download semantics remain unchanged.

Validation:

- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: confirmed by coordinator/user.

## WP14B — v13.8 DOCX reinsert upload/download UI app verification closeout

Status: superseded by WP14C final reconciliation.

WP14B was cautious because explicit app-verification evidence was not available to that worker at that time.

## WP14 — v13.8 DOCX reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

WP14 added controlled DOCX upload/download reinsert in `Originele waarden terugzetten` using `reinsert_docx_bytes(content, scrub_key)`.

Existing pasted-text reinsert and TXT reinsert remain available.

DOCX limitations remain visible in the UI.

## WP13B — v13.7 TXT reinsert upload/download UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

## Earlier completed work

- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
- Earlier Dutch Legal UI and recognizer work.

## Planned later phase

- WP15 — PDF text extraction reliability review only.
