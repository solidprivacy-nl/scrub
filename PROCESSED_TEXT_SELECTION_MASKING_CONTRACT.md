# Processed-text selection masking contract

Status: approved contract; pure action model implemented and test-gated
Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`  
Repository: `solidprivacy-nl/scrub`  
Approved: 2026-08-04 00:09 Europe/Amsterdam

## 1. Accepted product decision

The preferred manual-correction interaction is:

```text
select an unmasked value in Verwerkte tekst
→ right-click or invoke Masker selectie
→ inspect the server-validated impact
→ choose a broad masking type
→ add one normal manual replacement row
→ rerender and continue reviewing
```

Version one applies the selected value to **all safe exact occurrences** in the current document. It does not support occurrence-specific masking.

The interaction is an additional input route into the existing manual replacement path. It is not a second replacement engine, a rich-text editor, recognizer training or direct frontend mutation.

## 2. Non-negotiable authority boundaries

The server remains authoritative for:

- the current source document;
- the current processed preview;
- document scope and binding;
- selection validity and offsets;
- exact occurrence count;
- embedded-substring and replacement overlap detection;
- quick-type mapping;
- placeholder construction;
- replacement-table mutation;
- Scrub Key, export, reinsert and audit behavior.

The browser component may render, select, navigate and emit bounded events. It may never create a placeholder, alter session state, mutate the replacement table, write a Scrub Key or build an export.

The review table remains the source of truth and fallback. The existing `Gemiste waarde toevoegen` flow remains available until cross-flow and app verification are green.

## 3. Two-stage interaction protocol

A server-derived occurrence count must be visible before commitment. The component therefore uses two separate event stages.

### Stage A — inspect selection

The component emits `inspect_selection` when a user opens the custom context menu or invokes the visible/keyboard fallback for a valid selection.

Python validates the selection, recomputes its impact and returns one inspection result:

- `ready` — one to five safe exact occurrences;
- `confirmation_required` — six to twenty safe exact occurrences;
- `blocked` — invalid, stale, conflicting or more than twenty occurrences.

Only a `ready` or `confirmation_required` inspection result may expose type actions.

### Stage B — commit manual mask

The component emits `commit_manual_mask` only with a server-issued, current inspection ID. Python revalidates the document, preview, selection, occurrence impact and requested type before adding one row.

An inspection is single-use after a successful commit. A changed document, changed processed preview, changed replacement table or changed selection invalidates it.

## 4. Versioned event envelopes

### 4.1 Inspect event

```json
{
  "schema_version": 1,
  "action": "inspect_selection",
  "event_id": "sel_01J8Y7ZQMRM1VY2R5JQ6E3F2A9",
  "document_scope_key": "0123456789abcdef",
  "processed_text_hash": "64-lowercase-hex-sha256",
  "selection": {
    "text": "Stichting Zorgpunt",
    "start_utf16": 418,
    "end_utf16": 438,
    "intersects_marked_content": false
  },
  "ui_state": {
    "source_scroll_ratio": 0.41,
    "processed_scroll_ratio": 0.43
  }
}
```

### 4.2 Commit event

```json
{
  "schema_version": 1,
  "action": "commit_manual_mask",
  "event_id": "commit_01J8Y80C1W3Q8V4K7M6F2P9R5T",
  "inspection_id": "server-issued-opaque-id",
  "requested_type": "organization",
  "requested_scope": "all_exact",
  "confirmation_token": "server-issued-token-or-empty"
}
```

### 4.3 Envelope limits

- Serialized event payload: maximum 8192 UTF-8 bytes.
- `schema_version`: exactly integer `1`; booleans are not accepted as integers.
- `event_id`: 16–80 characters matching `^[A-Za-z0-9_-]+$`.
- `document_scope_key`: exactly sixteen lowercase hexadecimal characters.
- `processed_text_hash`: exactly sixty-four lowercase hexadecimal characters.
- Unknown fields may be ignored for forward-compatible parsing, but unknown actions, schema versions, requested types and scopes fail closed.
- Every accepted event ID is recorded in a bounded per-document replay set; a replay produces no mutation.

## 5. Offset and text contract

Browser DOM selections use UTF-16 code-unit offsets. Therefore:

- `start_utf16` and `end_utf16` are non-negative integer UTF-16 code-unit offsets into the exact current processed text;
- `end_utf16` must be greater than `start_utf16`;
- Python converts UTF-16 offsets explicitly before substring comparison;
- offsets splitting a surrogate pair are invalid;
- the decoded processed substring must exactly equal `selection.text`;
- the event text has no leading or trailing whitespace;
- the component adjusts offsets when trimming outer whitespace;
- Python repeats all trimming and equality checks;
- the selected value must also occur in the current source text.

This contract is covered with BMP text, accented Dutch text, combining marks and supplementary Unicode characters.

## 6. Quick-selection validity

A quick selection is rejected when any of the following is true:

- empty after outer whitespace trimming;
- longer than 160 Unicode code points;
- contains a carriage return, line feed, tab or another Unicode control character;
- contains no Unicode letter or number;
- contains or equals a strict Scrub placeholder token;
- intersects an existing marked/replaced range;
- does not match the current processed text at the supplied UTF-16 offsets;
- does not occur in the current source text;
- is already an exact `find` value in the replacement table;
- belongs to a stale document scope or processed-text hash;
- is accompanied by an unsupported action, type or scope.

The first version is single-line only. Multiline selections use the existing manual/table path.

Matching remains:

- case-sensitive;
- exact character sequence;
- outer-whitespace trim only;
- no internal whitespace normalization;
- no fuzzy matching;
- no automatic casing, spelling, singular/plural or variant expansion.

## 7. Exact-occurrence impact contract

The server counts non-overlapping exact occurrences in the current source text. This mirrors the current exact string replacement behavior.

Impact levels:

| Exact occurrences | Result | User action |
|---:|---|---|
| 1 | `ready` | choose type and commit |
| 2–5 | `ready` | count shown in every type action; choose and commit |
| 6–20 | `confirmation_required` | choose type, then explicitly confirm all occurrences |
| >20 | `blocked` | use the existing detailed manual/table path |

The count is recomputed at commit time. A changed count invalidates the inspection.

The UI says `exacte voorkomens`; it does not say `gelijke woorden` or imply occurrence-specific behavior.

## 8. Embedded-substring collision contract

A quick global action is blocked if any exact occurrence is embedded in a longer token.

For boundary classification, token-continuation characters include:

- every Unicode letter, number or combining mark;
- underscore;
- hyphen-minus and Unicode hyphen/dash characters;
- straight or curly apostrophes.

Examples blocked by the quick path:

```text
Jan inside Jansen
Jan inside Jan-Willem
Neil inside O'Neil
123 inside AB123C
```

The server inspects the character immediately before and after every exact occurrence when the selected value begins or ends with a token-continuation character.

Blocked copy:

```text
Deze selectie komt ook voor als onderdeel van een langere waarde. Selecteer meer tekst of gebruik ‘Gemiste waarde toevoegen’.
```

## 9. Existing-replacement overlap contract

The quick path blocks an action when the selected value conflicts with an included replacement rule:

- exact duplicate `find` value;
- selected value is a strict substring of an included `find` value;
- included `find` value is a strict substring of the selected value;
- any selected processed range overlaps a server-derived replacement/highlight span.

This conservative rule avoids ordering-dependent or partially nested replacements. The detailed review table remains available for deliberate resolution.

Excluded rows do not create a quick-path overlap block, but an exact duplicate row remains blocked regardless of include state so the user resolves the existing row rather than creating a second authority.

## 10. Quick type contract

The component emits only stable machine keys. Python owns all labels, entity mappings and placeholder prefixes.

| Machine key | User label | Manual helper label | Entity type | Placeholder prefix |
|---|---|---|---|---|
| `person` | Persoon | Persoon | `PERSON` | `PERSOON` |
| `organization` | Organisatie | Organisatie | `ORGANIZATION` | `ORGANISATIE` |
| `location` | Adres of locatie | Adres of locatie | `LOCATION` | `LOCATIE` |
| `email` | E-mailadres | E-mailadres | `EMAIL_ADDRESS` | `EMAIL` |
| `phone` | Telefoonnummer | Telefoonnummer | `NL_PHONE_NUMBER` | `TELEFOON` |
| `date_time` | Datum of tijd | Datum of tijd | `DATE_TIME` | `DATUM` |
| `reference` | Nummer of referentie | Nummer of referentie | `NL_OTHER_REFERENCE` | `OVERIGE_REFERENTIE` |
| `other` | Overige waarde | Overige waarde | `MANUAL` | `WAARDE` |

The quick type records a user decision. It does not claim automatic recognition and does not train a model.

A context-menu-created row uses:

```text
source = manual_selection
source_label = Handmatig uit tekst
review_status = manual
remember = false
include = true
```

The existing bound manual-placeholder path remains mandatory when a document binding ID is available.

## 11. Inspection result contract

A successful inspection result contains server-owned data only:

```json
{
  "schema_version": 1,
  "inspection_id": "opaque-server-id",
  "status": "ready",
  "selection_text": "Stichting Zorgpunt",
  "occurrence_count": 3,
  "requested_scope": "all_exact",
  "allowed_types": [
    "person",
    "organization",
    "location",
    "email",
    "phone",
    "date_time",
    "reference",
    "other"
  ],
  "confirmation_token": "",
  "message": "3 exacte voorkomens in dit document"
}
```

For six to twenty occurrences, `status` is `confirmation_required` and a server-issued confirmation token is present. For blocked selections, no inspection ID, confirmation token or type actions are returned.

Inspection state is scoped to the current Streamlit session and document. It is not written to browser storage, URLs, exports, audit downloads or Scrub Keys.

## 12. UI interaction contract

### 12.1 Context menu

The custom menu intercepts right-click only when:

- the pointer is inside `Verwerkte tekst`;
- a valid non-empty selection exists;
- the selection does not visibly intersect a marked replacement.

The native browser menu remains available:

- in the source pane;
- outside the review component;
- in the processed pane when no valid selection exists.

Escape, outside click, blur or document change closes the custom menu.

### 12.2 Discoverability and accessibility

The processed pane shows:

```text
Tip: selecteer een gemiste waarde en klik met rechts om die toe te voegen.
```

When a valid selection exists, a visible `Masker selectie` fallback is available.

Required keyboard behavior:

- Shift+F10 or the context-menu key opens inspection for the active selection;
- Arrow Up/Down navigates menu items;
- Home/End moves to first/last item;
- Enter or Space activates;
- Escape closes and returns focus;
- focus remains visible;
- status changes are announced through an ARIA live region;
- no state is conveyed only by color.

The menu uses `role="menu"`; actions use `role="menuitem"`.

## 13. Frozen user-facing copy

Inspection:

```text
“{selection}” geselecteerd
{count} exact voorkomen in dit document
{count} exacte voorkomens in dit document
```

Type action:

```text
Masker als {type}
Masker alle {count} exacte voorkomens als {type}
```

High-impact confirmation:

```text
Deze waarde komt {count} keer voor. Alle exacte voorkomens worden gemaskeerd.
Bevestig alle {count} voorkomens
```

Success:

```text
1 exact voorkomen gemaskeerd als {type}.
{count} exacte voorkomens gemaskeerd als {type}.
```

Undo action:

```text
Ongedaan maken
```

Stale view:

```text
De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.
```

Duplicate:

```text
Deze waarde staat al in de vervangtabel.
```

Too many occurrences:

```text
Deze selectie komt {count} keer voor. Voeg de waarde via ‘Gemiste waarde toevoegen’ toe om de impact uitgebreider te controleren.
```

Generic fail-closed message:

```text
Deze selectie kon niet veilig worden toegevoegd. Controleer de selectie of gebruik ‘Gemiste waarde toevoegen’.
```

## 14. Replay, stale-state and inspection lifecycle

- Every event ID is processed at most once.
- Replay history is document-scoped and bounded to the most recent 128 event IDs.
- Inspection IDs are opaque, server-generated and bound to document scope, processed hash, exact selection, offsets, occurrence count and impact classification.
- A successful commit consumes its inspection ID.
- Failed validation does not mutate rows and may invalidate the inspection.
- A changed source, processed preview, replacement-table mapping or document binding invalidates the inspection.
- A duplicate Streamlit rerun with the same component value produces no duplicate row.
- No automatic retry may repeat a mutation.

## 15. Undo contract

Version one provides one-step undo for the most recent successful selection action in the current document.

Undo:

- removes only the row created by the recorded selection action ID;
- does not remove automatic detections or older manual rows;
- is unavailable after the row is materially edited, excluded/reincluded through a conflicting state, or the document changes;
- rerenders through the normal replacement path;
- does not alter Scrub Key or export semantics outside the resulting table state.

The action model must provide a stable manual action ID separate from the browser event ID.

## 16. Privacy and security contract

The component and integration add no:

- analytics or document telemetry;
- external API calls;
- CDN scripts, styles, fonts or images;
- browser local storage, session storage or IndexedDB persistence;
- document or selection data in cookies, URLs or query parameters;
- clipboard writes without an explicit user copy action;
- cloud document processing.

Untrusted document text is rendered through text nodes or equivalent escaped rendering. It is never interpolated into executable script and never passed to `eval` or dynamic script creation.

Frontend values are untrusted input. Python recalculates every behavior-affecting value.

## 17. Fail-closed and rollback contract

- Invalid inspection: no row and no output change.
- Invalid commit: no row and no output change.
- Component exception: current manual form and review table remain usable.
- JavaScript failure: no hidden mutation or retry.
- Stale selection: user reselects the value.
- The current static renderer remains a rollback option until component, integration, cross-flow and live app verification are green.
- No export, Scrub Key or reinsert control may render against an accepted but not yet incorporated selection event.

## 18. Explicit non-goals

This contract does not authorize:

- only-this-occurrence masking;
- position-aware Scrub Key mappings;
- a rich-text/WYSIWYG editor;
- PDF visual redaction or OCR;
- direct browser editing of DOCX structures;
- recognizer learning or automatic type inference;
- automatic `remember` behavior;
- removal of the manual form or review table;
- a Streamlit upgrade;
- external frontend assets or telemetry;
- export filename, MIME type or format changes;
- Scrub Key schema, binding or lifecycle changes;
- reinsert semantic changes;
- production-readiness claims.

## 19. Sequential implementation gate

This contract authorizes only the next package:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL
```

The action model is implemented in `selection_mask_action.py` and passed the full adversarial regression. The next permitted package is the non-mutating component spike; table or Streamlit integration remains prohibited until that proof is green.
