"""Long-form synthetic narrative additions for the Zorgfilter test corpus.

The additions deliberately contain no digits or new identifying values. They
provide realistic document structure and care context while leaving every
existing replace, review, preserve and audit contract unchanged.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, List, Mapping


LONG_FORM_EXPANSIONS: Mapping[str, str] = {
    "care_daily_nursing_report_v1": """VERLOOP VAN DE DIENST

Bij aanvang van de dienst was de cliënt rustig wakker en georiënteerd in de eigen omgeving. De cliënt kon duidelijk aangeven wat nodig was en werkte mee aan de afgesproken zorgmomenten. Tijdens de ochtend werd geen acute verandering in het bewustzijn, de ademhaling of de algemene indruk gezien. De stemming was overwegend ontspannen, met kortdurende onzekerheid tijdens het opstaan.

PERSOONLIJKE VERZORGING EN MOBILITEIT

De cliënt voerde de verzorging van gezicht en bovenlichaam grotendeels zelfstandig uit. Bij het aankleden was verbale ondersteuning nodig om het tempo te bewaken. De transfer vanuit de stoel verliep gecontroleerd, waarbij de cliënt de afgesproken bewegingen herkende en aanwijzingen opvolgde. Tijdens het lopen bleef de houding stabiel. Na inspanning werd een korte rustpauze aangeboden.

VOEDING, VOCHT EN UITSCHEIDING

Het ontbijt werd volledig gebruikt en drinken werd verspreid aangeboden. Er waren geen aanwijzingen voor slikproblemen, buikklachten of verminderde eetlust. De uitscheiding verliep volgens het gebruikelijke patroon. De cliënt gaf aan zich comfortabel te voelen en kon zelfstandig naar het toilet met begeleiding op afstand.

PSYCHOSOCIAAL EN DAGBESTEDING

De cliënt nam deel aan een rustig contactmoment en sprak over de geplande activiteiten. Een vertrouwde dagstructuur gaf zichtbaar houvast. De cliënt reageerde positief op korte uitleg vooraf en maakte zelf een keuze voor een rustige activiteit.

AANDACHTSPUNTEN VOOR DE VOLGENDE DIENST

Blijf het tempo bij transfers afstemmen op wat de cliënt aankan. Observeer of de pijn opnieuw toeneemt bij mobiliseren en bied tijdig rust aan. Stimuleer eigen regie bij verzorging en drinken. Meld veranderingen in alertheid, mobiliteit, eetlust of algemeen welbevinden in de volgende rapportage.""",
    "care_plan_evaluation_v1": """HUIDIGE SITUATIE

De cliënt functioneert het best wanneer de dag voorspelbaar wordt opgebouwd en veranderingen vooraf worden uitgelegd. Onverwachte overgangsmomenten kunnen leiden tot spanning, terugtrekgedrag of herhaald vragen om bevestiging. In een rustige omgeving lukt het de cliënt meestal om aanwijzingen te begrijpen en een passende keuze te maken.

COMMUNICATIE EN SIGNALERING

Korte zinnen, concrete keuzes en visuele ondersteuning sluiten goed aan. De cliënt gebruikt het afgesproken signaal steeds vaker voordat de spanning te hoog oploopt. Begeleiders herkennen vroege signalen zoals sneller praten, minder oogcontact en herhaald controleren van de planning. Een rustige benadering en beperkte hoeveelheid taal helpen om overzicht terug te krijgen.

DAGSTRUCTUUR EN ZELFSTANDIGHEID

De vaste volgorde van opstaan, verzorging, activiteit en rustmoment biedt houvast. De cliënt kan verschillende onderdelen zelfstandig uitvoeren wanneer het materiaal vooraf klaarstaat. Bij nieuwe of minder vertrouwde taken blijft stapsgewijze ondersteuning nodig. Het team stimuleert keuzevrijheid zonder te veel opties tegelijk aan te bieden.

PARTICIPATIE EN WELBEVINDEN

De cliënt neemt met plezier deel aan kleinschalige activiteiten en zoekt contact met bekende begeleiders. In een drukke groep neemt de belastbaarheid af. Een tijdige pauze voorkomt doorgaans dat spanning verder oploopt. Positieve feedback op concreet gedrag werkt beter dan algemene complimenten.

EVALUATIE EN VERVOLG

