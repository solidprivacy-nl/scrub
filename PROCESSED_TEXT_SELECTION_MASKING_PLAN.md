# Processed-text selection masking — feasibility, UX and safety plan

Status: planning and discussion only  
Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN`  
Repository: `solidprivacy-nl/scrub`  
Date: 2026-08-03 23:42 Europe/Amsterdam

## 1. Executive conclusion

The requested interaction is technically feasible and strongly aligned with the document-centric review direction:

```text
Select an unmasked value in Verwerkte tekst
→ right-click
→ choose what kind of value it is
→ add it to the existing replacement table
→ rerender the processed text with a bound placeholder
```

The safest first implementation is **not** a new text editor and **not** a second replacement engine. It should be a new input route into the already verified manual-mask path:

```text
Interactive review component
→ bounded selection event
→ server-side validation
→ existing build_manual_mask_row(...)
→ existing document-scoped session state
→ existing replacement table
→ existing preview/export/Scrub Key/reinsert paths
```

Recommended first-version boundary:

```text
Mask all exact occurrences of the selected value.
Do not support “only this occurrence” yet.
```

That boundary is essential. The current product model stores replacement rules as exact string mappings and applies them globally. Supporting only one occurrence would require a new span-aware replacement model across preview, TXT, DOCX, PDF-to-TXT, Scrub Key, reinsert and audit. It is feasible later, but it is a separate architecture project and must not be smuggled into a context-menu feature.

The current `components.html(...)` side-by-side preview is display-only. It can detect a browser selection in JavaScript, but it cannot safely return a mutation request to Python. The recommended implementation therefore uses a small **bidirectional Streamlit custom component** on the current Streamlit v1 component API, while keeping a future migration path to the newer component API. A broad Streamlit upgrade and the context-menu feature should not be combined in one package.

## 2. Product problem

The current correction path works but interrupts the review task:

```text
Notice an unmasked value
→ remember or copy it
→ leave the text
→ open Gemiste waarde toevoegen
→ enter the value
→ choose a type
→ submit
→ return to the text
```

The desired path keeps the user in the document:

```text
Notice an unmasked value
→ select it
→ right-click
→ choose a type
→ continue reviewing nearby text
```

This is not merely cosmetic. The manual correction function mitigates the critical false-negative risk. Reducing the distance between noticing and correcting a missed value should lower omission risk, reduce copying errors and make long documents more reviewable.

## 3. Relationship to the current roadmap

The earlier side-by-side review specification explicitly excluded click-to-mark and a full document editor for that implementation phase. That exclusion protected the first side-by-side release from fragile mutation behavior. It should not be interpreted as a permanent product prohibition.

This proposal is a separately scoped next step because:

- the side-by-side surface is now live and verified;
- the manual missed-value path is live and verified;
- longer care examples make document-centric correction more relevant;
- the user has supplied direct usability evidence for the desired interaction;
- the proposal can preserve the existing table and export semantics.

This plan does not authorize implementation. It creates a bounded workpackage sequence for discussion and explicit approval.

## 4. Current architecture and consequences

### 4.1 Current processed-text pane

`side_by_side_review_panel_ui.py` currently:

- builds a processed preview from the current replacement rows;
- escapes source and processed text;
- renders both panes through `streamlit.components.v1.html`;
- synchronizes scrolling in browser-side JavaScript;
- marks existing replacements visually;
- explicitly declares itself visual-only and non-mutating.

`components.html` is suitable for display and local JavaScript behavior, but it does not return structured values to the Streamlit script. A context menu implemented only inside the current HTML iframe could look correct while having no supported route to add a row to Python state.

### 4.2 Current manual correction model

`manual_mask_entry.py` already provides the core safe path:

- strips only outer whitespace;
- validates that the value is non-empty;
- prevents an exact duplicate row;
- checks that the value occurs in the current source text;
- creates an included, non-remembered manual row;
- creates a document-bound placeholder when a binding ID is supplied;
- marks the row as manually added.

`presidio_streamlit.py` stores those rows under a document-specific session-state key and merges them into the existing replacement table before preview and export.

This is the correct mutation endpoint for a selection interaction. The browser component must never create placeholders, edit exports or write Scrub Key data itself.

### 4.3 Current replacement scope

The current preview and export logic use exact string replacement:

```text
for each selected find → replace_with mapping:
    replace every exact substring occurrence
