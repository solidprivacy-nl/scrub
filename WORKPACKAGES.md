# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Current status

WP0 through WP13B are complete.

WP14 — v13.8 DOCX reinsert upload/download UI:

Status: implemented; awaiting external verification evidence.

WP14 implementation added controlled DOCX upload/download reinsert in `Originele waarden terugzetten`, using the existing local helper `reinsert_docx_bytes(content, scrub_key)`. Existing pasted-text reinsert and TXT reinsert remain available.

## WP14B — v13.8 DOCX reinsert upload/download UI app verification closeout

Status: recorded; not closed as fully verified.

Reason: the WP14B request did not include explicit verification evidence. The connector also did not show status records or workflow runs for the latest WP14 commit checked: `8651fc7520cebc321b4b893557fce57afc314fe4`.

WP14B scope was documentation only:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260608_0030_v13_8_docx_reinsert_upload_download_ui_app_closeout.md`

No code files were changed in WP14B.

## Next recommended step

Provide final verification evidence for WP14, then run a final closeout.

Required evidence:

- tests green;
- deployment sync green;
- app check confirms the DOCX reinsert workflow works;
- existing anonymization and download behavior remains available.

After that, WP14 can be marked as completed and app-verified.
