"""Streamlit app for SolidPrivacy Scrub Legal.

v9 Dutch Legal UI Layer:
- presents Scrub as a Dutch legal document scrubber instead of a technical demo;
- keeps recognizer/engine internals under the hood;
- adds Dutch workflow labels, Dutch review table labels and Dutch download labels;
- preserves the existing detection, audit-candidate and export workflow.
"""

from __future__ import annotations

import ast
import logging
import os
import traceback
from pathlib import Path

import dotenv
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from annotated_text import annotated_text
from streamlit_tags import st_tags

from openai_fake_data_generator import OpenAIParams
from presidio_helpers import (
    get_supported_entities,
    analyze,
    anonymize,
    annotate,
    create_fake_data,
    analyzer_engine,
)
from document_tools import (
    uploaded_file_to_text,
    build_placeholder_replacements,
    apply_replacements_to_text,
    anonymized_docx_from_original,
    docx_from_text,
    pdf_from_text,
    replacement_report_csv,
    scrub_report_txt,
)
from replacement_memory import (
    load_remembered_replacements,
    save_remembered_replacements,
    clear_remembered_replacements,
    get_memory_file_path,
)
from ui_texts_nl import (
    APP_TITLE,
    APP_SUBTITLE,
    APP_INTRO,
    LOCAL_PROCESSING_NOTE,
    PROFILE_HELP,
    PROFILE_DESCRIPTIONS,
    OPERATOR_LABELS,
    OPERATOR_HELP,
    ADVANCED_SETTINGS_HELP,
)
from display_labels_nl import entity_label, source_label, confidence_label
from side_by_side_review_panel_ui import render_side_by_side_review_panel
from serial_review_panel_ui import render_serial_review_panel
from docx_hygiene_audit_panel_ui import render_docx_hygiene_audit_panel

try:
    from candidate_scanner import scan_unmasked_candidates
except Exception:
    def scan_unmasked_candidates(text, analyzer_results=None, max_candidates=50):
        return []

try:
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


LEGAL_EXAMPLES_IMPORT_ERROR = None

EMBEDDED_LEGAL_TEST_CASES = {
    "Fallback - referenties en administratieve nummers": """Clientnummer: CL-FAM-55201.
De schoolreferentie is HRZ-SAM-2026-04.
In het verslag van Stichting Horizonzorg wordt dezelfde referentie HRZ-SAM-2026-04 genoemd.
De factuur met nummer FACT-2026-4481 is onbetaald gebleven.
De interne klantreferentie van eiser is WR-KLANT-2026-7712.
De zaakreferentie is ZK-WOON-55091.
Het artikel 7:669 BW mag niet worden gemaskeerd.
De datum 15-12-2026 mag niet als referentie worden gezien.
Het bedrag EUR 1.250,00 mag niet als referentie worden gezien.
""",
    "Fallback - familierecht contextbehoud": """Aan de Rechtbank Amsterdam

Zaaknummer C/13/701234 / FA RK 26-321
Rekestnummer RK-2026-887

Verzoeker Fatima El Amrani verzoekt wijziging van de omgangsregeling
met betrekking tot de minderjarige Sami El Amrani.
Verweerder Peter Bakker woont aan Laan van Meerdervoort 55, 2517 AM Den Haag.
""",
}

PROFILE_OPTIONS = {
    "Juridische controle — streng": "Dutch Legal Strict",
    "Algemene Nederlandse controle": "Dutch / EU",
    "Algemene internationale controle": "General / International",
}
INTERNAL_PROFILE_TO_LABEL = {value: key for key, value in PROFILE_OPTIONS.items()}
OPERATOR_LABEL_TO_VALUE = {label: value for value, label in OPERATOR_LABELS.items()}


def _load_legal_test_cases_from_file():
    """Load legal examples as data instead of importing the module."""
    examples_path = Path(__file__).with_name("legal_test_examples.py")
    if not examples_path.exists():
        raise FileNotFoundError(f"{examples_path} does not exist")

    tree = ast.parse(examples_path.read_text(encoding="utf-8"), filename=str(examples_path))
    for node in tree.body:
        is_test_cases = (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "TEST_CASES" for target in node.targets)
        ) or (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "TEST_CASES"
        )
        if is_test_cases:
            cases = ast.literal_eval(node.value)
            if not isinstance(cases, list):
                raise ValueError("TEST_CASES is not a list")
            return cases
    raise ValueError("TEST_CASES assignment not found in legal_test_examples.py")


