# Workpackage Claim — WP_DUTCH_LEGAL_RECALL_GAP_TESTS

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_DUTCH_LEGAL_RECALL_GAP_TESTS — Add tests for known Dutch legal detection gaps
started timestamp: 2026-06-16 22:09 Europe/Amsterdam
completed timestamp: 2026-06-16 22:09 Europe/Amsterdam
scope: tests/documentation-only for known Dutch legal recall gaps
boundaries: no product-code, no recognizer, no UI, no export behavior changes

final commit SHA or PR link: c935f645c4b60e8e7e971250bd75b72e7155f101 — Add handover for Dutch legal recall gap tests
handover path: handover/workpackages/20260616_2209_dutch_legal_recall_gap_tests.md

files added:
- tests/test_dutch_legal_recall_gap_baseline.py
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md
- handover/workpackages/20260616_2209_dutch_legal_recall_gap_tests.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md

tests/checks:
- Required local tests were not runnable in this environment because the container could not clone/access GitHub for a local working tree.
- GitHub connector checks confirmed the new baseline test file exists and contains 2 normal tests plus 6 xfail(strict=False) tests.
- GitHub connector checks confirmed no product-code file was changed.

known gaps recorded:
- Dutch legal reference numbers and Rechtspraak-like rolnummers.
- Client/dossier/zaak numbers.
- Legal reference code misclassification as phone-number-like values.
- Generic legal role words that should remain readable.
- Over-masking risk where legal role structure becomes unreadable.

expected passing tests:
- test_synthetic_gap_fixture_contains_required_legal_references
- test_synthetic_role_fixture_contains_only_generic_role_words

expected xfail tests:
- test_known_gap_legal_reference_numbers_should_be_detectable
- test_known_gap_claim_reference_must_not_be_phone_number
- test_known_gap_client_dossier_and_zaak_numbers_should_be_detectable
- test_known_gap_rechtspraak_like_rolnummers_should_be_detectable
- test_known_gap_role_words_alone_should_not_be_detected_as_person_values
- test_known_gap_overmasking_should_not_remove_legal_role_structure

GitHub Actions status: unknown / not exposed through connector. `get_commit_combined_status` returned no statuses and `fetch_commit_workflow_runs` returned an empty list for checked commit `682f5b0e8b6e84d9bb4d2025d143682e26e4ddd6`.
Hugging Face sync status: unknown / not exposed through connector for these commits.
app verification status: not required; tests/documentation-only and no app behavior changed.

remaining risks:
- Local pytest/py_compile could not be executed here.
- CI/HF sync must be verified from GitHub UI or when connector visibility becomes available.
- The gaps are documented/test-visible only; recognizer behavior is not fixed in this package.

next recommended step: do not automatically start recognizer fixes. Likely next package after separate coordinator approval is WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.
