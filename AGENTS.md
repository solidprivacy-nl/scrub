# AGENTS.md — SolidPrivacy Scrub

These instructions apply to the full repository.

## Repository scope

Work only in:

```text
solidprivacy-nl/scrub
```

Do not modify unrelated repositories. If the active repository is not `solidprivacy-nl/scrub`, stop and report the mismatch.

## Required start sequence

Before starting any task, read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Also read when relevant:

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RELEASE_NOTES.md`
- feature specs such as `SCRUB_KEY_SPEC.md` and `PDF_TEXT_REINSERT_UI_PLAN.md`

## Workpackage claim check

Before starting implementation or documentation changes for a workpackage, check `workpackage_claims/`.

If a claim file for the same workpackage already exists:

- status `in_progress`: stop and report that the package is already claimed;
- status `completed`: stop and report that the package is already done;
- status `blocked`: stop and read the blocking reason;
- status `abandoned`: continue only with coordinator approval.

If no claim exists, create a new claim file before editing code, tests, UI, export, schema or shared documentation files.

Use `GitHub.create_file` for the claim. Do not overwrite an existing claim. This is the lightweight lock that prevents two workers from silently starting the same package.

When the workpackage is done, update the same claim file to `completed` and record the final commit or PR, handover path, tests/checks, validation status, remaining risks and next recommended step.

## Product direction

The product direction is:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The roadmap is risk-driven. Highest risks:

1. false negatives / missed sensitive data;
2. Scrub Key leakage or accidental sharing;
3. hidden document content and metadata leakage;
4. cloud-demo trust gap versus local-first promise;
5. placeholder corruption during AI roundtrip;
6. review UX limitations;
7. PDF-scope misunderstandings.

## Safety rules

Do not weaken privacy or review controls.

Do not silently change export semantics.

Do not introduce cloud document processing unless explicitly approved.

Do not store secrets, tokens or real personal data.

Use synthetic data only.

Preserve legal/professional context: replace sensitive values, not legal meaning.

Treat the Scrub Key as sensitive re-identification data.

## Workpackage discipline

Work only on the assigned workpackage.

Do not broaden scope.

Do not start another workpackage unless explicitly instructed.

If the task is specification-only, do not change code, tests, dependencies or UI.

If the task is closeout-only, do not change code, tests, dependencies or UI.

If the task is implementation, prefer helper modules and tests before UI changes.

## Parallelization rules

Safe to work on in parallel:

- separate specification documents;
- helper modules in separate files;
- tests that do not touch the same UI flow;
- risk reviews;
- architecture plans;
- non-UI documentation.

Do not work in parallel without explicit coordination on:

- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- `fix_streamlit_pdf_text_reinsert.py`
- review table UI flow
- export/download UI flow
- shared workflow state
- Docker/runtime startup patch order

## Testing and validation

Run the tests named in the workpackage.

If no tests are required because the task is documentation-only or specification-only, state that clearly.

For implementation tasks, run targeted tests first, then related regression tests when practical.

Do not claim success if tests were not run. State the exact validation status.

## GitHub Actions and sync

Where possible, check GitHub Actions and GitHub-to-Hugging-Face sync status for the relevant commit.

If connector or environment access prevents status lookup, say so clearly.

Do not ask for app verification until Actions and sync are green.

UI changes require app verification by the coordinator/user.

## Documentation updates

Update these files according to the workpackage:

- `WORKPACKAGES.md` for status and next queue;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-visible product changes;
- `RISK_REGISTER.md` for risk state changes;
- `DECISION_LOG.md` for accepted strategic/architecture decisions.

Do not update `ROADMAP.md` unless strategy, phase order or product direction changes.

## Handover process

Every task must create a handover file in:

```text
handover/workpackages/
```

Filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

The handover file must include:

- repository worked in;
- workpackage title;
- status;
- files added;
- files changed;
- tests added/updated;
- validation status;
- GitHub Actions status;
- Hugging Face sync status;
- app verification status;
- remaining risks;
- next recommended step.

For Codex or other parallel worker tasks, do not paste the full handover into the coordinator chat when the handover has been committed to the repository.

Instead, the final worker response should provide only:

- workpackage title;
- status;
- commit SHA or PR link;
- handover file path;
- short summary of files added/changed;
- tests/checks run;
- remaining risks;
- next recommended step.

The coordinator can then read the committed handover from GitHub.

Only paste the full handover into chat if:

- the handover could not be committed;
- GitHub access failed;
- there is a conflict or permission issue;
- the coordinator explicitly asks for the full text.

## Conflict rule

Before editing shared documentation files, fetch the latest version.

If there is a SHA conflict, update conflict or missing permission, stop and report instead of overwriting another worker’s changes.

## Final response requirements

In the final response, summarize:

- what was changed;
- which files were touched;
- what tests/checks were run;
- what was intentionally not changed;
- remaining risks;
- next recommended step.
