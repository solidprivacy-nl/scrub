from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEST = ROOT / "tests/test_scrub_key_binding_model.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label}, found {count}.")
    return text.replace(old, new, 1)


def main() -> None:
    text = TEST.read_text(encoding="utf-8")
    text = replace_once(
        text,
        'UI_PATH = ROOT / "reinsert_mode_ui.py"\n',
        'UI_PATH = ROOT / "reinsert_mode_ui.py"\n'
        'REINSERT_PATH = ROOT / "scrub_key_reinsert.py"\n',
        "reinsert path constant",
    )
    text = replace_once(
        text,
        'def test_model_package_does_not_integrate_current_export_or_reinsert_paths() -> None:\n'
        '    legacy_model = LEGACY_MODEL_PATH.read_text(encoding="utf-8")\n'
        '    ui = UI_PATH.read_text(encoding="utf-8")\n'
        '\n'
        '    assert \'SCRUB_KEY_SCHEMA_VERSION = "1.0"\' in legacy_model\n'
        '    assert "from scrub_key_binding import" not in legacy_model\n'
        '    assert "from scrub_key_binding import" not in ui\n'
        '    assert "document_binding_id" not in ui\n',
        'def test_model_package_stays_pure_while_sequential_integrations_use_it() -> None:\n'
        '    legacy_model = LEGACY_MODEL_PATH.read_text(encoding="utf-8")\n'
        '    ui = UI_PATH.read_text(encoding="utf-8")\n'
        '    reinsert = REINSERT_PATH.read_text(encoding="utf-8")\n'
        '\n'
        '    assert \'SCRUB_KEY_SCHEMA_VERSION = "1.0"\' in legacy_model\n'
        '    assert "from scrub_key_binding import" not in legacy_model\n'
        '    assert "from scrub_key_binding import" not in ui\n'
        '    assert "binding_status_notice" in ui\n'
        '    assert "validate_document_key_binding" in reinsert\n'
        '    assert "streamlit" not in reinsert\n',
        "obsolete no-integration contract",
    )
    TEST.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
