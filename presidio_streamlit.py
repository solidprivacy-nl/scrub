"""Streamlit app for SolidPrivacy Scrub / Microsoft Presidio.

Phase 1-3 update:
- Dutch Legal Strict recognition profile;
- Dutch legal test examples;
- Dutch Legal Reference Taxonomy for context-based reference codes;
- legal-aware replacement labels and scrub report download;
- keeps current workflow: upload -> detect -> editable replacement table -> export.
"""

import logging
import os
import traceback

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

try:
    from dutch_recognizers import (
        get_dutch_entity_names,
        get_dutch_general_entity_names,
        get_dutch_legal_entity_names,
    )
except Exception:  # keep app usable while new file is being added
    def get_dutch_entity_names(include_legal=True):
        return []

    def get_dutch_general_entity_names():
        return []

    def get_dutch_legal_entity_names():
        return []

LEGAL_EXAMPLES_IMPORT_ERROR = None

EMBEDDED_LEGAL_TEST_CASES = {
    "Fallback - referenties en administratieve nummers": """Cliëntnummer: CL-FAM-55201.
De schoolreferentie is HRZ-SAM-2026-04.
In het verslag van Stichting Horizonzorg wordt dezelfde referentie HRZ-SAM-2026-04 genoemd.
De factuur met nummer FACT-2026-4481 is onbetaald gebleven.
De interne klantreferentie van eiser is WR-KLANT-2026-7712.
De zaakreferentie is ZK-WOON-55091.
Het artikel 7:669 BW mag niet worden gemaskeerd.
De datum 15-12-2026 mag niet als referentie worden gezien.
Het bedrag € 1.250,00 mag niet als referentie worden gezien.
""",
    "Fallback - familierecht contextbehoud": """Aan de Rechtbank Amsterdam

Zaaknummer C/13/701234 / FA RK 26-321
Rekestnummer RK-2026-887

Verzoeker Fatima El Amrani verzoekt wijziging van de omgangsregeling
met betrekking tot de minderjarige Sami El Amrani.
Verweerder Peter Bakker woont aan Laan van Meerdervoort 55, 2517 AM Den Haag.
""",
}

try:
    from legal_test_examples import TEST_CASES, get_example_names, get_example_text
except Exception as exc:
    LEGAL_EXAMPLES_IMPORT_ERROR = exc
    TEST_CASES = []

    def get_example_names():
        return list(EMBEDDED_LEGAL_TEST_CASES.keys())

    def get_example_text(name: str):
        return EMBEDDED_LEGAL_TEST_CASES.get(name, "")


st.set_page_config(
    page_title="SolidPrivacy Scrub",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "https://microsoft.github.io/presidio/"},
)

dotenv.load_dotenv()
logger = logging.getLogger("presidio-streamlit")
allow_other_models = os.getenv("ALLOW_OTHER_MODELS", False)


# Sidebar
st.sidebar.header(
    """
    SolidPrivacy Scrub
    
    PII De-Identification with [Microsoft Presidio](https://microsoft.github.io/presidio/)
    """
)

model_help_text = """
Select which Named Entity Recognition (NER) model to use for PII detection,
in parallel to rule-based recognizers. The Dutch Legal Strict layer is rule-based
and does not require a cloud model.
"""

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

