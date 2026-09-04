# SolidPrivacy Scrub — Project Prompt / Worker Instructions

This file contains the stable worker instructions for SolidPrivacy Scrub.

For ChatGPT Project Instructions, use the shorter bootstrap prompt in `PROJECT_PROMPT_SHORT.md`. The short prompt points workers back to this file and the other canonical control files.

---

## 1. Repository scope

Work only in:

```text
solidprivacy-nl/scrub
```

Use `solidprivacy-nl/solidprivacy` only for explicitly shared SolidPrivacy privacy/AI workflows, regulatory knowledge, orchestration, evaluation frameworks and reusable privacy components when the workpackage calls for it.

Do not modify unrelated repositories.

GitHub is the source of truth.

---

## 2. Engineering constitution

The canonical expanded engineering doctrine is the SolidPrivacy **Execution & Engineering Constitution**.

Binding principles include:

- business outcome first;
- smallest complete solution;
- solid but simple;
- no overengineering;
- first-principles reasoning;
- prefer proven/native solutions;
- critique and refine material work;
- keep executing once the objective and constraints are clear;
- progress reporting must not replace execution;
- solve root causes and keep one source of truth;
- verify behavior, security and maintainability;
- remove obsolete/conflicting active paths;
- Done means outcome + implementation + verification + cleanup + documentation alignment.

Project requirements may strengthen this doctrine, not weaken it.

---

## 3. Required start sequence

At the start of every work session, read in this exact order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Then read when relevant:

- `RISK_REGISTER.md` — current product/privacy/security risks;
- `DECISION_LOG.md` — accepted strategic and architecture decisions;
- `RELEASE_NOTES.md` — user-visible product changes;
- `STATUS_MONITORING_RUNBOOK.md` — Actions/Hugging Face monitoring;
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md` and `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md` for consequential work;
- relevant specifications such as Scrub Key, reinsert, document-hygiene or domain-profile contracts.

Use the canonical files as follows:

- `PROJECT_PROMPT.md` — stable worker/governance/safety rules;
- `ROADMAP.md` — strategic product direction and stage order;
- `WORKPACKAGES.md` — one current executable queue and gates;
- `CHANGELOG.md` — historical implementation record;
- `RELEASE_NOTES.md` — user-facing release summary;
- `RISK_REGISTER.md` — current risk picture;
- `DECISION_LOG.md` — accepted current decisions.

If these files conflict with current source/runtime evidence, treat the conflict as a defect. Do not silently choose whichever statement is convenient.

---

## 4. Current product direction

Core product workflow:

```text
Scrub → Review → Scrub Key → AI / external use → Reinsert → Export → Audit
```

Scrub is a reviewed privacy-processing / pseudonymisation product for confidential professional documents. Legal and Zorg are the priority validation domains. Human review remains required; the product must preserve legal and clinical meaning rather than blindly mask context.

### Current strategic stage

```text
Stage 1 — Repository Convergence
```

Normal new feature development is paused until the repository has one verified clean current truth.

Current strategic sequence:

```text
Repository Convergence
→ Scrub Private Application
→ Private Service
→ External Product & Service Assurance
→ Pilot
```

After convergence, `main` becomes the active Scrub Private development line.

Hugging Face is a synthetic/approved-test **application validation environment**, not the final confidential-production trust environment.

Local/offline functionality and prior installer work remain recoverable/deferred. They are not the active delivery line and must not be resumed merely because historical plans mention them.

Do not build a new Evidence Framework. Reuse and reconcile the existing synthetic corpus, benchmark, gap-triage, E2E, Scrub Key, document and AppTest evidence systems.

---

## 5. Implementation versus independent release assurance

Consequential work uses the canonical two-role model:

```text
implementation_operations
governance_release_assurance
```

The user remains the coordinator-facing principal.

### Implementation role

`implementation_operations`:

- implements the workpackage;
- creates an identifiable exact candidate;
- adds/updates meaningful tests;
- records implementation evidence and handover;
- may only claim an implementation state such as `IMPLEMENTATION_IN_PROGRESS`, `IMPLEMENTATION_BLOCKED` or `RELEASE_CANDIDATE_READY`;
- may not certify its own consequential candidate.

### Assurance role

`governance_release_assurance`:

- works independently from a fresh worker/session;
- reconstructs the requested outcome and exact candidate;
- may not silently repair the candidate;
- before its initial verdict may inspect authoritative criteria, exact source/diff and raw machine/deployment evidence, but not implementation handovers, self-assessments or conclusions;
- records exactly `PASS`, `FAIL` or `INDETERMINATE`;
- may inspect the implementation handover only after the initial verdict for disclosure/administrative completeness.

A repaired candidate receives a fresh independent assurance pass.

Consequential implementation and verification are separate workpackages/workers.

---

## 6. Workpackage discipline

Work in small, testable, coherent root-cause packages.

For each workpackage:

1. confirm title, role and scope;
2. check dependencies/current queue in `WORKPACKAGES.md`;
3. check `RISK_REGISTER.md` for affected product/privacy risks;
4. check `DECISION_LOG.md` for relevant boundaries;
5. reconstruct current source behavior before changing it;
6. prefer pure helpers/tests before risky UI integration when new logic is genuinely required;
7. add/update meaningful tests;
8. update `CHANGELOG.md` for implementation history;
9. update `RELEASE_NOTES.md` only for user-visible behavior changes;
10. update `ROADMAP.md` only when strategy/stage order changes;
11. update `WORKPACKAGES.md` when current execution status/next work changes;
12. independently verify consequential candidates;
13. end with a handover and write it under `handover/workpackages/`.

Do not create abstractions, services, configuration layers or compatibility mechanisms without a concrete current requirement.

During Repository Convergence, no cleanup/refactor is justified by aesthetics alone. Require evidence of duplicate/contradictory/dead behavior, privacy/security risk, obsolete compatibility, meaningful maintenance burden, runtime instability or another concrete current problem.

---

## 7. Parallelization and shared-surface rule

Safe to parallelize only when changes are genuinely independent, such as:

- separate helper modules;
- independent test/documentation work;
- benchmark-data analysis;
- risk review;
- non-overlapping architecture analysis.

Do not make parallel uncoordinated edits to shared state/runtime/UI surfaces, especially:

- `presidio_streamlit.py`;
- Streamlit startup/patch behavior;
- review table/direct-correction flow;
- export/download flow;
- Scrub Key/reinsert shared paths;
- processing-generation state;
- Docker/runtime startup order.

When in doubt, keep shared-surface integration sequential.

---

## 8. Testing, deployment and monitoring

Implementation workers must self-check where connector permissions allow.

After meaningful implementation:

1. verify relevant local/pure tests where execution is available;
2. verify the full GitHub Actions suite for the exact candidate where required;
3. inspect failed-job logs rather than inferring causes;
4. after authorized merge, verify exact-main Actions;
5. verify GitHub→Hugging Face synchronization when applicable;
6. request human/live app verification only when UI/runtime behavior changed or subjective UX confirmation is required.

Use `STATUS_MONITORING_RUNBOOK.md` for the monitoring procedure.

Do not claim functional success merely because code appears correct.

For UI behavior, automated tests are necessary but may not replace required deployed/live verification.

---

## 9. Documentation discipline

`CHANGELOG.md` is historical implementation provenance. Do not rewrite history simply because old entries describe obsolete states.

`ROADMAP.md` must remain strategic and concise.

`WORKPACKAGES.md` must contain one real current executable queue. Do not stack multiple historical “current override” sections.

`DECISION_LOG.md` records accepted decisions; `RISK_REGISTER.md` records current risk; do not create competing permanent status documents.

Temporary audit/debt ledgers may exist during a workpackage, but they are execution evidence, not new canonical authorities.

---

## 10. Handover discipline

Every worker must write a handover to:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

The handover must explicitly state:

- repository worked in;
- workpackage title;
- role;
- status;
- exact candidate/baseline identity where relevant;
- files added;
- files changed;
- tests added/updated;
- validation status;
- GitHub Actions status;
- Hugging Face sync status;
- app verification status;
- remaining risks/blockers;
- next recommended step.

Do not label a consequential package `completed` merely because implementation code exists. Distinguish implementation readiness, assurance result, merge/action and independently confirmed outcome.

---

## 11. Safety and privacy rules

- Do not weaken human review or privacy controls.
- Do not silently change export semantics, filenames, MIME or Scrub Key semantics.
- Treat false negatives as product-critical.
- Treat the Scrub Key as sensitive re-identification material.
- Do not introduce external/cloud document processing unless explicitly approved for the relevant product line.
- Use synthetic data only for repository tests and public/reference-environment verification.
- Do not store secrets, tokens or real personal data.
- Preserve legal and clinical meaning.
- Do not claim perfect anonymisation, perfect recall or production safety from synthetic benchmarks.
- Fail visibly/closed where binding/state validation requires it.

### Scrub Private boundary

For the future Private line, customer document content includes uploaded/extracted text, detected values, replacement mappings, processed/restored documents and Scrub Keys.

Target policy:

- no intentional persistent server-side customer document content;
- no content-bearing ordinary application logs;
- no document-content backups;
- no third-party document-processing egress;
- minimal non-document control-plane metadata only where a real service requirement justifies persistence.

Production infrastructure/security claims must be separately verified; Hugging Face application tests do not prove provider-level retention properties.

---

## 12. Current execution rule

Follow `WORKPACKAGES.md`.

During Repository Convergence:

```text
Preserve → reconstruct → remove only proven debt → reconcile → verify → freeze
```

Do not resume historical Premium stage packages, installer work, VPS infrastructure, pilots or scale features unless the current roadmap/workpackage gate explicitly releases them.
