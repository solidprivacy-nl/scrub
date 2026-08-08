from pathlib import Path
import ast


PATH = Path("presidio_streamlit.py")
text = PATH.read_text(encoding="utf-8")

old_import = '''from premium_streamlit_state import (
    cache_analysis_results,
    get_cached_analysis_results,
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    processing_generation,
    set_stage_summary,
    synchronize_processing_generation,
    synchronize_shell_choices,
)
'''
new_import = '''from premium_streamlit_state import (
    ALLOW_LIST_KEY,
    DENY_LIST_KEY,
    analyzer_model_label,
    cache_analysis_results,
    get_cached_analysis_results,
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    persist_processing_settings,
    processing_generation,
    set_stage_summary,
    stored_analyzer_params,
    stored_entities,
    stored_operator_value,
    stored_profile_label,
    stored_string_list,
    stored_threshold,
    synchronize_processing_generation,
    synchronize_shell_choices,
)
'''
if old_import not in text:
    raise SystemExit("premium_streamlit_state import block not found")
text = text.replace(old_import, new_import, 1)

old_shell = '''premium_workflow = Workflow.ANONYMIZE if workflow_choice == "Anonimiseren" else Workflow.REINSERT
premium_presentation = PresentationMode.STANDARD if presentation_choice == "Standaard" else PresentationMode.EXPERT
premium_state = synchronize_shell_choices(
    st.session_state,
    workflow=premium_workflow,
    presentation_mode=premium_presentation,
)
is_premium_standard = premium_presentation is PresentationMode.STANDARD
is_premium_expert = premium_presentation is PresentationMode.EXPERT
'''
new_shell = '''premium_workflow = Workflow.ANONYMIZE if workflow_choice == "Anonimiseren" else Workflow.REINSERT
premium_presentation = PresentationMode.STANDARD if presentation_choice == "Standaard" else PresentationMode.EXPERT
previous_premium_state = get_core_flow_state(st.session_state)
presentation_mode_changed = previous_premium_state.presentation_mode is not premium_presentation
premium_state = synchronize_shell_choices(
    st.session_state,
    workflow=premium_workflow,
    presentation_mode=premium_presentation,
)
is_premium_standard = premium_presentation is PresentationMode.STANDARD
is_premium_expert = premium_presentation is PresentationMode.EXPERT
entering_expert = presentation_mode_changed and is_premium_expert
entering_standard = presentation_mode_changed and is_premium_standard
'''
if old_shell not in text:
    raise SystemExit("premium shell synchronization block not found")
text = text.replace(old_shell, new_shell, 1)

