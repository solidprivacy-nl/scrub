from __future__ import annotations

from pathlib import Path


UI = Path("reinsert_mode_ui.py")
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
CLAIM = Path(
    "workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md"
)
HANDOVER = Path(
    "handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md"
)


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count == 0 and new in text:
        return
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    replace_once(
        UI,
        '''        st.info(
            "Let op: DOCX-terugzetten ondersteunt in deze versie normale documenttekst en tabellen. "
            "Headers, footers, opmerkingen, bijgehouden wijzigingen en placeholders die door Word "
            "over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund."
        )
''',
        '''        st.info(
            "DOCX-terugzetten ondersteunt normale documenttekst, tabellen en bestaande kop- en voetteksten. "
            "Opmerkingen, bijgehouden wijzigingen, voetnoten/eindnoten, tekstvakken, metadata en placeholders "
            "die door Word over meerdere tekstfragmenten zijn gesplitst worden nog niet volledig ondersteund."
        )
''',
        "DOCX reinsert capability copy",
    )

    replace_once(
        CLAIM,
        "- Helper-level document reinsert only; no Streamlit UI changes.\n",
        "- Helper-level document reinsert plus capability-copy alignment only; no new Streamlit controls or flow.\n",
        "claim UI boundary",
    )

    replace_once(
        CHANGELOG,
        "- `scrub_key_document_reinsert.py`\n- `mvp_phase6_document_cases.py`\n",
        "- `scrub_key_document_reinsert.py`\n- `reinsert_mode_ui.py`\n- `mvp_phase6_document_cases.py`\n",
        "changelog file list",
    )
    replace_once(
        CHANGELOG,
        "- `tests/test_mvp_document_hygiene_fidelity_hardening.py`\n- `tests/test_mvp_document_fidelity_report.py`\n",
        "- `tests/test_mvp_document_hygiene_fidelity_hardening.py`\n- `tests/test_mvp_document_fidelity_report.py`\n- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
        "changelog test list",
    )
    replace_once(
        CHANGELOG,
        "- DOCX body paragraphs and tables remain supported.\n- `word/header*.xml` and `word/footer*.xml` text nodes are now restored deterministically.\n",
        "- DOCX body paragraphs and tables remain supported.\n- `word/header*.xml` and `word/footer*.xml` text nodes are now restored deterministically.\n- The DOCX reinsert capability copy now matches the supported body/table/header/footer scope.\n",
        "changelog implementation result",
    )
    replace_once(
        CHANGELOG,
        "- Streamlit UI, runtime or dependencies.\n",
        "- Streamlit controls/flow, runtime or dependencies; only capability copy was aligned.\n",
        "changelog intentional boundary",
    )

    replace_once(
        WORKPACKAGES,
        "- Preserved body/table behavior and unrelated OOXML package parts.\n",
        "- Preserved body/table behavior and unrelated OOXML package parts.\n- Aligned the existing DOCX reinsert information copy with the supported body/table/header/footer scope without adding controls.\n",
        "workpackages summary",
    )

    replace_once(
        HANDOVER,
        "- `scrub_key_document_reinsert.py`\n- `mvp_phase6_document_cases.py`\n",
        "- `scrub_key_document_reinsert.py`\n- `reinsert_mode_ui.py`\n- `mvp_phase6_document_cases.py`\n",
        "handover changed files",
    )
    replace_once(
        HANDOVER,
        "- `tests/test_mvp_document_hygiene_fidelity_hardening.py`\n- `tests/test_mvp_document_fidelity_report.py`\n",
        "- `tests/test_mvp_document_hygiene_fidelity_hardening.py`\n- `tests/test_mvp_document_fidelity_report.py`\n- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
        "handover added tests",
    )
    replace_once(
        HANDOVER,
        "- Current Phase 6 synthetic matrix tests.\n",
        "- Current Phase 6 synthetic matrix tests.\n- Source-level DOCX/PDF capability-copy contract tests.\n",
        "handover tests",
    )

    print("DOCX reinsert capability copy aligned.")


if __name__ == "__main__":
    main()