```

Consequences:

- one row normally affects every exact occurrence in the supported text surface;
- the table does not currently retain source offsets for individual occurrences;
- the Scrub Key maps placeholders to original values, not document occurrence spans;
- DOCX replacement searches paragraph text/runs for string values;
- “only this occurrence” is not representable without changing core semantics.

The context menu must therefore say what will happen, for example:

```text
Masker alle 3 exacte voorkomens als Persoon
```

It must not imply that only the highlighted visual occurrence will change.

## 5. Feasibility assessment

### 5.1 Feasible in a bounded first version

The following is feasible with medium implementation complexity:

- text selection in the processed pane;
- right-click context menu for a valid non-empty selection;
- explicit type choice;
- exact occurrence count shown before commitment;
- server-side validation against the current document and processed preview;
- creation of one existing manual replacement row;
- automatic rerender with the new placeholder;
- retention of table, export, Scrub Key and reinsert semantics;
- scroll restoration after the Streamlit rerun;
- undo of the most recent selection action;
- keyboard-accessible fallback;
- fail-closed fallback to the current manual form.

### 5.2 Feasible later but not in the first version

The following requires a separate span-aware architecture line:

- mask only the selected occurrence;
- different replacements for identical text at different positions;
- selecting directly across multiple DOCX structural parts while preserving exact visual position;
- rich-text editing inside the preview;
- directly changing generated DOCX runs from browser offsets;
- drag-based redaction regions in PDF pages;
- automatic learning or recognizer retraining from a manual selection.

### 5.3 Not recommended

The following implementation approaches should be rejected:

- manipulating Streamlit parent DOM from the current iframe;
- passing selections through query parameters;
- storing document text or actions in browser local storage;
- clipboard polling;
- a third-party rich-text editor for this narrow function;
- a full Streamlit upgrade combined with the first context-menu implementation;
- direct frontend mutation of the replacement table or export state;
- optimistic replacement before server validation;
- arbitrary frontend-supplied entity types or replacement strings.

## 6. Recommended user experience

### 6.1 Primary flow

In `Verwerkte tekst`:

1. The user selects an unmasked value.
2. The user opens the context menu with the right mouse button.
3. Scrub shows a compact custom menu beside the selection.
4. The menu repeats the selected value in truncated form.
5. The menu shows the number of exact source occurrences.
6. The user chooses a masking type.
7. Python validates the action and adds one manual row.
8. The app reruns, restores approximately the same scroll position and flashes the newly masked value.
9. A compact success message provides `Ongedaan maken`.

Example:

```text
“Stichting Zorgpunt” geselecteerd
3 exacte voorkomens in dit document

