# Premium Staged Workspace Decision

Status: `APPROVED_DIRECTION — RELEASE_CANDIDATE`

Coordinator approval: 2026-08-08 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE`

## 1. Decision

The Premium Standard interface for the Scrub anonymization core flow will use a **single-page staged document workspace**.

The three core stages remain persistently represented in the same workspace:

```text
1. Toevoegen
2. Controleren
3. Downloaden
```

Exactly one of those stages is expanded and dominant at any moment.

This is deliberately **not** a three-page wizard and deliberately **not** a conventional form with multiple independent expanders.

The governing product principle is:

```text
One document. One workspace. Three stages. One active task.
```

## 2. Problem being solved

The current verified functional baseline still reads visually as a long Streamlit form. Input, settings, review, manual corrections, downloads, Scrub Key controls and audit evidence compete for attention in one vertical page.

Earlier decluttering improved individual surfaces but did not solve the structural problem: the UI still exposes too much workflow state simultaneously and therefore asks the user to understand the implementation rather than the task.

The Premium line must reduce cognitive load without reducing review, privacy, auditability or control.

## 3. First-principles analysis

### 3.1 What is the user actually trying to accomplish?

The user's primary job is not to navigate pages or configure an anonymization engine. It is:

```text
safely transform one confidential document
→ inspect the result
→ obtain the right output
```

The interface should therefore model the **state of the document**, not a collection of pages or forms.

The minimum state story is:

```text
source supplied
→ processing result exists
→ result reviewed
→ current export is eligible
```

### 3.2 What information must remain visible?

At any moment the user needs to know:

1. what document/text is being worked on;
2. where they are in the workflow;
3. whether prior work is complete and still current;
4. what action is required next;
5. whether a later result has become stale after an earlier change.

A good UI should answer these questions without forcing navigation or exposing every control.

### 3.3 Why one active task matters

Human attention is the scarce resource in Scrub review. Displaying input, settings, review helpers, export choices, Scrub Key and audit controls at the same visual level increases decision surface without increasing safety.

Premium Standard therefore optimizes for:

```text
one dominant task
+ one dominant primary action
+ compact context from completed work
+ visible but non-competing future stages
```

This is lower cognitive load, not lower safety.

## 4. Alternatives considered

### Model A — three separate screens/pages

Concept:

```text
Toevoegen → separate page
Controleren → separate page
Downloaden → separate page
```

#### Advantages

- maximal visual isolation;
- very low per-screen control density;
- strong linear progress cue;
- naturally suppresses irrelevant controls;
- can feel polished when the process is strictly linear.

#### Disadvantages for Scrub

- loses document/workflow context when moving between stages;
- makes review-to-input correction feel like backward navigation rather than normal document iteration;
- creates more routing/state-restoration responsibility in Streamlit;
- increases the risk that users do not know whether a previous source/profile/result is still current;
- can encourage hidden reprocessing or stale-state bugs if navigation and processing state become coupled;
- makes the complete state of the document workflow less observable.

### Model B — single-page staged workspace

Concept:

```text
✓ Toevoegen — compact summary
▼ Controleren — active workspace
  Downloaden — visible, passive
