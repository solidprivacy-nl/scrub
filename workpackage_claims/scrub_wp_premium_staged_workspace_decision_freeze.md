# Workpackage Claim — SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Status: `IMPLEMENTATION_IN_PROGRESS`  
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
- claim and handover administration.

## Explicit intervention in active Premium work

PR #85 is amended, not discarded. Its current `premium_app_shell.py` and `tests/test_premium_app_shell.py` helper work is reusable. Production `presidio_streamlit.py` integration must not proceed under a three-page or generic nested-expander interpretation; it must incorporate this staged-workspace decision after the decision candidate is independently assured and merged.

## Administrative finalization

The large historical control files were updated through a temporary self-cleaning PR workflow so their existing history was **prepended to, not replaced or truncated**. The temporary workflow and prefix helper files removed themselves in the same administrative commit and are absent from the PR diff.

Final persistent candidate paths are limited to:

- `CHANGELOG.md`;
- `DECISION_LOG.md`;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- `ROADMAP.md`;
- `WORKPACKAGES.md`;
- `tests/test_premium_staged_workspace_decision.py`;
- this claim;
- final handover when written.

The first PR test runs before administrative finalization are not release evidence because the exact tested heads did not yet contain the new WORKPACKAGES/CHANGELOG/DECISION_LOG records. A connector-originated claim update is used to obtain a normal PR-triggered full regression on the complete candidate tree.

## Safety boundary

No production Streamlit/UI behavior changes in this package. No recognizer, threshold, replacement, review-table authority, direct masking, export bytes/names/MIME, Scrub Key, reinsert, audit, document-processing, dependency, hosting or Hugging Face behavior changes.

Human review remains mandatory. Synthetic/test content only.

## Validation plan

- documentation contract tests freeze staged-workspace semantics and execution order;
- full GitHub Actions regression on the exact PR candidate;
- fresh independent `governance_release_assurance` decision required before merge;
- Hugging Face sync: not applicable because no runtime files change;
- app verification: not applicable because no live UI behavior changes.

Implementation does not self-certify or self-merge.