Maskeren als:
- Persoon
- Organisatie
- Adres of locatie
- E-mailadres
- Telefoonnummer
- Datum of tijd
- Nummer of referentie
- Overige waarde
```

After choosing `Organisatie`:

```text
3 exacte voorkomens toegevoegd als Organisatie. [Ongedaan maken]
```

### 6.2 Native context-menu behavior

A custom browser context menu necessarily replaces the normal browser menu for that particular right-click. To limit disruption:

- intercept right-click only inside `Verwerkte tekst`;
- intercept only when a valid non-empty selection exists;
- keep the native context menu everywhere else;
- do not intercept right-click in the source pane;
- keep normal keyboard copy shortcuts working;
- close the custom menu with Escape, click outside or loss of focus.

### 6.3 Discoverability

Right-click alone is not sufficiently discoverable. Add one short caption below the processed pane:

```text
Tip: selecteer een gemiste waarde en klik met rechts om die toe te voegen.
```

A keyboard/visible fallback should also exist:

- Shift+F10 or the keyboard context-menu key opens the menu for the active selection;
- a small `Masker selectie` action becomes available when a valid selection exists.

The visible fallback is important for accessibility, touchpads and users who do not discover right-click.

### 6.4 Type choice

The first menu should use a stable, profile-independent set of broad types. It should not expose the full internal entity taxonomy.

Recommended quick types:

| User choice | Internal entity | Placeholder direction |
|---|---|---|
| Persoon | `PERSON` | `PERSOON` |
| Organisatie | `ORGANIZATION` | `ORGANISATIE` |
| Adres of locatie | `LOCATION` | `LOCATIE` |
| E-mailadres | `EMAIL_ADDRESS` | `EMAIL` |
| Telefoonnummer | `NL_PHONE_NUMBER` | `TELEFOON` |
| Datum of tijd | `DATE_TIME` | `DATUM` |
| Nummer of referentie | `NL_OTHER_REFERENCE` | `OVERIGE_REFERENTIE` |
| Overige waarde | `MANUAL` | `WAARDE` |

These choices describe the manual placeholder and audit label. They do not claim that the recognizer automatically classified the value, and they do not train or alter a recognition model.

Specialized legal or care subtypes can remain editable in the detailed table or be considered in a later menu extension. The first interaction should prioritize speed and predictable semantics.

### 6.5 Occurrence count and confirmation

The menu should display the server-derived impact before a high-impact action is committed.

Recommended behavior:

- one standalone occurrence: direct type choice is sufficient;
- two to five safe exact occurrences: show count in every action label;
- more than five occurrences: require a second explicit confirmation;
- embedded-substring collision: block the quick action and explain why;
- multiline or unusually long selection: route to the existing manual form/table.

The exact numeric thresholds should be frozen in contract tests before implementation and remain configurable in the pure action model rather than hard-coded in JavaScript.

## 7. Exact-selection safety

### 7.1 Selection validity

Reject a quick selection when it is:

- empty after outer whitespace trimming;
- whitespace or punctuation only;
- longer than the approved quick-selection maximum;
- spread across too many lines;
- partly or wholly inside an existing placeholder/highlight;
- a strict placeholder token;
- not present in the current server-side processed text at the reported offsets;
- not present in the current source text;
- already present as an exact replacement-table `find` value;
- associated with a stale document or stale processed-preview hash;
- accompanied by an unknown type or unsupported action scope.

### 7.2 Embedded-substring risk

The existing replacement engine uses string replacement. A selected short value can therefore occur inside a longer token:

```text
Selected: Jan
Source also contains: Jansen
```

A quick global action must not silently replace the `Jan` inside `Jansen`.

Before accepting the action, the server should calculate:

- total exact substring occurrences;
- standalone occurrences according to Unicode-aware word boundaries;
- embedded occurrences inside larger alphanumeric tokens;
- overlap with existing replacement terms.

Recommended first-version rule:

```text
If any occurrence is embedded in a longer alphanumeric token, block quick masking.
Ask the user to select more text or use the detailed manual/table path.
```

This is deliberately stricter than the current manual form because direct in-text action will be faster and more frequently used. It also identifies a safety hardening opportunity for the existing manual path, but that should be implemented through the shared action model rather than by changing export semantics invisibly.

### 7.3 Case and whitespace

The first version should preserve current semantics:

- case-sensitive;
- exact character sequence;
- trim only outer selection whitespace;
- do not normalize internal whitespace;
- do not fuzzy-match;
- do not infer singular/plural or spelling variants;
- do not silently add case-insensitive alternatives.

The menu copy must use `exacte voorkomens`, not `gelijke woorden`, because the replacement can contain spaces, punctuation or multiple words.

## 8. Recommended technical architecture

### 8.1 Component strategy

The repository currently pins Streamlit 1.39.0. The present `components.html` call is static. The safest implementation path is:

```text
Current Streamlit 1.39
+ Streamlit v1 bidirectional custom component
+ locally built and committed frontend assets
+ pure Python validation/action model
```

Do not combine this feature with a Streamlit major/minor upgrade. A later platform package may evaluate the newer component API independently.

### 8.2 Component responsibility

The browser component may:

- render escaped source and processed text;
- render existing highlights from server-supplied spans;
- synchronize scroll;
- calculate a selected range in processed-text coordinates;
- show the custom context menu;
- emit a bounded action request;
- restore supplied scroll ratios;
- focus the newly changed area after a successful rerun.

The component may not:

- create placeholders;
- decide whether the action is safe;
- derive or change the document binding ID;
- write session state directly;
- mutate the replacement table;
- build exports;
- build or write a Scrub Key;
- persist document text or selections in browser storage;
- call external services;
- load scripts, fonts or assets from a CDN.

### 8.3 Python responsibility

Python remains authoritative and must:

1. Rebuild the current processed preview from source and replacement rows.
2. Validate document scope and preview hash.
3. Validate selection offsets and selected text.
4. Recompute source occurrence impact.
5. Apply the type whitelist.
6. Check duplicates, collisions and replay IDs.
7. Build the row with the existing manual helper and current document binding ID.
8. Append the row to current document-scoped session state.
9. Record transient feedback/undo state.
10. Trigger an immediate rerun before export controls are rendered with stale state.

### 8.4 Proposed modules

```text
selection_mask_action.py
    Pure data model, validation, occurrence-impact analysis and action result.

