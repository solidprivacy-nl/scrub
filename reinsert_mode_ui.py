from __future__ import annotations

import hashlib

import streamlit as st

from reinsert_auto_flow import (
    build_reinsert_request_signature,
    build_reinsert_source,
    run_reinsert_request,
)
from scrub_key_binding_reinsert_status import binding_status_notice
from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result


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

_RESULT_KEYS = {
    "text": "reinsert_result",
    "txt": "txt_reinsert_result",
    "docx": "docx_reinsert_result",
    "pdf": "pdf_text_reinsert_result",
}

_SOURCE_LABELS = {
    "text": "Geplakte tekst",
    "txt": "TXT-bestand",
    "docx": "DOCX-bestand",
    "pdf": "PDF-bestand",
}


def _active_scrub_key() -> dict:
    return st.session_state.get("active_scrub_key", {})


def _clear_reinsert_results() -> None:
    for key in _RESULT_KEYS.values():
        st.session_state.pop(key, None)
    st.session_state.pop("auto_reinsert_request_signature", None)
    st.session_state.pop("auto_reinsert_error", None)
    st.session_state["ack_auto_reinsert_download_confidential"] = False


def _clear_active_scrub_key() -> None:
    st.session_state.pop("active_scrub_key", None)
    st.session_state.pop("scrub_key_import_rows", None)
    st.session_state.pop("auto_reinsert_scrub_key_signature", None)
    _clear_reinsert_results()


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
        binding_notice = binding_status_notice(result)
        st.markdown(f"- Document-/sleutelstatus: {binding_notice.get('status_label')}")
        st.markdown(f"- Documentmatch geverifieerd: {result.get('verified_document_match') is True}")
        st.markdown(f"- Legacy sleutel zonder binding: {result.get('legacy_unbound') is True}")
        st.markdown(f"- Documentcodes in document: {result.get('document_binding_ids', [])}")
        st.markdown(f"- Documentcode in sleutel: {result.get('key_binding_id', '')}")
        st.markdown(f"- Mapping-controlewaarde geldig: {result.get('mapping_digest_valid')}")
        st.markdown(f"- Bindingwaarschuwingen: {result.get('binding_warnings', [])}")
        st.markdown(f"- Validatieproblemen: {validation_issues}")
        st.markdown(f"- Lokaal uitgevoerd: {result.get('local_only') is True}")
        st.markdown(f"- AI-verwerking: {result.get('ai_processing') is True}")
        st.markdown(f"- Cloudverwerking: {result.get('cloud_processing') is True}")
        if result.get("limitations"):
            st.markdown(f"- Beperkingen: {result.get('limitations', [])}")


def _render_result_status(kind: str, result: dict, validation_issues: list) -> None:
    binding_notice = binding_status_notice(result)
    if binding_notice.get("level") == "success":
        st.success(binding_notice.get("message"))
    elif binding_notice.get("level") == "warning":
        st.warning(binding_notice.get("message"))
    elif binding_notice.get("level") == "error":
        st.error(binding_notice.get("message"))

    if validation_issues:
        st.warning(
            f"{kind} kan niet betrouwbaar worden uitgevoerd: "
            + "; ".join(validation_issues[:3])
        )
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
        st.caption("Niet alle mappingregels kwamen voor in het ingevoerde document.")


def _decode_scrub_key_upload(uploaded_file) -> tuple[str, str | None]:
    if uploaded_file is None:
        return "", None
    try:
        return uploaded_file.getvalue().decode("utf-8"), None
    except UnicodeDecodeError:
        return "", "Scrub Key bestand is geen geldige UTF-8 tekst."


def _load_scrub_key_automatically(scrub_key_text: str) -> dict | None:
    if not scrub_key_text.strip():
        _clear_active_scrub_key()
        return None

    result = build_scrub_key_import_result(scrub_key_text)
    if not result.get("ok"):
        _clear_active_scrub_key()
        for error in result.get("errors", []):
            st.error(error)
        return None

    signature = hashlib.sha256(scrub_key_text.encode("utf-8")).hexdigest()
    if st.session_state.get("auto_reinsert_scrub_key_signature") != signature:
        st.session_state["active_scrub_key"] = result.get("scrub_key")
        st.session_state["scrub_key_import_rows"] = result.get("mapping_rows", [])
        st.session_state["auto_reinsert_scrub_key_signature"] = signature
        st.session_state.pop("replacement_editor", None)
        _clear_reinsert_results()

    st.success(
        f"Scrub Key herkend en geldig: {result.get('item_count', 0)} mappingregel(s)."
    )
    return result.get("scrub_key")


