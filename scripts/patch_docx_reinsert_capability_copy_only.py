from __future__ import annotations

from pathlib import Path


path = Path("reinsert_mode_ui.py")
text = path.read_text(encoding="utf-8")
old = '''        st.info(
            "Let op: DOCX-terugzetten ondersteunt in deze versie normale documenttekst en tabellen. "
            "Headers, footers, opmerkingen, bijgehouden wijzigingen en placeholders die door Word "
            "over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund."
        )
'''
new = '''        st.info(
            "DOCX-terugzetten ondersteunt normale documenttekst, tabellen en bestaande kop- en voetteksten. "
            "Opmerkingen, bijgehouden wijzigingen, voetnoten/eindnoten, tekstvakken, metadata en placeholders "
            "die door Word over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund."
        )
'''
if new in text:
    print("DOCX capability copy already aligned.")
elif text.count(old) == 1:
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("DOCX capability copy aligned.")
else:
    raise SystemExit(f"Expected one old DOCX copy block, found {text.count(old)}")
