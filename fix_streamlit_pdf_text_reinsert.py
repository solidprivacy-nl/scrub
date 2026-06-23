"""Startup patch for PDF text extraction to restored TXT UI.

This patch runs after ``fix_streamlit_nested_expanders.py``. It adds a narrow
PDF-to-restored-TXT section inside ``Originele waarden terugzetten`` only.

It deliberately does not add restored PDF output, OCR, PDF-to-DOCX conversion,
AI calls, cloud processing, batch processing, storage, or export/download
semantic changes outside the approved restored TXT output for this workflow.

WP28C also uses this post-patch layer for MVP Scrub Key warnings and
acknowledgement gating after the main Scrub Key/reinsert UI has been injected.
The gating only disables high-risk buttons until the user checks the relevant
acknowledgement; it does not change JSON content, imported key handling,
reinsert helper behavior, output bytes, filenames or MIME types.
"""

from __future__ import annotations

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")


# Direct-source reinsert UI is now available. Do not mutate presidio_streamlit.py again.
if "from reinsert_mode_ui import render_reinsert_mode" in text:
    APP_FILE.write_text(text, encoding="utf-8")
    raise SystemExit(0)

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

# WP28C — MVP Scrub Key warning/acknowledgement UI implementation.
# These replacements run after the v13.x Scrub Key/reinsert UI is injected.
# They add acknowledgement gating only; they do not change helper behavior,
# exported JSON, imported key handling, restored file bytes, filenames or MIME types.
text = replace_once(
    text,
    '''            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
            )
''',
    '''            st.warning("Belangrijk: deze Scrub Key kan originele vertrouwelijke waarden herstellen. Download de sleutel alleen als u deze lokaal, apart en beveiligd kunt bewaren. Deel of upload de sleutel niet naar externe AI, e-mail of derden, tenzij dit bewust bedoeld en toegestaan is.")
            ack_scrub_key_export_risk = st.checkbox(
                "Ik begrijp dat deze Scrub Key herleidbaar is en dat ik deze niet samen met opgeschoonde uitvoer mag delen zonder geldige reden en toestemming.",
                key="ack_scrub_key_export_risk",
            )
            st.download_button(
                "Download Scrub Key (.json)",
                data=scrub_key_to_json(scrub_key),
                file_name="solidprivacy_scrub_key.json",
                mime="application/json",
                disabled=not ack_scrub_key_export_risk,
            )
            st.caption("Bewaar de Scrub Key niet onnodig in Downloads. Verplaats de sleutel naar een beveiligde lokale map of verwijder deze zodra hij niet meer nodig is.")
            with st.expander("Waar moet ik de Scrub Key bewaren?", expanded=False):
                st.markdown("Bewaar de Scrub Key lokaal, apart van de opgeschoonde tekst en bij voorkeur in een beveiligde map. Let op met Downloads, gedeelde computers, automatische cloudsync en back-ups.")
                st.markdown("Verwijder de Scrub Key handmatig zodra terugzetten niet meer nodig is en uw dossier- of organisatiebeleid dat toestaat. Let op: Scrub kan geen kopieën verwijderen uit Downloads, e-mail, cloudsync of back-ups.")
                st.markdown("Zonder Scrub Key kan Scrub originele waarden niet meer deterministisch terugzetten. Er is geen cloud- of serverherstel.")
''',
)

text = replace_once(
    text,
    '''    if st.button("Valideer en laad Scrub Key", key="load_scrub_key_import"):
''',
    '''    st.warning("Laad alleen een Scrub Key die bij dit document of dossier hoort. Een geldige sleutel kan originele vertrouwelijke waarden herstellen. Gebruik geen sleutel uit een ander dossier of van een onbekende bron.")
    ack_scrub_key_import_risk = st.checkbox(
        "Ik begrijp dat ik alleen een Scrub Key mag laden die bij dit document of dossier hoort.",
        key="ack_scrub_key_import_risk",
    )
    if st.button("Valideer en laad Scrub Key", key="load_scrub_key_import", disabled=not ack_scrub_key_import_risk):
''',
)

text = replace_once(
    text,
    '''if solidprivacy_work_mode == "Originele waarden terugzetten":
    st.caption("Originele waarden terugzetten: laad een Scrub Key en herstel placeholders lokaal in geplakte tekst.")
''',
    '''if solidprivacy_work_mode == "Originele waarden terugzetten":
    st.warning("Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens, dossierinformatie of andere vertrouwelijke gegevens bevatten.")
    st.caption("Terugzetten gebeurt lokaal met de geladen Scrub Key. Gebruik de Scrub Key niet in externe AI-diensten.")
    st.caption("Originele waarden terugzetten: laad een Scrub Key en herstel placeholders lokaal in geplakte tekst.")
''',
)

text = replace_once(
    text,
    '''    if st.button("Zet originele waarden lokaal terug", key="run_local_reinsert"):
''',
    '''    ack_reinsert_text_confidential = st.checkbox(
        "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
        key="ack_reinsert_text_confidential",
    )
    if st.button("Zet originele waarden lokaal terug", key="run_local_reinsert", disabled=not ack_reinsert_text_confidential):
''',
)

