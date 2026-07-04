# Workpackage claim — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — Lock single input-surface contract before implementation

Status: completed / PR validation pending

Claimed by: market-predictions via ChatGPT web worker

Claimed at: 2026-07-04 23:12 Europe/Amsterdam

Completed at: 2026-07-04 23:15 Europe/Amsterdam

Branch: scrub-duplicate-input-surface-contract-tests

PR: https://github.com/solidprivacy-nl/scrub/pull/22

Scope:
- Added source-level contract tests only.
- Updated CHANGELOG.md and WORKPACKAGES.md narrowly.
- Created required handover.

Boundaries:
- No product implementation files changed.
- No Streamlit imports in tests.
- No runtime/startup patches.
- No UI behavior changes.
- No export/Scrub Key/reinsert/recognizer/dependency changes.

Validation target:
- python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py
- related source-level UI/export contract checks named in the workpackage
- git diff --check

Validation status:
- Local sandbox could not clone GitHub due DNS/network restrictions, so local pytest execution in this chat environment was not possible.
- PR/GitHub Actions validation pending.

Handover: handover/workpackages/20260704_2318_duplicate_input_surface_contract_tests.md

Next recommended step:
- Review PR validation.
- If green, merge this contract-test package.
- Then start SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION.
