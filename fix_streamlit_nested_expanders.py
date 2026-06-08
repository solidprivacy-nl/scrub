"""Startup compatibility patches for the Streamlit app.

This script runs before Streamlit starts in the Docker container. It applies small
idempotent source patches that keep the Hugging Face Space usable while larger UI
refactors are being staged.

Patches currently applied:
- v9: remove nested Streamlit expander usage for Woordenlijsten.
- v12.1-v12.6: add review status, focus filters, guidance, summary and advisory export checks.
- v13.1: add local Scrub Key JSON export after review.
- v13.2: add local Scrub Key import/reload UI using the pure import helper.
- v13.3: add deterministic local reinsert UI using the pure reinsert helper.
- v13.6: add a two-mode UI skeleton with Anonimiseren / Originele waarden terugzetten tabs.
"""

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")


def replace_once(source: str, old: str, new: str) -> str:
    if old in source and new not in source:
        return source.replace(old, new, 1)
    return source


text = replace_once(text, 'from pathlib import Path\n', 'from pathlib import Path\nfrom datetime import datetime, timezone\n')

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
    'from review_summary import build_review_summary, review_summary_markdown\n'
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n'
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n'
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n'
    'from scrub_key_reinsert import reinsert_from_scrub_key\n',
)

text = replace_once(
    text,
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n',
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n'
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n'
    'from scrub_key_reinsert import reinsert_from_scrub_key\n',
)

text = replace_once(
    text,
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n',
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n'
    'from scrub_key_reinsert import reinsert_from_scrub_key\n',
)

text = replace_once(
    text,
    '''    st_deny_allow_expander = st.expander("Woordenlijsten", expanded=False)
    with st_deny_allow_expander:
        st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
        st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
        st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
''',
    '''    st.markdown("**Woordenlijsten**")
    st_allow_list = st_tags(label="Niet vervangen", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst worden niet als gevoelig gegeven behandeld.")
    st_deny_list = st_tags(label="Extra controleren", text="Voer woord in en druk op Enter.")
    st.caption("Woorden in deze lijst krijgen extra aandacht bij de herkenning.")
''',
)

for old, new in [
    (
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
    ),
    (
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
    ),
    (
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
    ),
    (
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
    ),
]:
    text = replace_once(text, old, new)

scrub_key_import_merge_block = '''        if "scrub_key_import_rows" in st.session_state:
            imported_scrub_key_rows = st.session_state.pop("scrub_key_import_rows")
            added_scrub_key_rows = 0
            existing_find_values = {str(row.get("find", "")).strip() for row in default_editor_rows}
            if len(default_editor_rows) == 1 and not str(default_editor_rows[0].get("find", "")).strip():
                default_editor_rows = []
                existing_find_values = set()
            for imported_scrub_key_row in imported_scrub_key_rows:
                imported_find = str(imported_scrub_key_row.get("find", "")).strip()
                imported_replace = str(imported_scrub_key_row.get("replace_with", "")).strip()
                if not imported_find or not imported_replace or imported_find in existing_find_values:
                    continue
                imported_row = dict(imported_scrub_key_row)
                imported_row.setdefault("include", True)
                imported_row.setdefault("remember", False)
                imported_row.setdefault("source", "scrub_key_import")
                imported_row.setdefault("source_label", "Scrub Key")
                imported_row.setdefault("reason", "Geladen uit Scrub Key")
                imported_row.setdefault("context", "")
                imported_row.setdefault("confidence", "")
                imported_row.setdefault("score", None)
                imported_row.setdefault("type_label", entity_label(imported_row.get("entity_type", "MANUAL")))
                imported_row.setdefault("review_status_label", review_status_label(imported_row.get("review_status", "manual")))
                imported_row.setdefault("review_order", review_status_order(imported_row.get("review_status", "manual")))
                default_editor_rows.append(imported_row)
                existing_find_values.add(imported_find)
                added_scrub_key_rows += 1
            if added_scrub_key_rows:
                st.success(f"{added_scrub_key_rows} Scrub Key regel(s) geladen in de vervangtabel.")
'''

