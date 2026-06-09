"""Startup patch for PDF text extraction to restored TXT UI.

This patch runs after ``fix_streamlit_nested_expanders.py``. It adds a narrow
PDF-to-restored-TXT section inside ``Originele waarden terugzetten`` only.

It deliberately does not add restored PDF output, OCR, PDF-to-DOCX conversion,
AI calls, cloud processing, batch processing, storage, or export/download
semantic changes outside the approved restored TXT output for this workflow.
"""

from __future__ import annotations

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")


def replace_once(source: str, old: str, new: str) -> str:
    if old in source and new not in source:
        return source.replace(old, new, 1)
    return source


text = replace_once(
    text,
    'from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes\n',
    'from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes\n'
    'from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes\n',
)

pdf_text_reinsert_ui_block = '''    st.markdown("**PDF-tekst terugzetten naar TXT**")
    st.warning("Let op: PDF-tekstextractie is niet altijd volledig. Opmaak, tabellen, kolommen, headers, footers en visuele volgorde kunnen verloren gaan. Deze functie maakt geen herstelde PDF. De uitvoer is alleen herstelde TXT-tekst. Scans of afbeelding-PDF’s worden niet ondersteund omdat OCR niet beschikbaar is.")
    st.warning("Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat zorgvuldig voordat u het deelt.")
    st.caption("PDF-bestand terugzetten naar TXT. Deze stap wordt lokaal uitgevoerd met uw Scrub Key. Scrub gebruikt hiervoor geen AI, geen cloudverwerking en geen OCR.")
    st.markdown("- Lokaal uitgevoerd: Ja")
    st.markdown("- AI-verwerking: Nee")
    st.markdown("- Cloudverwerking: Nee")
    st.markdown("- OCR gebruikt: Nee")
    st.markdown("- PDF-output: Nee")
    active_pdf_text_reinsert_scrub_key = st.session_state.get("active_scrub_key", {})
    pdf_text_reinsert_file = st.file_uploader(
        "Upload een PDF-bestand met placeholders",
        type=["pdf"],
        key="pdf_text_reinsert_file",
        help="Gebruik een tekstgebaseerde PDF met Scrub placeholders die bij de geladen Scrub Key horen.",
    )
    if st.button("Zet PDF-tekst lokaal terug", key="run_pdf_text_file_reinsert"):
        if not active_pdf_text_reinsert_scrub_key or not active_pdf_text_reinsert_scrub_key.get("items"):
            st.warning("Laad eerst een geldige Scrub Key voordat u PDF-tekst lokaal terugzet.")
        elif pdf_text_reinsert_file is None:
            st.warning("Upload eerst een PDF-bestand met placeholders.")
        else:
            st.session_state["pdf_text_reinsert_result"] = reinsert_pdf_text_bytes(
                pdf_text_reinsert_file.getvalue(),
                active_pdf_text_reinsert_scrub_key,
            )
    if "pdf_text_reinsert_result" in st.session_state:
        pdf_text_reinsert_result = st.session_state["pdf_text_reinsert_result"]
        pdf_text_validation_issues = pdf_text_reinsert_result.get("validation_issues", [])
        pdf_text_unsupported_reason = pdf_text_reinsert_result.get("unsupported_reason")
        pdf_text_restored_text = pdf_text_reinsert_result.get("restored_text") or pdf_text_reinsert_result.get("text", "")
        pdf_text_extracted_text = pdf_text_reinsert_result.get("extracted_text", "")
        extracted_text_length = len(pdf_text_extracted_text)
        pdf_text_can_download = not pdf_text_validation_issues and not pdf_text_unsupported_reason and bool(str(pdf_text_restored_text).strip())
        if pdf_text_validation_issues:
            st.warning("PDF-tekst terugzetten kan niet betrouwbaar worden uitgevoerd: " + "; ".join(pdf_text_validation_issues[:3]))
        elif pdf_text_unsupported_reason:
            st.warning(pdf_text_unsupported_reason)
            st.warning("Geen bruikbare tekstlaag gevonden. Scans of afbeelding-PDF’s worden niet ondersteund, omdat OCR niet beschikbaar is.")
        elif pdf_text_reinsert_result.get("replacement_count", 0) > 0:
            st.success(f"{pdf_text_reinsert_result.get('replacement_count', 0)} waarde(n) lokaal teruggezet uit PDF-tekst.")
        else:
            st.info("PDF-tekst is lokaal geëxtraheerd, maar er zijn geen placeholders teruggezet. Controleer of de juiste Scrub Key is geladen.")
        if pdf_text_can_download:
            st.text_area(
                "Herstelde TXT-tekst uit PDF",
                value=pdf_text_restored_text,
                height=220,
                key="pdf_text_reinsert_output_text",
            )
            st.download_button(
                "Download herstelde TXT uit PDF (.txt)",
                data=str(pdf_text_restored_text).encode("utf-8"),
                file_name="solidprivacy_herstelde_txt_uit_pdf.txt",
                mime="text/plain",
            )
        with st.expander("Controleverslag PDF-tekst terugzetten", expanded=True):
            st.markdown(f"- Documenttype (document_type): {pdf_text_reinsert_result.get('document_type', 'pdf_text')}")
            st.markdown(f"- Lengte geëxtraheerde tekst (extracted_text_length): {extracted_text_length}")
            st.markdown(f"- Aantal teruggezette waarden (replacement_count): {pdf_text_reinsert_result.get('replacement_count', 0)}")
            st.markdown(f"- Mappingregels totaal (item_count): {pdf_text_reinsert_result.get('item_count', 0)}")
            st.markdown(f"- Actieve mappingregels (active_item_count): {pdf_text_reinsert_result.get('active_item_count', 0)}")
            st.markdown(f"- Uitgesloten mappingregels (excluded_item_count): {pdf_text_reinsert_result.get('excluded_item_count', 0)}")
            st.markdown(f"- Niet gevonden placeholders (placeholders_not_found): {pdf_text_reinsert_result.get('placeholders_not_found', [])}")
            st.markdown(f"- Onbekende placeholders in tekst (unknown_placeholders): {pdf_text_reinsert_result.get('unknown_placeholders', [])}")
            st.markdown(f"- Dubbele placeholders in sleutel (duplicate_placeholders): {pdf_text_reinsert_result.get('duplicate_placeholders', [])}")
            st.markdown(f"- Validatieproblemen (validation_issues): {pdf_text_validation_issues}")
            st.markdown(f"- Niet-ondersteund reden (unsupported_reason): {pdf_text_unsupported_reason}")
            st.markdown(f"- Lokaal uitgevoerd (local_only): {'Ja' if pdf_text_reinsert_result.get('local_only') is True else 'Nee'}")
            st.markdown(f"- AI-verwerking (ai_processing): {'Ja' if pdf_text_reinsert_result.get('ai_processing') is True else 'Nee'}")
            st.markdown(f"- Cloudverwerking (cloud_processing): {'Ja' if pdf_text_reinsert_result.get('cloud_processing') is True else 'Nee'}")
            st.markdown(f"- OCR gebruikt (ocr_used): {'Ja' if pdf_text_reinsert_result.get('ocr_used') is True else 'Nee'}")
            st.markdown(f"- PDF-output (pdf_output): {'Ja' if pdf_text_reinsert_result.get('pdf_output') is True else 'Nee'}")
        if extracted_text_length < 20 and not pdf_text_unsupported_reason:
            st.warning("Er is weinig tekst uit de PDF gehaald. Controleer of de PDF een bruikbare tekstlaag heeft en of de extractie volledig genoeg is.")
        if pdf_text_reinsert_result.get("unknown_placeholders"):
            st.warning("De PDF-tekst bevat placeholders die niet in de actieve Scrub Key staan. Deze waarden zijn niet teruggezet.")
        if pdf_text_reinsert_result.get("duplicate_placeholders"):
            st.warning("De Scrub Key bevat dubbele placeholders. Deze zijn niet automatisch teruggezet.")
        if pdf_text_reinsert_result.get("placeholders_not_found"):
            st.caption("Niet alle mappingregels uit de Scrub Key zijn gevonden in de geëxtraheerde PDF-tekst.")
'''

pdf_insert_marker = '''        if docx_reinsert_result.get("placeholders_not_found"):
            st.caption("Niet alle mappingregels kwamen voor in het DOCX-bestand.")
else:
'''

text = replace_once(
    text,
    pdf_insert_marker,
    '''        if docx_reinsert_result.get("placeholders_not_found"):
            st.caption("Niet alle mappingregels kwamen voor in het DOCX-bestand.")
'''
    + pdf_text_reinsert_ui_block
    + '''else:
''',
)

APP_FILE.write_text(text, encoding="utf-8")
