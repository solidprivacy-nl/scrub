# SolidPrivacy Scrub — Workpackages

This file translates `ROADMAP.md` into executable workpackages.

Use:

- `PROJECT_PROMPT.md` for full worker instructions and operating rules.
- `PROJECT_PROMPT_SHORT.md` for the compact ChatGPT Project Instructions version.
- `ROADMAP.md` for product direction and phase order.
- `WORKPACKAGES.md` for immediate execution planning and parallelization.
- `CHANGELOG.md` for implementation history.

---

## Mandatory worker start sequence

Every worker must start by reading, in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

If the active repository is not `solidprivacy-nl/scrub`, stop and report the mismatch.

Every worker must end with a handover summary and write that summary to:

```text
handover/workpackages/
```

Filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

---

## Current execution principle

Avoid parallel edits to the same Streamlit UI patch area.

Parallel work is safe for helper modules, tests, specifications, documentation and non-UI architecture work.

Parallel work is risky for:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- export/download UI blocks;
- shared replacement table flow.

UI integration should therefore happen sequentially.

---

## Completed prerequisite and UI workpackages

### WP0 — v12.3 stabilization check

Status: completed by user verification.

### WP1 — v12.4 Review guidance text

Status: completed.

### WP2 — v12.5 Final review summary

Status: completed and formally closed after verification.

### WP3 — v12.6 Export sanity checks

Status: completed and formally closed.

Outcome:

- v12 Review UX line is complete from WP1 through WP3.
- Existing export/download behavior was preserved.

---

## Completed strategic / helper workpackages

### WP4 — v13.0 Scrub Key specification and pure model

Status: completed.

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and app-verified.

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: completed.

### WP6 — v13.2 Scrub Key import/reload UI integration

Status: completed and app-verified.

### WP7A / WP7B / WP7B-FINAL — v13.3 Deterministic reinsert helper

Status: completed and formally closed after Actions/sync verification.

### WP8 — v13.3 Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

### WP8B / WP8C — v13.3 Deterministic reinsert UI implementation and app verification closeout

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local pasted-text reinsert UI is completed, app-verified and formally closed.
- No AI/cloud processing or document upload reinsert was added.
- Existing scrubbed export/download behavior was not changed.

### WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Outcome:

- Recommended two-mode direction: `Anonimiseren` and `Originele waarden terugzetten`.
- Recommended keeping pasted-text reinsert as fallback.
- Recommended controlled TXT/DOCX phases before PDF.
- Recommended local-only, deterministic, helper-first architecture.

### WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Outcome:

- Added pure TXT/DOCX helper foundation.
- No UI, PDF, AI/cloud, or export/download behavior change.

### WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

### WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

Outcome:

- Recommended moving Scrub to a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.

### WP12 / WP12-FIX / WP12-FIX2 / WP12B — v13.6 Two-mode UI implementation and app verification closeout

Status: completed and app-verified after Actions/sync verification.

Implementation sequence:

- WP12 introduced the two-mode UI skeleton.
- WP12-FIX cleaned up content separation.
- WP12-FIX2 fixed the generated indentation/runtime error around `Scrub Key laden`.
- WP12B closed the v13.6 two-mode UI line after successful technical verification and app verification.

Technical verification evidence:

```text
Tests #155 green — commit b27d115
Sync to Hugging Face Space #169 green — commit b27d115
Tests #156 green — commit 0e357bb
Sync to Hugging Face Space #170 green — commit 0e357bb
Tests #157 green — commit 268234d
Sync to Hugging Face Space #171 green — commit 268234d
```

Latest verified WP12-FIX2 commit:

```text
268234d9d1aeb9c82658c4c30702f51cfdd58c96
```

---

## Current implementation workpackages

### WP13 / WP13B — v13.7 TXT reinsert upload/download UI

Status: implemented; Actions/sync verified; awaiting app verification.

WP13 implemented latest commit:

```text
443d6af99cfac47ed007d0d1cd666d1549e855d5
```

WP13 added:

- `tests/test_txt_reinsert_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_7_txt_reinsert_upload_download_ui.md`

WP13 changed:

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP13 implemented behavior inside `Originele waarden terugzetten`:

```text
TXT-bestand terugzetten
Upload een TXT-bestand met placeholders
Zet TXT-bestand lokaal terug
Herstelde TXT-tekst
Download hersteld TXT-bestand (.txt)
Controleverslag TXT terugzetten
```

The UI uses:

```python
reinsert_txt_bytes(content, scrub_key, encoding="utf-8")
```

Pasted-text reinsert remains available as fallback.

WP13B closeout status:

- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: pending.
- WP13 is not yet marked completed/app-verified because no confirmed Hugging Face app verification evidence was supplied in this closeout request.
- No new tests were required or added in WP13B.
- No code files were changed in WP13B.

Technical verification evidence:

```text
Tests #164 green — commit e442d28
Sync to Hugging Face Space #178 green — commit e442d28
Tests #165 green — commit ce7721d
Sync to Hugging Face Space #179 green — commit ce7721d
Tests #166 green — commit 6bf359f
Sync to Hugging Face Space #180 green — commit 6bf359f
Tests #167 green — commit 443d6af
Sync to Hugging Face Space #181 green — commit 443d6af
```

Boundaries preserved in WP13B:

- Only documentation and handover files may be changed.
- No code or test files are changed in this closeout.
- No DOCX upload reinsert UI is added.
- No PDF reinsert is added.
- No AI/cloud behavior is added.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior remains unchanged.
- Existing Scrub Key export/import behavior remains unchanged.

---

## Active / next recommended workpackage

### WP13B-APPVERIFY — v13.7 TXT reinsert upload/download UI app verification completion

Status: recommended next step.

Goal:

- Complete the Hugging Face app verification checklist.
- If confirmed, close WP13 as completed and app-verified after Actions/sync verification.

Required app verification:

In `Originele waarden terugzetten`:

- `Scrub Key laden` remains visible;
- Scrub Key upload/paste validation remains visible;
- pasted-text reinsert remains visible;
- `TXT-bestand terugzetten` is visible;
- TXT upload accepts `.txt`;
- `Zet TXT-bestand lokaal terug` works with a valid Scrub Key;
- `Herstelde TXT-tekst` appears;
- `Download hersteld TXT-bestand (.txt)` works;
- `Controleverslag TXT terugzetten` appears;
- warning about restored sensitive/confidential data is visible;
- local-only / no-AI / no-cloud text is visible.

In `Anonimiseren`:

- normal anonymization workflow remains available;
- source text/file input remains visible;
- review table appears;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- Scrub Key JSON export remains available;
- TXT reinsert upload UI is not shown as part of the anonymization workflow.

Also confirm:

- no DOCX upload reinsert UI appears yet;
- no PDF reinsert appears;
- no AI/cloud behavior appears;
- existing Scrub Key export/import remains available;
- existing scrubbed export/download semantics are unchanged.

Recommended later workpackages after app verification:

```text
WP14 — v13.8 DOCX reinsert upload/download UI
WP15 — PDF text extraction reliability review only
```

---

## Recommended execution order

1. Complete WP13 app verification in Hugging Face.
2. If green, perform a short WP13 app-verification completion closeout.
3. After TXT UI is app-verified, implement DOCX reinsert upload/download UI.
4. Keep PDF full reinsert out of scope until a separate reliability review.
5. Keep AI/cloud behavior out unless explicitly approved.
6. Preserve export/download and Scrub Key import/export semantics.
