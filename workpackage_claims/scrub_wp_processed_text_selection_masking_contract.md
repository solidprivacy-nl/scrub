# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-masking-contract`  
Claimed: 2026-08-04 00:09 Europe/Amsterdam  
Status: in_progress

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

## Scope

- freeze the versioned component action envelope;
- freeze quick type keys and server-side mappings;
- freeze all-exact occurrence semantics;
- freeze selection length, multiline, punctuation and placeholder rules;
- freeze occurrence-count confirmation thresholds;
- freeze embedded-substring and overlap collision behavior;
- freeze replay, stale-view, document-scope and payload-size guards;
- freeze right-click, keyboard and visible-fallback behavior;
- freeze success, warning, failure and undo copy;
- freeze privacy, XSS, no-network and fail-closed boundaries;
- record implementation authorization in roadmap/governance files.

## Boundaries

- contract/specification and contract tests only;
- no runtime action helper yet;
- no browser component yet;
- no `presidio_streamlit.py`, review table, export or download flow change;
- no occurrence-specific replacement;
- no Streamlit upgrade;
- no Scrub Key, reinsert, recognizer, profile or cloud-processing change;
- review table and current manual form remain authoritative fallbacks.
