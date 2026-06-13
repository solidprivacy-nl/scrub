# Handover — WP39D DOCX hygiene audit UI implementation

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP39D — DOCX hygiene audit UI implementation`

Coordinator approval noted: explicit.

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented a small report-only DOCX hygiene audit panel in the existing Scrub Streamlit interface.

The new panel uses the existing `docx_hygiene_audit.py` helper and appears near the existing DOCX download button. It reports DOCX hygiene risk and supported findings, but does not mutate documents, block export, change download buttons, change Scrub Key behavior or change reinsert behavior.

## Files added

- `docx_hygiene_audit_panel_ui.py`
- `tests/test_docx_hygiene_audit_ui_patch.py`
- `workpackage_claims/WP39D_docx_hygiene_audit_ui_implementation.md`
- `handover/workpackages/20260613_1405_docx_hygiene_audit_ui_implementation.md`

## Files changed

- `presidio_streamlit.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP39D_docx_hygiene_audit_ui_implementation.md`

## Tests added/updated

Added `tests/test_docx_hygiene_audit_ui_patch.py` with static checks for:

- `presidio_streamlit.py` importing and using `render_docx_hygiene_audit_panel`;
- `docx_hygiene_audit_panel_ui.py` using `build_docx_hygiene_audit_report` from `docx_hygiene_audit.py`;
- required visible UI text:
  - `DOCX hygiene audit`;
  - `Alleen rapportage`;
  - `Geen clean-DOCX garantie`;
  - `Export wordt niet geblokkeerd`;
  - `Bestaande export blijft ongewijzigd`;
  - metadata/opmerkingen/revisies/verborgen inhoud;
- no export blocking implementation markers;
- no DOCX cleaner/removal implementation markers;
- no Scrub Key or reinsert function calls in the renderer;
- no startup source mutation;
- no cloud/real-data behavior;
- no click-to-mark, advanced editor, full-document marking or raw HTML behavior.

## Tests/checks run

No shell, pytest or py_compile execution was available through the ChatGPT GitHub connector for the checked-out repository.

Expected checks:

```text
python -m py_compile presidio_streamlit.py
python -m py_compile docx_hygiene_audit_panel_ui.py
pytest tests/test_docx_hygiene_audit_ui_patch.py
pytest tests/test_docx_hygiene_audit.py tests/test_docx_hygiene_audit_ui_plan.py tests/test_docx_hygiene_audit_ui_patch.py
pytest
```

Static source checks through GitHub connector:

- `presidio_streamlit.py` now imports `render_docx_hygiene_audit_panel`.
- `presidio_streamlit.py` calls `render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)` immediately before the existing DOCX download button.
- Existing DOCX download label, data, filename, MIME type and key remain unchanged.
- `fix_streamlit_nested_expanders.py` was read but not changed.

## Validation status

Implementation committed. Runtime validation is pending.

This package changes UI/runtime behavior, so it requires:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

## GitHub Actions status

Unknown at handover time. Actions must be checked for the final implementation/claim commit.

## Hugging Face sync status

Unknown at handover time. Sync must be checked after Actions.

## App verification status

Pending and required because UI/runtime behavior changed.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- existing export/download section remains visible;
- DOCX hygiene audit UI is visible;
- text makes clear it is report-only;
- no clean-DOCX claim;
- no export blocking;
- no static-highlight startup error.

## Boundaries preserved

- No DOCX cleaner implementation.
- No comments removal.
- No tracked changes removal.
- No metadata removal.
- No clean-DOCX claim.
- No export blocking.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.
- No startup source mutation.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No broad UI rewrite.

## Remaining risks

- The panel reports supported DOCX hygiene risks only; it does not clean files.
- Word comments, tracked changes, metadata and other hidden parts may still remain in DOCX outputs.
- No clean-DOCX export claim is supported.
- Export blocking remains unimplemented and requires separate approval.

## Next recommended step

```text
WP39D-VERIFY — closeout/app verification for DOCX hygiene audit UI after green Actions and Hugging Face sync.
```

Do not start without separate coordinator approval:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION
click-to-mark
advanced editor
full-document marking
clean DOCX export blocking
DOCX cleaner/removal
```
