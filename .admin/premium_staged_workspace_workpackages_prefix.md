# SolidPrivacy Scrub — Current authoritative execution queue

> **Current status override — 2026-08-08 Europe/Amsterdam**  
> This section is the authoritative current execution queue. Older queue/status sections retained below are historical records and must not override this section.

## Premium UI priority

The coordinator has explicitly prioritized the Premium interface. The active Standard target is a **single-page staged document workspace**, not three separate routed core-flow pages and not a long form with nested expanders.

Binding principle:

```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

All three stage headers remain present in one workspace. Exactly one stage is expanded/dominant at a time. Completed stages collapse to compact summaries, future stages remain visible but passive, successful completion auto-advances, and explicit return to an earlier stage is allowed. Processing-affecting earlier changes invalidate downstream state fail-closed.

Governing design:
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- merged `premium_core_flow_state.py` state invariants;
- ROADMAP Premium core-flow section.

Historical prerequisites now completed:
- `SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN` — planning completed;
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION` — independent governance gate closed;
- `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT` — merged through PR #80;
- `SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL` — merged through PR #82.

### 1. SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — urgent architecture gate

Status: `IMPLEMENTATION_IN_PROGRESS` until exact-head CI and independent assurance.  
Role: `implementation_operations`  
Issue: #86  
Dependency: merged PR #80 UI contract + merged PR #82 state model.  
Parallelization: documentation/contract-only; production Streamlit integration in PR #85 must wait for this decision to be incorporated.

Goal:
- freeze the approved staged-workspace interaction model before the active App Shell package enters `presidio_streamlit.py`;
- remove ambiguity between three routed screens versus one persistent staged workspace;
- make the Premium line the dominant execution queue.

Required output:
- detailed first-principles design decision;
- roadmap realignment;
- this authoritative workpackage queue;
- changelog and decision-log record;
- contract tests;
- explicit binding note on issue #84 / PR #85;
- implementation claim and handover.

Acceptance:
- Standard explicitly means one persistent page/workspace with three persistent stage headers;
- exactly one stage exposes its full surface at a time;
- completed stages summarize, future stages remain passive;
- successful stage completion advances automatically;
- explicit prior-stage return is allowed;
- processing-affecting changes invalidate downstream state;
- three isolated routed pages are rejected for the Standard core flow;
- nested core-flow expanders are rejected as the default Standard pattern;
- no runtime/UI product semantics change in this package;
- exact-head GitHub Actions passes;
- fresh independent `governance_release_assurance` is required before merge.

Intentionally excluded:
- recognizers, thresholds, replacement logic, review authority;
- export bytes/names/MIME;
- Scrub Key/reinsert/audit semantics;
- production Streamlit integration;
- dependencies, runtime, deployment or Hugging Face behavior.

### 2. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — active draft PR #85, amended

Status: active draft; **production integration gated by package 1**.  
Issue: #84  
PR: #85  
Dependency: `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` merged after independent PASS.

Existing reusable work:
- `premium_app_shell.py` presentation primitives;
- `tests/test_premium_app_shell.py`;
- top-level `Anonimiseren | Terugzetten` labels;
- global `Standaard | Expert` labels;
- stage labels and one-active-stage primitive;
- Standard sidebar-hidden / Expert sidebar-available primitive.

Required before production integration:
- model active / completed / future stage presentation explicitly;
- compact completed-stage summary contract;
- passive future-stage contract;
- automatic progression hooks from Add → Review → Download;
- explicit prior-stage return/edit affordance;
- no routed-page interpretation for the three anonymization stages;
- no generic nested-expander hierarchy in Standard;
- bind to `premium_core_flow_state.py` lineage/invalidation rules.

Production integration acceptance:
- integrate the staged shell in the existing Streamlit application without changing processing semantics;
- all three stage headers remain persistently represented;
- exactly one stage is dominant;
- no permanent Standard configuration sidebar;
- no stale review/export remains presented as current;
- current review table/include authority, direct masking, export, Scrub Key, reinsert and audit semantics remain intact;
- full exact-head regression green;
- independent assurance PASS before merge.

Do not merge PR #85 merely because helper tests are green.

### 3. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION

Status: queued after App Shell PASS/merge.  
Dependency: package 2 merged.  
Shared UI rule: sequential; do not edit `presidio_streamlit.py` in parallel with another Premium production package.

Goal:
- make `Toevoegen` feel like one clear acquisition task rather than a settings form.

Target Standard surface:
- upload document OR paste text through one coherent source surface;
- essential recognition profile/context visible and understandable;
- one dominant action: `Document verwerken`;
- nonessential tuning hidden or moved to Expert/secondary disclosure;
- source identity survives into the compact completed-stage summary.

