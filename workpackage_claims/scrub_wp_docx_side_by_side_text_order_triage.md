# Workpackage claim — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

repo=solidprivacy-nl/scrub
workpackage=SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE
status=in_progress
branch=scrub-docx-side-by-side-text-order-triage

Goal:
- Reproduce and triage DOCX side-by-side preview text order mismatch.

Scope:
- Investigate DOCX-to-text extraction used for preview/side-by-side only.
- Add synthetic regression test for DOCX visual/order markers.
- Do not change DOCX export semantics.
- Do not change Scrub Key JSON semantics.
- Do not change reinsert helper behavior.
- Do not add OCR, cloud processing, AI, PDF reconstruction or DOCX reconstruction.
- Use synthetic data only.

Known finding:
- Uploaded DOCX can show page/order mismatch in side-by-side preview.
- Restored DOCX output appears to preserve the correct document order.