```

#### Advantages

- preserves one-task-at-a-time focus;
- keeps the document workflow spatially coherent;
- makes progress and previous-state summaries visible without reopening full controls;
- makes deliberate return to an earlier stage natural;
- maps directly to the existing state-model concept of source/processed/review/export lineage;
- fits Streamlit without requiring page routing as the primary state mechanism;
- supports automatic progression while preserving explicit user control;
- allows stale downstream state to be represented clearly after earlier changes.

#### Risks

- can regress into the current form-like experience if implemented as generic/nested expanders;
- collapsed sections can become visually noisy if summaries contain too much detail;
- careless accordion controls can make the interface feel like a website FAQ rather than an application.

These risks are addressed through the rules below.

## 5. Decision rationale

Scrub is not a strictly linear checkout flow. Human review is central, and review can legitimately cause a return to earlier work. The product must therefore preserve both **focus** and **workflow context**.

The staged workspace wins because it treats the source, review and output as states of one document rather than unrelated destinations.

The decision is especially strong for the current Streamlit architecture because it minimizes routing complexity while allowing the already merged `premium_core_flow_state.py` invariants to remain authoritative.

The design preference is approximately:

```text
single-page staged workspace: strong preference
three separate core-flow pages: rejected for Standard
```

Separate top-level workflows such as `Anonimiseren | Terugzetten` remain valid. The rejection applies to turning the three anonymization core stages into routed pages.

## 6. Binding Standard-mode interaction contract

### 6.1 Persistent stage rail/workspace

All three stage headers remain present in the same page/workspace:

```text
1. Toevoegen
2. Controleren
3. Downloaden
```

They must not all expose their full internals simultaneously.

### 6.2 Exactly one expanded stage

At all times exactly one core stage is dominant and expanded.

Opening a different eligible stage collapses the currently expanded stage.

There is no Standard-mode state where two core stages expose their full working surfaces at once.

### 6.3 Completed-stage summaries

A completed prior stage collapses into a compact summary that gives only the information needed for trust and orientation.

Examples:

```text
✓ Toevoegen — contract.docx · Juridisch
✓ Controleren — 14 gecontroleerd · 1 handmatig toegevoegd
```

Summary content must not become a second mini-form.

### 6.4 Future-stage visibility

Future stages remain visible so the complete workflow is understandable, but they are passive until prerequisites are satisfied.

Example:

```text
Downloaden — beschikbaar na controle
```

A passive future stage must not expose disabled forests of controls.

### 6.5 Automatic progression

After successful processing:

```text
Toevoegen collapses
→ Controleren opens automatically
```

After explicit review completion:

```text
Controleren collapses
→ Downloaden opens automatically
```

The transition should feel like the workspace advancing, not a page reload/navigation event.

### 6.6 Explicit return/edit

A user may deliberately return to an earlier eligible stage.

The action must be explicit, understandable and reversible where appropriate.

If the user changes input or a processing-affecting setting, downstream review/export lineage is invalidated according to `premium_core_flow_state.py`. Stale output must never remain visually presented as current.

### 6.7 One dominant primary action

Each active stage has one visually dominant primary action.

Target examples:

```text
Toevoegen:     Document verwerken
Controleren:   Controle afronden
Downloaden:    Document downloaden
```

Secondary actions remain subordinate and should not compete visually.

### 6.8 No nested core-flow accordion hierarchy

Standard must not re-create form complexity through nested expanders inside the active stage.

Where secondary disclosure is necessary, prefer:

- inline contextual reveal;
- a compact secondary action;
- a modal/popover where technically appropriate and safe;
- Expert mode for genuinely technical controls.

Do not build an accordion inside an accordion as the default Standard interaction pattern.

### 6.9 Stage panels, not generic Streamlit expanders

The interaction may use Streamlit primitives internally, but the user-facing presentation should read as a staged application workspace.

The stage header should communicate:

- stage number/name;
- status: active/completed/future;
- compact summary when completed;
- explicit edit/return affordance where allowed.

Avoid generic `st.expander` visual language when it reinforces a settings-form feeling.

## 7. Standard and Expert relationship

`Standaard` and `Expert` are presentation modes over the same processing state.

Standard:

- staged workspace is the dominant interaction model;
- no permanent configuration sidebar;
- one primary task/action at a time;
- advanced settings, alternate output formats, Scrub Key and detailed audit are progressively disclosed.

Expert:

- may expose additional inspection/tuning surfaces;
- may retain the configuration sidebar or equivalent advanced controls;
- must preserve the same authoritative document lineage and review semantics;
- may not silently process a different document state from Standard.

Switching Standard ↔ Expert is presentation-only unless an explicitly changed expert setting affects processing; such a setting change must then invalidate downstream state according to the state model.

## 8. Top-level workflows

The staged-workspace decision does not collapse `Anonimiseren` and `Terugzetten` into one ambiguous flow.

Top level remains:

```text
Anonimiseren | Terugzetten
```

The three-stage staged workspace is the binding Standard pattern for the anonymization core flow.

The Reinsert/Terugzetten flow should follow the same Premium principles — one task at a time, minimal controls, clear source/key/output state — but its exact staged structure remains governed by its own existing behavior and future dedicated UI work. This decision must not silently alter reinsert semantics.

## 9. Safety and state invariants

This UI decision must not change:

- recognizers or thresholds;
- replacement decisions;
- review-table authority;
- direct missed-value masking semantics;
- export bytes, filenames or MIME types;
- Scrub Key schema, binding, warning or lifecycle;
- reinsert semantics;
- audit evidence;
- local-processing boundaries;
- human-review requirement.

The UI must fail closed on stale state:

```text
source/profile/threshold change affecting processing
→ processed lineage invalid
→ reviewed lineage invalid
→ export lineage invalid
→ user returned to appropriate earlier stage
```

## 10. Visual hierarchy principles

Premium does not mean decoration. It means controlled hierarchy.

Standard should prioritize:

1. document identity/context;
2. current stage/task;
3. current primary action;
4. required review information;
5. secondary safety/audit controls only when relevant.

Avoid:

- multiple equally prominent buttons;
- permanent explanatory text blocks;
- repeated labels already implied by stage context;
- technical variable-like terms;
- duplicated upload/input surfaces;
- default-open diagnostics;
- stacked download buttons of equal weight;
- nested accordion trees.

## 11. Workpackage realignment

This decision intervenes in the current Premium sequence before production integration in PR #85.

### Immediate package

`SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE`

Deliverables:

- this decision document;
- roadmap update;
- workpackage queue update;
- changelog entry;
- binding note on active App Shell issue/PR.

No runtime product behavior changes.

### Current package — amended, not discarded

`SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION`

PR #85's existing pure presentation helpers/tests remain reusable.

Before production Streamlit integration, extend/freeze its acceptance criteria so the shell represents:

- all three persistent stage headers;
- exactly one active/expanded stage;
- completed/future/active stage presentation states;
- compact completed summaries;
- passive future states;
- automatic next-stage progression hooks;
- explicit prior-stage return/edit affordances;
- no permanent Standard configuration sidebar;
- no three-page routing for the core stages.

Only after these shell semantics are testable should `presidio_streamlit.py` production integration proceed.

### Subsequent stage packages

`SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`

- reduce Toevoegen to source + essential profile/context + one primary process action;
- hide nonessential tuning in Standard;
- preserve ingestion and processing semantics.

`SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION`

- make side-by-side/document review dominant;
- retain review table as authoritative fallback/source of truth;
- keep direct missed-value masking accessible;
- move technical review controls out of the primary visual hierarchy.

`SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION`

- present one recommended cleaned-document download as dominant;
- make alternate formats, Scrub Key and audit evidence secondary but accessible;
- do not alter export semantics.

`SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION`

- prove Standard hides complexity without removing capability;
- prove Standard/Expert switching preserves valid state;
- prove processing-affecting Expert changes invalidate downstream state correctly;
- prove no safety/export/reinsert capabilities disappeared.

`SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT`

- verify deployment and actual live staged-workspace behavior;
- require coordinator/user UX confirmation because UI behavior changed;
- close only after exact GitHub Actions, Hugging Face synchronization and app verification evidence.

## 12. Acceptance criteria for the final Premium Standard core flow

The final Premium Standard line is not complete until live app verification confirms all of the following:

1. The first impression is a task workspace, not a long form.
2. `Toevoegen`, `Controleren`, `Downloaden` remain visible as the workflow structure.
3. Only one stage exposes its full contents at a time.
4. Successful stage completion automatically advances the active workspace.
5. Completed stages collapse to useful one-line/compact summaries.
6. Future stages do not compete for attention.
7. Returning to an earlier stage is obvious.
8. Processing-affecting earlier changes visibly invalidate stale downstream results.
9. There is one dominant primary action per active stage.
10. Standard has no permanent configuration sidebar.
11. The review surface remains sufficiently powerful for mandatory human review.
12. The recommended cleaned-document download is dominant in the final stage.
13. Scrub Key, alternate formats and audit remain accessible but secondary.
14. No nested-expander form hierarchy has replaced the old long form.
15. No export, Scrub Key, reinsert, recognition or audit semantics changed unintentionally.

## 13. Non-goals

This decision does not authorize:

- a frontend framework migration;
- cloud document processing;
- a full document editor;
- occurrence-specific replacement;
- redesign of anonymization algorithms;
- new export formats;
- Scrub Key semantic changes;
- reinsert semantic changes;
- packaging/installer work.

## 14. Governance and execution boundary

The Premium UI is consequential production-facing work.

Implementation workers create identifiable candidates and machine evidence. Separate `governance_release_assurance` workers issue `PASS | FAIL | INDETERMINATE` and may not silently repair candidates.

The current PR #85 must not be merged merely because its primitive helper tests are green. It must first incorporate this approved staged-workspace direction, complete its production integration, pass exact-head regression, and receive independent assurance.

## 15. Short design test

When uncertain whether a control belongs in Standard, ask:

```text
Does the user need this to complete the current stage safely?
```

If no:

```text
hide it, defer it, summarize it, or move it to Expert/secondary disclosure.
```

When uncertain whether a new screen is needed, ask:

```text
Is this a different top-level job, or merely another state of the same document?
```

For `Toevoegen → Controleren → Downloaden`, the answer is: another state of the same document. Therefore it remains one staged workspace.