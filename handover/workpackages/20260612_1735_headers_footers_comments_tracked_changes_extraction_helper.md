# Handover — WP37 Headers/footers/comments/tracked-changes extraction helper

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP37 — Headers/footers/comments/tracked-changes extraction helper`

Status: completed helper/tests/documentation-only.

## Summary

WP37 added a pure local, read-only DOCX hidden-content extraction helper that makes high-risk DOCX parts audit-visible before any cleaner, removal policy or export-blocking policy is implemented.

The helper detects and extracts text from headers, footers, comments/person metadata and tracked-change markers. It returns audit-oriented fields and explicit non-change flags such as `extraction_only: true`, `cleaning_applied: false` and `export_blocking: false`.

## Files added

- `docx_hidden_content_extractor.py`
- `DOCX_HIDDEN_CONTENT_EXTRACTION_HELPER.md`
- `tests/test_docx_hidden_content_extractor.py`
- `workpackage_claims/WP37_headers_footers_comments_tracked_changes_extraction_helper.md`
- `handover/workpackages/20260612_1735_headers_footers_comments_tracked_changes_extraction_helper.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests added/updated

Added:

```text
tests/test_docx_hidden_content_extractor.py
```

The tests use synthetic data only and cover:

- extracting `word/header1.xml`, `word/footer1.xml`, `word/comments.xml` and tracked-change markers from `word/document.xml`;
- reporting absence of headers/footers/comments/tracked changes without warnings;
- invalid DOCX bytes safely returning validation issues;
- non-bytes input safely returning validation issues;
- synthetic-only fixture boundaries.

## Tests/checks run

No tests were run in the live GitHub checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Expected targeted validation:

```text
pytest tests/test_docx_hidden_content_extractor.py
```

Expected related regression validation:

```text
pytest tests/test_docx_hidden_content_extractor.py tests/test_docx_residual_placeholder_comments_risk.py tests/test_scrub_key_document_reinsert.py
```

## Validation status

- Required start sequence was followed from GitHub `main`.
- WP37 claim was checked and created before changes.
- Existing DOCX hidden-content risk review, WP36A triage and current DOCX reinsert limitations were inspected.
- Helper is local, read-only and side-effect free.
- No real data was added.

## GitHub Actions status

- Pending / not verified through connector at handover time.
- The final commits should be validated by GitHub Actions.

## Hugging Face sync status

- Not applicable for app behavior. WP37 does not change UI/runtime behavior in the Hugging Face Space.
- Repository sync status may still be checked by normal project monitoring.

## App verification status

- Not applicable; no UI behavior changed.

## Remaining risks

- WP37 only extracts/detects hidden DOCX content. It does not scrub, clean, remove, block export or surface the audit in UI.
- Comments, tracked changes, headers and footers can still contain sensitive data in real documents.
- No DOCX hygiene audit report consumes this helper output yet.
- No clean DOCX export policy exists yet.
- Footnotes, endnotes, metadata, custom XML, text boxes/shapes and embedded objects are still future work.

## Next recommended step

- `WP38 — DOCX hygiene audit report`.

## Intentionally not changed

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking.
- No export semantics changed.
- No DOCX reinsert behavior changed.
- No Streamlit UI changed.
- No Scrub Key schema changed.
- No dependency change.
- No real data added.
- No cloud processing added.