De afgesproken aanpak wordt door het team consequent toegepast en lijkt effect te hebben. De komende periode blijft de nadruk liggen op vroeg signaleren, zelf aangeven van rustbehoefte en het voorspelbaar aanbieden van veranderingen. Bij de volgende evaluatie worden zelfstandigheid, herstel na spanning en deelname aan activiteiten opnieuw gezamenlijk beoordeeld.""",
    "care_nursing_transfer_v1": """ALGEMENE TOESTAND BIJ OVERDRACHT

De patiënt is medisch stabiel en begrijpt eenvoudige uitleg over de vervolgzorg. Vermoeidheid neemt toe na langere gesprekken of inspanning. Er zijn geen aanwijzingen voor acute benauwdheid, koorts of nieuwe neurologische uitval. De patiënt kan behoeften kenbaar maken en vraagt zo nodig om ondersteuning.

MOBILITEIT EN VALPREVENTIE

Bij opstaan en gaan zitten is begeleiding nodig om de beweging rustig en veilig uit te voeren. De patiënt gebruikt het loophulpmiddel op de afgesproken manier, maar heeft soms herinnering nodig om niet te snel te draaien. Zorg voor een vrije looproute, passend schoeisel en toezicht bij momenten waarop de patiënt vermoeid is.

PERSOONLIJKE VERZORGING EN DAGELIJKSE ACTIVITEITEN

De patiënt kan het bovenlichaam grotendeels zelfstandig verzorgen. Voor het onderlichaam, aankleden en douchen is gedeeltelijke ondersteuning nodig. Geef voldoende tijd om handelingen zelf uit te voeren en neem alleen over wanneer veiligheid of overbelasting dit vraagt. De patiënt waardeert duidelijke uitleg vóór iedere handeling.

VOEDING, COMMUNICATIE EN MEDICATIE

Eten en drinken verlopen zonder zichtbare problemen. Laat de patiënt rechtop zitten en controleer of het tempo rustig blijft. De spraak is begrijpelijk, maar formuleren kost soms extra tijd. Onderbreek niet onnodig en controleer of informatie goed is begrepen. De medicatie kan volgens het meegegeven schema worden voortgezet.

VERVOLGZORG EN OBSERVATIE

Let op verandering in kracht, spraak, alertheid, slikken, mobiliteit of gedrag. Stimuleer dagelijkse oefening binnen de afgesproken belastbaarheid. Stem fysiotherapeutische oefeningen af met de wijkverpleging en leg bijzonderheden eenduidig vast. Neem bij plotselinge achteruitgang direct contact op volgens de geldende escalatieafspraken.""",
    "care_discharge_letter_v1": """KLINISCH BELOOP

Tijdens de opname verbeterde de algemene conditie geleidelijk na herstel van de vochtbalans. Misselijkheid en diarree namen af en de orale inname kwam weer op gang. De patiënt bleef hemodynamisch stabiel en ontwikkelde geen nieuwe klachten. De nierfunctie herstelde in samenhang met de klinische verbetering.

ONDERZOEK EN INTERPRETATIE

Het lichamelijk onderzoek liet bij ontslag geen tekenen van overvulling of dehydratie zien. De buik was soepel en niet drukpijnlijk. Er waren geen aanwijzingen voor een actieve infectieuze complicatie. De laboratoriumuitslagen pasten bij herstel en gaven geen reden om de opname te verlengen.

BEHANDELING TIJDENS OPNAME

De behandeling bestond uit vochttoediening, bewaking van de nierfunctie en tijdelijke aanpassing van medicatie die de nierbelasting kon beïnvloeden. Na verbetering werd de gebruikelijke orale medicatie opnieuw beoordeeld. De patiënt kreeg uitleg over signalen van uitdroging en het belang van voldoende vochtinname.

CONDITIE BIJ ONTSLAG

De patiënt kan zelfstandig eten, drinken en mobiliseren en voelt zich voldoende hersteld om naar huis te gaan. Er is geen aanvullende thuiszorg aangevraagd. De patiënt en naaste hebben de ontslaginformatie doorgenomen en konden de belangrijkste aandachtspunten in eigen woorden herhalen.

ADVIES EN FOLLOW-UP

Adviseer regelmatige vochtinname, geleidelijke hervatting van dagelijkse activiteiten en contact met de huisarts bij opnieuw afnemende urineproductie, aanhoudend braken, sufheid of snelle achteruitgang. Controle van nierfunctie en medicatie blijft aangewezen. De definitieve vervolgafspraken worden door de huisarts afgestemd op het klinisch herstel.""",
    "care_gp_referral_v1": """ANAMNESE

