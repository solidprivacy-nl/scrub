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
- v13.2: add local Scrub Key import/reload UI using the pure import helper.
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

# v12/v13: import review, export sanity, Scrub Key export and Scrub Key import helpers.
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
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n',
)

# v12.6/v13.1/v13.2: extend imports on already partially patched app files.
text = replace_once(
    text,
    'from review_summary import build_review_summary, review_summary_markdown\n',
    'from review_summary import build_review_summary, review_summary_markdown\n'
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n'
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n'
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n',
)

text = replace_once(
    text,
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n',
    'from export_sanity import build_export_sanity_checks, export_sanity_warnings\n'
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n'
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n',
)

text = replace_once(
    text,
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n',
    'from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key\n'
    'from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n',
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

# v13.2: merge imported Scrub Key mappings into the review table only after a visible user action.
text = replace_once(
    text,
    '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
''',
    scrub_key_import_merge_block + '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
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

text = replace_once(
    text,
    '            help="Gebruik dit als overzichtsfilter. De volledige vervangtabel hieronder blijft leidend voor de export.",\n',
    '            help=FOCUS_FILTER_GUIDANCE,\n',
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
                    st.session_state["scrub_key_import_rows"] = scrub_key_import_result.get("mapping_rows", [])
                    if "replacement_editor" in st.session_state:
                        del st.session_state["replacement_editor"]
                    st.rerun()
                else:
                    for scrub_key_import_error in scrub_key_import_result.get("errors", []):
                        st.error(scrub_key_import_error)
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
                "Download Scrub Key (.json)
",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
''' + scrub_key_import_ui_block + '''        st.warning(EXPORT_GUIDANCE)
'''

# v12.5/v12.6/v13.1/v13.2: add final review summary, advisory export sanity warnings,
# Scrub Key JSON export and Scrub Key import/reload.
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

# v13.2: extend an already patched Scrub Key JSON export block with import/reload UI.
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
''' + scrub_key_import_ui_block + '''        st.warning(EXPORT_GUIDANCE)
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
