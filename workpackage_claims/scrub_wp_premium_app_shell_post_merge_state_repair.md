# Workpackage Claim — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_STATE_REPAIR

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #98  
PR: #99  
Parent governance conflict: #96  
Status: `IMPLEMENTATION_VALIDATION`

## Scope

Repair only the reproduced post-merge App Shell cross-mode state defects:

- preserve authoritative source text/file context across `Standaard ↔ Expert` presentation switches;
- reuse current-generation analysis across both presentation modes;
- preserve a generation-bound authoritative review working set across both modes;
- invalidate downstream review/download lineage fail-closed only when source, processing settings, or review decisions genuinely change.

## Safety boundary

No intended changes to recognizers/profile rules, threshold meaning, review-table/include authority, direct masking, export bytes/names/MIME, Scrub Key, reinsert, audit, dependencies, local/cloud processing boundary, or mandatory human review.

## Execution-continuity note — 2026-08-08 20:42 Europe/Amsterdam

The implementation/admin branch reached bot-authored head `61af4d45f624e663bd9f13ba68cb1b9a15362d3f`; its PR-triggered Tests and evidence-carrier events ended `action_required` before useful exact-head execution. This claim commit is a semantics-neutral repository-user event to obtain executable CI for the resulting current head. The new head produced by this commit supersedes `61af4d45…` for all later validation and assurance.

Implementation does not self-certify or self-merge. Fresh exact-head full regression and independent `governance_release_assurance` remain mandatory before merge. Premium Input Stage remains blocked while issue #96 is open.