settings_start = text.index('if is_premium_expert:\n    st.sidebar.header(APP_TITLE)')
settings_end = text.index('\nif is_premium_expert:\n    with st.expander("Over deze app"', settings_start)
new_settings = '''if is_premium_expert:
    st.sidebar.header(APP_TITLE)
    st.sidebar.caption(APP_SUBTITLE)

    profile_options = list(PROFILE_OPTIONS.keys())
    profile_label = stored_profile_label(st.session_state, profile_options)
    stored_operator = stored_operator_value(st.session_state, OPERATOR_LABELS.keys())
    if entering_expert:
        st.session_state["premium_profile_expert_widget"] = profile_label
        st.session_state["premium_operator_expert_widget"] = OPERATOR_LABELS[stored_operator]

    profile_label = st.sidebar.selectbox(
        "Controlemodus",
        profile_options,
        index=profile_options.index(profile_label),
        help=PROFILE_HELP,
        key="premium_profile_expert_widget",
    )
    st_recognition_profile = PROFILE_OPTIONS[profile_label]
    with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False):
        st.info(configured_description(st_recognition_profile))

    stored_operator_label = OPERATOR_LABELS[stored_operator]
    operator_values = list(OPERATOR_LABELS.values())
    operator_label = st.sidebar.selectbox(
        "Manier van vervangen",
        operator_values,
        index=operator_values.index(stored_operator_label),
        help=OPERATOR_HELP,
        key="premium_operator_expert_widget",
    )
    st_operator = OPERATOR_LABEL_TO_VALUE[operator_label]

    st_threshold_default = configured_threshold(st_recognition_profile)
    threshold_value = stored_threshold(st.session_state, st_threshold_default)
    if entering_expert:
        st.session_state["premium_threshold_expert_widget"] = threshold_value

    with st.sidebar.expander("Geavanceerde instellingen", expanded=False):
        st.caption(ADVANCED_SETTINGS_HELP)
        model_help_text = (
            "Kies het NER-model dat naast regelherkenning wordt gebruikt. "
            "De Nederlandse profielherkenners voor zorg en juridisch zijn regelgebaseerd."
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

        saved_analyzer_params = stored_analyzer_params(
            st.session_state,
            ("flair", "flair/ner-english-large", "", ""),
        )
        saved_model_label = analyzer_model_label(saved_analyzer_params, model_list)
        if entering_expert:
            st.session_state["premium_model_expert_widget"] = saved_model_label
        selected_model_label = st.selectbox(
            "Technisch NER-model",
            model_list,
            index=model_list.index(saved_model_label),
            help=model_help_text,
            key="premium_model_expert_widget",
        )

        st_model_package = selected_model_label.split("/")[0]
        st_model = (
            selected_model_label
            if st_model_package.lower() not in ("spacy", "stanza", "huggingface")
            else "/".join(selected_model_label.split("/")[1:])
        )

        if selected_model_label == "Other":
            custom_packages = ["spaCy", "stanza", "Flair", "HuggingFace"]
            saved_package = str(saved_analyzer_params[0])
            custom_package_default = saved_package if saved_package in custom_packages else custom_packages[0]
            custom_model_default = str(saved_analyzer_params[1])
            if entering_expert:
                st.session_state["premium_custom_model_package_widget"] = custom_package_default
                st.session_state["premium_custom_model_name_widget"] = custom_model_default
            st_model_package = st.selectbox(
                "NER-modelpakket",
                options=custom_packages,
                index=custom_packages.index(custom_package_default),
                key="premium_custom_model_package_widget",
            )
            st_model = st.text_input(
                "NER-modelnaam",
                value=custom_model_default,
                key="premium_custom_model_name_widget",
            )

        if selected_model_label == "Azure AI Language":
            saved_is_azure = analyzer_model_label(saved_analyzer_params, ["Azure AI Language", "Other"]) == "Azure AI Language"
            saved_ta_key = str(saved_analyzer_params[2]) if saved_is_azure else os.getenv("TA_KEY", "")
            saved_ta_endpoint = str(saved_analyzer_params[3]) if saved_is_azure else os.getenv("TA_ENDPOINT", default="")
            if entering_expert:
                st.session_state["premium_ta_key_widget"] = saved_ta_key
                st.session_state["premium_ta_endpoint_widget"] = saved_ta_endpoint
            st_ta_key = st.text_input(
                "Azure AI Language key",
                value=saved_ta_key,
                type="password",
                key="premium_ta_key_widget",
            )
            st_ta_endpoint = st.text_input(
                "Azure AI Language endpoint",
                value=saved_ta_endpoint,
                key="premium_ta_endpoint_widget",
            )

        st_threshold = st.slider(
            label="Gevoeligheid van herkenning",
            min_value=0.0,
            max_value=1.0,
            value=threshold_value,
            help="Lagere waarde = meer gevonden gegevens, maar ook meer kans op fout-positieven.",
            key="premium_threshold_expert_widget",
        )
        stored_return_decision = bool(st.session_state.get("_premium_return_decision_process", False))
        stored_mask_char = str(st.session_state.get("_premium_mask_char", "*"))
        stored_number_of_chars = int(st.session_state.get("_premium_number_of_chars", 15))
        stored_encrypt_key = str(st.session_state.get("_premium_encrypt_key", "WmZq4t7w!z%C&F)J"))
        if entering_expert:
            st.session_state["premium_return_decision_widget"] = stored_return_decision
            st.session_state["premium_mask_char_widget"] = stored_mask_char
            st.session_state["premium_number_chars_widget"] = stored_number_of_chars
            st.session_state["premium_encrypt_key_widget"] = stored_encrypt_key
        st_return_decision_process = st.checkbox(
            "Toon technische beslisinformatie",
            value=stored_return_decision,
            help="Voegt technische uitlegvelden toe aan de resultatentabel.",
            key="premium_return_decision_widget",
        )
        st_mask_char = st.text_input(
            "Maskeringsteken", value=stored_mask_char, max_chars=1, key="premium_mask_char_widget"
        )
        st_number_of_chars = st.number_input(
            "Aantal te maskeren tekens",
            value=stored_number_of_chars,
            min_value=0,
            max_value=100,
            key="premium_number_chars_widget",
        )
        st_encrypt_key = st.text_input(
            "AES-sleutel", value=stored_encrypt_key, key="premium_encrypt_key_widget"
        )

        st.markdown("**Woordenlijsten**")
        st_allow_list = st_tags(
            label="Niet vervangen",
            text="Voer woord in en druk op Enter.",
            value=stored_string_list(st.session_state, ALLOW_LIST_KEY),
        )
        st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
        st_deny_list = st_tags(
            label="Extra controleren",
            text="Voer woord in en druk op Enter.",
            value=stored_string_list(st.session_state, DENY_LIST_KEY),
        )
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
else:
    profile_options = list(PROFILE_OPTIONS.keys())
    profile_label = stored_profile_label(st.session_state, profile_options)
    st_recognition_profile = PROFILE_OPTIONS[profile_label]

    st_operator = stored_operator_value(st.session_state, OPERATOR_LABELS.keys())
    if not standard_operator_is_supported(st_operator):
        st.warning(
            "Deze geavanceerde manier van vervangen is alleen beschikbaar in Expert. "
            "Schakel terug naar Expert om deze instelling te behouden of aan te passen."
        )
        st.caption("Standaard wijzigt deze Expert-instelling niet automatisch.")
        st.stop()

    st_threshold_default = configured_threshold(st_recognition_profile)
    st_threshold = stored_threshold(st.session_state, st_threshold_default)
    st_return_decision_process = bool(st.session_state.get("_premium_return_decision_process", False))
    st_mask_char = str(st.session_state.get("_premium_mask_char", "*"))
    st_number_of_chars = int(st.session_state.get("_premium_number_of_chars", 15))
    st_encrypt_key = str(st.session_state.get("_premium_encrypt_key", "WmZq4t7w!z%C&F)J"))
    st_allow_list = stored_string_list(st.session_state, ALLOW_LIST_KEY)
    st_deny_list = stored_string_list(st.session_state, DENY_LIST_KEY)
    analyzer_params = stored_analyzer_params(
        st.session_state,
        ("flair", "flair/ner-english-large", "", ""),
    )
    open_ai_params = None

    if st_operator == "synthesize":
        if os.getenv("OPENAI_TYPE", default="openai") == "Azure":
            openai_api_type = "azure"
            st_openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT", default="")
            openai_key = os.getenv("AZURE_OPENAI_KEY", default="")
            st_deployment_id = os.getenv("AZURE_OPENAI_DEPLOYMENT", default="")
            st_openai_version = os.getenv("OPENAI_API_VERSION", default="2023-05-15")
        else:
            openai_api_type = "openai"
            st_openai_version = st_openai_api_base = None
            st_deployment_id = ""
            openai_key = os.getenv("OPENAI_KEY", default="")
        open_ai_params = OpenAIParams(
            openai_key=openai_key,
            model=os.getenv("OPENAI_MODEL", default="gpt-3.5-turbo-instruct"),
            api_base=st_openai_api_base,
            deployment_id=st_deployment_id,
            api_version=st_openai_version,
            api_type=openai_api_type,
        )

persist_processing_settings(
    st.session_state,
    profile_label=profile_label,
    operator=st_operator,
    threshold=st_threshold,
    allow_list=st_allow_list,
    deny_list=st_deny_list,
    analyzer_params=analyzer_params,
)
st.session_state["_premium_return_decision_process"] = bool(st_return_decision_process)
st.session_state["_premium_mask_char"] = st_mask_char
st.session_state["_premium_number_of_chars"] = int(st_number_of_chars)
st.session_state["_premium_encrypt_key"] = st_encrypt_key
'''
text = text[:settings_start] + new_settings + text[settings_end:]

