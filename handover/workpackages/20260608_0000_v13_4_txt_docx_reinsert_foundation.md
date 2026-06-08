# Handover — WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Repository: `solidprivacy-nl/scrub`  
Status: implemented; GitHub Actions and Hugging Face sync pending coordinator/app-independent verification

## Summary

WP10 implemented a helper/test-only document-level reinsert foundation for TXT and DOCX.

The new helper wraps the existing deterministic `reinsert_from_scrub_key(...)` logic and adds document-level wrappers for:

- plain text;
- TXT bytes;
- DOCX bytes.

No UI was added. No PDF reinsert was implemented. No AI calls or cloud processing were added. Existing scrubbed export/download behavior and Scrub Key export/import behavior were not changed.

## Files added

- `scrub_key_document_reinsert.py`
- `tests/test_scrub_key_document_reinsert.py`
- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Local reconstructed targeted validation:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py
# 6 passed

PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py
# 12 passed

PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py
# 14 passed
```

Local reconstructed full available subset:

```bash
PYTHONPATH=. pytest -q
# 32 passed
```

Important validation note:

- Repository clone via container was not possible because outbound GitHub DNS was unavailable.
- Validation was performed on reconstructed files from GitHub-fetched content plus the new helper/tests.

## Validation

- Helper validation: passed locally on reconstructed targeted test set.
- GitHub Actions: pending / not checked after final commit.
- Hugging Face sync: pending / not checked after final commit.
- App verification: not applicable; no UI behavior changed.

## GitHub Actions status

Pending / not checked after final commit.

## Hugging Face sync status

Pending / not checked after final commit.

## App verification status

Not applicable; no UI behavior changed.

## Implemented behavior

New helper module:

```text
scrub_key_document_reinsert.py
```

Functions added:

```python
reinsert_text_document(text, scrub_key) -> dict
reinsert_txt_bytes(content, scrub_key, encoding="utf-8") -> dict
reinsert_docx_bytes(content, scrub_key) -> dict
```

The helper:

- reuses `reinsert_from_scrub_key(...)`;
- supports text/TXT input;
- supports DOCX input via standard-library OOXML package handling;
- returns restored text and restored bytes where applicable;
- returns audit summary fields;
- reports `document_type`;
- reports `local_only=True`;
- reports `ai_processing=False`;
- reports `cloud_processing=False`;
- does not mutate the input Scrub Key;
- remains side-effect free.

## DOCX limitations

DOCX support is intentionally foundation-level only:

- only `word/document.xml` text nodes are processed;
- normal body paragraphs and tables in `word/document.xml` are supported;
- placeholders split across multiple Word runs/text nodes are not restored;
- headers, footers, comments, tracked changes and metadata are not processed;
- perfect formatting preservation is not claimed;
- limitations are returned in `limitations` and `unsupported_parts`.

## Remaining risks

- DOCX placeholders split across multiple runs are not restored yet.
- Headers/footers/comments/tracked changes/metadata remain out of scope.
- Real-world DOCX files may contain richer structures than the synthetic tests.
- GitHub Actions and Hugging Face sync still need coordinator/app-independent verification.
- Future UI work must not be run in parallel with other edits to `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`.

## Next recommended step

1. Verify GitHub Actions and Hugging Face sync for WP10.
2. Start:

```text
WP11 — v13.5 Two-mode reinsert UI planning
```

Recommended WP11 scope:

- planning/specification only;
- plan `Anonimiseren` / `Originele waarden terugzetten` mode structure;
- decide where TXT/DOCX reinsert upload should appear;
- do not edit UI code yet;
- do not implement PDF reinsert;
- do not add AI/cloud behavior.
