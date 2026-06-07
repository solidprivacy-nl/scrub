# SolidPrivacy Scrub — Short Project Prompt

Use this short prompt in ChatGPT Project Instructions. The full worker instruction is in `PROJECT_PROMPT.md`.

---

You are working on the SolidPrivacy Scrub project.

Work only in:

```text
solidprivacy-nl/scrub
```

GitHub is the source of truth. At the start of every work session, read:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Follow the current workpackage plan in `WORKPACKAGES.md`. Do not invent a new direction if it conflicts with the roadmap.

Use small, testable workpackages. Prefer helper modules and tests before UI changes. Avoid parallel edits to the same UI flow, especially:

- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- review table flow
- export/download flow

After meaningful changes:

- update `CHANGELOG.md`;
- update `ROADMAP.md` only when strategy or phase order changes;
- update `WORKPACKAGES.md` when execution status or next workpackages change;
- verify GitHub Actions tests;
- verify GitHub to Hugging Face sync;
- ask for app verification when UI behavior changed.

Every worker must end with a handover summary and also write it to:

```text
handover/workpackages/
```

Use filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

The handover must explicitly state:

- repository worked in;
- workpackage title;
- status;
- files added/changed;
- tests;
- validation status;
- GitHub Actions status;
- Hugging Face sync status;
- app verification status;
- remaining risks;
- next recommended step.

Safety rules:

- Do not weaken privacy or review controls.
- Do not silently change export semantics.
- Do not introduce cloud document processing unless explicitly approved.
- Do not store secrets, tokens, or real personal data.
- Use synthetic data only.
- Preserve legal context: replace sensitive values, not legal meaning.

Product direction:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

Immediate line: v12 Review UX, then v13 Scrub Key / Reinsert.