text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
''',
    scrub_key_import_merge_block + '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
''',
)

review_table_intro_block = '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
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
'''

text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        edited_replacements_df = st.data_editor(
''',
    review_table_intro_block,
)

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

scrub_key_import_ui_block = '''        st.markdown("**Scrub Key laden**")
        st.warning("Let op: een Scrub Key maakt vervangen waarden lokaal herleidbaar. Dit is pseudonimisering, geen volledige anonimisering. Bewaar deze sleutel lokaal en deel deze niet met AI-diensten of derden tenzij dat bewust en toegestaan is.")
        st.caption("Upload of plak een eerder geëxporteerde Scrub Key JSON. De sleutel wordt eerst gevalideerd en daarna pas na jouw klik aan de vervangtabel toegevoegd.")
        scrub_key_import_file = st.file_uploader(
            "Upload Scrub Key JSON (.json)",
            type=["json"],
            key="scrub_key_import_file",
            help="Gebruik alleen een lokale Scrub Key die bij dit dossier of document hoort.",
        )
        scrub_key_import_paste = st.text_area(
            "Of plak Scrub Key JSON",
            value="",
            height=120,
            key="scrub_key_import_paste",
        )
        scrub_key_import_text = ""
        scrub_key_import_decode_error = None
        if scrub_key_import_file is not None:
            try:
                scrub_key_import_text = scrub_key_import_file.getvalue().decode("utf-8")
            except UnicodeDecodeError:
                scrub_key_import_decode_error = "Scrub Key bestand is geen geldige UTF-8 tekst."
        elif scrub_key_import_paste.strip():
            scrub_key_import_text = scrub_key_import_paste
        if st.button("Valideer en laad Scrub Key", key="load_scrub_key_import"):
            if scrub_key_import_decode_error:
                st.error(scrub_key_import_decode_error)
            else:
                scrub_key_import_result = build_scrub_key_import_result(scrub_key_import_text)
                for scrub_key_import_warning in scrub_key_import_result.get("warnings", [IMPORT_PRIVACY_WARNING]):
                    st.warning(scrub_key_import_warning)
                if scrub_key_import_result.get("ok"):
                    st.success(f"Scrub Key geldig: {scrub_key_import_result.get('item_count', 0)} mappingregel(s) gevonden.")
                    st.session_state["active_scrub_key"] = scrub_key_import_result.get("scrub_key")
                    st.session_state["scrub_key_import_rows"] = scrub_key_import_result.get("mapping_rows", [])
                    if "replacement_editor" in st.session_state:
                        del st.session_state["replacement_editor"]
                    st.rerun()
                else:
                    for scrub_key_import_error in scrub_key_import_result.get("errors", []):
                        st.error(scrub_key_import_error)
'''

