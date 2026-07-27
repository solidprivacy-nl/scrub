from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE"
MARKER = f"## 2026-07-27 19:18 Europe/Amsterdam — {TITLE}"
HANDOVER = ROOT / "handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, block.rstrip() + "\n\n" + text)


workpackages_block = f"""{MARKER}

Status: completed; targeted validation passed; PR verification pending.

Summary:
- Classified the critical same-placeholder wrong-key finding by accidental pairing, accidental corruption and malicious tampering.
- Rejected document labels, complete-content hashes, placeholder-list hashes, filenames, hidden metadata and extra sidecars as sufficient primary binding controls.
- Recommended a non-sensitive document binding ID carried in every automatic/manual placeholder and the corresponding Scrub Key.
- Recommended a canonical SHA-256 mapping digest as a complementary accidental-corruption control, not as an authenticity signature.
- Deferred signature/HMAC protection until a trusted local signing-key lifecycle exists.
- Preserved the three-step document-first reinsert flow without new confirmation buttons or checkboxes.
- Changed no product code, UI, schema, placeholders, export or reinsert semantics.

Approved sequential implementation line:
1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`
2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`
3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`
4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`
5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Optional later package:
- `SCRUB-WP_MVP_MALFORMED_PLACEHOLDER_DIAGNOSTIC_HARDENING`.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.
"""
prepend_once("WORKPACKAGES.md", MARKER, workpackages_block)

changelog_block = f"""{MARKER}

Status: completed; targeted validation passed; PR verification pending.

Purpose:
- Determine the smallest safe cross-format mitigation for the critical document/Scrub-Key binding gap before changing schema, placeholders, export or reinsert behavior.

Files added:
- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`
- `tests/test_mvp_scrub_key_document_binding_gap_triage.py`
- `tests/test_mvp_scrub_key_document_binding_gap_triage_validation.py`
- `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Triage result:
- Primary MVP threat: accidental wrong-document/key pairing.
- Secondary MVP threat: accidental key corruption.
- Deferred threat: malicious tampering requiring protected signing-key infrastructure.
- Recommended primary control: document-specific non-sensitive binding ID in all placeholders and the key.
- Recommended complementary control: canonical SHA-256 mapping digest.
- Explicitly not sufficient: document labels, filenames, content hashes, placeholder-list hashes or metadata-only binding.
- Legacy v1.0 keys require explicit unbound status and warning; they must not be silently treated as bound.
- Bound-key mismatch, mixed IDs and digest mismatch must fail closed with zero replacements.
- Human review remains required; production readiness remains false.

Intentionally not changed:
- product code or UI;
- Scrub Key schema/version or serialization;
- placeholder generation or grammar;
- export/download or reinsert semantics;
- document processing;
- cloud, AI, OCR or secret storage.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` before implementation.

---
"""
prepend_once("CHANGELOG.md", MARKER, changelog_block)

roadmap = read("ROADMAP.md")
roadmap = roadmap.replace(
    "Last roadmap strategy update: 2026-07-27 — Scrub Key roundtrip validation is complete and exposed a critical document/key-binding gap; evidence triage is now active before any schema or export change.",
    "Last roadmap strategy update: 2026-07-27 — document/key-binding triage is complete; test-first bound-placeholder and Scrub Key contract work is now active before implementation.",
)
roadmap = roadmap.replace(
    "6. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — active\n7. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n8. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
    "6. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed\n7. SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — active\n8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION\n9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION\n10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION\n11. SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY\n12. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE\n13. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT",
)
status_anchor = "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed with 15/15 cases passing and a critical document/key-binding gap routed to triage."
if "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed with" not in roadmap:
    roadmap = roadmap.replace(
        status_anchor,
        status_anchor
        + "\nSCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed with a bound-placeholder plus mapping-digest recommendation and a test-first implementation sequence.",
    )
write("ROADMAP.md", roadmap)

plan = read("MVP_PHASE6_EXECUTION_PLAN.md")
triage_text = (
    "### 4A. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE\n\n"
    "Classify the critical finding that a structurally valid wrong key can reuse the same placeholder namespace and restore incorrect values without a detectable mismatch. Decide whether document/key binding requires a key identifier, content fingerprint, manifest binding or another explicit contract. Do not change schema, export or reinsert semantics in the triage package."
)
replacement = triage_text + "\n\nTriage result: use a non-sensitive document binding ID in every placeholder and the corresponding key, complemented by a canonical mapping digest. Implement sequentially through contract tests, pure model helpers, export integration, reinsert integration and live verification. Legacy unbound keys remain explicit; malicious tampering remains outside the MVP without protected signing-key management."
plan = plan.replace(triage_text, replacement)
write("MVP_PHASE6_EXECUTION_PLAN.md", plan)

risk = read("RISK_REGISTER.md")
r2_anchor = "This is routed to `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`; no schema or export change is authorized by the validation package."
r2_replacement = r2_anchor + " Triage recommends a non-sensitive document binding ID inside every automatic/manual placeholder and the corresponding key, plus a canonical mapping digest for accidental corruption. Contract tests must define legacy v1.0 behavior and fail-closed mismatch rules before implementation. Signatures/HMAC remain deferred until protected local signing-key management exists."
risk = risk.replace(r2_anchor, r2_replacement)
r3_anchor = "This diagnostic limitation is included in the document-binding gap triage."
r3_replacement = r3_anchor + " It is not part of the critical binding implementation line; an optional later diagnostic-hardening package may report malformed near-placeholders directly without guessing or repairing values."
risk = risk.replace(r3_anchor, r3_replacement)
write("RISK_REGISTER.md", risk)

