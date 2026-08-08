# SolidPrivacy Scrub — Current execution status override

> **2026-08-08 15:28 Europe/Amsterdam**  
> This block supersedes lower current-status fields until the next Premium package transition. Historical package descriptions remain retained below.

## Premium UI execution queue

1. `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` — **COMPLETED / independently PASSed / PR #87 merged** as `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`.
2. `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION` — **RELEASE_CANDIDATE_READY / independent assurance pending**, issue #84 / PR #85. Production `presidio_streamlit.py` integration is present. Clean runtime/product head `0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d` passed 1225 tests in 12.55s; final post-administration exact-head CI remains mandatory before assurance.
3. `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` — **QUEUED**, may start only after package 2 independently PASSes, merges unchanged, exact-main/deployment evidence is green and required App Shell verification is closed.
4. `SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION` — queued after Input Stage.
5. `SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION` — queued after Review Stage.
6. `SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION` — queued after the three stage packages.
7. `SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT` — final live Premium gate.

### App Shell candidate scope now implemented

- top-level `Anonimiseren | Terugzetten`;
- global `Standaard | Expert`;
- one persistent `Toevoegen → Controleren → Downloaden` workspace;
- exactly one active Standard stage;
- completed summaries, passive future stages and explicit return;
- automatic Add → Review and explicit Review → Download progression;
- deterministic processing lineage, fail-closed invalidation and current-generation analysis/review caching;
- no permanent Standard settings sidebar;
- Expert-only `highlight` / `synthesize` choices are preserved and require Expert rather than being silently rewritten;
- legacy runtime patching cannot re-inject the retired form shell into the direct Premium source.

### Governance gate

Do **not** merge PR #85 or start shared Streamlit work for package 3 until a fresh independent `governance_release_assurance` reviewer records `PASS` on the final exact PR head. Implementation does not self-certify.

---

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

### 2. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repaired candidate pending fresh assurance

Status: `RELEASE_CANDIDATE_READY` after repair of the prior assurance FAIL; fresh exact-head CI + fresh blind assurance required before merge.  
Issue: #84  
PR: #85  
Dependency: `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` merged after independent PASS.


Repair gate — 2026-08-08:
- prior exact head `2b04ca6260bddee07fbcf901239cee2955bd6dc7` received independent `FAIL` because Standard → Expert could silently reset Zorg to Juridisch;
- repaired candidate must preserve profile, operator, threshold, entity selection, allow/deny lists and analyzer configuration across presentation-only switching;
- presentation-only Standard ↔ Expert must keep deterministic processing generation and valid downstream lineage unchanged;
- a real processing-setting change must invalidate downstream lineage fail-closed;
- dedicated Standard Zorg → Expert → Standard regression coverage is mandatory;
- the repaired head requires a completely fresh blind reviewer; prior issue #90 cannot authorize the repair.

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

## 2026-08-07 Europe/Amsterdam — SCRUB-WP_ISSUE70_POST_MERGE_ACTIONS_EVIDENCE_RECOVERY — repaired candidate

Status: `RELEASE_CANDIDATE_READY`; fresh exact-head blind assurance required before merge.

Purpose:
- recover issue #70 exact-current-main GitHub Actions evidence without coordinator/manual GitHub actions;
- repair the first PR #73 candidate after independent assurance correctly rejected its expired June carrier handle.

Repaired execution mechanism:
- added purpose-built `Issue70 exact-main evidence carrier` workflow;
- carrier is read-only/no-op: no checkout, secrets, repository write, artifact write, deployment or product side effect;
- `Tests` retains push-main, pull-request, workflow-dispatch, no path filter, read-only checkout and full `python -m pytest -q tests` command;
- recovery `workflow_run` runs only for a successful carrier rerun with `run_attempt > 1`.

Raw implementation evidence:
- carrier run `31216068355` / run #3 initially succeeded;
- connector rerun invocation succeeded and produced attempt 2, job `92989859101`, conclusion `success`;
- PR Tests run `31216068325` / #2115 completed `1170 passed in 11.00s`;
- no coordinator/manual GitHub step was used.

Governance boundary:
- rejected assurance decision on old head remains valid only for that old identity;
- final PR #73 head must be frozen and reviewed afresh as `governance_release_assurance`;
- implementation cannot self-certify/self-merge, close #70 or start Premium Core Flow UI;
- after PASS and merge, implementation reruns the approved fresh carrier and assurance independently verifies exact-current-main Tests evidence before #70 closeout.

## 2026-08-06 21:30 Europe/Amsterdam — Independent assurance and merge closeout for PR #69

### SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY

Initial assurance decision: `PASS`.  
Closeout status: `ACTION_EXECUTED_UNVERIFIED`.

Evidence and action:
- the initial decision was recorded on issue #70 before implementation handovers, claims or implementation conclusions were opened;
- no repair was performed in the candidate;
- implementation claim and handover were checked only after PASS and were administratively complete;
- PR #69 was merged unchanged as `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71`;
- actual and tested merge candidates have identical parents and tree `4c993cbed86eade252cec6799f7dae5919b84085`;
- raw run #2105 passed all 1165 tests in 12.41s on tested merge candidate `13d55b6d74ad6f31446e16bcad0794abea32f9e7`.

### SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY

Initial assurance decision: `PASS`.  
Closeout status: `ACTION_EXECUTED_UNVERIFIED`.

Evidence and action:
- independent source/test reconstruction covered selection commit, all-exact TXT/processed-text replacement, original-DOCX replacement, bound Scrub Key, TXT/DOCX reinsert, CSV/scrub-report audit, include=false, fail-closed custom replacement and local-only/no-AI/no-cloud evidence;
- no production Python, Streamlit, frontend, runtime, dependency, workflow or deployment file changed;
- implementation claim and handover were checked only after PASS and were administratively complete;
- PR #69 was merged without candidate repair.

Post-action boundary:
- no distinct GitHub Actions push run on actual merged SHA `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71` was observable at closeout-writing time;
- `OUTCOME_CONFIRMED` is therefore deliberately not claimed yet;
- Hugging Face sync is not applicable because no runtime file changed and all changed paths are ignored by the sync workflow;
- app verification is not applicable because no UI behavior changed.

Verification records:
- `workpackage_claims/scrub_wp_two_role_governance_adoption_verify.md`;
- `workpackage_claims/scrub_wp_processed_text_selection_cross_flow_regression_verify.md`;
- `handover/workpackages/20260806_2130_two_role_governance_adoption_verify.md`;
- `handover/workpackages/20260806_2130_processed_text_selection_cross_flow_regression_verify.md`.

Next gate:
- complete the documentation-only closeout PR;
- promote both packages to `OUTCOME_CONFIRMED` only after the contract-required post-action evidence is available;
- do not start `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT` before that closeout confirmation.

## 2026-08-06 11:37 Europe/Amsterdam — Two-role governance adoption and processed-text cross-flow regression

### SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION

Status: `RELEASE_CANDIDATE_READY`; independent governance verification pending.

Goal:
- Adopt the canonical cross-project implementation-versus-release-assurance model used by Weekly ETF, strengthened for Scrub with a blind-review boundary.

Candidate files:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- project prompt, roadmap and decision-log invocation records;
- separate implementation and verification workpackages.

Verification gate:
- `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY` must be claimed by `governance_release_assurance` in a separate worker/session;
- before its initial decision, that worker must not read implementation handovers or implementation conclusions;
- governance may issue only `PASS`, `FAIL` or `INDETERMINATE` and may not silently repair the candidate.

### SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: `RELEASE_CANDIDATE_READY`; GitHub Actions PR #69 run #2097 green (`1165 passed in 9.62s`); independent governance verification pending.

Goal:
- Prove with synthetic chain tests that a processed-text selection row remains one normal authoritative review-table row across document export, Scrub Key, TXT/DOCX reinsert and audit evidence.

Candidate evidence:
- `tests/test_processed_text_selection_cross_flow_regression.py`;
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`;
- no production product-code or UI changes.

Required independent follow-up:
1. `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY`;
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY`;
3. only after both governance passes may `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT` start.

Safety boundary:
- synthetic data only;
- no recognizer, replacement, export, filename, MIME, Scrub Key, reinsert, audit, runtime or UI semantic changes;
- review-table include state and human review remain authoritative;
- custom replacement text remains document-exportable but verified bound-key generation must fail closed.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Status: completed planning/design-only; implementation not started.

Goal:
- Reassess the current interface after direct live-app evidence and replace incremental form decluttering with a coherent premium single-task app-shell direction.

Decision result:
```text
Top-level workflows: Anonimiseren | Terugzetten
Global presentation: Standaard | Expert
Standard stages: Toevoegen → Controleren → Downloaden
Only one active stage expanded
One primary action per stage
No permanent configuration sidebar in Standard
One recommended document download; other formats, Scrub Key and audit remain secondary
```

Safety boundary:
- visibility and grouping only unless a later package explicitly freezes state behavior;
- no recognizer, replacement, export, Scrub Key, reinsert, audit, runtime or dependency semantic change;
- human review remains mandatory.

Execution gate:
```text
1. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
2. SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT
3. SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL
4. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION
5. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
6. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
7. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
8. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
9. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

Parallelization:
- do not run the shared Streamlit UI packages in parallel;
- contract and pure state helpers precede UI integration;
- input, review and export are separate sequential patches.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Evidence:
- PR #66 merged as `74b7a15ee74f6330f7fc37892b65246c1a61afaf`;
- final run #2080: 1155 tests passed in 12.44s;
- independent deployment run #2082: 4/4 runtime files exact, health `ok`, root HTTP 200, frontend tests passed, 1155 tests passed in 11.49s;
- coordinator/user confirmation: `Aanpassing is geslaagd. Ik zie nu inderdaad kortere vervangingscodes.`

Confirmed boundary:
- compact aliases are display-only;
- full 80-bit-bound tokens remain internal and in exports;
- export, Scrub Key and reinsert semantics remain unchanged.

## 2026-08-04 22:22 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Goal:
- Record the coordinator/user confirmation that direct masking from `Verwerkte tekst` works in the deployed app.

Verification evidence:
```text
Integration PR: #63
Merge commit: 53fad202ae88a97b1ea476a9c3ba787932cd62ae
Final merge-candidate run: #2051 — 1146 passed in 11.59s
Independent deployment run: #2064
Runtime/component files exact on Hugging Face: 11/11
Space health: HTTP 200 / ok
Frontend component tests: passed
Post-deployment Python regression: 1146 passed in 11.47s
App verification: confirmed — "Het werkt."
```

Confirmed behavior:
- selection, safe inspection, type choice and exact-occurrence masking work;
- one normal `Handmatig uit tekst` row is created;
- one-step undo works;
- review table, manual fallback, export, Scrub Key and reinsert remain available;
- no Script execution error was reported.

New evidence finding:
- the repeated 80-bit document-binding segment makes bound placeholders visually long;
- shortening the underlying binding to four characters is not authorized because it would weaken wrong-key protection;
- next narrow package: `SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION`.

Boundaries:
- closeout-only; no product code or placeholder grammar changed;
- human review remains mandatory;
- no production-readiness claim.

## 2026-08-04 01:34 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Status: completed in GitHub; deployment synchronization and app verification pending.

Goal:
- Integrate direct selection masking with the existing document-scoped manual rows and authoritative review table.

Implementation result:

```text
Interactive component in production review: implemented
Static renderer environment/exception fallback: retained
Manual Gemiste waarde toevoegen fallback: retained
Inspect after current editable table state: implemented
Commit exactly one bound manual row: implemented
Immediate rerun before serial review/export: implemented
Protected spans when visual markers hidden: implemented
Replay/stale/collision guards: retained
Undo latest unchanged selection row: implemented
Undo after visible table edit: blocked
Export/Scrub Key/reinsert semantics changed: false
```

Files added:
- `processed_text_selection_integration.py`
- `tests/test_processed_text_selection_integration.py`
- `tests/test_processed_text_selection_table_integration_contract.py`
- `PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_table_integration.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

