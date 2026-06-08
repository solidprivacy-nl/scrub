# Changelog — SolidPrivacy Scrub

## WP14B — v13.8 DOCX reinsert upload/download UI app verification closeout

Status: recorded; final verified closeout still pending.

Scope was documentation only:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260608_0030_v13_8_docx_reinsert_upload_download_ui_app_closeout.md`

No code files were changed in WP14B.

Finding:

- WP14 was implemented before this closeout.
- At the start of WP14B, WP14 was still waiting for final verification evidence.
- The WP14B request did not include explicit app verification evidence.
- The connector did not show status records or workflow runs for commit `8651fc7520cebc321b4b893557fce57afc314fe4`.

Result:

- WP14B is documented.
- WP14 is not marked as fully verified yet.
- A final closeout remains needed after evidence is supplied.

Next required evidence:

- tests green;
- deployment sync green;
- app check confirms DOCX upload/download reinsert works;
- existing anonymization and download behavior remains available.

## WP14 — v13.8 DOCX reinsert upload/download UI

Status: implemented; awaiting final verification evidence.

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

- WP14B-FINAL — final verification closeout once evidence is supplied.
- WP15 — PDF text extraction reliability review only.
