# Workpackage claim — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Remove duplicate upload/input presentation while preserving ingestion behavior

Status: in_progress

Claimed by: market-predictions via ChatGPT web worker

Claimed at: 2026-07-04 23:27 Europe/Amsterdam

Branch: scrub-duplicate-input-surface-simplification-implementation

Scope:
- Implement one coherent visible input surface in the default Anonimiseren flow.
- Keep existing upload, synthetic example, pasted/extracted text and input precedence semantics.
- Keep review/export/Scrub Key/reinsert/audit behavior unchanged.

Boundaries:
- No startup/runtime patching.
- No new upload backend.
- No OCR, AI document processing or cloud document processing.
- No recognizer, export, Scrub Key or reinsert semantic changes.

Validation target:
- python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py
- related source-level UI/export tests
- git diff --check
