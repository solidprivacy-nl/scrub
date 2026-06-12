# Scrub Key Warning Implementation Plan — WP28B

Status: completed UI/security implementation-planning-only  
Repository: `solidprivacy-nl/scrub`

This plan translates the WP27 warning UX plan and WP28 expiry/delete policy into exact implementation locations, acknowledgement states and copy inventory for a future Streamlit UI implementation package.

This document does **not** implement UI, change Streamlit patch files, change helper logic, change Scrub Key schema, change import/export behavior, change reinsert behavior, add encryption, add deletion automation, add expiry blocking, add dependencies, add secrets, add real data or add cloud processing.

---

## 1. Scope

WP28B is a planning package only.

The future MVP warning implementation should make Scrub Key risk visible at the points where the user creates, downloads, imports, uses or downloads output from a Scrub Key.

The plan covers:

- exact current UI flow locations;
- warning placement;
- acknowledgement placement;
- Dutch copy inventory;
- guidance-only versus acknowledgement versus later blocking candidates;
- Streamlit implementation risks;
- test expectations for the later implementation package.

The implementation must preserve the current product boundary:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The Scrub Key remains sensitive re-identification data. Scrub Key-based output remains pseudonymized, not fully anonymized, while the key exists.

---

## 2. Current UI implementation surface

The current Streamlit app is patched through:

```text
fix_streamlit_nested_expanders.py
```

The base app remains:

```text
presidio_streamlit.py
```

Current Scrub Key and reinsert UI is injected mainly through these patch blocks in `fix_streamlit_nested_expanders.py`:

| Current block | Current purpose | Future warning relevance |
| --- | --- | --- |
| `review_summary_block` | Final review/export section and Scrub Key JSON download. | Scrub Key creation, export/download, storage, loss-of-key and AI/e-mail warning. |
| `scrub_key_import_ui_block` | Scrub Key upload/paste, validation and loading. | Import/reload acknowledgement, malformed key warning, wrong-document warning. |
| `reinsert_ui_block` | Pasted-text reinsert with active Scrub Key. | Reinsert acknowledgement, local-only warning, restored-output warning, audit warnings. |
| `txt_reinsert_ui_block` | TXT upload and restored TXT download. | File reinsert acknowledgement and restored TXT download warning. |
| `docx_reinsert_ui_block` | DOCX upload and restored DOCX download. | File reinsert acknowledgement, restored DOCX warning and DOCX limitation warning. |
| Future PDF-to-TXT reinsert block, if present | PDF text extraction to restored TXT output. | Same as TXT/file reinsert plus PDF-scope limitation. |
| `two_mode_selection_block` | Mode selector for `Anonimiseren` and `Originele waarden terugzetten`. | Entry warning for reinsert mode and local-only/no-AI/no-cloud reminder. |

Future implementation should edit the patch layer first unless the project later decides to refactor away from startup patching. Direct edits to `presidio_streamlit.py` should be avoided unless that becomes an explicit refactor workpackage.

---

## 3. MVP warning principles

MVP warnings should be clear and repeated at the relevant moment, but they must not silently change current behavior.

MVP must not add:

- encryption claims;
- automatic deletion;
- expiry blocking;
- hidden recovery;
- app-managed vault claims;
- Scrub Key schema migration;
- import/export behavior changes;
- reinsert behavior changes;
- cloud processing;
- real-data examples.

MVP may add:

- warning text;
- captions/help text;
- checkboxes/acknowledgements;
- disabled buttons until acknowledgement is checked;
- audit-visible warning messages that do not store original values.

Button gating by acknowledgement is acceptable only when it prevents accidental high-risk clicks while preserving the same underlying export/reinsert action once acknowledged. It must not change exported content, Scrub Key JSON semantics or reinsert output.

---

## 4. Exact warning placement plan

### 4.1 Scrub Key creation

Current location:

```text
fix_streamlit_nested_expanders.py → review_summary_block
```

Place warning directly before the Scrub Key is built and the download area is shown.

Current nearby UI:

```text
st.markdown("**Scrub Key (JSON)**")
st.warning("Let op: een Scrub Key maakt ...")
scrub_key = build_scrub_key(scrub_key_rows)
```

MVP warning:

```text
Let op: u maakt nu een Scrub Key. Deze sleutel koppelt placeholders aan originele vertrouwelijke waarden. Zolang deze sleutel bestaat, is de opgeschoonde tekst pseudoniem en niet volledig anoniem.
```

Acknowledgement:

- Creation preview: guidance-only.
- Download/export: required before the download button is active.

Implementation note:

- Do not show original values in warning copy.
- Do not add entity-specific details that expose sensitive values.

---

### 4.2 Scrub Key download/export

Current location:

```text
fix_streamlit_nested_expanders.py → review_summary_block → st.download_button("Download Scrub Key (.json)")
```

Place critical warning and acknowledgement immediately before the Scrub Key download button.

MVP warning before download:

```text
Belangrijk: deze Scrub Key kan originele vertrouwelijke waarden herstellen. Download de sleutel alleen als u deze lokaal, apart en beveiligd kunt bewaren. Deel of upload de sleutel niet naar externe AI, e-mail of derden, tenzij dit bewust bedoeld en toegestaan is.
```

Required acknowledgement checkbox:

```text
Ik begrijp dat deze Scrub Key herleidbaar is en dat ik deze niet samen met opgeschoonde uitvoer mag delen zonder geldige reden en toestemming.
```

Post-download guidance near the button:

```text
Bewaar de Scrub Key niet onnodig in Downloads. Verplaats de sleutel naar een beveiligde lokale map of verwijder deze zodra hij niet meer nodig is.
```

Implementation note:

- The download button may be disabled until the acknowledgement is checked.
- The JSON content, filename and MIME type must remain unchanged unless a separate approved package changes export semantics.
- Do not silently include the Scrub Key in any other export bundle.

---

### 4.3 Local storage and Downloads guidance

Current location:

```text
fix_streamlit_nested_expanders.py → review_summary_block
```

Also applicable to future help text in `presidio_streamlit.py` after refactor.

Place near the Scrub Key download area and optionally inside an expander such as:

```text
Waar moet ik de Scrub Key bewaren?
```

MVP guidance text:

```text
Bewaar de Scrub Key lokaal, apart van de opgeschoonde tekst en bij voorkeur in een beveiligde map. Let op met Downloads, gedeelde computers, automatische cloudsync en back-ups.
```

Manual deletion guidance:

```text
Verwijder de Scrub Key handmatig zodra terugzetten niet meer nodig is en uw dossier- of organisatiebeleid dat toestaat. Let op: Scrub kan geen kopieën verwijderen uit Downloads, e-mail, cloudsync of back-ups.
```

Acknowledgement:

- No separate acknowledgement in MVP beyond export acknowledgement.
- Later local desktop versions may require storage-path acknowledgement.

---

### 4.4 Scrub Key import/reload

Current location:

```text
fix_streamlit_nested_expanders.py → scrub_key_import_ui_block
```

Place warning above upload/paste controls and acknowledgement before the `Valideer en laad Scrub Key` button.

Current nearby UI:

```text
st.markdown("**Scrub Key laden**")
st.warning(...)
st.file_uploader("Upload Scrub Key JSON (.json)")
st.text_area("Of plak Scrub Key JSON")
st.button("Valideer en laad Scrub Key")
```

MVP warning before import:

```text
Laad alleen een Scrub Key die bij dit document of dossier hoort. Een geldige sleutel kan originele vertrouwelijke waarden herstellen. Gebruik geen sleutel uit een ander dossier of van een onbekende bron.
```

Required acknowledgement checkbox:

```text
Ik begrijp dat ik alleen een Scrub Key mag laden die bij dit document of dossier hoort.
```

Validation error copy:

```text
Deze Scrub Key kan niet veilig worden geladen. De structuur of verplichte velden kloppen niet. Controleer of dit het juiste bestand is en gebruik geen handmatig aangepakte sleutel zonder extra controle.
```

Correction for implementation copy:

```text
Deze Scrub Key kan niet veilig worden geladen. De structuur of verplichte velden kloppen niet. Controleer of dit het juiste bestand is en gebruik geen handmatig aangepaste sleutel zonder extra controle.
```

Implementation note:

- Keep current validation through `build_scrub_key_import_result`.
- Keep failed import as fail-closed.
- Do not imply that a structurally valid key definitely belongs to the current document.
- Do not log original values from validation failures.

---

### 4.5 Reinsert mode entry

Current location:

```text
fix_streamlit_nested_expanders.py → two_mode_selection_block
fix_streamlit_nested_expanders.py → reinsert_ui_block
```

Place entry warning when `solidprivacy_work_mode == "Originele waarden terugzetten"` and before the reinsert input controls.

MVP warning:

```text
Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens, dossierinformatie of andere vertrouwelijke gegevens bevatten. Controleer het resultaat zorgvuldig voordat u het opslaat of deelt.
```

Local-only copy:

```text
Terugzetten gebeurt lokaal met de geladen Scrub Key. Gebruik de Scrub Key niet in externe AI-diensten.
```

Acknowledgement checkbox before running reinsert:

```text
Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.
```

Implementation note:

- Use the same acknowledgement concept for pasted text, TXT, DOCX and PDF-to-TXT reinsert flows.
- Do not alter `reinsert_from_scrub_key` or document reinsert helpers in this warning implementation package.

---

### 4.6 Pasted-text reinsert action

Current location:

```text
fix_streamlit_nested_expanders.py → reinsert_ui_block → st.button("Zet originele waarden lokaal terug")
```

Required MVP behavior:

- Show critical warning above the button.
- Require acknowledgement before running reinsert.
- Keep current missing-text warning.
- Keep current active Scrub Key validation behavior.

Audit/mismatch warnings should remain near the existing `Controleverslag terugzetten` block.

MVP mismatch/tampering copy:

```text
Deze Scrub Key lijkt mogelijk niet volledig bij deze tekst te passen, of bevat dubbele/ongeldige mappings. Terugzetten kan daardoor onvolledig of onjuist zijn. Controleer het controleverslag en gebruik bij twijfel de juiste sleutel opnieuw.
```

Unknown placeholders copy:

```text
De tekst bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.
```

Duplicate placeholders copy:

```text
De Scrub Key bevat dubbele placeholders. Deze mappings worden niet automatisch teruggezet om verkeerde herleiding te voorkomen.
```

---

### 4.7 TXT file reinsert and restored TXT download

Current location:

```text
fix_streamlit_nested_expanders.py → txt_reinsert_ui_block
```

Place acknowledgement before:

```text
st.button("Zet TXT-bestand lokaal terug")
```

Place restored-output warning before:

```text
st.download_button("Download hersteld TXT-bestand (.txt)")
```

Restored output warning:

```text
De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.
```

Download acknowledgement:

```text
Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.
```

Implementation note:

- Do not change file content bytes, filename or MIME type.
- Do not add blocking based on unknown/not-found placeholders in MVP unless separately approved.
- Warning may be shown when audit fields contain unknown, duplicate or not-found placeholders.

---

### 4.8 DOCX file reinsert and restored DOCX download

Current location:

```text
fix_streamlit_nested_expanders.py → docx_reinsert_ui_block
```

Place acknowledgement before:

```text
st.button("Zet DOCX-bestand lokaal terug")
```

Place restored-output warning before:

```text
st.download_button("Download hersteld DOCX-bestand (.docx)")
```

Restored output warning:

```text
De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.
```

Keep existing DOCX limitation warning and consider strengthening it with:

```text
Let op: DOCX-terugzetten ondersteunt in deze versie normale documenttekst en tabellen. Headers, footers, opmerkingen, bijgehouden wijzigingen, metadata en placeholders die door Word over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund.
```

Implementation note:

- Do not change DOCX helper behavior.
- Do not make clean-DOCX claims.
- Do not block downloads based on hidden-content risk until a later approved DOCX hygiene package defines that policy.

---

### 4.9 PDF-to-TXT reinsert, if present

Current approved PDF scope:

```text
PDF upload → local selectable-text extraction → deterministic Scrub Key reinsert → restored TXT preview/download only
```

Place warnings in the PDF-to-TXT reinsert UI block if present, or in the future patch block that exposes that flow.

MVP copy:

```text
PDF-terugzetten ondersteunt alleen lokaal extraheerbare tekst en levert herstelde TXT-uitvoer op. Het maakt geen herstelde PDF en gebruikt geen OCR.
```

Restored TXT warning should match TXT reinsert:

```text
De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.
```

Implementation note:

- Do not add OCR.
- Do not add restored PDF output.
- Do not imply full PDF reconstruction.

---

### 4.10 Expiry/delete guidance

Current locations:

```text
review_summary_block       → after Scrub Key download guidance
scrub_key_import_ui_block  → before/after import guidance
reinsert_ui_block          → after successful reinsert or in help text
txt_reinsert_ui_block      → after successful reinsert or restored download guidance
docx_reinsert_ui_block     → after successful reinsert or restored download guidance
```

MVP guidance:

```text
Bewaar de Scrub Key niet langer dan nodig. Verwijder de sleutel zodra het doel is afgerond en uw dossier- of organisatiebeleid dat toestaat. Let op: zonder Scrub Key kan Scrub originele waarden niet meer deterministisch terugzetten.
```

Expiry guidance:

```text
Een Scrub Key verloopt niet automatisch. Controleer zelf of de sleutel nog nodig is. Is het doel afgerond? Verwijder de sleutel volgens uw beleid.
```

Manual deletion guidance:

```text
Controleer vóór verwijderen of u de Scrub Key niet meer nodig heeft. Zonder sleutel kan Scrub de originele waarden niet meer automatisch terugzetten. Verwijder daarna ook eventuele kopieën in Downloads, cloudsync, e-mail of gedeelde mappen.
```

MVP behavior:

- Guidance-only.
- No automatic deletion.
- No expiry metadata.
- No old-key blocking.
- No hidden recovery.

---

### 4.11 Shared-computer warning

Current locations:

```text
review_summary_block
scrub_key_import_ui_block
two_mode_selection_block
local storage guidance/help text
```

MVP copy:

```text
Gebruikt u een gedeelde computer, gedeeld browserprofiel of onbeheerde werkplek? Verwerk dan geen echte vertrouwelijke documenten en laat geen Scrub Keys of herstelde bestanden achter in Downloads, recente bestanden of tijdelijke mappen.
```

Implementation note:

- In the Hugging Face demo, this should be guidance/warning text only.
- Do not claim the cloud demo is appropriate for real confidential documents.
- Future local runtime may add stronger checks after WP47/WP48.

---

### 4.12 Email/AI upload warning

Current locations:

```text
review_summary_block      → Scrub Key export/download
scrub_key_import_ui_block → import guidance
two_mode_selection_block  → mode guidance
reinsert_ui_block         → local-only copy
```

MVP copy:

```text
Upload de Scrub Key niet naar externe AI. Voor AI gebruikt u alleen de gecontroleerde opgeschoonde tekst, niet de sleutel. Mail de Scrub Key ook niet mee met de opgeschoonde tekst, tenzij de ontvanger de inhoud bewust mag herleiden.
```

Acknowledgement:

- Include in Scrub Key export acknowledgement.
- Optional in reinsert mode if repeated too often.

---

### 4.13 Loss-of-key warning

Current locations:

```text
review_summary_block → before/after Scrub Key download
expiry/delete guidance help text
future deletion UI, if approved later
```

MVP copy:

```text
Zonder Scrub Key kan Scrub originele waarden niet meer deterministisch terugzetten. Bewaar de sleutel zolang terugzetten nog nodig is, maar verwijder hem daarna volgens uw dossier- of organisatiebeleid.
```

Implementation note:

- Do not promise cloud/server recovery.
- Do not add key recovery features.
- Do not log original values for recovery.

---

### 4.14 Tampering/mismatch warnings

Current locations:

```text
scrub_key_import_ui_block → validation errors
reinsert_ui_block         → Controleverslag terugzetten
txt_reinsert_ui_block     → Controleverslag TXT terugzetten
docx_reinsert_ui_block    → Controleverslag DOCX terugzetten
future PDF-to-TXT block   → audit section
```

Use existing audit fields:

```text
validation_issues
unknown_placeholders
duplicate_placeholders
placeholders_not_found
replacement_count
local_only
ai_processing
cloud_processing
```

MVP copy for mismatch/tampering risk:

```text
Deze Scrub Key lijkt mogelijk niet volledig bij deze tekst te passen, of bevat dubbele/ongeldige mappings. Terugzetten kan daardoor onvolledig of onjuist zijn. Controleer het controleverslag en gebruik bij twijfel de juiste sleutel opnieuw.
```

Unknown placeholders copy:

```text
De tekst bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.
```

Duplicate placeholders copy:

```text
De Scrub Key bevat dubbele placeholders. Deze mappings worden niet automatisch teruggezet om verkeerde herleiding te voorkomen.
```

Implementation note:

- Keep unknown, duplicate and not-found placeholders visible.
- Do not silently repair placeholders.
- Do not guess original values.
- Do not add tamper-proof claims before key-container integrity exists.

---

## 5. MVP acknowledgement inventory

| Moment | MVP acknowledgement? | Suggested key/state name | Notes |
| --- | --- | --- | --- |
| Scrub Key creation preview | No | N/A | Warning only. |
| Scrub Key download/export | Yes | `ack_scrub_key_export_risk` | Disable Scrub Key download until checked. |
| Scrub Key import/reload | Yes | `ack_scrub_key_import_risk` | Disable `Valideer en laad Scrub Key` until checked if key text/file is present. |
| Pasted-text reinsert | Yes | `ack_reinsert_text_confidential` | Disable local reinsert button until checked. |
| TXT reinsert | Yes | `ack_reinsert_txt_confidential` | Disable TXT reinsert button until checked. |
| DOCX reinsert | Yes | `ack_reinsert_docx_confidential` | Disable DOCX reinsert button until checked. |
| PDF-to-TXT reinsert | Yes, if flow is present | `ack_reinsert_pdf_text_confidential` | Also show PDF-scope warning. |
| Restored TXT download | Yes or explicit button text | `ack_download_restored_txt_confidential` | Prefer checkbox near download. |
| Restored DOCX download | Yes or explicit button text | `ack_download_restored_docx_confidential` | Keep DOCX limitation visible. |
| Expiry/delete guidance | No | N/A | Guidance only in MVP. |
| Future deletion action | Yes, later only | TBD | Separate implementation package required. |

Implementation note:

- Use unique Streamlit keys.
- Do not reuse one acknowledgement checkbox across unrelated actions in a way that hides the risk of later actions.
- Acknowledgements should reset naturally with Streamlit session state when the session ends; do not persist them to disk.

---

## 6. Guidance-only warnings in MVP

These warnings are guidance-only and should not block behavior in MVP:

- local storage and Downloads cleanup guidance;
- shared-computer warning;
- expiry guidance;
- manual deletion guidance;
- loss-of-key guidance unless future deletion action exists;
- DOCX limitation warning;
- PDF scope warning;
- audit note that unknown/not-found placeholders require review.

---

## 7. Later blocking candidates

Do not implement these in MVP without a separate approved workpackage:

- block import for detected key/document mismatch;
- block use of expired/no-longer-needed keys;
- block export until protected storage is chosen;
- block restored download if audit has unresolved high-risk conditions;
- block shared-device or cloud-synced storage paths;
- block or require extra approval for failed future integrity checks;
- enforce encrypted key containers;
- enforce local vault storage;
- implement recovery/escrow.

---

## 8. Streamlit implementation risks

1. **Patch fragility** — current UI is modified through startup string replacement. The later implementation must avoid broad replacements that can duplicate UI blocks.
2. **State key collisions** — acknowledgements need stable unique keys across text, TXT, DOCX and PDF-to-TXT flows.
3. **Over-blocking risk** — disabling buttons without clear explanation can feel like changed export semantics. Keep button gating limited to acknowledgement.
4. **Session-state persistence** — acknowledgements should not be treated as durable consent or organizational policy acceptance.
5. **Warning fatigue** — repeat key concepts at high-risk points, but keep copy short and contextual.
6. **No sensitive logging** — do not write original values, full mappings, full keys or local file paths with matter names into logs or audit text.
7. **Hugging Face trust gap** — warning copy must not imply that the cloud demo is safe for real confidential processing.
8. **DOCX/PDF scope confusion** — restored output warnings must not imply complete DOCX/PDF hygiene.

---

## 9. Later implementation test expectations

A later MVP UI implementation package should add or update tests without changing helper semantics.

Expected test direction:

- Scrub Key export warning text appears near the JSON download block.
- Scrub Key export acknowledgement checkbox is present.
- Scrub Key download button is gated by acknowledgement only.
- Scrub Key import warning and acknowledgement appear before validation/loading.
- Reinsert mode warning and acknowledgement appear before pasted-text reinsert.
- TXT reinsert warning and acknowledgement appear before TXT reinsert.
- DOCX reinsert warning and acknowledgement appear before DOCX reinsert.
- Restored TXT/DOCX download warning appears near download buttons.
- Existing audit fields for unknown, duplicate, not-found and validation issues remain visible.
- Tests assert no encryption/deletion/expiry-blocking claims are introduced.
- Tests assert no Scrub Key schema migration is introduced.
- Existing secure import/export helper tests continue to pass.

Likely test files:

```text
tests/test_scrub_key_ui_patch.py
tests/test_two_mode_ui_patch.py
tests/test_txt_reinsert_ui_patch.py
tests/test_docx_reinsert_ui_patch.py
tests/test_scrub_key_secure_import_export.py
```

---

## 10. Recommended next implementation workpackage

Recommended next package:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

Suggested scope:

- Implement MVP warning and acknowledgement copy from this plan in `fix_streamlit_nested_expanders.py`.
- Add/update tests for warning placement and acknowledgement gating.
- Keep all helper, schema, import/export and reinsert semantics unchanged.
- No encryption.
- No automatic deletion.
- No expiry blocking.
- No cloud processing.
- Ask for app verification after Actions/sync are green because UI behavior will change.

Alternative if the coordinator wants more test hardening first:

```text
WP29C — Scrub Key warning UI regression test scaffolding
```

But the recommended path is WP28C because WP27, WP28, WP29 and WP29B now provide enough policy/test basis for warning implementation.

---

## 11. Explicit non-changes in WP28B

This planning package did not change:

- `fix_streamlit_nested_expanders.py`;
- `presidio_streamlit.py`;
- Scrub Key schema;
- Scrub Key import/export behavior;
- reinsert behavior;
- helper logic;
- encryption behavior;
- deletion behavior;
- expiry behavior;
- dependency set;
- cloud/local runtime behavior;
- tests.
