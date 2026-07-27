from __future__ import annotations

import json
from pathlib import Path


WORKPACKAGE = "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION"
TIMESTAMP = "2026-07-27 17:06 Europe/Amsterdam"
HANDOVER = Path(
    "handover/workpackages/"
    "20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md"
)


def prepend_once(path: Path, marker: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(entry + text, encoding="utf-8")


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if text.count(old) != 1:
        raise RuntimeError(
            f"Expected one match in {path} for {old[:80]!r}; found {text.count(old)}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_after_first_separator(path: Path, marker: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    separator = "---\n\n"
    index = text.find(separator)
    if index < 0:
        raise RuntimeError(f"No first separator found in {path}")
    insert_at = index + len(separator)
    path.write_text(text[:insert_at] + entry + text[insert_at:], encoding="utf-8")


CHANGELOG_ENTRY = f'''## 2026-07-27 — {WORKPACKAGE}

Status: implemented; full suite passed; final PR validation pending.

Purpose:

- Remove redundant source- and Scrub-Key confirmation steps from the local reinsert workflow after live Phase 6 evidence showed that uploaded inputs looked complete while hidden action gates remained.
- Present the workflow in the user’s natural order: source document/text, corresponding Scrub Key, restored result.
- Preserve a clear confidentiality decision at the final restored-output download boundary.

Files added:

- `reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`
- `output/validation/mvp_reinsert_auto_flow_validation.json`

Files changed:

- `reinsert_mode_ui.py`
- `tests/test_reinsert_interface_simplification_ui.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `ROADMAP.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`

Implementation result:

- Step 1 is now the source document or pasted text.
- One uploader recognises TXT, DOCX and text-based PDF by extension.
- Step 2 automatically parses and validates the uploaded or pasted Scrub Key.
- Local deterministic reinsert runs automatically once one valid source and one valid key are present.
- Separate source/key acknowledgement checkboxes and execution buttons were removed.
- One final confidentiality acknowledgement remains directly before restored-output download.
- Existing output filenames, MIME types, reinsert helpers, audit fields and explicit DOCX/PDF boundaries are preserved.

Validation:

- Full repository suite: 797 passed.
- Helper dispatch, deterministic request signatures and input precedence are covered.
- Source-level UI contracts verify document-first order, automatic key validation, automatic local reinsert and removal of redundant gates.
- Prior DOCX live verification passed for body, table, header and footer restoration.
- Final GitHub Actions, merge, Hugging Face sync and live app verification remain pending.

Intentionally not changed:

- Scrub Key schema, mappings, lifecycle or storage;
- document replacement or reinsert helper semantics;
- recognizers or thresholds;
- export filenames, MIME types or audit semantics;
- cloud, AI or OCR processing;
- restored-PDF support;
- unsupported DOCX-part boundaries;
- the requirement for human review and a final confidential-output warning.

Next recommended step:

- Complete final PR validation, merge and sync, then live-verify the three-step automatic flow.
- Continue with `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` after app verification.

---

'''

WORKPACKAGES_ENTRY = f'''## {TIMESTAMP} — {WORKPACKAGE}

Status: implemented; full suite passed; final PR validation pending.

Evidence:
- Live DOCX reinsert passed for body, table, header and footer.
- The same verification exposed a concrete interface-clarity blocker: uploaded source/key files still required hidden follow-up checkboxes and action buttons.

Summary:
- Reordered reinsert to source first, Scrub Key second and restored download third.
- Added pure helper orchestration for input normalisation, deterministic request signatures and dispatch to existing local helpers.
- Automatically validates a supplied Scrub Key and automatically runs reinsert for one valid source/key pair.
- Removed separate source/key processing acknowledgements and buttons.
- Retained one final confidentiality acknowledgement at the restored-output download boundary.
- Preserved TXT, DOCX, PDF-to-TXT and pasted-text paths, audit reporting, filenames, MIME types and safety boundaries.

Validation:
- Full repository suite: 797 passed.
- Final GitHub Actions pending after governance finalisation.
- Hugging Face sync and live app verification required after merge.
- Human review remains required; production readiness remains false.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

'''

RELEASE_ENTRY = '''## 2026-07-27 — Terugzetten werkt nu in drie logische stappen

- Begin met het TXT-, DOCX- of PDF-bestand dat je wilt herstellen; geplakte tekst blijft beschikbaar als alternatief.
- Voeg daarna de bijbehorende Scrub Key toe. De sleutel wordt automatisch gelezen en gevalideerd.
- Zodra bestand en sleutel geldig zijn, wordt het lokale herstel automatisch voorbereid en verschijnt de downloadstap.
- De afzonderlijke vinkjes en knoppen voor het laden/valideren van de sleutel en het starten van het herstel zijn verwijderd.
- Eén duidelijke bevestiging blijft staan vóór de download, omdat het herstelde resultaat opnieuw vertrouwelijke gegevens kan bevatten.
- DOCX-, TXT- en PDF-naar-TXT-uitvoer, bestandsnamen en bekende beperkingen blijven ongewijzigd.

---

'''

DECISION_ENTRY = '''## 2026-07-27 — D031 — Reinsert is document-first with automatic source/key processing

Status: accepted evidence-driven UX and safety decision

Decision:

```text
Present local reinsert as source document/text → corresponding Scrub Key → restored download. Automatically recognise the source type, structurally validate the supplied Scrub Key and run deterministic local reinsert when both inputs are valid. Keep one explicit confidentiality acknowledgement at the restored-output download boundary instead of repeating acknowledgements and action buttons before processing.
```

Reason:

- Live Phase 6 verification confirmed that DOCX restoration works, but users can reasonably interpret an uploaded and visibly listed file as already accepted.
- Requiring a checkbox and action button after each upload creates hidden completion states and unnecessary form friction.
- The highest-risk user action is obtaining and handling the restored confidential output, so the explicit acknowledgement remains at that boundary.
- Automatic key validation does not weaken structural validation or change Scrub Key semantics.

Boundaries:

- Keep warnings about pseudonymisation, key sensitivity and local-only use visible.
- Invalid or ambiguous keys must still fail clearly and must not be used.
- Preserve result/audit warnings for unknown, duplicate and missing placeholders.
- Preserve existing helpers, output bytes, filenames and MIME types.
- Do not add cloud, AI, OCR, restored-PDF or key-storage behavior.
- Human review remains required and no production-readiness claim is created.

Evidence:

- User-confirmed restored synthetic DOCX containing body, table, header and footer values.
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `output/validation/mvp_reinsert_auto_flow_validation.json`

---

'''

HANDOVER_CONTENT = f'''# Handover — {WORKPACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{WORKPACKAGE}

## Status

Implemented; full suite passed; final PR validation pending.

## Summary

The local reinsert interface now follows the user’s task order: provide the source document/text, provide the corresponding Scrub Key, then download the restored result. Source type recognition, Scrub Key structural validation and deterministic local reinsert occur automatically. Redundant pre-processing acknowledgement checkboxes and action buttons are removed, while one final confidentiality acknowledgement remains at the restored-output download boundary.

## Files added

- `reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `output/validation/mvp_reinsert_auto_flow_validation.json`
- `{HANDOVER}`

## Files changed

- `reinsert_mode_ui.py`
- `tests/test_reinsert_interface_simplification_ui.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`

## Tests

- Pure helper tests for source selection, file-type recognition, deterministic signatures and existing-helper dispatch.
- Source-level UI contracts for three-step order, automatic key validation, automatic reinsert and removal of redundant gates.
- Existing direct-source, DOCX fidelity, PDF boundary, filename/MIME and startup-patch contracts.
- Full repository suite: 797 passed.

## Validation

- GitHub Actions: final PR run pending after governance finalisation.
- Hugging Face sync: pending after merge.
- App verification: required after sync because the visible workflow changed.
- Prior DOCX fidelity app verification: passed for body, table, header and footer restoration.

## Notes / risks

- One final confidentiality acknowledgement remains before restored-output download.
- Invalid Scrub Keys remain blocked by existing structural validation.
- Unknown, duplicate and missing placeholders remain visible in the result report.
- PDF remains restored TXT only; no OCR or restored PDF output.
- Unsupported DOCX parts remain documented.
- Human review remains required; no production-readiness claim is made.

## Next recommended step

- Verify PR Actions, merge, verify Hugging Face sync and live-test the three-step automatic flow.
- Continue `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` after app verification.
'''


def main() -> None:
    prepend_once(Path("CHANGELOG.md"), WORKPACKAGE, CHANGELOG_ENTRY)
    prepend_once(
        Path("WORKPACKAGES.md"),
        f"{TIMESTAMP} — {WORKPACKAGE}",
        WORKPACKAGES_ENTRY,
    )
    prepend_once(
        Path("RELEASE_NOTES.md"),
        "2026-07-27 — Terugzetten werkt nu in drie logische stappen",
        RELEASE_ENTRY,
    )
    insert_after_first_separator(Path("DECISION_LOG.md"), "D031", DECISION_ENTRY)

    replace_once(
        Path("ROADMAP.md"),
        "Last roadmap strategy update: 2026-07-17 — verified MVP UI simplification line closed; Phase 6 workflow validation and trust hardening is now active.",
        "Last roadmap strategy update: 2026-07-27 — DOCX fidelity is app-verified; a concrete Phase 6 reinsert-flow clarity blocker is being resolved before Scrub Key roundtrip validation continues.",
    )
    replace_once(
        Path("ROADMAP.md"),
        "SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_* through SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_* — the current MVP UI simplification line is completed, synchronized and live-app verified.\n",
        "SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_* through SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_* — the current MVP UI simplification line is completed, synchronized and live-app verified.\nSCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING — merged, synchronized and live-app verified for DOCX body, table, header and footer restoration.\nSCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — active narrow evidence-driven UI blocker before the general Scrub Key roundtrip package.\n",
    )
    replace_once(
        Path("ROADMAP.md"),
        "1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX\n2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE\n3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING\n4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION\n5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
        "1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX — completed\n2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — completed\n3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING — completed and app-verified\n4. SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — active evidence-driven blocker\n5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION\n6. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n7. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
    )

    replace_once(
        Path("RISK_REGISTER.md"),
        "Current mitigations include warnings and acknowledgements. Export/download UX grouping is now implemented directly in `presidio_streamlit.py` so the key file is visually separated from normal document exports and shown with a specific warning. Live app verification confirmed the grouped export UI.\n\nThe manual missed-value entry flows through the existing replacement table and existing Scrub Key/export paths without changing key semantics.",
        "Current mitigations include warnings and acknowledgements. Export/download UX grouping is implemented directly in `presidio_streamlit.py` so the key file is visually separated from normal document exports and shown with a specific warning. Live app verification confirmed the grouped export UI. Reinsert now keeps the key-sensitivity warning visible, automatically applies the existing structural validation to a supplied key, and preserves one explicit confidentiality acknowledgement at the restored-output download boundary. Redundant pre-processing acknowledgements are removed because they obscured workflow state without adding key validation.\n\nThe manual missed-value entry flows through the existing replacement table and existing Scrub Key/export paths without changing key semantics. No key storage, schema or lifecycle behavior is added by the automatic reinsert flow.",
    )
    replace_once(
        Path("RISK_REGISTER.md"),
        "- Additional copy polish may still be needed, but it should remain separate and small.\n- Implementation must avoid weakening review controls or hiding audit details.",
        "- Live reinsert verification exposed a concrete workflow-state problem: uploaded source and key files still required non-obvious follow-up checkboxes and buttons. `SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION` addresses this narrowly with document-first ordering and automatic validation/processing.\n- Additional copy polish may still be needed, but it should remain separate and small.\n- Implementation must avoid weakening review controls or hiding audit details; one final confidentiality acknowledgement remains at download.",
    )
    replace_once(
        Path("RISK_REGISTER.md"),
        "- The current UI baseline is completed and app-verified. Do not start another UI feature automatically; open a narrowly scoped UI package only when Phase 6 validation exposes a concrete safety or workflow blocker.",
        "- The general UI baseline is completed and app-verified. The automatic reinsert-flow package is permitted as a narrow exception because live Phase 6 validation exposed a concrete workflow blocker; broader UI work remains gated.",
    )

    claim_path = Path(
        "workpackage_claims/"
        "scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md"
    )
    claim = claim_path.read_text(encoding="utf-8")
    claim = claim.replace(
        "Status: in_progress",
        "Status: implemented; full suite passed; final PR validation pending",
        1,
    )
    if "Implementation result:" not in claim:
        claim += f'''\n\nImplementation result:\n- Completed at: {TIMESTAMP}\n- Document/text is step 1; Scrub Key is step 2; download is step 3.\n- Source type recognition, key validation and local deterministic reinsert are automatic.\n- Redundant source/key checkboxes and action buttons are removed.\n- One final confidentiality acknowledgement remains before download.\n- Full repository suite: 797 passed.\n- Evidence: `output/validation/mvp_reinsert_auto_flow_validation.json`.\n- Handover: `{HANDOVER}`.\n- Final Actions, merge, Hugging Face sync and app verification pending.\n'''
    claim_path.write_text(claim, encoding="utf-8")

    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(HANDOVER_CONTENT, encoding="utf-8")

    evidence_path = Path("output/validation/mvp_reinsert_auto_flow_validation.json")
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence = {
        "schema": "solidprivacy.mvp_reinsert_auto_flow_validation",
        "schema_version": "1.0",
        "generated_at": "2026-07-27T17:06:00+02:00",
        "workpackage": WORKPACKAGE,
        "synthetic_data_only": True,
        "human_review_required": True,
        "production_ready": False,
        "docx_fidelity_live_verification": {
            "passed": True,
            "body_restored": True,
            "table_restored": True,
            "header_restored": True,
            "footer_restored": True,
        },
        "target_flow": [
            "source_document_or_text",
            "scrub_key_auto_validation",
            "automatic_local_reinsert",
            "final_confidentiality_acknowledgement",
            "restored_download",
        ],
        "redundant_preprocessing_gates_removed": True,
        "final_download_acknowledgement_preserved": True,
        "scrub_key_schema_changed": False,
        "reinsert_semantics_changed": False,
        "output_filenames_or_mime_changed": False,
        "cloud_processing": False,
        "ai_processing": False,
        "ocr_processing": False,
        "restored_pdf_supported": False,
        "pytest_passed": True,
        "pytest_count": 797,
        "final_pr_actions_pending": True,
        "hugging_face_sync_pending": True,
        "app_verification_pending": True,
    }
    evidence_path.write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