Files changed:
- `processed_text_selection_component.py`
- `side_by_side_review_panel_ui.py`
- `presidio_streamlit.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Validation:
- cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only;
- final clean PR run #2047: 1146 Python tests passed in 11.97s;
- Hugging Face sync and app verification pending after merge.

Next gate:
- synchronization plus focused live app verification;
- then `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`.

## 2026-08-04 01:00 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Status: completed; technical validation green.

Dependency:
- action model merged through PR #61 as `3e0e5be9457654d3dfb6e52e0e701a08b438a4d9`.

Goal:
- Prove a local bidirectional Streamlit v1 component can transport safe processed-text selections and server inspection results without mutating production state.

Implementation result:

```text
Local Streamlit v1 wrapper: implemented
Local dependency-free frontend assets: implemented
Python-codepoint → UTF-16 highlight conversion: implemented
Selection offsets across plain/marked nodes: implemented
Synchronized scroll: implemented
Right-click + Shift+F10 + ContextMenu + visible fallback: implemented
Accessible menu and ARIA status: implemented
inspect_selection event: implemented
Server inspection result display: implemented
commit_manual_mask intent: implemented
Actual commit/table mutation: deliberately absent
Production renderer integration: absent
External assets/network/storage/telemetry: absent
```

Files added:
- `processed_text_selection_component.py`
- `processed_text_selection_component_spike_demo.py`
- `frontend/processed_text_selection_component/`
- `tests/test_processed_text_selection_component_spike.py`
- `tests/frontend/processed_text_selection_component_core.test.js`
- `PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE.md`
- `workpackage_claims/scrub_wp_processed_text_selection_component_spike.md`
- `handover/workpackages/20260804_0100_processed_text_selection_component_spike.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Validation:
- standard run #1977: 1126 tests passed in 13.83s;
- dedicated Streamlit 1.39 smoke run #1979: 1126 tests passed in 13.79s;
- AppTest: no script exceptions;
- local server health: `ok`;
- root HTML and startup log checks: passed;
- clean post-governance standard run #1989: 1126 tests passed in 10.87s.

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`

Boundaries:
- no production UI or replacement-table mutation;
- no export, Scrub Key, reinsert, recognizer or profile change;
- no Streamlit upgrade, new runtime dependency or external asset;
- no occurrence-specific masking.

## 2026-08-04 00:30 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Status: completed; GitHub Actions green.

Dependency:
- contract package merged through PR #60 as `23cb5d667461f84a01e96ee007b2ef10bd2e6b40`.

Goal:
- Implement a pure Python, Streamlit-free and browser-free action model for the approved two-stage selection masking contract.

Implementation result:

```text
Inspect/commit event parsing: implemented
UTF-16 conversion and split-surrogate rejection: implemented
Selection validity and placeholder blocking: implemented
Exact non-overlapping occurrence count: implemented
Unicode embedded-token collision guard: implemented
Nested replacement conflict guard: implemented
1–5 / 6–20 / >20 impact bands: implemented
Replay history and single-use inspections: implemented
Commit-time source/processed/binding/table revalidation: implemented
Bound manual row adapter: implemented
Stable action ID and one-step undo: implemented
Streamlit/browser integration: not included
```

Files added:
- `selection_mask_action.py`
- `tests/test_selection_mask_action.py`
- `PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md`
- `handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md`

Files changed:
- `manual_mask_entry.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Validation:
- initial run #1957 exposed one missing local event-ID assignment and one overly literal source-text assertion;
- corrected run #1961: 1106 tests passed in 10.66s;
- clean standard run #1970: 1106 tests passed in 10.71s.

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`

Boundaries:
- no Streamlit/session-state or browser component;
- no `presidio_streamlit.py`, review-table, export, Scrub Key or reinsert change;
- no occurrence-specific replacement or dependency upgrade.

## 2026-08-04 00:09 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Status: completed; GitHub Actions green.

Approval evidence:
- coordinator/user approved the proposed direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam.

Goal:
- Freeze the exact interaction, event, safety, privacy and sequencing contract before action-model or component implementation.

Contract result:

```text
Protocol: inspect_selection → server impact result → commit_manual_mask
Scope: all exact occurrences only
1–5 safe occurrences: ready
6–20 safe occurrences: explicit confirmation required
>20 occurrences: blocked from quick path
Selection maximum: 160 Unicode code points, one line
Offset unit: UTF-16 code units
Payload maximum: 8192 UTF-8 bytes
Replay history: 128 event IDs per document
Quick types: 8 stable machine keys
Embedded/nested/marked collisions: fail closed
Review table source of truth: preserved
Manual form fallback: preserved
Export/Scrub Key/reinsert semantics: unchanged
```

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `test_cases/processed_text_selection_masking/contract.json`
- `tests/test_processed_text_selection_masking_contract.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md`
- `handover/workpackages/20260804_0009_processed_text_selection_masking_contract.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`

Boundaries:
- specification and contract tests only;
- no runtime, Streamlit, browser component, review-table or export-flow change;
- no occurrence-specific replacement or Streamlit upgrade;
- no Scrub Key, reinsert, recognizer, profile or cloud-processing change.

## 2026-08-03 23:42 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Status: completed as planning; GitHub Actions green.

Goal:
- Determine whether an unmasked value can be selected in `Verwerkte tekst`, classified through a right-click menu and safely added through the existing manual replacement path.

Planning result:

```text
Technically feasible: yes
Recommended component: bidirectional Streamlit v1 custom component
Current static components.html mutation-capable: no
First scope: all exact occurrences only
Only selected occurrence: deferred; requires span-aware architecture
Review table source of truth: preserved
Existing manual form fallback: preserved
Export/Scrub Key/reinsert semantics: unchanged
Implementation authorized: no
GitHub Actions: PR #59 run #1937 — 1015 passed in 11.64s
```

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `tests/test_processed_text_selection_masking_plan.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md`
- `handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md`

Files changed:
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`

Proposed implementation sequence:
1. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`
3. `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`
4. `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`
5. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`
6. `SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY`

Boundaries:
- planning and documentation only;
- no Streamlit UI, component, helper, dependency or runtime change;
- no occurrence-specific replacement;
- no recognizer, export, Scrub Key, reinsert or cloud-processing change;
- implementation requires explicit coordinator approval after discussion.

## 2026-08-03 23:26 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT

Status: completed; final documentation-only GitHub Actions confirmation pending.

Goal:
- Record the coordinator/user confirmation that the deployed long-form synthetic Zorgfilter examples work and close the package without changing product behavior.

Evidence:
```text
PR #56 merge: 1244663d3e69a56d6efc825a6fc019ba72d3782a
Final clean PR run #1926: 1003 passed in 11.51s
Deployment verification run #1931: 1003 passed in 11.35s
Runtime files exact on Hugging Face: 2/2
Space health: HTTP 200 / ok
App verification: confirmed — Alles werkt
```

Boundaries:
- closeout-only;
- no product code, UI, corpus, recognizer, profile, export, Scrub Key or reinsert change;
- no production-readiness claim;
- human review remains mandatory.

## 2026-08-03 22:17 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Status: completed and app-verified after GitHub Actions and Hugging Face synchronization verification.

Goal:
- Replace the short tester-facing care examples with longer, structured synthetic documents while preserving every existing recognition and policy contract.

Implementation result:

```text
Stable care-document families: 8
Added document-specific sections per example: 5
Minimum added narrative per example: 200 words
Minimum total visible length per example: 250 words
New identifying values in additions: 0
Digits in additions: 0
Recognizer/profile policy changed: false
Export/Scrub Key/reinsert semantics changed: false
```

