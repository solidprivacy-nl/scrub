# Handover — WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — Verify Dutch legal recall pattern fixes after implementation`

Status: completed after coordinator Actions/HF/app verification evidence.

## Summary

Verified the Dutch legal recall pattern-fix package through GitHub connector/static checks and commit comparison. The coordinator then supplied external evidence that Actions, Hugging Face sync and a live app smoke check are green. No product code, recognizer code, UI, export, Scrub Key, reinsert, Docker/startup or dependency changes were made in this verify package.

The implementation being verified remains narrow: the only product/helper code changed by the pattern-fix package is `candidate_scanner.py`, with tests updated in `tests/test_dutch_legal_recall_gap_baseline.py`.

## Files added

- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md`
- `handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md`
- `handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md`

## Product-code changes in this verify package

None.

## Verified pattern-fix commit SHA

- `77090c5d7cba75bc30d49a77a56116e37a78b0fc` — candidate scanner helper change.
- `440bd27c4e02006c231fbb61a38567a8635d783f` — Dutch legal recall baseline test conversion.
- Pattern-fix closeout claim commit: `5345912f62e83ea49d55884c6b4bd6c5da50d5f2`.
- Verify closeout commit checked by coordinator: `e1e44b3cb664f913414ed80baa6086cf207d67f0`.

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

Coordinator external verification evidence:

- GitHub Actions `Tests #1115` for commit `e1e44b3` completed successfully.
- `Sync to Hugging Face Space #1116` for commit `e1e44b3` completed successfully.
- Earlier `Sync to Hugging Face Space #1112` for commit `ca5cb3f` failed, but was superseded by later green sync evidence.
- Hugging Face app screenshot shows the Space running without Script execution error.
- App screenshot confirms `2. Controleer de tekst` and side-by-side review remain visible.
- App screenshot confirms `3. Controleer gevonden gegevens` remains visible.
- App screenshot confirms collapsed `Vervangtabel controleren — 16 items` remains visible.
- App screenshot confirms Serial review, export/download buttons and DOCX hygiene audit remain visible.

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
- Coordinator screenshot evidence was used as external source of truth for Actions and Hugging Face status.

## GitHub Actions status

Green by coordinator screenshot evidence:

- `Tests #1115` for commit `e1e44b3` succeeded.

## Hugging Face sync status

Green by coordinator screenshot evidence:

- `Sync to Hugging Face Space #1116` for commit `e1e44b3` succeeded.

## App verification status

Confirmed by coordinator screenshot evidence.

Verified visible in the live app:

- Space running without Script execution error.
- `2. Controleer de tekst` side-by-side review.
- `3. Controleer gevonden gegevens`.
- Collapsed `Vervangtabel controleren — 16 items`.
- Serial review.
- Export/download buttons.
- DOCX hygiene audit.

## Fixed gaps verified

Static verification and green CI evidence confirm test/helper coverage for:

- Legal reference values including Rechtspraak-like case/role references.
- Client/dossier/zaak references in synthetic test text.
- CLM reference not being accepted as a phone-number entity in the baseline assertion.
- Generic legal role words not being detected as person values in the baseline assertion.
- Over-masking guard that keeps legal role structure readable.

## Remaining gaps

- The implemented fix improves review-candidate visibility, not complete automatic recognizer classification for every Dutch legal reference type.
- Broader recall/precision scorecard and gold-label corpus work remain future work.

## Remaining risks

- Helper-level candidate surfacing requires human review; candidates are not automatically applied.
- Broader recall/precision scorecard and gold-label corpus work remain future work.
- A later app/user test may still identify new Dutch legal patterns that need a separate approved round.

## Next recommended step

Do not automatically start a new pattern-fix round.

No immediate extra pattern round is required based on current coordinator verification evidence. If remaining gaps appear after real test/app usage, use a separately approved:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2
```

Alternative later option after approval:

```text
WP_RECALL_SCORECARD_REFRESH
```
