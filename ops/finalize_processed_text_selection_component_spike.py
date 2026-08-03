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
    "workpackage_claims/scrub_wp_processed_text_selection_component_spike.md",
    "Status: completed; standard and Streamlit smoke validation green; final clean regression pending",
    "Status: completed; GitHub Actions and Streamlit smoke validation green",
)

replace_once(
    "handover/workpackages/20260804_0100_processed_text_selection_component_spike.md",
    "Status: implemented; governance closeout and final clean regression pending",
    "Status: completed; GitHub Actions and Streamlit smoke validation green",
)
replace_once(
    "handover/workpackages/20260804_0100_processed_text_selection_component_spike.md",
    "- Governance closeout and final standard regression: pending.",
    "- Governance closeout applied and clean standard run #1989: **1126 tests passed in 10.87s**.",
)
replace_once(
    "handover/workpackages/20260804_0100_processed_text_selection_component_spike.md",
    "Green on standard run #1977 and dedicated Streamlit smoke run #1979. Final clean standard run pending after workflow restoration and governance closeout.",
    "Green. Standard run #1977 passed 1126 tests in 13.83s; dedicated Streamlit smoke run #1979 passed 1126 tests in 13.79s with AppTest and local health checks; clean post-governance run #1989 passed 1126 tests in 10.87s.",
)

replace_once(
    "WORKPACKAGES.md",
    "- final clean standard regression pending after governance/workflow restoration.",
    "- clean post-governance standard run #1989: 1126 tests passed in 10.87s.",
)

replace_once(
    "CHANGELOG.md",
    "- final clean standard regression pending.",
    "- clean post-governance standard run #1989: 1126 tests passed in 10.87s.",
)

replace_once(
    "PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE.md",
    "Initial standard PR run #1977 passed **1126 tests in 13.83s**.",
    "Initial standard PR run #1977 passed **1126 tests in 13.83s**. Clean post-governance run #1989 passed **1126 tests in 10.87s**.",
)
