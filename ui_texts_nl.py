APP_TITLE = "SolidPrivacy Scrub"
APP_SUBTITLE = "Lokale controle van vertrouwelijke documenten"
APP_VERSION = "v9.1"
APP_INTRO = (
    "Schoon zorgdocumenten, juridische stukken, brieven en professionele notities op "
    "voordat je ze deelt of gebruikt in AI-tools. Scrub zoekt herleidbare gegevens "
    "en laat jou controleren wat wordt vervangen, terwijl professionele en klinische "
    "betekenis zo veel mogelijk leesbaar blijft."
)
LOCAL_PROCESSING_NOTE = (
    "Deze prototypeversie gebruikt herkenningsregels en lokale app-logica. "
    "Gebruik in de publieke omgeving alleen synthetische of goedgekeurde testdocumenten "
    "en controleer het resultaat altijd handmatig."
)
PROFILE_HELP = (
    "Kies het documentprofiel. Zorg en Juridisch voegen eigen terminologie en "
    "patroonherkenning toe; Algemeen Nederlands en Internationaal gebruiken de "
    "bredere basiscontrole."
)
PROFILE_DESCRIPTIONS = {
    "Zorgcontrole — streng": (
        "Extra controle op patiënt- en cliëntnummers, EPD/ECD- en dossiernummers, "
        "verwijzingen, laboratorium- en incidentreferenties, zorgverleners, organisaties, "
        "locaties en exacte zorgdata. Diagnose, medicatie, dosering, laboratoriumwaarden "
        "en observaties blijven zo veel mogelijk leesbaar."
    ),
    "Juridische controle — streng": (
        "Extra herkenning voor zaaknummers, rolnummers, parketnummers, dossiernummers, "
        "cliëntreferenties, ECLI's, claimnummers, incidentnummers en andere juridische of "
        "administratieve verwijzingen. Ook worden mogelijke gemiste referenties apart getoond."
    ),
    "Algemene Nederlandse controle": (
        "Herkenning voor algemene Nederlandse gegevens zoals BSN, postcode, KvK, btw-nummer, "
        "IBAN, telefoonnummers, adressen, kentekens, rijbewijsachtige nummers en BIG-nummers."
    ),
    "Algemene internationale controle": (
        "Algemene herkenning op basis van de standaard herkenningsengine en het gekozen NER-model."
    ),
}
OPERATOR_LABELS = {
    "replace": "Vervangen door placeholder",
    "redact": "Verwijderen",
    "highlight": "Markeren",
    "mask": "Maskeren met teken",
    "hash": "Hashen",
    "encrypt": "Versleutelen",
    "synthesize": "Synthetische tekst maken",
}
OPERATOR_HELP = (
    "Kies wat Scrub in de directe voorbeeldweergave doet. Voor de uiteindelijke export "
    "gebruik je altijd de controleerbare vervangtabel."
)
ADVANCED_SETTINGS_HELP = (
    "Deze instellingen zijn vooral bedoeld voor testen, tuning en technische controle. "
    "Laat ze op de standaardwaarden staan voor normaal professioneel gebruik."
)
