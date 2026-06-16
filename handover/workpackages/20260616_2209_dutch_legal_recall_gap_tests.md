# Handover — WP_DUTCH_LEGAL_RECALL_GAP_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_DUTCH_LEGAL_RECALL_GAP_TESTS — Add tests for known Dutch legal detection gaps`

Status: completed as tests/documentation-only baseline. No product behavior was changed.

## Summary

Added a new tests-only baseline file for known Dutch legal recall and precision gaps. The tests use synthetic Dutch legal text and mark known current shortcomings as `xfail(strict=False)`, so CI can remain green while gaps stay visible for a later pattern-fix workpackage.

## Files added

- `tests/test_dutch_legal_recall_gap_baseline.py`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md`
- `handover/workpackages/20260616_2209_dutch_legal_recall_gap_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md` pending final closeout update after this handover file

## Gaps recorded

The new baseline records these known Dutch legal detection risks:

- legal reference numbers and Rechtspraak-like references:
  - `10598721 / UE VERZ 26-441`
  - `ARN 26/4412`
  - `ZK-WOON-55091`
  - `CL-FAM-55201`
  - `WR-KLANT-2026-7712`
  - `FACT-2026-4481`
  - `CAM-MAAS-2026-0518`
  - `INC-2026-0912`
  - `REP-2026-4410`
  - `CLM-2026-112233`
- client/dossier/zaak numbers:
  - `CLNT-2026-0042`
  - `DOS-2026-778899`
  - `ZK-WOON-55091`
- claim/reference-code misclassification risk where legal codes resemble phone numbers.
- Rechtspraak-like rolnummer detection.
- generic legal role words that should remain readable:
  - `eiser`
  - `verweerder`
  - `getuige`
  - `arts`
  - `slachtoffer`
  - `minderjarige`
- over-masking risk where legal role structure becomes unreadable.

## Tests/checks run

Required local shell commands requested by the workpackage:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests
```

Result: not runnable in this environment. The container has no working GitHub network access for cloning the repository, so local pytest/py_compile execution could not be performed here.

Static repository checks completed through the GitHub connector:

- Confirmed the claim did not exist before starting, then created it.
- Read required control files: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Read relevant governance docs: `RISK_REGISTER.md`, `RELEASE_NOTES.md`, `DECISION_LOG.md`, `RECALL_BENCHMARK_SPEC.md`.
- Confirmed `RECALL_PRECISION_SCORECARD.md` and `RECALL_RESIDUAL_RISK_REPORT.md` are not present at repo root.
- Read active `presidio_streamlit.py` without changing it.
- Added and re-read `tests/test_dutch_legal_recall_gap_baseline.py` through the GitHub connector.

## Tests expected in new file

Expected normal passing tests:

- `test_synthetic_gap_fixture_contains_required_legal_references`
- `test_synthetic_role_fixture_contains_only_generic_role_words`

Expected xfail tests with `strict=False`:

- `test_known_gap_legal_reference_numbers_should_be_detectable`
- `test_known_gap_claim_reference_must_not_be_phone_number`
- `test_known_gap_client_dossier_and_zaak_numbers_should_be_detectable`
- `test_known_gap_rechtspraak_like_rolnummers_should_be_detectable`
- `test_known_gap_role_words_alone_should_not_be_detected_as_person_values`
- `test_known_gap_overmasking_should_not_remove_legal_role_structure`

Note: the new file contains 2 normal tests and 6 xfail tests. The scope asked for known gaps as xfail where current behavior is expected to be incomplete; this matches that goal.

## Validation status

- Tests/documentation-only changes completed.
- No product-code file was changed.
- No recognizer/pattern behavior was changed.
- Final execution should be verified by GitHub Actions because local execution was unavailable in this environment.

## GitHub Actions status

Unknown / not exposed through connector at handover time.

Details:

- `get_commit_combined_status` for commit `682f5b0e8b6e84d9bb4d2025d143682e26e4ddd6` returned no statuses.
- `fetch_commit_workflow_runs` for the same commit returned an empty workflow-run list.
- The connector may not expose push-triggered workflow runs in this setup.

## Hugging Face sync status

Unknown / not exposed through connector at handover time.

Expected app impact: none. This package added tests and internal documentation only.

## App verification status

Not required. This is tests/documentation-only and does not change app behavior.

## Remaining risks

- The tests were not executed locally in this environment.
- GitHub Actions/HF sync visibility was unavailable through the connector for these direct-push commits.
- The recorded gaps are not fixed yet; this package makes them visible and regression-testable only.
- A later pattern-fix package must be careful to preserve legal role/context words while detecting names and reference values.

## Next recommended step

Do not automatically start recognizer fixes.

Likely next workpackage only after separate coordinator approval:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES
```

Purpose of that later package would be to improve Dutch legal patterns, reduce misclassification, and convert selected xfail baseline tests into passing tests without weakening role/context preservation.
