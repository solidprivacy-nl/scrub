# Changelog — SolidPrivacy Scrub

## WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — Contract tests for simple masked-text highlight toggle plan

Status: completed tests/documentation-only; awaiting GitHub Actions and Hugging Face sync evidence.

Files added:

- `tests/test_review_highlight_toggle_plan.py`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260613_1745_review_highlight_toggle_contract_tests.md`

Summary:

- Added contract tests for `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`.
- Tests cover Dutch labels, on/off copy, read-only and visual-only boundaries, table-first/source-of-truth behavior, exact matching only, allowed and forbidden highlighted values, no replacement table mutation, no automatic replacement, no Scrub Key writes, no export/download changes, no export blocking, no reinsert changes, no old WP42D startup mutation route, no click-to-mark, no advanced editor, no full-document marking, raw-HTML escaping/accessibility expectations and synthetic-only/no-real-data constraints.
- No Streamlit UI, product runtime, export/download, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

Next recommended step:

- Verify Actions and sync.
- `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION` remains blocked without separate coordinator approval.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3 — Restore exact replacement UI plan sequencing phrase

Status: completed after Actions/HF verification; app verification not applicable.

Summary:

- Restored: `Only after that should a small UI implementation package be considered.`
- Coordinator screenshot evidence confirmed `Tests #855` green and `Sync to Hugging Face Space #867` green for commit `c9b5201`.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning

Status: completed planning/specification-only; no UI or product code changed.

Summary:

- Planned a simple optional review toggle: `Markeringen tonen` / `Markeringen tonen in voorbeeldtekst`.
- Goal is to show subtle visual markers for values already masked/replaced in the preview text.
- The planned toggle remains visual-only, read-only, non-authoritative and non-mutating.
- The review table remains the source of truth and fallback.
- Explicitly blocks the old WP42D static-highlight startup mutation route, startup patching of `presidio_streamlit.py`, click-to-mark, advanced editor behavior, full-document marking, raw unsafe HTML, Scrub Key writes, export/download changes and reinsert changes.

## WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

Status: completed product rollback/hide.

Summary:

- Product feedback rejected the technically working replacement helper panel as not intuitive enough for the normal user flow.
- The panel is no longer rendered from the normal Scrub Legal flow.
- Helper and contract assets remain available for later redesign.
- No replacement behavior, export behavior, Scrub Key behavior or reinsert behavior changed.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — replacement-logic contract text repair.
- WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — workflow-status risk wording repair.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
