# Handover — WP8 — v13.3 Deterministic reinsert UI planning

Repository: solidprivacy-nl/scrub  
Workpackage title: WP8 — v13.3 Deterministic reinsert UI planning  
Status: implemented; reinsert UI implementation can start as a separate sequential workpackage

## Summary

Created a planning/specification document for future deterministic local reinsert UI integration.

This was a planning-only workpackage. No UI code, tests, helper logic, export behavior or download behavior was changed.

The new spec defines where the future reinsert UI should appear, what labels it should use, how it should use a validated Scrub Key, how it should call `reinsert_from_scrub_key(text, scrub_key)`, what output and audit summary it should show, which warnings must be visible, what must not happen automatically, and which tests the future UI implementation should include.

## Files added

- `REINSERT_UI_SPEC.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `fix_streamlit_nested_expanders.py`
- `presidio_streamlit.py`
- `scrub_key_reinsert.py`
- `scrub_key.py`
- `scrub_key_import.py`
- `tests/*`

## Tests

No tests were added or run.

Reason:

- This was a planning/specification-only workpackage.
- No UI behavior, helper behavior, tests, export behavior or download behavior changed.

## Validation status

Completed for planning scope.

The following files were inspected before writing the spec:

- `scrub_key_reinsert.py`
- `scrub_key.py`
- `scrub_key_import.py`
- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_reinsert.py`
- `tests/test_scrub_key_import_ui_patch.py`
- `tests/test_scrub_key_ui_patch.py`

## GitHub Actions status

Not required for this planning-only workpackage.

A sync/test run may still occur because documentation changed, but no functional code was changed.

## Hugging Face sync status

Not required for this planning-only workpackage.

A sync run may still occur as part of normal GitHub-to-Hugging-Face hygiene, but no app behavior changed.

## App verification status

Not applicable.

No UI behavior changed.

## Planning decisions recorded

The future reinsert UI should appear after the existing Scrub Key import/reload block near the current download/export area.

Suggested labels:

- Section: `Originele waarden terugzetten`.
- Input: `Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten`.
- Button: `Zet originele waarden lokaal terug`.
- Output: `Herstelde tekst`.
- Download: `Download herstelde tekst (.txt)`.

The future UI must call:

```python
reinsert_from_scrub_key(text, scrub_key)
```

The future UI must show audit fields for:

- mapping item count;
- active item count;
- excluded item count;
- replacement count;
- placeholders not found;
- unknown placeholders;
- duplicate placeholders;
- validation issues;
- local-only / no-AI / no-cloud status.

## Required warning recorded

```text
Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat zorgvuldig voordat u het deelt.
```

The spec also records that the UI must warn that:

- a Scrub Key is reversible/pseudonymization, not full anonymization;
- the key must remain local and protected;
- no AI/cloud processing is involved in the local reinsert step.

## Boundaries preserved

- No UI code changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No tests added or changed.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No TXT, CSV, DOCX or PDF export behavior changed.
- No Scrub Key JSON export behavior changed.
- No Scrub Key import/reload behavior changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- Future UI implementation will touch `fix_streamlit_nested_expanders.py`, which is a sensitive sequential UI patch area.
- Future UI implementation must not blur deterministic local reinsert with AI-output-specific behavior.
- Restored text may contain personal or confidential information and must be clearly warned and manually reviewed.
- The Scrub Key remains sensitive because it makes scrubbed values reversible.

## Next recommended step

Start a separate sequential UI workpackage:

```text
WP8B — v13.3 Deterministic reinsert UI implementation
```

Recommended scope:

- update `fix_streamlit_nested_expanders.py` only for the UI integration;
- add `tests/test_scrub_key_reinsert_ui_patch.py`;
- keep AI-output behavior separate unless explicitly approved;
- preserve all existing TXT/CSV/DOCX/PDF and Scrub Key import/export behavior;
- verify GitHub Actions and Hugging Face sync;
- ask for app verification because UI behavior will change.
