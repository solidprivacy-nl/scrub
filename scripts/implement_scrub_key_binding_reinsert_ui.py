from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "reinsert_mode_ui.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} block, found {count}.")
    return text.replace(old, new, 1)


def main() -> None:
    text = UI.read_text(encoding="utf-8")

    text = replace_once(
        text,
        "from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n",
        "from scrub_key_binding_reinsert_status import binding_status_notice\n"
        "from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result\n",
        "status-helper import",
    )

    text = replace_once(
        text,
        "        st.markdown(f\"- Validatieproblemen: {validation_issues}\")\n"
        "        st.markdown(f\"- Lokaal uitgevoerd: {result.get('local_only') is True}\")\n",
        "        binding_notice = binding_status_notice(result)\n"
        "        st.markdown(f\"- Document-/sleutelstatus: {binding_notice.get('status_label')}\")\n"
        "        st.markdown(f\"- Documentmatch geverifieerd: {result.get('verified_document_match') is True}\")\n"
        "        st.markdown(f\"- Legacy sleutel zonder binding: {result.get('legacy_unbound') is True}\")\n"
        "        st.markdown(f\"- Documentcodes in document: {result.get('document_binding_ids', [])}\")\n"
        "        st.markdown(f\"- Documentcode in sleutel: {result.get('key_binding_id', '')}\")\n"
        "        st.markdown(f\"- Mapping-controlewaarde geldig: {result.get('mapping_digest_valid')}\")\n"
        "        st.markdown(f\"- Bindingwaarschuwingen: {result.get('binding_warnings', [])}\")\n"
        "        st.markdown(f\"- Validatieproblemen: {validation_issues}\")\n"
        "        st.markdown(f\"- Lokaal uitgevoerd: {result.get('local_only') is True}\")\n",
        "binding audit report",
    )

    text = replace_once(
        text,
        "def _render_result_status(kind: str, result: dict, validation_issues: list) -> None:\n"
        "    if validation_issues:\n",
        "def _render_result_status(kind: str, result: dict, validation_issues: list) -> None:\n"
        "    binding_notice = binding_status_notice(result)\n"
        "    if binding_notice.get(\"level\") == \"success\":\n"
        "        st.success(binding_notice.get(\"message\"))\n"
        "    elif binding_notice.get(\"level\") == \"warning\":\n"
        "        st.warning(binding_notice.get(\"message\"))\n"
        "    elif binding_notice.get(\"level\") == \"error\":\n"
        "        st.error(binding_notice.get(\"message\"))\n"
        "\n"
        "    if validation_issues:\n",
        "binding result status",
    )

    UI.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