Acceptance:
- no duplicate input surfaces;
- no forest of default-open settings;
- one dominant processing action;
- profile never changes silently;
- ingestion, recognizer selection and processing semantics unchanged;
- processing-affecting edits invalidate downstream state;
- full regression + independent assurance before merge;
- live app verification after deployment because UI behavior changes.

### 4. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION

Status: queued after Input Stage PASS/merge.  
Dependency: package 3.  
Conflict boundary: exclusive ownership of shared review/Streamlit surfaces while active.

Goal:
- make `Controleren` the main document-review workspace rather than a collection of helper panels.

Target Standard surface:
- source and processed/checked text form the dominant review surface;
- direct missed-value masking remains accessible where the user notices a miss;
- review table remains authoritative source of truth and fallback, but not necessarily the visually dominant first surface;
- technical filters, diagnostics and tuning move out of the primary hierarchy;
- one dominant completion action: `Controle afronden`.

Acceptance:
- mandatory human review is not weakened;
- include/exclude state remains authoritative;
- direct masking produces normal document-bound manual rows;
- no recognizer/export/Scrub Key/reinsert semantic drift;
- compact completed review summary is trustworthy and nontechnical;
- full regression + independent assurance before merge;
- live app verification required.

### 5. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION

Status: queued after Review Stage PASS/merge.  
Dependency: package 4.  
Conflict boundary: exclusive ownership of shared export/Streamlit surfaces while active.

Goal:
- make `Downloaden` end with one obvious recommended cleaned-document action instead of multiple equal-weight download controls.

Target Standard surface:
- one dominant recommended document download selected only from already eligible outputs;
- alternate formats secondary;
- Scrub Key clearly separated as sensitive restoration material;
- audit/residual-risk evidence accessible but secondary;
- one dominant action: `Document downloaden`.

Acceptance:
- export bytes, eligibility, filenames and MIME types unchanged;
- Scrub Key lifecycle/warning/binding unchanged;
- audit evidence not removed;
- current-generation guard prevents stale downloads;
- full regression + independent assurance before merge;
- live app verification required.

### 6. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION

Status: queued after Export Stage PASS/merge.  
Dependency: packages 2–5.

Goal:
- prove that Standard removes visual complexity without removing capability or safety.

Required evidence:
- Standard ↔ Expert presentation switch preserves valid source/review state;
- presentation-only changes do not reprocess;
- processing-affecting Expert changes invalidate downstream lineage correctly;
- all advanced review, audit and troubleshooting capabilities remain available where intended;
- no review/export/Scrub Key/reinsert capability is silently lost;
- Standard cannot expose stale current-looking output.

Acceptance:
- deterministic parity/regression tests;
- full suite green;
- independent assurance PASS.

### 7. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT

Status: final queued Premium gate.  
Dependency: packages 2–6 independently passed and merged.

Goal:
- verify the deployed Premium Standard flow end-to-end in the actual app.

Required live acceptance:
1. first impression is a task workspace, not a long form;
2. `Toevoegen`, `Controleren`, `Downloaden` remain visibly the workflow structure;
3. only one stage is fully open at once;
4. successful completion auto-advances;
5. completed stages collapse into compact meaningful summaries;
6. future stages remain passive and non-competing;
7. returning to an earlier stage is obvious;
8. stale downstream state is invalidated visibly and safely;
9. one dominant primary action per active stage;
10. Standard has no permanent configuration sidebar;
11. review remains sufficient for mandatory human review;
12. one recommended cleaned-document download dominates the final stage;
13. Scrub Key, alternate formats and audit remain accessible but secondary;
14. no nested-expander form hierarchy replaces the old long form;
15. no recognizer/export/Scrub Key/reinsert/audit semantics changed unintentionally.

Validation:
- exact GitHub Actions evidence;
- GitHub → Hugging Face synchronization for the exact runtime candidate;
- runtime health/smoke evidence;
- coordinator/user subjective UX verification;
- final governance closeout.

## Binding execution order

```text
SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE
→ SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION
→ SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
→ SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
→ SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
→ SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
→ SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

Safety/coordination rule:
- **do not run the shared Streamlit UI packages in parallel**;
- specifically avoid parallel edits to `presidio_streamlit.py`, `fix_streamlit_nested_expanders.py`, review-table flow and export/download flow;
- helper/spec/test work can proceed separately only when it does not create conflicting implementation authority;
- privacy/safety blockers may interrupt this sequence, but generic backlog work must not dilute the current Premium UI focus by default.

---

