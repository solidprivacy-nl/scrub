"""Startup compatibility patches for the Streamlit app.

This script runs before Streamlit starts in the Docker container. It applies small
idempotent source patches that keep the Hugging Face Space usable while larger UI
refactors are being staged.

Patches currently applied:
- v9: remove nested Streamlit expander usage for Woordenlijsten.
- v12.1: add a user-facing review status model to the replacement table.
"""

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")


def replace_once(source: str, old: str, new: str) -> str:
    if old in source and new not in source:
        return source.replace(old, new, 1)
    return source


# v9 compatibility: Streamlit does not allow an expander inside another expander.
nested_old = '''    st_deny_allow_expander = st.expander("Woordenlijsten", expanded=False)
    with st_deny_allow_expander:
        st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
        st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
'''

nested_new = '''    st.markdown("**Woordenlijsten**")
    st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
    st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
'''

text = replace_once(text, nested_old, nested_new)

# v12.1: import review-status helpers.
text = replace_once(
    text,
    'from display_labels_nl import entity_label, source_label, confidence_label\n',
    'from display_labels_nl import entity_label, source_label, confidence_label\n'
    'from review_status import review_status_for_source, review_status_label, review_status_order\n',
)

# v12.1: add review status fields to remembered rows.
text = replace_once(
    text,
    '''                    "source_label": source_label("remembered"),
                    "source": "remembered",
                    "reason": "Opgeslagen herbruikbare vervanging",
''',
    '''                    "source_label": source_label("remembered"),
                    "source": "remembered",
                    "review_status": review_status_for_source("remembered", entity_type, None),
                    "review_status_label": review_status_label(review_status_for_source("remembered", entity_type, None)),
                    "review_order": review_status_order(review_status_for_source("remembered", entity_type, None)),
                    "reason": "Opgeslagen herbruikbare vervanging",
''',
)

# v12.1: add review status fields to automatically detected rows.
text = replace_once(
    text,
    '''                    "source_label": source_label("detected"),
                    "source": "detected",
                    "reason": "Automatisch herkend",
''',
    '''                    "source_label": source_label("detected"),
                    "source": "detected",
                    "review_status": review_status_for_source("detected", entity_type, score),
                    "review_status_label": review_status_label(review_status_for_source("detected", entity_type, score)),
                    "review_order": review_status_order(review_status_for_source("detected", entity_type, score)),
                    "reason": "Automatisch herkend",
''',
)

# v12.1: add review status fields to candidate rows.
text = replace_once(
    text,
    '''                    "source_label": source_label("candidate"),
                    "source": "candidate",
                    "reason": candidate.get("reason", "Mogelijke gemiste waarde"),
''',
    '''                    "source_label": source_label("candidate"),
                    "source": "candidate",
                    "review_status": review_status_for_source("candidate", entity_type, score),
                    "review_status_label": review_status_label(review_status_for_source("candidate", entity_type, score)),
                    "review_order": review_status_order(review_status_for_source("candidate", entity_type, score)),
                    "reason": candidate.get("reason", "Mogelijke gemiste waarde"),
''',
)

# v12.1: add review status fields to empty/manual fallback rows.
text = replace_once(
    text,
    '''                    "source_label": source_label("manual"),
                    "source": "manual",
                    "reason": "Handmatige vervangingsregel",
''',
    '''                    "source_label": source_label("manual"),
                    "source": "manual",
                    "review_status": review_status_for_source("manual", "MANUAL", None),
                    "review_status_label": review_status_label(review_status_for_source("manual", "MANUAL", None)),
                    "review_order": review_status_order(review_status_for_source("manual", "MANUAL", None)),
                    "reason": "Handmatige vervangingsregel",
''',
)

# v12.1: sort review rows and show a compact status summary above the editor.
text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        edited_replacements_df = st.data_editor(
''',
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        if "review_order" in replacement_editor_df.columns:
            replacement_editor_df = replacement_editor_df.sort_values(
                by=["review_order", "type_label", "find"], kind="stable"
            ).reset_index(drop=True)
        if "review_status_label" in replacement_editor_df.columns:
            status_counts = replacement_editor_df["review_status_label"].value_counts().to_dict()
            status_parts = [f"{label}: {count}" for label, count in status_counts.items()]
            if status_parts:
                st.caption("Reviewstatus: " + " · ".join(status_parts))
        edited_replacements_df = st.data_editor(
''',
)

# v12.1: make status visible in the editor.
text = replace_once(
    text,
    '''                "include",
                "remember",
                "find",
''',
    '''                "include",
                "remember",
                "review_status_label",
                "find",
''',
)

text = replace_once(
    text,
    '''                "find": st.column_config.TextColumn(
                    "Gevonden tekst", help="Exacte tekst die vervangen moet worden."
                ),
''',
    '''                "review_status_label": st.column_config.TextColumn(
                    "Status", help="Reviewstatus: automatisch vervangen, controle nodig, handmatig of onthouden."
                ),
                "find": st.column_config.TextColumn(
                    "Gevonden tekst", help="Exacte tekst die vervangen moet worden."
                ),
''',
)

# v12.1: include status in the scrub report rows where downstream exporters keep it.
text = replace_once(
    text,
    '''                    "source": safe_cell(row.get("source", "")),
                    "reason": safe_cell(row.get("reason", "")),
''',
    '''                    "source": safe_cell(row.get("source", "")),
                    "review_status": safe_cell(row.get("review_status", "")),
                    "review_status_label": safe_cell(row.get("review_status_label", "")),
                    "reason": safe_cell(row.get("reason", "")),
''',
)

APP_FILE.write_text(text, encoding="utf-8")
