## 2026-08-04 23:15 Europe/Amsterdam — Kortere placeholders in de controleweergave

- Lange documentgebonden placeholders worden in de controleweergave compacter getoond. Zo wordt bijvoorbeeld `[LOCATIE_BSK732WYQ424ZIEQ6_02]` zichtbaar als `[LOCATIE_02]`.
- Handmatig toegevoegde waarden krijgen in de weergave een korte `H`, bijvoorbeeld `[EMAIL_H_03]`.
- Dit is uitsluitend een leesbaarheidsverbetering: de volledige beveiligde placeholder blijft intern en in gedownloade documenten intact.
- Scrub Key, documentbinding, controlewaarde en originele waarden terugzetten zijn niet gewijzigd.
- Vrij aangepaste vervangtekst en oudere of afwijkende placeholders worden niet stilzwijgend herschreven.
- Direct selecteren van een gemiste waarde blijft op de volledige onderliggende tekst werken, ook na een compact weergegeven placeholder.
- Menselijke controle blijft noodzakelijk.

## 2026-08-04 22:22 Europe/Amsterdam — Direct maskeren vanuit de verwerkte tekst geverifieerd

De nieuwe correctieroute is live gecontroleerd: een gemiste waarde kan direct in de verwerkte tekst worden geselecteerd, veilig worden geïnspecteerd, als type worden toegevoegd en daarna weer ongedaan worden gemaakt. De vervangtabel, handmatige invoer, downloads, Scrub Key en herstelroute blijven beschikbaar.

De lange documentbinding in placeholders blijft technisch intact. Een afzonderlijke verbetering gaat de weergave compacter maken zonder de beveiliging te verkorten.

## 2026-08-04 — Gemiste waarden direct vanuit de tekst maskeren

- In `Verwerkte tekst` kan een gebruiker een nog zichtbare gevoelige waarde selecteren en via rechtermuisknop, toetsenbord of `Masker selectie` toevoegen.
- Scrub controleert de selectie eerst op de server en toont hoeveel exacte voorkomens in het document worden geraakt.
- De gebruiker kiest zelf een algemeen type, zoals persoon, organisatie, locatie, e-mailadres, telefoonnummer, datum/tijd of referentie.
- De eerste versie maskeert alle veilige exacte voorkomens van de gekozen waarde; alleen één specifieke tekstpositie maskeren is nog niet ondersteund.
- Korte of botsende selecties die onderdeel zijn van een langere waarde worden geblokkeerd en verwezen naar de bestaande gedetailleerde invoer.
- Een bevestigde selectie wordt als normale handmatige rij zichtbaar in de bestaande vervangtabel.
- De meest recente ongewijzigde selectieactie kan één stap ongedaan worden gemaakt.
- `Gemiste waarde toevoegen`, de volledige vervangtabel en de statische reviewweergave blijven als fallback beschikbaar.
- Exportformaten, Scrub Key, terugzetten, herkenningsprofielen en documentverwerking zijn niet gewijzigd.
- Menselijke controle blijft verplicht; de functie versnelt correctie maar geeft geen garantie dat alle gevoelige gegevens zijn gevonden.

---

## 2026-08-03 — Langere synthetische zorgvoorbeelden

- De acht voorbeelden onder `Zorgcontrole — streng` bevatten nu langere, realistisch opgebouwde zorgteksten.
- Elk voorbeeld krijgt vijf herkenbare inhoudssecties, bijvoorbeeld observaties, beoordeling, zorgacties en vervolgafspraken.
- De bestaande synthetische namen, nummers en andere testwaarden blijven gelijk, zodat herkenningsresultaten vergelijkbaar blijven.
- De extra tekst introduceert geen nieuwe persoonsnamen, identificatienummers, data, adressen of contactgegevens.
- Diagnose, medicatie, observaties, laboratoriuminformatie en andere klinische betekenis blijven leesbare testcontext.
- Herkenning, vervangtabel, export, Scrub Key en terugzetten zijn niet gewijzigd.
- Menselijke controle blijft noodzakelijk; de voorbeelden zijn synthetische testdocumenten en geen productiebenchmark.

---

## 2026-08-03 — Zorgcontrole toegevoegd aan het prototype

- De controlemodus krijgt een vierde keuze: `Zorgcontrole — streng`.
- De bestaande juridische controle blijft de standaardkeuze; Zorg wordt nooit stilzwijgend geactiveerd.
- Zorgcontrole zoekt extra naar patiënt- en cliëntnummers, EPD/ECD- en dossiernummers, verzekerden- en verwijsnummers, laboratorium- en incidentreferenties, zorgverleners, zorgorganisaties, locaties en exacte zorgdata.
- Acht volledig synthetische zorgvoorbeelden zijn beschikbaar om de werking te testen.
- Zorgverlener-, organisatie-, locatie- en zorgdatumregels blijven standaard geselecteerd, maar krijgen zichtbaar de status `Controle nodig`.
- Mogelijke gemiste administratieve zorgreferenties worden alleen als uitgevinkte controlekandidaat toegevoegd.
- Diagnose, medicatie, doseringen, laboratoriumwaarden en observaties blijven een expliciet te behouden onderdeel van de tekst.
- De vervangtabel, documentdownloads, Scrub Key, terugzetten en bestandsformaten zijn niet gewijzigd.
- Menselijke controle blijft noodzakelijk; deze prototypefunctie is geen productiegarantie.