try:
    TEST_CASES = _load_legal_test_cases_from_file()
except Exception as exc:
    LEGAL_EXAMPLES_IMPORT_ERROR = exc
    TEST_CASES = []


def get_example_names():
    if TEST_CASES:
        return [str(case.get("name", "Naamloos voorbeeld")) for case in TEST_CASES]
    return list(EMBEDDED_LEGAL_TEST_CASES.keys())


def get_example_text(name: str):
    for case in TEST_CASES:
        if str(case.get("name", "")) == name:
            return str(case.get("text", ""))
    return EMBEDDED_LEGAL_TEST_CASES.get(name, "")


def safe_cell(value):
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    return str(value).strip()


def safe_bool(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if pd.isna(value):
            return False
    except Exception:
        pass
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in ("true", "1", "yes", "y", "checked", "ja")


st.set_page_config(
    page_title=APP_TITLE,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "SolidPrivacy Scrub Legal"},
)

dotenv.load_dotenv()
logger = logging.getLogger("solidprivacy-scrub")
allow_other_models = os.getenv("ALLOW_OTHER_MODELS", False)

st.sidebar.header(APP_TITLE)
st.sidebar.caption(APP_SUBTITLE)

profile_label = st.sidebar.selectbox(
    "Controlemodus",
    list(PROFILE_OPTIONS.keys()),
    index=0,
    help=PROFILE_HELP,
)
st_recognition_profile = PROFILE_OPTIONS[profile_label]
st.sidebar.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))

operator_label = st.sidebar.selectbox(
    "Manier van vervangen",
    list(OPERATOR_LABELS.values()),
    index=list(OPERATOR_LABELS.keys()).index("replace"),
    help=OPERATOR_HELP,
)
st_operator = OPERATOR_LABEL_TO_VALUE[operator_label]

st_threshold_default = 0.30 if st_recognition_profile == "Dutch Legal Strict" else 0.35

with st.sidebar.expander("Geavanceerde instellingen", expanded=False):
    st.caption(ADVANCED_SETTINGS_HELP)
    model_help_text = (
        "Kies het NER-model dat naast regelherkenning wordt gebruikt. "
        "De Nederlandse juridische herkenners zijn regelgebaseerd."
    )
    st_ta_key = st_ta_endpoint = ""
    model_list = [
        "spaCy/en_core_web_lg",
        "flair/ner-english-large",
        "HuggingFace/obi/deid_roberta_i2b2",
        "HuggingFace/StanfordAIMI/stanford-deidentifier-base",
        "stanza/en",
        "Azure AI Language",
        "Other",
    ]
    if not allow_other_models:
        model_list.pop()
    st_model = st.selectbox(
        "Technisch NER-model",
        model_list,
        index=1,
        help=model_help_text,
    )

    st_model_package = st_model.split("/")[0]
    st_model = (
        st_model
        if st_model_package.lower() not in ("spacy", "stanza", "huggingface")
        else "/".join(st_model.split("/")[1:])
    )

    if st_model == "Other":
        st_model_package = st.selectbox(
            "NER-modelpakket", options=["spaCy", "stanza", "Flair", "HuggingFace"]
        )
        st_model = st.text_input("NER-modelnaam", value="")

    if st_model == "Azure AI Language":
        st_ta_key = st.text_input(
            "Azure AI Language key", value=os.getenv("TA_KEY", ""), type="password"
        )
        st_ta_endpoint = st.text_input(
            "Azure AI Language endpoint",
            value=os.getenv("TA_ENDPOINT", default=""),
        )

    st_threshold = st.slider(
        label="Gevoeligheid van herkenning",
        min_value=0.0,
        max_value=1.0,
        value=st_threshold_default,
        help="Lagere waarde = meer gevonden gegevens, maar ook meer kans op fout-positieven.",
    )
    st_return_decision_process = st.checkbox(
        "Toon technische beslisinformatie",
        value=False,
        help="Voegt technische uitlegvelden toe aan de resultatentabel.",
    )
    st_mask_char = st.text_input("Maskeringsteken", value="*", max_chars=1)
    st_number_of_chars = st.number_input("Aantal te maskeren tekens", value=15, min_value=0, max_value=100)
    st_encrypt_key = st.text_input("AES-sleutel", value="WmZq4t7w!z%C&F)J")

    st_deny_allow_expander = st.expander("Woordenlijsten", expanded=False)
    with st_deny_allow_expander:
        st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
        st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")

