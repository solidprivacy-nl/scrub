from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one {label} in {path.name}, found {count}.")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend(path: Path, section: str) -> None:
    text = path.read_text(encoding="utf-8")
    if section.strip() in text:
        raise RuntimeError(f"Section already present in {path.name}.")
    path.write_text(section + text, encoding="utf-8")


def main() -> None:
    evidence = {
        "workpackage": "SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION",
        "status": "implemented_full_actions_passed",
        "github_actions_run_number": 1789,
        "github_actions_conclusion": "success",
        "dual_read_legacy_v1_0": True,
        "dual_read_bound_v1_1": True,
        "bound_match_verified": True,
        "legacy_unbound_compatibility": True,
        "fail_closed_statuses": [
            "binding_mismatch",
            "mixed_document_bindings",
            "missing_document_binding",
            "invalid_mapping_digest",
            "invalid_bound_key",
            "legacy_key_for_bound_document",
        ],
        "zero_replacements_on_fail_closed": True,
        "docx_original_bytes_preserved_on_binding_failure": True,
        "supported_paths": ["text", "txt", "docx", "pdf_to_txt"],
        "new_execution_buttons": False,
        "new_acknowledgement_checkboxes": False,
        "filenames_changed": False,
        "mime_types_changed": False,
        "cloud_processing": False,
        "ai_processing": False,
        "ocr_added": False,
        "restored_pdf_added": False,
        "production_ready": False,
        "human_review_required": True,
        "next_workpackage": "SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY",
    }
    evidence_path = ROOT / "output/validation/mvp_scrub_key_binding_reinsert_validation.json"
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    claim = """# Workpackage claim — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Repository: solidprivacy-nl/scrub

Workpackage title: SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; app verification pending

Claimed by: ChatGPT GitHub worker

Claimed at: 2026-07-28 00:10 Europe/Amsterdam

Branch: scrub-mvp-scrub-key-binding-reinsert-integration

Dependencies:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` — merged as PR #42.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` — merged as PR #43.
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` — merged as PR #44 (`2f5085a700ba6ced3f41859b1e702bb2da7cd88c`).

Implementation result:
- Structurally valid legacy v1.0 and bound v1.1 Scrub Keys are read explicitly.
- Document/key binding is validated before text, TXT, DOCX or PDF-to-TXT replacement.
- `bound_match` is a verified match; valid legacy v1.0 remains explicit unverified compatibility.
- Six frozen mismatch/corruption states fail closed with zero replacements.
- DOCX binding failure returns the exact original package bytes without partial output.
- Stable binding status, warnings, IDs and digest state are visible in the existing report/status surfaces.
- The three-step document-first flow and single final confidential-output acknowledgement remain unchanged.

Validation:
- Adversarial synthetic tests cover correct, wrong, mixed, missing, legacy and tampered key/document combinations.
- TXT, DOCX body/header/footer and PDF-to-TXT paths are covered.
- Normal full GitHub Actions run #1789 passed.
- Temporary operator, diagnostic, validation and contract workflows, triggers, scripts and logs were removed.
- Evidence: `output/validation/mvp_scrub_key_binding_reinsert_validation.json`.

Boundaries:
- No filename, MIME type or supported-format change.
- No automatic legacy upgrade or fabricated document code.
- No signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.
- Human review remains required; production readiness remains false.

Next step:
- Merge after final clean PR validation, verify GitHub-to-Hugging-Face sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.
"""
    (ROOT / "workpackage_claims/scrub_wp_mvp_scrub_key_binding_reinsert_integration.md").write_text(
        claim,
        encoding="utf-8",
    )

    handover = """# Handover — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

## Status

Implemented; full GitHub Actions passed; merge, sync and live app verification pending.

## Files added

- `scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_integration.py`
- `tests/test_scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_ui.py`
- `output/validation/mvp_scrub_key_binding_reinsert_validation.json`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_reinsert_integration.md`
- `handover/workpackages/20260728_0052_mvp_scrub_key_binding_reinsert_integration.md`

## Files changed

- `scrub_key_import.py`
- `scrub_key_reinsert.py`
- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `tests/test_scrub_key_binding_model.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Bound key import and metadata.
- Correct bound match and verified status.
- Wrong-key mismatch, mixed document IDs and missing document binding.
- Legacy key for bound document and bound key for legacy document.
- Mapping-digest tampering.
- Explicit legacy unbound compatibility.
- TXT, DOCX body/header/footer and PDF-to-TXT enforcement.
- Exact original DOCX bytes on fail-closed mismatch.
- Input immutability and pure status-model boundaries.
- Existing import, document reinsert, fidelity and automatic-flow regressions.

## Validation

- Normal full GitHub Actions run #1789: passed.
- GitHub Actions final clean PR run: pending after governance finalisation.
- Hugging Face sync: pending after merge.
- App verification: required for correct bound key, wrong key, tampered key and legacy compatibility.

## Notes / risks

- The accidental wrong-document/key pairing and accidental mapping-corruption path is technically mitigated but remains open until deployed app verification passes.
- Mapping digest is not malicious-tampering authenticity; signing/HMAC remains deferred until protected key management exists.
- Legacy v1.0 compatibility is intentionally unverified and visibly warned.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Merge after final clean PR validation, verify sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.
"""
    handover_path = ROOT / "handover/workpackages/20260728_0052_mvp_scrub_key_binding_reinsert_integration.md"
    handover_path.parent.mkdir(parents=True, exist_ok=True)
    handover_path.write_text(handover, encoding="utf-8")

    prepend(
        ROOT / "WORKPACKAGES.md",
        """## 2026-07-28 00:52 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; app verification pending.

Summary:
- Binding validation now gates every text, TXT, DOCX and PDF-to-TXT reinsert before replacement.
- Correct bound keys are verified; legacy v1.0 remains explicit unverified compatibility.
- Wrong, mixed, missing or corrupted bindings restore zero values.
- The existing three-step flow and final confidentiality acknowledgement remain unchanged.

Next recommended step:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY` after merge and sync.

""",
    )

    prepend(
        ROOT / "CHANGELOG.md",
        """## 2026-07-28 00:52 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; final PR validation pending.

Purpose:
- Prevent a wrong, mixed or accidentally corrupted Scrub Key from restoring values before document/key binding is verified.

Files added:
- `scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_integration.py`
- `tests/test_scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_ui.py`
- `output/validation/mvp_scrub_key_binding_reinsert_validation.json`
- `handover/workpackages/20260728_0052_mvp_scrub_key_binding_reinsert_integration.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_reinsert_integration.md`

Files changed:
- `scrub_key_import.py`
- `scrub_key_reinsert.py`
- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `tests/test_scrub_key_binding_model.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Implementation result:
- Dual-read import supports structurally valid legacy v1.0 and bound v1.1 keys.
- Binding validation runs before any local deterministic replacement.
- `bound_match` is verified; `legacy_unbound` remains compatible but explicitly unverified.
- Six frozen mismatch/corruption states fail closed with zero replacements.
- DOCX mismatch returns exact original bytes; no partial package is produced.
- Binding status, IDs, digest state and warnings are shown in existing feedback/report surfaces.
- No new source/key execution button or acknowledgement checkbox was added.

Validation:
- Normal full GitHub Actions run #1789 passed.
- Synthetic adversarial coverage spans text, TXT, DOCX body/header/footer and PDF-to-TXT.
- Human review remains required; production readiness remains false.

Intentionally not changed:
- Output filenames or MIME types.
- Supported TXT, DOCX and PDF-to-TXT boundaries.
- Legacy key migration.
- Signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Complete final PR validation and merge, verify sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.

---

""",
    )

    prepend(
        ROOT / "RELEASE_NOTES.md",
        """## 2026-07-28 — Verkeerde Scrub Key wordt vóór herstel geblokkeerd

- Nieuwe documentgebonden Scrub Keys worden automatisch vergeleken met de documentcode in het aangeleverde bestand.
- Een verkeerde sleutel, meerdere documentcodes of een ongeldige controlewaarde blokkeren het terugzetten voordat originele waarden worden hersteld.
- Bij een geldige documentgebonden match toont de app dat document en sleutel aantoonbaar bij elkaar horen.
- Oudere Scrub Keys blijven bruikbaar voor compatibiliteit, maar de app waarschuwt zichtbaar dat de documentmatch niet kan worden bewezen.
- De bestaande drie stappen, downloadnamen en TXT/DOCX/PDF-naar-TXT-grenzen blijven gelijk.

---

""",
    )

    prepend(
        ROOT / "DECISION_LOG.md",
        """## 2026-07-28 — D037 — Validate document/key binding before every reinsert replacement

Status: accepted reinsert-integration decision

Decision:

```text
Validate the complete supported text surface against the supplied Scrub Key before any original value is restored. Permit verified bound matches and explicit legacy-v1.0 compatibility only. All mismatch, mixed-binding, missing-binding, invalid-digest and invalid-bound-key states fail closed with zero replacements and no partial DOCX output.
```

Reason:

- Structural key validity alone cannot prove that a key belongs to a document.
- Applying a wrong but valid key can silently restore incorrect confidential values.
- Validation must happen before mutation so document-level helpers cannot produce partial output.
- Legacy compatibility remains necessary, but it must never be presented as a verified document match.
- The document-first three-step UX remains simpler and does not require new execution gates.

---

""",
    )

    replace_once(
        ROOT / "ROADMAP.md",
        "Last roadmap strategy update: 2026-07-27 — bound placeholder and Scrub Key export integration is implemented; fail-closed reinsert enforcement is now active next.",
        "Last roadmap strategy update: 2026-07-28 — bound export and fail-closed reinsert enforcement are implemented; deployed binding app verification is now the active gate.",
        "roadmap strategy status",
    )
    replace_once(
        ROOT / "ROADMAP.md",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — implemented with pure binding-ID, placeholder, digest, bound-key and document/key validation helpers; not yet integrated into export or reinsert.\n",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — completed with pure binding-ID, placeholder, digest, bound-key and document/key validation helpers.\n"
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — completed with bound placeholders and schema-1.1 key export.\n"
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — implemented with dual-read import, fail-closed binding enforcement and explicit legacy compatibility; app verification pending.\n",
        "roadmap implementation status",
    )
    replace_once(
        ROOT / "ROADMAP.md",
        "9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — implemented\n10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — active\n11. SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY",
        "9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — completed\n10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — implemented\n11. SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY — active",
        "roadmap execution queue",
    )

    replace_once(
        ROOT / "MVP_PHASE6_EXECUTION_PLAN.md",
        "Contract status: frozen. Binding IDs use `B[A-Z2-7]{16}`; bound keys use an explicit new schema direction with canonical SHA-256 mapping digest, eight statuses and fail-closed mismatch rules. Pure model implementation is complete and isolated; export integration is active next, followed by reinsert enforcement.",
        "Implementation status: the frozen contract, pure model, bound export and fail-closed reinsert enforcement are implemented. The active next gate is deployed app verification across correct, wrong, tampered and legacy key scenarios.",
        "phase 6 binding status",
    )

    replace_once(
        ROOT / "RISK_REGISTER.md",
        "Risk remains open until binding validation gates replacement during reinsert. Signatures/HMAC remain deferred until protected local signing-key management exists.",
        "Reinsert now validates the complete supported document text surface before replacement. Correct bound matches are verified; wrong, mixed, missing or digest-invalid bindings fail closed with zero replacements, and DOCX failures return the exact original package bytes. Legacy v1.0 compatibility remains explicitly unverified. The accidental pairing/corruption path is technically mitigated but the risk remains open until deployed app verification passes. Signatures/HMAC remain deferred until protected local signing-key management exists.",
        "Scrub Key risk mitigation status",
    )


if __name__ == "__main__":
    main()
