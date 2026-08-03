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
    "workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md",
    "Status: implemented; corrected GitHub Actions run green; final clean regression pending",
    "Status: completed; GitHub Actions green",
)

replace_once(
    "handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md",
    "Status: implemented; clean GitHub Actions regression pending",
    "Status: completed; GitHub Actions green",
)
replace_once(
    "handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md",
    "- Clean standard PR regression: pending on this status-only commit.",
    "- Clean standard PR run #1970: **1106 tests passed in 10.71s**.",
)
replace_once(
    "handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md",
    "Corrected implementation green on run #1961. This connector-authored status commit triggers the clean standard PR regression.",
    "Green. Corrected implementation run #1961 passed 1106 tests in 10.66s; clean standard PR run #1970 passed 1106 tests in 10.71s. One final status-only regression follows this closeout update.",
)

replace_once(
    "WORKPACKAGES.md",
    "Status: implemented; final clean GitHub Actions regression pending.",
    "Status: completed; GitHub Actions green.",
)
replace_once(
    "WORKPACKAGES.md",
    "- final clean regression pending after governance updates.",
    "- clean standard run #1970: 1106 tests passed in 10.71s.",
)
replace_once(
    "WORKPACKAGES.md",
    "Status: implemented; GitHub Actions pending.\n\nApproval evidence:",
    "Status: completed; GitHub Actions green.\n\nApproval evidence:",
)

replace_once(
    "CHANGELOG.md",
    "Status: implemented; final clean validation pending.",
    "Status: completed; validation green.",
)
replace_once(
    "CHANGELOG.md",
    "- final clean standard regression pending.",
    "- clean standard run #1970: 1106 tests passed in 10.71s.",
)
replace_once(
    "CHANGELOG.md",
    "Status: implemented; validation pending.\n\nPurpose:\n- Convert the approved processed-text selection direction",
    "Status: completed; validation green.\n\nPurpose:\n- Convert the approved processed-text selection direction",
)
replace_once(
    "CHANGELOG.md",
    "- full GitHub Actions pending;\n- Hugging Face sync not functionally relevant;\n- app verification not applicable because no runtime behavior changed.",
    "- clean contract run #1954: 1027 tests passed in 11.48s;\n- Hugging Face sync not functionally relevant;\n- app verification not applicable because no runtime behavior changed.",
)

replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md",
    "- PR run #1961: **1106 tests passed in 10.66s**.",
    "- PR run #1961: **1106 tests passed in 10.66s**;\n- clean standard PR run #1970: **1106 tests passed in 10.71s**.",
)
