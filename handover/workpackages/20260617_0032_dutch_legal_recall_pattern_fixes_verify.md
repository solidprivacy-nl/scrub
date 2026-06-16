# Handover — WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — Verify Dutch legal recall pattern fixes after implementation`

Status: completed as verification/closeout-only with validation limitations.

## Summary

Verified the Dutch legal recall pattern-fix package through GitHub connector/static checks and commit comparison. No product code, recognizer code, UI, export, Scrub Key, reinsert, Docker/startup or dependency changes were made in this verify package.

The implementation being verified remains narrow: the only product/helper code changed by the pattern-fix package is `candidate_scanner.py`, with tests updated in `tests/test_dutch_legal_recall_gap_baseline.py`.

## Files added

- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md`
- `handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md` pending final closeout update after this handover file

## Product-code changes in this verify package

None.

## Verified pattern-fix commit SHA

- `77090c5d7cba75bc30d49a77a56116e37a78b0fc` — candidate scanner helper change.
- `440bd27c4e02006c231fbb61a38567a8635d783f` — Dutch legal recall baseline test conversion.
- Pattern-fix closeout claim commit: `5345912f62e83ea49d55884c6b4bd6c5da50d5f2`.

## Verification performed

Static/connector verification:

- Confirmed `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES` has `status: completed`.
- Confirmed the changed production/helper code is limited to `candidate_scanner.py`.
- Confirmed `candidate_scanner.py` adds context-bound case-number-shaped candidate detection and extra context cues.
- Confirmed candidate scanning remains value-only and review/audit-layer oriented.
- Confirmed `tests/test_dutch_legal_recall_gap_baseline.py` includes required synthetic legal references and role words.
- Confirmed the baseline has normal asserts and no `pytest.mark.xfail` markers for the first fixed round.
- Confirmed `CLM-2026-112233` is tested as not `PHONE` in returned entity types.
- Confirmed existing review/export contract tests still assert review-table, side-by-side and download boundaries.
- Confirmed `presidio_streamlit.py` was not changed by the pattern-fix package and still imports the candidate scanner into the existing review table candidate flow.

## Tests/checks run

Required local checks attempted:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

Result: not runnable locally in this environment. The container cannot resolve `github.com`, so it cannot clone the repository for local execution.

Connector checks:

- `get_commit_combined_status` returned no statuses for checked pattern-fix commits.
- `fetch_commit_workflow_runs` returned empty workflow-run lists for checked pattern-fix commits.
- Public web lookup for GitHub Actions/Hugging Face was unavailable in this environment.

## GitHub Actions status

Unknown from this worker. No statuses/workflow runs were exposed through the connector for the checked commits.

## Hugging Face sync status

Unknown from this worker. Sync could not be confirmed green.

## App verification status

Not performed. The workpackage requested light app verification only if Hugging Face sync is green. HF sync could not be confirmed green from this environment.

## Fixed gaps verified

Static verification confirms test and helper coverage for:

- Legal reference values including Rechtspraak-like case/role references.
- Client/dossier/zaak references in synthetic test text.
- CLM reference not being accepted as a phone-number entity in the baseline assertion.
- Generic legal role words not being detected as person values in the baseline assertion.
- Over-masking guard that keeps legal role structure readable.

## Remaining gaps

- No local pytest execution evidence from this worker.
- No GitHub Actions/HF sync evidence from this worker.
- No live app verification from this worker.
- The implemented fix improves review-candidate visibility, not complete automatic recognizer classification for every Dutch legal reference type.

## Remaining risks

- CI or runtime may still expose issues that static review cannot catch.
- Helper-level candidate surfacing requires human review; candidates are not automatically applied.
- Broader recall/precision scorecard and gold-label corpus work remain future work.

## Next recommended step

Do not automatically start a new pattern-fix round.

If the coordinator can verify GitHub Actions/HF sync externally, record that evidence only. If remaining gaps appear after real test/app verification, use a separately approved:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2
```

Alternative later option after approval:

```text
WP_RECALL_SCORECARD_REFRESH
```
