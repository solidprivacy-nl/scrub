# Workpackage Claim — SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY`  
Issue: #86  
PR: #87  
Base main: `d5fcd8d6019f136e82877b646af2d085f9eb1720`  
Branch: `wp/premium-staged-workspace-decision`

## Goal

Freeze the coordinator-approved Premium Standard interaction architecture before production Streamlit integration continues in PR #85.

Binding direction:

```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

The three stage headers remain in one persistent page/workspace. Exactly one stage is expanded at a time; completed stages collapse to compact summaries; future stages remain visible but passive; successful completion auto-advances; deliberate return to an earlier stage is allowed; processing-affecting changes invalidate downstream state fail-closed.

## Scope

Planning, architecture, execution-order and contract-test changes only:

- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- `ROADMAP.md`;
- `WORKPACKAGES.md`;
- `CHANGELOG.md`;
- `DECISION_LOG.md`;
- `tests/test_premium_staged_workspace_decision.py`;
- issue/PR binding notes for active PR #85;
- this claim and the final handover.

## Explicit intervention in active Premium work

PR #85 is amended, not discarded. Its current `premium_app_shell.py` and `tests/test_premium_app_shell.py` helper work is reusable. Production `presidio_streamlit.py` integration must not proceed under a three-page or generic nested-expander interpretation; it must incorporate this staged-workspace decision after the decision candidate is independently assured and merged.

## Administrative finalization

The large historical control files were updated through temporary self-cleaning PR workflows so their existing history was prepended to, not replaced or truncated. Those workflows and temporary helper files removed themselves and are absent from the persistent PR diff.

Persistent candidate paths are:

- `CHANGELOG.md`;
- `DECISION_LOG.md`;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- `ROADMAP.md`;
- `WORKPACKAGES.md`;
- `tests/test_premium_staged_workspace_decision.py`;
- `workpackage_claims/scrub_wp_premium_staged_workspace_decision_freeze.md`;
- `handover/workpackages/20260808_1255_premium_staged_workspace_decision_freeze.md`.

## Safety boundary

No production Streamlit/UI behavior changes in this package. No recognizer, threshold, replacement, review-table authority, direct masking, export bytes/names/MIME, Scrub Key, reinsert, audit, document-processing, dependency, hosting or Hugging Face behavior changes.

Human review remains mandatory. Synthetic/test content only.

## Validation

One initial new-test assertion was overly literal about Markdown emphasis and produced `1 failed, 1189 passed` on run #2143. It was repaired without weakening the architecture contract.

Pre-final administrative candidate:

```text
GitHub Actions Tests run #2145 / ID 31253772414
python -m pytest -q tests
1190 passed in 12.23s
conclusion: success
```

After that run, only roadmap scope cleanup plus this claim/handover administration changed. A fresh normal full `Tests` run on the exact final PR head is mandatory before assurance may treat this claim as machine-evidence-complete. No further candidate edits are permitted after that exact-head run unless the candidate returns to implementation for repair.

- Hugging Face sync: `NOT APPLICABLE` — no runtime/deployment files changed.
- App verification: `NOT APPLICABLE` — no live UI behavior changed.
- Independent `governance_release_assurance`: `REQUIRED` before merge.

Implementation does not self-certify or self-merge.