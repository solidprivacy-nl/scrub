from pathlib import Path
import ast
import subprocess
import textwrap

path = Path("presidio_streamlit.py")
text = path.read_text(encoding="utf-8")
original = subprocess.check_output(
    ["git", "show", "d54eb06f9c6fea7c1f36cdb082b475c0d4666507:presidio_streamlit.py"],
    text=True,
)

original_controls_start = original.index("st.sidebar.header(APP_TITLE)")
original_controls_end = original.index("st.title(APP_TITLE)", original_controls_start)
expert_controls = original[original_controls_start:original_controls_end].rstrip()

start = text.index("st.title(APP_TITLE)", text.index("allow_other_models"))
end_marker = 'if is_premium_expert:\n    with st.expander("Over deze app"'
end = text.index(end_marker, start)

new_controls = '''st.title(APP_TITLE)
st.subheader(APP_SUBTITLE)
st.write(APP_INTRO)
st.info(LOCAL_PROCESSING_NOTE)

workflow_col, presentation_col = st.columns([1.2, 1.0])
with workflow_col:
    workflow_choice = st.radio(
        "Werkstroom",
        ["Anonimiseren", "Terugzetten"],
        horizontal=True,
        key="premium_workflow_choice",
        help="Anonimiseren maakt een veilig deelbare versie. Terugzetten herstelt lokaal originele waarden met een Scrub Key.",
    )
with presentation_col:
    presentation_choice = st.radio(
        "Weergave",
        ["Standaard", "Expert"],
        horizontal=True,
        key="premium_presentation_choice",
        help="Standaard toont alleen de kernworkflow. Expert ontsluit technische instellingen en extra controlehulpen.",
    )

premium_workflow = Workflow.ANONYMIZE if workflow_choice == "Anonimiseren" else Workflow.REINSERT
premium_presentation = PresentationMode.STANDARD if presentation_choice == "Standaard" else PresentationMode.EXPERT
premium_state = synchronize_shell_choices(
    st.session_state,
    workflow=premium_workflow,
    presentation_mode=premium_presentation,
)
is_premium_standard = premium_presentation is PresentationMode.STANDARD
is_premium_expert = premium_presentation is PresentationMode.EXPERT

if premium_workflow is Workflow.REINSERT:
    render_reinsert_mode()
    st.stop()

if is_premium_expert:
'''
new_controls += textwrap.indent(expert_controls, "    ")
new_controls += '''
    st.session_state["_premium_profile_label"] = profile_label
    st.session_state["_premium_operator_value"] = st_operator
    st.session_state["_premium_threshold"] = float(st_threshold)
    st.session_state["_premium_return_decision_process"] = bool(st_return_decision_process)
    st.session_state["_premium_mask_char"] = st_mask_char
    st.session_state["_premium_number_of_chars"] = int(st_number_of_chars)
    st.session_state["_premium_encrypt_key"] = st_encrypt_key
    st.session_state["_premium_allow_list"] = list(st_allow_list or [])
    st.session_state["_premium_deny_list"] = list(st_deny_list or [])
    st.session_state["_premium_analyzer_params"] = tuple(analyzer_params)
else:
    profile_options = list(PROFILE_OPTIONS.keys())
    profile_label = st.session_state.get("_premium_profile_label", profile_options[1])
    if profile_label not in profile_options:
        profile_label = profile_options[1]
    st_recognition_profile = PROFILE_OPTIONS[profile_label]

    st_operator = st.session_state.get("_premium_operator_value", "replace")
    if st_operator not in OPERATOR_LABELS:
        st_operator = "replace"

    st_threshold_default = configured_threshold(st_recognition_profile)
    st_threshold = float(st.session_state.get("_premium_threshold", st_threshold_default))
    st_return_decision_process = bool(st.session_state.get("_premium_return_decision_process", False))
    st_mask_char = str(st.session_state.get("_premium_mask_char", "*"))
    st_number_of_chars = int(st.session_state.get("_premium_number_of_chars", 15))
    st_encrypt_key = str(st.session_state.get("_premium_encrypt_key", "WmZq4t7w!z%C&F)J"))
    st_allow_list = list(st.session_state.get("_premium_allow_list", []))
    st_deny_list = list(st.session_state.get("_premium_deny_list", []))
    analyzer_params = tuple(
        st.session_state.get(
            "_premium_analyzer_params",
            ("flair", "flair/ner-english-large", "", ""),
        )
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

'''

text = text[:start] + new_controls + text[end:]
path.write_text(text, encoding="utf-8")
try:
    ast.parse(text)
except SyntaxError as exc:
    print(f"SYNTAX_ERROR line={exc.lineno} offset={exc.offset}: {exc.msg}")
    if exc.lineno:
        lines = text.splitlines()
        lo = max(0, exc.lineno - 6)
        hi = min(len(lines), exc.lineno + 5)
        for number in range(lo, hi):
            print(f"{number + 1:04d}: {lines[number]}")
    raise

Path("tools/_repair_premium_app_shell.py").unlink()
Path(".github/workflows/premium-app-shell-repair.yml").unlink()
