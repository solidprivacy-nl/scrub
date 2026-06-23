from __future__ import annotations

import streamlit as st

from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result
from scrub_key_reinsert import reinsert_from_scrub_key
from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes
from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes


CONFIDENTIAL_OUTPUT_WARNING = (
    "Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer "
    "persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat "
    "zorgvuldig voordat u het deelt."
)

RESTORED_DOWNLOAD_WARNING = (
    "De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke "
    "waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet "
    "extern zonder controle en toestemming."
)


def _active_scrub_key() -> dict:
    return st.session_state.get("active_scrub_key", {})


def _has_active_scrub_key() -> bool:
    key = _active_scrub_key()
    return bool(key and key.get("items"))


def _render_result_report(title: str, result: dict, validation_issues: list) -> None:
    with st.expander(title, expanded=False):
        st.markdown(f"- Documenttype: {result.get('document_type', 'tekst')}")
        st.markdown(f"- Mappingregels totaal: {result.get('item_count', 0)}")
        st.markdown(f"- Actieve mappingregels: {result.get('active_item_count', 0)}")
        st.markdown(f"- Uitgesloten mappingregels: {result.get('excluded_item_count', 0)}")
        st.markdown(f"- Aantal teruggezette waarden: {result.get('replacement_count', 0)}")
        st.markdown(f"- Niet gevonden placeholders: {result.get('placeholders_not_found', [])}")
        st.markdown(f"- Onbekende placeholders in tekst: {result.get('unknown_placeholders', [])}")
        st.markdown(f"- Dubbele placeholders in sleutel: {result.get('duplicate_placeholders', [])}")
        st.markdown(f"- Validatieproblemen: {validation_issues}")
        st.markdown(f"- Lokaal uitgevoerd: {result.get('local_only') is True}")
        st.markdown(f"- AI-verwerking: {result.get('ai_processing') is True}")
        st.markdown(f"- Cloudverwerking: {result.get('cloud_processing') is True}")
        if result.get("limitations"):
            st.markdown(f"- Beperkingen: {result.get('limitations', [])}")


def _render_result_status(kind: str, result: dict, validation_issues: list) -> None:
    if validation_issues:
        st.warning(f"{kind} kan niet betrouwbaar worden uitgevoerd: " + "; ".join(validation_issues[:3]))
    elif result.get("replacement_count", 0) > 0:
        st.success(f"{result.get('replacement_count', 0)} waarde(n) lokaal teruggezet.")
    else:
        st.info("Er zijn geen placeholders teruggezet. Controleer of de juiste Scrub Key is geladen.")

    if result.get("unknown_placeholders"):
        st.warning(
            "De tekst bevat placeholders die niet in de geladen Scrub Key staan. "
            "Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel."
        )
    if result.get("duplicate_placeholders"):
        st.warning(
            "De Scrub Key bevat dubbele placeholders. Deze mappings worden niet automatisch "
            "teruggezet om verkeerde herleiding te voorkomen."
        )
    if result.get("placeholders_not_found"):
        st.caption("Niet alle mappingregels kwamen voor in de ingevoerde tekst.")