Files added:
- `care_test_example_expansions.py`
- `tests/test_care_profile_long_form_corpus.py`
- `CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS.md`
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`

Files changed:
- `care_test_examples.py`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Verification result:
- final clean PR run #1926: 1003 tests passed in 11.51s;
- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Space health HTTP 200 / `ok`, and 1003 tests passed in 11.35s;
- coordinator/user app verification at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

Boundaries:
- synthetic data only;
- no recognizer, threshold, collision or profile-policy change;
- no review-table, export, Scrub Key or reinsert change;
- no dependency or cloud-processing change;
- human review and non-production boundaries remain unchanged.

## 2026-08-03 19:12 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_APP_VERIFY

Status: completed and app-verified after Actions/sync verification.

Goal:
- Verify the deployed Zorgfilter selector and review behavior after technical integration and cross-profile regression passed.

Technical deployment result:

```text
GitHub main commit: cca4a25aaff28a7ba647c961d8e50f0e076921e2
Hugging Face Space: solidprivacy/scrub
Files compared: 12
Exact byte matches: 12/12
Correctly scoped markers: all passed
Space health: HTTP 200 / ok
Space root: HTTP 200
Technical deployment verified: true
Functional app verification: confirmed — alles groen
Production ready: false
```

Evidence:
- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

Confirmed coordinator/user checks:
- four profile choices and stable default;
- eight synthetic care examples;
- `Controle nodig` rendering for review-selected care rows while selected;
- patient/client replacement defaults;
- unchecked care candidates;
- unchanged Legal/General/International, review, export, Scrub Key and reinsert flows;
- no Script execution error.

Gate status:
- completed: coordinator/user confirmed `alles groen` at 2026-08-03 20:35 Europe/Amsterdam; final verification-only CI run #1909 passed 998 tests.

Boundaries:
- verification-only; no product code or UI change;
- synthetic examples only;
- human review remains required;
- no production-readiness claim.

## 2026-08-03 18:58 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX

Status: completed; deterministic cross-profile gates are green.

Goal:
- Verify that Zorgfilter adds care-specific recognition without contaminating Legal or General profiles or masking protected clinical meaning.

Result:

```text
Profiles evaluated: 4
Care document families: 8
Legal examples: 12
Dedicated Care expectations: 108/108
Hard profile failures: 0
Protected clinical overlaps: 0
Care/International parity: passed
Legal/International parity: passed
Historical legal metadata: 132/148
Recorded historical gaps: 16
Recorded negative observations: 4
Final validated run #1899: 995 tests passed
Generic NER evaluated: false
Production ready: false
```

Evidence:
- `CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX.md`
- `output/validation/care_profile_cross_profile_matrix.json`
- `handover/workpackages/20260803_1858_care_profile_cross_profile_regression_matrix.md`

Active next package:
- `SCRUB-WP_CARE_PROFILE_APP_VERIFY`

Gate status:
- completed downstream: synchronization, deployed app behavior and verification-only regression are green.

Boundaries:
- pure helper/test/evidence package only;
- no Streamlit, review, export, Scrub Key or reinsert change;
- generic NER is model-dependent and deferred to deployed-app observation;
- synthetic data only;
- human review remains required;
- no production-readiness claim.

## 2026-08-03 18:28 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION

Status: completed, merged, synchronized and app-verified.

Goal:
- Register and expose the approved Zorgfilter v1 profile in the current Streamlit flow without changing export, Scrub Key or reinsert semantics.

Result:

```text
Visible profiles: 4
Default profile: Juridische controle — streng
Dedicated care recognizers registered: 16
Synthetic care examples: 8
Care candidates: review-only and unchecked
Review-selected detections: selected by default, status Controle nodig
GitHub Actions run #1877: 983 tests passed
Export semantics changed: false
Scrub Key semantics changed: false
Reinsert semantics changed: false
Production ready: false
```

Implementation:
- central profile configuration drives labels, thresholds and entity composition;
- exact-span care/legacy and AGB/BSN collision resolution runs before the replacement table;
- conservative strongly-labelled care candidate scanner added;
- user-facing care labels, placeholders and generalized product copy added;
- Legal remains the initial default and no profile changes silently;
- clinical meaning remains a preservation target.

Evidence:
- `CARE_PROFILE_CURRENT_UI_INTEGRATION.md`
- `output/validation/care_profile_current_ui_integration.json`
- `handover/workpackages/20260803_1828_care_profile_current_ui_integration.md`

Active next package:
- `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`

Required later gate:
- `SCRUB-WP_CARE_PROFILE_APP_VERIFY` completed after deployment sync and coordinator/user confirmation.

Boundaries:
- human review remains required;
- synthetic evidence does not prove production recall or precision;
- no cloud document processing or new dependency;
- no export filename, MIME type, Scrub Key schema/binding or reinsert behavior change.

## 2026-08-03 17:12 Europe/Amsterdam — SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR

Status: completed; pure four-profile configuration implemented, live integration still closed.

Goal:
- Centralize General Dutch, Care, Legal and International recognition behavior before changing the visible Streamlit selector.

Result:

```text
Profiles defined: 4
Current visible options preserved: 3
Future Streamlit order: Care, Legal, General Dutch, International
Desktop order: General Dutch, Care, Legal, International
Exact-span precedence winners: 15
Initial regression run #1865: 965 tests passed
Live UI changed: false
Care recognizers registered: false
```

Configuration includes:
- stable labels, internal values and thresholds;
- profile-specific entity groups;
- legal/care candidate and example direction;
- approved Care replace versus review-selected policy;
- exact-span AGB-over-BSN and care-specific-over-broad-legacy precedence;
- preservation of partial overlaps and non-Care profile behavior.

Evidence:
- `RECOGNITION_PROFILE_CONFIGURATION.md`
- `output/validation/recognition_profile_configuration.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`

Boundaries:
- no `presidio_streamlit.py` or `presidio_helpers.py` change;
- no live selector, threshold or entity behavior change;
- no export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.

## 2026-08-03 16:52 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION

Status: completed; pure recognizers implemented and contract-validated, app registration still closed.

Goal:
- Implement the frozen sixteen-entity Zorgfilter recognizer module without changing current app behavior.

Result:

```text
Dedicated entities: 16
Positive contracts: 37/37 passed
Forbidden positive collisions: 0
Negative/collision contracts: 16/16 passed
Dedicated corpus expectations: 54/54 passed
Protected clinical phrase overlaps: 0
Full regression run #1854: 953 tests passed
App registration: false
```

Implementation:
- `dutch_care_recognizers.py` with value-only Presidio capture results;
- strong-context administrative references and AGB;
- provider-name recognition preserving professional roles;
- labeled organizations and bounded locations;
- room/bed/apartment references;
- care-event dates separated from date of birth;
- no Streamlit, network, AI, cloud or file-write behavior.

Evidence:
- `CARE_RECOGNIZER_IMPLEMENTATION_V1.md`
- `output/validation/care_recognizer_implementation_validation.json`

Active next package:
- `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`

Boundaries:
- recognizers are not registered in `presidio_helpers.py` or the UI;
- generic PERSON/e-mail remain generic-profile dependencies;
- AGB/BSN profile-level precedence remains to be validated;
- no export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.

## 2026-08-03 16:34 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS

Status: completed; recognizer contract frozen before implementation.

Goal:
- Freeze exact positive, value-only, policy, collision and clinical-preservation behavior for the dedicated Zorgfilter recognizer module.

Contract result:

```text
Dedicated care entities: 16
Positive exact-span cases: 37
- care-reference/collision cases: 17
- contextual review cases: 20
Negative/collision/preservation cases: 16
Future module: dutch_care_recognizers.py
Public API: get_dutch_care_entity_names, get_dutch_care_recognizers
```

Frozen boundaries:
- generic PERSON and e-mail stay in the generic profile layer;
- care providers, organizations, locations, room/bed and care-event dates use context-bound review recognition;
- AGB requires strong context and must not become BSN;
- labels and professional roles remain readable;
- vital signs, medication, dosages, administration times, lab values, DBC/ICD codes and clinical meaning remain preserved;
- no app registration or UI integration in this package.

Evidence:
- `CARE_RECOGNIZER_CONTRACT_V1.md`
- `output/validation/care_recognizer_contract_v1_summary.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`

Production readiness: false. Human review remains required.

## 2026-08-03 16:25 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_GAP_TRIAGE

Status: completed; all current care-corpus expectations classified.

Goal:
- Route every correct, missed or misclassified baseline value to a concrete follow-up mechanism before recognizer implementation.

Result:

```text
Expectations classified: 81/81
Reuse current recognizer: 14
Generic profile dependency: 13
Contextual care review recognizer: 36
Care-specific reclassification: 10
Dedicated care reference recognizer: 5
Care collision guard: 3
Unclassified: 0
```

Key decisions:
- keep address, BIG, BSN, date-of-birth and Dutch-phone recognizers;
- keep generic PERSON and e-mail in the generic local profile layer;
- split broad healthcare/legal references into care-specific policy entities;
- build a context-bound review layer for providers, organizations, locations, room/bed and care-event dates;
- require explicit AGB/BSN precedence and negative medical-number contracts;
- keep diagnosis, medication, dosages, lab values, observations and roles under preservation guards.

Evidence:
- `CARE_PROFILE_GAP_TRIAGE.md`
- `output/validation/care_profile_v1_gap_triage.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`

Boundaries:
- no recognizer or UI implementation;
- no threshold, export, Scrub Key or reinsert change;
- synthetic data only;
- human review remains required;
- production readiness remains false.

## 2026-08-03 16:10 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE

Status: completed; corrected current-engine evidence baseline implemented and validated.

Goal:
- Measure the unchanged deterministic Dutch custom recognizers against the eight-document synthetic care corpus before dedicated Zorgfilter recognizers are added.

Result:

```text
Expected replace/review values: 81
Exact normalized spans found: 25 (30.86%)
Correct intended entity type: 14 (17.28%)
Misclassified values: 11
Missed values: 56
Protected clinical phrase overlaps: 0
```

Key evidence:
- strong bounded coverage for addresses, BIG numbers, BSN, dates of birth and Dutch telephone numbers;
- no bounded custom-rule coverage for generic PERSON names, care-provider names, care organizations, exact care-event dates, care locations or room/bed references;
- review-selected layer: 4/42 spans found and 3/42 correctly classified;
- one AGB code collided with BSN recognition;
- broad existing healthcare/legal references find several values but do not express the approved care policy;
- generic NER was excluded and the baseline is not a full-app or production-readiness measurement.

Evidence:
- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `output/validation/care_profile_v1_current_engine_baseline.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`

Boundaries:
- synthetic data only;
- no recognizer behavior, UI, threshold, export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.

## 2026-08-03 15:31 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION

Status: completed; policy/corpus foundation implemented and validated.

Goal:
- Establish the approved Zorgfilter v1 policy and a fully synthetic, machine-readable care-document corpus before adding recognizers or UI.

Current package scope:
- roadmap, decision and risk alignment;
- pure care-profile action contract;
- eight synthetic care-document families;
- corpus contract tests;
- current custom-recognizer baseline helper and report generator.

Approved policy:
- date of birth and patient/client identity: replace;
- other exact care dates and provider identity: review, selected by default;
- diagnosis, medication, dosage, lab results and observations: preserve;
- rare-case re-identification: audit warning only.

Active next package:
1. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`
2. `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`
3. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`
4. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`
5. `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`
6. `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`
7. `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`
8. `SCRUB-WP_CARE_PROFILE_APP_VERIFY`
9. `SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT`