---

## 2026-07-28 — Verkeerde Scrub Key wordt vóór herstel geblokkeerd

- Nieuwe documentgebonden Scrub Keys worden automatisch vergeleken met de documentcode in het aangeleverde bestand.
- Een verkeerde sleutel, meerdere documentcodes of een ongeldige controlewaarde blokkeren het terugzetten voordat originele waarden worden hersteld.
- Bij een geldige documentgebonden match toont de app dat document en sleutel aantoonbaar bij elkaar horen.
- Oudere Scrub Keys blijven bruikbaar voor compatibiliteit, maar de app waarschuwt zichtbaar dat de documentmatch niet kan worden bewezen.
- De bestaande drie stappen, downloadnamen en TXT/DOCX/PDF-naar-TXT-grenzen blijven gelijk.

---

## 2026-07-27 — Document en Scrub Key worden aan elkaar gekoppeld

- Nieuwe standaardplaceholders bevatten een niet-gevoelige documentcode.
- De bijbehorende Scrub Key bevat dezelfde code en een controlewaarde tegen onbedoelde wijzigingen.
- Vrij aangepaste vervangtekst blijft ongewijzigd, maar kan niet als geverifieerde documentgebonden Scrub Key worden gedownload.
- Bestandsnamen, documentformaten en de bestaande reviewstappen blijven gelijk.

---

## 2026-07-27 — Terugzetten werkt nu in drie logische stappen

- Begin met het TXT-, DOCX- of PDF-bestand dat je wilt herstellen; geplakte tekst blijft beschikbaar als alternatief.
- Voeg daarna de bijbehorende Scrub Key toe. De sleutel wordt automatisch gelezen en gevalideerd.
- Zodra bestand en sleutel geldig zijn, wordt het lokale herstel automatisch voorbereid en verschijnt de downloadstap.
- De afzonderlijke vinkjes en knoppen voor het laden/valideren van de sleutel en het starten van het herstel zijn verwijderd.
- Eén duidelijke bevestiging blijft staan vóór de download, omdat het herstelde resultaat opnieuw vertrouwelijke gegevens kan bevatten.
- DOCX-, TXT- en PDF-naar-TXT-uitvoer, bestandsnamen en bekende beperkingen blijven ongewijzigd.

---

## 2026-07-17 — DOCX-herstel omvat nu kop- en voetteksten

- Bij het terugzetten van originele waarden in een DOCX worden nu ook bestaande kop- en voetteksten meegenomen.
- Hoofdtekst en tabellen blijven ondersteund.
- Opmerkingen, alleen-in-wijzigingen aanwezige tekst, voetnoten/eindnoten, tekstvakken, metadata en placeholders die over meerdere Word-tekstnodes zijn verdeeld, blijven buiten deze versie.
- PDF-herstel blijft beperkt tot herstelde TXT; OCR en een hersteld PDF-bestand zijn niet toegevoegd.

---

## 2026-07-16 — Handmatige aanvulling compacter

- `Gemiste waarde toevoegen` gebruikt bij openen een compactere invoerregel voor waarde, type en vervanging.
- De dubbele interne kop is verwijderd; de functie en validatiemeldingen blijven ongewijzigd.
- De vervangtabel, exports, Scrub Key en terugzetworkflow zijn niet gewijzigd.

---

## 2026-07-03 — Secondary review controls calmer

- De extra controleopties onder `2. Controleer resultaat` krijgen een duidelijker verzamelpunt: `Meer controleopties`.
- Handmatige aanvulling, vervangtabel, stap-voor-stap controle, Scrub Key, downloads en auditdetails blijven beschikbaar.
- Export, Scrub Key, reinsert, herkenning en bestandssemantiek zijn niet gewijzigd.

---

## 2026-07-03 — Review surface calmer

- De controleweergave is rustiger gemaakt: de side-by-side controle gebruikt kortere tekst en verwijst duidelijker naar veilig downloaden als volgende stap.
- De vervangtabel, handmatige aanvulling, stap-voor-stap controle, Scrub Key, documentdownloads en auditdetails blijven beschikbaar.
- Export, Scrub Key, reinsert, herkenning en bestandssemantiek zijn niet gewijzigd.

---

## 2026-06-23 20:43 Europe/Amsterdam — Reinsert interface simplified

## 2026-06-23 — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

