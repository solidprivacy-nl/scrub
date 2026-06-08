# Handover — WP11 — v13.5 Two-mode reinsert UI planning

Repository: `solidprivacy-nl/scrub`  
Status: completed; planning/specification-only workpackage

## Summary

WP11 planned the future two-mode UI before changing Streamlit UI code.

The planning document recommends moving Scrub toward two clear modes:

```text
1. Anonimiseren
2. Originele waarden terugzetten
```

The recommended first implementation is a low-risk Streamlit tabs / mode-panel skeleton, not a full landing-page refactor yet.

The long-term product direction remains a landing choice with two large cards/buttons, but that should come after the current patch-based UI is simplified or replaced.

## Files added

- `TWO_MODE_UI_SPEC.md`
- `handover/workpackages/20260608_0000_v13_5_two_mode_ui_planning.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Tests: not applicable; planning/specification-only workpackage.
- No tests added or changed.
- No local test run required by scope.

## Validation status

- Documentation/spec validation: completed.
- GitHub Actions: not required for planning-only documentation change.
- Hugging Face sync: not required for planning-only documentation change.
- App verification: not applicable; no UI behavior changed.

## GitHub Actions status

Not required / not checked for this planning-only documentation workpackage.

## Hugging Face sync status

Not required / not checked for this planning-only documentation workpackage.

## App verification status

Not applicable; no UI behavior changed.

## Main recommendations

1. Move to a two-mode UI:

```text
Anonimiseren
Originele waarden terugzetten
```

2. Use Streamlit tabs or two clear mode panels first.
3. Treat landing cards as the later mature product direction.
4. Keep pasted-text reinsert available as the simplest fallback.
5. Add TXT upload/download reinsert UI after the mode skeleton is verified.
6. Add DOCX upload/download reinsert UI later using the WP10 helper.
7. Keep PDF reinsert excluded until a separate reliability review.
8. Keep AI/cloud behavior out unless explicitly approved.

## Options compared

- Option A — current single-scroll workflow:
  - lowest short-term cost;
  - not recommended as the next growth step because privacy states are not separated enough.
- Option B — Streamlit tabs:
  - recommended first implementation direction;
  - clear mode separation with lower patch-based implementation risk.
- Option C — landing choice with two large cards/buttons:
  - best long-term product UX;
  - not recommended as the immediate next step because it requires a larger refactor.

## Required journeys specified

`Anonimiseren` journey:

1. Upload/paste source text or document.
2. Review detected replacements.
3. Download currently supported scrubbed TXT/DOCX/PDF outputs.
4. Optionally download Scrub Key JSON.
5. Warn that the Scrub Key is reversible/pseudonymization.

`Originele waarden terugzetten` journey:

1. Load/paste Scrub Key.
2. Choose input type: paste text, upload TXT, upload DOCX.
3. Validate key locally.
4. Reinsert original values locally.
5. Show audit summary.
6. Warn restored output may contain sensitive/confidential data again.
7. Download restored TXT or DOCX where supported.

## Boundaries preserved

- No UI code changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No edit to `scrub_key_document_reinsert.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No TXT/DOCX reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior changed.
- No Scrub Key export/import behavior changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- The current app is still patch-based through `fix_streamlit_nested_expanders.py`; future UI implementation must be sequential.
- Tabs can still share session state if implemented carelessly, so WP12 must keep state explicit.
- Moving reinsert out of the export flow must not break existing scrubbed downloads.
- DOCX reinsert UI must later show WP10 limitations clearly.
- PDF reinsert remains high risk and must stay out of implementation until a separate reliability review.

## Next recommended step

Start:

```text
WP12 — v13.6 Two-mode UI skeleton and tab separation
```

Recommended WP12 scope:

- UI skeleton/navigation only;
- use two tabs or clear mode panels;
- keep current anonymization workflow working;
- keep pasted-text reinsert available;
- no TXT upload reinsert yet;
- no DOCX upload reinsert yet;
- no PDF reinsert;
- no AI/cloud behavior;
- no export/download semantics change;
- add patch-level UI tests;
- require app verification after sync.
