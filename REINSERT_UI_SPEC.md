# REINSERT_UI_SPEC — v13.3 Deterministic local reinsert UI

Status: planning/specification only.  
Workpackage: WP8 — v13.3 Deterministic reinsert UI planning.  
Repository: `solidprivacy-nl/scrub`.

This document specifies the future UI integration for deterministic local reinsert. It does **not** implement UI behavior.

---

## 1. Purpose

The deterministic reinsert UI should let a user locally restore original values into scrubbed text by using a previously validated Scrub Key.

Target workflow:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

For this specific UI step, the product should stay local and deterministic:

```text
Scrubbed or AI-generated text + validated Scrub Key → restored text + audit summary
```

The reinsert step must not call AI and must not send text or keys to a cloud service.

---

## 2. Existing helpers to use

The future UI implementation should use the verified helper:

```python
from scrub_key_reinsert import reinsert_from_scrub_key
```

Relevant helper API:

```python
reinsert_from_scrub_key(text, scrub_key) -> dict
```

The helper already returns:

- `text`;
- `replacement_count`;
- `item_count`;
- `active_item_count`;
- `excluded_item_count`;
- `placeholders_not_found`;
- `unknown_placeholders`;
- `duplicate_placeholders`;
- `validation_issues`;
- `reinserted`;
- `local_only`;
- `ai_processing`;
- `cloud_processing`.

The future UI should not duplicate the replacement logic. It should call the helper and render the result.

---

## 3. Placement in the current app flow

The reinsert UI should appear after the existing Scrub Key import/reload section, near the current download/export area.

Recommended placement order in the future UI:

```text
4. Download opgeschoonde bestanden
Eindcontrole vóór download
Extra exportcontrole
Scrub Key (JSON)
Scrub Key laden
Originele waarden terugzetten
Existing TXT/CSV/DOCX/PDF downloads
```

Rationale:

- The user first creates or loads a Scrub Key.
- The user then pastes scrubbed or AI-generated text.
- The user explicitly chooses to restore original values locally.
- Existing downloads remain available and unchanged.

The UI must not silently reinsert values when a key is loaded. Reinsertion must require a separate visible user action.

---

## 4. Suggested UI labels

Section label:

```text
Originele waarden terugzetten
```

Input label:

```text
Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten
```

Action button:

```text
Zet originele waarden lokaal terug
```

Output label:

```text
Herstelde tekst
```

Download label:

```text
Download herstelde tekst (.txt)
```

Optional audit label:

```text
Controleverslag terugzetten
```

---

## 5. User interaction flow

The future UI should follow this sequence:

1. User scrubs a document and reviews replacements.
2. User exports or loads a valid Scrub Key.
3. User opens the section `Originele waarden terugzetten`.
4. User pastes scrubbed or AI-generated text into the text area.
5. User clicks `Zet originele waarden lokaal terug`.
6. UI calls `reinsert_from_scrub_key(pasted_text, scrub_key)`.
7. UI displays warnings, restored text and audit summary.
8. User may download restored text as `.txt`.

The UI should only use a Scrub Key that is already validated by the current Scrub Key export/import flow or by the helper validation in `reinsert_from_scrub_key(...)`.

---

## 6. Required state handling

Future UI implementation should define one clear source for the active Scrub Key.

Preferred order:

1. Use a successfully imported Scrub Key from the existing import/reload flow.
2. If no imported key exists, use the Scrub Key built from the current reviewed replacement table.
3. If neither exists or validation fails, show a validation warning and do not reinsert.

Possible Streamlit state keys for future implementation:

```text
st.session_state["active_scrub_key"]
st.session_state["scrub_key_import_rows"]
st.session_state["reinsert_input_text"]
st.session_state["reinsert_result"]
```

The exact state key names may differ, but the future implementation must keep the state explicit and auditable.

The UI must not overwrite the replacement table, Scrub Key export, or imported mapping rows while reinserting text.

---

## 7. Helper call contract

Future UI implementation should call:

```python
result = reinsert_from_scrub_key(reinsert_input_text, active_scrub_key)
```

The UI should then read:

```python
result["text"]
result["replacement_count"]
result["item_count"]
result["active_item_count"]
result["excluded_item_count"]
result["placeholders_not_found"]
result["unknown_placeholders"]
result["duplicate_placeholders"]
result["validation_issues"]
result["reinserted"]
result["local_only"]
result["ai_processing"]
result["cloud_processing"]
```

If `validation_issues` is not empty, the UI must show those issues and must not present the result as successfully restored.

If `replacement_count` is `0`, the UI should explain that no placeholders were replaced.

---

## 8. Output behavior

The future UI should display:

- restored text in a read-only or editable text area labelled `Herstelde tekst`;
- a `.txt` download button labelled `Download herstelde tekst (.txt)`;
- audit summary in a compact visible block;
- warnings for unknown, duplicate or missing placeholders where applicable.

The future UI should not automatically create DOCX or PDF restored files in the first implementation. Start with text output only.

---

## 9. Required audit summary fields

The future UI should show at least:

- mapping item count;
- active item count;
- excluded item count;
- replacement count;
- placeholders not found;
- unknown placeholders;
- duplicate placeholders;
- validation issues;
- local-only status;
- no-AI status;
- no-cloud status.

Suggested Dutch rendering:

```text
Mappingregels totaal: <item_count>
Actieve mappingregels: <active_item_count>
Uitgesloten mappingregels: <excluded_item_count>
Aantal teruggezette waarden: <replacement_count>
Niet gevonden placeholders: <placeholders_not_found>
Onbekende placeholders in tekst: <unknown_placeholders>
Dubbele placeholders in sleutel: <duplicate_placeholders>
Validatieproblemen: <validation_issues>
Lokaal uitgevoerd: ja
AI-verwerking: nee
Cloudverwerking: nee
```

---

## 10. Required warnings

The future UI must display this warning near the action button and/or output:

```text
Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat zorgvuldig voordat u het deelt.
```

The future UI must also clearly communicate:

- reinsertion restores original sensitive values;
- restored text may again contain personal or confidential information;
- restored output must be manually reviewed before sharing;
- a Scrub Key is reversible/pseudonymization, not full anonymization;
- the key must remain local and protected;
- no AI/cloud processing is involved in this reinsert step.

Suggested additional caption:

```text
Deze stap wordt lokaal uitgevoerd met uw Scrub Key. Er wordt geen AI- of cloudverwerking gebruikt voor het terugzetten.
```

---

## 11. What must not happen automatically

The future UI must not:

- reinsert values automatically when a Scrub Key is loaded;
- silently replace the current reviewed replacement table;
- silently overwrite scrubbed output;
- automatically rehydrate DOCX, PDF or original documents;
- call AI services;
- send Scrub Key contents to any external service;
- change existing TXT/CSV/DOCX/PDF export behavior;
- change existing Scrub Key JSON export behavior;
- change existing Scrub Key import/reload behavior;
- store Scrub Keys server-side;
- store secrets, tokens or real personal data.

---

## 12. Required tests for future UI implementation

The future UI implementation workpackage should add tests, likely in a new file such as:

```text
tests/test_scrub_key_reinsert_ui_patch.py
```

Required test coverage:

1. The Streamlit patch imports `reinsert_from_scrub_key`.
2. The UI contains `Originele waarden terugzetten`.
3. The UI contains the paste input label.
4. The UI contains the button `Zet originele waarden lokaal terug`.
5. The UI contains `Herstelde tekst`.
6. The UI contains `Download herstelde tekst (.txt)`.
7. The required warning about restoring sensitive values is present.
8. The pseudonymization/reversibility warning remains present.
9. The audit summary fields are represented in the UI patch.
10. The helper is called only after a visible button action.
11. The UI does not add AI calls or cloud processing.
12. The UI does not call `st.stop()` or block existing downloads.
13. Existing `Download Scrub Key (.json)` remains present.
14. Existing TXT/CSV/DOCX/PDF download markers are not removed.
15. The import/reload UI remains present.
16. No automatic document rehydration wording or behavior is introduced.

Suggested targeted validation after future implementation:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py
```

If feasible:

```bash
PYTHONPATH=. pytest -q
```

---

## 13. Non-goals for the next UI implementation

The next implementation should not include:

- AI-output-specific parsing beyond accepting pasted text;
- calls to AI providers;
- cloud processing;
- DOCX/PDF rehydration;
- replacing uploaded source documents;
- metadata cleaning;
- batch processing;
- server-side key storage;
- durable project vault storage;
- automatic sharing/export of restored text.

Those should remain separate future workpackages.

---

## 14. Suggested future workpackage sequence

Recommended next workpackage:

```text
WP8B — v13.3 Deterministic reinsert UI implementation
```

Scope for WP8B:

- update `fix_streamlit_nested_expanders.py` only;
- add `tests/test_scrub_key_reinsert_ui_patch.py`;
- keep UI integration sequential;
- do not add AI/cloud behavior;
- do not change existing export/download semantics;
- ask for app verification after sync because UI behavior changes.

Later workpackage, only after WP8B is verified:

```text
WP9 — AI-output reinsert workflow review
```

That later workpackage should explicitly review whether AI-output-specific behavior is needed and how to keep it safe.
