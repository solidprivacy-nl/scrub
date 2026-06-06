"""Fake Dutch legal test examples for SolidPrivacy Scrub.

These examples are synthetic and should be safe to use in a public demo.
They are meant for quick manual validation of the Dutch Legal Strict profile.
"""

from __future__ import annotations

from typing import Dict, List


TEST_CASES: List[Dict[str, object]] = [
    {
        "name": "Arbeidsrecht - ontslag en dossiernummer",
        "text": """Geachte mr. De Vries,

Namens cliënt Jan Jansen, wonende aan Keizersgracht 123, 1015 CJ Amsterdam, reageer ik op het ontslag op staande voet.
Het dossiernummer is ARB-2026-00421 en het cliëntnummer is CL-88421.
Werkgever BrightCare B.V. is gevestigd aan Zorglaan 7, 3521 AB Utrecht.
Het telefoonnummer van cliënt is 06 12345678 en zijn e-mail is jan.jansen@example.nl.
De geboortedatum van cliënt is 12-05-1980. Dit is géén BSN: 12-05-1980.
""",
        "should_contain": [
            "NL_ADDRESS",
            "NL_POSTCODE",
            "NL_PHONE_NUMBER",
            "NL_DOSSIER_NUMBER",
            "NL_CLIENT_NUMBER",
            "NL_DATE_OF_BIRTH",
        ],
        "should_not_contain": ["NL_BSN"],
    },
    {
        "name": "Familierecht - verzoekschrift en minderjarige",
        "text": """Aan de Rechtbank Amsterdam

Zaaknummer C/13/701234 / FA RK 26-321
Rekestnummer RK-2026-887

Verzoeker Fatima El Amrani verzoekt wijziging van de omgangsregeling met betrekking tot de minderjarige Sami El Amrani.
Verweerder Peter Bakker woont aan Laan van Meerdervoort 55, 2517 AM Den Haag.
""",
        "should_contain": [
            "NL_COURT_OR_AUTHORITY",
            "NL_LEGAL_CASE_NUMBER",
            "NL_REKESTNUMMER",
            "NL_LEGAL_PARTY_NAME",
            "NL_ADDRESS",
        ],
        "should_not_contain": [],
    },
    {
        "name": "Strafrecht - parketnummer en CJIB",
        "text": """Betreft: strafzaak tegen verdachte Mohamed Ait Said

Parketnummer: 13/123456-26
CJIB-nummer: 9876543210123456
Proces-verbaalnummer: PL1300-20260606-123456

De zitting staat gepland op 20-11-2026. Deze datum mag niet als telefoonnummer of BSN worden gezien.
""",
        "should_contain": [
            "NL_PARKETNUMMER",
            "NL_CJIB_NUMBER",
            "NL_POLICE_REPORT_NUMBER",
            "NL_LEGAL_PARTY_NAME",
        ],
        "should_not_contain": ["NL_BSN", "NL_PHONE_NUMBER"],
    },
    {
        "name": "Civiel - ECLI en rolnummer",
        "text": """In de zaak met rolnummer CV EXPL 26-9921 is gewezen op ECLI:NL:RBAMS:2026:1234.
Eiser Stichting Woonrecht vordert betaling van gedaagde Pieter de Groot.
Het IBAN van de wederpartij is NL91 ABNA 0417 1643 00.
""",
        "should_contain": [
            "NL_ROLNUMMER",
            "NL_ECLI",
            "NL_LEGAL_PARTY_NAME",
            "NL_IBAN",
        ],
        "should_not_contain": [],
    },
    {
        "name": "Letselschade - claim en polis",
        "text": """Schadenummer: LS-2026-009812
Polisnummer: POL-44556677

Slachtoffer Emma Smit is behandeld door arts BIG-nummer 12345678901.
Haar telefoonnummer is +31 6 87654321. De datum 15-12-2025 is alleen een datum.
""",
        "should_contain": [
            "NL_INSURANCE_CLAIM_NUMBER",
            "NL_BIG_NUMBER",
            "NL_PHONE_NUMBER",
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