def _result_can_download(source_type: str, result: dict) -> bool:
    if result.get("validation_issues"):
        return False
    if source_type == "text":
        return bool(str(result.get("text", "")).strip())
    if source_type == "txt":
        return bool(result.get("content_bytes") or str(result.get("text", "")).strip())
    if source_type == "docx":
        return bool(result.get("docx_bytes"))
    if source_type == "pdf":
        restored_text = result.get("restored_text") or result.get("text", "")
        return not result.get("unsupported_reason") and bool(str(restored_text).strip())
    return False


def _render_download(source_type: str, result: dict, acknowledged: bool) -> None:
    if source_type == "text":
        restored_text = result.get("text", "")
        if acknowledged:
            st.text_area(
                "Herstelde tekst",
                value=restored_text,
                height=220,
                key="reinsert_output_text",
            )
        st.download_button(
            "Download herstelde tekst (.txt)",
            data=restored_text,
            file_name="solidprivacy_herstelde_tekst.txt",
            mime="text/plain",
            disabled=not acknowledged,
            use_container_width=True,
        )
        return

    if source_type == "txt":
        st.download_button(
            "Download hersteld TXT-bestand (.txt)",
            data=result.get("content_bytes", result.get("text", "").encode("utf-8")),
            file_name="solidprivacy_hersteld_txt_bestand.txt",
            mime="text/plain",
            disabled=not acknowledged,
            use_container_width=True,
        )
        return

    if source_type == "docx":
        st.download_button(
            "Download hersteld DOCX-bestand (.docx)",
            data=result.get("docx_bytes", b""),
            file_name="solidprivacy_hersteld_docx_bestand.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            disabled=not acknowledged,
            use_container_width=True,
        )
        return

    restored_text = result.get("restored_text") or result.get("text", "")
    st.download_button(
        "Download herstelde TXT uit PDF (.txt)",
        data=str(restored_text).encode("utf-8"),
        file_name="solidprivacy_herstelde_txt_uit_pdf.txt",
        mime="text/plain",
        disabled=not acknowledged,
        use_container_width=True,
    )