processed_text_selection_component.py
    Python wrapper around the bidirectional Streamlit component.

frontend/processed_text_selection/
    Local source and built assets for two-pane rendering, selection and menu.

side_by_side_review_panel_ui.py
    Integration point; returns a selection action but does not mutate table state.

presidio_streamlit.py
    Authoritative action handling through existing manual row/session flow.
```

Keep `manual_mask_entry.py` as the row-construction source of truth. If type options are broadened, extend that mapping centrally rather than duplicating mappings in JavaScript.

### 8.5 Event contract

The component should emit one versioned, bounded object:

```json
{
  "schema_version": 1,
  "action": "add_manual_mask",
  "event_id": "browser-generated-unique-id",
  "document_scope_key": "server-supplied-scope-key",
  "processed_text_hash": "server-supplied-preview-hash",
  "selection": {
    "text": "Stichting Zorgpunt",
    "start": 418,
    "end": 438,
    "intersects_marked_content": false
  },
  "requested_type": "organization",
  "requested_scope": "all_exact",
  "ui_state": {
    "source_scroll_ratio": 0.41,
    "processed_scroll_ratio": 0.43
  }
}
```

Frontend values are untrusted input. The server must recompute and validate every field that affects behavior.

### 8.6 Selection offsets across highlights

The processed pane contains plain text nodes and marked placeholder nodes. The frontend should compute absolute processed-text offsets by walking text nodes rather than relying on raw HTML offsets.

Contract requirements:

- offsets count Unicode code units consistently with the JavaScript/Python contract;
- selection text equals the processed substring at `[start:end]` after the agreed conversion;
- any range intersecting a marked node is rejected;
- source text and placeholder markup are rendered with text nodes, not unescaped `innerHTML`;
- newline behavior is covered by tests.

A spike must prove this selection mapping before table integration is permitted.

## 9. Streamlit rerun and state handling

### 9.1 Replay prevention

Custom component values can survive a rerun. Without a replay guard, the same action could add the same row twice.

Required controls:

- every emitted action has an `event_id`;
- processed event IDs are stored per document session;
- duplicate event IDs are acknowledged but do not mutate state;
- exact duplicate `find` rows remain blocked by the existing/helper validation;
- event history is bounded so session state does not grow indefinitely.

### 9.2 Stale-view prevention

The event must be rejected when:

- the user switched document;
- replacement-table edits changed the processed preview;
- the selection offsets no longer match the processed text;
- the active document binding changed;
- the current work mode is no longer anonymization/review.

The rejection message should be simple:

```text
De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.
```

### 9.3 Scroll restoration

Adding a row causes a Streamlit rerun. To keep the interaction document-centric:

- capture both pane scroll ratios in the action;
- store them transiently server-side after validation;
- pass them back to the new component instance;
- restore after rendering;
- briefly flash the newly created placeholder;
- clear restoration state after acknowledgement.

Percentage restoration is acceptable and consistent with the existing synchronized-scroll limitation.

### 9.4 Undo

The success message should offer one-step undo.

A safe undo requires a stable action identifier attached to the new session row or retained in a separate transient action record. Undo must:

- remove only the row created by that selection event;
- remain scoped to the current document;
- never remove an automatic detection or an older manual row with the same display text;
- rerender preview/export through the normal path;
- expire when the document changes or the row is materially edited.

## 10. Privacy and security implications

### 10.1 Data exposure

The current side-by-side iframe already receives source and processed text for local display. A custom component does not need to expand the data category, but it adds an event channel back to Python.

Required privacy boundary:

```text
No selection or document content leaves the existing Streamlit session.
No analytics, telemetry, CDN, font, script, fetch, websocket or API call is added by the component.
```

The web prototype remains a development/demo environment. The future confidential trust environment remains local desktop/offline.

### 10.2 Cross-site scripting

Confidential document text is untrusted content. The frontend must:

- render text using `textContent` or explicitly created text nodes;
- construct highlights from trusted server span metadata;
- never interpolate document text into executable JavaScript;
- avoid `eval`, dynamic script creation and `dangerouslySetInnerHTML` for user text;
- validate style/class inputs against fixed constants;
- include adversarial synthetic XSS strings in tests.

### 10.3 Payload tampering

A malicious or malfunctioning browser can alter event data. Therefore:

- do not trust occurrence count from the browser;
- do not trust type-to-entity mapping from the browser;
- do not trust selection text without offset/hash validation;
- do not accept a frontend-generated placeholder;
- do not accept custom replacement strings through the quick menu;
- do not accept document binding IDs from the browser as authority;
- do not process unknown schema versions or actions;
- cap payload and selection size before further processing.

### 10.4 Browser persistence

Do not store document text, selected values or action history in:

- local storage;
- session storage;
- IndexedDB;
- cookies;
- URL/query parameters;
- clipboard without an explicit user copy action.

All durable mutation remains in existing Streamlit session state and export artifacts chosen by the user.

### 10.5 Failure behavior

The feature must fail closed:

- component load failure leaves the current manual form and table available;
- invalid event produces no row and no export change;
- stale event produces no row;
- JavaScript error must not block the rest of the app;
- no hidden retry may repeat a mutation;
- the current static/read-only renderer should remain available as a rollback path until live verification is green.

## 11. Review, audit and Scrub Key implications

### 11.1 Review table

The review table remains the source of truth and fallback.

A context-menu action should create a normal included row that is visible in the table with a source label such as:

```text
Handmatig uit tekst
```

The user can still:

- uncheck it;
- change the replacement;
- inspect the type;
- use expert review;
- exclude it before export.

### 11.2 Scrub Key

The frontend must not write Scrub Key data. By using `build_manual_mask_row` with the current server-side document binding ID, the resulting placeholder should follow the existing bound-placeholder path.

No Scrub Key schema, digest, binding or warning changes are required for the all-exact first version.

### 11.3 Export and reinsert

The first version deliberately reuses current exact-string export semantics. Consequently:

- TXT, DOCX and PDF-to-TXT paths continue to use current mapping behavior;
- the same selected value is replaced wherever the current engine would replace that exact string;
- reinsert continues through the normal bound Scrub Key mapping;
- no output filename, MIME type or supported-format change is needed.

### 11.4 Audit data

The row may record a non-sensitive action-origin marker such as `manual_selection`, but should not persist surrounding confidential context merely for convenience.

Recommended audit fields:

- action origin;
- selected type;
- exact occurrence count at acceptance;
- include state;
- manual action ID.

Do not add surrounding source sentences to downloadable audit output without a separate privacy review.

## 12. Accessibility and platform considerations

Required behaviors:

- `role="menu"` and `role="menuitem"` semantics;
- visible focus state;
- Arrow Up/Down navigation;
- Enter/Space activation;
- Escape close;
- Shift+F10/context-menu-key opening;
- selection status announced through an ARIA live region;
- no color-only confirmation;
- usable at browser zoom levels relevant to desktop users;
- predictable behavior with trackpads and high-DPI displays.

Initial browser verification should cover current desktop versions of:

- Microsoft Edge;
- Google Chrome;
- Firefox.

Safari and touch/mobile long-press behavior may be documented as best-effort for the web prototype. The product direction is desktop-first, but the visible non-right-click fallback should still work where text selection is available.

## 13. Testing strategy

### 13.1 Pure Python action-model tests

Create comprehensive tests before UI integration for:

- valid single occurrence;
- valid multiple safe occurrences;
- unknown type;
- unsupported scope;
- empty/whitespace/punctuation selection;
- oversized and multiline selection;
- selected placeholder;
- duplicate exact row;
- stale document scope;
- stale preview hash;
- mismatched offsets/text;
- embedded substring collision;
- overlap with existing find terms;
- Unicode names and accented text;
- hyphenated names/references;
- replayed event ID;
- high occurrence count confirmation requirement;
- bound placeholder construction through the existing helper;
- no automatic remember behavior;
- no export/Scrub Key/reinsert mutation in the action model.

### 13.2 Frontend/component tests

The component spike must test:

- selection offsets in plain text;
- selection offsets before, after and across `<mark>` nodes;
- rejection of a range intersecting a mark;
- right-click menu opens only for a valid selection;
- native menu remains elsewhere;
- menu closes on Escape/outside click;
- keyboard menu navigation;
- emitted schema and fixed type keys;
- source pane cannot emit mask actions;
- scroll ratio capture and restoration;
- user text rendered as text, not executable HTML;
- no external network calls or external asset URLs.

### 13.3 Streamlit integration tests

Test that:

- one accepted event adds exactly one manual row;
- a rerun does not replay the event;
- changing document scopes does not carry the row across documents;
- the row appears in the existing table;
- preview updates through the existing mapping;
- disabling the row restores visible text;
- undo removes only the action row;
- existing manual form remains operational;
- existing Basiscontrole/Expertcontrole behavior remains visibility-only;
- exports match the table state;
- bound Scrub Key export remains valid;
- reinsert restores the manually selected value;
- no output format or filename changes.

### 13.4 Cross-flow regression

Use synthetic TXT, DOCX and text-based PDF inputs to verify:

```text
Import
→ detect
→ review
→ select unmasked value
→ right-click type choice
→ replacement table
→ export
→ Scrub Key
→ reinsert
→ audit
```

DOCX tests should include body, table, header and footer examples where supported. PDF remains restored-TXT-only; no OCR or restored PDF is implied.

### 13.5 Live app verification

After Actions and Hugging Face synchronization are green, verify:

- no `Script execution error`;
- selection works in a long care document;
- context menu appears at the expected place;
- all quick types render correctly;
- occurrence count is understandable;
- collision warning prevents unsafe short-substring replacement;
- row appears in table;
- preview changes immediately after rerun;
- scroll position remains close to the prior location;
- undo works;
- current manual form remains available;
- export, Scrub Key and reinsert remain present and unchanged.

## 14. Recommended implementation sequence

Implementation should remain sequential because it touches the central review flow.

### WP 1 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`