analyzer_params = (st_model_package, st_model, st_ta_key, st_ta_endpoint)
open_ai_params = None


def set_up_openai_synthesis():
    if os.getenv("OPENAI_TYPE", default="openai") == "Azure":
        openai_api_type = "azure"
        st_openai_api_base = st.sidebar.text_input(
            "Azure OpenAI base URL", value=os.getenv("AZURE_OPENAI_ENDPOINT", default="")
        )
        openai_key = os.getenv("AZURE_OPENAI_KEY", default="")
        st_deployment_id = st.sidebar.text_input(
            "Deployment name", value=os.getenv("AZURE_OPENAI_DEPLOYMENT", default="")
        )
        st_openai_version = st.sidebar.text_input(
            "OpenAI version", value=os.getenv("OPENAI_API_VERSION", default="2023-05-15")
        )
    else:
        openai_api_type = "openai"
        st_openai_version = st_openai_api_base = None
        st_deployment_id = ""
        openai_key = os.getenv("OPENAI_KEY", default="")

    st_openai_key = st.sidebar.text_input("OPENAI_KEY", value=openai_key, type="password")
    st_openai_model = st.sidebar.text_input(
        "OpenAI-model voor synthetische tekst",
        value=os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo-instruct"),
    )
    return (
        openai_api_type,
        st_openai_api_base,
        st_deployment_id,
        st_openai_version,
        st_openai_key,
        st_openai_model,
    )


if st_operator == "synthesize":
    (
        openai_api_type,
        st_openai_api_base,
        st_deployment_id,
        st_openai_version,
        st_openai_key,
        st_openai_model,
    ) = set_up_openai_synthesis()
    open_ai_params = OpenAIParams(
        openai_key=st_openai_key,
        model=st_openai_model,
        api_base=st_openai_api_base,
        deployment_id=st_deployment_id,
        api_version=st_openai_version,
        api_type=openai_api_type,
    )

st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)
st.write(APP_INTRO)
st.info(LOCAL_PROCESSING_NOTE)

with st.expander("Over deze app", expanded=False):
    st.write(
        "Scrub Legal helpt bij het controleerbaar opschonen van juridische tekst. "
        "De herkenning combineert algemene patroonherkenning, Nederlandse herkenners, "
        "juridische referentietaxonomie en een auditlaag voor mogelijke gemiste waarden."
    )
    st.write(
        "De technische detectie-engine blijft onder de motorkap. De gebruiker beoordeelt "
        "altijd zelf de gevonden gegevens en mogelijke kandidaten in de vervangtabel."
    )

if st_recognition_profile == "Dutch Legal Strict":
    st.info(
        "Juridische controle is actief. Scrub zoekt extra naar zaaknummers, rolnummers, "
        "rekestnummers, parketnummers, dossiernummers, clientnummers, CJIB, ECLI, "
        "procespartijen, instanties en mogelijke juridische referenties."
    )
elif st_recognition_profile == "Dutch / EU":
    st.info(
        "Algemene Nederlandse controle is actief. Scrub zoekt onder meer naar BSN, postcode, "
        "KvK, btw-nummer, Nederlandse IBAN, telefoonnummers, adressen, kentekens en BIG-nummers."
    )

try:
    with open("demo_text.txt", encoding="utf-8") as f:
        demo_text = f.readlines()
except Exception:
    demo_text = ["Plak of upload hier tekst om te controleren."]

