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
    "workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md",
    "Status: completed as planning; GitHub Actions pending",
    "Status: completed as planning; GitHub Actions green",
)

replace_once(
    "handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md",
    "Status: completed as planning; GitHub Actions pending",
    "Status: completed as planning; GitHub Actions green",
)
replace_once(
    "handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md",
    "- GitHub Actions: pending planning PR.\n- Hugging Face sync: not functionally relevant; documentation/tests only.\n- App verification: not applicable; no UI or runtime behavior changed.",
    "- GitHub Actions: green on PR #59 run #1937 — 1015 tests passed in 11.64s.\n- Hugging Face sync: not functionally relevant; documentation/tests only.\n- App verification: not applicable; no UI or runtime behavior changed.",
)
replace_once(
    "handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md",
    "Pending.",
    "Green on PR #59 run #1937 — 1015 tests passed in 11.64s. One final clean run follows this status-only update.",
)

replace_once(
    "WORKPACKAGES.md",
    "Status: completed as planning; GitHub Actions pending.",
    "Status: completed as planning; GitHub Actions green.",
)
replace_once(
    "WORKPACKAGES.md",
    "Implementation authorized: no\n```",
    "Implementation authorized: no\nGitHub Actions: PR #59 run #1937 — 1015 passed in 11.64s\n```",
)

replace_once(
    "CHANGELOG.md",
    "Status: completed as planning; validation pending.",
    "Status: completed as planning; validation green.",
)
replace_once(
    "CHANGELOG.md",
    "- full GitHub Actions pending;\n- Hugging Face sync not functionally relevant;\n- app verification not applicable because no product behavior changed.",
    "- PR #59 run #1937: 1015 tests passed in 11.64s;\n- one final clean regression follows the status-only update;\n- Hugging Face sync not functionally relevant;\n- app verification not applicable because no product behavior changed.",
)
