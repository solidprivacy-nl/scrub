"""Startup patch for the collapsible review table section.

The app source is still kept as the table-first fallback. This compatibility
patch runs after the existing Streamlit compatibility patch and wraps the
`Controleer gevonden gegevens` review table block in one collapsible section.

Scope:
- keep the review table available as source of truth/fallback;
- keep `replacement_editor`, include, remember, find and replace_with;
- avoid nested expanders by rendering possible missed values directly inside
  the collapsible section;
- do not change export, Scrub Key, reinsert or replacement behavior.
"""

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")

OLD_REVIEW_TABLE_BLOCK = '''        st.divider()
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
            column_order=main_review_columns(replacement_editor_df.columns),
            column_config={
                "include": st.column_config.CheckboxColumn(
                    "Meenemen", help="Vink uit om deze vervanging niet toe te passen.", default=True
                ),
                "remember": st.column_config.CheckboxColumn(
                    "Onthouden", help="Bewaar deze vervanging voor later gebruik.", default=False
                ),
                "review_status_label": st.column_config.TextColumn(
                    "Status", help="Reviewstatus: automatisch vervangen, controle nodig, handmatig of onthouden."
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
'''

NEW_REVIEW_TABLE_BLOCK = '''        st.divider()
        review_table_item_count = len(replacement_editor_df.index)
        review_table_expander_label = f"3. Controleer gevonden gegevens — {review_table_item_count} items"
        with st.expander(review_table_expander_label, expanded=False):
            st.caption(
                "Vink fout-positieven uit, pas placeholders aan, voeg handmatige vervangingen toe "
                "en vink Onthouden aan voor vervangingen die je opnieuw wilt gebruiken. "
                "Mogelijke kandidaten staan standaard uitgevinkt. De vervangtabel blijft leidend."
            )
            st.caption("De vervangtabel blijft leidend voor beslissingen en export.")

            if st_recognition_profile == "Dutch Legal Strict":
                st.markdown("**Mogelijke gemiste waarden**")
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
                column_order=main_review_columns(replacement_editor_df.columns),
                column_config={
                    "include": st.column_config.CheckboxColumn(
                        "Meenemen", help="Vink uit om deze vervanging niet toe te passen.", default=True
                    ),
                    "remember": st.column_config.CheckboxColumn(
                        "Onthouden", help="Bewaar deze vervanging voor later gebruik.", default=False
                    ),
                    "review_status_label": st.column_config.TextColumn(
                        "Status", help="Reviewstatus: automatisch vervangen, controle nodig, handmatig of onthouden."
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
'''

if NEW_REVIEW_TABLE_BLOCK not in text:
    text = text.replace(OLD_REVIEW_TABLE_BLOCK, NEW_REVIEW_TABLE_BLOCK, 1)

APP_FILE.write_text(text, encoding="utf-8")