st.subheader("1. Voeg document of tekst toe")
uploaded_file = st.file_uploader(
    "Upload een .txt-, .docx- of tekstgebaseerd .pdf-bestand",
    type=["txt", "docx", "pdf"],
    help="Gebruik in deze publieke prototypeomgeving alleen synthetische of goedgekeurde testdocumenten.",
)

uploaded_file_type = None
input_text = "".join(demo_text)

if st_recognition_profile == "Dutch Legal Strict":
    with st.expander("Gebruik een synthetisch juridisch testvoorbeeld", expanded=False):
        example_names = get_example_names()
        if LEGAL_EXAMPLES_IMPORT_ERROR is not None:
            st.warning(
                "Kon legal_test_examples.py niet laden. Ingebouwde fallback-voorbeelden worden getoond. "
                f"Foutmelding: {LEGAL_EXAMPLES_IMPORT_ERROR}"
            )
        elif not example_names:
            st.warning("Er zijn geen juridische voorbeelden geladen.")
            example_names = list(EMBEDDED_LEGAL_TEST_CASES.keys())

        sample_name = st.selectbox(
            "Laad synthetisch juridisch voorbeeld",
            ["Geen testvoorbeeld laden"] + example_names,
            index=0,
        )
        if sample_name != "Geen testvoorbeeld laden" and uploaded_file is None:
            example_text = get_example_text(sample_name)
            if not example_text and sample_name in EMBEDDED_LEGAL_TEST_CASES:
                example_text = EMBEDDED_LEGAL_TEST_CASES[sample_name]
            input_text = example_text
            st.caption("Synthetische voorbeeldtekst geladen. Er staan geen echte persoonsgegevens in.")

if uploaded_file is not None:
    try:
        input_text, uploaded_file_type = uploaded_file_to_text(uploaded_file)
        st.success(f"Bestand geladen: {uploaded_file.name}")
    except Exception as upload_error:
        st.error(f"Kon het bestand niet lezen: {upload_error}")

st_text = st.text_area(
    label="Plak tekst of controleer de uit het document gehaalde tekst",
    value=input_text,
    height=300,
    key="text_input",
)