De patiënt beschrijft een drukkend gevoel op de borst dat vooral ontstaat bij stevig doorlopen en afneemt na rust. De klachten zijn niet continu aanwezig en gaan niet gepaard met koorts of een duidelijke luchtweginfectie. Er is soms kortademigheid bij inspanning, zonder benauwdheid in rust. De patiënt ervaart onzekerheid over de betekenis van de klachten.

RISICOPROFIEL EN VOORGESCHIEDENIS

De bekende cardiovasculaire risicofactoren worden behandeld. De medicatie wordt naar eigen zeggen consequent gebruikt. Er zijn geen recente episoden met bewustzijnsverlies gemeld. De familieanamnese en leefstijlfactoren zijn besproken en ondersteunen de vraag om nadere cardiale beoordeling.

LICHAMELIJK ONDERZOEK

De patiënt maakte tijdens het consult een niet acuut zieke indruk. Harttonen waren regulair en bij longonderzoek werden geen afwijkende bijgeluiden gehoord. Er was geen zichtbaar perifeer oedeem. De klachten konden in de spreekkamer niet worden opgewekt.

BELEID IN AFWACHTING VAN BEOORDELING

De huidige medicatie wordt voortgezet. De patiënt heeft uitleg gekregen over het beperken van zware inspanning zolang de oorzaak niet duidelijk is. Bij aanhoudende pijn in rust, duidelijke benauwdheid, zweten, misselijkheid of snelle verslechtering moet met spoed medische hulp worden ingeschakeld.

VRAAG AAN DE CARDIOLOOG

Graag beoordeling van de waarschijnlijkheid van cardiale ischemie en advies over aanvullend onderzoek en behandeling. Ook wordt gevraagd mee te wegen of aanpassing van cardiovasculaire risicoreductie nodig is. Terugkoppeling over diagnose, beleid en eventuele beperkingen is gewenst voor verdere begeleiding in de huisartsenpraktijk.""",
    "care_medication_overview_v1": """MEDICATIEVERIFICATIE

Het overzicht is samen met de patiënt doorgenomen. De patiënt herkent de middelen, het gebruiksdoel en de gebruikelijke innamemomenten. Er zijn geen aanwijzingen dat middelen van andere voorschrijvers ontbreken. Zelfzorgmiddelen en incidenteel gebruik zijn nagevraagd en leveren geen aanvullend aandachtspunt op.

GEBRUIK EN THERAPIETROUW

De patiënt gebruikt een weekdoos en koppelt de inname aan vaste momenten in de dag. Een enkele keer wordt een dosis later ingenomen wanneer de dagelijkse routine afwijkt. De patiënt begrijpt dat gemiste doses niet zonder overleg dubbel mogen worden ingenomen. De praktische organisatie van de medicatie wordt als haalbaar ervaren.

WERKING EN BIJWERKINGEN

Er zijn geen nieuwe bloedingen, duizeligheid, maagklachten of andere duidelijke bijwerkingen gemeld. De bekende overgevoeligheidsreactie blijft relevant voor toekomstige voorschriften. De patiënt weet dat onverwachte huidreacties, benauwdheid of zwelling direct moeten worden gemeld.

TOEDIENADVIES

Slik de medicatie in met voldoende water en volg de afgesproken relatie tot maaltijden. Houd de vaste innamemomenten aan en wijzig dosering of stopmoment niet op eigen initiatief. Bij braken, slikproblemen of tijdelijk niet kunnen eten is overleg met apotheek of voorschrijver nodig.

CONTROLEPUNTEN

Bij ieder nieuw voorschrift moet worden gecontroleerd op interacties en dubbele medicatie. Bespreek veranderingen in nierfunctie, gewicht, valneiging of bloedingsklachten tijdig. Neem het actuele overzicht mee naar afspraken en laat wijzigingen door één betrokken zorgverlener verwerken voordat een nieuwe versie wordt gebruikt.""",
    "care_laboratory_report_v1": """MATERIAAL EN KWALITEIT

Het aangeleverde materiaal was geschikt voor analyse. Er waren geen zichtbare aanwijzingen voor stolling, ernstige hemolyse of onvoldoende volume. De technische kwaliteitscontroles voldeden aan de interne acceptatiecriteria. De resultaten kunnen daarom in samenhang met de klinische vraagstelling worden geïnterpreteerd.

