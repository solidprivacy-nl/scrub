"""Startup patch for grouped export/download UX.

WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION keeps export semantics unchanged. This patch
only changes presentation/copy/grouping in the export/download section. It does
not change bytes, filenames, MIME types, Scrub Key contents, reinsert behavior,
recognizers or benchmark logic.
"""

from __future__ import annotations

from pathlib import Path


APP_FILE = Path(__file__).with_name("presidio_streamlit.py")


OLD_EXPORT_DOWNLOAD_SECTION = '''        st.subheader("5. Download opgeschoonde bestanden")
        if uploaded_file is not None:
            st.info(f"Bestand beschikbaar voor export: {uploaded_file.name}")
        else:
            st.info("Geen uploadbestand aanwezig. Export wordt gemaakt op basis van het tekstvak.")

        st.download_button(
            label="Download opgeschoonde tekst (.txt)",
            data=export_text.encode("utf-8"),
            file_name="opgeschoonde_tekst.txt",
            mime="text/plain",
            key="download_txt",
        )
        st.download_button(
            label="Download vervangtabel (.csv)",
            data=replacement_report_csv(edited_report_rows),
            file_name="vervangtabel.csv",
            mime="text/csv",
            key="download_csv",
        )
        st.download_button(
            label="Download scrubrapport (.txt)",
            data=scrub_report_txt(
                edited_report_rows,
                profile=profile_label,
                source_filename=uploaded_file.name if uploaded_file is not None else None,
            ),
            file_name="scrubrapport.txt",
            mime="text/plain",
            key="download_scrub_report",
        )

        try:
            if uploaded_file is not None and uploaded_file.name.lower().endswith(".docx"):
                docx_bytes = anonymized_docx_from_original(uploaded_file, edited_replacements)
                docx_filename = "opgeschoond_" + uploaded_file.name
            else:
                docx_bytes = docx_from_text(export_text)
                docx_filename = "opgeschoonde_tekst.docx"
            render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)
            st.download_button(
                label="Download opgeschoond Word-bestand (.docx)",
                data=docx_bytes,
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_docx",
            )
        except Exception as docx_error:
            st.error(f"Kon geen DOCX-export maken: {docx_error}")

        try:
            st.download_button(
                label="Download opgeschoonde PDF (.pdf)",
                data=pdf_from_text(export_text),
                file_name="opgeschoonde_tekst.pdf",
                mime="application/pdf",
                key="download_pdf",
            )
        except Exception as pdf_error:
            st.error(f"Kon geen PDF-export maken: {pdf_error}")
'''


NEW_EXPORT_DOWNLOAD_SECTION = '''        st.subheader("5. Exporteer resultaat")
        st.info("Je export wordt gemaakt op basis van de gecontroleerde vervangtabel. Controleer bij twijfel eerst de gevonden gegevens hierboven.")
        if uploaded_file is not None:
            st.info(f"Bestand beschikbaar voor export: {uploaded_file.name}")
        else:
            st.info("Je gebruikt tekst uit het invoervak. De export wordt gemaakt op basis van deze tekst.")

        st.markdown("**Document downloaden**")
        st.download_button(
            label="Download opgeschoonde tekst (.txt)",
            data=export_text.encode("utf-8"),
            file_name="opgeschoonde_tekst.txt",
            mime="text/plain",
            key="download_txt",
        )

        docx_bytes = None
        docx_filename = "opgeschoonde_tekst.docx"
        try:
            if uploaded_file is not None and uploaded_file.name.lower().endswith(".docx"):
                docx_bytes = anonymized_docx_from_original(uploaded_file, edited_replacements)
                docx_filename = "opgeschoond_" + uploaded_file.name
            else:
                docx_bytes = docx_from_text(export_text)
                docx_filename = "opgeschoonde_tekst.docx"
            st.download_button(
                label="Download opgeschoond Word-bestand (.docx)",
                data=docx_bytes,
                file_name=docx_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key="download_docx",
            )
        except Exception as docx_error:
            st.error(f"Kon geen DOCX-export maken: {docx_error}")

        try:
            st.download_button(
                label="Download opgeschoonde PDF (.pdf)",
                data=pdf_from_text(export_text),
                file_name="opgeschoonde_tekst.pdf",
                mime="application/pdf",
                key="download_pdf",
            )
        except Exception as pdf_error:
            st.error(f"Kon geen PDF-export maken: {pdf_error}")

        st.markdown("**Scrub Key**")
        st.warning("De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.")
        scrub_key_rows = edited_replacements_df.copy()
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
        scrub_key_issues = validate_scrub_key(scrub_key)
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
                key="download_scrub_key",
            )

        st.markdown("**Audit en technische bestanden**")
        st.download_button(
            label="Vervangtabel downloaden (.csv)",
            data=replacement_report_csv(edited_report_rows),
            file_name="vervangtabel.csv",
            mime="text/csv",
            key="download_csv",
        )
        st.download_button(
            label="Scrubrapport downloaden (.txt)",
            data=scrub_report_txt(
                edited_report_rows,
                profile=profile_label,
                source_filename=uploaded_file.name if uploaded_file is not None else None,
            ),
            file_name="scrubrapport.txt",
            mime="text/plain",
            key="download_scrub_report",
        )
        render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)
        with st.expander("Technische informatie", expanded=False):
            st.caption("Geavanceerde technische exportinformatie blijft beschikbaar. Bestaande exportbestanden, bestandsnamen en inhoud zijn niet gewijzigd.")
'''


def apply_export_download_ux_patch(source: str) -> str:
    """Return app source with grouped export/download UI, if the old block exists."""

    if 'st.subheader("5. Exporteer resultaat")' in source:
        return source
    if OLD_EXPORT_DOWNLOAD_SECTION not in source:
        return source
    return source.replace(OLD_EXPORT_DOWNLOAD_SECTION, NEW_EXPORT_DOWNLOAD_SECTION, 1)


def main() -> None:
    source = APP_FILE.read_text(encoding="utf-8")
    APP_FILE.write_text(apply_export_download_ux_patch(source), encoding="utf-8")


if __name__ == "__main__":
    main()
