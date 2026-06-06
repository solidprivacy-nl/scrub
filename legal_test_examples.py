"""Expanded fake Dutch legal test examples for SolidPrivacy Scrub.

All examples are fully synthetic. They are intentionally longer than the first
smoke-test examples, so the Dutch Legal Strict profile can be tested on more
realistic legal document structure, legal roles, matter identifiers, addresses,
dates, phone numbers, e-mail addresses, court references and false-positive traps.

These examples are not legal advice and do not contain real client data.
"""

from __future__ import annotations

from typing import Dict, List


TEST_CASES: List[Dict[str, object]] = [
    {
        "name": "Arbeidsrecht - lang verweerschrift ontslag",
        "text": """RECHTBANK MIDDEN-NEDERLAND
Team kanton en handelsrecht, locatie Utrecht

Zaaknummer: 10598721 / UE VERZ 26-441
Dossiernummer: ARB-2026-00421
Cliëntnummer: CL-88421
Betreft: verweerschrift namens werknemer in ontslagzaak

Geachte kantonrechter,

Namens cliënt Jan Jansen, geboren op 12-05-1980, wonende aan Keizersgracht 123, 1015 CJ Amsterdam, dien ik hierbij een verweerschrift in tegen het verzoek van werkgever BrightCare B.V., gevestigd aan Zorglaan 7, 3521 AB Utrecht. Cliënt is bereikbaar via 06 12345678 en via jan.jansen@example.nl. De datum 12-05-1980 is een geboortedatum en mag niet als BSN worden gezien. Ook de datum 20-11-2026 is slechts de datum waarop de mondelinge behandeling voorlopig is gepland.

Werkgever stelt dat sprake is van verwijtbaar handelen omdat cliënt op 14-03-2026 niet op het rooster zou zijn verschenen. Cliënt betwist dat. Uit de WhatsApp-correspondentie met teamleider mevrouw Karin de Waal blijkt dat cliënt op 13-03-2026 telefonisch heeft gemeld dat hij ziek was. Het telefoonnummer waarmee de ziekmelding is gedaan, was 06 12345678. De bedrijfsarts, dr. Pieter van Leeuwen, BIG-nummer 12345678901, heeft op 18-03-2026 bevestigd dat cliënt arbeidsongeschikt was. De medische reden wordt in dit processtuk niet inhoudelijk beschreven, maar de enkele verwijzing naar arbeidsongeschiktheid is relevant voor het arbeidsrechtelijke kader.

Het door werkgever overgelegde onderzoeksrapport draagt referentie BC-ONDR-2026-7781. In het rapport wordt cliënt aangeduid als werknemer 4417. De salarisadministratie gebruikt daarnaast personeelsnummer PERS-2026-1187. De gemachtigde van werkgever, mr. Simone Kuipers, gebruikt in correspondentie kenmerk SK/BrightCare/JJ/2026-04. Namens cliënt wordt verzocht deze gegevens als matter-identifying te behandelen wanneer het stuk extern of in een AI-tool wordt gebruikt.

Cliënt stelt dat het ontslag op staande voet niet rechtsgeldig is gegeven. Er was geen dringende reden, de werkgever heeft onvoldoende onderzoek gedaan en het ontslag is niet onverwijld medegedeeld. Subsidiair wordt aanspraak gemaakt op loon, vakantiebijslag, transitievergoeding, billijke vergoeding en wettelijke verhoging. De bankrekening waarop achterstallig loon normaliter werd betaald is NL91 ABNA 0417 1643 00, ten name van Jan Jansen. Dit IBAN is uitsluitend opgenomen om de detectie van financiële gegevens te testen.

De wederpartij heeft in haar verzoekschrift ook verwezen naar een intern incidentnummer INC-2026-0912 en naar een e-mailbericht van 16-03-2026 met onderwerp 'afwezigheid Jan'. Dat soort referenties kan in combinatie met de werkgever en de functie van cliënt herleidbaar zijn. Daarom hoort een juridische scrubber niet alleen namen en e-mailadressen te maskeren, maar ook dossiernummers, cliëntnummers, personeelsnummers, interne incidentnummers en zaakreferenties.

Conclusie: cliënt verzoekt de kantonrechter het verzoek van BrightCare B.V. af te wijzen, het ontslag op staande voet te vernietigen en werkgever te veroordelen tot doorbetaling van loon, vermeerderd met wettelijke verhoging en wettelijke rente.
""",
        "should_contain": [
            "NL_ADDRESS",
            "NL_POSTCODE",
            "NL_PHONE_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_DATE_OF_BIRTH",
            "NL_BIG_NUMBER",
            "NL_IBAN",
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Familierecht - lang verzoekschrift gezag en omgang",
        "text": """AAN DE RECHTBANK AMSTERDAM
Team familie en jeugdrecht

Zaaknummer: C/13/701234 / FA RK 26-321
Rekestnummer: RK-2026-887
Dossiernummer: FAM-2026-00314
Cliëntnummer: CL-FAM-55201

VERZOEKSCHRIFT WIJZIGING OMGANGSREGELING EN INFORMATIEREGELING

Verzoeker Fatima El Amrani, wonende aan Proceslaan 44, 1098 ZX Amsterdam, kiest woonplaats ten kantore van haar advocaat mr. Noor van Dijk, Fictief Advocaten, aan de Juristenkade 12, 1017 AB Amsterdam. Verweerder Peter Bakker, wonende aan Laan van Meerdervoort 55, 2517 AM Den Haag, wordt in deze procedure bijgestaan door mr. Sander Meijer. De minderjarige Sami El Amrani, geboren op 03-09-2015, staat ingeschreven op het adres van verzoeker. De geboortedatum 03-09-2015 is alleen een datum en mag niet als telefoonnummer, postcode of BSN worden gemarkeerd.

Partijen zijn op 22-06-2014 met elkaar gehuwd en bij beschikking van deze rechtbank van 12-10-2023 is de echtscheiding uitgesproken. In die beschikking is bepaald dat de minderjarige hoofdverblijfplaats heeft bij verzoeker en dat verweerder eenmaal per twee weken omgang heeft van vrijdag 17.00 uur tot zondag 18.00 uur. De beschikking is geregistreerd onder intern kenmerk FAM/AMS/2023/7788. De communicatie tussen partijen verloopt sinds januari 2026 moeizaam en wordt deels gevoerd via het e-mailadres fatima.elamrani@example.nl en deels via het telefoonnummer +31 6 44556677.

Verzoeker stelt dat de bestaande omgangsregeling niet langer in het belang van de minderjarige is. De minderjarige heeft op school, Basisschool De Horizon, meerdere malen aangegeven spanning te ervaren voorafgaand aan de weekendregeling. De intern begeleider, mevrouw Elise van Roon, heeft hierover op 15-04-2026 een verslag opgesteld met schoolreferentie HRZ-SAM-2026-04. Verzoeker wenst niet dat de schoolreferentie, de naam van de minderjarige of de concrete woonadressen zichtbaar blijven wanneer dit processtuk buiten de procedure wordt gebruikt.

Verweerder betwist dat sprake is van een onveilige situatie. Hij stelt dat verzoeker de omgang frustreert en verwijst naar berichten van 08-02-2026, 15-02-2026 en 01-03-2026. Deze data zijn gewone procesdata en mogen niet als BSN worden gezien. Verweerder voert aan dat hij beschikt over een passende woning en dat de minderjarige een eigen slaapkamer heeft. Zijn telefoonnummer is 070 2345678 en zijn alternatieve e-mailadres is peter.bakker@example.nl.

Verzoeker verzoekt de rechtbank de omgang tijdelijk te beperken tot begeleide omgang via een omgangshuis, althans een regeling vast te stellen waarbij de overdrachten plaatsvinden op neutraal terrein. Daarnaast wordt verzocht een informatieregeling vast te stellen waarbij verweerder eenmaal per maand per e-mail wordt geïnformeerd over school, gezondheid en belangrijke gebeurtenissen. De belangen van de minderjarige staan daarbij voorop.

Bijlagen:
1. Beschikking rechtbank Amsterdam d.d. 12-10-2023;
2. Verslag Basisschool De Horizon, referentie HRZ-SAM-2026-04;
3. Overzicht communicatie via telefoonnummer +31 6 44556677;
4. Uittreksel BRP met adresgegevens van verzoeker en minderjarige.

Aldus opgesteld te Amsterdam op 06-06-2026.
""",
        "should_contain": [
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
            "NL_REKESTNUMMER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_PHONE_NUMBER",
            "NL_DATE_OF_BIRTH",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Strafrecht - lange pleitnotitie verdachte",
        "text": """RECHTBANK ROTTERDAM
Team strafrecht

Parketnummer: 10/456789-26
Proces-verbaalnummer: PL1700-20260518-334455
CJIB-nummer: 9876543210123456
Dossiernummer advocaat: STRAF-2026-00991
Betreft: pleitnotitie voorlopige hechtenis

Edelachtbare rechtbank,

Namens verdachte Mohamed Ait Said, geboren op 17-08-1992 en wonende aan Havenstraat 8, 3024 KL Rotterdam, wordt het volgende naar voren gebracht. Verdachte wordt bijgestaan door mr. Eva Brouwer, advocaat te Rotterdam. Het telefoonnummer van verdachte is 06 99887766 en zijn e-mailadres is mohamed.aitsaid@example.nl. De datum 17-08-1992 is een geboortedatum. Het nummer 10/456789-26 is een parketnummer en moet niet als telefoonnummer worden geïnterpreteerd.

De verdenking betreft diefstal in vereniging, subsidiair heling, gepleegd op of omstreeks 18-05-2026 in Rotterdam. Het proces-verbaal vermeldt dat aangever Pieter van Dam aangifte heeft gedaan namens Winkelbedrijf Maas B.V., gevestigd aan Koopmansplein 3, 3011 AA Rotterdam. In het dossier wordt daarnaast verwezen naar camerabeeld met referentie CAM-MAAS-2026-0518 en naar een intern incidentnummer van de winkel, INC-WM-559812.

De verdediging stelt dat ernstige bezwaren onvoldoende blijken uit het dossier. De enkele herkenning door verbalisant J. Vermeer is niet ondersteund door objectieve kenmerken. In het proces-verbaal van bevindingen wordt gesproken over 'een man met donkere jas', maar er wordt geen uniek kledingstuk, tatoeage of ander onderscheidend kenmerk genoemd. Het telefoonnummer +31 6 11223344 dat in het dossier wordt genoemd, behoort volgens verdachte niet aan hem toe. Dit nummer is in het dossier aangetroffen bij een andere betrokkene, aangeduid als getuige A.

Slachtoffer of aangever Pieter van Dam heeft verklaard dat hij de verdachte niet persoonlijk kent. De medeverdachte, volgens het dossier Youssef Benali, heeft zich beroepen op zijn zwijgrecht. De verdediging verzoekt bij openbaar gebruik van deze pleitnotitie de namen van verdachte, aangever, medeverdachte en getuigen te maskeren, maar termen als verdachte, aangever, slachtoffer, medeverdachte en getuige te laten staan. Deze rollen zijn juridisch relevant en maken de tekst leesbaar.

Ten aanzien van de persoonlijke omstandigheden merkt de verdediging op dat verdachte een huurwoning heeft, werkt via uitzendbureau WerkPunt B.V. en mantelzorg verleent aan zijn moeder, mevrouw Samira Ait Said. Deze omstandigheden zijn relevant voor het recidiverisico en de proportionaliteit van voorlopige hechtenis. Tegelijkertijd zijn namen, adressen, werkgever, dossiernummers en telefoonnummers privacygevoelig en matter-identifying.

De verdediging verzoekt de voorlopige hechtenis op te heffen, althans te schorsen onder voorwaarden, waaronder een meldplicht, een contactverbod met aangever en een locatieverbod voor Winkelbedrijf Maas B.V. De zitting is gepland op 20-11-2026. Ook die datum is slechts een datum en mag niet als BSN worden gezien.
""",
        "should_contain": [
            "NL_PARKETNUMMER",
            "NL_CJIB_NUMBER",
            "NL_POLICE_REPORT_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_PHONE_NUMBER",
            "NL_DATE_OF_BIRTH",
            "NL_COURT_OR_AUTHORITY",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Civiel recht - lange dagvaarding met rolnummer en ECLI",
        "text": """RECHTBANK AMSTERDAM
Team handel

Rolnummer: CV EXPL 26-9921
Zaaknummer: C/13/712345 / HA ZA 26-210
ECLI eerdere uitspraak: ECLI:NL:RBAMS:2026:1234
Dossiernummer: CIV-2026-00721

DAGVAARDING INZAKE BETALINGSVORDERING

Eiser Stichting Woonrecht, gevestigd aan Processtraat 22, 1012 AB Amsterdam, wordt in deze zaak vertegenwoordigd door mr. Lotte Vermeer. Gedaagde Pieter de Groot, wonende aan Oude Haven 19, 2312 BT Leiden, wordt aangeschreven in verband met een openstaande betalingsverplichting uit hoofde van een dienstverleningsovereenkomst. Het IBAN van gedaagde dat in de overeenkomst is vermeld, luidt NL91 ABNA 0417 1643 00. Het telefoonnummer van gedaagde in het klantdossier is 071 2345678 en zijn e-mailadres is pieter.degroot@example.nl.

Eiser stelt dat gedaagde op 01-02-2026 een overeenkomst heeft gesloten voor juridische ondersteuning bij een huurgeschil. De factuur met nummer FACT-2026-4481 is verzonden op 15-03-2026 en bleef ondanks herinneringen van 01-04-2026 en 15-04-2026 onbetaald. Deze factuurdata moeten niet worden gezien als BSN, telefoonnummer of postcode. De interne klantreferentie van eiser is WR-KLANT-2026-7712. In correspondentie wordt daarnaast verwezen naar zaakreferentie ZK-WOON-55091.

Gedaagde heeft per e-mail aangevoerd dat de overeenkomst door misverstand tot stand zou zijn gekomen. Hij verwijst naar contact met medewerker Sara van den Berg en stelt dat hem telefonisch zou zijn toegezegd dat de eerste beoordeling kosteloos was. Eiser betwist dat. Uit het gespreksverslag van 02-02-2026 blijkt dat een uurtarief is genoemd en dat de algemene voorwaarden digitaal zijn verzonden.

Eiser vordert betaling van EUR 1.842,50, vermeerderd met wettelijke rente en buitengerechtelijke incassokosten. Daarnaast vordert eiser proceskosten. Indien dit processtuk wordt gebruikt voor training, analyse of externe AI-verwerking, moeten namen van natuurlijke personen, adressen, bankrekeningnummers, telefoonnummers, e-mailadressen, rolnummer, zaaknummer, dossiernummer en klantreferenties worden verwijderd of vervangen. Het woord eiser en het woord gedaagde moeten juist blijven staan, omdat die rollen nodig zijn om het juridische betoog te begrijpen.

In een vergelijkbare zaak heeft deze rechtbank op 12-01-2026 geoordeeld, gepubliceerd onder ECLI:NL:RBAMS:2026:1234, dat duidelijke informatie over tarieven vooraf moet worden verstrekt. Die ECLI is een juridische verwijzing en kan soms openbaar zijn, maar in een scrubmodus voor externe AI kan ook een ECLI als matter-identifying worden gemaskeerd wanneer de combinatie met partijen herleidbaarheid oplevert.

Eiser verzoekt de kantonrechter gedaagde te veroordelen tot betaling van de hoofdsom, rente, incassokosten en proceskosten.
""",
        "should_contain": [
            "NL_ROLNUMMER",
            "NL_LEGAL_CASE_NUMBER",
            "NL_ECLI",
            "NL_DOSSIER_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_IBAN",
            "NL_PHONE_NUMBER",
            "NL_COURT_OR_AUTHORITY",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Letselschade - lange aansprakelijkstelling en medische context",
        "text": """AANSPRAKELIJKSTELLING LETSELSCHADE

Schadenummer: LS-2026-009812
Polisnummer: POL-44556677
Dossiernummer: LETSEL-2026-77104
Claimreferentie verzekeraar: CLM-2026-112233

Geachte heer/mevrouw,

Namens slachtoffer Emma Smit, wonende aan Revalidatielaan 6, 6812 CD Arnhem, stel ik hierbij verzekerde Koeriersdienst Snelweg B.V., gevestigd aan Transportweg 45, 3542 AB Utrecht, aansprakelijk voor de gevolgen van het ongeval van 15-12-2025. Het ongeval vond plaats op de kruising van de Fictieveweg en de Spoorlaan te Arnhem. Het telefoonnummer van slachtoffer is +31 6 87654321 en haar e-mailadres is emma.smit@example.nl.

Cliënte is na het ongeval behandeld door huisarts dr. Bram Koster, BIG-nummer 12345678901, en vervolgens door fysiotherapeut Lisa van Rijn. In de medische correspondentie wordt verwezen naar patiëntnummer PAT-2026-55441. De medische diagnose wordt hier bewust beperkt omschreven, maar de termen nekklachten, hoofdpijn, concentratieproblemen en arbeidsongeschiktheid zijn relevant voor de schadebegroting. Een scrubber moet namen, adressen, patiëntnummers, BIG-nummers, telefoonnummers en e-mailadressen maskeren, maar niet de juridische of medische context zo breed verwijderen dat het schadebeeld onleesbaar wordt.

Uit het politierapport met proces-verbaalnummer PL0900-20251215-778899 blijkt dat de bestuurder van de bestelbus, de heer Mark de Wit, de voorrangsregels niet in acht heeft genomen. Zijn werkgever heeft de schade gemeld bij verzekeraar VeiligVerkeer Schade N.V. onder schadenummer LS-2026-009812. In de correspondentie wordt ook verwezen naar kenteken XX-123-X en intern dossiernummer VV-ARN-2026-4409. De datum 15-12-2025 is uitsluitend een datum; de reeks 20251215 in het proces-verbaalnummer is onderdeel van de politie-referentie en niet een geboortedatum.

Cliënte werkte voor het ongeval als administratief medewerker bij ZorgAdministratie Nederland B.V. te Arnhem. Door de klachten is zij sinds 16-12-2025 gedeeltelijk arbeidsongeschikt. De werkgever heeft loon doorbetaald maar maakt aanspraak op regres. Het personeelsnummer van cliënte in de loonadministratie is PERS-7721. Het bankrekeningnummer waarop schadevergoeding kan worden betaald is NL02 RABO 0123 4567 89. Dit is testdata en geen werkelijk rekeningnummer.

Namens cliënte verzoek ik erkenning van aansprakelijkheid binnen veertien dagen, betaling van een voorschot van EUR 2.500,00 en bevestiging dat redelijke kosten ter vaststelling van schade en aansprakelijkheid worden vergoed. Alle hiervoor genoemde persoonsgegevens en matter-identifiers moeten in een extern te gebruiken versie worden gescrubd, terwijl termen als slachtoffer, verzekeraar, bestuurder, werkgever en huisarts behouden moeten blijven.
""",
        "should_contain": [
            "NL_INSURANCE_CLAIM_NUMBER",
            "NL_BIG_NUMBER",
            "NL_PHONE_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_DOSSIER_NUMBER",
            "NL_POLICE_REPORT_NUMBER",
            "NL_IBAN",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Huurrecht - lange conclusie van antwoord",
        "text": """RECHTBANK DEN HAAG
Team kanton, locatie Den Haag

Rolnummer: CV EXPL 26-1844
Dossiernummer: HUUR-2026-00382
Cliëntnummer: CL-HUUR-7718
Betreft: conclusie van antwoord in huurzaak

CONCLUSIE VAN ANTWOORD

Gedaagde Nadia Verhoeven, wonende aan Huurdersplein 18, 2525 LM Den Haag, voert verweer tegen de vordering van eiser Vastgoed Noordzee B.V., gevestigd aan Beleggingslaan 4, 2596 AA Den Haag. Gedaagde wordt bijgestaan door mr. Thomas van Es. De gemachtigde van eiser is mr. Petra de Koning. Gedaagde is bereikbaar via 06 55443322 en via nadia.verhoeven@example.nl.

Eiser vordert ontbinding van de huurovereenkomst en ontruiming van de woning wegens een gestelde huurachterstand. Gedaagde betwist de hoogte van de achterstand. Volgens haar betalingsbewijzen is op 01-02-2026, 01-03-2026 en 01-04-2026 telkens huur betaald op IBAN NL91 ABNA 0417 1643 00 ten name van Vastgoed Noordzee B.V. De data in deze zin zijn betalingsdata en moeten niet als BSN of telefoonnummer worden gemarkeerd.

Gedaagde voert aan dat zij sinds 10-01-2026 ernstige gebreken aan de woning heeft gemeld: lekkage in de badkamer, schimmelvorming in de slaapkamer van haar kind en een defecte mechanische ventilatie. De verhuurder heeft de melding geregistreerd onder reparatienummer REP-2026-4410. De Huurcommissie heeft een afzonderlijk dossier geopend onder referentie HC-2026-77881. In correspondentie wordt ook verwezen naar klantnummer VGN-99012.

De minderjarige dochter van gedaagde, Lina Verhoeven, heeft gezondheidsklachten ontwikkeld. Gedaagde wil dat de term minderjarige en de juridische context behouden blijven, maar dat de naam van het kind, het woonadres, telefoonnummers, e-mailadressen en dossiernummers worden verwijderd. Hetzelfde geldt voor de naam van de huisarts, dr. Amal Said, BIG-nummer 10987654321.

Gedaagde verzoekt de kantonrechter de vordering tot ontbinding af te wijzen, althans eiser eerst in de gelegenheid te stellen de gebreken te herstellen en een huurprijsvermindering vast te stellen vanaf 10-01-2026. Subsidiair verzoekt gedaagde om een betalingsregeling van EUR 150,00 per maand. De zitting staat gepland op 18-09-2026 om 10.30 uur.

Dit document is synthetisch en bedoeld om te testen of rolnummers, huurdossiers, klantnummers, adressen, minderjarigen, artsen en BIG-nummers correct maar contextbehoudend worden gemaskeerd.
""",
        "should_contain": [
            "NL_ROLNUMMER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_PHONE_NUMBER",
            "NL_IBAN",
            "NL_COURT_OR_AUTHORITY",
            "NL_BIG_NUMBER",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Bestuursrecht - lang beroepschrift gemeente en besluitnummer",
        "text": """RECHTBANK GELDERLAND
Afdeling bestuursrecht

Zaaknummer: ARN 26/4412
Besluitnummer gemeente: GEM-2026-88901
Dossiernummer: BEST-2026-01170
Cliëntnummer: CL-BEST-4402
Betreft: beroepschrift tegen besluit college van burgemeester en wethouders

Edelachtbare rechtbank,

Namens eiseres Marieke van Dalen, wonende aan Bezwaarstraat 9, 6811 AA Arnhem, stel ik beroep in tegen het besluit van het college van burgemeester en wethouders van de gemeente Arnhem van 22-04-2026. Het besluit is verzonden aan eiseres onder kenmerk GEM-2026-88901 en betreft de afwijzing van een aanvraag om bijzondere bijstand. Eiseres is bereikbaar via 026 3456789 en marieke.vandalen@example.nl.

Het primaire besluit dateert van 12-02-2026. Het bezwaarschrift is ingediend op 20-02-2026. Bij beslissing op bezwaar van 22-04-2026 is het bezwaar ongegrond verklaard. Deze data zijn normale procesdata en moeten niet als BSN worden gelezen. In het gemeentelijke systeem wordt eiseres aangeduid met klantnummer SOC-2026-77812. In de correspondentie van de gemeente staat ook registratienummer ZAAK-0044556677.

Eiseres stelt dat het college de hardheidsclausule ten onrechte niet heeft toegepast. Zij heeft hoge zorgkosten, een tijdelijke betalingsachterstand en een beperkte draagkracht. De bijlagen bevatten bankafschriften, medische informatie en correspondentie met schuldhulpverlening. Voor openbaar of extern gebruik moeten de naam van eiseres, adresgegevens, telefoonnummers, e-mailadressen, klantnummers, besluitnummers, zaaknummers en medische referenties worden gescrubd. Termen als eiseres, college, besluit, bezwaar en beroep moeten behouden blijven.

In het dossier is verder correspondentie opgenomen met schuldhulpverlener Tom Bakker van Stichting BudgetHulp, bereikbaar via tom.bakker@example.nl. Ook is er een brief van huisarts dr. Sophie Meurs, BIG-nummer 10293847561, waarin staat dat eiseres onder behandeling is. De inhoud van die brief wordt niet integraal overgenomen. Alleen de relevante procescontext wordt vermeld.

Eiseres verzoekt de rechtbank het bestreden besluit te vernietigen, het college op te dragen een nieuw besluit te nemen en het college te veroordelen in de proceskosten. Voor zover de rechtbank zelf in de zaak kan voorzien, verzoekt eiseres om toekenning van bijzondere bijstand voor de opgevoerde kosten.
""",
        "should_contain": [
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_PHONE_NUMBER",
            "NL_BIG_NUMBER",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Vreemdelingenrecht - lang beroep verblijfsvergunning",
        "text": """RECHTBANK DEN HAAG
Zittingsplaats Haarlem
Afdeling vreemdelingenzaken

Zaaknummer: NL26.12345
V-nummer: V-8877665544
IND-kenmerk: IND-2026-554433
Dossiernummer advocaat: VREEMD-2026-00654
Cliëntnummer: CL-VR-6612

BEROEPSCHRIFT

Namens eiser Rami Al Nouri, geboren op 04-04-1991 en verblijvende aan Opvanglaan 3, 2132 AB Hoofddorp, stel ik beroep in tegen het besluit van de Immigratie- en Naturalisatiedienst van 19-05-2026. Eiser wordt bijgestaan door mr. Joris de Vries. Het telefoonnummer van eiser is +31 6 66554433 en zijn e-mailadres is rami.alnouri@example.nl.

De IND heeft de aanvraag om verlenging van de verblijfsvergunning afgewezen. Volgens verweerder zou eiser onvoldoende hebben aangetoond dat hij aan het middelenvereiste voldoet. Eiser betwist dat. Hij werkt sinds 01-01-2026 bij Logistiek Centrum West B.V. en ontvangt maandelijks loon op IBAN NL02 RABO 0123 4567 89. Zijn personeelsnummer is LCW-2026-3341. De arbeidsovereenkomst is als bijlage overgelegd.

Eiser voert aan dat de IND onvoldoende rekening heeft gehouden met zijn gezinssituatie. Zijn partner, Laila Haddad, woont met hun minderjarige dochter Noor Al Nouri op hetzelfde opvangadres. De minderjarige is geboren op 11-11-2019. Deze geboortedatum moet als datum worden behandeld, niet als BSN of telefoonnummer. Het belang van het kind is relevant, maar de namen van partner en minderjarige moeten worden gemaskeerd bij extern gebruik.

In het dossier staan medische stukken van huisarts dr. Marit Vos, BIG-nummer 11223344556, en correspondentie van VluchtelingenWerk met referentie VWN-HLM-2026-1188. Verder bevat het dossier een brief van de gemeente Haarlemmermeer met zaaknummer GEM-HLM-2026-2210. Al deze identificerende nummers kunnen in samenhang met de procedure herleidbaar zijn.

Eiser verzoekt de rechtbank het beroep gegrond te verklaren, het bestreden besluit te vernietigen en verweerder op te dragen een nieuw besluit te nemen. Daarnaast verzoekt eiser om vergoeding van proceskosten en om te bepalen dat hij de beslissing op bezwaar in Nederland mag afwachten.
""",
        "should_contain": [
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_PHONE_NUMBER",
            "NL_DATE_OF_BIRTH",
            "NL_BIG_NUMBER",
            "NL_IBAN",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Ondernemingsrecht - enquêteverzoek aandeelhoudersgeschil",
        "text": """GERECHTSHOF AMSTERDAM
Ondernemingskamer

Zaaknummer: 200.345.678/01 OK
Dossiernummer: OND-2026-00888
Cliëntnummer: CL-OND-2901
KvK-nummer vennootschap: 76543210
BTW-nummer: NL123456789B01

VERZOEKSCHRIFT TOT HET BEVELEN VAN EEN ONDERZOEK

Verzoekers zijn Holding Van Rijn B.V., gevestigd aan Handelsplein 10, 1077 XX Amsterdam, en mevrouw Elise van Rijn, wonende aan Notarissenlaan 27, 2012 AB Haarlem. Zij worden bijgestaan door mr. Maarten de Boer. Verweerder is de vennootschap TechNova Zorgsystemen B.V., statutair gevestigd te Utrecht en kantoorhoudende aan Innovatieweg 88, 3584 BA Utrecht. De bestuurder van verweerder is de heer Koen Smit, bereikbaar via koen.smit@example.nl.

Verzoekers houden gezamenlijk 42 procent van de aandelen in TechNova Zorgsystemen B.V. Zij stellen dat sprake is van gegronde redenen om te twijfelen aan een juist beleid en juiste gang van zaken. In het bijzonder verwijzen zij naar de verkoop van een softwarelicentie aan CareBridge N.V. onder contractnummer CNTR-2026-9981 en naar een leningsovereenkomst met referentie LOAN-2026-5512. De bankrekening van de vennootschap is NL91 ABNA 0417 1643 00.

In de aandeelhoudersovereenkomst van 15-01-2024 is bepaald dat besluiten boven EUR 100.000,00 voorafgaande goedkeuring van de algemene vergadering vereisen. Verzoekers stellen dat bestuurder Koen Smit zonder die goedkeuring verplichtingen is aangegaan. De e-mailwisseling van 03-03-2026 tot en met 07-03-2026, waarin onder meer medewerker Niels Vermeer wordt genoemd, ondersteunt volgens verzoekers hun standpunt.

Verzoekers verzoeken de Ondernemingskamer een onderzoek te bevelen, een tijdelijk bestuurder te benoemen en verweerder te verbieden uitvoering te geven aan de betwiste transactie totdat duidelijkheid bestaat over de financiële positie. Voor gebruik buiten deze procedure moeten namen van natuurlijke personen, adressen, e-mailadressen, KvK-nummer, btw-nummer, contractnummers, leningnummers, zaaknummer, dossiernummer en cliëntnummer worden gemaskeerd. Begrippen als verzoekers, verweerder, bestuurder, aandeelhoudersovereenkomst en Ondernemingskamer moeten zichtbaar blijven.
""",
        "should_contain": [
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_KVK",
            "NL_VAT",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
            "NL_IBAN",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "False positives - lange controletekst datums bedragen en artikelen",
        "text": """CONTROLEDOCUMENT VOOR FALSE POSITIVES

Dit synthetische document bevat bewust veel getallen, datums en juridische verwijzingen die niet automatisch als BSN, telefoonnummer, postcode of persoonsgegeven moeten worden gezien. Het doel is om te controleren of het profiel Dutch Legal Strict niet te agressief maskeert.

Artikel 7:669 lid 3 sub e BW, artikel 6:162 BW, artikel 8 EVRM, artikel 1:253a BW en artikel 287 Sv zijn juridische bepalingen. De getallen 7:669, 6:162, 8, 1:253a en 287 zijn geen telefoonnummers, BSN's of dossiernummers. Het bedrag EUR 12.500,00 is een geldbedrag. De bedragen EUR 150,00, EUR 2.500,00 en EUR 100.000,00 zijn ook bedragen.

De data 01-01-2026, 12-05-1980, 03-09-2015, 15-12-2025, 20-11-2026 en 06-06-2026 zijn datums. Zij mogen niet worden omgezet naar NL_BSN. De tijdstippen 10.30 uur, 17.00 uur en 18.00 uur zijn tijdstippen en geen telefoonnummers. De tekst 'zaak 26' zonder concreet nummer is geen zaaknummer. De tekst 'processtuk 3' is geen proces-verbaalnummer.

Wel moet het volgende worden herkend: rolnummer CV EXPL 26-9921, zaaknummer C/13/701234 / FA RK 26-321, parketnummer 13/123456-26, ECLI:NL:RBAMS:2026:1234, dossiernummer TEST-2026-9911, cliëntnummer CL-TEST-7771, telefoonnummer 06 12345678, e-mailadres testpersoon@example.nl en adres Teststraat 12, 1234 AB Teststad.

De persoon Test Persoon treedt op als eiser en de persoon Voorbeeld Gedaagde treedt op als gedaagde. De minderjarige Klein Voorbeeld wordt alleen gebruikt om te testen of het woord minderjarige behouden blijft terwijl de naam wordt gemaskeerd. De termen eiser, gedaagde, minderjarige, slachtoffer, verdachte, verzoeker en verweerder moeten in beginsel leesbaar blijven omdat zij de juridische context dragen.
""",
        "should_contain": [
            "NL_ROLNUMMER",
            "NL_LEGAL_CASE_NUMBER",
            "NL_PARKETNUMMER",
            "NL_ECLI",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_PHONE_NUMBER",
            "NL_ADDRESS",
            "NL_LEGAL_PARTY_NAME",
        ],
        "should_not_contain": ["NL_BSN"],
    },
]


def get_example_names() -> List[str]:
    return [str(case["name"]) for case in TEST_CASES]


def get_example_text(name: str) -> str:
    for case in TEST_CASES:
        if case["name"] == name:
            return str(case["text"])
    return ""
