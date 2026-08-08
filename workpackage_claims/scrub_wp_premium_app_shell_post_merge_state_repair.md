# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Parent governance gate: issue #96  
Implementation issue: #98  
PR: #99  
Branch: `wp/premium-app-shell-post-merge-state-repair`  
Status: `RELEASE_CANDIDATE_READY` only if the exact-head full-suite run triggered by this final repository mutation is green

## Reproduced defect class

The concrete issue #92 post-merge findings were independently reproduced on current main before implementation:

- Expert could use demo fallback text instead of the current Standard source merely because presentation mode changed.
- Expert did not reliably reuse the current-generation analysis cache or restore the authoritative reviewed working set.

Because these findings reproduced, issue #96 cannot be reconciled by treating the old #93 PASS as sufficient. A repaired candidate is required.

## Implemented repair

The PR #99 candidate now:

- hydrates one authoritative source text and uploaded-file context across Standard and Expert;
- reuses current-generation analysis in both presentation modes;
- binds cached review rows to the deterministic processing generation;
- restores and persists the same authoritative review working set in both modes;
- keeps presentation-only Standard↔Expert switching from changing source/generation/analysis/review state;
- invalidates completed Review/Download lineage when a user actually changes the reviewed working set, while preserving current source/processed lineage;
- clears stale analysis and review caches on real source/processing-generation changes;
- preserves the existing fail-closed boundary for unsupported Expert-only operators in Standard.

## Regression coverage

New and updated tests cover:

- completed Standard Review/Download → Expert → Standard without source or lineage drift;
- current-generation analysis reuse in Expert;
- generation-bound authoritative review-row restoration;
- real review decision change detection including NaN-containing rows;
- fail-closed Review/Download invalidation after a real review change;
- stale review/analysis cache clearing after a real processing-generation change;
- source-level integration invariants proving the removed Standard-only cache/source paths do not return.

Pre-administration evidence:

```text
Tests #2247 / run 31272188513
job 93139919879
branch head: 69fde971783aa20d5cbcb2c13cd8a8538fa1ebe4
base main: 4130976b7d9489de148dd17234faff4a18fad2f0
PR merge candidate: 65ca1ab73f03a2513a2004d49f190c2a233d261e
python -m pytest -q tests
1240 passed in 9.65s
conclusion: success
```

## Protected semantics

No intended changes to:

- recognizers or profile rules;
- threshold meaning;
- authoritative include/review decisions;
- direct manual or processed-text masking semantics;
- export bytes, filenames or MIME types;
- Scrub Key schema, document binding, warnings or lifecycle;
- TXT/DOCX reinsert behavior;
- audit semantics;
- dependencies;
- local/cloud document-processing boundary;
- mandatory human review.

## Final candidate identity boundary

**This claim update is the final repository mutation before exact-head CI.**

The commit created by this update becomes the only candidate head eligible for release assurance. From this point onward:

- do not modify repository content unless assurance returns the candidate to implementation for repair;
- run the full GitHub Actions regression suite on this exact head / resulting PR merge candidate;
- record final exact-head SHA, merge-candidate checkout, run/job/result and current base main in PR #99 and issue #98 metadata only;
- metadata updates must not mutate repository content;
- a changed head invalidates any prior assurance evidence.

## Governance

Implementation does not self-certify and does not self-merge. PR #99 requires a new independent `governance_release_assurance` reviewer working under the blind-review boundary. Issue #96 remains open until the repaired runtime is independently PASSed, merged, exact-main/deployment evidence is green and the App Shell outcome is independently closed. Premium Input Stage remains blocked.