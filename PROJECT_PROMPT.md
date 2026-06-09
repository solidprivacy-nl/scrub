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

Then read these when relevant:

- `RISK_REGISTER.md` for product, privacy and trust risks;
- `DECISION_LOG.md` for strategic decisions and architectural boundaries;
- `RELEASE_NOTES.md` for user-facing product changes;
- `STATUS_MONITORING_RUNBOOK.md` for Actions/sync monitoring procedure;
- relevant specs such as `SCRUB_KEY_SPEC.md` and `PDF_TEXT_REINSERT_UI_PLAN.md`.

Use these files as follows:

- `PROJECT_PROMPT.md` = full worker rules and operating model.
- `PROJECT_PROMPT_SHORT.md` = short bootstrap prompt suitable for ChatGPT Project Instructions.
- `ROADMAP.md` = product vision, risk-driven strategic direction, phase order, architecture.
- `WORKPACKAGES.md` = current executable workpackages, dependencies, parallelization rules.
- `CHANGELOG.md` = internal implementation history.
- `RELEASE_NOTES.md` = human/user-facing product change summary.
- `RISK_REGISTER.md` = active risk list and mitigation ownership.
- `DECISION_LOG.md` = accepted strategic/product/architecture decisions.

Do not invent a new direction if it conflicts with these files. If the roadmap is stale, unclear, or internally inconsistent, report that first.

---

## Current way of working

Work in small, testable workpackages.

Scrub is now run as a risk-driven privacy product, not as a simple feature ladder. The highest priority risks are:

1. missed sensitive data / false negatives;
2. Scrub Key leakage or misuse;
3. hidden document content and metadata;
4. cloud/demo trust gap versus local-first promise;
5. placeholder corruption during AI roundtrip;
6. UI review limitations that prevent reliable human review.

For each workpackage:

1. Confirm the workpackage title and scope.
2. Check dependencies in `WORKPACKAGES.md`.
3. Check `RISK_REGISTER.md` when the work touches detection, Scrub Key, export, document parsing, UI review or deployment.
4. Check `DECISION_LOG.md` when the work touches strategy, architecture or explicit product boundaries.
5. Prefer helper modules and tests before UI changes.
6. Avoid parallel edits to the same UI patch area.
7. Add or update tests where meaningful.
8. Update `CHANGELOG.md` for implementation history.
9. Update `RELEASE_NOTES.md` for user-visible product changes.
10. Update `ROADMAP.md` only when strategy, phase status, risk priority or sequence changes.
11. Update `WORKPACKAGES.md` when execution status, dependencies or next workpackages change.
12. End with a handover summary.
13. Write the handover summary to `handover/workpackages/`.

---

## Parallelization rule

Safe to do in parallel:

- helper modules with separate files;
- tests that do not touch the same UI patch;
- specifications;
- documentation;
- benchmark data design;
- risk reviews;
- non-UI architecture work.

Do not do in parallel without explicit coordination:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- any additional Streamlit patch file that edits the same UI flow;
- review table UI flow;
- export/download UI flow;
- shared workflow state;
- Docker/runtime startup patch order.

When in doubt, keep UI integration sequential.

---

## Testing, sync and self-monitoring

After implementation, workers must not rely on coordinator screenshots as the first verification path.

Workers should self-check, where connector permissions allow:

1. GitHub Actions status for the relevant commit.
2. GitHub to Hugging Face sync status for the relevant commit.
3. Failed-job logs when Actions are red.
4. Whether a fix workpackage is needed before asking for app verification.

Use `STATUS_MONITORING_RUNBOOK.md` for the monitoring procedure.

Only ask the coordinator/user for:

- app verification when UI behavior changed;
- missing permissions or inaccessible logs;
- subjective UX confirmation;
- explicit approval for gated workpackages.

Do not claim functional success until either tests prove it or the user confirms it in the app.

---

## Changelog and release-notes discipline

Every meaningful internal change must be reflected in `CHANGELOG.md`.

Include:

- workpackage/version;
- status;
- purpose;
- files added/changed;
- main changes;
- tests;
- validation status;
- intentionally not changed.

For user-visible product changes, also update `RELEASE_NOTES.md` in human language.

Keep `CHANGELOG.md` as an internal implementation log. Keep `RELEASE_NOTES.md` as the product-facing summary.

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
- Do not store secrets, tokens or real personal data.
- Use synthetic data only.
- Preserve legal context: replace sensitive values, not legal meaning.
- Be honest about uncertainty, failed validation or incomplete implementation.
- Treat the Scrub Key as sensitive data because it can re-identify scrubbed content.
- Treat false negatives as a product-critical risk, not as a cosmetic bug.

---

## Product direction

The product direction remains:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The first product wedge remains Dutch confidential professional documents, with Legal and Zorg as the most relevant early validation markets.

The broader direction is a local-first Dutch privacy scrubber for professional confidential documents.

The immediate development discipline is now risk-driven:

```text
Stabilize open UI work → Trust/recall benchmark → Scrub Key security → Placeholder robustness → Document hygiene → Document-centric review → Local runtime → Pilot validation → Scale features
```
