"""Simplify the default Streamlit execution interface at app startup.

Presentation-only patch. It collapses secondary controls and keeps document
processing, replacement, export, Scrub Key and reinsert semantics unchanged.
"""

from __future__ import annotations

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")


def replace_once(source: str, old: str, new: str) -> str:
    if new in source:
        return source
    if old in source:
        return source.replace(old, new, 1)
    return source


def wrap_block_by_markers(source: str, start_marker: str, end_marker: str, opener: str) -> str:
    if opener in source:
        return source

    lines = source.splitlines(keepends=True)
    start = next((i for i, line in enumerate(lines) if start_marker in line), None)
    if start is None:
        return source
    end = next((i for i in range(start + 1, len(lines)) if end_marker in lines[i]), None)
    if end is None:
        return source

    indent = lines[start][: len(lines[start]) - len(lines[start].lstrip())]
    wrapped = [f"{indent}{opener}\n"]
    for line in lines[start:end]:
        wrapped.append(f"{indent}    {line[len(indent):]}")
    return "".join(lines[:start] + wrapped + lines[end:])


def apply_execution_interface_simplification(source: str) -> str:
    text = source

    text = replace_once(
        text,
        'st.sidebar.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))\n',
        'with st.sidebar.expander("Wat doet deze controlemodus?", expanded=False):\n    st.info(PROFILE_DESCRIPTIONS.get(profile_label, ""))\n',
    )

    text = wrap_block_by_markers(
        text,
        'if st_recognition_profile == "Dutch Legal Strict":',
        'try:',
        'with st.expander("Controle-instellingen en herkenning", expanded=False):',
    )

    text = replace_once(text, 'height=300,\n    key="text_input",', 'height=240,\n    key="text_input",')

    text = replace_once(
        text,
        '            "Centrale side-by-side reviewweergave. Brontekst links, verwerkte tekst rechts. "\n            "Synchroon scrollen en optionele markeringen blijven visuele hulp."',
        '            "Controleer het resultaat. Details en extra hulpmiddelen staan standaard ingeklapt."',
    )

    text = replace_once(
        text,
        '            "Vink fout-positieven uit, pas placeholders aan, voeg handmatige vervangingen toe "\n            "en vink Onthouden aan voor vervangingen die je opnieuw wilt gebruiken. "\n            "Mogelijke kandidaten staan standaard uitgevinkt. De vervangtabel blijft leidend."',
        '            "Controleer alleen wat nodig is. De vervangtabel blijft leidend en blijft beschikbaar voor detailcontrole."',
    )

    text = replace_once(
        text,
        'with st.expander("Mogelijk extra te controleren waarden", expanded=bool(candidate_rows)):',
        'with st.expander("Mogelijk extra te controleren waarden", expanded=False):',
    )

    text = wrap_block_by_markers(
        text,
        'st.markdown("**Gemiste waarde toevoegen**")',
        'if manual_submit:',
        'with st.expander("Gemiste waarde toevoegen", expanded=False):',
    )

    text = wrap_block_by_markers(
        text,
        'st.subheader("4. Onthoud herbruikbare vervangingen")',
        'st.subheader("5. Exporteer resultaat")',
        'with st.expander("Herbruikbare vervangingen", expanded=False):',
    )
    text = replace_once(text, 'st.subheader("5. Exporteer resultaat")', 'st.subheader("4. Exporteer resultaat")')

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
''',
        '''        st.caption(
            "Download de opgeschoonde documenten. Scrub Key en auditbestanden staan in aparte secties."
        )
''',
    )

    text = wrap_block_by_markers(
        text,
        'st.markdown("**Scrub Key**")',
        'st.markdown("**Audit en technische bestanden**")',
        'with st.expander("Scrub Key downloaden", expanded=False):',
    )

    text = wrap_block_by_markers(
        text,
        'st.markdown("**Audit en technische bestanden**")',
        'if docx_bytes is not None:',
        'with st.expander("Auditbestanden downloaden", expanded=False):',
    )

    return text


def main() -> None:
    source = APP_FILE.read_text(encoding="utf-8")
    patched = apply_execution_interface_simplification(source)
    if patched != source:
        APP_FILE.write_text(patched, encoding="utf-8")


if __name__ == "__main__":
    main()
