from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "selection_mask_action.py",
    "def parse_inspect_event(event: Any) -> InspectSelectionEvent:\n    mapping = _validate_common_envelope(event, INSPECT_ACTION)\n\n    document_scope_key = _require_string(",
    "def parse_inspect_event(event: Any) -> InspectSelectionEvent:\n    mapping = _validate_common_envelope(event, INSPECT_ACTION)\n    event_id = str(mapping[\"event_id\"])\n\n    document_scope_key = _require_string(",
)

replace_once(
    "tests/test_selection_mask_action.py",
    "    assert \"components.html\" not in source\n    assert \"javascript\" not in source.lower()\n    assert \"localstorage\" not in source.lower()\n",
    "    assert \"components.html\" not in source\n    assert \"components.declare_component\" not in source\n    assert \"localstorage\" not in source.lower()\n",
)
