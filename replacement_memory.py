import json
from pathlib import Path


# If Hugging Face persistent storage is attached, /data is the preferred location.
# If /data does not exist, this falls back to the app folder, but that is not guaranteed
# to survive restarts/rebuilds.
DATA_DIR = Path("/data") if Path("/data").exists() else Path(".")
MEMORY_FILE = DATA_DIR / "replacement_memory.json"


def get_memory_file_path():
    return str(MEMORY_FILE)


def load_remembered_replacements():
    if not MEMORY_FILE.exists():
        return []

    try:
        with MEMORY_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        cleaned = []

        for row in data:
            find_text = str(row.get("find", "")).strip()
            replace_with = str(row.get("replace_with", "")).strip()
            entity_type = str(row.get("entity_type", "REMEMBERED")).strip() or "REMEMBERED"

            if not find_text or not replace_with:
                continue

            cleaned.append(
                {
                    "include": True,
                    "remember": True,
                    "find": find_text,
                    "replace_with": replace_with,
                    "entity_type": entity_type,
                    "score": "",
                }
            )

        return cleaned

    except Exception:
        return []


def save_remembered_replacements(rows):
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    deduped = {}

    for row in rows:
        find_text = str(row.get("find", "")).strip()
        replace_with = str(row.get("replace_with", "")).strip()
        entity_type = str(row.get("entity_type", "REMEMBERED")).strip() or "REMEMBERED"

        if not find_text or not replace_with:
            continue

        deduped[find_text] = {
            "find": find_text,
            "replace_with": replace_with,
            "entity_type": entity_type,
        }

    final_rows = list(deduped.values())

    with MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(final_rows, f, ensure_ascii=False, indent=2)

    return len(final_rows)


def clear_remembered_replacements():
    if MEMORY_FILE.exists():
        MEMORY_FILE.unlink()