SAMENVATTING VAN DE BEVINDINGEN

Het bloedbeeld laat een lichte afwijking zien zonder aanwijzingen voor een acute ontstekingsreactie. De overige gemeten parameters liggen binnen of dicht bij de verwachte bandbreedte. Een geïsoleerde laboratoriumafwijking heeft beperkte betekenis zonder informatie over klachten, voorgeschiedenis en eerder gemeten waarden.

KLINISCHE INTERPRETATIE

De bevinding kan passen bij een milde anemie, maar de oorzaak kan op basis van dit onderzoek niet worden vastgesteld. Denk bij persisterende afwijkingen aan beoordeling van voedingstoestand, ijzerstatus, vitaminevoorziening, chronische ziekte en eventueel bloedverlies. De aanvrager bepaalt welke aanvullende diagnostiek passend is.

ADVIES VOOR VERVOLG

Vergelijk de uitkomst met eerdere metingen en beoordeel het klinische beloop. Herhaling kan zinvol zijn wanneer klachten blijven bestaan of wanneer de afwijking onverwacht is. Aanvullend onderzoek wordt alleen geadviseerd wanneer dit aansluit bij de anamnese en het lichamelijk onderzoek.

OPMERKING

Dit rapport bevat laboratoriuminformatie en vervangt geen medische beoordeling. Referentiegebieden kunnen verschillen door methode en patiëntkenmerken. Bij een onverwachte discrepantie tussen kliniek en uitslag kan overleg met het laboratorium plaatsvinden voordat conclusies aan de uitslag worden verbonden.""",
    "care_incident_report_v1": """DIRECTE GEVOLGEN EN HANDELEN

Na ontdekking van de omissie is de cliënt direct beoordeeld. Er waren geen zichtbare tekenen van acute achteruitgang. De betrokken zorgverleners hebben het geldende medicatieprotocol gevolgd en de medische beoordeling vastgelegd. De cliënt en contactpersoon kregen uitleg over wat was gebeurd en welke observaties nodig bleven.

ANALYSE VAN HET PROCES

De medicatie was op het juiste moment beschikbaar, maar de aftekening in de werkvoorraad gaf onvoldoende duidelijkheid over de uitvoeringsstatus. Tijdens de overdracht lag de aandacht bij meerdere gelijktijdige zorgtaken. Hierdoor werd niet tijdig onderkend dat de toediening nog openstond.

MENSELIJKE EN ORGANISATORISCHE FACTOREN

De medewerker was bevoegd en bekend met de werkwijze. Er was geen sprake van bewust afwijken van het voorschrift. De combinatie van werkdruk, onderbreking en een onduidelijke visuele status vergrootte de kans op een vergissing. Het team bespreekt het incident zonder schuldtoewijzing en richt zich op verbetering van het proces.

VERBETERMAATREGELEN

Bij de start en afronding van de medicatieronde wordt voortaan een korte gezamenlijke controle uitgevoerd. Openstaande toedieningen worden expliciet benoemd bij overdracht. Onderbrekingen tijdens kritieke handelingen worden waar mogelijk beperkt. De werking van deze afspraken wordt tijdens een volgend teamoverleg geëvalueerd.

NAZORG EN LEREN

De cliënt blijft volgens de gebruikelijke afspraken geobserveerd. Eventuele nieuwe klachten worden direct medisch beoordeeld. De melder ontvangt terugkoppeling over de analyse en verbetermaatregelen. Het incident wordt gebruikt als leermoment voor het hele team en niet als individuele beoordelingsmaatstaf.""",
}


def expand_case_texts(cases: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return copied cases with their stable long-form narrative appended."""

    expanded: List[Dict[str, Any]] = []
    seen_ids = set()

    for case in cases:
        copied = deepcopy(case)
        case_id = str(copied.get("id", ""))
        if case_id not in LONG_FORM_EXPANSIONS:
            raise ValueError(f"Missing long-form expansion for care case: {case_id}")

        original_text = str(copied.get("text", "")).rstrip()
        addition = str(LONG_FORM_EXPANSIONS[case_id]).strip()
        copied["text"] = f"{original_text}\n\n{addition}\n"
        expanded.append(copied)
        seen_ids.add(case_id)

    unused = set(LONG_FORM_EXPANSIONS) - seen_ids
    if unused:
        raise ValueError(f"Unused long-form care expansions: {sorted(unused)}")

    return expanded
