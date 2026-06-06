"""Dutch legal reference taxonomy for SolidPrivacy Scrub.

This file centralises context words for Dutch legal/administrative reference
numbers. The recognizer keeps the context word readable and masks only the
reference value next to it.

Examples:
- "Cliëntnummer: CL-FAM-55201" -> "Cliëntnummer: <NL_CLIENT_REFERENCE>"
- "schoolreferentie HRZ-SAM-2026-04" -> "schoolreferentie <NL_SCHOOL_REFERENCE>"
- "factuur met nummer FACT-2026-4481" -> "factuur met nummer <NL_INVOICE_NUMBER>"

All entries are local, deterministic and offline-compatible. They are intended
for Dutch Legal Strict mode and should be conservative: context is required.

V8 adds vehicle/object reference categories and a separate candidate-review
strategy. Auto-masking stays conservative; suspicious leftovers can be shown in
the UI as review candidates instead of silently remaining invisible.
"""

from __future__ import annotations

from typing import Dict, List, TypedDict


class ReferenceCategory(TypedDict):
    entity_type: str
    placeholder: str
    domain: str
    score: float
    keywords: List[str]
    examples: List[str]


LEGAL_REFERENCE_CATEGORIES: List[ReferenceCategory] = [
    {
        "entity_type": "NL_DOSSIER_NUMBER",
        "placeholder": "DOSSIERNUMMER",
        "domain": "general_legal",
        "score": 0.88,
        "keywords": [
            "dossiernummer",
            "dossiernr",
            "dossier nr",
            "ons dossier",
            "uw dossier",
            "kantoordossier",
            "procesdossier",
            "zaakdossier",
            "advocaatdossier",
        ],
        "examples": ["DOSS/2026/1189", "FAM-2026-88721", "ARB-2026-00421"],
    },
    {
        "entity_type": "NL_CLIENT_REFERENCE",
        "placeholder": "CLIENT_REFERENTIE",
        "domain": "general_legal",
        "score": 0.90,
        "keywords": [
            "cliëntnummer",
            "clientnummer",
            "cliëntnr",
            "clientnr",
            "klantnummer",
            "klantnr",
            "interne klantreferentie",
            "interne cliëntreferentie",
            "interne clientreferentie",
            "relatienummer",
            "debiteurnummer",
            "crediteurnummer",
        ],
        "examples": ["CL-FAM-55201", "WR-KLANT-2026-7712", "REL-2026-8810"],
    },
    {
        "entity_type": "NL_CASE_REFERENCE",
        "placeholder": "ZAAKREFERENTIE",
        "domain": "court_or_matter",
        "score": 0.88,
        "keywords": [
            "zaakreferentie",
            "zaakcode",
            "procesreferentie",
            "procedurekenmerk",
            "procedurereferentie",
            "matter number",
            "case reference",
            "file number",
        ],
        "examples": ["ZK-WOON-55091", "PROC-2026-4418"],
    },
    {
        "entity_type": "NL_INTERNAL_REFERENCE",
        "placeholder": "INTERNE_REFERENTIE",
        "domain": "general_legal",
        "score": 0.82,
        "keywords": [
            "interne referentie",
            "kantoorreferentie",
            "ons kenmerk",
            "uw kenmerk",
            "kenmerk advocaat",
            "kenmerk kantoor",
            "documentreferentie",
            "documentkenmerk",
        ],
        "examples": ["INT-2026-1182", "DOC-FAM-2026-04"],
    },
    {
        "entity_type": "NL_CONTEXTUAL_REFERENCE",
        "placeholder": "REFERENTIE",
        "domain": "generic_contextual",
        "score": 0.74,
        "keywords": [
            "referentie",
            "kenmerk",
            "registratienummer",
            "referentienummer",
            "referentienr",
        ],
        "examples": ["HRZ-SAM-2026-04", "REF-2026-4431"],
    },
    {
        "entity_type": "NL_INVOICE_NUMBER",
        "placeholder": "FACTUURNUMMER",
        "domain": "finance_admin",
        "score": 0.87,
        "keywords": [
            "factuurnummer",
            "factuur met nummer",
            "factuur nummer",
            "factuurnr",
            "declaratienummer",
            "declaratienr",
            "betalingskenmerk",
            "betaalkenmerk",
            "transactienummer",
            "boekingsnummer",
        ],
        "examples": ["FACT-2026-4481", "DECL-2026-1104"],
    },
    {
        "entity_type": "NL_ORDER_OR_CONTRACT_NUMBER",
        "placeholder": "CONTRACT_OF_ORDERNUMMER",
        "domain": "commercial_admin",
        "score": 0.84,
        "keywords": [
            "contractnummer",
            "contractnr",
            "overeenkomstnummer",
            "ordernummer",
            "offertenummer",
            "opdrachtnummer",
            "leningsovereenkomst",
            "leningnummer",
            "licentienummer",
        ],
        "examples": ["CNTR-2026-9981", "LOAN-2026-5512", "ORD-2026-3312"],
    },
    {
        "entity_type": "NL_SCHOOL_REFERENCE",
        "placeholder": "SCHOOLREFERENTIE",
        "domain": "family_youth_school",
        "score": 0.86,
        "keywords": [
            "schoolreferentie",
            "schoolkenmerk",
            "leerlingnummer",
            "onderwijsnummer",
            "intern begeleider referentie",
            "ib-referentie",
        ],
        "examples": ["HRZ-SAM-2026-04", "SCH-2026-7741"],
    },
    {
        "entity_type": "NL_CHILD_PROTECTION_REFERENCE",
        "placeholder": "JEUGD_OF_BESCHERMINGSREFERENTIE",
        "domain": "family_youth",
        "score": 0.87,
        "keywords": [
            "veilig thuis-melding",
            "vt-melding",
            "veilig thuis referentie",
            "ots-nummer",
            "uithuisplaatsingskenmerk",
            "jeugdbeschermingsreferentie",
            "jeugdzorgreferentie",
            "rvdk-kenmerk",
            "raad voor de kinderbescherming kenmerk",
            "gezagsregisterreferentie",
        ],
        "examples": ["VT-2026-44918", "RVDK-2026-01772", "OTS-2026-1188"],
    },
    {
        "entity_type": "NL_EMPLOYMENT_REFERENCE",
        "placeholder": "ARBEIDSREFERENTIE",
        "domain": "employment_law",
        "score": 0.86,
        "keywords": [
            "personeelsnummer",
            "werknemersnummer",
            "loonnummer",
            "hr-referentie",
            "verzuimnummer",
            "uwv-zaaknummer",
            "wia-nummer",
            "ziektewet-referentie",
            "arbodienstreferentie",
            "re-integratiedossier",
        ],
        "examples": ["HR-2026-7731", "UWV-WIA-2026-11902", "ARB-2026-00421"],
    },
    {
        "entity_type": "NL_INSURANCE_REFERENCE",
        "placeholder": "VERZEKERINGSREFERENTIE",
        "domain": "insurance_injury",
        "score": 0.86,
        "keywords": [
            "polisnummer",
            "polisnr",
            "schadenummer",
            "schadenr",
            "claimnummer",
            "claimnr",
            "letselschadenummer",
            "verzekeringsreferentie",
            "aansprakelijkheidsreferentie",
        ],
        "examples": ["POL-44556677", "LS-2026-009812", "CLAIM-2026-7781"],
    },
    {
        "entity_type": "NL_HEALTHCARE_REFERENCE",
        "placeholder": "ZORGREFERENTIE",
        "domain": "medical_injury",
        "score": 0.86,
        "keywords": [
            "patiëntnummer",
            "patientnummer",
            "medisch dossiernummer",
            "behandelnummer",
            "verwijsnummer",
            "zorgverzekeringsnummer",
            "dbc-code",
            "zorgreferentie",
        ],
        "examples": ["PAT-2026-1148", "MD-2026-4412", "DBC-2026-7711"],
    },
    {
        "entity_type": "NL_POLICE_REFERENCE",
        "placeholder": "POLITIE_OF_OM_REFERENTIE",
        "domain": "criminal_law",
        "score": 0.87,
        "keywords": [
            "proces-verbaalnummer",
            "proces-verbaal nr",
            "pv-nummer",
            "pv nummer",
            "aangiftenummer",
            "incidentnummer",
            "mutatienummer",
            "politieregistratienummer",
            "bvh-nummer",
            "detentienummer",
            "reclasseringsnummer",
        ],
        "examples": ["PL1700-20260518-334455", "PV-AMS-2026-77812", "INC-WM-559812"],
    },
    {
        "entity_type": "NL_IMMIGRATION_REFERENCE",
        "placeholder": "VREEMDELINGENREFERENTIE",
        "domain": "immigration_law",
        "score": 0.87,
        "keywords": [
            "ind-nummer",
            "ind nummer",
            "v-nummer",
            "v nummer",
            "aanvraagnummer ind",
            "verblijfsvergunningnummer",
            "vreemdelingennummer",
        ],
        "examples": ["IND-2026-44129", "V-1234567890"],
    },
    {
        "entity_type": "NL_MUNICIPAL_REFERENCE",
        "placeholder": "BESTUURSREFERENTIE",
        "domain": "administrative_law",
        "score": 0.85,
        "keywords": [
            "besluitnummer",
            "beschikkingsnummer",
            "aanvraagnummer",
            "vergunningnummer",
            "gemeentelijk kenmerk",
            "collegekenmerk",
            "bezwaarnummer",
            "beroepsnummer",
            "subsidienummer",
        ],
        "examples": ["BESL-2026-9912", "GEM-AMS-2026-1148", "SUB-2026-8821"],
    },
    {
        "entity_type": "NL_REAL_ESTATE_REFERENCE",
        "placeholder": "VASTGOEDREFERENTIE",
        "domain": "housing_real_estate",
        "score": 0.84,
        "keywords": [
            "huurovereenkomstnummer",
            "huurcontractnummer",
            "contractnummer huur",
            "objectnummer",
            "adrescode",
            "complexnummer",
            "woningnummer",
            "huurdersnummer",
            "servicekostenreferentie",
            "vve-nummer",
            "kadasterreferentie",
            "kadastraal nummer",
        ],
        "examples": ["HUUR-2026-8891", "VVE-AMS-2026-04", "OBJ-55091"],
    },
    {
        "entity_type": "NL_VEHICLE_REFERENCE",
        "placeholder": "VOERTUIG_OF_KENTEKENREFERENTIE",
        "domain": "vehicle_traffic_injury",
        "score": 0.84,
        "keywords": [
            "kenteken",
            "kentekennummer",
            "nummerplaat",
            "voertuigkenteken",
            "voertuigidentificatie",
            "voertuigreferentie",
            "chassisnummer",
            "vin",
            "rdw-kenmerk",
            "leaseautonummer",
            "wagenparknummer",
        ],
        "examples": ["XX123X", "12-ABC-3", "VIN-2026-77812"],
    },
    {
        "entity_type": "NL_OBJECT_REFERENCE",
        "placeholder": "OBJECTREFERENTIE",
        "domain": "objects_assets_property",
        "score": 0.82,
        "keywords": [
            "objectreferentie",
            "objectcode",
            "inventarisnummer",
            "assetnummer",
            "serienummer",
            "apparaatnummer",
            "zaakobject",
        ],
        "examples": ["OBJ-WOON-55091", "ASSET-2026-4410"],
    },
]


REFERENCE_ENTITY_TYPES: List[str] = [entry["entity_type"] for entry in LEGAL_REFERENCE_CATEGORIES]

# These generic words are weaker than explicit labels like "cliëntnummer".
# The recognizer lowers confidence for these words unless the value pattern is strong.
WEAK_REFERENCE_KEYWORDS = {
    "referentie",
    "kenmerk",
    "registratienummer",
    "referentienummer",
    "referentienr",
}

# Candidate scanner categories are intentionally not always auto-masked. They
# are used by candidate_scanner.py to surface suspicious unmasked values in the
# review table. The user can then decide whether to include them.
CANDIDATE_ENTITY_TYPES = [
    "NL_SUSPICIOUS_REFERENCE_CANDIDATE",
    "NL_POSSIBLE_LICENSE_PLATE",
]