reinsert_ui_block = '''        st.markdown("**Originele waarden terugzetten**")
        st.warning("Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat zorgvuldig voordat u het deelt.")
        st.caption("Deze stap wordt lokaal uitgevoerd met uw Scrub Key. Er wordt geen AI- of cloudverwerking gebruikt voor het terugzetten.")
        active_reinsert_scrub_key = st.session_state.get("active_scrub_key", scrub_key)
        reinsert_input_text = st.text_area(
            "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten",
            value="",
            height=180,
            key="reinsert_input_text",
        )
        if st.button("Zet originele waarden lokaal terug", key="run_local_reinsert"):
            if not reinsert_input_text.strip():
                st.warning("Plak eerst tekst waarin placeholders staan die u lokaal wilt terugzetten.")
            else:
                st.session_state["reinsert_result"] = reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)
        if "reinsert_result" in st.session_state:
            reinsert_result = st.session_state["reinsert_result"]
            reinsert_validation_issues = reinsert_result.get("validation_issues", [])
            if reinsert_validation_issues:
                st.warning("Terugzetten kan niet betrouwbaar worden uitgevoerd: " + "; ".join(reinsert_validation_issues[:3]))
            elif reinsert_result.get("replacement_count", 0) > 0:
                st.success(f"{reinsert_result.get('replacement_count', 0)} waarde(n) lokaal teruggezet.")
            else:
                st.info("Er zijn geen placeholders teruggezet. Controleer of de tekst placeholders bevat die in de Scrub Key staan.")
            st.text_area(
                "Herstelde tekst",
                value=reinsert_result.get("text", ""),
                height=220,
                key="reinsert_output_text",
            )
            st.download_button(
                "Download herstelde tekst (.txt)",
                data=reinsert_result.get("text", ""),
                file_name="solidprivacy_herstelde_tekst.txt",
                mime="text/plain",
            )
            with st.expander("Controleverslag terugzetten", expanded=True):
                st.markdown(f"- Mappingregels totaal: {reinsert_result.get('item_count', 0)}")
                st.markdown(f"- Actieve mappingregels: {reinsert_result.get('active_item_count', 0)}")
                st.markdown(f"- Uitgesloten mappingregels: {reinsert_result.get('excluded_item_count', 0)}")
                st.markdown(f"- Aantal teruggezette waarden: {reinsert_result.get('replacement_count', 0)}")
                st.markdown(f"- Niet gevonden placeholders: {reinsert_result.get('placeholders_not_found', [])}")
                st.markdown(f"- Onbekende placeholders in tekst: {reinsert_result.get('unknown_placeholders', [])}")
                st.markdown(f"- Dubbele placeholders in sleutel: {reinsert_result.get('duplicate_placeholders', [])}")
                st.markdown(f"- Validatieproblemen: {reinsert_validation_issues}")
                st.markdown(f"- Lokaal uitgevoerd: {reinsert_result.get('local_only') is True}")
                st.markdown(f"- AI-verwerking: {reinsert_result.get('ai_processing') is True}")
                st.markdown(f"- Cloudverwerking: {reinsert_result.get('cloud_processing') is True}")
            if reinsert_result.get("unknown_placeholders"):
                st.warning("De tekst bevat placeholders die niet in de actieve Scrub Key staan.")
            if reinsert_result.get("duplicate_placeholders"):
                st.warning("De Scrub Key bevat dubbele placeholders. Deze zijn niet automatisch teruggezet.")
            if reinsert_result.get("placeholders_not_found"):
                st.caption("Niet alle mappingregels kwamen voor in de ingevoerde tekst.")
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
''' + scrub_key_import_ui_block + reinsert_ui_block + '''        st.warning(EXPORT_GUIDANCE)
'''

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

text = replace_once(
    text,
    '''            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
        st.warning(EXPORT_GUIDANCE)
''',
    '''            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
''' + scrub_key_import_ui_block + reinsert_ui_block + '''        st.warning(EXPORT_GUIDANCE)
''',
)

text = replace_once(
    text,
    '''            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
''' + scrub_key_import_ui_block + '''        st.warning(EXPORT_GUIDANCE)
''',
    '''            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
''' + scrub_key_import_ui_block + reinsert_ui_block + '''        st.warning(EXPORT_GUIDANCE)
''',
)

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

two_mode_intro_block = '''st.markdown("**Kies werkmodus**")
two_mode_anon_tab, two_mode_reinsert_tab = st.tabs(["Anonimiseren", "Originele waarden terugzetten"])
with two_mode_anon_tab:
    st.caption("Anonimiseren: upload of plak brontekst, controleer gevonden gegevens en download opgeschoonde uitvoer.")
with two_mode_reinsert_tab:
    st.caption("Originele waarden terugzetten: laad een Scrub Key en gebruik de bestaande lokale tekst-terugzetflow verderop in deze app.")
'''

text = replace_once(
    text,
    '''st.info(LOCAL_PROCESSING_NOTE)

with st.expander("Over deze app", expanded=False):
''',
    '''st.info(LOCAL_PROCESSING_NOTE)
''' + two_mode_intro_block + '''
with st.expander("Over deze app", expanded=False):
''',
)

APP_FILE.write_text(text, encoding="utf-8")