try:
    all_supported_entities = list(get_supported_entities(*analyzer_params))
    general_dutch_entities = set(get_dutch_general_entity_names())
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

    with st.sidebar.expander("Te herkennen gegevenstypen", expanded=False):
        st_entities = st.multiselect(
            label="Welke typen gegevens moet Scrub zoeken?",
            options=all_supported_entities,
            default=default_entities,
            help="Laat dit standaard staan, tenzij je gericht wilt testen of tunen.",
        )

    analyzer_load_state = st.info("Herkenningsengine starten...")
    analyzer = analyzer_engine(*analyzer_params)
    analyzer_load_state.empty()

    st_analyze_results = analyze(
        *analyzer_params,
        text=st_text,
        entities=st_entities,
        language="en",
        score_threshold=st_threshold,
        return_decision_process=st_return_decision_process,
        allow_list=st_allow_list,
        deny_list=st_deny_list,
    )

    if st_operator not in ("highlight", "synthesize"):
        _, report_rows = build_placeholder_replacements(st_text, st_analyze_results)
        candidate_rows = []
        if st_recognition_profile == "Dutch Legal Strict":
            candidate_rows = scan_unmasked_candidates(st_text, st_analyze_results, max_candidates=50)

        remembered_rows = load_remembered_replacements()
        default_editor_rows = []
        seen_find_values = set()

        for row in remembered_rows:
            find_text = str(row.get("find", "")).strip()
            replace_with = str(row.get("replace_with", "")).strip()
            if not find_text or not replace_with:
                continue
            entity_type = row.get("entity_type", "REMEMBERED")
            default_editor_rows.append(
                {
                    "include": row.get("include", True),
                    "remember": row.get("remember", True),
                    "find": find_text,
                    "replace_with": replace_with,
                    "type_label": entity_label(entity_type),
                    "entity_type": entity_type,
                    "confidence": "",
                    "score": None,
                    "source_label": source_label("remembered"),
                    "source": "remembered",
                    "reason": "Opgeslagen herbruikbare vervanging",
                    "context": "",
                }
            )
            seen_find_values.add(find_text)

        for row in report_rows:
            find_text = str(row.get("detected_text", "")).strip()
            if not find_text or find_text in seen_find_values:
                continue
            entity_type = row.get("entity_type", "")
            score = row.get("score", None)
            default_editor_rows.append(
                {
                    "include": True,
                    "remember": False,
                    "find": find_text,
                    "replace_with": row.get("placeholder", ""),
                    "type_label": entity_label(entity_type),
                    "entity_type": entity_type,
                    "confidence": confidence_label(score),
                    "score": score,
                    "source_label": source_label("detected"),
                    "source": "detected",
                    "reason": "Automatisch herkend",
                    "context": "",
                }
            )
            seen_find_values.add(find_text)

        for candidate in candidate_rows:
            find_text = str(candidate.get("text", "")).strip()
            if not find_text or find_text in seen_find_values:
                continue
            entity_type = candidate.get("entity_type", "NL_SUSPICIOUS_REFERENCE_CANDIDATE")
            score = candidate.get("score", None)
            default_editor_rows.append(
                {
                    "include": False,
                    "remember": False,
                    "find": find_text,
                    "replace_with": candidate.get("placeholder", "<MOGELIJKE_REFERENTIE>"),
                    "type_label": entity_label(entity_type),
                    "entity_type": entity_type,
                    "confidence": confidence_label(score),
                    "score": score,
                    "source_label": source_label("candidate"),
                    "source": "candidate",
                    "reason": candidate.get("reason", "Mogelijke gemiste waarde"),
                    "context": candidate.get("context", ""),
                }
            )
            seen_find_values.add(find_text)

        if not default_editor_rows:
            default_editor_rows = [
                {
                    "include": True,
                    "remember": False,
                    "find": "",
                    "replace_with": "",
                    "type_label": entity_label("MANUAL"),
                    "entity_type": "MANUAL",
                    "confidence": "",
                    "score": None,
                    "source_label": source_label("manual"),
                    "source": "manual",
                    "reason": "Handmatige vervangingsregel",
                    "context": "",
                }
            ]

        replacement_editor_df = pd.DataFrame(default_editor_rows)

        st.divider()
        st.subheader("2. Controleer de tekst")
        st.caption(
            "Centrale side-by-side reviewweergave. Brontekst links, verwerkte tekst rechts. "
            "Synchroon scrollen en optionele markeringen blijven visuele hulp."
        )
        render_side_by_side_review_panel(
            source_text=st_text,
            edited_replacements_df=replacement_editor_df,
        )

        st.divider()
        st.subheader("3. Controleer gevonden gegevens")
        st.caption(
            "Vink fout-positieven uit, pas placeholders aan, voeg handmatige vervangingen toe "
            "en vink Onthouden aan voor vervangingen die je opnieuw wilt gebruiken. "
            "Mogelijke kandidaten staan standaard uitgevinkt. De vervangtabel blijft leidend."
        )

        if st_recognition_profile == "Dutch Legal Strict":
            with st.expander("Mogelijke gemiste waarden", expanded=bool(candidate_rows)):
                if candidate_rows:
                    st.warning(
                        "Deze waarden zijn niet automatisch vervangen, maar lijken mogelijk op juridische of administratieve referenties. "
                        "Controleer ze en vink ze alleen aan als ze echt vervangen moeten worden."
                    )
                    candidate_display_df = pd.DataFrame(candidate_rows)
                    candidate_display_df["type_gegeven"] = candidate_display_df["entity_type"].map(entity_label)
                    candidate_display_df["zekerheid"] = candidate_display_df["score"].map(confidence_label)
                    candidate_display_df = candidate_display_df[
                        ["type_gegeven", "text", "placeholder", "zekerheid", "reason", "context"]
                    ].rename(
                        columns={
                            "type_gegeven": "Type gegeven",
                            "text": "Gevonden tekst",
                            "placeholder": "Voorgestelde vervanging",
                            "zekerheid": "Zekerheid",
                            "reason": "Reden",
                            "context": "Context",
                        }
                    )
                    st.dataframe(candidate_display_df, use_container_width=True)
                else:
                    st.success("Geen mogelijke gemiste referenties gevonden door de auditlaag.")

        edited_replacements_df = st.data_editor(
            replacement_editor_df,
            hide_index=True,
            num_rows="dynamic",
            use_container_width=True,
            column_order=[
                "include",
                "remember",
                "find",
                "replace_with",
                "type_label",
                "confidence",
                "source_label",
                "reason",
                "context",
                "entity_type",
                "score",
                "source",
            ],
            column_config={
                "include": st.column_config.CheckboxColumn(
                    "Meenemen", help="Vink uit om deze vervanging niet toe te passen.", default=True
                ),
                "remember": st.column_config.CheckboxColumn(
                    "Onthouden", help="Bewaar deze vervanging voor later gebruik.", default=False
                ),
                "find": st.column_config.TextColumn(
                    "Gevonden tekst", help="Exacte tekst die vervangen moet worden."
                ),
                "replace_with": st.column_config.TextColumn(
                    "Vervangen door", help="Placeholder of vervangende tekst."
                ),
                "type_label": st.column_config.TextColumn(
                    "Type gegeven", help="Gebruiksvriendelijke categorie."
                ),
                "confidence": st.column_config.TextColumn(
                    "Zekerheid", help="Globale inschatting van de herkenningszekerheid."
                ),
                "source_label": st.column_config.TextColumn(
                    "Bron", help="Automatisch herkend, mogelijke kandidaat, onthouden of handmatig."
                ),
                "reason": st.column_config.TextColumn(
                    "Reden", help="Waarom deze regel is voorgesteld."
                ),
                "context": st.column_config.TextColumn(
                    "Context", help="Nabije tekst voor kandidaatregels."
                ),
                "entity_type": st.column_config.TextColumn(
                    "Technisch type", help="Interne herkennercategorie."
                ),
                "score": st.column_config.NumberColumn(
                    "Technische score", help="Numerieke score, indien beschikbaar.", format="%.3f"
                ),
                "source": st.column_config.TextColumn("Technische bron"),
            },
            key="replacement_editor",
        )

        render_serial_review_panel(
            displayed_text=st_text,
            edited_replacements_df=edited_replacements_df,
            include_side_by_side=False,
        )

        edited_replacements = {}
        edited_report_rows = []
        for _, row in edited_replacements_df.iterrows():
            include = safe_bool(row.get("include", False))
            find_text = safe_cell(row.get("find", ""))
            replace_text = safe_cell(row.get("replace_with", ""))
            entity_type = safe_cell(row.get("entity_type", "MANUAL")) or "MANUAL"
            score = row.get("score", None)
            if not include or not find_text or not replace_text:
                continue
            edited_replacements[find_text] = replace_text
            edited_report_rows.append(
                {
                    "entity_type": entity_type,
                    "detected_text": find_text,
                    "placeholder": replace_text,
                    "score": score if score is not None else "",
                    "source": safe_cell(row.get("source", "")),
                    "reason": safe_cell(row.get("reason", "")),
                }
            )

        st.info(f"{len(edited_replacements)} vervanging(en) worden toegepast op de exports.")

        export_text = apply_replacements_to_text(st_text, edited_replacements)

        st.subheader("4. Onthoud herbruikbare vervangingen")
        remember_rows_to_save = []
        for _, row in edited_replacements_df.iterrows():
            include = safe_bool(row.get("include", False))
            remember = safe_bool(row.get("remember", False))
            find_text = safe_cell(row.get("find", ""))
            replace_text = safe_cell(row.get("replace_with", ""))
            entity_type = safe_cell(row.get("entity_type", "REMEMBERED")) or "REMEMBERED"
            if include and remember and find_text and replace_text:
                remember_rows_to_save.append({"find": find_text, "replace_with": replace_text, "entity_type": entity_type})

        memory_col1, memory_col2 = st.columns(2)
        with memory_col1:
            if st.button("Onthouden vervangingen opslaan"):
                saved_count = save_remembered_replacements(remember_rows_to_save)
                st.success(f"{saved_count} vervanging(en) opgeslagen.")
                st.info(f"Geheugenbestand: {get_memory_file_path()}")
        with memory_col2:
            if st.button("Onthouden vervangingen wissen"):
                clear_remembered_replacements()
                st.warning("Onthouden vervangingen gewist.")

        st.subheader("5. Download opgeschoonde bestanden")
        if uploaded_file is not None:
            st.info(f"Bestand beschikbaar voor export: {uploaded_file.name}")
        else:
            st.info("Geen uploadbestand aanwezig. Export wordt gemaakt op basis van het tekstvak.")

        st.download_button(
            label="Download opgeschoonde tekst (.txt)",
            data=export_text.encode("utf-8"),
            file_name="opgeschoonde_tekst.txt",
            mime="text/plain",
            key="download_txt",
        )
        st.download_button(
            label="Download vervangtabel (.csv)",
            data=replacement_report_csv(edited_report_rows),
            file_name="vervangtabel.csv",
            mime="text/csv",
            key="download_csv",
        )
        st.download_button(
            label="Download scrubrapport (.txt)",
            data=scrub_report_txt(
                edited_report_rows,
                profile=profile_label,
                source_filename=uploaded_file.name if uploaded_file is not None else None,
            ),
            file_name="scrubrapport.txt",
            mime="text/plain",
            key="download_scrub_report",
        )

        try:
            if uploaded_file is not None and uploaded_file.name.lower().endswith(".docx"):
                docx_bytes = anonymized_docx_from_original(uploaded_file, edited_replacements)
                docx_filename = "opgeschoond_" + uploaded_file.name
            else:
                docx_bytes = docx_from_text(export_text)
                docx_filename = "opgeschoonde_tekst.docx"
            render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)
            st.download_button(
                label="Download opgeschoond Word-bestand (.docx)",
                data=docx_bytes,
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_docx",
            )
        except Exception as docx_error:
            st.error(f"Kon geen DOCX-export maken: {docx_error}")

        try:
            st.download_button(
                label="Download opgeschoonde PDF (.pdf)",
                data=pdf_from_text(export_text),
                file_name="opgeschoonde_tekst.pdf",
                mime="application/pdf",
                key="download_pdf",
            )
        except Exception as pdf_error:
            st.error(f"Kon geen PDF-export maken: {pdf_error}")

    elif st_operator == "synthesize":
        st.subheader("Synthetische tekst")
        fake_data = create_fake_data(st_text, st_analyze_results, open_ai_params)
        st.text_area(label="Synthetische data", value=fake_data, height=400)
    else:
        st.subheader("Gemarkeerde tekst")
        annotated_tokens = annotate(text=st_text, analyze_results=st_analyze_results)
        annotated_text(*annotated_tokens)

    with st.expander("Technische herkenningen", expanded=False):
        if st_analyze_results:
            df = pd.DataFrame.from_records([r.to_dict() for r in st_analyze_results])
            df["text"] = [st_text[res.start : res.end] for res in st_analyze_results]
            df["type_gegeven"] = df["entity_type"].map(entity_label)
            df["zekerheid"] = df["score"].map(confidence_label)
            df_subset = df[["type_gegeven", "text", "start", "end", "score", "zekerheid", "entity_type"]].rename(
                {
                    "type_gegeven": "Type gegeven",
                    "text": "Gevonden tekst",
                    "start": "Start",
                    "end": "Einde",
                    "score": "Score",
                    "zekerheid": "Zekerheid",
                    "entity_type": "Technisch type",
                },
                axis=1,
            )
            if st_return_decision_process:
                analysis_explanation_df = pd.DataFrame.from_records(
                    [r.analysis_explanation.to_dict() for r in st_analyze_results]
                )
                df_subset = pd.concat([df_subset, analysis_explanation_df], axis=1)
            st.dataframe(df_subset.reset_index(drop=True), use_container_width=True)
        else:
            st.text("Geen herkenningen gevonden.")

except Exception as e:
    print(e)
    traceback.print_exc()
    st.error(e)

components.html(""" """)
