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

### WP13 / WP13B — v13.7 TXT reinsert upload/download UI and app verification closeout

Status: completed and app-verified after Actions/sync verification.

WP13 implemented latest commit:

```text
443d6af99cfac47ed007d0d1cd666d1549e855d5
```

WP13 added:

- `tests/test_txt_reinsert_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_7_txt_reinsert_upload_download_ui.md`

WP13B added:

- `handover/workpackages/20260608_0015_v13_7_txt_reinsert_upload_download_ui_app_closeout.md`

WP13 changed:

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP13B changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Implemented behavior inside `Originele waarden terugzetten`:

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

App verification confirmed by coordinator/user:

- `Originele waarden terugzetten` mode is active.
- `Scrub Key laden` is visible.
- Scrub Key JSON is loaded.
- Pasted-text reinsert remains available.
- `TXT-bestand terugzetten` is visible.
- TXT file upload works.
- `Zet TXT-bestand lokaal terug` works with a valid Scrub Key.
- Result message appears: `37 waarde(n) lokaal teruggezet in het TXT-bestand.`
- `Herstelde TXT-tekst` appears.
- `Download hersteld TXT-bestand (.txt)` is visible.
- `Controleverslag TXT terugzetten` appears.
- Audit shows document type `txt`.
- Audit shows mapping counts, restored value count, not-found placeholders, unknown placeholders and validation issues.
- Audit shows `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Boundaries preserved:

- No code or test files changed in WP13B.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI/cloud behavior added.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior remains unchanged.
- Existing Scrub Key export/import behavior remains unchanged.
- Existing pasted-text reinsert remains available.

---

## Active / next recommended workpackage

### WP14 — v13.8 DOCX reinsert upload/download UI

Status: recommended next implementation workpackage after v13.7 app verification closeout.

Goal:

- Add controlled DOCX upload/download support for local reinsert in `Originele waarden terugzetten`.
- Reuse the existing `reinsert_docx_bytes(content, scrub_key)` helper.
- Keep pasted-text reinsert and TXT reinsert upload/download available.
- Preserve existing anonymization export/download semantics.
- Do not add PDF reinsert.
- Do not add AI/cloud behavior.

Known DOCX helper limitations from v13.4 foundation:

- Supports `word/document.xml`, normal body paragraphs and tables inside `word/document.xml`.
- Does not yet support placeholders split across multiple Word runs, headers, footers, comments, tracked changes or metadata cleaning.
- Do not claim perfect DOCX formatting preservation.

Recommended later workpackage:

```text
WP15 — PDF text extraction reliability review only
```

---

## Recommended execution order

1. Start WP14 only after v13.7 closeout is recorded.
2. Implement DOCX reinsert upload/download UI sequentially.
3. Verify GitHub Actions tests.
4. Verify GitHub to Hugging Face sync.
5. App-verify DOCX reinsert behavior.
6. Keep PDF full reinsert out of scope until a separate reliability review.
7. Keep AI/cloud behavior out unless explicitly approved.
8. Preserve export/download and Scrub Key import/export semantics.