Boundaries:
- no Streamlit change in this package;
- no recognizer behavior change yet;
- no export, Scrub Key, reinsert, cloud or dependency change;
- synthetic data only;
- current Phase 6 binding verification remains an independent active gate.

## 2026-08-03 14:47 Europe/Amsterdam — SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT

Status: completed; documentation/strategy alignment only.

Summary:
- Added an AI-first execution model for the final local Windows desktop/offline packaging phase.
- Preserved the existing gate: installer implementation remains deferred until Phase 6 quality closeout and explicit coordinator approval.
- Refined the eventual target to a signed Tauri shell, bundled PyInstaller onedir Python/Presidio sidecar, setup.exe and MSI.
- Recorded planning assumptions that 60–70% of first-cycle development/integration labor and 75–90% of later repetitive release work may be agent-executed.
- Kept publisher identity, signing, public release, security claims, real-user acceptance and safety-critical semantic changes under human control.
- Added no product code, installer, runtime, dependency or UI change.

Next recommended step:
- Continue the active Phase 6 queue. Open the Phase 9 desktop distribution contract only after quality-gate closeout and explicit approval.

## 2026-07-28 00:52 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; app verification pending.

Summary:
- Binding validation now gates every text, TXT, DOCX and PDF-to-TXT reinsert before replacement.
- Correct bound keys are verified; legacy v1.0 remains explicit unverified compatibility.
- Wrong, mixed, missing or corrupted bindings restore zero values.
- The existing three-step flow and final confidentiality acknowledgement remain unchanged.

Next recommended step:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY` after merge and sync.

## 2026-07-27 21:45 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Status: implemented; targeted validation pending.

Summary:
- Bound placeholder and schema-1.1 key creation is integrated into anonymization/export.
- Custom replacement text is preserved and cannot be silently represented as a verified bound mapping.
- Reinsert enforcement remains the active next package.

Next recommended step:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.

## 2026-07-27 20:05 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Status: implemented; targeted validation passed; PR verification pending.

Summary:
- Added `scrub_key_binding.py` as a pure, Streamlit-free binding model.
- Implemented local binding-ID generation using ten random bytes and uppercase base32.
- Implemented strict binding-ID validation and automatic/manual bound placeholder build/parse helpers.
- Implemented strict document binding-ID extraction from bound placeholders.
- Implemented canonical mapping-digest payload and SHA-256 digest helpers matching the frozen fixture.
- Implemented bound Scrub Key structural, policy, item-binding, duplicate and digest validation.
- Implemented all eight frozen document/key statuses, including explicit legacy-v1.0 unbound compatibility.
- Enforced six fail-closed statuses before any later replacement integration.
- Preserved immutable inputs and stable result fields.
- Integrated nothing into current placeholder generation, export, reinsert or UI paths.

Validation boundaries:
- Contract fixture digest matched exactly.
- Targeted model, contract, legacy import/export and roundtrip tests passed.
- No Streamlit, network, AI, cloud or file-write behavior exists in the model.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`.

