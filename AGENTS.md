# AGENTS.md — SolidPrivacy Scrub

These instructions apply to the full repository.

## Repository scope

Work only in:

```text
solidprivacy-nl/scrub
```

Use `solidprivacy-nl/solidprivacy` only when an explicitly shared SolidPrivacy workflow/component is required by the current workpackage. Do not modify unrelated repositories.

## Required start sequence

Before starting any task, read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

For consequential work also read:

1. `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
2. `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`

Read `RISK_REGISTER.md`, `DECISION_LOG.md` and relevant product contracts for the affected surface.

GitHub is the source of truth. If canonical docs conflict with current source/runtime evidence, surface and reconcile the conflict rather than silently selecting one.

## Engineering doctrine

Follow the SolidPrivacy Execution & Engineering Constitution:

- business outcome first;
- smallest complete solution;
- solid but simple;
- no overengineering;
- first-principles reasoning;
- proven/native solutions before custom machinery;
- one source of truth;
- remove obsolete/conflicting active paths;
- verify behavior and security;
- Done requires implementation, verification, cleanup and documentation alignment.

## Current strategic direction

The active line is:

```text
Repository Convergence
→ Scrub Private Application
→ Private Service
→ External Product & Service Assurance
→ Pilot
```

Normal new feature development is paused until `SCRUB_REPOSITORY_CONVERGED`.

After convergence, `main` becomes the active Scrub Private line.

Hugging Face is a synthetic/approved-test application-validation environment, not the final confidential-production trust environment.

Local/offline functionality is preserved/deferred. Do not restart old installer or historical Premium work merely because old files/issues mention it.

Do not build a new Evidence Framework; reuse and reconcile the existing validation systems.

## Worker claim rule

Before implementation, claim one specific workpackage in `workpackage_claims/` with:

- workpackage title;
- role;
- issue/branch where applicable;
- exact starting base;
- scope and exclusions;
- required validation.

Do not claim multiple overlapping shared-surface packages in one worker.

## Implementation and assurance separation

Consequential work uses two separated roles:

```text
implementation_operations
governance_release_assurance
```

Implementation may create a candidate but may not certify it.

Assurance must use a fresh independent worker/session, reconstruct exact source/evidence, and record `PASS`, `FAIL` or `INDETERMINATE`. Before its initial verdict it must not rely on implementation handovers, self-assessments or conclusions. Assurance may not silently repair what it reviews.

A changed/repaired exact head requires a fresh assurance pass.

## Workpackage sizing

Use small coherent root-cause packages.

Do not create one giant convergence PR. Do not fragment trivial administrative edits into meaningless ritual packages.

**Do not refactor for aesthetics.**

During Repository Convergence, a cleanup/refactor requires a concrete current reason such as duplicate/contradictory/dead behavior, privacy/security risk, obsolete compatibility, meaningful maintenance burden, runtime instability or evidence-authority ambiguity.

“A cleaner architecture” alone is not sufficient.

## Shared-surface sequencing

Avoid uncoordinated parallel edits to:

- `presidio_streamlit.py`;
- Streamlit/Docker startup behavior;
- review table/direct-correction flow;
- processing-generation state;
- export/download flow;
- Scrub Key/reinsert paths.

Keep shared runtime/UI integration sequential unless explicit coordination proves independence.

## Testing and deployment

Where tools allow, workers self-check:

1. relevant focused tests;
2. full GitHub Actions on the exact candidate when required;
3. failed-job logs;
4. exact-main Actions after authorized merge;
5. GitHub→Hugging Face sync when applicable;
6. deployed/live app verification when visible/runtime behavior changed.

Do not treat code inspection alone as proof.

## Documentation ownership

- `ROADMAP.md` = strategic stages, not implementation history.
- `WORKPACKAGES.md` = one current executable queue.
- `CHANGELOG.md` = current implementation history; exact pre-convergence history is preserved in `history/CHANGELOG_PRE_CONVERGENCE_20260904.md` and Git at the baseline SHA.
- `DECISION_LOG.md` = accepted current binding decisions.
- `RISK_REGISTER.md` = current risks.
- temporary audit/debt ledgers = execution evidence only; they must not become competing permanent status authorities.

## Handover

Every worker writes:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

Include:

- repository;
- workpackage;
- role/status;
- exact candidate/baseline identity where relevant;
- files added/changed;
- tests;
- validation;
- GitHub Actions;
- Hugging Face sync;
- app verification;
- remaining risks/blockers;
- next recommended step.

## Safety

- Do not weaken human review/privacy controls.
- Do not silently change export or Scrub Key semantics.
- Treat false negatives as product-critical.
- Treat Scrub Keys as sensitive re-identification material.
- Use synthetic data only.
- Do not store secrets/tokens/real personal data.
- Preserve legal and clinical meaning.
- Do not introduce external/cloud document processing unless explicitly approved for the relevant product line.
- Do not claim perfect anonymisation/recall or production readiness from synthetic tests.

For Scrub Private, the target is no intentional persistent customer document content, no content-bearing ordinary logs, no document-content backup and no third-party document-processing egress. Minimal non-document control-plane metadata may persist only when justified by a real service requirement.