Freeze:

- user flow and copy;
- quick type keys and mappings;
- `all_exact` scope only;
- selection limits;
- occurrence/collision rules;
- event schema;
- replay/stale-view behavior;
- accessibility and failure boundaries;
- explicit non-goals.

No UI or runtime change.

### WP 2 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`

Implement a pure Streamlit-free helper for:

- event parsing;
- text/hash/range validation;
- occurrence-impact analysis;
- type whitelist;
- collision classification;
- action result and feedback model;
- existing manual-row creation adapter.

No component or `presidio_streamlit.py` change.

### WP 3 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`

Build a synthetic, non-mutating bidirectional component proof:

- reproduce side-by-side rendering and synchronized scrolling;
- select text in processed pane;
- open menu;
- return a validated-shape event to a standalone demo/test wrapper;
- prove offset handling around highlights;
- no replacement-table integration.

Stop if the component cannot be made reliable and accessible without destabilizing the current app.

### WP 4 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`

After explicit approval and green spike:

- replace the static renderer through a rollback-safe integration;
- process accepted events in `presidio_streamlit.py`;
- add rows through the current manual helper/session path;
- add feedback, scroll restoration and undo;
- retain manual form and table fallback;
- preserve export, Scrub Key and reinsert semantics.

This is the first user-visible mutation package.

