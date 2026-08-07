# Status addendum — issue #70 Actions recovery

Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`

This addendum records that the final technical candidate replaces the earlier issue-comment fallback with the more deterministic `workflow_run` carrier mechanism.

Final technical files:

- `.github/workflows/tests.yml` — adds `workflow_run` for `Diagnostic recall benchmark report`, gated to successful reruns (`run_attempt > 1`);
- `tests/test_issue70_actions_evidence_recovery_workflow.py` — freezes push/main, pull_request, workflow_dispatch, no path filters, carrier gate, default-branch checkout, and unchanged full-suite command;
- `ISSUE70_ACTIONS_EVIDENCE_RECOVERY.md` — implementation-side evidence contract.

Focused validation: `4 passed in 0.03s`.

Safe carrier: run ID `27715364089`, job ID `81986778399`.

No product/runtime/UI/export/Scrub-Key/reinsert/Hugging-Face behavior changed. Independent assurance remains mandatory before merge.