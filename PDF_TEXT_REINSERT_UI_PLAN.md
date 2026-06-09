# PDF_TEXT_REINSERT_UI_PLAN — WP17 planning only

Workpackage: `WP17 — PDF text extraction reinsert UI planning only`  
Repository: `solidprivacy-nl/scrub`  
Status: completed planning/specification-only  
Date: 2026-06-09

This document specifies a safe future UI plan for exposing the WP16 text-based PDF extraction helper.

No UI, code, tests, dependencies, export behavior, Scrub Key behavior, OCR, AI calls or cloud processing are changed by this plan.

---

## 1. Product decision

PDF text extraction may be exposed in the UI, but only in a narrow, explicitly limited form:

```text
PDF support may be exposed only as text-based PDF extraction to restored TXT output.
```

The future UI must not present this as full PDF reinsert. It must not imply layout preservation, legal completeness, visual fidelity or restored PDF generation.

Allowed future direction:

```text
PDF upload → local selectable-text extraction → existing Scrub Key reinsert → restored TXT preview/download only
```

DOCX remains the preferred document-level reinsert route.

Reasoning:

- DOCX is a document format where controlled document-level output is more realistic.
- PDF is a presentation/layout format, so extraction may lose order, structure, headers, footers, tables or columns.
- Text-based PDF support can still be useful when a user only has a PDF with selectable placeholders, but the output must be treated as a text convenience result, not as a reconstructed legal document.

Product decision:

```text
Expose only if the future implementation keeps the UI clearly limited, warning-heavy, local-only and TXT-only.
```

---

## 2. Proposed user workflow

The future workflow should be:

1. User opens `Originele waarden terugzetten`.
2. User loads or pastes a Scrub Key.
3. User uploads a text-based PDF.
4. Scrub extracts selectable text locally.
5. Scrub reinserts values using the Scrub Key.
6. Scrub shows restored TXT preview.
7. Scrub offers restored TXT download only.
8. Scrub shows an audit report and warnings.

The UI must require a deliberate user action before reinsertion. Loading a Scrub Key or uploading a PDF must not automatically restore values.

Recommended processing model:

```text
active Scrub Key + uploaded PDF bytes
→ reinsert_pdf_text_bytes(pdf_bytes, active_scrub_key)
→ restored text/TXT + audit fields + warnings
```

The future implementation should reuse the WP16 helper. It must not create a second replacement engine.

---

## 3. UI placement

The future PDF text extraction UI must be placed only in:

```text
Originele waarden terugzetten
```

It must not appear in the `Anonimiseren` flow.

Suggested placement inside `Originele waarden terugzetten`:

```text
1. Scrub Key laden
2. Originele waarden terugzetten — geplakte tekst
3. TXT-bestand terugzetten
4. DOCX-bestand terugzetten
5. PDF-tekst terugzetten
```

Suggested future section label:

```text
PDF-tekst terugzetten
```

Suggested upload label:

```text
Upload een tekstgebaseerde PDF met placeholders
```

Suggested button label:

```text
Extraheer tekst en zet lokaal terug
```

Suggested preview label:

```text
Herstelde PDF-tekst
```

Suggested download label:

```text
Download herstelde tekst (.txt)
```

Suggested audit label:

```text
Controleverslag PDF-tekst terugzetten
```

The future UI should visually separate restored TXT download from scrubbed export/download controls. It must not be placed near `Download opgeschoonde bestanden` in a way that could confuse scrubbed output with restored sensitive output.

---

## 4. Required warnings

The future UI must show strong warnings before the action button and near the result area.

Required PDF limitation warning:

```text
Let op: PDF-tekstextractie is niet gegarandeerd volledig. Opmaak, kolommen, tabellen, kopteksten, voetteksten en leesvolgorde kunnen afwijken. Controleer de volledige herstelde tekst handmatig voordat u deze gebruikt of deelt.
```

Required sensitive-output warning:

```text
Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten.
```

Required unsupported/OCR warning:

```text
Scans of image-only PDF's worden niet ondersteund. OCR is niet beschikbaar in deze versie.
```

Required output warning:

```text
Scrub maakt geen herstelde PDF. De uitvoer is alleen tekst/TXT.
```

Additional recommended caption:

```text
Deze stap wordt lokaal uitgevoerd met uw Scrub Key. Scrub gebruikt hiervoor geen AI, geen cloudverwerking en geen OCR.
```