decision = read("DECISION_LOG.md")
decision_marker = "## 2026-07-27 — D033 — Bind new Scrub Keys through document-specific placeholder namespaces"
if decision_marker not in decision:
    insertion = f"""{decision_marker}

Status: accepted planning/architecture decision; implementation requires green contract tests

Decision:

```text
For new bound Scrub Keys, carry one locally generated, non-sensitive document binding ID in every automatic and manual placeholder and in the corresponding Scrub Key. Complement this with a canonical SHA-256 mapping digest for accidental key-corruption detection. Reinsert must fail closed before any replacement when a bound key mismatches the document, the document contains mixed binding IDs, or the mapping digest is invalid.
```

Reason:

- Generic placeholder namespaces allow a wrong valid key to restore wrong originals without an audit mismatch.
- A binding token inside placeholders survives pasted-text, TXT, DOCX and PDF-text roundtrips when the placeholders themselves survive.
- Labels, filenames, metadata, content hashes and placeholder-list hashes are not reliable cross-format AI-roundtrip bindings.
- A digest detects accidental edits but is not authenticity; malicious tampering requires later protected signing-key infrastructure.

Compatibility and UX boundaries:

- Introduce an explicit new bound-key contract; do not silently reinterpret legacy v1.0 keys.
- Legacy unbound keys may remain dual-readable with a visible unbound warning.
- Preserve the document-first three-step reinsert flow and the final confidential-download acknowledgement.
- Add no repeated confirmation buttons or checkboxes.
- Preserve unknown, duplicate and missing-placeholder audit reporting.
- No cloud processing, server secret, OCR or restored-PDF behavior.
- Human review remains mandatory; no production-readiness claim.

Approved sequence:

1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`
2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`
3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`
4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`
5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Evidence:

- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`

---

"""
    decision = decision.replace("---\n\n## 2026-07-27 — D032", "---\n\n" + insertion + "## 2026-07-27 — D032", 1)
write("DECISION_LOG.md", decision)

claim_path = "workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md"
claim = read(claim_path)
claim = claim.replace("Status: in_progress", "Status: completed; targeted validation passed; PR verification pending")
claim = claim.replace(
    "- Inspect current placeholder/key architecture, evaluate binding options and record a decision-backed implementation sequence.",
    "- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.",
)
if "Triage result:" not in claim:
    claim += """

Triage result:
- Recommended primary control: non-sensitive document binding ID in every automatic/manual placeholder and the corresponding key.
- Recommended complementary control: canonical SHA-256 mapping digest for accidental key corruption.
- Legacy v1.0 keys remain explicit unbound compatibility, not silently bound.
- Bound mismatch, mixed IDs and invalid digest must fail closed with zero replacements.
- Signatures/HMAC deferred until protected local signing-key lifecycle exists.
- Targeted triage/source-evidence tests passed.
- Implementation authorized in this package: false.
- Production ready: false; human review required: true.
- Triage: `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`.
- Evidence: `output/validation/mvp_scrub_key_document_binding_gap_triage.json`.
- Validation evidence: `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`.
- Handover: `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`.
"""
write(claim_path, claim)

HANDOVER.parent.mkdir(parents=True, exist_ok=True)
HANDOVER.write_text(
    f"""# Handover — {TITLE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{TITLE}

## Status

Completed; targeted validation passed; PR verification pending.

## Summary

The critical same-placeholder wrong-key finding was classified and routed to a test-first implementation line. The recommended MVP contract adds one non-sensitive document binding ID to every automatic/manual placeholder and the corresponding Scrub Key, plus a canonical mapping digest for accidental corruption. No product behavior was changed.

## Files added

- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`
- `tests/test_mvp_scrub_key_document_binding_gap_triage.py`
- `tests/test_mvp_scrub_key_document_binding_gap_triage_validation.py`
- `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Source critical finding must be consumed by triage.
- Accidental mismatch, accidental corruption and malicious tampering must remain distinct.
- Weak binding options must remain rejected.
- Recommended binding must be cross-format and preserve the three-step UX.
- Mapping digest must not be represented as authenticity.
- Bound mismatch/mixed IDs/invalid digest must be fail-closed requirements.
- Approved sequence must remain test-first.
- Validation evidence and temporary-workflow cleanup are contract-tested.

## Validation

- Targeted triage and source-evidence tests: passed.
- Critical findings triaged: 1.
- Medium findings triaged: 1.
- Implementation authorized: false.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally applicable; no runtime/app code changed.
- App verification: not applicable; no visible behavior changed.

## Notes / risks

- Binding IDs mitigate accidental wrong-key pairing but are not secret and do not stop a fully malicious editor who changes both document and key.
- An unkeyed mapping digest detects accidental edits but is not a signature.
- Strong malicious-tampering protection requires protected local signing-key management.
- Legacy keys remain unbound and require explicit status/warning.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.
""",
    encoding="utf-8",
)
