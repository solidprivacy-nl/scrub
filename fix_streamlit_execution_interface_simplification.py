"""Apply a small execution-interface simplification patch to the Streamlit app.

This script is intentionally presentation-only. It reduces visible default UI
noise in the Hugging Face Streamlit app by moving secondary controls behind
clear expanders. It must not change replacement/export/Scrub Key/reinsert
semantics.
"""

from __future__ import annotations

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")


def replace_once(source: str, old: str, new: str) -> str:
    """Replace one exact source block, idempotently."""

    if new in source:
        return source
    if old in source:
        return source.replace(old, new, 1)
    return source


def apply_execution_interface_simplification(source: str) -> str:
    """Return Streamlit source with a calmer default execution interface."""

    text = source

    text = replace_once(
        text,
        '''st.sidebar.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))
''',
        '''with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False):
    st.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))
''',
    )

    text = replace_once(
        text,
        '''if st_recognition_profile == "Dutch Legal Strict":
    st.info(
        "Juridische controle is actief. Scrub zoekt extra naar zaaknummers, rolnummers, "
        "rekestnummers, parketnummers, dossiernummers, clientnummers, CJIB, ECLI, "
        "procespartijen, instanties en mogelijke juridische referenties."
    )
elif st_recognition_profile == "Dutch / EU":
    st.info(
        "Algemene Nederlandse controle is actief. Scrub zoekt onder meer naar BSN, postcode, "
        "KvK, btw-nummer, Nederlandse IBAN, telefoonnummers, adressen, kentekens en BIG-nummers."
    )
''',
        '''with st.expander("Controle-instellingen en herkenning", expanded=False):
    if st_recognition_profile == "Dutch Legal Strict":
        st.info(
            "Juridische controle is actief. Scrub zoekt extra naar zaaknummers, rolnummers, "
            "rekestnummers, parketnummers, dossiernummers, clientnummers, CJIB, ECLI, "
            "procespartijen, instanties en mogelijke juridische referenties."
        )
    elif st_recognition_profile == "Dutch / EU":
        st.info(
            "Algemene Nederlandse controle is actief. Scrub zoekt onder meer naar BSN, postcode, "
            "KvK, btw-nummer, Nederlandse IBAN, telefoonnummers, adressen, kentekens en BIG-nummers."
        )
''',
    )

    text = replace_once(
        text,
        '''st_text = st.text_area(
    label="Plak tekst of controleer de uit het document gehaalde tekst",
    value=input_text,
    height=300,
    key="text_input",
)
''',
        '''st_text = st.text_area(
    label="Plak tekst of controleer de uit het document gehaalde tekst",
    value=input_text,
    height=240,
    key="text_input",
)
''',
    )

    text = replace_once(
        text,
        '''        st.caption(
            "Centrale side-by-side reviewweergave. Brontekst links, verwerkte tekst rechts. "
            "Synchroon scrollen en optionele markeringen blijven visuele hulp."
        )
''',
        '''        st.caption(
            "Controleer het resultaat. Details en extra hulpmiddelen staan standaard ingeklapt."
        )
''',
    )

    text = replace_once(
        text,
        '''        st.caption(
            "Vink fout-positieven uit, pas placeholders aan, voeg handmatige vervangingen toe "
            "en vink Onthouden aan voor vervangingen die je opnieuw wilt gebruiken. "
            "Mogelijke kandidaten staan standaard uitgevinkt. De vervangtabel blijft leidend."
        )
        st.caption("De vervangtabel blijft leidend voor beslissingen en export.")
        st.info(REVIEW_INTRO_GUIDANCE)
        with st.expander("Uitleg bij deze controle", expanded=False):
            st.markdown(f"- {CANDIDATE_GUIDANCE}")
            st.markdown(f"- {FOCUS_FILTER_GUIDANCE}")
            st.markdown(f"- {TECHNICAL_DETAILS_GUIDANCE}")
            st.markdown(f"- {AI_USAGE_GUIDANCE}")
''',
        '''        st.caption(
            "Controleer alleen wat nodig is. De vervangtabel blijft leidend en blijft beschikbaar voor detailcontrole."
        )
        with st.expander("Waarom controleren?", expanded=False):
            st.info(REVIEW_INTRO_GUIDANCE)
            st.markdown(f"- {CANDIDATE_GUIDANCE}")
            st.markdown(f"- {FOCUS_FILTER_GUIDANCE}")
            st.markdown(f"- {TECHNICAL_DETAILS_GUIDANCE}")
            st.markdown(f"- {AI_USAGE_GUIDANCE}")
''',
    )

    text = replace_once(
        text,
        '''        st.markdown("**Gemiste waarde toevoegen**")
        st.caption("Voeg snel een waarde toe die Scrub heeft gemist.")
        with st.form("manual_mask_entry_form", clear_on_submit=True):
            manual_value = st.text_input("Waarde die alsnog gemaskeerd moet worden")
            manual_type_label = st.selectbox("Type gegeven", list(MANUAL_MASK_TYPE_OPTIONS))
            manual_placeholder = build_manual_placeholder(manual_type_label, replacement_editor_df)
            manual_replace_with = st.text_input("Vervangen door", value=manual_placeholder)
            manual_submit = st.form_submit_button("Toevoegen aan vervangtabel")
''',
        '''        with st.expander("Gemiste waarde toevoegen", expanded=False):
            st.caption("Voeg een waarde toe die Scrub heeft gemist.")
            with st.form("manual_mask_entry_form", clear_on_submit=True):
                manual_value = st.text_input("Waarde die alsnog gemaskeerd moet worden")
                manual_type_label = st.selectbox("Type gegeven", list(MANUAL_MASK_TYPE_OPTIONS))
                manual_placeholder = build_manual_placeholder(manual_type_label, replacement_editor_df)
                manual_replace_with = st.text_input("Vervangen door", value=manual_placeholder)
                manual_submit = st.form_submit_button("Toevoegen aan vervangtabel")
''',
    )

    text = replace_once(
        text,
        '''        review_filter = st.selectbox(
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

        if st_recognition_profile == "Dutch Legal Strict":
            with st.expander("Mogelijk extra te controleren waarden", expanded=bool(candidate_rows)):
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
''',
        '''        with st.expander("Extra controlehulpen", expanded=False):
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

            if st_recognition_profile == "Dutch Legal Strict":
                st.markdown("**Mogelijk extra te controleren waarden**")
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
''',
    )

    text = replace_once(
        text,
        '''        st.subheader("4. Onthoud herbruikbare vervangingen")
        remember_rows_to_save = []
        for _, row in edited_replacements_df.iterrows():
            include = safe_bool(row.get("include", False))
            remember = safe_bool(row.get("remember", False))
            find_text = safe_cell(row.get("find", ""))
            replace_text = safe_cell(row.get("replace_with", ""))
            entity_type = safe_cell(row.get("entity_type", "REMEMBERED")) or "REMEMBERED"
            if include and remember and find_text and replace_text:
                remember_rows_to_save.append({"find": find_text, "replace_with": replace_text, "entity_type": entity_type})

        memory_col1, memory_col2 = st.columns(2)
        with memory_col1:
            if st.button("Onthouden vervangingen opslaan"):
                saved_count = save_remembered_replacements(remember_rows_to_save)
                st.success(f"{saved_count} vervanging(en) opgeslagen.")
                st.info(f"Geheugenbestand: {get_memory_file_path()}")
        with memory_col2:
            if st.button("Onthouden vervangingen wissen"):
                clear_remembered_replacements()
                st.warning("Onthouden vervangingen gewist.")

        st.subheader("5. Exporteer resultaat")
''',
        '''        remember_rows_to_save = []
        for _, row in edited_replacements_df.iterrows():
            include = safe_bool(row.get("include", False))
            remember = safe_bool(row.get("remember", False))
            find_text = safe_cell(row.get("find", ""))
            replace_text = safe_cell(row.get("replace_with", ""))
            entity_type = safe_cell(row.get("entity_type", "REMEMBERED")) or "REMEMBERED"
            if include and remember and find_text and replace_text:
                remember_rows_to_save.append({"find": find_text, "replace_with": replace_text, "entity_type": entity_type})

        with st.expander("Herbruikbare vervangingen", expanded=False):
            memory_col1, memory_col2 = st.columns(2)
            with memory_col1:
                if st.button("Onthouden vervangingen opslaan"):
                    saved_count = save_remembered_replacements(remember_rows_to_save)
                    st.success(f"{saved_count} vervanging(en) opgeslagen.")
                    st.info(f"Geheugenbestand: {get_memory_file_path()}")
            with memory_col2:
                if st.button("Onthouden vervangingen wissen"):
                    clear_remembered_replacements()
                    st.warning("Onthouden vervangingen gewist.")

        st.subheader("4. Exporteer resultaat")
''',
    )

    text = replace_once(
        text,
        '''        st.info(
            "Je export wordt gemaakt op basis van de gecontroleerde vervangtabel. "
            "Controleer bij twijfel eerst de gevonden gegevens hierboven."
        )
        if uploaded_file is not None:
            st.info(f"Bestand beschikbaar voor export: {uploaded_file.name}")
        else:
            st.info("Je gebruikt tekst uit het invoervak. De export wordt gemaakt op basis van deze tekst.")

        st.markdown("**Document downloaden**")
''',
        '''        st.caption(
            "Download de opgeschoonde documenten. Scrub Key en auditbestanden staan in aparte secties."
        )

        st.markdown("**Document downloaden**")
''',
    )

    text = replace_once(
        text,
        '''        st.markdown("**Scrub Key**")
        st.warning("De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.")
''',
        '''        with st.expander("Scrub Key downloaden", expanded=False):
            st.warning("De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.")
''',
    )

    text = replace_once(
        text,
        '''        scrub_key_rows = edited_replacements_df.copy()
''',
        '''            scrub_key_rows = edited_replacements_df.copy()
''',
    )

    text = replace_once(
        text,
        '''        st.markdown("**Audit en technische bestanden**")
        st.download_button(
''',
        '''        with st.expander("Audit en technische bestanden", expanded=False):
            st.download_button(
''',
    )

    text = replace_once(
        text,
        '''        if docx_bytes is not None:
            render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)

        with st.expander("Technische informatie", expanded=False):
            st.caption(
                "Geavanceerde technische exportinformatie blijft beschikbaar. "
                "Bestaande exportbestanden, bestandsnamen en inhoud zijn niet gewijzigd."
            )
''',
        '''            if docx_bytes is not None:
                render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)

            with st.expander("Technische informatie", expanded=False):
                st.caption(
                    "Geavanceerde technische exportinformatie blijft beschikbaar. "
                    "Bestaande exportbestanden, bestandsnamen en inhoud zijn niet gewijzigd."
                )
''',
    )

    return text


def main() -> None:
    source = APP_FILE.read_text(encoding="utf-8")
    patched = apply_execution_interface_simplification(source)
    if patched != source:
        APP_FILE.write_text(patched, encoding="utf-8")


if __name__ == "__main__":
    main()
