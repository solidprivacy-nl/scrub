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
    "WORKPACKAGES.md",
    "Validation:\n- exact finalized tree validated in GitHub Actions run #2044;\n- frontend component tests and full Python regression required green before merge;\n- Hugging Face sync and app verification pending after merge.",
    "Validation:\n- cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only;\n- final clean PR run #2047: 1146 Python tests passed in 11.97s;\n- Hugging Face sync and app verification pending after merge.",
)

replace_once(
    "CHANGELOG.md",
    "Validation:\n- exact finalized tree validated in GitHub Actions run #2044;\n- automated merge is permitted only after frontend and full Python regressions succeed;\n- Hugging Face sync and live app verification pending.",
    "Validation:\n- cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only;\n- final clean PR run #2047: 1146 Python tests passed in 11.97s;\n- Hugging Face sync and live app verification pending.",
)

replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "- `RISK_REGISTER.md`",
    "- `RELEASE_NOTES.md`\n- `RISK_REGISTER.md`",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "- Controlled production patch and exact final governance validated in GitHub Actions run #2044.\n- Frontend component tests and the complete Python regression must succeed before merge.\n- Hugging Face sync pending merge.\n- App verification pending merge and synchronization.",
    "- Cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only.\n- Final clean PR run #2047: 1146 Python tests passed in 11.97s.\n- Hugging Face sync pending merge.\n- App verification pending merge and synchronization.",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Exact finalized tree is validated in run #2044; merge remains conditional on frontend and full Python regression success.",
    "Green. Frontend component tests passed in cleanup run #2044; final clean PR run #2047 passed 1146 Python tests in 11.97s. One final documentation-only PR run follows this evidence correction.",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Merge only after the exact final branch passes the complete regression. Then verify GitHub-to-Hugging-Face synchronization and request focused live app verification before starting cross-flow regression.",
    "Merge after the final documentation-only PR run is green. Then verify GitHub-to-Hugging-Face synchronization and request focused live app verification before starting cross-flow regression.",
)
