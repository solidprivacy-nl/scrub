# Explicit second push after the closeout workflow exists.
from __future__ import annotations

import json
from pathlib import Path


CONFIRMED_AT = "2026-08-03T20:35:00+02:00"
CONFIRMED_AT_DISPLAY = "2026-08-03 20:35 Europe/Amsterdam"
ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_once(path: str, anchor: str, addition: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(anchor)
    if count != 1:
        raise RuntimeError(f"Expected exactly one anchor in {path}, found {count}: {anchor!r}")
    target.write_text(text.replace(anchor, addition + anchor, 1), encoding="utf-8")


report_path = ROOT / "output/validation/care_profile_hf_sync_verification.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
report["schema_version"] = "1.2"
report["functional_app_verification"] = True
report["functional_app_verification_status"] = "confirmed_all_green"
report["app_verified_at"] = CONFIRMED_AT
report["app_verification_source"] = "coordinator_user_confirmation"
report["app_verification_confirmation"] = "alles groen"
report["app_verification_checks"] = {
    "four_profile_choices_visible_in_approved_order": True,
    "legal_profile_remains_initial_default": True,
    "care_description_and_eight_synthetic_examples_visible": True,
    "patient_and_client_identifiers_selected_for_replacement": True,
    "review_selected_care_context_selected_and_shows_controle_nodig": True,
    "unresolved_care_reference_candidates_unchecked": True,
    "clinical_meaning_remains_readable": True,
    "existing_profiles_review_export_scrub_key_and_reinsert_present": True,
    "no_script_execution_error": True,
}
report["human_review_required"] = True
report["production_ready"] = False
report_path.write_text(
    json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

replace_once(
    "tests/test_care_profile_hf_sync_verification.py",
    'assert report["schema_version"] == "1.1"',
    'assert report["schema_version"] == "1.2"',
)
replace_once(
    "tests/test_care_profile_hf_sync_verification.py",
    '''def test_app_verification_remains_open_until_user_confirmation():
    report = _report()

    assert report["functional_app_verification"] is False
    assert (
        report["functional_app_verification_status"]
        == "pending_coordinator_user_confirmation"
    )
    assert report["human_review_required"] is True
    assert report["production_ready"] is False
''',
    '''def test_app_verification_is_confirmed_by_user():
    report = _report()

    assert report["functional_app_verification"] is True
    assert report["functional_app_verification_status"] == "confirmed_all_green"
    assert report["app_verified_at"] == "2026-08-03T20:35:00+02:00"
    assert report["app_verification_source"] == "coordinator_user_confirmation"
    assert report["app_verification_confirmation"] == "alles groen"
    assert all(report["app_verification_checks"].values())
    assert report["human_review_required"] is True
    assert report["production_ready"] is False
''',
)

replace_once(
    "CARE_PROFILE_APP_VERIFICATION.md",
    "Status: technical deployment verified; visible app verification pending coordinator/user confirmation.",
    "Status: completed and app-verified after technical deployment verification.",
)
insert_once(
    "CARE_PROFILE_APP_VERIFICATION.md",
    "## Closeout rule\n",
    f'''## Verification result\n\nCoordinator/user confirmation received at `{CONFIRMED_AT_DISPLAY}`:\n\n```text\nalles groen\n```\n\nConfirmed visible behavior:\n\n- four profiles are visible in the approved order;\n- Legal remains the initial default;\n- the Care description and eight synthetic examples are present;\n- patient/client identifiers are selected for replacement;\n- review-selected care context remains selected and shows `Controle nodig`;\n- unresolved care-reference candidates remain unchecked;\n- clinical meaning remains readable;\n- Legal, General, International, review, export, Scrub Key and reinsert remain present;\n- no Script execution error is visible.\n\n''',
)
replace_once(
    "CARE_PROFILE_APP_VERIFICATION.md",
    "The package may be marked completed only after the coordinator/user confirms the visible behavior above. Technical deployment evidence alone does not establish functional or production readiness.",
    "The coordinator/user confirmed all visible checks. The package is completed and app-verified. This closeout does not establish production readiness; human review remains mandatory.",
)

replace_once(
    "workpackage_claims/scrub_wp_care_profile_app_verify.md",
    "Status: Actions/sync verified; awaiting coordinator/user app verification",
    "Status: completed and app-verified after Actions/sync verification",
)
replace_once(
    "workpackage_claims/scrub_wp_care_profile_app_verify.md",
    "Do not mark completed until technical sync/health evidence is green and the coordinator/user confirms the visible app behavior.",
    f"Closeout gate passed: technical sync/health evidence is green and the coordinator/user confirmed `alles groen` at {CONFIRMED_AT_DISPLAY}.",
)

replace_once(
    "WORKPACKAGES.md",
    "Status: implemented; Actions/sync verified; awaiting coordinator/user app verification.",
    "Status: completed and app-verified after Actions/sync verification.",
)
replace_once(
    "WORKPACKAGES.md",
    "Functional app verification: pending",
    "Functional app verification: confirmed — alles groen",
)
replace_once(
    "WORKPACKAGES.md",
    "Pending coordinator/user checks:",
    "Confirmed coordinator/user checks:",
)
replace_once(
    "WORKPACKAGES.md",
    "- do not close or merge the verification-only package until the coordinator/user confirms the visible behavior.",
    f"- completed: coordinator/user confirmed `alles groen` at {CONFIRMED_AT_DISPLAY}; final verification-only CI run #1909 passed 998 tests.",
)
replace_once(
    "WORKPACKAGES.md",
    "- app verification is blocked until GitHub-to-Hugging-Face sync for the merged UI integration is independently confirmed.",
    "- completed downstream: synchronization, deployed app behavior and verification-only regression are green.",
)
replace_once(
    "WORKPACKAGES.md",
    "Status: implemented and regression-green; merge, sync and deployed app verification pending.",
    "Status: completed, merged, synchronized and app-verified.",
)
replace_once(
    "WORKPACKAGES.md",
    "- `SCRUB-WP_CARE_PROFILE_APP_VERIFY` after merge and deployment sync.",
    "- `SCRUB-WP_CARE_PROFILE_APP_VERIFY` completed after deployment sync and coordinator/user confirmation.",
)

replace_once(
    "CHANGELOG.md",
    "Status: technical deployment verified; visible app verification pending.",
    "Status: completed and app-verified after technical deployment verification.",
)
replace_once(
    "CHANGELOG.md",
    "- recorded functional app verification as pending rather than claiming success.",
    f"- recorded coordinator/user confirmation `alles groen` at {CONFIRMED_AT_DISPLAY};\n- confirmed all nine visible verification checks and retained the non-production/human-review boundary.",
)
replace_once(
    "CHANGELOG.md",
    "- verification-evidence tests and normal branch regression pending PR creation.",
    "- verification-only run #1908 passed 998 tests; final closeout run #1909 passed 998 tests in 10.45s.",
)
replace_once(
    "CHANGELOG.md",
    "- final clean run pending after governance finalization.",
    "- final clean run #1906 passed: 995 tests in 9.96s.",
)
replace_once(
    "CHANGELOG.md",
    "Status: implemented and regression-tested; deployment verification pending.",
    "Status: completed, deployed and app-verified.",
)
replace_once(
    "CHANGELOG.md",
    "- final clean run pending after governance finalization;\n- Hugging Face sync pending merge;\n- app verification pending deployment.",
    "- final clean integration run #1885 passed: 986 tests;\n- Hugging Face synchronization verified byte-for-byte for 12/12 relevant files;\n- deployed app verification confirmed `alles groen` by the coordinator/user.",
)

replace_once(
    "ROADMAP.md",
    "Generic NER remains outside this matrix. The next gate is deployed app verification after GitHub-to-Hugging-Face sync is confirmed.",
    "Generic NER remains outside this matrix. GitHub-to-Hugging-Face synchronization and deployed app behavior were confirmed on 2026-08-03; the current-web Zorgfilter line is completed and app-verified. Desktop UX work remains separately gated by Phase 9 and explicit approval.",
)

replace_once(
    "RISK_REGISTER.md",
    "The current Streamlit integration now registers the sixteen care recognizers and applies the central profile policy. Review-selected care detections are selected by default but visibly marked `Controle nodig`; unresolved strongly labelled references remain unchecked candidates. Regression run #1877 passed 983 tests and existing export, Scrub Key and reinsert behavior remains unchanged. Risk R10 remains mitigating because cross-profile regression, deployment sync, generic-NER observation and live app verification are still pending.",
    "The current Streamlit integration registers the sixteen care recognizers and applies the central profile policy. Review-selected care detections are selected by default but visibly marked `Controle nodig`; unresolved strongly labelled references remain unchecked candidates. Cross-profile regression, byte-for-byte deployment verification and live app verification are green, including confirmation that clinical meaning remains readable and existing review, export, Scrub Key and reinsert flows remain present. Risk R10 remains mitigating because synthetic and bounded app evidence does not establish production recall, precision or rare-case safety; human review remains mandatory.",
)

replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "Status: technical deployment verified; coordinator/user app verification pending",
    "Status: completed and app-verified after technical deployment verification",
)
replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "The technical deployment is verified. No product code was changed. Functional closeout remains blocked on coordinator/user verification of the visible app behavior.",
    f"The technical deployment is verified. No product code was changed. The coordinator/user confirmed `alles groen` at {CONFIRMED_AT_DISPLAY}, completing the functional closeout.",
)
replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "- `ROADMAP.md` — pending verification-status finalizer\n- `WORKPACKAGES.md` — pending verification-status finalizer\n- `CHANGELOG.md` — pending verification-status finalizer\n- `RISK_REGISTER.md` — pending verification-status finalizer",
    "- `ROADMAP.md` — current-web Zorgfilter line marked completed and app-verified\n- `WORKPACKAGES.md` — package and downstream gates closed\n- `CHANGELOG.md` — final CI and user verification recorded\n- `RISK_REGISTER.md` — R10 mitigation evidence updated without closing production risk\n- `CARE_PROFILE_APP_VERIFICATION.md` — visible verification result recorded\n- `output/validation/care_profile_hf_sync_verification.json` — functional verification fields completed\n- `tests/test_care_profile_hf_sync_verification.py` — closeout evidence assertions updated\n- `workpackage_claims/scrub_wp_care_profile_app_verify.md` — claim marked completed",
)
replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "- Verification-branch normal regression run: pending after PR creation.",
    "- Verification-only run #1908 passed: 998 tests in 10.07s.\n- Final closeout run #1909 passed: 998 tests in 10.45s.",
)
replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "Pending coordinator/user confirmation. Required visible checks are documented in `CARE_PROFILE_APP_VERIFICATION.md`.",
    f"Confirmed. The coordinator/user reported `alles groen` at {CONFIRMED_AT_DISPLAY}; all documented visible checks passed.",
)
replace_once(
    "handover/workpackages/20260803_1912_care_profile_app_verify.md",
    "Coordinator/user opens the deployed Space and follows `CARE_PROFILE_APP_VERIFICATION.md`. After confirmation, update the evidence status, complete governance closeout and merge the verification-only PR.",
    "Merge verification-only PR #55. Do not automatically open desktop UX or installer work; continue with the active risk-driven Phase 6 queue and explicit coordinator approval gates.",
)

for temporary_path in (
    ROOT / "ops/finalize_care_profile_app_verify_complete.py",
    ROOT / ".github/workflows/finalize-care-profile-app-verify-complete.yml",
):
    temporary_path.unlink(missing_ok=True)
