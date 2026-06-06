"""Synthetic Dutch legal regression cases for Scrub.

All examples are fake. These cases document the behaviour we want to protect
before adding more recognizers.
"""

CANDIDATE_SCANNER_TEXT = """
De verhuurder heeft de melding geregistreerd onder reparatienummer REP-2026-4410.
De wederpartij verwees naar intern incidentnummer INC-2026-0912.
Het kenteken XX123X staat in het proces-verbaal.
De interne klantreferentie van eiser is WR-KLANT-2026-7712.
Het dossiernummer is DOSS/2026/1189.
Het artikel 7:669 BW mag niet als referentie worden gemaskeerd.
De datum 15-12-2025 is alleen een datum.
Het bedrag EUR 1.250,00 is alleen een bedrag.
"""

EXPECTED_CANDIDATES = {
    "REP-2026-4410",
    "INC-2026-0912",
    "XX123X",
    "WR-KLANT-2026-7712",
    "DOSS/2026/1189",
}

NEGATIVE_VALUES = {
    "7:669",
    "15-12-2025",
    "EUR",
    "1.250",
}

CONTEXT_PRESERVATION_EXAMPLES = [
    {
        "text": "Slachtoffer Emma Smit is behandeld door arts met BIG-nummer 12345678901.",
        "context_words_to_preserve": ["Slachtoffer", "is behandeld door arts met", "BIG-nummer"],
        "sensitive_values": ["Emma Smit", "12345678901"],
    },
    {
        "text": "Verzoeker Fatima El Amrani verzoekt wijziging voor de minderjarige Sami El Amrani.",
        "context_words_to_preserve": ["Verzoeker", "verzoekt wijziging", "minderjarige"],
        "sensitive_values": ["Fatima El Amrani", "Sami El Amrani"],
    },
]

CASE_NUMBER_EXAMPLES = [
    "10598721 / UE VERZ 26-441",
    "ARN 26/4412",
    "NL26.12345",
    "200.345.678/01 OK",
    "C/13/701234 / FA RK 26-321",
]
