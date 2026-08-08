from pathlib import Path
import ast

path = Path("presidio_streamlit.py")
text = path.read_text(encoding="utf-8")

old_import = "from premium_app_shell import stage_is_active\n"
new_import = "from premium_app_shell import stage_is_active, standard_operator_is_supported\n"
if old_import in text:
    text = text.replace(old_import, new_import, 1)
elif new_import not in text:
    raise SystemExit("premium_app_shell import marker not found")

needle = '''    st_operator = st.session_state.get("_premium_operator_value", "replace")
    if st_operator not in OPERATOR_LABELS:
        st_operator = "replace"

    st_threshold_default = configured_threshold(st_recognition_profile)
'''
replacement = '''    st_operator = st.session_state.get("_premium_operator_value", "replace")
    if st_operator not in OPERATOR_LABELS:
        st_operator = "replace"
    if not standard_operator_is_supported(st_operator):
        st.warning(
            "Deze geavanceerde manier van vervangen is alleen beschikbaar in Expert. "
            "Schakel terug naar Expert om deze instelling te behouden of aan te passen."
        )
        st.caption("Standaard wijzigt deze Expert-instelling niet automatisch.")
        st.stop()

    st_threshold_default = configured_threshold(st_recognition_profile)
'''
if needle not in text:
    raise SystemExit("Standard operator marker not found")
text = text.replace(needle, replacement, 1)

path.write_text(text, encoding="utf-8")
ast.parse(text)
Path("tools/_guard_standard_advanced_operator.py").unlink()
Path(".github/workflows/premium-standard-operator-guard.yml").unlink()