## 2026-07-27 19:38 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Status: completed; contract frozen; PR validation pending.

Summary:
- Added a versioned binding contract and synthetic fixture before any product implementation.
- Locked binding ID grammar `B[A-Z2-7]{16}` with an 80-bit random payload.
- Locked automatic placeholders as `[LABEL_BINDINGID_INDEX]` and manual placeholders as `[LABEL_BINDINGID_HANDMATIG_INDEX]`.
- Locked bound Scrub Key metadata direction as schema version `1.1`, binding version `1`, a document binding ID and canonical SHA-256 mapping digest.
- Locked eight binding statuses and six fail-closed statuses that must produce zero replacements.
- Locked explicit legacy-v1.0 unbound compatibility without silent upgrading.
- Preserved the existing three-step source → key → download UX and final confidential-download acknowledgement.
- Defined the pure helper responsibilities for model implementation.
- Changed no product helper, UI, placeholder generation, Scrub Key schema implementation, export or reinsert behavior.

Validation boundaries:
- Fixed synthetic digest: `516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3`.
- Mapping digest is accidental-corruption evidence, not authenticity or a signature.
- Malformed placeholders are never guessed or repaired.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.

## 2026-07-27 19:18 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: completed; targeted validation passed; PR verification pending.

Summary:
- Classified the critical same-placeholder wrong-key finding by accidental pairing, accidental corruption and malicious tampering.
- Rejected document labels, complete-content hashes, placeholder-list hashes, filenames, hidden metadata and extra sidecars as sufficient primary binding controls.
- Recommended a non-sensitive document binding ID carried in every automatic/manual placeholder and the corresponding Scrub Key.
- Recommended a canonical SHA-256 mapping digest as a complementary accidental-corruption control, not as an authenticity signature.
- Deferred signature/HMAC protection until a trusted local signing-key lifecycle exists.
- Preserved the three-step document-first reinsert flow without new confirmation buttons or checkboxes.
- Changed no product code, UI, schema, placeholders, export or reinsert semantics.

Approved sequential implementation line:
1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`
2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`
3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`
4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`
5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Optional later package:
- `SCRUB-WP_MVP_MALFORMED_PLACEHOLDER_DIAGNOSTIC_HARDENING`.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.

## 2026-07-27 18:55 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Status: completed; deterministic validation passed; PR verification pending.

Summary:
- Added a versioned synthetic adversarial matrix with 15 Scrub Key and placeholder roundtrip scenarios.
- Verified intact, repeated, missing, unknown, translated, merged, malformed and changed placeholder behavior.
- Verified duplicate, incomplete, malformed, tampered and wrong Scrub Key behavior.
- Confirmed deterministic local execution with no AI or cloud processing.
- Changed no product code, UI, Scrub Key schema, export or reinsert semantics.

Validation result:
- Cases: 15.
- Failing cases: 0.
- Findings: 2.
- Critical findings: 1.
- Medium findings: 1.
- Production readiness: false.
- Human review remains required.

Critical evidence:
- A structurally valid wrong or tampered Scrub Key that reuses the same placeholder namespace can restore incorrect original values without a detectable mismatch.
- This requires separate triage because a safe solution may affect document/key binding, Scrub Key schema or export semantics.

Secondary evidence:
- Malformed tokens outside the strict placeholder grammar are reported indirectly through expected placeholders not found, rather than as explicit unknown malformed tokens.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`.

## 2026-07-27 18:28 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Evidence:
- PR #38 merged as `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678 passed.
- The coordinator live-tested the deployed three-step workflow and confirmed it is working.
- The live result proves that the merged UI reached the Hugging Face Space.

Verified behavior:
- Step 1 begins with the source document or pasted text.
- Step 2 accepts and automatically validates the corresponding Scrub Key.
- Local deterministic reinsert starts automatically for one valid source/key pair.
- Redundant source/key acknowledgement checkboxes and execution buttons are absent.
- One confidentiality acknowledgement remains immediately before download.
- Existing output filenames, MIME types, audit reporting and DOCX/PDF boundaries remain intact.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-27 17:06 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; full suite passed; final PR validation pending.

Evidence:
- Live DOCX reinsert passed for body, table, header and footer.
- The same verification exposed a concrete interface-clarity blocker: uploaded source/key files still required hidden follow-up checkboxes and action buttons.

Summary:
- Reordered reinsert to source first, Scrub Key second and restored download third.
- Added pure helper orchestration for input normalisation, deterministic request signatures and dispatch to existing local helpers.
- Automatically validates a supplied Scrub Key and automatically runs reinsert for one valid source/key pair.
- Removed separate source/key acknowledgement checkboxes and execution buttons.
- Retained one final confidentiality acknowledgement at the restored-output download boundary.
- Preserved TXT, DOCX, PDF-to-TXT and pasted-text paths, audit reporting, filenames, MIME types and safety boundaries.

Validation:
- Full repository suite: 797 passed.
- Final GitHub Actions pending after governance finalisation.
- Hugging Face sync and live app verification required after merge.
- Human review remains required; production readiness remains false.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-17 22:30 Europe/Amsterdam — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Summary:
- Extended deterministic DOCX reinsert from `word/document.xml` to existing `word/header*.xml` and `word/footer*.xml` text nodes.
- Preserved body/table behavior and unrelated OOXML package parts.
- Aligned existing DOCX reinsert copy with the supported body/table/header/footer scope without adding controls.
- Kept comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata and split placeholders explicitly unsupported.
- Resolved the DOCX header/footer finding and retained the PDF TXT-only/no-OCR boundary.

Validation:
- DOCX header/footer resolution: true.
- Resolved findings: 1.
- Remaining findings: 1.
- Production readiness: false.
- Human review remains required.
- Final clean-branch GitHub Actions validation required before merge.
- Hugging Face sync and live app verification required after merge.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-17 11:45 Europe/Amsterdam — HF Space runtime incident closeout

Status: completed and app-verified.

Summary:
- Restored the Hugging Face Space and confirmed runtime stage `RUNNING`.
- Coordinator confirmed that the application opens again.
- Merged a conservative sync-churn guard so clearly non-runtime-only commits no longer rebuild the Space.
- Removed temporary recovery and probe workflows/triggers.
- No product behavior or privacy controls changed.

Active next package:
- Resume `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING` in PR #33.

## 2026-07-17 22:08 Europe/Amsterdam — SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Status: completed / ready for PR verification.

Summary:
- Classified all 2 evidence items from the Phase 6 synthetic matrix.
- Confirmed that the corrected matrix contains no reproducible false negative, misclassification or role-over-masking result that justifies recognizer changes.
- Routed the DOCX header/footer reinsert limitation and PDF restored-TXT-only boundary to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.
- Recorded the `.invalid` fixture correction so it cannot reappear as a false product gap.
- No product code or behavior changed.

