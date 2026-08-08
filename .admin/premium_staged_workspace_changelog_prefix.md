## 2026-08-08 Europe/Amsterdam — SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — staged workspace architecture candidate

Status: `IMPLEMENTATION_IN_PROGRESS`; exact-head CI and independent assurance required before merge.

Purpose:
- convert the coordinator-approved first-principles comparison of three routed screens versus a one-page staged workspace into a binding Premium UI architecture decision;
- intervene before PR #85 enters production `presidio_streamlit.py` integration;
- make the Premium staged-workspace sequence the authoritative active execution queue.

Decision:
```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

Binding Standard behavior:
- all three stage headers remain in one persistent page/workspace;
- exactly one stage is expanded/dominant at a time;
- completed stages collapse to compact status summaries;
- future stages remain visible but passive;
- successful completion auto-advances to the next stage;
- deliberate return to an earlier stage remains possible;
- processing-affecting earlier changes invalidate processed/review/export lineage fail-closed;
- three separate routed pages are rejected for these core stages;
- a classic nested-expander form is also rejected as the default Standard pattern.

First-principles rationale:
- Scrub is an iterative document-review workflow, not a strictly linear checkout;
- the interface should represent document state rather than page navigation;
- the staged workspace preserves one-task-at-a-time focus while retaining document identity, progress, correction context and visible trust state;
- it aligns directly with the merged `premium_core_flow_state.py` generation/invalidation model and reduces routing/state-restoration complexity in Streamlit.

Current PR #85 consequence:
- PR #85 is amended, not discarded;
- current pure `premium_app_shell.py` helper work remains reusable;
- production Streamlit integration is gated until this decision is independently assured and incorporated;
- PR #85 must add/test completed/future/active panels, compact summaries, auto-progression hooks, prior-stage return/edit and no-three-page semantics before production integration.

Files added/changed in the candidate:
- added `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- updated `ROADMAP.md`;
- updated `WORKPACKAGES.md` with an authoritative current Premium queue while retaining older content as historical records;
- updated `DECISION_LOG.md` with D043;
- updated `CHANGELOG.md`;
- added `tests/test_premium_staged_workspace_decision.py`;
- added implementation claim and handover administration.

Validation boundary:
- documentation/architecture/contract-only package;
- no production Streamlit or runtime product behavior changes;
- no recognizer, threshold, replacement, review authority, export bytes/names/MIME, Scrub Key, reinsert, audit, dependency or Hugging Face behavior changes;
- Hugging Face sync: not applicable;
- app verification: not applicable;
- exact-head GitHub Actions and independent `governance_release_assurance` remain required before merge.

---

