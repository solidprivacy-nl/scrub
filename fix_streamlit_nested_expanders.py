"""Startup hotfix for Streamlit nested expander limitation.

Streamlit does not allow an expander inside another expander. v9 placed the
'Woordenlijsten' section inside 'Geavanceerde instellingen'. This script patches
that small block before the app starts, without changing recognizer behaviour.
"""

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")

old = '''    st_deny_allow_expander = st.expander("Woordenlijsten", expanded=False)
    with st_deny_allow_expander:
        st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
        st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
'''

new = '''    st.markdown("**Woordenlijsten**")
    st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
    st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
'''

if old in text:
    APP_FILE.write_text(text.replace(old, new), encoding="utf-8")