Validation:
- Machine-readable triage must match every evidence gap in the source report.
- Recognizer fix required: false.
- Production readiness: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

## 2026-07-17 20:20 Europe/Amsterdam — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: completed / ready for PR verification.

Summary:
- Added a versioned synthetic validation manifest with TXT, DOCX and text-based PDF cases.
- Added pure helper-driven validation for import, review rows, manual additions, replacements, Scrub Key, reinsert, export representation and DOCX hygiene evidence.
- Generated `output/validation/mvp_phase6_synthetic_validation_report.json` as the machine-readable Phase 6 baseline.
- Recorded existing DOCX header/footer reinsert and PDF TXT-only limitations as evidence rather than silently accepting or changing them.
- No UI, recognizer, export, Scrub Key, reinsert or document-processing semantics changed.

Validation:
- Cases: 3.
- Failing cases: 0.
- Evidence gaps: 3.
- Categories: false_negative_or_detection_gap, known_docx_reinsert_limitation, known_pdf_reinsert_limitation.
- Production-readiness claim: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`.

## 2026-07-17 20:12 Europe/Amsterdam — SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT

Status: completed / ready for PR verification.

Summary:
- Closed the verified MVP UI simplification line as the default development focus.
- Made Phase 6 end-to-end workflow validation and trust hardening the active execution line.
- Added `MVP_PHASE6_EXECUTION_PLAN.md` with the ordered validation, triage, hardening, evidence and quality-gate packages.
- Preserved the Phase 7 pilot, local packaging and production-readiness gates.
- No product code, tests, UI, recognizers, replacement semantics, export, Scrub Key, reinsert, document processing, runtime or dependencies changed.

Validation:
- Documentation consistency checks required through PR review and GitHub Actions.
- Hugging Face sync not functionally relevant because no app code changed.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX`.

## 2026-07-16 23:43 Europe/Amsterdam — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Summary:
- Live Hugging Face app verification passed after PR #28 merge.
- The manual correction panel opens with one concise caption, a compact three-column input row and one full-width submit action.
- The duplicate internal heading is absent.
- Synthetic value `lantaarnbloem` was successfully added and is visible in the replacement table as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.
- The screenshot confirms the merged UI reached the Hugging Face Space and no Script execution error is visible.
- No product code or behavioral semantics changed in this docs-only closeout.

Validation:
- PR #28 final GitHub Actions test run passed before merge.
- Hugging Face sync confirmed by live deployed UI.
- App verification passed.

Related package status:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

Next recommended step:
- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

## 2026-07-16 20:40 Europe/Amsterdam — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Summary:
- Converted the open manual correction form from a vertical stack to one compact three-column input row.
- Removed the duplicate internal `Gemiste waarde toevoegen` heading.
- Kept the expander collapsed by default and retained one full-width submit action.
- Preserved validation, session state, replacement-table integration and all export/Scrub Key/reinsert semantics.

Validation:
- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- App verification required after sync.

Next recommended step:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY`.

## 2026-07-05 22:42 Europe/Amsterdam — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Summary:
- Recorded live app verification for the Review/Export vertical-density implementation.
- Confirmed the Export section is materially less tall and less form-like because TXT/DOCX/PDF downloads are shown in a compact row.
- Confirmed Review safety controls remain visible or accessible: Basiscontrole/Expertcontrole, Markeringen tonen, side-by-side review, Gemiste waarde toevoegen, vervangtabel and replacement status.
- Confirmed Scrub Key, audit/technical files and DOCX hygiene audit remain separate and accessible.
- No product code, tests, export payloads, filenames, MIME types, Scrub Key JSON, reinsert behavior or startup/runtime behavior changed in this closeout.

Validation:
- Coordinator live Hugging Face screenshot reviewed.
- GitHub Actions for PR #26 passed before merge.
- Live Hugging Face app shows the merged UI behavior.
- `git diff --check` required before PR.

Next recommended step:
- Decide whether the current MVP UI is good enough for this pass, or start a new separately approved small UI package.

Related package status:
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN` — completed and merged.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS` — completed and merged.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

## 2026-07-05 22:13 Europe/Amsterdam — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Summary:
- Implemented the conservative Option B Review/Export density pass.
- Compressed repeated Review helper copy without hiding the main side-by-side review.
- Kept manual missed-value entry and the replacement table collapsed and accessible.
- Changed the primary TXT/DOCX/PDF document downloads from three stacked buttons into a compact three-column layout.
- Preserved export payloads, filenames, MIME types, Scrub Key JSON, reinsert behavior, recognition behavior and startup/runtime boundaries.

Validation:
- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required because visible UI behavior changed.

Next recommended step:
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY`.

## 2026-07-05 01:13 Europe/Amsterdam — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Summary:
- Resumed the implementation branch after the connector-only worker was blocked before product edit.
- Grouped the existing upload, synthetic example selector and pasted/extracted text area into one input surface under the single `1. Voeg document of tekst toe` heading.
- Preserved existing input variables, input precedence, TXT/DOCX/PDF support, review/export/Scrub Key/reinsert/audit behavior and startup/runtime boundaries.
- Added a source-level implementation guard for the unified input surface.

Validation:
- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI grouping changed.

Next recommended step:
- Run required guardrail tests, open PR, verify Actions, merge when green, verify Hugging Face sync, and request live app verification.

## 2026-07-04 23:18 Europe/Amsterdam — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Status: completed / PR validation pending.

Summary:
- Added source-level contract tests for the duplicate input-surface simplification line.
- Locked the intended single `1. Voeg document of tekst toe` input step before any implementation touches `presidio_streamlit.py`.
- Protected existing TXT/DOCX/PDF upload support, synthetic legal examples, pasted/extracted text area, input precedence, review controls, Scrub Key/export/audit surface and startup-patch boundaries.
- No product code, UI behavior, export semantics, Scrub Key semantics, reinsert behavior, recognizers, dependencies or startup/runtime patches changed.

Validation:
- Targeted and related source-level checks are expected through PR validation/GitHub Actions.
- Hugging Face sync is not applicable until merge.
- App verification is not applicable for this contract-test-only package because no UI behavior changed.

Next recommended step:
- Review PR validation. If green, merge and start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow package.

## 2026-07-03 00:00 UTC — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / PR validation pending.

Summary:
- Calmer side-by-side review copy implemented in `side_by_side_review_panel_ui.py`.
- The review surface now refers more clearly to the safe download step while keeping the comparison report-only.
- Added `tests/test_review_surface_simplification_implementation.py`.
- Updated source-level copy tests for the calmer review surface.
- No replacement logic, export content, filenames, MIME types, Scrub Key JSON, reinsert behavior, recognizers, benchmarks, runtime/startup or dependency behavior changed.

