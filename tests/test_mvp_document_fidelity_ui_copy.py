from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "reinsert_mode_ui.py"
THIS_TEST = ROOT / "tests" / "test_mvp_document_fidelity_ui_copy.py"


def test_docx_reinsert_copy_matches_supported_parts() -> None:
    text = UI.read_text(encoding="utf-8")

    for marker in [
        "normale documenttekst, tabellen en bestaande ",
        "kop- en voetteksten",
        "Opmerkingen, bijgehouden wijzigingen, voetnoten/eindnoten",
        "tekstvakken, metadata",
        "over meerdere tekstfragmenten zijn ",
        "gesplitst worden nog niet volledig ondersteund",
    ]:
        assert marker in text
    assert "Headers, footers" not in text


def test_pdf_txt_only_and_no_ocr_copy_remains_unchanged() -> None:
    text = UI.read_text(encoding="utf-8")

    assert "Deze functie maakt geen herstelde PDF" in text
    assert "OCR niet beschikbaar" in text
    assert "PDF-output: Nee" in text


def test_copy_contract_does_not_import_streamlit_or_product_ui() -> None:
    tree = ast.parse(THIS_TEST.read_text(encoding="utf-8"))
    imported_roots: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "reinsert_mode_ui" not in imported_roots