st_model = st.sidebar.selectbox(
    "NER model package",
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
    st_model_package = st.sidebar.selectbox(
        "NER model OSS package", options=["spaCy", "stanza", "Flair", "HuggingFace"]
    )
    st_model = st.sidebar.text_input("NER model name", value="")

if st_model == "Azure AI Language":
    st_ta_key = st.sidebar.text_input(
        "Azure AI Language key", value=os.getenv("TA_KEY", ""), type="password"
    )
    st_ta_endpoint = st.sidebar.text_input(
        "Azure AI Language endpoint",
        value=os.getenv("TA_ENDPOINT", default=""),
        help="For more info: https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/overview",
    )

st.sidebar.warning("Note: some NER models might take time to download/load.")
analyzer_params = (st_model_package, st_model, st_ta_key, st_ta_endpoint)
logger.debug("analyzer_params: %s", analyzer_params)

st_recognition_profile = st.sidebar.selectbox(
    "Recognition profile",
    ["Dutch Legal Strict", "Dutch / EU", "General / International"],
    index=0,
    help=(
        "Dutch Legal Strict adds Dutch legal/matter identifiers such as zaaknummer, "
        "rolnummer, parketnummer, dossiernummer, cliëntnummer, CJIB and ECLI. "
        "Dutch / EU enables general Dutch identifiers such as BSN, postcode, KvK, BTW/VAT, "
        "Dutch IBAN, Dutch phone numbers and Dutch address patterns."
    ),
)

st_operator = st.sidebar.selectbox(
    "De-identification approach",
    ["redact", "replace", "synthesize", "highlight", "mask", "hash", "encrypt"],
    index=1,
    help="""
    Select which manipulation is requested after PII has been identified.
    - Redact: completely remove the PII text
    - Replace: replace PII with a placeholder
    - Synthesize: replace with fake values; requires an OpenAI key
    - Highlight: show original text with PII highlighted
    - Mask: replace characters with a mask character
    - Hash: replace with a hash
    - Encrypt: replace with AES encryption, reversible with the key
    """,
)

st_mask_char = "*"
st_number_of_chars = 15
st_encrypt_key = "WmZq4t7w!z%C&F)J"
open_ai_params = None
logger.debug("st_operator: %s", st_operator)


def set_up_openai_synthesis():
    """Set up the OpenAI API key and model for text synthesis."""
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

    st_openai_key = st.sidebar.text_input(
        "OPENAI_KEY",
        value=openai_key,
        help="See https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key for more info.",
        type="password",
    )
    st_openai_model = st.sidebar.text_input(
        "OpenAI model for text synthesis",
        value=os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo-instruct"),
        help="See more here: https://platform.openai.com/docs/models/",
    )
    return (
        openai_api_type,
        st_openai_api_base,
        st_deployment_id,
        st_openai_version,
        st_openai_key,
        st_openai_model,
    )


if st_operator == "mask":
    st_number_of_chars = st.sidebar.number_input(
        "number of chars", value=st_number_of_chars, min_value=0, max_value=100
    )
    st_mask_char = st.sidebar.text_input("Mask character", value=st_mask_char, max_chars=1)
elif st_operator == "encrypt":
    st_encrypt_key = st.sidebar.text_input("AES key", value=st_encrypt_key)
elif st_operator == "synthesize":
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

st_threshold_default = 0.30 if st_recognition_profile == "Dutch Legal Strict" else 0.35
st_threshold = st.sidebar.slider(
    label="Acceptance threshold",
    min_value=0.0,
    max_value=1.0,
    value=st_threshold_default,
    help="Define the threshold for accepting a detection as PII.",
)

st_return_decision_process = st.sidebar.checkbox(
    "Add analysis explanations to findings",
    value=False,
    help=(
        "Add the decision process to the output table. More information: "
        "https://microsoft.github.io/presidio/analyzer/decision_process/"
    ),
)

st_deny_allow_expander = st.sidebar.expander("Allowlists and denylists", expanded=False)
with st_deny_allow_expander:
    st_allow_list = st_tags(label="Add words to the allowlist", text="Enter word and press enter.")
    st.caption("Allowlists contain words that are not considered PII, but are detected as such.")
    st_deny_list = st_tags(label="Add words to the denylist", text="Enter word and press enter.")
    st.caption("Denylists contain words that are considered PII, but are not detected as such.")


# Main panel
with st.expander("About this demo", expanded=False):
    st.info(
        """
        Presidio is an open source customizable framework for PII detection and de-identification.

        [Code](https://aka.ms/presidio) | [Tutorial](https://microsoft.github.io/presidio/tutorial/) |
        [Installation](https://microsoft.github.io/presidio/installation/) |
        [FAQ](https://microsoft.github.io/presidio/faq/) |
        [Feedback](https://forms.office.com/r/9ufyYjfDaY)
        """
    )
    st.info(
        """
        SolidPrivacy Scrub extends the demo with Dutch/EU and Dutch legal recognizers.
        For legal/confidential material, use fake documents in this public Space.
        The recognizer pack is designed to be local/offline compatible for a future desktop/MSI version.
        """
    )

analyzer_load_state = st.info("Starting Presidio analyzer...")
analyzer_load_state.empty()

if st_recognition_profile == "Dutch Legal Strict":
    st.info(
        "Dutch Legal Strict mode is active. The app adds Dutch/EU recognizers plus legal/matter identifiers: "
        "zaaknummer, rolnummer, rekestnummer, parketnummer, dossiernummer, cliëntnummer, CJIB, ECLI, "
        "legal party references and court/authority references. Always review the editable replacement table."
    )
elif st_recognition_profile == "Dutch / EU":
    st.info(
        "Dutch / EU mode is active. The app adds Dutch pattern recognizers for BSN, postcode, KvK, BTW/VAT, "
        "Dutch IBAN, Dutch phone numbers, addresses, license plates, rijbewijs-style numbers and BIG numbers. "
        "Always review the editable replacement table before exporting."
    )

# Read default text
with open("demo_text.txt", encoding="utf-8") as f:
    demo_text = f.readlines()

st.subheader("Document input")
uploaded_file = st.file_uploader(
    "Upload a .txt, .docx, or text-based .pdf file",
    type=["txt", "docx", "pdf"],
    help="For legal/confidential material, use only approved environments. This public demo should be used with fake or test documents.",
)

uploaded_file_type = None
input_text = "".join(demo_text)

if st_recognition_profile == "Dutch Legal Strict":
    with st.expander("Use a fake Dutch legal test example", expanded=False):
        example_names = get_example_names()
        if LEGAL_EXAMPLES_IMPORT_ERROR is not None:
            st.warning(
                "Could not import legal_test_examples.py. Showing embedded fallback examples. "
                "Check that legal_test_examples.py exists in the Space root. "
                f"Import error: {LEGAL_EXAMPLES_IMPORT_ERROR}"
            )
        elif not example_names:
            st.warning(
                "No legal examples were loaded from legal_test_examples.py. "
                "Check that TEST_CASES contains examples and that get_example_names() returns names."
            )
            example_names = list(EMBEDDED_LEGAL_TEST_CASES.keys())

        sample_name = st.selectbox(
            "Load synthetic legal example",
            ["Do not load a test example"] + example_names,
            index=0,
        )
        if sample_name != "Do not load a test example" and uploaded_file is None:
            example_text = get_example_text(sample_name)
            if not example_text and sample_name in EMBEDDED_LEGAL_TEST_CASES:
                example_text = EMBEDDED_LEGAL_TEST_CASES[sample_name]
            input_text = example_text
            st.caption("Loaded synthetic example text. No real personal data is included.")

if uploaded_file is not None:
    try:
        input_text, uploaded_file_type = uploaded_file_to_text(uploaded_file)
        st.success(f"Loaded file: {uploaded_file.name}")
    except Exception as upload_error:
        st.error(f"Could not read uploaded file: {upload_error}")

col1, col2 = st.columns(2)
col1.subheader("Input")
st_text = col1.text_area(
    label="Enter text or review extracted document text",
    value=input_text,
    height=400,
    key="text_input",
)

try:
    all_supported_entities = list(get_supported_entities(*analyzer_params))
    general_dutch_entities = set(get_dutch_general_entity_names())
    legal_dutch_entities = set(get_dutch_legal_entity_names())
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

    st_entities_expander = st.sidebar.expander("Choose entities to look for")
    st_entities = st_entities_expander.multiselect(
        label="Which entities to look for?",
        options=all_supported_entities,
        default=default_entities,
        help=(
            "Dutch / EU mode adds recognizers such as NL_BSN, NL_POSTCODE, NL_KVK_NUMBER, "
            "NL_VAT_NUMBER, NL_IBAN and NL_PHONE_NUMBER. Dutch Legal Strict additionally adds "
            "NL_ECLI, NL_LEGAL_CASE_NUMBER, NL_PARKETNUMMER, NL_DOSSIER_NUMBER, NL_CLIENT_NUMBER, "
            "plus contextual references such as NL_CLIENT_REFERENCE, NL_SCHOOL_REFERENCE, "
            "NL_INVOICE_NUMBER, NL_CASE_REFERENCE and related legal/admin IDs."
        ),
    )

    analyzer_load_state = st.info("Starting Presidio analyzer...")
    analyzer = analyzer_engine(*analyzer_params)
    analyzer_load_state.empty()

    # The current demo uses English NER models. Dutch/EU pattern recognizers are
    # registered under language="en" so they can run without a separate Dutch NLP model.
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
        with col2:
            st.subheader("Output")
            st_anonymize_results = anonymize(
                text=st_text,
                operator=st_operator,
                mask_char=st_mask_char,
                number_of_chars=st_number_of_chars,
                encrypt_key=st_encrypt_key,
                analyze_results=st_analyze_results,
            )
            st.text_area(label="De-identified", value=st_anonymize_results.text, height=400)

        _, report_rows = build_placeholder_replacements(st_text, st_analyze_results)

        st.divider()
        st.subheader("Review replacement table before export")
        st.caption(
            "Untick false positives, change placeholders, add your own word pairs, "
            "and tick Remember for pairs you want to reuse in future documents."
        )

        remembered_rows = load_remembered_replacements()
        default_editor_rows = []
        seen_find_values = set()

        for row in remembered_rows:
            find_text = str(row.get("find", "")).strip()
            replace_with = str(row.get("replace_with", "")).strip()
            if not find_text or not replace_with:
                continue
            default_editor_rows.append(
                {
                    "include": row.get("include", True),
                    "remember": row.get("remember", True),
                    "find": find_text,
                    "replace_with": replace_with,
                    "entity_type": row.get("entity_type", "REMEMBERED"),
                    "score": None,
                }
            )
            seen_find_values.add(find_text)

        for row in report_rows:
            find_text = str(row.get("detected_text", "")).strip()
            if not find_text or find_text in seen_find_values:
                continue
            default_editor_rows.append(
                {
                    "include": True,
                    "remember": False,
                    "find": find_text,
                    "replace_with": row.get("placeholder", ""),
                    "entity_type": row.get("entity_type", ""),
                    "score": row.get("score", None),
                }
            )

        if not default_editor_rows:
            default_editor_rows = [
                {
                    "include": True,
                    "remember": False,
                    "find": "",
                    "replace_with": "",
                    "entity_type": "MANUAL",
                    "score": None,
                }
            ]

        replacement_editor_df = pd.DataFrame(default_editor_rows)
        edited_replacements_df = st.data_editor(
            replacement_editor_df,
            hide_index=True,
            num_rows="dynamic",
            use_container_width=True,
            column_order=["include", "remember", "find", "replace_with", "entity_type", "score"],
            column_config={
                "include": st.column_config.CheckboxColumn(
                    "Use", help="Untick to exclude this replacement from the export.", default=True
                ),
                "remember": st.column_config.CheckboxColumn(
                    "Remember", help="Save this replacement pair for future documents/sessions.", default=False
                ),
                "find": st.column_config.TextColumn(
                    "Find text", help="The exact text that should be replaced."
                ),
                "replace_with": st.column_config.TextColumn(
                    "Replace with", help="The placeholder to insert."
                ),
                "entity_type": st.column_config.TextColumn(
                    "Entity type", help="Presidio entity type or MANUAL."
                ),
                "score": st.column_config.NumberColumn(
                    "Score", help="Presidio confidence score, if available.", format="%.3f"
                ),
            },
            key="replacement_editor",
        )

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
            return str(value).strip().lower() in ("true", "1", "yes", "y", "checked")

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
                }
            )

        st.info(f"{len(edited_replacements)} replacement pair(s) will be applied to the exports.")

        export_text = apply_replacements_to_text(st_text, edited_replacements)
        with st.expander("Preview anonymized text generated from edited table", expanded=False):
            st.text_area(label="Preview", value=export_text, height=300, key="edited_export_preview")

        st.subheader("Remember reusable replacements")
        remember_rows_to_save = []
        for _, row in edited_replacements_df.iterrows():
            include = safe_bool(row.get("include", False))
            remember = safe_bool(row.get("remember", False))
            find_text = safe_cell(row.get("find", ""))
            replace_text = safe_cell(row.get("replace_with", ""))
            entity_type = safe_cell(row.get("entity_type", "REMEMBERED")) or "REMEMBERED"
            if include and remember and find_text and replace_text:
                remember_rows_to_save.append(
                    {"find": find_text, "replace_with": replace_text, "entity_type": entity_type}
                )

        memory_col1, memory_col2 = st.columns(2)
        with memory_col1:
            if st.button("Save remembered replacements"):
                saved_count = save_remembered_replacements(remember_rows_to_save)
                st.success(f"Saved {saved_count} remembered replacement pair(s).")
                st.info(f"Memory file: {get_memory_file_path()}")
        with memory_col2:
            if st.button("Clear remembered replacements"):
                clear_remembered_replacements()
                st.warning("Remembered replacements cleared.")

        st.subheader("Export anonymized files")
        if uploaded_file is not None:
            st.info(f"Uploaded file detected for export: {uploaded_file.name}")
        else:
            st.info("No uploaded file detected for export. Exporting from text area only.")

        st.download_button(
            label="Download anonymized text (.txt)",
            data=export_text.encode("utf-8"),
            file_name="anonymized_text.txt",
            mime="text/plain",
            key="download_txt",
        )
        st.download_button(
            label="Download replacement table (.csv)",
            data=replacement_report_csv(edited_report_rows),
            file_name="replacement_table.csv",
            mime="text/csv",
            key="download_csv",
        )
        st.download_button(
            label="Download scrub report (.txt)",
            data=scrub_report_txt(
                edited_report_rows,
                profile=st_recognition_profile,
                source_filename=uploaded_file.name if uploaded_file is not None else None,
            ),
            file_name="scrub_report.txt",
            mime="text/plain",
            key="download_scrub_report",
        )

        try:
            if uploaded_file is not None and uploaded_file.name.lower().endswith(".docx"):
                docx_bytes = anonymized_docx_from_original(uploaded_file, edited_replacements)
                docx_filename = "anonymized_" + uploaded_file.name
            else:
                docx_bytes = docx_from_text(export_text)
                docx_filename = "anonymized_text.docx"
            st.download_button(
                label="Download anonymized Word file (.docx)",
                data=docx_bytes,
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_docx",
            )
        except Exception as docx_error:
            st.error(f"Could not create DOCX export: {docx_error}")

        try:
            st.download_button(
                label="Download anonymized PDF (.pdf)",
                data=pdf_from_text(export_text),
                file_name="anonymized_text.pdf",
                mime="application/pdf",
                key="download_pdf",
            )
        except Exception as pdf_error:
            st.error(f"Could not create PDF export: {pdf_error}")

    elif st_operator == "synthesize":
        with col2:
            st.subheader("OpenAI Generated output")
            fake_data = create_fake_data(st_text, st_analyze_results, open_ai_params)
            st.text_area(label="Synthetic data", value=fake_data, height=400)
    else:
        st.subheader("Highlighted")
        annotated_tokens = annotate(text=st_text, analyze_results=st_analyze_results)
        annotated_text(*annotated_tokens)

    st.subheader("Findings" if not st_return_decision_process else "Findings with decision factors")
    if st_analyze_results:
        df = pd.DataFrame.from_records([r.to_dict() for r in st_analyze_results])
        df["text"] = [st_text[res.start : res.end] for res in st_analyze_results]
        df_subset = df[["entity_type", "text", "start", "end", "score"]].rename(
            {
                "entity_type": "Entity type",
                "text": "Text",
                "start": "Start",
                "end": "End",
                "score": "Confidence",
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
        st.text("No findings")

except Exception as e:
    print(e)
    traceback.print_exc()
    st.error(e)

components.html(""" """)
