# Assurance request — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY

Status: ready_for_independent_assurance  
Implementation role: `implementation_operations`

A fresh `governance_release_assurance` worker must independently inspect the exact candidate branch/PR before merge.

Required checks:

1. Existing `push` on `main`, `pull_request`, and `workflow_dispatch` triggers remain present.
2. No path filters exclude administrative closeout commits.
3. Added `workflow_run` carrier is limited to `Diagnostic recall benchmark report`.
4. The Tests job accepts carrier events only for `run_attempt > 1` and carrier conclusion `success`.
5. `actions/checkout@v4` has no ref override, preserving the default-branch SHA supplied by `workflow_run`.
6. The command remains exactly `python -m pytest -q tests`.
7. Carrier workflow is artifact-only and does not mutate repository/product/Hugging Face state.
8. No product/runtime/UI/export/Scrub-Key/reinsert semantics changed.
9. Focused contract validation is `4 passed in 0.03s`.

Implementation must not self-certify or self-merge this candidate.