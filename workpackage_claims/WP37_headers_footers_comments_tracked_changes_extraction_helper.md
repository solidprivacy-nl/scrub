# Workpackage claim — WP37 Headers/footers/comments/tracked-changes extraction helper

Repository: `solidprivacy-nl/scrub`

Workpackage: `WP37 — Headers/footers/comments/tracked-changes extraction helper`

Status: `completed`

Claimed by: `ChatGPT webinterface worker`

Claim created: `2026-06-12`

Completed: `2026-06-12`

Scope completed:

- Added a pure local DOCX inspection/extraction helper for headers, footers, comments and tracked-change signals.
- Added synthetic tests.
- Updated central status/risk docs and handover.

Do not change boundary preserved:

- No DOCX cleaner behavior.
- No comments/tracked-changes removal behavior.
- No export blocking.
- No export semantics.
- No Streamlit UI.
- No DOCX reinsert behavior.
- No Scrub Key schema.
- No dependencies.
- No cloud processing.
- No real data.

Files added:

```text
docx_hidden_content_extractor.py
DOCX_HIDDEN_CONTENT_EXTRACTION_HELPER.md
tests/test_docx_hidden_content_extractor.py
handover/workpackages/20260612_1735_headers_footers_comments_tracked_changes_extraction_helper.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP37_headers_footers_comments_tracked_changes_extraction_helper.md
```

Validation:

```text
Not run in live GitHub checkout. Validate with GitHub Actions.
```

Expected checks:

```text
pytest tests/test_docx_hidden_content_extractor.py
pytest tests/test_docx_hidden_content_extractor.py tests/test_docx_residual_placeholder_comments_risk.py tests/test_scrub_key_document_reinsert.py
```

Handover path:

```text
handover/workpackages/20260612_1735_headers_footers_comments_tracked_changes_extraction_helper.md
```

Remaining risks:

```text
The helper extracts/detects hidden DOCX content but does not scrub, clean, remove, block export or expose a user-facing audit report yet.
```

Next recommended step:

```text
WP38 — DOCX hygiene audit report
```