text = replace_once(
    text,
    '''        st.download_button(
            "Download herstelde tekst (.txt)",
            data=reinsert_result.get("text", ""),
            file_name="solidprivacy_herstelde_tekst.txt",
            mime="text/plain",
        )
''',
    '''        st.warning("De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.")
        ack_download_restored_text_confidential = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_text_confidential",
        )
        st.download_button(
            "Download herstelde tekst (.txt)",
            data=reinsert_result.get("text", ""),
            file_name="solidprivacy_herstelde_tekst.txt",
            mime="text/plain",
            disabled=not ack_download_restored_text_confidential,
        )
''',
)

text = replace_once(
    text,
    '''    if st.button("Zet TXT-bestand lokaal terug", key="run_txt_file_reinsert"):
''',
    '''    ack_reinsert_txt_confidential = st.checkbox(
        "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
        key="ack_reinsert_txt_confidential",
    )
    if st.button("Zet TXT-bestand lokaal terug", key="run_txt_file_reinsert", disabled=not ack_reinsert_txt_confidential):
''',
)

text = replace_once(
    text,
    '''        st.download_button(
            "Download hersteld TXT-bestand (.txt)",
            data=txt_reinsert_result.get("content_bytes", txt_reinsert_result.get("text", "").encode("utf-8")),
            file_name="solidprivacy_hersteld_txt_bestand.txt",
            mime="text/plain",
        )
''',
    '''        st.warning("De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.")
        ack_download_restored_txt_confidential = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_txt_confidential",
        )
        st.download_button(
            "Download hersteld TXT-bestand (.txt)",
            data=txt_reinsert_result.get("content_bytes", txt_reinsert_result.get("text", "").encode("utf-8")),
            file_name="solidprivacy_hersteld_txt_bestand.txt",
            mime="text/plain",
            disabled=not ack_download_restored_txt_confidential,
        )
''',
)

text = replace_once(
    text,
    '''    if st.button("Zet DOCX-bestand lokaal terug", key="run_docx_file_reinsert"):
''',
    '''    ack_reinsert_docx_confidential = st.checkbox(
        "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
        key="ack_reinsert_docx_confidential",
    )
    if st.button("Zet DOCX-bestand lokaal terug", key="run_docx_file_reinsert", disabled=not ack_reinsert_docx_confidential):
''',
)

text = replace_once(
    text,
    '''        st.download_button(
            "Download hersteld DOCX-bestand (.docx)",
            data=docx_reinsert_result.get("docx_bytes", b""),
            file_name="solidprivacy_hersteld_docx_bestand.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
''',
    '''        st.warning("De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.")
        ack_download_restored_docx_confidential = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_docx_confidential",
        )
        st.download_button(
            "Download hersteld DOCX-bestand (.docx)",
            data=docx_reinsert_result.get("docx_bytes", b""),
            file_name="solidprivacy_hersteld_docx_bestand.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            disabled=not ack_download_restored_docx_confidential,
        )
''',
)

text = replace_once(
    text,
    '''    if st.button("Zet PDF-tekst lokaal terug", key="run_pdf_text_file_reinsert"):
''',
    '''    ack_reinsert_pdf_text_confidential = st.checkbox(
        "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
        key="ack_reinsert_pdf_text_confidential",
    )
    if st.button("Zet PDF-tekst lokaal terug", key="run_pdf_text_file_reinsert", disabled=not ack_reinsert_pdf_text_confidential):
''',
)

text = replace_once(
    text,
    '''            st.download_button(
                "Download herstelde TXT uit PDF (.txt)",
                data=str(pdf_text_restored_text).encode("utf-8"),
                file_name="solidprivacy_herstelde_txt_uit_pdf.txt",
                mime="text/plain",
            )
''',
    '''            st.warning("De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.")
            ack_download_restored_pdf_text_confidential = st.checkbox(
                "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
                key="ack_download_restored_pdf_text_confidential",
            )
            st.download_button(
                "Download herstelde TXT uit PDF (.txt)",
                data=str(pdf_text_restored_text).encode("utf-8"),
                file_name="solidprivacy_herstelde_txt_uit_pdf.txt",
                mime="text/plain",
                disabled=not ack_download_restored_pdf_text_confidential,
            )
''',
)

text = text.replace(
    "De tekst bevat placeholders die niet in de actieve Scrub Key staan.",
    "De tekst bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.",
)
text = text.replace(
    "Het TXT-bestand bevat placeholders die niet in de actieve Scrub Key staan.",
    "Het TXT-bestand bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.",
)
text = text.replace(
    "Het DOCX-bestand bevat placeholders die niet in de actieve Scrub Key staan.",
    "Het DOCX-bestand bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.",
)
text = text.replace(
    "De Scrub Key bevat dubbele placeholders. Deze zijn niet automatisch teruggezet.",
    "De Scrub Key bevat dubbele placeholders. Deze mappings worden niet automatisch teruggezet om verkeerde herleiding te voorkomen.",
)

APP_FILE.write_text(text, encoding="utf-8")
