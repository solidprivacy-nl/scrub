# Handover — WP8B — v13.3 Deterministic reinsert UI implementation

Repository: solidprivacy-nl/scrub  
Workpackage title: WP8B — v13.3 Deterministic reinsert UI implementation  
Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification

## Summary

Implemented the deterministic local reinsert UI described in `REINSERT_UI_SPEC.md`.

The future user flow is now represented in the startup patch:

1. User has or loads a Scrub Key.
2. User pastes scrubbed or AI-generated text.
3. User explicitly clicks `Zet originele waarden lokaal terug`.
4. The app calls the verified helper `reinsert_from_scrub_key(...)` locally.
5. The app shows restored text, an audit summary and a `.txt` download for restored text.

This workpackage did not add AI calls, cloud processing, automatic document rehydration or DOCX/PDF reinsert.

## Files added

- `tests/test_scrub_key_reinsert_ui_patch.py`
- `handover/workpackages/20260607_1915_v13_3_reinsert_ui_implementation.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `presidio_streamlit.py`
- `scrub_key_reinsert.py`
- `scrub_key.py`
- `scrub_key_import.py`
- existing TXT/CSV/DOCX/PDF export implementation files

## Implementation details

Added import/wiring:

```python
from scrub_key_reinsert import reinsert_from_scrub_key
```

Added UI section:

```text
Originele waarden terugzetten
```

Added input label:

```text
Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten
```

Added action button:

```text
Zet originele waarden lokaal terug
```

Added output label:

```text
Herstelde tekst
```

Added download button:

```text
Download herstelde tekst (.txt)
```

Added audit summary section:

```text
Controleverslag terugzetten
```

The UI calls:

```python
reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)
```

The UI uses `st.session_state["active_scrub_key"]` when a key was imported successfully. If no imported key is active, it falls back to the current Scrub Key built from reviewed replacement rows.

## Tests

Added:

- `tests/test_scrub_key_reinsert_ui_patch.py`

Updated:

- `tests/test_scrub_key_ui_patch.py`

The new/updated tests guard:

- `reinsert_from_scrub_key` import and use;
- required UI labels;
- warning that restored text may contain personal/confidential data again;
- local-only/no-AI/no-cloud wording;
- explicit button-gated helper call;
- audit summary fields;
- preservation of existing Scrub Key export/import labels;
- preservation of existing download/export markers;
- no `st.stop()` or blocking behavior;
- no AI calls;
- no cloud calls;
- no automatic document rehydration;
- no DOCX/PDF reinsert markers;
- no changes to existing replacement application or scrubbed download functions.

## Validation status

Local targeted validation on a reconstructed subset passed:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py tests/test_scrub_key_reinsert_ui_patch.py tests/test_scrub_key_import_ui_patch.py tests/test_scrub_key_ui_patch.py
```

Result:

```text
57 passed
```

Full repository test suite was not run from this connector environment.

## GitHub Actions status

Pending for WP8B commits.

Commits created in this workpackage:

- `ada543c989f45d083c2b38c8008a9030ce34ca1f` — Add deterministic reinsert UI patch.
- `22400b7653e4ed9c26fb5da6f89eb8cdbe6a990f` — Add deterministic reinsert UI patch tests.
- `dfcfc4bc9d23a561a6bfffebb9b53c53cef58b44` — Update Scrub Key UI patch boundary tests for reinsert.
- `7725182c5d248bfb98f87a04e1c5da6453fdbfa7` — Record deterministic reinsert UI implementation status.
- `84f531293d26a800faa1e608041f089d6333901f` — Record deterministic reinsert UI implementation.

## Hugging Face sync status

Pending for WP8B commits.

## App verification status

Pending.

App verification is required because UI behavior changed.

The coordinator/user should verify that:

- `Originele waarden terugzetten` is visible after the Scrub Key area.
- User can paste scrubbed or AI-generated text.
- User can click `Zet originele waarden lokaal terug`.
- Mapped placeholders are restored locally.
- `Herstelde tekst` is shown.
- `Download herstelde tekst (.txt)` works.
- `Controleverslag terugzetten` is visible.
- Warning text about restored sensitive/confidential data is visible.
- Existing `Download Scrub Key (.json)` remains visible.
- Existing `Scrub Key laden` import/reload remains visible.
- Existing TXT, CSV, DOCX and PDF scrubbed downloads remain available.

## Boundary confirmation

Preserved boundaries:

- No direct edit to `presidio_streamlit.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No DOCX/PDF reinsert added.
- No TXT, CSV, DOCX or PDF scrubbed export behavior changed.
- No Scrub Key JSON export behavior intentionally changed.
- No Scrub Key import/reload behavior intentionally changed except storing the validated imported key in session state for reinsert use.
- No silent overwrite of existing review rows.
- No secrets, tokens or real personal data stored.

## Remaining risks

- UI patch area is still a sensitive sequential integration area.
- Hugging Face runtime still needs app verification after sync.
- Restored text may contain personal or confidential information and requires manual review before sharing.
- AI-output-specific behavior remains future work and should be separately reviewed.

## Next recommended step

Start WP8C — v13.3 Deterministic reinsert UI verification and closeout:

1. Verify GitHub Actions tests for WP8B.
2. Verify GitHub to Hugging Face sync.
3. Ask the coordinator/user to verify the app behavior.
4. Close WP8B only after tests, sync and app verification are green/confirmed.
