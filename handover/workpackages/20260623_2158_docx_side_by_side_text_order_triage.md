# Handover — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

Repository worked in:
- solidprivacy-nl/scrub

Workpackage title:
- SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

Status:
- completed / ready for PR verification

Summary:
- Investigated DOCX side-by-side preview order mismatch found during live app verification.
- Root cause reproduced: DOCX plain-text extraction yielded all body paragraphs before body tables.
- Fixed extraction so DOCX body paragraphs and tables are yielded in document XML order.
- Header and footer support remains appended after main body, preserving the existing support boundary.
- Added synthetic regression tests for interleaved paragraph/table order.
- No DOCX export semantics changed.
- No Scrub Key JSON semantics changed.
- No reinsert helper behavior changed.
- No OCR, cloud, AI, PDF reconstruction or DOCX reconstruction added.

Files added/changed:
- document_tools.py
- tests/test_docx_text_order_extraction.py
- workpackage_claims/scrub_wp_docx_side_by_side_text_order_triage.md
- CHANGELOG.md
- RELEASE_NOTES.md
- WORKPACKAGES.md
- handover/workpackages/20260623_2158_docx_side_by_side_text_order_triage.md
- .github/workflows/tests.yml

Tests:
- python -m pytest -q tests/test_docx_text_order_extraction.py → 2 passed
- python -m pytest -q tests/test_docx_text_order_extraction.py tests/test_scrub_key_document_reinsert.py tests/test_docx_reinsert_ui_patch.py tests/test_docx_hygiene_audit.py tests/test_docx_hygiene_audit_ui_patch.py → 40 passed
- python -m pytest tests -x -vv → 649 passed in 102.51s
- python -m py_compile document_tools.py presidio_streamlit.py → passed
- git diff --check → passed

Validation status:
- Local validation passed.

GitHub Actions status:
- Initial PR run failed because the Tests workflow did not install DOCX/PDF runtime dependencies.
- `.github/workflows/tests.yml` updated to install `python-docx`, `pymupdf`, `reportlab` and `pypdf` for regression tests.
- Pending rerun after amended push.

Hugging Face sync status:
- Pending merge to main.

App verification status:
- Pending after merge and sync.
- Specific live verification needed: upload DOCX with interleaved body paragraph/table content and confirm side-by-side preview order matches expected reading order.

Remaining risks:
- DOCX text boxes, floating shapes and other non-body layout objects may still have extraction-order limitations because python-docx does not model Word's visual pagination.
- This fix targets body paragraph/table order only.

Next recommended step:
- Open PR for review.
- After GitHub Actions pass, merge.
- Verify GitHub to Hugging Face sync.
- Verify live app side-by-side DOCX preview order with a synthetic/non-sensitive DOCX.
