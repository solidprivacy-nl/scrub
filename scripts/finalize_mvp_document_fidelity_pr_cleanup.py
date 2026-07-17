from __future__ import annotations

from pathlib import Path


SELF = Path(__file__)
TEMP_PATCH = Path("scripts/patch_docx_reinsert_capability_copy_only.py")


def replace_once(path: str, old: str, new: str) -> None:
    file = Path(path)
    text = file.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new, 1)
    file.write_text(text, encoding="utf-8")


def main() -> None:
    replace_once(
        "CHANGELOG.md",
        "- `tests/test_mvp_document_fidelity_ui_copy.py`\n- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
        "- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
    )
    replace_once(
        "CHANGELOG.md",
        "- The DOCX reinsert capability copy now matches the supported body/table/header/footer scope.\n- The DOCX reinsert capability copy now matches the supported body/table/header/footer scope.\n",
        "- The DOCX reinsert capability copy now matches the supported body/table/header/footer scope.\n",
    )
    replace_once(
        "WORKPACKAGES.md",
        "- Aligned the existing DOCX reinsert information copy with the supported body/table/header/footer scope without adding controls.\n- Aligned the existing DOCX reinsert information copy with the supported body/table/header/footer scope without adding controls.\n",
        "- Aligned the existing DOCX reinsert information copy with the supported body/table/header/footer scope without adding controls.\n",
    )
    replace_once(
        "handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md",
        "- `tests/test_mvp_document_fidelity_ui_copy.py`\n- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
        "- `tests/test_mvp_document_fidelity_ui_copy.py`\n",
    )
    replace_once(
        "handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md",
        "- Source-level DOCX/PDF capability-copy contract tests.\n- Source-level DOCX/PDF capability-copy contract tests.\n",
        "- Source-level DOCX/PDF capability-copy contract tests.\n",
    )
    replace_once(
        "workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md",
        "Next step:\n- Add failing contract tests, implement multi-part OOXML reinsert narrowly, rerun the synthetic matrix and related document/Scrub Key/hygiene suites, then update governance evidence and handover.\n",
        "Next step:\n- Run final PR validation, merge after green Actions, verify Hugging Face sync and request live DOCX reinsert verification.\n",
    )
    if TEMP_PATCH.exists():
        TEMP_PATCH.unlink()
    SELF.unlink()


if __name__ == "__main__":
    main()