- Fixed DOCX plain-text extraction order for side-by-side preview.
- DOCX body paragraphs and tables are now read in document XML order instead of all paragraphs first and all tables afterwards.
- Added synthetic regression coverage for interleaved paragraph/table order.
- Preserved DOCX export, Scrub Key and reinsert semantics.
- Validation: `python -m pytest tests -x -vv` → 649 passed in 102.51s.

- The “Originele waarden terugzetten” workflow is now presented as a clearer four-step flow:
  1. Voeg Scrub Key toe
  2. Voeg tekst of document toe
  3. Controleer herstelrapport
  4. Download herstelde output
- Existing safety controls remain in place: Scrub Key warnings, acknowledgement gates and restored-output warnings.
- Existing restored output semantics remain unchanged: filenames, MIME types and supported output types are preserved.
- PDF reinsert remains TXT-only: no restored PDF, no OCR, no cloud processing and no AI processing.


# SolidPrivacy Scrub — Release Notes

## Execution interface simplification

- The default Scrub flow is calmer and more execution-oriented: add document/text, check result, export result.
- Secondary controls remain available but are collapsed by default.
- Primary document downloads remain visible; Scrub Key and audit downloads are separated into optional sections.
- No export, Scrub Key, reinsert or recognition behavior was changed.


This file is the user-facing product changelog.

For internal workpackage history, see `CHANGELOG.md` and `handover/workpackages/`.

---

## Current prototype capabilities

### Scrub / anonymize

- Upload and process supported document text flows in the Streamlit prototype.
- Review detected replacement candidates before export.
- Add a missed value manually with `Gemiste waarde toevoegen` so it enters the existing replacement table before export.
- Preserve legal/professional context where possible.
- Nederlandse juridische referenties zoals dossier-, zaak-, cliënt- en administratieve referentiecodes worden beter als review-kandidaat zichtbaar gemaakt wanneer automatische herkenning ze mist.
- Juridische rolwoorden blijven beter behouden als juridische context; Scrub doet geen claim dat alle juridische nummers altijd automatisch worden herkend.
- Export scrubbed outputs according to existing app behavior.

### Review

- The review flow has one central side-by-side review surface near the top of the review workflow.
- The side-by-side review surface uses one section heading: `2. Controleer resultaat`.
- `Brontekst` appears on the left and `Verwerkte tekst` on the right.
- The side-by-side panes use equal visual height.
- The side-by-side panes scroll together by default.
- The side-by-side helper text is shorter and clearer: it says that this view is for comparison and that decisions are still made in the replacement table.
- Markers are on by default and can be hidden with `Markeringen tonen`.
- Users can add a missed value manually near `2. Controleer resultaat`; it is added to the same replacement table used for export.
- The detailed replacement-table section is visually quieter: the replacement table is now under a collapsed `Vervangtabel controleren — <items> items` section.
- The replacement table remains the source of truth and fallback for review decisions and export construction.
- Serial review remains available as a small read-only review aid below the replacement table, with clearer Dutch labels for open items, risk items, duplicate values and next open item.
- Markers are visual-only. They do not change the replacement table, export, Scrub Key or reinsert behavior.

### Export

- Improved the export/download section by grouping document downloads, Scrub Key and audit/technical files more clearly.
- Existing export content, filenames and file types remain unchanged.
- The Scrub Key remains sensitive because it can restore original values.

### Scrub Key

- Export a Scrub Key JSON mapping file.
- Import/reload a Scrub Key for controlled reinsert.
- Clear warnings are shown because the Scrub Key can restore confidential values.
- Scrub Key export and import now require an explicit acknowledgement before the high-risk action button is active.

### Reinsert

Supported reinsert paths:

```text
Pasted text → restored text
TXT upload  → restored TXT
DOCX upload → restored DOCX, within documented helper limits
PDF upload  → restored TXT only
```

- Pasted-text, TXT, DOCX and PDF-to-TXT reinsert actions now require acknowledgement that restored output is confidential again.
- Restored output download buttons now show an additional warning and acknowledgement before download.
- The restored output content, filenames and file types are unchanged after acknowledgement.

PDF support is intentionally limited:

- restored output is TXT only;
- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no layout preservation guarantee;
- scanned/image-only PDFs are unsupported.

---

## Known important limitations

- The Hugging Face Space is a demo/development environment, not the final local confidential processing environment.
- The final product direction is local-first/offline capable.
- The Scrub Key is sensitive because it can re-identify scrubbed content.
- UI acknowledgements are safety prompts, not managed key storage.
- Side-by-side synchronized scrolling is percentage-based and can still create imperfect alignment when source and processed text differ structurally.
- The review table remains the source of truth and fallback.
- The side-by-side review surface does not implement direct marking in the document text, an advanced editor or full-document marking.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

The roadmap prioritizes MVP product quality across:

```text
Import → Scrub → Review → Handmatig aanvullen → Replace → Scrub Key → Reinsert → Export → Audit
```

Local installer work remains later, after the core workflow is good enough.
