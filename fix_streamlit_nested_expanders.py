"""Startup compatibility patches for the Streamlit app.

This script runs before Streamlit starts in the Docker container. It applies small
idempotent source patches that keep the Hugging Face Space usable while larger UI
refactors are being staged.

Patches currently applied:
- v9: remove nested Streamlit expander usage for Woordenlijsten.
- v12.1: add a user-facing review status model to the replacement table.
- v12.2: add safe review-focus filters without changing export semantics.
- v12.3: simplify the main review table and move audit details to a technical view.
- v12.4: add clear review guidance text around the review workflow.
- v12.5: show a final review summary before download/export.
- v12.6: show advisory export sanity warnings before download/export.
- v13.1: add local Scrub Key JSON export after review.
- v13.1 hotfix: map Streamlit review-table columns to Scrub Key fields before JSON export.
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

# v13.1: timestamp Scrub Key mappings in the UI/export layer, not inside the pure model.
text = replace_once(
    text,
    'from pathlib import Path\n',
    'from pathlib import Path\nfrom datetime import datetime, timezone\n',
)

# v12.1/v12.2/v12.3/v12.4/v12.5: import review helpers.
text = replace_once(
    text,
    'from display_labels_nl import entity_label, source_label, confidence_label\n',
    'from display_labels_nl import entity_label, source_label, confidence_label\n'
    'from review_status import review_status_for_source, review_status_label, review_status_order\n'
    'from review_filters import REVIEW_FILTER_OPTIONS, FILTER_SHOW_ALL, filter_review_dataframe\n'
    'from review_table_config import main_review_columns, technical_display_columns\n'
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n'
    'from review_summary import build_review_summary, review_summary_markdown\n',
)

# If v12.1 already added review_status but later helpers are not present yet, extend imports only.
text = replace_once(
    text,
    'from review_status import review_status_for_source, review_status_label, review_status_order\n',
    'from review_status import review_status_for_source, review_status_label, review_status_order\n'
    'from review_filters import REVIEW_FILTER_OPTIONS, FILTER_SHOW_ALL, filter_review_dataframe\n'
    'from review_table_config import main_review_columns, technical_display_columns\n'
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n'
    'from review_summary import build_review_summary, review_summary_markdown\n',
)

text = replace_once(
    text,
    'from review_filters import REVIEW_FILTER_OPTIONS, FILTER_SHOW_ALL, filter_review_dataframe\n',
    'from review_filters import REVIEW_FILTER_OPTIONS, FILTER_SHOW_ALL, filter_review_dataframe\n'
    'from review_table_config import main_review_columns, technical_display_columns\n'
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n'
    'from review_summary import build_review_summary, review_summary_markdown\n',
)

text = replace_once(
    text,
    'from review_table_config import main_review_columns, technical_display_columns\n',
    'from review_table_config import main_review_columns, technical_display_columns\n'
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n'
    'from review_summary import build_review_summary, review_summary_markdown\n',
)

text = replace_once(
    text,
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n',
    'from review_guidance import (\n'
    '    REVIEW_INTRO_GUIDANCE,\n'
    '    CANDIDATE_GUIDANCE,\n'
    '    FOCUS_FILTER_GUIDANCE,\n'
    '    TECHNICAL_DETAILS_GUIDANCE,\n'
    '    AI_USAGE_GUIDANCE,\n'
    '    EXPORT_GUIDANCE,\n'
    ')\n'
    'from review_summary import build_review_summary, review_summary_markdown\n',
)

# v12.6: import advisory export sanity helpers without changing export behavior.
text = replace_once(
    text,
    'from review_summary import build_review_summary, review_summary_markdown\n',
    'from review_summary import build_review_summary, review_summary_markdown\n'
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n',
)

# v13.1: import Scrub Key JSON export helpers.
text = replace_once(
    text,
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n',
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n'
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n',
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

# v12.1/v12.2/v12.3/v12.4: sort review rows, show guidance/status summary, focus filters and technical view.
text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        edited_replacements_df = st.data_editor(
''',
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        st.info(REVIEW_INTRO_GUIDANCE)
        with st.expander("Uitleg bij deze controle", expanded=False):
            st.markdown(f"- {CANDIDATE_GUIDANCE}")
            st.markdown(f"- {FOCUS_FILTER_GUIDANCE}")
            st.markdown(f"- {TECHNICAL_DETAILS_GUIDANCE}")
            st.markdown(f"- {AI_USAGE_GUIDANCE}")
        if "review_order" in replacement_editor_df.columns:
            replacement_editor_df = replacement_editor_df.sort_values(
                by=["review_order", "type_label", "find"], kind="stable"
            ).reset_index(drop=True)
        if "review_status_label" in replacement_editor_df.columns:
            status_counts = replacement_editor_df["review_status_label"].value_counts().to_dict()
            status_parts = [f"{label}: {count}" for label, count in status_counts.items()]
            if status_parts:
                st.caption("Reviewstatus: " + " · ".join(status_parts))
        review_filter = st.selectbox(
            "Focusfilter voor controle",
            REVIEW_FILTER_OPTIONS,
            index=REVIEW_FILTER_OPTIONS.index(FILTER_SHOW_ALL),
            help=FOCUS_FILTER_GUIDANCE,
        )
        if review_filter != FILTER_SHOW_ALL:
            focus_df = filter_review_dataframe(replacement_editor_df, review_filter)
            st.caption(f"{len(focus_df)} van {len(replacement_editor_df)} rij(en) zichtbaar in dit focusoverzicht.")
            st.dataframe(
                focus_df[[col for col in ["review_status_label", "find", "replace_with", "type_label", "confidence", "source_label"] if col in focus_df.columns]],
                use_container_width=True,
            )
            st.caption("Pas wijzigingen toe in de volledige vervangtabel hieronder; dit focusoverzicht is alleen bedoeld om sneller te controleren.")
        with st.expander("Technische details bij de vervangtabel", expanded=False):
            st.caption(TECHNICAL_DETAILS_GUIDANCE)
            technical_columns = technical_display_columns(replacement_editor_df.columns)
            if technical_columns:
                st.dataframe(replacement_editor_df[technical_columns], use_container_width=True)
            else:
                st.caption("Geen technische detailkolommen beschikbaar.")
        edited_replacements_df = st.data_editor(
''',
)

# v12.4: if v12.1/v12.2/v12.3 block is already present, add guidance to that block.
text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        if "review_order" in replacement_editor_df.columns:
''',
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        st.info(REVIEW_INTRO_GUIDANCE)
        with st.expander("Uitleg bij deze controle", expanded=False):
            st.markdown(f"- {CANDIDATE_GUIDANCE}")
            st.markdown(f"- {FOCUS_FILTER_GUIDANCE}")
            st.markdown(f"- {TECHNICAL_DETAILS_GUIDANCE}")
            st.markdown(f"- {AI_USAGE_GUIDANCE}")
        if "review_order" in replacement_editor_df.columns:
''',
)

text = replace_once(
    text,
    '            help="Gebruik dit als overzichtsfilter. De volledige vervangtabel hieronder blijft leidend voor de export.",\n',
    '            help=FOCUS_FILTER_GUIDANCE,\n',
)

text = replace_once(
    text,
    '''        with st.expander("Technische details bij de vervangtabel", expanded=False):
            technical_columns = technical_display_columns(replacement_editor_df.columns)
''',
    '''        with st.expander("Technische details bij de vervangtabel", expanded=False):
            st.caption(TECHNICAL_DETAILS_GUIDANCE)
            technical_columns = technical_display_columns(replacement_editor_df.columns)
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

# v12.3: reduce the editable table to user-facing columns only.
text = replace_once(
    text,
    '''            column_order=[
                "include",
                "remember",
                "review_status_label",
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
''',
    '''            column_order=main_review_columns(replacement_editor_df.columns),
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

scrub_key_mapping_block = '''        scrub_key_rows = edited_replacements_df.copy()
        scrub_key_field_map = {
            "find": "original_value",
            "replace_with": "placeholder",
            "entity_type": "entity_type",
            "type_label": "type_label",
            "source": "source",
            "review_status": "review_status",
            "include": "include",
        }
        for scrub_key_source_column, scrub_key_target_column in scrub_key_field_map.items():
            if scrub_key_source_column in scrub_key_rows.columns:
                scrub_key_rows[scrub_key_target_column] = scrub_key_rows[scrub_key_source_column]
        scrub_key_timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        if "timestamp" not in scrub_key_rows.columns:
            scrub_key_rows["timestamp"] = scrub_key_timestamp
        else:
            scrub_key_rows["timestamp"] = scrub_key_rows["timestamp"].fillna("").replace("", scrub_key_timestamp)
        scrub_key = build_scrub_key(scrub_key_rows)
'''

review_summary_block = '''        st.subheader("4. Download opgeschoonde bestanden")
        final_review_summary = build_review_summary(edited_replacements_df)
        st.markdown("**Eindcontrole vóór download**")
        if final_review_summary.get("open_candidate_warning") or final_review_summary.get("checked_rows_included_in_export", 0) == 0:
            st.warning(final_review_summary.get("readiness_label", "Controle nodig voor export"))
        else:
            st.success(final_review_summary.get("readiness_label", "Klaar voor export na gebruikerscontrole"))
        st.markdown(review_summary_markdown(final_review_summary))
        export_sanity_checks = build_export_sanity_checks(edited_replacements_df)
        st.markdown("**Extra exportcontrole**")
        for export_sanity_warning in export_sanity_warnings(export_sanity_checks):
            st.warning(export_sanity_warning)
        st.caption("Deze exportcontrole is adviserend: downloads blijven beschikbaar en de exportinstellingen blijven ongewijzigd.")
        st.markdown("**Scrub Key (JSON)**")
        st.warning("Let op: een Scrub Key maakt de vervangen waarden lokaal herleidbaar. Dit is pseudonimisering, geen volledige anonimisering. Deel deze sleutel niet met AI-diensten of derden tenzij dat bewust en toegestaan is.")
''' + scrub_key_mapping_block + '''        scrub_key_issues = validate_scrub_key(scrub_key)
        if scrub_key_issues:
            st.warning("Scrub Key kan nog niet betrouwbaar worden geëxporteerd: " + "; ".join(scrub_key_issues[:3]))
        else:
            if scrub_key.get("item_count", 0) == 0:
                st.info("Er zijn geen geselecteerde vervangingen voor de Scrub Key. De JSON bevat dan geen mapping-items.")
            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
        st.warning(EXPORT_GUIDANCE)
'''

# v12.5/v12.6/v13.1: add final review summary, advisory export sanity warnings and Scrub Key JSON export.
# Handle both unpatched and v12.4-patched app text.
text = replace_once(
    text,
    '''        st.subheader("4. Download opgeschoonde bestanden")
        st.warning(EXPORT_GUIDANCE)
''',
    review_summary_block,
)

text = replace_once(
    text,
    '''        st.subheader("4. Download opgeschoonde bestanden")
''',
    review_summary_block,
)

# v12.6: extend an existing v12.5 review-summary block with advisory sanity warnings.
text = replace_once(
    text,
    '''        st.markdown(review_summary_markdown(final_review_summary))
        st.warning(EXPORT_GUIDANCE)
''',
    '''        st.markdown(review_summary_markdown(final_review_summary))
        export_sanity_checks = build_export_sanity_checks(edited_replacements_df)
        st.markdown("**Extra exportcontrole**")
        for export_sanity_warning in export_sanity_warnings(export_sanity_checks):
            st.warning(export_sanity_warning)
        st.caption("Deze exportcontrole is adviserend: downloads blijven beschikbaar en de exportinstellingen blijven ongewijzigd.")
        st.warning(EXPORT_GUIDANCE)
''',
)

# v13.1: extend an existing v12.6 block with Scrub Key JSON export.
text = replace_once(
    text,
    '''        st.caption("Deze exportcontrole is adviserend: downloads blijven beschikbaar en de exportinstellingen blijven ongewijzigd.")
        st.warning(EXPORT_GUIDANCE)
''',
    '''        st.caption("Deze exportcontrole is adviserend: downloads blijven beschikbaar en de exportinstellingen blijven ongewijzigd.")
        st.markdown("**Scrub Key (JSON)**")
        st.warning("Let op: een Scrub Key maakt de vervangen waarden lokaal herleidbaar. Dit is pseudonimisering, geen volledige anonimisering. Deel deze sleutel niet met AI-diensten of derden tenzij dat bewust en toegestaan is.")
''' + scrub_key_mapping_block + '''        scrub_key_issues = validate_scrub_key(scrub_key)
        if scrub_key_issues:
            st.warning("Scrub Key kan nog niet betrouwbaar worden geëxporteerd: " + "; ".join(scrub_key_issues[:3]))
        else:
            if scrub_key.get("item_count", 0) == 0:
                st.info("Er zijn geen geselecteerde vervangingen voor de Scrub Key. De JSON bevat dan geen mapping-items.")
            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
        st.warning(EXPORT_GUIDANCE)
''',
)

# v13.1 hotfix: map rows in an already-patched Scrub Key block before building the key.
text = replace_once(
    text,
    '''        scrub_key_rows = edited_replacements_df.copy()
        scrub_key_timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        if "timestamp" not in scrub_key_rows.columns:
            scrub_key_rows["timestamp"] = scrub_key_timestamp
        else:
            scrub_key_rows["timestamp"] = scrub_key_rows["timestamp"].fillna("").replace("", scrub_key_timestamp)
        scrub_key = build_scrub_key(scrub_key_rows)
''',
    scrub_key_mapping_block,
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