def render_reinsert_mode() -> None:
    st.subheader("1. Voeg het bestand toe dat je wilt herstellen")
    st.caption(
        "Upload één TXT-, DOCX- of tekstgebaseerd PDF-bestand. Het bestand wordt lokaal "
        "herkend; een afzonderlijke startknop is niet nodig."
    )

    source_file = st.file_uploader(
        "Upload het bestand met placeholders",
        type=["txt", "docx", "pdf"],
        key="reinsert_source_file",
        help="DOCX wordt als DOCX hersteld. PDF wordt alleen naar herstelde TXT omgezet.",
    )
    with st.expander("Of plak tekst in plaats van een bestand", expanded=False):
        pasted_text = st.text_area(
            "Plak tekst met placeholders",
            value="",
            height=180,
            key="reinsert_source_pasted_text",
        )

    try:
        source = build_reinsert_source(
            file_name=getattr(source_file, "name", None),
            file_bytes=source_file.getvalue() if source_file is not None else None,
            pasted_text=pasted_text,
        )
    except ValueError as exc:
        source = None
        st.error(str(exc))

    if source is not None:
        source_type = source["source_type"]
        source_name = source.get("file_name") or "geplakte tekst"
        st.success(f"{_SOURCE_LABELS[source_type]} ontvangen: {source_name}")
        if source.get("pasted_text_ignored"):
            st.caption("Het geüploade bestand heeft voorrang op de geplakte tekst.")
        if source_type == "docx":
            st.info(
                "DOCX-terugzetten ondersteunt normale documenttekst, tabellen en bestaande "
                "kop- en voetteksten. Opmerkingen, bijgehouden wijzigingen, voetnoten/eindnoten, "
                "tekstvakken, metadata en placeholders die over meerdere tekstfragmenten zijn "
                "gesplitst worden nog niet volledig ondersteund."
            )
        elif source_type == "pdf":
            st.warning(
                "PDF-tekstextractie is niet altijd volledig. De uitvoer is alleen herstelde TXT. "
                "Deze functie maakt geen herstelde PDF. OCR niet beschikbaar. PDF-output: Nee."
            )

    st.divider()
    st.subheader("2. Voeg de bijbehorende Scrub Key toe")
    st.warning(
        "Een Scrub Key maakt deze tekst omkeerbaar. Dit is pseudonimisering, geen volledige "
        "anonimisering. Bewaar de sleutel lokaal en beveiligd. Deel de Scrub Key niet met "
        "externe AI-diensten, tenzij dit bewust is bedoeld en toegestaan."
    )
    st.caption(
        "De Scrub Key wordt na upload automatisch gelezen en gevalideerd. Alleen een geldige "
        "sleutel wordt gebruikt voor lokaal terugzetten."
    )

    scrub_key_file = st.file_uploader(
        "Upload de Scrub Key (.json)",
        type=["json"],
        key="reinsert_scrub_key_file",
        help="Gebruik alleen de lokale Scrub Key die bij dit document of dossier hoort.",
    )
    with st.expander("Of plak Scrub Key JSON", expanded=False):
        scrub_key_paste = st.text_area(
            "Plak Scrub Key JSON",
            value="",
            height=120,
            key="reinsert_scrub_key_paste",
        )

    uploaded_key_text, decode_error = _decode_scrub_key_upload(scrub_key_file)
    if scrub_key_file is not None and scrub_key_paste.strip():
        st.caption("Het geüploade Scrub Key-bestand heeft voorrang op de geplakte JSON.")
    scrub_key_text = uploaded_key_text or scrub_key_paste

    active_key = None
    if decode_error:
        _clear_active_scrub_key()
        st.error(decode_error)
    elif scrub_key_text.strip():
        active_key = _load_scrub_key_automatically(scrub_key_text)
        st.caption(IMPORT_PRIVACY_WARNING)
    else:
        _clear_active_scrub_key()

    st.divider()
    st.subheader("3. Download het herstelde resultaat")

    if source is None:
        st.info("Upload eerst het bestand of plak de tekst die je wilt herstellen.")
        return
    if not active_key:
        st.info("Upload daarna de bijbehorende geldige Scrub Key.")
        return

    request_signature = build_reinsert_request_signature(source, active_key)
    source_type = source["source_type"]
    result_key = _RESULT_KEYS[source_type]

    if st.session_state.get("auto_reinsert_request_signature") != request_signature:
        _clear_reinsert_results()
        try:
            result = run_reinsert_request(source, active_key)
        except Exception:
            st.session_state["auto_reinsert_error"] = (
                "Het bestand kon niet veilig worden hersteld. Controleer of het bestand geldig "
                "is en of de Scrub Key bij dit document hoort."
            )
        else:
            st.session_state[result_key] = result
            st.session_state["auto_reinsert_request_signature"] = request_signature

    if st.session_state.get("auto_reinsert_error"):
        st.error(st.session_state["auto_reinsert_error"])
        return

    result = st.session_state.get(result_key)
    if not result:
        st.error("Er is geen herstelresultaat beschikbaar.")
        return

    validation_issues = result.get("validation_issues", [])
    _render_result_status("Terugzetten", result, validation_issues)
    _render_result_report("Controleverslag terugzetten", result, validation_issues)

    if not _result_can_download(source_type, result):
        return

    st.warning(CONFIDENTIAL_OUTPUT_WARNING)
    st.warning(RESTORED_DOWNLOAD_WARNING)
    acknowledged = st.checkbox(
        "Ik begrijp dat het herstelde resultaat weer vertrouwelijke originele waarden bevat.",
        key="ack_auto_reinsert_download_confidential",
    )
    _render_download(source_type, result, acknowledged)
