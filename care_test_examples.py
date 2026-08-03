"""Fully synthetic Dutch care-document corpus for Zorgfilter v1.

The corpus contains no real people, organizations, identifiers or care records.
Every case separates values that should be replaced, values that should be
reviewed and selected by default, and clinical phrases that must be preserved.
"""

from __future__ import annotations

from typing import Any, Dict, List


TEST_CASES: List[Dict[str, Any]] = [
    {
        "id": "care_daily_nursing_report_v1",
        "name": "VVT - dagelijkse verpleegkundige rapportage",
        "sector": "verpleging_verzorging_thuiszorg",
        "document_type": "dagrapportage",
        "text": """DAGELIJKSE RAPPORTAGE\n
Cliënt: Ahmed El Mansouri\n
Cliëntnummer: CL-ZORG-7712\n
ECD-nummer: ECD-889144\n
Geboortedatum: 14-02-1948\n
Adres: Zorglaan 18, 3511 AB Utrecht\n
Telefoon contactpersoon: 06 12345678\n
Contactpersoon: Fatima El Mansouri\n
Locatie: Stichting Morgenlicht, locatie Parkzicht, kamer 214\n
Rapportagedatum: 12-06-2026\n
Rapporteur: verpleegkundige Omar El Idrissi, BIG-nummer 12345678901\n

Cliënt was vanochtend helder en goed aanspreekbaar. Bloeddruk 123/78 mmHg, pols 72 per minuut en temperatuur 36,8 °C. Cliënt mobiliseert met rollator en had pijnscore 6 bij het opstaan. Na rust daalde de pijnscore naar 3. Metformine 500 mg werd volgens schema toegediend. Geen misselijkheid gemeld. Zorgdoel blijft: zelfstandig transfereren binnen zes weken.\n""",
        "replace": [
            {"value": "Ahmed El Mansouri", "entity_type": "PERSON"},
            {"value": "CL-ZORG-7712", "entity_type": "NL_CARE_CLIENT_NUMBER"},
            {"value": "ECD-889144", "entity_type": "NL_EPD_ECD_NUMBER"},
            {"value": "14-02-1948", "entity_type": "NL_DATE_OF_BIRTH"},
            {"value": "Zorglaan 18, 3511 AB Utrecht", "entity_type": "NL_ADDRESS"},
            {"value": "06 12345678", "entity_type": "NL_PHONE_NUMBER"},
            {"value": "Fatima El Mansouri", "entity_type": "PERSON"},
        ],
        "review_selected": [
            {"value": "Stichting Morgenlicht", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "locatie Parkzicht", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
            {"value": "kamer 214", "entity_type": "NL_ROOM_OR_BED_REFERENCE"},
            {"value": "12-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Omar El Idrissi", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "12345678901", "entity_type": "NL_BIG_NUMBER"},
        ],
        "preserve": [
            "verpleegkundige",
            "Bloeddruk 123/78 mmHg",
            "pols 72 per minuut",
            "temperatuur 36,8 °C",
            "mobiliseert met rollator",
            "pijnscore 6",
            "Metformine 500 mg",
            "zelfstandig transfereren binnen zes weken",
        ],
        "audit_only": [],
        "ambiguity_traps": ["123/78", "72", "36,8", "500 mg", "pijnscore 6"],
    },
    {
        "id": "care_plan_evaluation_v1",
        "name": "Gehandicaptenzorg - zorgplan en evaluatie",
        "sector": "gehandicaptenzorg",
        "document_type": "zorgplan_evaluatie",
        "text": """ZORGPLAN EN EVALUATIE\n
Cliënt: Noor van den Berg\n
Patiëntnummer: PAT-2026-1148\n
Medisch dossiernummer: MD-2026-4412\n
Vertegenwoordiger: mevrouw Elise van den Berg\n
E-mailadres vertegenwoordiger: elise.vandenberg@example.invalid\n
Zorgorganisatie: Zorggroep Kompas, woonlocatie De Linde, appartement 3B\n
Evaluatiedatum: 01-07-2026\n
Persoonlijk begeleider: Sanne de Wit\n

Probleem: cliënt raakt overprikkeld bij onverwachte wijzigingen in het dagprogramma. Diagnose autismespectrumstoornis blijft relevante klinische context. Zorgdoel: cliënt geeft met een pictogram aan wanneer rust nodig is. Actie: begeleider kondigt wijzigingen minimaal vijftien minuten vooraf aan. Evaluatie: het aantal escalaties daalde van vier naar één per week. Allergie: geen bekende medicatieallergieën.\n""",
        "replace": [
            {"value": "Noor van den Berg", "entity_type": "PERSON"},
            {"value": "PAT-2026-1148", "entity_type": "NL_PATIENT_NUMBER"},
            {"value": "MD-2026-4412", "entity_type": "NL_MEDICAL_RECORD_NUMBER"},
            {"value": "Elise van den Berg", "entity_type": "PERSON"},
            {"value": "elise.vandenberg@example.invalid", "entity_type": "EMAIL_ADDRESS"},
        ],
        "review_selected": [
            {"value": "Zorggroep Kompas", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "woonlocatie De Linde", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
            {"value": "appartement 3B", "entity_type": "NL_ROOM_OR_BED_REFERENCE"},
            {"value": "01-07-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Sanne de Wit", "entity_type": "NL_CARE_PROVIDER_NAME"},
        ],
        "preserve": [
            "autismespectrumstoornis",
            "raakt overprikkeld",
            "Zorgdoel",
            "pictogram",
            "vijftien minuten vooraf",
            "vier naar één per week",
            "geen bekende medicatieallergieën",
        ],
        "audit_only": ["diagnose plus kleine woonlocatie en exact evaluatiemoment"],
        "ambiguity_traps": ["vier", "één per week", "3B"],
    },
    {
        "id": "care_nursing_transfer_v1",
        "name": "Ziekenhuis naar wijkverpleging - verpleegkundige overdracht",
        "sector": "ziekenhuis_en_wijkverpleging",
        "document_type": "verpleegkundige_overdracht",
        "text": """VERPLEEGKUNDIGE OVERDRACHT\n
Patiënt: mevrouw Laila Ait Haddou\n
EPD-nummer: EPD-2026-5501\n
BSN: 123456782\n
Geboortedatum: 03-09-1957\n
Woonadres: Herstelstraat 42, 3062 KL Rotterdam\n
Telefoon: 010 2345678\n
Verzendende organisatie: Stedelijk Ziekenhuis Noord, afdeling Neurologie B, bed B-12\n
Ontvangende organisatie: Wijkzorg Rijnmond, team Kralingen\n
Ontslagdatum: 18-06-2026\n
Overdragend verpleegkundige: Karin de Groot\n

Medische context: ischemisch CVA links. Patiënt is alert, heeft lichte rechtszijdige krachtsvermindering en spreekt korte zinnen. Mobiliteit: transfer met één persoon en rollator. Voeding: normaal dieet, dunne vloeistoffen toegestaan. Medicatie: clopidogrel 75 mg eenmaal daags en atorvastatine 40 mg eenmaal daags. Allergisch voor penicilline. Wondzorg is niet van toepassing. Vervolg: fysiotherapie en controle bij neuroloog over zes weken.\n""",
        "replace": [
            {"value": "Laila Ait Haddou", "entity_type": "PERSON"},
            {"value": "EPD-2026-5501", "entity_type": "NL_EPD_ECD_NUMBER"},
            {"value": "123456782", "entity_type": "NL_BSN"},
            {"value": "03-09-1957", "entity_type": "NL_DATE_OF_BIRTH"},
            {"value": "Herstelstraat 42, 3062 KL Rotterdam", "entity_type": "NL_ADDRESS"},
            {"value": "010 2345678", "entity_type": "NL_PHONE_NUMBER"},
        ],
        "review_selected": [
            {"value": "Stedelijk Ziekenhuis Noord", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "afdeling Neurologie B", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
            {"value": "bed B-12", "entity_type": "NL_ROOM_OR_BED_REFERENCE"},
            {"value": "Wijkzorg Rijnmond", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "team Kralingen", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
            {"value": "18-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Karin de Groot", "entity_type": "NL_CARE_PROVIDER_NAME"},
        ],
        "preserve": [
            "ischemisch CVA links",
            "lichte rechtszijdige krachtsvermindering",
            "transfer met één persoon en rollator",
            "clopidogrel 75 mg eenmaal daags",
            "atorvastatine 40 mg eenmaal daags",
            "Allergisch voor penicilline",
            "fysiotherapie",
        ],
        "audit_only": [],
        "ambiguity_traps": ["75 mg", "40 mg", "zes weken", "B-12"],
    },
    {
        "id": "care_discharge_letter_v1",
        "name": "Medisch-specialistische ontslagbrief",
        "sector": "medisch_specialistische_zorg",
        "document_type": "ontslagbrief",
        "text": """ONTSLAGBRIEF INTERNE GENEESKUNDE\n
Patiënt: Peter van Leeuwen\n
Patiëntnummer: PAT-2026-7781\n
Verzekerdennummer: VERZ-88441122\n
Opnamedatum: 10-06-2026\n
Ontslagdatum: 14-06-2026\n
Huisarts: dr. Miriam Vos, AGB-code 01020304\n
Behandelend internist: dr. Jeroen de Bruin, BIG-nummer 10987654321\n
Ziekenhuis: Medisch Centrum Rivierenland, afdeling Interne Geneeskunde\n

Reden opname: dehydratie bij gastro-enteritis. Hoofddiagnose: acute nierinsufficiëntie, volledig hersteld na intraveneuze vochttoediening. Bij ontslag creatinine 88 µmol/L en natrium 139 mmol/L. Medicatie bij ontslag: amlodipine 5 mg eenmaal daags. Advies: voldoende drinken en nierfunctiecontrole bij de huisarts binnen één week.\n""",
        "replace": [
            {"value": "Peter van Leeuwen", "entity_type": "PERSON"},
            {"value": "PAT-2026-7781", "entity_type": "NL_PATIENT_NUMBER"},
            {"value": "VERZ-88441122", "entity_type": "NL_HEALTH_INSURANCE_NUMBER"},
        ],
        "review_selected": [
            {"value": "10-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "14-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Miriam Vos", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "01020304", "entity_type": "NL_AGB_CODE"},
            {"value": "Jeroen de Bruin", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "10987654321", "entity_type": "NL_BIG_NUMBER"},
            {"value": "Medisch Centrum Rivierenland", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "afdeling Interne Geneeskunde", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
        ],
        "preserve": [
            "dehydratie bij gastro-enteritis",
            "acute nierinsufficiëntie",
            "intraveneuze vochttoediening",
            "creatinine 88 µmol/L",
            "natrium 139 mmol/L",
            "amlodipine 5 mg eenmaal daags",
            "nierfunctiecontrole",
        ],
        "audit_only": ["zeldzame diagnose in combinatie met kleine afdeling en exacte opnameperiode"],
        "ambiguity_traps": ["88 µmol/L", "139 mmol/L", "5 mg", "één week"],
    },
    {
        "id": "care_gp_referral_v1",
        "name": "Huisartsverwijzing cardiologie",
        "sector": "huisartsenzorg",
        "document_type": "verwijsbrief",
        "text": """VERWIJSBRIEF CARDIOLOGIE\n
Patiënt: Samira Benali\n
Geboortedatum: 22-11-1966\n
BSN: 123456782\n
Verwijsnummer: VERW-2026-7711\n
Behandelnummer: BEH-2026-1188\n
Huisarts: dr. Thomas Mulder, praktijk De Stadspoort, AGB-code 87654321\n
E-mail patiënt: samira.benali@example.invalid\n

Vraagstelling: beoordeling van inspanningsgebonden thoracale druk. Voorgeschiedenis: hypertensie en diabetes mellitus type 2. Medicatie: metformine 500 mg tweemaal daags en lisinopril 10 mg eenmaal daags. Bloeddruk op het spreekuur 148/86 mmHg. Geen bekende geneesmiddelenallergieën. Graag beoordeling en behandeladvies.\n""",
        "replace": [
            {"value": "Samira Benali", "entity_type": "PERSON"},
            {"value": "22-11-1966", "entity_type": "NL_DATE_OF_BIRTH"},
            {"value": "123456782", "entity_type": "NL_BSN"},
            {"value": "VERW-2026-7711", "entity_type": "NL_REFERRAL_NUMBER"},
            {"value": "BEH-2026-1188", "entity_type": "NL_TREATMENT_REFERENCE"},
            {"value": "samira.benali@example.invalid", "entity_type": "EMAIL_ADDRESS"},
        ],
        "review_selected": [
            {"value": "Thomas Mulder", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "praktijk De Stadspoort", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "87654321", "entity_type": "NL_AGB_CODE"},
        ],
        "preserve": [
            "inspanningsgebonden thoracale druk",
            "hypertensie",
            "diabetes mellitus type 2",
            "metformine 500 mg tweemaal daags",
            "lisinopril 10 mg eenmaal daags",
            "148/86 mmHg",
            "Geen bekende geneesmiddelenallergieën",
        ],
        "audit_only": [],
        "ambiguity_traps": ["148/86", "500 mg", "10 mg", "type 2"],
    },
    {
        "id": "care_medication_overview_v1",
        "name": "Apotheek - medicatieoverzicht",
        "sector": "farmaceutische_zorg",
        "document_type": "medicatieoverzicht",
        "text": """ACTUEEL MEDICATIEOVERZICHT\n
Patiënt: Willem de Jong\n
Patiëntnummer: PAT-2026-3321\n
Geboortedatum: 09-04-1952\n
Apotheek: Apotheek Waterlinie, AGB-code 11223344\n
Voorschrijver: huisarts dr. Eva Smit, BIG-nummer 11223344556\n
Receptnummer: BEH-2026-2244\n

1. Metoprolol 50 mg, eenmaal daags om 08:00 uur.\n
2. Apixaban 5 mg, tweemaal daags om 08:00 en 20:00 uur.\n
3. Omeprazol 20 mg, eenmaal daags voor het ontbijt.\n
Allergie: naproxen veroorzaakt urticaria.\n""",
        "replace": [
            {"value": "Willem de Jong", "entity_type": "PERSON"},
            {"value": "PAT-2026-3321", "entity_type": "NL_PATIENT_NUMBER"},
            {"value": "09-04-1952", "entity_type": "NL_DATE_OF_BIRTH"},
            {"value": "BEH-2026-2244", "entity_type": "NL_TREATMENT_REFERENCE"},
        ],
        "review_selected": [
            {"value": "Apotheek Waterlinie", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "11223344", "entity_type": "NL_AGB_CODE"},
            {"value": "Eva Smit", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "11223344556", "entity_type": "NL_BIG_NUMBER"},
        ],
        "preserve": [
            "Metoprolol 50 mg",
            "eenmaal daags om 08:00 uur",
            "Apixaban 5 mg",
            "tweemaal daags om 08:00 en 20:00 uur",
            "Omeprazol 20 mg",
            "naproxen veroorzaakt urticaria",
        ],
        "audit_only": [],
        "ambiguity_traps": ["50 mg", "5 mg", "20 mg", "08:00", "20:00"],
    },
    {
        "id": "care_laboratory_report_v1",
        "name": "Laboratorium - klinisch chemisch rapport",
        "sector": "laboratoriumzorg",
        "document_type": "laboratoriumrapport",
        "text": """KLINISCH CHEMISCH RAPPORT\n
Patiënt: Daan Vermeer\n
Medisch dossiernummer: MD-2026-7744\n
Monsternummer: LAB-2026-4412\n
Afnamedatum: 20-06-2026\n
Aanvrager: dr. Nadia Bos\n
Laboratorium: Diagnostiek Centrum Delta\n

Hemoglobine: 7,8 mmol/L (referentie 8,5-11,0).\n
Leukocyten: 6,2 x10^9/L (referentie 4,0-10,0).\n
CRP: 4 mg/L (referentie kleiner dan 5).\n
Glucose: 4,4 mmol/L.\n
Conclusie: licht verlaagd hemoglobine, overige waarden zonder bijzonderheden.\n""",
        "replace": [
            {"value": "Daan Vermeer", "entity_type": "PERSON"},
            {"value": "MD-2026-7744", "entity_type": "NL_MEDICAL_RECORD_NUMBER"},
            {"value": "LAB-2026-4412", "entity_type": "NL_LAB_SAMPLE_NUMBER"},
        ],
        "review_selected": [
            {"value": "20-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Nadia Bos", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "Diagnostiek Centrum Delta", "entity_type": "NL_CARE_ORGANIZATION"},
        ],
        "preserve": [
            "Hemoglobine: 7,8 mmol/L",
            "referentie 8,5-11,0",
            "Leukocyten: 6,2 x10^9/L",
            "CRP: 4 mg/L",
            "Glucose: 4,4 mmol/L",
            "licht verlaagd hemoglobine",
        ],
        "audit_only": [],
        "ambiguity_traps": ["7,8", "8,5-11,0", "6,2", "4 mg/L", "4,4"],
    },
    {
        "id": "care_incident_report_v1",
        "name": "VVT - MIC medicatie-incident",
        "sector": "verpleging_verzorging_thuiszorg",
        "document_type": "mic_mim_vim_rapport",
        "text": """MIC-MELDING MEDICATIE-INCIDENT\n
Cliënt: mevrouw Johanna Peters\n
Cliëntnummer: CL-ZORG-9901\n
Incidentnummer: MIC-2026-0912\n
Locatie: woonzorgcentrum De Brug, afdeling Waterkant, kamer 18\n
Incidentdatum: 21-06-2026 om 20:15 uur\n
Melder: verzorgende IG Youssef Amrani\n
Betrokken arts: dr. Lotte Kramer\n
Contactpersoon familie: Mark Peters, telefoon 06 87654321\n

Omschrijving: de avonddosering apixaban 5 mg is om 20:00 uur niet toegediend. De omissie werd om 20:15 uur ontdekt. De arts beoordeelde dat geen inhaaldosis nodig was. Cliënt had geen klachten en de vitale parameters waren stabiel. Maatregel: dubbele controle van de medicatielijst bij de avonddienst.\n""",
        "replace": [
            {"value": "Johanna Peters", "entity_type": "PERSON"},
            {"value": "CL-ZORG-9901", "entity_type": "NL_CARE_CLIENT_NUMBER"},
            {"value": "MIC-2026-0912", "entity_type": "NL_CARE_INCIDENT_NUMBER"},
            {"value": "Mark Peters", "entity_type": "PERSON"},
            {"value": "06 87654321", "entity_type": "NL_PHONE_NUMBER"},
        ],
        "review_selected": [
            {"value": "woonzorgcentrum De Brug", "entity_type": "NL_CARE_ORGANIZATION"},
            {"value": "afdeling Waterkant", "entity_type": "NL_CARE_LOCATION_REFERENCE"},
            {"value": "kamer 18", "entity_type": "NL_ROOM_OR_BED_REFERENCE"},
            {"value": "21-06-2026", "entity_type": "NL_CARE_EVENT_DATE"},
            {"value": "Youssef Amrani", "entity_type": "NL_CARE_PROVIDER_NAME"},
            {"value": "Lotte Kramer", "entity_type": "NL_CARE_PROVIDER_NAME"},
        ],
        "preserve": [
            "verzorgende IG",
            "apixaban 5 mg",
            "20:00 uur niet toegediend",
            "geen inhaaldosis nodig",
            "geen klachten",
            "vitale parameters waren stabiel",
            "dubbele controle van de medicatielijst",
        ],
        "audit_only": ["kleine woonlocatie plus exact incidentmoment en zeldzame gebeurtenis"],
        "ambiguity_traps": ["5 mg", "20:00", "20:15", "kamer 18"],
    },
]


def get_case(case_id: str) -> Dict[str, Any]:
    """Return one synthetic case by stable ID."""

    for case in TEST_CASES:
        if case["id"] == case_id:
            return case
    raise KeyError(case_id)


def all_expected_values(case: Dict[str, Any]) -> List[str]:
    """Return all exact replace/review values from one case."""

    values: List[str] = []
    for bucket in ("replace", "review_selected"):
        values.extend(str(item["value"]) for item in case.get(bucket, []))
    return values