### WP 5 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`

Validate:

- profiles;
- synthetic legal and care documents;
- TXT/DOCX/PDF-to-TXT;
- preview/table/export/key/reinsert/audit;
- collision and stale-event safety;
- browser event replay.

### WP 6 — `SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY`

Verify synchronization and user-visible behavior in the deployed prototype. Keep the old static/manual route available until this package is green.

## 15. Rough implementation impact

Expected complexity: medium to medium-high.

The pure Python action model is straightforward. The highest-risk work is the browser component because it must combine:

- exact text selection offsets;
- existing highlights;
- synchronized scrolling;
- right-click and keyboard menus;
- bidirectional Streamlit reruns;
- safe rendering of untrusted document text;
- scroll/focus restoration.

A disciplined implementation should be expected to span several small workpackages rather than one broad UI commit. The component spike is the decisive technical gate.

No new cloud service or paid API is needed. A frontend build tool may be needed during development/CI, but the deployed app should use committed local static assets and should not require Node.js at runtime.

## 16. Explicit non-goals

This plan does not approve:

- implementation in this workpackage;
- occurrence-specific replacement;
- a rich-text or WYSIWYG editor;
- PDF visual redaction;
- OCR;
- direct DOCX editing in the browser;
- recognizer learning from user actions;
- automatic type inference;
- automatic `remember` behavior;
- hidden replacement-table mutation;
- removal of the manual form or table fallback;
- Streamlit upgrade;
- external frontend assets or telemetry;
- Scrub Key schema/binding change;
- reinsert or export semantic change;
- production-readiness claims.

## 17. Decisions proposed for discussion

Recommended decisions:

1. **Approve the product direction**: direct selection in `Verwerkte tekst` becomes the preferred manual-correction entry point.
2. **Keep the table authoritative**: the context menu creates a normal manual row; it does not replace the table.
3. **Use all exact occurrences in version one**: the menu states the server-derived count; occurrence-only is deferred.
4. **Use a compact profile-independent type menu**: broad readable types, no automatic inference.
5. **Use a bidirectional Streamlit v1 custom component**: no broad Streamlit upgrade in the same line.
6. **Keep the current manual form as fallback** until cross-flow and live app verification are green.
7. **Require collision guards and replay protection** before any UI mutation package.
8. **Require explicit coordinator approval** before starting the contract and implementation sequence.

## 18. Recommended final position

Proceed with the direction, but only through the proposed contract → action model → non-mutating component spike → integration sequence.

The product experience should feel like masking in the document itself, while the architecture continues to behave conservatively:

```text
The document is where the user notices and initiates the correction.
The server validates it.
The replacement table remains the authority.
The existing bound export and reinsert chain remains unchanged.
```
