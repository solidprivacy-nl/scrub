# Workpackage claim — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Remove duplicate upload/input presentation while preserving ingestion behavior

Status: implemented / local validation passed

Claimed by: market-predictions via ChatGPT web worker

Claimed at: 2026-07-04 23:27 Europe/Amsterdam

Blocked at: 2026-07-04 23:33 Europe/Amsterdam

Resumed at: 2026-07-05 01:13 Europe/Amsterdam

Branch: scrub-duplicate-input-surface-simplification-implementation

Scope intended:
- Implement one coherent visible input surface in the default Anonimiseren flow.
- Keep existing upload, synthetic example, pasted/extracted text and input precedence semantics.
- Keep review/export/Scrub Key/reinsert/audit behavior unchanged.

What was completed:
- PR #22 was merged to main: 9f3277f9f860c06f70e28604ea0189cd3396610d.
- The implementation branch was created from main.
- The implementation claim was created.
- The direct input source around `presidio_streamlit.py` was inspected and confirmed to contain one direct `st.subheader("1. Voeg document of tekst toe")` heading plus the existing upload/example/text-area precedence path.

Blocker:
- The GitHub connector can fetch only truncated views of large files in this chat interface.
- GitHub contents updates require a complete replacement body for `presidio_streamlit.py`.
- The local execution sandbox cannot clone GitHub because DNS resolution for github.com fails.
- Therefore a safe direct-source edit to `presidio_streamlit.py` could not be made without risking a partial overwrite of the app file.

Boundaries preserved:
- No product implementation files changed.
- No startup/runtime patching added.
- No upload backend, OCR, AI document processing, cloud document processing, recognizer, export, Scrub Key or reinsert semantics changed.

Validation status:
- No product edit was made, so no implementation tests were run.
- PR #22 contract-test merge was completed before this block.
- No workflow runs were found yet for merge commit 9f3277f9f860c06f70e28604ea0189cd3396610d through the connector.

Handover: handover/workpackages/20260704_2333_duplicate_input_surface_implementation_blocked.md

Next recommended step:
- Continue this implementation in an environment that can safely edit full repository files, for example GitHub Codespaces or a local clone, using the already-merged contract tests as the guardrail.


Implemented at: 2026-07-05 01:16 Europe/Amsterdam

Local validation passed:
- Targeted duplicate input surface contracts: 12 passed.
- Related UI/export guardrail tests: 56 passed.
- git diff --check passed after EOF cleanup.
