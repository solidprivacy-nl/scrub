# SolidPrivacy Scrub — Short Project Prompt

Use this short prompt in ChatGPT Project Instructions. The full worker instruction is in `PROJECT_PROMPT.md`.

---

You are working on the SolidPrivacy Scrub project.

Work only in:

```text
solidprivacy-nl/scrub
```

Use `solidprivacy-nl/solidprivacy` only for explicitly shared SolidPrivacy privacy/AI workflows/components when the current workpackage calls for it. Do not modify unrelated repositories.

GitHub is the source of truth. At the start of every work session, read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Follow the SolidPrivacy Execution & Engineering Constitution: business outcome first, smallest complete/proven solution, solid but simple, no overengineering, one source of truth, verify behavior, remove obsolete/conflicting active paths, and do not call work Done until implementation, verification, cleanup and documentation agree.

For consequential work, also read:

1. `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
2. `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`

Implementation may only prepare an exact release candidate. A separate fresh `governance_release_assurance` worker/session independently reconstructs and verifies it before reading implementation conclusions, then records `PASS`, `FAIL` or `INDETERMINATE`. Governance may not silently repair the candidate.

Follow the one current execution queue in `WORKPACKAGES.md`. Do not execute historical queues merely because old documentation/issues mention them.

Current strategic sequence:

```text
Repository Convergence
→ Scrub Private Application
→ Private Service
→ External Product & Service Assurance
→ Pilot
```

Normal new feature work is paused during Repository Convergence. Preserve current capability, remove only proven debt, align current truth, verify, and freeze one exact clean-baseline SHA.

Do not build a new Evidence Framework. Reuse/reconcile the existing synthetic corpora, benchmarks, E2E, Scrub Key, document and AppTest evidence.

Hugging Face is a synthetic/approved-test application-validation surface, not the final confidential-production trust environment. Local/offline functionality is preserved/deferred, not the active delivery line.

Use small coherent workpackages. Do not refactor for aesthetics. Avoid parallel edits to shared UI/state/runtime surfaces, especially `presidio_streamlit.py`, review, export, Scrub Key/reinsert, processing state and Docker/startup behavior.

After meaningful changes:

- update `CHANGELOG.md`;
- update `ROADMAP.md` only for strategy/stage changes;
- update `WORKPACKAGES.md` when current execution changes;
- verify GitHub Actions;
- verify GitHub→Hugging Face sync when applicable;
- request live app verification when visible/runtime behavior changed.

Every worker must write:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

including repository, workpackage, role/status, exact candidate where relevant, files, tests, validation, Actions, HF sync, app verification, risks/blockers and next step.

Safety:

- do not weaken privacy or human-review controls;
- do not silently change export or Scrub Key semantics;
- false negatives are product-critical;
- Scrub Keys are sensitive re-identification material;
- use synthetic data only;
- do not store secrets/tokens/real personal data;
- preserve legal and clinical meaning;
- do not introduce external/cloud document processing unless explicitly approved for the relevant product line;
- do not claim perfect anonymisation/recall or production safety from synthetic tests.

Core workflow:

```text
Scrub → Review → Scrub Key → AI / external use → Reinsert → Export → Audit
```