The UI should avoid success language that implies completeness. Prefer:

```text
Tekst is lokaal geëxtraheerd en waar mogelijk teruggezet. Controleer het volledige resultaat handmatig.
```

Do not use wording such as:

```text
PDF succesvol hersteld
```

because that implies restored PDF fidelity.

---

## 5. Required audit fields

The future UI must show at least these audit fields:

- document type;
- extracted text length;
- restored value count;
- mapping item count;
- active item count;
- excluded item count;
- placeholders not found;
- unknown placeholders;
- duplicate placeholders;
- validation issues;
- unsupported reason;
- local-only status;
- AI-processing status;
- cloud-processing status;
- OCR-used status;
- PDF-output status.

Suggested Dutch rendering:

```text
Documenttype: <document_type>
Lengte geëxtraheerde tekst: <len(extracted_text)>
Aantal teruggezette waarden: <replacement_count>
Mappingregels totaal: <item_count>
Actieve mappingregels: <active_item_count>
Uitgesloten mappingregels: <excluded_item_count>
Niet gevonden placeholders: <placeholders_not_found>
Onbekende placeholders in tekst: <unknown_placeholders>
Dubbele placeholders in sleutel: <duplicate_placeholders>
Validatieproblemen: <validation_issues>
Niet-ondersteund reden: <unsupported_reason>
Lokaal uitgevoerd: ja/nee
AI-verwerking: ja/nee
Cloudverwerking: ja/nee
OCR gebruikt: ja/nee
PDF-uitvoer gemaakt: ja/nee
```

Expected safe values for a valid WP16-based future implementation:

```text
document_type = pdf_text
local_only = True
ai_processing = False
cloud_processing = False
ocr_used = False
pdf_output = False
```

The UI must display warnings when:

- `validation_issues` is not empty;
- `unsupported_reason` is present;
- `replacement_count` is zero;
- `unknown_placeholders` is not empty;
- `duplicate_placeholders` is not empty;
- `placeholders_not_found` is not empty;
- extracted text length is suspiciously low.

---

## 6. Unsupported cases

Each unsupported or risky case must produce a clear message and must not silently succeed.

### Scanned/image-only PDF

Expected behavior:

- Do not run OCR.
- Show unsupported warning.
- Do not offer restored output as successful.

Suggested message:

```text
Deze PDF bevat geen bruikbare tekstlaag of lijkt een scan/image-only PDF. Scans worden niet ondersteund omdat OCR niet beschikbaar is in deze versie.
```

### PDF with no usable text layer

Expected behavior:

- Mark as unsupported.
- Show the unsupported reason from the helper where available.
- Do not show a successful restored TXT result.

Suggested message:

```text
Geen bruikbare tekstlaag gevonden. Scrub kan alleen tekstgebaseerde PDF's verwerken en gebruikt geen OCR.
```

### Malformed PDF

Expected behavior:

- Show validation issue.
- Do not attempt fallback conversion.
- Do not call external services.

Suggested message:

```text
De PDF kan niet betrouwbaar worden gelezen. Controleer of het bestand een geldige PDF is.
```

### Encrypted/password-protected PDF

Expected behavior:

- Show validation issue or unsupported reason.
- Do not ask for or store passwords in WP18 unless separately approved.
- Do not attempt cloud unlocking or conversion.

Suggested message:

```text
Deze PDF lijkt beveiligd of versleuteld en kan niet lokaal worden uitgelezen in deze versie.
```

### PDF where text extraction returns very little text

Expected behavior:

- Show extracted text length.
- Warn that the result may be incomplete.
- Do not imply legal completeness.

Suggested message:

```text
Er is weinig tekst uit de PDF gehaald. Dit kan betekenen dat de PDF een scan is, een onbruikbare tekstlaag heeft of dat extractie onvolledig is. Controleer het resultaat handmatig.
```

### PDF where placeholders are split or changed

Expected behavior:

- Do not guess or fuzzy-match placeholders.
- Report mapped placeholders not found and/or unknown placeholders.
- Keep output as text only.

Suggested message:

```text
Sommige placeholders zijn mogelijk gesplitst of gewijzigd tijdens PDF-tekstextractie. Scrub zet alleen intacte placeholders terug en gokt niet.
```

### Unknown placeholders

Expected behavior:

- Show the list of unknown placeholders from the result.
- Warn that these placeholders are not in the active Scrub Key.
- Do not invent original values.

Suggested message:

```text
De PDF-tekst bevat placeholders die niet in de actieve Scrub Key staan. Deze waarden zijn niet teruggezet.
```

### Mapped placeholders not found

Expected behavior:

- Show placeholders from the Scrub Key that were not found in the extracted text.
- Warn that this may be caused by missing text, changed placeholders, split placeholders, or a wrong Scrub Key.

Suggested message:

```text
Niet alle mappingregels uit de Scrub Key zijn gevonden in de geëxtraheerde PDF-tekst. Controleer of de juiste Scrub Key is geladen en of de PDF-tekst volledig is geëxtraheerd.
```

---

## 7. Non-goals

The future PDF text reinsert UI must keep these out of scope unless a later workpackage explicitly approves them:

```text
full restored PDF output
OCR
PDF-to-DOCX reconstruction
cloud PDF conversion
AI-based extraction
layout preservation promises
batch PDF processing
real-data PDF test cases
automatic PDF rehydration
```

Also out of scope:

- automatic fuzzy placeholder repair;
- automatic password handling for encrypted PDFs;
- server-side Scrub Key storage;
- durable storage of restored PDF text;
- changes to existing scrubbed TXT/CSV/DOCX/PDF export/download semantics;
- changes to existing pasted-text, TXT or DOCX reinsert semantics;
- changes to Scrub Key import/export behavior.

---

## 8. Safety and privacy rules

The future implementation must preserve:

- local-only processing;
- no AI calls;
- no cloud processing;
- no OCR;
- no real personal data in tests;
- Scrub Key remains sensitive and must be protected;
- restored output may contain confidential data again.

User-facing safety position:

```text
Een Scrub Key maakt vervangen waarden lokaal herleidbaar. Dit is pseudonimisering, geen volledige anonimisering. Bewaar de sleutel lokaal en beveiligd. Deel de Scrub Key niet met AI-diensten of derden tenzij dat bewust en toegestaan is.
```

The future UI must make clear that restored TXT is sensitive output:

```text
Herstelde tekst kan weer originele persoonsgegevens, zaakgegevens of vertrouwelijke informatie bevatten.
```

The future UI must not store uploaded PDFs, Scrub Keys or restored TXT beyond normal in-session UI state unless a later approved storage/vault workpackage changes that policy.

---

## 9. Future implementation package

The safest next implementation workpackage, if approved, is:

```text
WP18 — PDF text extraction to restored TXT UI implementation
```

WP18 must not start inside WP17.

Recommended WP18 scope:

```text
Originele waarden terugzetten only
PDF upload
local text extraction via WP16 helper
restored TXT preview
restored TXT download
audit report
strong warnings
no PDF output
no OCR
no AI/cloud
```

Likely implementation files for WP18, if approved later:

```text
fix_streamlit_nested_expanders.py
tests/test_pdf_text_reinsert_ui_patch.py
```

WP18 should not edit `presidio_streamlit.py` directly unless the coordinator explicitly approves direct UI refactoring. The current project pattern uses `fix_streamlit_nested_expanders.py` for controlled patch-level UI integration.

Required future tests for WP18 should verify at least:

- the PDF UI appears only under `Originele waarden terugzetten`;
- the PDF UI does not appear in `Anonimiseren`;
- the UI imports or references the WP16 helper;
- the upload label is present;
- the action button is present;
- required warnings are present;
- restored TXT preview label is present;
- restored TXT download label is present;
- audit label is present;
- required audit fields are represented;
- no `Download herstelde PDF` label is introduced;
- no OCR wording suggests support;
- no AI/cloud behavior is introduced;
- existing pasted-text, TXT and DOCX reinsert labels remain present;
- existing scrubbed export/download labels remain unchanged;
- existing Scrub Key import/export behavior remains unchanged.

Validation for WP18 should include targeted UI patch tests and app verification after GitHub Actions and Hugging Face sync are green, because WP18 would change UI behavior.

---

## Final planning conclusion

PDF text extraction may be exposed in the UI only as a cautious TXT-only convenience workflow inside `Originele waarden terugzetten`.

The UI must be warning-heavy, audit-visible and explicit that:

- PDF extraction is not guaranteed complete;
- output is restored TXT/text only;
- restored output may contain sensitive/confidential values again;
- DOCX remains the preferred document-level reinsert route;
- full restored PDF output, OCR, PDF-to-DOCX reconstruction, cloud conversion and AI-based extraction remain out of scope.
