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

App verification was confirmed by coordinator/user for TXT upload/download reinsert.

Boundaries preserved:

- No DOCX upload reinsert UI was added in WP13.
- No PDF reinsert was added.
- No AI/cloud behavior was added.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior remained unchanged.
- Existing Scrub Key export/import behavior remained unchanged.
- Existing pasted-text reinsert remained available.

---

## Current implementation workpackages

### WP14 — v13.8 DOCX reinsert upload/download UI

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Implementation commits:

```text
83f7ebb0afea4798e4295b088b0a3f8058a9a64d
292d34ea8e4f179b5e93ebfcd93397891cf6e659
e36915b61d21d10a2fb30ebe9f7d5b8581c561f3
22b7066cd89c98f3e81e87ec5cf96ee07e5b58b5
```

Changed files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `tests/test_txt_reinsert_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Added files:

- `tests/test_docx_reinsert_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_8_docx_reinsert_upload_download_ui.md`

Implemented behavior inside `Originele waarden terugzetten`:

```text
DOCX-bestand terugzetten
Upload een DOCX-bestand met placeholders
Zet DOCX-bestand lokaal terug
DOCX-bestand lokaal teruggezet
Download hersteld DOCX-bestand (.docx)
Controleverslag DOCX terugzetten
```

The UI uses the existing deterministic local helper:

```python
reinsert_docx_bytes(content, scrub_key)
```

Existing pasted-text reinsert remains available.

Existing TXT upload/download reinsert remains available.

DOCX limitations are shown in the UI:

- supports normal document text and tables in this version;
- headers, footers, comments, tracked changes and placeholders split over multiple Word text fragments are not fully supported;
- no perfect DOCX formatting preservation is claimed.

Validation status:

- Added `tests/test_docx_reinsert_ui_patch.py` to verify DOCX helper import/use, labels, `.docx` upload-only configuration, Scrub Key requirement, reinsert-mode-only placement, limitations warning, audit summary, existing pasted-text/TXT flows, existing anonymization/export markers, no PDF reinsert, no AI/cloud behavior and no export rewiring.
- Updated `tests/test_two_mode_ui_patch.py` to include DOCX in the reinsert branch and continue guarding mode separation, anonymization flow and no PDF/AI/cloud behavior.
- Updated `tests/test_txt_reinsert_ui_patch.py` so TXT remains guarded while DOCX is now an allowed WP14 feature.
- Local test execution was not performed in this connector session.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required because UI behavior changed.

Boundaries preserved:

- `presidio_streamlit.py` was not directly edited.
- No PDF reinsert was added.
- No AI calls were added.
- No cloud processing was added.
- No automatic document rehydration beyond the documented local DOCX helper was added.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior was not intentionally changed.
- Existing TXT reinsert upload/download behavior was not intentionally changed.
- Existing pasted-text reinsert was not removed.
- Existing Scrub Key JSON export/import behavior was not intentionally changed.
- No Scrub Keys, secrets, tokens or real personal data were stored.

---

## Active / next recommended workpackage

### WP14-CLOSEOUT — v13.8 DOCX reinsert upload/download UI app verification closeout

Status: recommended next workpackage after coordinator evidence.

Goal:

- Verify GitHub Actions tests.
- Verify GitHub to Hugging Face sync.
- App-verify DOCX upload/download reinsert behavior.
- Close WP14 only after evidence confirms the UI works safely within documented DOCX helper limits.

Required app verification:

In `Anonimiseren`:

- anonymization workflow remains available;
- source text/file input remains visible;
- review table remains visible;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- Scrub Key JSON export remains available;
- DOCX reinsert upload UI is not shown as part of the anonymization workflow.

In `Originele waarden terugzetten`:

- `Scrub Key laden` remains visible;
- Scrub Key upload/paste validation remains visible;
- pasted-text reinsert remains visible;
- TXT reinsert upload/download remains visible;
- `DOCX-bestand terugzetten` is visible;
- DOCX upload accepts `.docx`;
- `Zet DOCX-bestand lokaal terug` works with a valid Scrub Key;
- restored DOCX download appears;
- `Download hersteld DOCX-bestand (.docx)` works;
- `Controleverslag DOCX terugzetten` appears;
- DOCX limitations warning is visible;
- warning about restored sensitive/confidential data is visible;
- local-only / no-AI / no-cloud text is visible.

Also confirm:

- no PDF reinsert appears;
- no AI/cloud behavior appears;
- existing Scrub Key export/import remains available;
- existing scrubbed export/download semantics are unchanged.

Recommended later workpackage:

```text
WP15 — PDF text extraction reliability review only
```

---

## Recommended execution order

1. Verify WP14 GitHub Actions and Hugging Face sync.
2. Verify DOCX reinsert upload/download behavior in the app.
3. Close WP14 through closeout if verification is green.
4. Keep PDF full reinsert out of scope until a separate reliability review.
5. Keep AI/cloud behavior out unless explicitly approved.
6. Preserve export/download and Scrub Key import/export semantics.
