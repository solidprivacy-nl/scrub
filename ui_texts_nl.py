APP_TITLE = "Scrub Legal"
APP_SUBTITLE = "Lokale juridische documentcontrole"
APP_VERSION = "v9.1"
APP_INTRO = (
    "Schoon processtukken, brieven en juridische notities op voordat je ze deelt "
    "of gebruikt in AI-tools. Scrub zoekt namen, adressen, zaaknummers, "
    "dossiernummers en andere herleidbare gegevens en laat jou controleren wat "
    "wordt vervangen."
)
LOCAL_PROCESSING_NOTE = (
    "Deze prototypeversie gebruikt herkenningsregels en lokale app-logica. "
    "Controleer het resultaat altijd handmatig voordat je het document gebruikt."
)
PROFILE_HELP = (
    "Kies hoe streng Scrub moet zoeken. Juridisch streng is bedoeld voor Nederlandse "
    "processtukken, dossiers, correspondentie en juridische notities."
)
PROFILE_DESCRIPTIONS = {
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
    "Laat ze op de standaardwaarden staan voor normaal juridisch gebruik."
)