old_standard_profile = '''        if is_premium_standard:
            selected_profile_label = st.selectbox(
                "Controlemodus",
                profile_options,
                index=profile_options.index(profile_label),
                help=PROFILE_HELP,
                key="premium_profile_standard_widget",
            )
'''
new_standard_profile = '''        if is_premium_standard:
            if entering_standard:
                st.session_state["premium_profile_standard_widget"] = profile_label
            selected_profile_label = st.selectbox(
                "Controlemodus",
                profile_options,
                index=profile_options.index(profile_label),
                help=PROFILE_HELP,
                key="premium_profile_standard_widget",
            )
'''
if old_standard_profile not in text:
    raise SystemExit("Standard profile widget block not found")
text = text.replace(old_standard_profile, new_standard_profile, 1)

entity_start = text.index('    if is_premium_expert:\n        with st.sidebar.expander("Te herkennen gegevenstypen"')
entity_end = text.index('\n    current_processing_generation = processing_generation(', entity_start)
new_entities = '''    entity_defaults = stored_entities(
        st.session_state,
        all_supported_entities,
        default_entities,
    )
    if is_premium_expert:
        with st.sidebar.expander("Te herkennen gegevenstypen", expanded=False):
            if entering_expert:
                st.session_state["premium_entities_expert_widget"] = list(entity_defaults)
            st_entities = st.multiselect(
                label="Welke typen gegevens moet Scrub zoeken?",
                options=all_supported_entities,
                default=entity_defaults,
                help="Laat dit standaard staan, tenzij je gericht wilt testen of tunen.",
                key="premium_entities_expert_widget",
            )
    else:
        st_entities = list(entity_defaults)

    persist_processing_settings(
        st.session_state,
        profile_label=profile_label,
        operator=st_operator,
        threshold=st_threshold,
        entities=st_entities,
        allow_list=st_allow_list,
        deny_list=st_deny_list,
        analyzer_params=analyzer_params,
    )
'''
text = text[:entity_start] + new_entities + text[entity_end:]

old_sync = '''    if is_premium_standard and st_operator not in ("highlight", "synthesize"):
        premium_state, processing_inputs_changed = synchronize_processing_generation(
            st.session_state, current_processing_generation
        )
        if processing_inputs_changed:
            st.session_state.pop("_premium_cached_review_rows", None)
        if stage_is_active(premium_state, Stage.ADD):
'''
new_sync = '''    premium_state, processing_inputs_changed = synchronize_processing_generation(
        st.session_state, current_processing_generation
    )
    if processing_inputs_changed:
        st.session_state.pop("_premium_cached_review_rows", None)

    if is_premium_standard and st_operator not in ("highlight", "synthesize"):
        if stage_is_active(premium_state, Stage.ADD):
'''
if old_sync not in text:
    raise SystemExit("processing synchronization block not found")
text = text.replace(old_sync, new_sync, 1)

ast.parse(text)
PATH.write_text(text, encoding="utf-8")
print("premium presentation-state repair applied and syntax-valid")
