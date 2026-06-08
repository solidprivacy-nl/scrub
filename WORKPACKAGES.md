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

## WP14 / WP14B / WP14C — v13.8 DOCX reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

WP14 implemented controlled DOCX upload/download reinsert in `Originele waarden terugzetten`, using the existing local helper `reinsert_docx_bytes(content, scrub_key)`.

Existing pasted-text reinsert and TXT reinsert remain available.

WP14B was recorded cautiously because explicit verification evidence was not available to that worker at the time.

WP14C reconciles the status after coordinator/user evidence was supplied.

## Technical verification evidence

Coordinator evidence:

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

## App verification evidence

Coordinator/user evidence confirms:

- `Originele waarden terugzetten` is active.
- `Scrub Key laden` is visible.
- Scrub Key JSON is loaded.
- Pasted-text reinsert remains available.
- TXT reinsert remains available.
- `DOCX-bestand terugzetten` is visible.
- DOCX limitations warning is visible.
- DOCX file upload works.
- `Zet DOCX-bestand lokaal terug` works with a valid Scrub Key.
- Result message appears: `DOCX-bestand lokaal teruggezet`.
- Result message appears: `15 waarde(n) lokaal teruggezet in het DOCX-bestand.`
- `Download hersteld DOCX-bestand (.docx)` is visible.
- `Controleverslag DOCX terugzetten` appears.
- Audit shows document type `docx`, mapping counts, restored value count, placeholder checks, validation issues and DOCX limitations.
- Audit shows `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Also confirmed:

- No PDF reinsert appears.
- No AI/cloud behavior appears.
- Existing pasted-text reinsert remains available.
- Existing TXT reinsert remains available.
- Existing Scrub Key import/export remains available.
- Existing scrubbed export/download semantics remain unchanged.

## WP14C — final verification reconciliation

Status: completed.

Scope:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260608_0045_v13_8_docx_reinsert_upload_download_ui_final_reconciliation.md`

No code files were changed in WP14C.

## Next recommended step

WP15 — PDF text extraction reliability review only.
