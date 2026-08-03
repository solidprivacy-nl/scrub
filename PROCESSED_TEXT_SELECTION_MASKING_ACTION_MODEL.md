# Processed-text selection masking action model

Status: implemented and test-gated  
Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`  
Repository: `solidprivacy-nl/scrub`  
Date: 2026-08-04 Europe/Amsterdam

## Purpose

This package implements the server-authoritative logic behind the approved selection-driven correction flow without introducing Streamlit, browser, component or UI behavior.

The model supports:

```text
inspect_selection
→ validate current document and processed text
→ decode UTF-16 browser offsets
→ validate selected text
→ calculate all exact source occurrences
→ block unsafe collisions
→ issue ready / confirmation_required / blocked inspection

commit_manual_mask
→ require a current single-use inspection
→ revalidate all server-owned state
→ require confirmation when needed
→ build one document-bound normal manual replacement row
→ return a stable action record for one-step undo
```

## Files

Runtime helper:

- `selection_mask_action.py`

Extended internal mapping adapter:

- `manual_mask_entry.py`

Tests:

- `tests/test_selection_mask_action.py`

No Streamlit, JavaScript, session-state, export, Scrub Key or reinsert integration is included.

## Core implementation

### Strict event parsing

The model validates:

- schema version;
- action name;
- event ID format;
- document-scope key;
- lowercase SHA-256 processed-text hash;
- selection object and booleans;
- UTF-16 offsets;
- optional scroll ratios;
- quick type and `all_exact` scope;
- confirmation-token size;
- total serialized payload size.

Unknown fields may be ignored for forward compatibility. Unknown actions, types, scopes and versions fail closed.

### UTF-16 conversion

Browser selection offsets are expressed as UTF-16 code units. Python indexes Unicode code points. The helper therefore explicitly converts offsets and rejects an offset which falls inside a supplementary character's surrogate pair.

Tests cover:

- ASCII and BMP text;
- accented Dutch characters;
- combining marks;
- emoji and other supplementary characters;
- negative, out-of-range and split-surrogate offsets.

### Selection validity

The quick path blocks:

- empty or whitespace-padded selections;
- selections longer than 160 code points;
- multiline, tabbed or control-character selections;
- punctuation-only selections;
- strict Scrub placeholders;
- processed-text/offset mismatches;
- frontend-declared or server-derived marked-range overlap;
- values absent from the current source text;
- exact duplicate replacement rows.

Matching remains case-sensitive and exact. No fuzzy or normalized variants are inferred.

### Exact occurrence impact

The model finds non-overlapping exact source occurrences and classifies:

```text
1–5   → ready
6–20  → confirmation_required
>20   → blocked
```

The count and occurrence ranges are stored in an opaque inspection record and recalculated at commit time.

### Collision protection

A selection is blocked when an occurrence is embedded in a longer token. Unicode letters, numbers, combining marks, underscore, hyphen/dash characters and apostrophes are treated as token continuations.

Examples blocked:

```text
Jan in Jansen
Jan in Jan-Willem
Neil in O'Neil
123 in AB123C
```

The model also blocks exact/nested conflicts with included replacement-table terms to avoid ordering-dependent partial replacement.

### Replay and stale-state protection

`SelectionActionState` provides caller-owned, document-scoped state:

- bounded replay history, default 128 event IDs;
- opaque inspection records;
- single-use inspection consumption;
- explicit invalidation.

Before commitment, the model revalidates:

- document scope;
- document binding;
- processed-text hash;
- source-text hash;
- replacement-table state hash;
- selection text and offsets;
- occurrence count and ranges;
- type and scope;
- confirmation token.

A failed validation creates no row. A repeated event creates no mutation.

### Manual row adapter

The approved quick types map server-side to internal manual labels, entity types and placeholder prefixes. `manual_mask_entry.py` now supports those internal labels while leaving the existing visible `MANUAL_MASK_TYPE_OPTIONS` unchanged.

A successful commit calls the existing `build_manual_mask_row(...)`, preserving document-bound placeholder construction, then records:

```text
source = manual_selection
source_label = Handmatig uit tekst
review_status = manual
include = true
remember = false
selection_scope = all_exact
selection_occurrence_count = server-derived count
manual_action_id = server-generated stable ID
```

The resulting row is suitable for the existing table and export paths but is not inserted into any Streamlit state by this package.

### One-step undo model

A successful commit returns a `ManualSelectionActionRecord` with a fingerprint of the exact created row.

Undo succeeds only when:

- the current document scope matches;
- exactly one row has the action ID;
- the row is unchanged since creation.

Undo fails closed when the row was edited, removed, duplicated or belongs to another document.

## Validation

Initial PR run #1957 exposed:

- one missing local assignment for the already validated inspect event ID;
- one test which incorrectly rejected the word `JavaScript` inside an explanatory docstring.

Neither issue required weakening the action contract. After correction:

- PR run #1961: **1106 tests passed in 10.66s**;
- clean standard PR run #1970: **1106 tests passed in 10.71s**.

## Boundaries preserved

This package does not:

- import Streamlit;
- implement or declare a browser component;
- mutate session state;
- modify `presidio_streamlit.py` or the side-by-side renderer;
- change visible manual form options;
- change review-table behavior;
- change export, Scrub Key or reinsert semantics;
- support only-one-occurrence masking;
- add external calls, assets, telemetry or persistence;
- upgrade Streamlit or dependencies.

## Next gate

The next permitted package is:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE
```

The spike must remain non-mutating. It must prove reliable rendering, selection-offset calculation, custom context-menu accessibility and bidirectional event transport before table integration is allowed.
