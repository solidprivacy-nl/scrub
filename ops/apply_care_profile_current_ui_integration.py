from __future__ import annotations

from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Expected anchor not found in {path}: {old[:180]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def patch_presidio_helpers() -> None:
    path = "presidio_helpers.py"
    replace_once(
        path,
        '''try:
    from dutch_recognizers import get_dutch_recognizers, get_dutch_entity_names
except Exception:  # pragma: no cover - keeps original demo usable if file is absent
    get_dutch_recognizers = None
    get_dutch_entity_names = None
''',
        '''try:
    from dutch_recognizers import get_dutch_recognizers, get_dutch_entity_names
except Exception:  # pragma: no cover - keeps original demo usable if file is absent
    get_dutch_recognizers = None
    get_dutch_entity_names = None

try:
    from dutch_care_recognizers import (
        get_dutch_care_recognizers,
        get_dutch_care_entity_names,
    )
except Exception:  # pragma: no cover - keeps original demo usable if file is absent
    get_dutch_care_recognizers = None
    get_dutch_care_entity_names = None
''',
    )
    replace_once(
        path,
        '''@st.cache_resource
def analyzer_engine(
''',
        '''def register_custom_recognizers(analyzer: AnalyzerEngine) -> None:
    """Register Dutch general/legal and dedicated care recognizers."""

    for factory in (get_dutch_recognizers, get_dutch_care_recognizers):
        if factory is None:
            continue
        for recognizer in factory(supported_language="en"):
            try:
                analyzer.registry.add_recognizer(recognizer)
            except Exception as exc:
                logger.debug("Could not register %s: %s", recognizer, exc)


def get_custom_entity_names() -> List[str]:
    """Return stable, de-duplicated Dutch general/legal/care entity names."""

    names: List[str] = []
    for factory in (get_dutch_entity_names, get_dutch_care_entity_names):
        if factory is None:
            continue
        for entity in factory():
            if entity not in names:
                names.append(entity)
    return names


@st.cache_resource
def analyzer_engine(
''',
    )
    replace_once(
        path,
        '''    # Register Dutch/EU pattern recognizers. They are registered for language="en"
    # because this demo currently calls analyzer.analyze(language="en") and uses
    # English NER models. This makes Dutch identifiers available without requiring
    # a separate Dutch NLP model.
    if get_dutch_recognizers is not None:
        for recognizer in get_dutch_recognizers(supported_language="en"):
            try:
                analyzer.registry.add_recognizer(recognizer)
            except Exception as exc:  # avoid breaking the demo on duplicate/registry edge cases
                logger.debug("Could not register %s: %s", recognizer, exc)

    return analyzer
''',
        '''    # Register all local Dutch general/legal and dedicated care recognizers.
    # They use supported_language="en" because the current demo invokes Presidio
    # with language="en" while using Dutch custom patterns.
    register_custom_recognizers(analyzer)

    return analyzer
''',
    )
    replace_once(
        path,
        '''    if get_dutch_entity_names is not None:
        for entity in get_dutch_entity_names():
            if entity not in entities:
                entities.append(entity)
''',
        '''    for entity in get_custom_entity_names():
        if entity not in entities:
            entities.append(entity)
''',
    )


def patch_document_tools() -> None:
    path = "document_tools.py"
    replace_once(
        path,
        '''    "NL_HEALTHCARE_REFERENCE": "ZORGREFERENTIE",
    "NL_POLICE_REFERENCE": "POLITIEREFERENTIE",
''',
        '''    "NL_HEALTHCARE_REFERENCE": "ZORGREFERENTIE",
    "NL_PATIENT_NUMBER": "PATIENTNUMMER",
    "NL_CARE_CLIENT_NUMBER": "ZORGCLIENTNUMMER",
    "NL_MEDICAL_RECORD_NUMBER": "MEDISCH_DOSSIERNUMMER",
    "NL_EPD_ECD_NUMBER": "EPD_ECD_NUMMER",
    "NL_HEALTH_INSURANCE_NUMBER": "VERZEKERDENNUMMER",
    "NL_REFERRAL_NUMBER": "VERWIJSNUMMER",
    "NL_TREATMENT_REFERENCE": "BEHANDELREFERENTIE",
    "NL_LAB_SAMPLE_NUMBER": "LABREFERENTIE",
    "NL_CARE_INCIDENT_NUMBER": "ZORGINCIDENTNUMMER",
    "NL_CARE_INDICATION_REFERENCE": "ZORGINDICATIEREFERENTIE",
    "NL_AGB_CODE": "AGB_CODE",
    "NL_CARE_PROVIDER_NAME": "ZORGVERLENER",
    "NL_CARE_ORGANIZATION": "ZORGORGANISATIE",
    "NL_CARE_LOCATION_REFERENCE": "ZORGLOCATIE",
    "NL_ROOM_OR_BED_REFERENCE": "KAMER_OF_BED",
    "NL_CARE_EVENT_DATE": "ZORGDATUM",
    "NL_POLICE_REFERENCE": "POLITIEREFERENTIE",
''',
    )
    replace_once(
        path,
        '''STRUCTURED_ENTITY_TYPES = LEGAL_ENTITY_TYPES | {
''',
        '''CARE_ENTITY_TYPES = {
    "NL_PATIENT_NUMBER",
    "NL_CARE_CLIENT_NUMBER",
    "NL_MEDICAL_RECORD_NUMBER",
    "NL_EPD_ECD_NUMBER",
    "NL_HEALTH_INSURANCE_NUMBER",
    "NL_REFERRAL_NUMBER",
    "NL_TREATMENT_REFERENCE",
    "NL_LAB_SAMPLE_NUMBER",
    "NL_CARE_INCIDENT_NUMBER",
    "NL_CARE_INDICATION_REFERENCE",
    "NL_AGB_CODE",
    "NL_CARE_PROVIDER_NAME",
    "NL_CARE_ORGANIZATION",
    "NL_CARE_LOCATION_REFERENCE",
    "NL_ROOM_OR_BED_REFERENCE",
    "NL_CARE_EVENT_DATE",
}

STRUCTURED_ENTITY_TYPES = LEGAL_ENTITY_TYPES | CARE_ENTITY_TYPES | {
''',
    )
    replace_once(
        path,
        '''    # Legal identifiers are usually safer to include once our recognizers find them.
    if entity_type in LEGAL_ENTITY_TYPES:
        return False
''',
        '''    # Context-bound legal and care identifiers are safer to include once
    # their dedicated recognizers find the exact value span.
    if entity_type in LEGAL_ENTITY_TYPES or entity_type in CARE_ENTITY_TYPES:
        return False
''',
    )


def patch_streamlit_app() -> None:
    path = "presidio_streamlit.py"
    replace_once(
        path,
        '''    PROFILE_HELP,
    PROFILE_DESCRIPTIONS,
    OPERATOR_LABELS,
''',
        '''    PROFILE_HELP,
    OPERATOR_LABELS,
''',
    )
    replace_once(
        path,
        '''try:
    from candidate_scanner import scan_unmasked_candidates
except Exception:
    def scan_unmasked_candidates(text, analyzer_results=None, max_candidates=50):
        return []

''',
        '''from profile_ui_support import (
    care_example_names,
    care_example_text,
    configured_description,
    configured_entity_names,
    configured_threshold,
    current_profile_options_with_care,
    detected_reason,
    resolve_configured_analysis_results,
    scan_configured_candidates,
)

''',
    )
    replace_once(
        path,
        '''try:
    from dutch_recognizers import (
        get_dutch_entity_names,
        get_dutch_general_entity_names,
        get_dutch_legal_entity_names,
    )
except Exception:
    def get_dutch_entity_names(include_legal=True):
        return []

    def get_dutch_general_entity_names():
        return []

    def get_dutch_legal_entity_names():
        return []

''',
        '''try:
    from dutch_recognizers import (
        get_dutch_entity_names,
        get_dutch_general_entity_names,
        get_dutch_legal_entity_names,
    )
except Exception:
    def get_dutch_entity_names(include_legal=True):
        return []

    def get_dutch_general_entity_names():
        return []

    def get_dutch_legal_entity_names():
        return []

try:
    from dutch_care_recognizers import get_dutch_care_entity_names
except Exception:
    def get_dutch_care_entity_names():
        return []

''',
    )
    replace_once(
        path,
        '''PROFILE_OPTIONS = {
    "Juridische controle — streng": "Dutch Legal Strict",
    "Algemene Nederlandse controle": "Dutch / EU",
    "Algemene internationale controle": "General / International",
}
''',
        '''PROFILE_OPTIONS = current_profile_options_with_care()
''',
    )
    replace_once(
        path,
        '''    menu_items={"About": "SolidPrivacy Scrub Legal"},
''',
        '''    menu_items={"About": "SolidPrivacy Scrub"},
''',
    )
    replace_once(
        path,
        '''profile_label = st.sidebar.selectbox(
    "Controlemodus",
    list(PROFILE_OPTIONS.keys()),
    index=0,
    help=PROFILE_HELP,
)
st_recognition_profile = PROFILE_OPTIONS[profile_label]
with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False):
    st.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))
''',
        '''profile_label = st.sidebar.selectbox(
    "Controlemodus",
    list(PROFILE_OPTIONS.keys()),
    index=1,
    help=PROFILE_HELP,
)
st_recognition_profile = PROFILE_OPTIONS[profile_label]
with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False):
    st.info(configured_description(st_recognition_profile))
''',
    )
    replace_once(
        path,
        '''st_threshold_default = 0.30 if st_recognition_profile == "Dutch Legal Strict" else 0.35
''',
        '''st_threshold_default = configured_threshold(st_recognition_profile)
''',
    )
    replace_once(
        path,
        '''with st.expander("Over deze app", expanded=False):
    st.write(
        "Scrub Legal helpt bij het controleerbaar opschonen van juridische tekst. "
        "De herkenning combineert algemene patroonherkenning, Nederlandse herkenners, "
        "juridische referentietaxonomie en een auditlaag voor mogelijke gemiste waarden."
    )
    st.write(
        "De technische detectie-engine blijft onder de motorkap. De gebruiker beoordeelt "
        "altijd zelf de gevonden gegevens en mogelijke kandidaten in de vervangtabel."
    )
''',
        '''with st.expander("Over deze app", expanded=False):
    st.write(
        "SolidPrivacy Scrub helpt bij het controleerbaar opschonen van vertrouwelijke "
        "Nederlandse documenten. De herkenning combineert algemene patroonherkenning "
        "met expliciete profielen voor zorg en juridische documenten."
    )
    st.write(
        "De technische detectie-engine blijft onder de motorkap. De gebruiker beoordeelt "
        "altijd zelf de gevonden gegevens en mogelijke kandidaten in de vervangtabel."
    )
''',
    )
    replace_once(
        path,
        '''with st.expander("Controle-instellingen en herkenning", expanded=False):
    if st_recognition_profile == "Dutch Legal Strict":
''',
        '''with st.expander("Controle-instellingen en herkenning", expanded=False):
    if st_recognition_profile == "Dutch Care Strict":
        st.info(
            "Zorgcontrole is actief. Scrub zoekt extra naar patiënt- en cliëntnummers, "
            "EPD/ECD- en dossiernummers, verwijzingen, laboratorium- en incidentreferenties, "
            "zorgverleners, organisaties, locaties en exacte zorgdata. Diagnose, medicatie, "
            "dosering, labwaarden en observaties blijven zo veel mogelijk leesbaar."
        )
    elif st_recognition_profile == "Dutch Legal Strict":
''',
    )
    replace_once(
        path,
        '''    if st_recognition_profile == "Dutch Legal Strict":
        with st.expander("Gebruik een synthetisch juridisch testvoorbeeld", expanded=False):
''',
        '''    if st_recognition_profile == "Dutch Care Strict":
        with st.expander("Gebruik een synthetisch zorgvoorbeeld", expanded=False):
            sample_name = st.selectbox(
                "Laad synthetisch zorgvoorbeeld",
                ["Geen testvoorbeeld laden"] + care_example_names(),
                index=0,
            )
            if sample_name != "Geen testvoorbeeld laden" and uploaded_file is None:
                input_text = care_example_text(sample_name)
                st.caption("Synthetische voorbeeldtekst geladen. Er staan geen echte persoonsgegevens in.")

    elif st_recognition_profile == "Dutch Legal Strict":
        with st.expander("Gebruik een synthetisch juridisch testvoorbeeld", expanded=False):
''',
    )
    replace_once(
        path,
        '''    general_dutch_entities = set(get_dutch_general_entity_names())
    all_dutch_entities = set(get_dutch_entity_names(include_legal=True))

    base_preferred_entities = {
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "IBAN_CODE",
        "URL",
        "IP_ADDRESS",
        "GENERIC_PII",
        "DATE_TIME",
    }

    if st_recognition_profile == "Dutch Legal Strict":
        preferred_entities = base_preferred_entities | all_dutch_entities
    elif st_recognition_profile == "Dutch / EU":
        preferred_entities = base_preferred_entities | general_dutch_entities
    else:
        preferred_entities = set(all_supported_entities)

    default_entities = [entity for entity in all_supported_entities if entity in preferred_entities]
''',
        '''    general_dutch_entities = set(get_dutch_general_entity_names())
    legal_dutch_entities = set(get_dutch_legal_entity_names())
    care_dutch_entities = set(get_dutch_care_entity_names())

    default_entities = configured_entity_names(
        st_recognition_profile,
        all_supported_entities,
        dutch_general_entities=general_dutch_entities,
        dutch_legal_entities=legal_dutch_entities,
        dutch_care_entities=care_dutch_entities,
    )
''',
    )
    replace_once(
        path,
        '''        deny_list=st_deny_list,
    )

    if st_operator not in ("highlight", "synthesize"):
''',
        '''        deny_list=st_deny_list,
    )
    st_analyze_results = resolve_configured_analysis_results(
        st_recognition_profile,
        st_analyze_results,
    )

    if st_operator not in ("highlight", "synthesize"):
''',
    )
    replace_once(
        path,
        '''        candidate_rows = []
        if st_recognition_profile == "Dutch Legal Strict":
            candidate_rows = scan_unmasked_candidates(st_text, st_analyze_results, max_candidates=50)
''',
        '''        candidate_rows = scan_configured_candidates(
            st_recognition_profile,
            st_text,
            st_analyze_results,
            max_candidates=50,
        )
''',
    )
    replace_once(
        path,
        '''                    "reason": "Automatisch herkend",
''',
        '''                    "reason": detected_reason(st_recognition_profile, entity_type),
''',
    )


def patch_ui_texts() -> None:
    Path("ui_texts_nl.py").write_text(
        '''APP_TITLE = "SolidPrivacy Scrub"
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
''',
        encoding="utf-8",
    )


def patch_display_labels() -> None:
    path = "display_labels_nl.py"
    replace_once(
        path,
        '''    "NL_HEALTHCARE_REFERENCE": "Zorgreferentie",
    "NL_POLICE_REFERENCE": "Politie-/OM-referentie",
''',
        '''    "NL_HEALTHCARE_REFERENCE": "Zorgreferentie",
    "NL_PATIENT_NUMBER": "Patiëntnummer",
    "NL_CARE_CLIENT_NUMBER": "Zorgcliëntnummer",
    "NL_MEDICAL_RECORD_NUMBER": "Medisch dossiernummer",
    "NL_EPD_ECD_NUMBER": "EPD- of ECD-nummer",
    "NL_HEALTH_INSURANCE_NUMBER": "Verzekerdennummer",
    "NL_REFERRAL_NUMBER": "Verwijsnummer",
    "NL_TREATMENT_REFERENCE": "Behandel- of zorgtrajectnummer",
    "NL_LAB_SAMPLE_NUMBER": "Laboratorium- of monsternummer",
    "NL_CARE_INCIDENT_NUMBER": "Zorgincidentnummer",
    "NL_CARE_INDICATION_REFERENCE": "Indicatie- of beschikkingreferentie",
    "NL_AGB_CODE": "AGB-code",
    "NL_CARE_PROVIDER_NAME": "Zorgverlener / naam",
    "NL_CARE_ORGANIZATION": "Zorgorganisatie",
    "NL_CARE_LOCATION_REFERENCE": "Zorglocatie, afdeling of team",
    "NL_ROOM_OR_BED_REFERENCE": "Kamer- of bedreferentie",
    "NL_CARE_EVENT_DATE": "Exacte zorgdatum",
    "NL_POLICE_REFERENCE": "Politie-/OM-referentie",
''',
    )


def main() -> None:
    patch_presidio_helpers()
    patch_document_tools()
    patch_streamlit_app()
    patch_ui_texts()
    patch_display_labels()

    Path("ops/apply_care_profile_current_ui_integration.py").unlink(missing_ok=True)
    Path(".github/workflows/apply-care-profile-current-ui-integration.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
