# SolidPrivacy Scrub — Project Prompt / Worker Instructions

This file is the full project prompt for workers on SolidPrivacy Scrub.

For ChatGPT Project Instructions, use the shorter bootstrap prompt in `PROJECT_PROMPT_SHORT.md`. The short prompt points workers back to this file and the other central control files.

---

## Repository

Work only in:

```text
solidprivacy-nl/scrub
```

Do not modify unrelated repositories. If the active repository is not `solidprivacy-nl/scrub`, stop and report the mismatch.

---

## Source of truth

GitHub is the source of truth.

Always start by reading, in this order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Use these files as follows:

- `PROJECT_PROMPT.md` = full worker rules and operating model.
- `PROJECT_PROMPT_SHORT.md` = short bootstrap prompt suitable for ChatGPT Project Instructions.
- `ROADMAP.md` = product vision, strategic direction, phase order, bigger picture.
- `WORKPACKAGES.md` = current executable workpackages, dependencies, parallelization rules.
- `CHANGELOG.md` = historical implementation log.

Do not invent a new direction if it conflicts with these files. If the roadmap is stale, unclear, or internally inconsistent, report that first.

---

## Current way of working

Work in small, testable workpackages.

For each workpackage:

1. Confirm the workpackage title and scope.
2. Check dependencies in `WORKPACKAGES.md`.
3. Prefer helper modules and tests before UI changes.
4. Avoid parallel edits to the same UI patch area.
5. Add or update tests where meaningful.
6. Update `CHANGELOG.md` for implementation history.
7. Update `ROADMAP.md` only when strategy, phase status, or sequence changes.
8. Update `WORKPACKAGES.md` when execution status, dependencies, or next workpackages change.
9. End with a handover summary.
10. Write the handover summary to `handover/workpackages/`.

---

## Parallelization rule

Safe to do in parallel:

- helper modules;
- tests;
- specifications;
- documentation;
- non-UI architecture work.

Do not do in parallel without explicit coordination:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- review table UI flow;
- export/download UI flow;
- shared workflow state.

When in doubt, keep UI integration sequential.

---

## Testing and sync

After implementation:

1. Confirm GitHub Actions tests are green.
2. Confirm GitHub to Hugging Face sync is green.
3. Ask the coordinator/user to verify the Hugging Face app when visual or UI behavior changed.
4. Do not claim functional success until either tests prove it or the user confirms it in the app.

---

## Changelog discipline

Every meaningful change must be reflected in `CHANGELOG.md`.

Include:

- workpackage/version;
- status;
- purpose;
- files added/changed;
- main changes;
- tests;
- validation status;
- intentionally not changed.

Keep the changelog human-readable.

---

## Handover discipline

Every worker must end with a handover summary.

The handover must explicitly state:

- repository worked in;
- workpackage title;
- status;
- files added;
- files changed;
- tests added/updated;
- validation status;
- GitHub Actions status if known;
- Hugging Face sync status if known;
- app verification status if known;
- remaining risks or follow-up actions;
- next recommended step.

Also write the same handover summary to:

```text
handover/workpackages/
```

Use this filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

Example:

```text
handover/workpackages/20260607_1430_v12_5_final_review_summary.md
```

The coordinator can use this directory to automatically read worker updates.

### Handover template

```markdown
# Handover — <Workpackage title>

Repository: solidprivacy-nl/scrub  
Status: <completed / implemented / blocked / pending verification>

## Summary

<Short explanation of what was done.>

## Files added

- ...

## Files changed

- ...

## Tests

- ...

## Validation

- GitHub Actions: <green/red/unknown>
- Hugging Face sync: <green/red/unknown>
- App verification: <confirmed/pending/not applicable>

## Notes / risks

- ...

## Next recommended step

- ...
```

---

## Safety and quality rules

- Do not remove existing functionality unless the workpackage explicitly requires it.
- Do not silently change export semantics.
- Do not weaken privacy or review controls.
- Do not introduce cloud dependencies for document processing unless explicitly approved.
- Do not store secrets, tokens, or real personal data.
- Use synthetic data only.
- Preserve legal context: replace sensitive values, not legal meaning.
- Be honest about uncertainty, failed validation, or incomplete implementation.

---

## Product direction

The current product direction is:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The first market is Dutch legal documents.

The broader direction is a local-first Dutch privacy scrubber for professional confidential documents.

The immediate development line is v12 Review UX, followed by v13 Scrub Key / Reinsert.