Validation:
- Targeted and related tests are expected through PR validation/GitHub Actions.
- Hugging Face sync required after merge.
- Live app verification required after Actions and sync are green because visible UI copy changed.

Next recommended step:
- Review PR validation. If green, merge and request live app verification.

## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

Status: in_progress / implementation complete / full-suite validation pending

Scope completed:
- migrated reinsert UI to direct source via `reinsert_mode_ui.py`;
- simplified visible reinsert flow into four user-facing steps;
- kept `presidio_streamlit.py` change minimal;
- added startup no-op guard for direct-source reinsert UI;
- added source-level UI contract tests.

Validation so far:
- targeted reinsert simplification test passed;
- existing reinsert UI patch tests passed;
- warning/two-mode UI tests passed.

Remaining:
- run full test suite;
- commit and open PR;
- verify GitHub Actions;
- verify GitHub to Hugging Face sync;
- request live app verification.


# SolidPrivacy Scrub — Workpackages

Repository: `solidprivacy-nl/scrub`.

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

## Claim rule

Before starting a package, check `workpackage_claims/`. If a claim for the same workpackage is already `in_progress`, stop and report the collision. If no claim exists, create one before changing files. When done, update the claim with status, final commit, handover path, validation and next step.

## Current status

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION — implemented / PR validation pending; visible review copy changed; live app verification required after Actions/HF sync.
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — completed / merged to main / Actions + HF sync green.
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN — completed / merged to main / Actions + HF sync green.
SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — completed and verified; default UI flow simplified toward execution interface, secondary controls collapsed, no export/Scrub Key/reinsert/recognizer/benchmark/startup semantics changed.
SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION — completed; small visible Dutch copy polish for side-by-side review and serial review labels, no product behavior or export semantics changed.
SCRUB-WP_MAIN_NOOP_CLEANUP — completed; accidental noop files and accidental copy-polish claim were removed from main.
SCRUB-WP_MVP_UI_APP_VERIFICATION_CLOSEOUT — completed; verification/closeout-only status recorded for the current MVP UI baseline, no product code or export semantics changed.
WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — completed; MVP UI cleanup and export/download redesign route planned.
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — completed and verified; contract tests added for professional export/download UX redesign.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — superseded by direct repair after startup-patch app verification failed.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — completed and verified; export/download UX implemented directly in presidio_streamlit.py.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN — completed; sharp interface cleanup plan added without adding a new review loop.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — completed and verified; step-by-step review collapsed by default, debug governance captions removed from primary UI, Actions/HF/app verified.
WP_MVP_FAST_MANUAL_MASK_ENTRY — completed and verified; simple manual entry for missed values is implemented in the existing review flow and live app verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — completed and verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — completed and verified.
WP_RECALL_PERSON_NAME_COVERAGE_TESTS — completed and verified.
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — completed.
WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — completed.
WP_SERIAL_REVIEW_UI — completed and app-verified.
```

Earlier completed workpackages remain available in Git history and handover files.

## Active product line

```text
Import -> Scrub -> Review -> Handmatig aanvullen -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend baseline

The review table remains source of truth and fallback. The normal app keeps one central side-by-side review surface, visible markers, a simple manual missed-value entry, the collapsible replacement table, optional step-by-step review, export/download and DOCX hygiene audit.

Current product direction remains MVP interface cleanup and fast anonymization workflow before more recall/benchmark follow-up.

## MVP UI/export redesign status

Planning, contract and implementation files:

```text
MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
MVP_UI_APP_VERIFICATION_CLOSEOUT.md
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
tests/test_export_download_ux_implementation.py
REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md
manual_mask_entry.py
presidio_streamlit.py
serial_review_panel_ui.py
side_by_side_review_panel_ui.py
tests/test_review_copy_polish_ui.py
REVIEW_SURFACE_SIMPLIFICATION_PLAN.md
REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md
tests/test_review_surface_simplification_contracts.py
tests/test_review_surface_simplification_implementation.py
```

The failed startup-patch route was removed after live app verification showed the old export section. Direct implementation now lives in `presidio_streamlit.py` and is verified in the live app.

The review debug collapse implementation keeps the change interface-focused: the existing serial review renderer is collapsed by default and no new review/benchmark/safeguard loop is introduced. Verification shows the primary review UI no longer displays old debug/governance captions.

The fast manual mask entry implementation adds a simple MVP control near `2. Controleer resultaat` so a user can add a missed value to the existing replacement table. It does not add right-click, context menu, custom editor, export semantics, Scrub Key semantics, reinsert semantics or recognizer changes. Actions, Hugging Face sync and live app verification are complete.

The MVP UI app verification closeout records the current verified MVP UI baseline as an administrative checkpoint only. It does not change product code, UI behavior, export semantics, Scrub Key semantics, reinsert semantics, recognizer logic, benchmark logic or local packaging.

The review copy polish implementation improves visible Dutch helper text in the side-by-side review and serial review panel only. It does not change the review table, export construction, Scrub Key, reinsert, recognizers, benchmarks or local packaging.

The review surface simplification line protects and implements a calmer side-by-side review copy before broader review-flow implementation. Export, Scrub Key, reinsert and recognition behavior remain unchanged.

Contract and implementation protection covers:

```text
export/download grouping
Scrub Key separation and warning
primary document downloads vs audit downloads
no export semantics change
audit/technical details remain available
copy-cleanup direction
implementation route
manual missed-value entry through the existing replacement table
MVP UI verification closeout without product behavior change
copy polish without product behavior change
review-surface simplification boundaries before implementation
```

## Recall/benchmark status

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

## Active / next recommended execution queue

```text
1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX
2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — only for reproducible gaps found by the matrix
3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING
4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION
5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE
6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT
```

The UI simplification baseline is completed and app-verified. Do not start another UI package by default; use evidence from Phase 6 validation to justify any future UI change.

## Boundaries

Do not start further UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.

## SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE — completed

Status: completed / ready for PR verification.

Summary:
- Reproduced DOCX side-by-side preview order issue with synthetic paragraph/table markers.
- Fixed DOCX plain-text extraction to preserve interleaved paragraph/table body order.
- No export, Scrub Key or reinsert semantics changed.

Validation:
- Targeted DOCX/reinsert/hygiene tests: 40 passed.
- Full suite: 649 passed in 102.51s.

## SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN — completed

Status: completed as planning/design-only; merged to main.

Summary:
- Added `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` for the next premium MVP review-surface simplification line.
- Target flow: `1. Voeg document toe` -> `2. Controleer resultaat` -> `3. Download veilig`.
- Keeps side-by-side review central, review table available as source of truth/fallback, and safety/audit controls available through calmer secondary layers.
- Defines `SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS` as the recommended next package before implementation touches `presidio_streamlit.py` or review flow.

Validation:
- Planning/design-only package; no product tests required.
- No app verification required because no UI behavior changed.