def render_reinsert_mode() -> None:
    st.subheader("1. Voeg Scrub Key toe")
    st.warning(
        "Let op: een Scrub Key maakt vervangen waarden lokaal herleidbaar. Dit is "
        "pseudonimisering, geen volledige anonimisering. Bewaar deze sleutel lokaal en deel "
        "deze niet met AI-diensten of derden tenzij dat bewust en toegestaan is."
    )
    st.caption(
        "Upload of plak een eerder geëxporteerde Scrub Key JSON. De sleutel wordt eerst "
        "gevalideerd en daarna pas na jouw klik gebruikt voor lokaal terugzetten."
    )

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

    st.warning(
        "Laad alleen een Scrub Key die bij dit document of dossier hoort. Een geldige sleutel "
        "kan originele vertrouwelijke waarden herstellen. Gebruik geen sleutel uit een ander "
        "dossier of van een onbekende bron."
    )
    ack_scrub_key_import_risk = st.checkbox(
        "Ik begrijp dat ik alleen een Scrub Key mag laden die bij dit document of dossier hoort.",
        key="ack_scrub_key_import_risk",
    )
    if st.button(
        "Valideer en laad Scrub Key",
        key="load_scrub_key_import",
        disabled=not ack_scrub_key_import_risk,
    ):
        if scrub_key_import_decode_error:
            st.error(scrub_key_import_decode_error)
        else:
            scrub_key_import_result = build_scrub_key_import_result(scrub_key_import_text)
            for warning in scrub_key_import_result.get("warnings", [IMPORT_PRIVACY_WARNING]):
                st.warning(warning)
            if scrub_key_import_result.get("ok"):
                st.success(
                    f"Scrub Key geldig: {scrub_key_import_result.get('item_count', 0)} "
                    "mappingregel(s) gevonden."
                )
                st.session_state["active_scrub_key"] = scrub_key_import_result.get("scrub_key")
                st.session_state["scrub_key_import_rows"] = scrub_key_import_result.get("mapping_rows", [])
                if "replacement_editor" in st.session_state:
                    del st.session_state["replacement_editor"]
                st.rerun()
            else:
                for error in scrub_key_import_result.get("errors", []):
                    st.error(error)

    st.divider()
    st.subheader("2. Voeg tekst of document toe")
    st.caption(
        "Kies één invoer: geplakte tekst, TXT, DOCX of tekstgebaseerde PDF. "
        "Terugzetten gebeurt lokaal met de geladen Scrub Key."
    )

    text_tab, txt_tab, docx_tab, pdf_tab = st.tabs(["Tekst plakken", "TXT", "DOCX", "PDF → TXT"])

    with text_tab:
        st.markdown("**Originele waarden terugzetten**")
        st.warning(CONFIDENTIAL_OUTPUT_WARNING)
        st.caption("Terugzetten gebeurt lokaal met de geladen Scrub Key. Gebruik de Scrub Key niet in externe AI-diensten.")
        reinsert_input_text = st.text_area(
            "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten",
            value="",
            height=180,
            key="reinsert_input_text",
        )
        ack_reinsert_text_confidential = st.checkbox(
            "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
            key="ack_reinsert_text_confidential",
        )
        if st.button(
            "Zet originele waarden lokaal terug",
            key="run_local_reinsert",
            disabled=not ack_reinsert_text_confidential,
        ):
            if not reinsert_input_text.strip():
                st.warning("Plak eerst tekst waarin placeholders staan die u lokaal wilt terugzetten.")
            else:
                st.session_state["reinsert_result"] = reinsert_from_scrub_key(
                    reinsert_input_text,
                    _active_scrub_key(),
                )

    with txt_tab:
        st.markdown("**TXT-bestand terugzetten**")
        st.warning(CONFIDENTIAL_OUTPUT_WARNING)
        st.caption("Upload een TXT-bestand met placeholders. Er wordt geen AI- of cloudverwerking gebruikt.")
        txt_reinsert_file = st.file_uploader(
            "Upload een TXT-bestand met placeholders",
            type=["txt"],
            key="txt_reinsert_file",
        )
        ack_reinsert_txt_confidential = st.checkbox(
            "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
            key="ack_reinsert_txt_confidential",
        )
        if st.button(
            "Zet TXT-bestand lokaal terug",
            key="run_txt_file_reinsert",
            disabled=not ack_reinsert_txt_confidential,
        ):
            if not _has_active_scrub_key():
                st.warning("Laad eerst een geldige Scrub Key voordat u een TXT-bestand lokaal terugzet.")
            elif txt_reinsert_file is None:
                st.warning("Upload eerst een TXT-bestand met placeholders.")
            else:
                st.session_state["txt_reinsert_result"] = reinsert_txt_bytes(
                    txt_reinsert_file.getvalue(),
                    _active_scrub_key(),
                    encoding="utf-8",
                )

    with docx_tab:
        st.markdown("**DOCX-bestand terugzetten**")
        st.warning(CONFIDENTIAL_OUTPUT_WARNING)
        st.caption("Upload een DOCX-bestand met placeholders. Er wordt geen AI- of cloudverwerking gebruikt.")
        st.info(
            "Let op: DOCX-terugzetten ondersteunt in deze versie normale documenttekst en tabellen. "
            "Headers, footers, opmerkingen, bijgehouden wijzigingen en placeholders die door Word "
            "over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund."
        )
        docx_reinsert_file = st.file_uploader(
            "Upload een DOCX-bestand met placeholders",
            type=["docx"],
            key="docx_reinsert_file",
        )
        ack_reinsert_docx_confidential = st.checkbox(
            "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
            key="ack_reinsert_docx_confidential",
        )
        if st.button(
            "Zet DOCX-bestand lokaal terug",
            key="run_docx_file_reinsert",
            disabled=not ack_reinsert_docx_confidential,
        ):
            if not _has_active_scrub_key():
                st.warning("Laad eerst een geldige Scrub Key voordat u een DOCX-bestand lokaal terugzet.")
            elif docx_reinsert_file is None:
                st.warning("Upload eerst een DOCX-bestand met placeholders.")
            else:
                st.session_state["docx_reinsert_result"] = reinsert_docx_bytes(
                    docx_reinsert_file.getvalue(),
                    _active_scrub_key(),
                )

    with pdf_tab:
        st.markdown("**PDF-tekst terugzetten naar TXT**")
        st.warning(
            "Let op: PDF-tekstextractie is niet altijd volledig. Deze functie maakt geen "
            "herstelde PDF. De uitvoer is alleen herstelde TXT-tekst. Scans of afbeelding-PDF’s "
            "worden niet ondersteund omdat OCR niet beschikbaar is."
        )
        st.warning(CONFIDENTIAL_OUTPUT_WARNING)
        st.caption("PDF-bestand terugzetten naar TXT. Scrub gebruikt hiervoor geen AI, geen cloudverwerking en geen OCR.")
        st.markdown("- Lokaal uitgevoerd: Ja")
        st.markdown("- AI-verwerking: Nee")
        st.markdown("- Cloudverwerking: Nee")
        st.markdown("- OCR gebruikt: Nee")
        st.markdown("- PDF-output: Nee")
        st.caption("Deze functie maakt geen herstelde PDF.")
        pdf_text_reinsert_file = st.file_uploader(
            "Upload een PDF-bestand met placeholders",
            type=["pdf"],
            key="pdf_text_reinsert_file",
        )
        ack_reinsert_pdf_text_confidential = st.checkbox(
            "Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.",
            key="ack_reinsert_pdf_text_confidential",
        )
        if st.button(
            "Zet PDF-tekst lokaal terug",
            key="run_pdf_text_file_reinsert",
            disabled=not ack_reinsert_pdf_text_confidential,
        ):
            if not _has_active_scrub_key():
                st.warning("Laad eerst een geldige Scrub Key voordat u PDF-tekst lokaal terugzet.")
            elif pdf_text_reinsert_file is None:
                st.warning("Upload eerst een PDF-bestand met placeholders.")
            else:
                st.session_state["pdf_text_reinsert_result"] = reinsert_pdf_text_bytes(
                    pdf_text_reinsert_file.getvalue(),
                    _active_scrub_key(),
                )

    st.divider()
    st.subheader("3. Controleer herstelrapport")

    for key, label in [
        ("reinsert_result", "Controleverslag terugzetten"),
        ("txt_reinsert_result", "Controleverslag TXT terugzetten"),
        ("docx_reinsert_result", "Controleverslag DOCX terugzetten"),
        ("pdf_text_reinsert_result", "Controleverslag PDF-tekst terugzetten"),
    ]:
        if key not in st.session_state:
            continue
        result = st.session_state[key]
        validation_issues = result.get("validation_issues", [])
        _render_result_status(label, result, validation_issues)
        if key == "reinsert_result":
            st.text_area("Herstelde tekst", value=result.get("text", ""), height=220, key="reinsert_output_text")
        elif key == "txt_reinsert_result":
            st.text_area("Herstelde TXT-tekst", value=result.get("text", ""), height=220, key="txt_reinsert_output_text")
        elif key == "pdf_text_reinsert_result":
            restored_text = result.get("restored_text") or result.get("text", "")
            if restored_text:
                st.text_area("Herstelde TXT-tekst uit PDF", value=restored_text, height=220, key="pdf_text_reinsert_output_text")
        _render_result_report(label, result, validation_issues)

    st.divider()
    st.subheader("4. Download herstelde output")

    if "reinsert_result" in st.session_state:
        result = st.session_state["reinsert_result"]
        st.warning(RESTORED_DOWNLOAD_WARNING)
        ack = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_text_confidential",
        )
        st.download_button(
            "Download herstelde tekst (.txt)",
            data=result.get("text", ""),
            file_name="solidprivacy_herstelde_tekst.txt",
            mime="text/plain",
            disabled=not ack,
        )

    if "txt_reinsert_result" in st.session_state:
        result = st.session_state["txt_reinsert_result"]
        st.warning(RESTORED_DOWNLOAD_WARNING)
        ack = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_txt_confidential",
        )
        st.download_button(
            "Download hersteld TXT-bestand (.txt)",
            data=result.get("content_bytes", result.get("text", "").encode("utf-8")),
            file_name="solidprivacy_hersteld_txt_bestand.txt",
            mime="text/plain",
            disabled=not ack,
        )

    if "docx_reinsert_result" in st.session_state:
        result = st.session_state["docx_reinsert_result"]
        st.warning(RESTORED_DOWNLOAD_WARNING)
        ack = st.checkbox(
            "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
            key="ack_download_restored_docx_confidential",
        )
        st.download_button(
            "Download hersteld DOCX-bestand (.docx)",
            data=result.get("docx_bytes", b""),
            file_name="solidprivacy_hersteld_docx_bestand.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            disabled=not ack,
        )

    if "pdf_text_reinsert_result" in st.session_state:
        result = st.session_state["pdf_text_reinsert_result"]
        validation_issues = result.get("validation_issues", [])
        unsupported_reason = result.get("unsupported_reason")
        restored_text = result.get("restored_text") or result.get("text", "")
        can_download = not validation_issues and not unsupported_reason and bool(str(restored_text).strip())
        if can_download:
            st.warning(RESTORED_DOWNLOAD_WARNING)
            ack = st.checkbox(
                "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.",
                key="ack_download_restored_pdf_text_confidential",
            )
            st.download_button(
                "Download herstelde TXT uit PDF (.txt)",
                data=str(restored_text).encode("utf-8"),
                file_name="solidprivacy_herstelde_txt_uit_pdf.txt",
                mime="text/plain",
                disabled=not ack,
            )
