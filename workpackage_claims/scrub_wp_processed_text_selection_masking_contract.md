# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-masking-contract`  
Claimed: 2026-08-04 00:09 Europe/Amsterdam  
Status: completed; GitHub Actions green

## Approval evidence

Coordinator/user approval at 2026-08-04 00:09 Europe/Amsterdam:

```text
Akkoord. Ga aan de slag, werk autonoom, wees creatief met het oplossen van problemen, hou me op de hoogte, stop alleen als je tegen een muur aanloopt of als je klaar bent en iets hebt om te presenteren.
```

The approval includes the recommended version-one boundary:

```text
all exact occurrences of the selected value
```

## Goal

Freeze the user-visible, technical and safety contract for direct manual masking from a selection in `Verwerkte tekst` before implementing the action model or browser component.

## Scope completed

- froze the versioned two-stage component action envelope;
- froze quick type keys and server-side mappings;
- froze all-exact occurrence semantics;
- froze selection length, multiline, punctuation and placeholder rules;
- froze occurrence-count confirmation thresholds;
- froze embedded-substring and overlap collision behavior;
- froze replay, stale-view, document-scope and payload-size guards;
- froze right-click, keyboard and visible-fallback behavior;
- froze success, warning, failure and undo copy;
- froze privacy, XSS, no-network and fail-closed boundaries;
- recorded implementation authorization in roadmap/governance files.

## Validation

- Clean PR run #1954: **1027 tests passed in 11.48s**.
- The preceding clean run #1953 exposed one stale planning-status assertion while 1026 tests passed; the assertion was aligned to the approved contract state.
- Hugging Face sync is not functionally relevant because this package changes no runtime/UI behavior.
- App verification is not applicable.

## Boundaries preserved

- no runtime action helper yet;
- no browser component yet;
- no `presidio_streamlit.py`, review table, export or download flow change;
- no occurrence-specific replacement;
- no Streamlit upgrade;
- no Scrub Key, reinsert, recognizer, profile or cloud-processing change;
- review table and current manual form remain authoritative fallbacks.

## Next authorized package

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL
```
