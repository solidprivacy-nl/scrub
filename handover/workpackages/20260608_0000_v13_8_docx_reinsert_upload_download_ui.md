# Handover — WP14 — v13.8 DOCX reinsert upload/download UI

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP14 — v13.8 — DOCX reinsert upload/download UI`

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

WP14 adds controlled DOCX upload/download support for local reinsert inside `Originele waarden terugzetten`.

The implementation reuses the existing deterministic helper:

```python
reinsert_docx_bytes(content, scrub_key)
```

Existing pasted-text reinsert remains available.

Existing TXT upload/download reinsert remains available.

Existing anonymization export/download behavior is not intentionally changed.

## Files added

- `tests/test_docx_reinsert_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_8_docx_reinsert_upload_download_ui.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `tests/test_txt_reinsert_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Implementation commits

```text
83f7ebb0afea4798e4295b088b0a3f8058a9a64d
292d34ea8e4f179b5e93ebfcd93397891cf6e659
e36915b61d21d10a2fb30ebe9f7d5b8581c561f3
22b7066cd89c98f3e81e87ec5cf96ee07e5b58b5
68379c66bdcfb5595871cc322983848c38e7d005
03fd2cd58831b4e225c65576c891f2bdcb5fccf2
```

## UI behavior added

Inside `Originele waarden terugzetten`, the UI now includes:

```text
DOCX-bestand terugzetten
Upload een DOCX-bestand met placeholders
Zet DOCX-bestand lokaal terug
DOCX-bestand lokaal teruggezet
Download hersteld DOCX-bestand (.docx)
Controleverslag DOCX terugzetten
```

The DOCX upload accepts `.docx` only and requires a loaded valid Scrub Key before reinsert runs.

The restored DOCX output is available as a `.docx` download.

The audit summary includes:

- document type;
- mapping item count;
- active item count;
- excluded item count;
- replacement count;
- placeholders not found;
- unknown placeholders;
- duplicate placeholders;
- validation issues;
- local-only status;
- no-AI status;
- no-cloud status;
- DOCX limitation note.

## DOCX limitations shown

The UI explicitly states that DOCX reinsert currently supports normal document text and tables, and that headers, footers, comments, tracked changes and placeholders split across Word text fragments are not fully supported.

No perfect DOCX formatting preservation is claimed.

## Tests

Added:

```text
tests/test_docx_reinsert_ui_patch.py
```

Updated:

```text
tests/test_two_mode_ui_patch.py
tests/test_txt_reinsert_ui_patch.py
```

The tests guard:

- `reinsert_docx_bytes` import/use;
- DOCX UI labels;
- `.docx` upload-only configuration;
- loaded Scrub Key requirement;
- placement only in `Originele waarden terugzetten`;
- DOCX limitations warning;
- DOCX audit fields;
- existing pasted-text reinsert;
- existing TXT reinsert;
- existing anonymization/export markers;
- existing Scrub Key export/import labels;
- no PDF reinsert;
- no AI/cloud behavior;
- no direct rewrite of existing scrubbed download widgets;
- no alteration of `apply_replacements_to_text`.

## Validation status

Local test execution was not performed in this connector session.

Recommended validation commands:

```bash
PYTHONPATH=. pytest -q tests/test_docx_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_txt_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_two_mode_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py
```

If feasible:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py
PYTHONPATH=. pytest -q tests/test_scrub_key_import.py
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py
PYTHONPATH=. pytest -q
```

## GitHub Actions status

Pending / not visible through the connector at handover time.

The combined-status endpoint returned no status records for the latest implementation commit checked during the session.

## Hugging Face sync status

Pending / not yet verified.

## App verification status

Required and pending because WP14 changes UI behavior.

App verification should confirm:

### In `Anonimiseren`

- anonymization workflow remains available;
- source text/file input remains visible;
- review table remains visible;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- Scrub Key JSON export remains available;
- DOCX reinsert upload UI is not shown as part of the anonymization workflow.

### In `Originele waarden terugzetten`

- `Scrub Key laden` remains visible;
- Scrub Key upload/paste validation remains visible;
- pasted-text reinsert remains visible;
- TXT reinsert upload/download remains visible;
- `DOCX-bestand terugzetten` is visible;
- DOCX upload accepts `.docx`;
- `Zet DOCX-bestand lokaal terug` works with a valid Scrub Key;
- restored DOCX download appears;
- `Download hersteld DOCX-bestand (.docx)` works;
- `Controleverslag DOCX terugzetten` appears;
- DOCX limitations warning is visible;
- warning about restored sensitive/confidential data is visible;
- local-only / no-AI / no-cloud text is visible.

Also confirm:

- no PDF reinsert appears;
- no AI/cloud behavior appears;
- existing Scrub Key export/import remains available;
- existing scrubbed export/download semantics are unchanged.

## Boundaries preserved

- `presidio_streamlit.py` was not directly edited.
- No PDF reinsert was added.
- No AI calls were added.
- No cloud processing was added.
- No automatic document rehydration beyond the documented local DOCX helper was added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior was intentionally changed.
- No TXT reinsert upload/download behavior was intentionally changed.
- No pasted-text reinsert behavior was intentionally changed.
- No Scrub Key JSON export/import behavior was intentionally changed.
- No Scrub Keys, secrets, tokens or real personal data were stored.

## Remaining risks

- GitHub Actions still need to be verified.
- GitHub to Hugging Face sync still needs to be verified.
- Hugging Face app verification is still required.
- DOCX support remains limited to the existing helper scope.
- Placeholders split across Word text fragments may not be restored.
- Headers, footers, comments, tracked changes and metadata are not handled by the current DOCX helper.

## Next recommended step

```text
WP14-CLOSEOUT — v13.8 DOCX reinsert upload/download UI app verification closeout
```

Start closeout only after GitHub Actions, Hugging Face sync and app verification evidence are available.
