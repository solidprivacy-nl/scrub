# Handover — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR

- Repository worked in: `solidprivacy-nl/scrub`
- Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR — preserve source, analysis and review state across Standard↔Expert`
- Role: `implementation_operations`
- Parent governance gate: issue #96
- Implementation issue: #98
- Pull request: #99
- Status: `IMPLEMENTATION_IN_PROGRESS` until the final exact-head full-suite run is green and a fresh independent assurance reviewer issues a verdict

## Files added/changed

Runtime/state:
- `premium_streamlit_state.py`
- `presidio_streamlit.py`

Tests:
- `tests/test_premium_cross_mode_runtime_state.py`
- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `tests/test_premium_app_shell_streamlit_integration.py`

Administration:
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- this handover
- `workpackage_claims/scrub_wp_premium_app_shell_post_merge_state_repair.md` will be the final repository mutation before exact-head CI

## Repair summary

The concrete post-merge findings from issue #92 were independently reproduced by `implementation_operations` on current main before repair:

1. Expert could initialize source text from the demo fallback instead of deterministically hydrating the current Standard source.
2. Expert did not reliably reuse the current-generation analysis cache and could reconstruct review state instead of restoring the authoritative reviewed working set.

The repair:
- makes source text and current uploaded-file context presentation-neutral;
- reuses current-generation analysis in both Standard and Expert;
- generation-binds authoritative review rows;
- restores and persists those rows in both Standard and Expert;
- invalidates completed Review/Download lineage if the reviewed working set is genuinely changed, while preserving source/processed lineage;
- clears stale analysis/review caches fail-closed after a real processing-generation change;
- preserves the existing Standard block for unsupported Expert-only operators rather than silently coercing them.

## Tests

Pre-administration full-suite evidence:
- GitHub Actions Tests #2247 / run `31272188513`
- job `93139919879`
- branch head under test: `69fde971783aa20d5cbcb2c13cd8a8538fa1ebe4`
- tested PR merge candidate: `65ca1ab73f03a2513a2004d49f190c2a233d261e`
- base main: `4130976b7d9489de148dd17234faff4a18fad2f0`
- command: `python -m pytest -q tests`
- result: `1240 passed in 9.65s`
- conclusion: success

Final post-administration exact-head full-suite evidence is intentionally pending at handover-write time. It must be recorded in PR #99 / issue #98 metadata after the final claim commit, without further repository mutation.

## Validation status

- Source hydration defect: reproduced and repaired in candidate.
- Current-generation analysis cache bypass: reproduced and repaired in candidate.
- Review working-set reconstruction gap: reproduced and repaired in candidate.
- Presentation-only Standard↔Expert roundtrip: covered by new cross-mode state tests.
- Real reviewed-working-set change: covered as fail-closed Review/Download invalidation.
- Real source/processing generation change: covered as fail-closed cache/downstream invalidation.
- Protected export, Scrub Key and reinsert semantics: intentionally unchanged by this workpackage.

## GitHub Actions status

Pre-administration candidate is green. Final exact-head full-suite run remains mandatory after the implementation claim becomes the final repository commit.

## Hugging Face sync status

Not applicable before merge. PR #99 is not authorized for deployment. If independently PASSed and merged, the exact runtime merge commit must be synchronized and verified on Hugging Face.

## App verification status

Pending and blocked. Do not ask the coordinator to test the app until the repaired runtime is independently PASSed, merged and synchronized.

## Remaining risks

- The previously merged App Shell remains governance-unconfirmed while issue #96 is open.
- Fresh independent assurance must reconstruct PR #99 without relying on this implementation handover or claim before its initial verdict.
- Any repository-head movement after final exact-head assurance evidence invalidates the reviewed candidate identity.
- Premium Input Stage remains blocked until the repaired App Shell and issue #96 outcome are independently closed.

## Next recommended step

Create the implementation claim as the final repository mutation, run full exact-head GitHub Actions, freeze the resulting head, then route PR #99 to a new blind `governance_release_assurance` worker. Do not self-certify, self-merge or start Premium Input Stage.