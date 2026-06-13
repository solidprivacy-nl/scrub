from pathlib import Path


PLAN = Path("DOCX_HYGIENE_AUDIT_UI_PLAN.md").read_text(encoding="utf-8")
PLAN_LOWER = PLAN.lower()


def _assert_all_present(needles: list[str]) -> None:
    for needle in needles:
        assert needle in PLAN


def _assert_all_present_lower(needles: list[str]) -> None:
    for needle in needles:
        assert needle.lower() in PLAN_LOWER


def test_plan_preserves_report_only_boundary():
    _assert_all_present([
        "report-only",
        "Rapportage-only",
        "Geen schoonmaak toegepast",
        "Geen exportblokkade toegepast",
    ])
    _assert_all_present([
        "cleaning_applied: false",
        "export_blocking: false",
        "export_semantics_changed: false",
    ])


def test_plan_blocks_clean_docx_claims():
    _assert_all_present([
        "Geen schone-DOCX garantie",
        "safe_to_claim_clean: false",
        "no clean-DOCX guarantee",
    ])
    _assert_all_present_lower([
        "must not be described as clean DOCX export",
        "no clean-DOCX guarantee",
        "safe_to_claim_clean",
    ])


def test_plan_forbids_export_blocking_in_first_ui_surface():
    _assert_all_present([
        "export blocking",
        "Blokkeer export",
        "no export blocking",
    ])
    _assert_all_present_lower([
        "does not change export/download behavior",
        "export/download buttons remain unchanged",
        "must not silently change DOCX output bytes, filenames, MIME types, or export availability",
    ])


def test_plan_forbids_docx_cleaning_and_removal():
    _assert_all_present([
        "Verwijder opmerkingen",
        "Accepteer/verwijder bijgehouden wijzigingen",
        "Verwijder metadata",
        "no cleaning/removal",
    ])
    _assert_all_present_lower([
        "no cleaning applied",
        "geen opmerkingen of wijzigingen verwijderd",
        "no cleaning/removal",
    ])


def test_plan_forbids_scrub_key_and_reinsert_changes():
    _assert_all_present([
        "Geen wijziging aan Scrub Key",
        "Geen wijziging aan terugzetten/originele waarden",
        "Scrub Key changes",
        "reinsert behavior changes",
    ])
    _assert_all_present_lower([
        "no mutation of scrub key state",
        "no mutation of reinsert output",
        "scrub key changes",
        "reinsert behavior changes",
    ])


def test_plan_forbids_cloud_ai_persistence_and_real_data():
    _assert_all_present([
        "no cloud document processing",
        "no AI calls",
        "no persistence of document bytes",
        "no real data",
    ])
    _assert_all_present_lower([
        "no cloud processing",
        "real-data fixtures",
        "uploaded DOCX bytes already provided by the user in the current session",
    ])


def test_plan_requires_expected_visible_ui_labels():
    _assert_all_present([
        "DOCX-hygiënecontrole — rapportage, geen schoonmaak",
        "Risiconiveau",
        "Kopteksten",
        "Voetteksten",
        "Opmerkingen / kantlijncommentaren",
        "Wijzigingen bijhouden",
        "Geen schone-DOCX garantie",
    ])


def test_plan_defines_severity_behavior_without_export_blocking():
    _assert_all_present([
        "### `low`",
        "### `medium`",
        "### `high`",
        "high-risk warning",
        "section expanded by default",
        "export/download buttons remain unchanged",
    ])
    assert PLAN.count("export/download buttons remain unchanged") >= 3


def test_plan_requires_future_implementation_gate_after_contract_tests_and_approval():
    _assert_all_present([
        "WP39C — DOCX hygiene audit UI contract tests",
        "WP39D — DOCX hygiene audit UI implementation",
        "Only after those contract tests are green and coordinator approval is explicit",
    ])
    _assert_all_present_lower([
        "later implementation must remain report-only",
        "separate approved policy package changes export-blocking or clean-DOCX semantics",
    ])


def test_contract_tests_use_no_real_personal_data_examples():
    rendered = PLAN + Path(__file__).read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
