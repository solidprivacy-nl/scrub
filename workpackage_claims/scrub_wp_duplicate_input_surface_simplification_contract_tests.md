# Workpackage claim — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — Lock single input-surface contract before implementation

Status: in_progress

Claimed by: market-predictions via ChatGPT web worker

Claimed at: 2026-07-04 23:12 Europe/Amsterdam

Branch: scrub-duplicate-input-surface-contract-tests

Scope:
- Add source-level contract tests only.
- Update CHANGELOG.md and WORKPACKAGES.md narrowly.
- Create required handover.

Boundaries:
- No product implementation files changed.
- No Streamlit imports in tests.
- No runtime/startup patches.
- No UI behavior changes.

Validation target:
- python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py
- related source-level UI/export contract checks named in the workpackage
- git diff --check

