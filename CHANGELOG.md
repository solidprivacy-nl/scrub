# Changelog — SolidPrivacy Scrub

## WP_RECALL_GOLD_LABEL_CORPUS_SEED — Add synthetic gold-label corpus seed

Status: completed as benchmark/data/documentation-only.

Files added:

- `corpus/README.md`
- `corpus/legal/legal_reference_seed_001.txt`
- `corpus/legal/legal_reference_seed_001.gold.json`
- `corpus/legal/legal_role_preservation_seed_001.txt`
- `corpus/legal/legal_role_preservation_seed_001.gold.json`
- `corpus/care/care_reference_seed_001.txt`
- `corpus/care/care_reference_seed_001.gold.json`
- `tests/test_recall_gold_label_corpus_seed.py`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md`
- `handover/workpackages/20260617_0816_recall_gold_label_corpus_seed.md`

Files changed:

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md`

Summary:

- Added a first synthetic gold-label corpus seed for future recall/precision benchmarking.
- Added legal reference, legal role-preservation and care reference seed texts.
- Added `.gold.json` sidecars with exact offsets, labels, preserve terms and known traps.
- Added tests-only sidecar integrity checks for valid JSON, synthetic flag, source-file existence, offset matching, required label fields, preserve-term matching, reserved `.example.test` email domains and role-word preservation.
- Updated the recall/precision scorecard to record that a gold-label seed now exists, while quantitative recall/precision is still pending a runner.

Tests/checks:

- Local tests were not runnable in this environment because the container cannot clone/access GitHub for a local working tree.
- Required test commands remain:
  - `python -m pytest -q tests/test_recall_gold_label_corpus_seed.py`
  - `python -m py_compile presidio_streamlit.py`
  - `python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py`
- GitHub Actions and Hugging Face sync should be used as final execution proof for the documentation/data commits.

Intentionally not changed:

- No product code change.
- No `candidate_scanner.py` change.
- No `dutch_recognizers.py` change.
- No `presidio_streamlit.py` change.
- No recognizer/pattern fix.
- No UI change.
- No review table change.
- No side-by-side change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No DOCX/PDF flow change.
- No Docker/startup/dependency change.
- No cloud processing.
- No real personal data.
- No benchmark runner implementation.

Remaining gaps:

- The seed corpus is intentionally small.
- No benchmark runner exists yet.
- No formal recall/precision threshold exists yet.
- No production-blocking benchmark gate exists yet.
- Quantitative recall/precision remains future work.

Next recommended step:

- Do not automatically start another pattern-fix round.
- Consider `WP_RECALL_BENCHMARK_RUNNER_MINIMAL` after separate approval if quantitative measurement is now desired.
- Consider `WP_RECALL_GOLD_LABEL_CORPUS_EXPAND` after separate approval if more corpus coverage is desired first.
- Consider `WP_DOCX_HYGIENE_RECALL_FOLLOWUP` if document/export risks now dominate.

## WP_RECALL_SCORECARD_REFRESH — Refresh recall/precision scorecard after Dutch legal fixes

Status: completed as benchmark/documentation-only.

Files added:

- `RECALL_PRECISION_SCORECARD.md`
- `workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md`
- `handover/workpackages/20260617_0112_recall_scorecard_refresh.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md`

Summary:

- Added `RECALL_PRECISION_SCORECARD.md` because no scorecard file existed at repo root.
- Refreshed Dutch legal recall/precision status after the gap tests, first pattern-fix round and verify closeout.
- Recorded coverage for the documented legal reference values, CLM/phone-number risk, role-word preservation and over-masking guard.
- Clarified that the improvement is review-candidate visibility, not a complete automatic-recognition guarantee.
- Recorded that no immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` is recommended unless concrete new misses are observed.

## WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — Verify Dutch legal recall pattern fixes

Status: completed after coordinator Actions/HF/app verification evidence.

Summary:

- Verified the implementation scope by comparing the pattern-fix commit range: product/helper code change is limited to `candidate_scanner.py`; tests changed in `tests/test_dutch_legal_recall_gap_baseline.py`; no `presidio_streamlit.py` product-code change was part of the pattern-fix range.
- Verified the candidate scanner keeps the new case-number-shaped scan context-bound and value-only.
- Verified the Dutch legal recall baseline now contains normal assertions for legal references, client/dossier/zaak references, CLM reference not as phone, role-word preservation and over-masking prevention.
- Coordinator screenshot evidence shows `Tests #1115` and `Sync to Hugging Face Space #1116` green for commit `e1e44b3`.
- Coordinator app screenshot confirms the Hugging Face Space runs without Script execution error and the review/export flow remains visible.

## WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — Improve Dutch legal reference detection

Status: completed as a targeted helper-level detection improvement.

Summary:

- Improved the Dutch Legal candidate scanner for reference-like values that should be surfaced in the review/replacement table when recognizers miss them.
- Added context-bound case-number scanning for values with spaces, including numeric court role references and `ARN 26/4412`-style references.
- Broadened safe context cues for `client`, `cliënt`, `camera`, `incident`, `reparatie`, `rolnummer` and `rolnr`.
- Converted the Dutch legal recall baseline from `xfail(strict=False)` gap documentation to direct helper-level passing assertions for the first fixed round.
- No `presidio_streamlit.py`, UI, export, Scrub Key or reinsert behavior changed.

## WP_DUTCH_LEGAL_RECALL_GAP_TESTS — Add tests for known Dutch legal recall gaps

Status: completed as tests/documentation-only baseline.

Summary:

- Added a tests-only baseline for known Dutch legal recall and precision gaps.
- Used synthetic legal text only.
- Captured known gaps for legal reference numbers, Rechtspraak-like rolnummers, client/dossier/zaak numbers, legal-code misclassification, role-word preservation and over-masking risk.
- Used `pytest.mark.xfail(..., strict=False)` for current known gaps so CI could remain green while the shortcomings stayed visible before the pattern-fix round.

## WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — Remove temporary candidate artifacts

Status: completed as repo-hygiene cleanup after verified promotion.

Summary:

- Removed temporary candidate/helper files after the collapsible review table was promoted, tested and app-verified.
- Active app behavior is unchanged.
- The collapsible review-table behavior remains in `presidio_streamlit.py`.
- Review table source-of-truth controls remain preserved.

## Recent previous entries

Detailed previous history remains available in Git history and includes:

- WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — verified promoted collapsible review table.
- WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — contract tests for collapsible review table section.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — repaired stale review surface control assertions.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP — simplified side-by-side review controls.
- WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — consolidated preview surfaces and Dutch legal sample.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — production integration of synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
