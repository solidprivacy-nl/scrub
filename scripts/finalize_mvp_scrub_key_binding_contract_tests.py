from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS"
MARKER = f"## 2026-07-27 19:38 Europe/Amsterdam — {TITLE}"
HANDOVER = ROOT / "handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, block.rstrip() + "\n\n" + text)


workpackages_block = f"""{MARKER}

Status: completed; contract frozen; PR validation pending.

Summary:
- Added a versioned binding contract and synthetic fixture before any product implementation.
- Locked binding ID grammar `B[A-Z2-7]{{16}}` with an 80-bit random payload.
- Locked automatic placeholders as `[LABEL_BINDINGID_INDEX]` and manual placeholders as `[LABEL_BINDINGID_HANDMATIG_INDEX]`.
- Locked bound Scrub Key metadata direction as schema version `1.1`, binding version `1`, a document binding ID and canonical SHA-256 mapping digest.
- Locked eight binding statuses and six fail-closed statuses that must produce zero replacements.
- Locked explicit legacy-v1.0 unbound compatibility without silent upgrading.
- Preserved the existing three-step source → key → download UX and final confidential-download acknowledgement.
- Defined the pure helper responsibilities for model implementation.
- Changed no product helper, UI, placeholder generation, Scrub Key schema implementation, export or reinsert behavior.

Validation boundaries:
- Fixed synthetic digest: `516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3`.
- Mapping digest is accidental-corruption evidence, not authenticity or a signature.
- Malformed placeholders are never guessed or repaired.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.
"""
prepend_once("WORKPACKAGES.md", MARKER, workpackages_block)

changelog_block = f"""{MARKER}

Status: completed; contract frozen; PR validation pending.

Purpose:
- Freeze the bound-placeholder, Scrub Key metadata, mapping-digest, legacy compatibility and fail-closed validation contracts before implementing the model.

Files added:
- `SCRUB_KEY_BINDING_CONTRACT.md`
- `test_cases/mvp_phase6/scrub_key_binding_contract.json`
- `tests/test_mvp_scrub_key_binding_contracts.py`
- `tests/test_mvp_scrub_key_binding_contract_validation.py`
- `output/validation/mvp_scrub_key_binding_contract_validation.json`
- `handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_contract_tests.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Contract result:
- Binding ID grammar: `B[A-Z2-7]{{16}}`.
- Automatic placeholder grammar: `[LABEL_BINDINGID_INDEX]`.
- Manual placeholder grammar: `[LABEL_BINDINGID_HANDMATIG_INDEX]`.
- Proposed bound key schema: `1.1`; binding version: `1`.
- Canonical digest algorithm: SHA-256.
- Eight binding statuses; six are fail-closed with zero replacements.
- Legacy v1.0 remains explicit unbound compatibility and cannot be used for bound documents.
- Current three-step reinsert UX remains unchanged; no new source/key buttons or checkboxes.
- Product code changed: false.
- Production ready: false; human review required: true.

Intentionally not changed:
- existing product helpers;
- automatic/manual placeholder generation;
- Scrub Key build, validation, serialization or import implementation;
- export or reinsert semantics;
- UI or download behavior;
- signing/HMAC or secret storage;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` after PR validation and merge.

---
"""
prepend_once("CHANGELOG.md", MARKER, changelog_block)

roadmap = read("ROADMAP.md")
roadmap = roadmap.replace(
    "Last roadmap strategy update: 2026-07-27 — document/key-binding triage is complete; test-first bound-placeholder and Scrub Key contract work is now active before implementation.",
    "Last roadmap strategy update: 2026-07-27 — the bound-placeholder and Scrub Key contract is frozen; pure binding-model implementation is now active before export or reinsert integration.",
)
roadmap = roadmap.replace(
    "7. SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — active\n8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION",
    "7. SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed\n8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — active",
)
status_anchor = "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed with a bound-placeholder plus mapping-digest recommendation and a test-first implementation sequence."
if "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed with" not in roadmap:
    roadmap = roadmap.replace(
        status_anchor,
        status_anchor
        + "\nSCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed with frozen placeholder, digest, legacy and fail-closed model contracts.",
    )
write("ROADMAP.md", roadmap)

plan = read("MVP_PHASE6_EXECUTION_PLAN.md")
anchor = (
    "Triage result: use a non-sensitive document binding ID in every placeholder and the corresponding key, complemented by a canonical mapping digest. Implement sequentially through contract tests, pure model helpers, export integration, reinsert integration and live verification. Legacy unbound keys remain explicit; malicious tampering remains outside the MVP without protected signing-key management."
)
replacement = anchor + "\n\nContract status: frozen. Binding IDs use `B[A-Z2-7]{16}`; bound keys use an explicit new schema direction with canonical SHA-256 mapping digest, eight statuses and fail-closed mismatch rules. Pure model implementation is the active next package."
plan = plan.replace(anchor, replacement)
write("MVP_PHASE6_EXECUTION_PLAN.md", plan)

risk = read("RISK_REGISTER.md")
r2_anchor = "Contract tests must define legacy v1.0 behavior and fail-closed mismatch rules before implementation."
r2_replacement = "Contract tests now freeze legacy v1.0 unbound behavior, a document-specific base32 binding ID, canonical SHA-256 mapping digest and fail-closed mismatch/mixed-ID/digest-error statuses before model implementation."
risk = risk.replace(r2_anchor, r2_replacement)
write("RISK_REGISTER.md", risk)

decision = read("DECISION_LOG.md")
decision_marker = "## 2026-07-27 — D034 — Freeze the bound-placeholder and mapping-digest contract before model implementation"
if decision_marker not in decision:
    insertion = f"""{decision_marker}

Status: accepted test/specification decision; model implementation may proceed

Decision:

```text
Freeze binding IDs as B plus sixteen uppercase RFC 4648 base32 characters, automatic placeholders as [LABEL_BINDINGID_INDEX], manual placeholders as [LABEL_BINDINGID_HANDMATIG_INDEX], and the bound-key direction as schema version 1.1 with binding version 1 and a canonical SHA-256 mapping digest. Preserve explicit legacy-v1.0 unbound compatibility and require all bound mismatch, mixed-ID, missing-binding, invalid-digest and invalid-bound-key states to fail closed before replacement.
```

Reason:

- Exact grammar and canonicalization are required before multiple shared placeholder, export and reinsert surfaces change.
- A fixed synthetic digest fixture makes implementation independently testable.
- Bound and legacy statuses must not be conflated.
- UI simplification must survive the security change without new source/key execution gates.

Boundaries:

- Contract/tests only in this package; no product behavior change.
- Mapping digest is not authenticity or a signature.
- No automatic placeholder repair or legacy upgrade.
- Preserve the three-step document-first reinsert flow and final confidential-download acknowledgement.
- Model implementation remains pure and Streamlit-free.
- Export and reinsert integration require later sequential packages.
- Human review remains mandatory; no production-readiness claim.

Evidence:

- `SCRUB_KEY_BINDING_CONTRACT.md`
- `test_cases/mvp_phase6/scrub_key_binding_contract.json`
- `tests/test_mvp_scrub_key_binding_contracts.py`
- `output/validation/mvp_scrub_key_binding_contract_validation.json`

---

"""
    decision = decision.replace("---\n\n## 2026-07-27 — D033", "---\n\n" + insertion + "## 2026-07-27 — D033", 1)
write("DECISION_LOG.md", decision)

claim_path = "workpackage_claims/scrub_wp_mvp_scrub_key_binding_contract_tests.md"
claim = read(claim_path)
claim = claim.replace("Status: in_progress", "Status: completed; contract frozen; PR validation pending")
claim = claim.replace(
    "- Record green contract evidence, remove temporary tooling and hand over to `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.",
    "- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.",
)
if "Contract result:" not in claim:
    claim += """

Contract result:
- Binding ID: `B[A-Z2-7]{16}` with an 80-bit random payload.
- Bound automatic/manual placeholder grammar frozen.
- Bound-key schema direction `1.1`, binding version `1` and canonical SHA-256 mapping digest frozen.
- Eight binding statuses and six fail-closed states frozen.
- Legacy v1.0 remains explicit unbound compatibility.
- Three-step reinsert UX and final download acknowledgement preserved.
- Canonical synthetic digest independently recomputed.
- Implementation authorized in this package: false.
- Product code changed: false.
- Production ready: false; human review required: true.
- Evidence: `output/validation/mvp_scrub_key_binding_contract_validation.json`.
- Handover: `handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md`.
"""
write(claim_path, claim)

HANDOVER.parent.mkdir(parents=True, exist_ok=True)
HANDOVER.write_text(
    f"""# Handover — {TITLE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{TITLE}

## Status

Completed; contract frozen; PR validation pending.

## Summary

The document/Scrub-Key binding contract is frozen before model implementation. It defines the binding-ID and bound-placeholder grammar, bound-key metadata direction, canonical mapping digest, explicit legacy compatibility, stable validation result fields and fail-closed statuses. No product behavior changed.

## Files added

- `SCRUB_KEY_BINDING_CONTRACT.md`
- `test_cases/mvp_phase6/scrub_key_binding_contract.json`
- `tests/test_mvp_scrub_key_binding_contracts.py`
- `tests/test_mvp_scrub_key_binding_contract_validation.py`
- `output/validation/mvp_scrub_key_binding_contract_validation.json`
- `handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_contract_tests.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Binding-ID valid/invalid grammar.
- Automatic/manual placeholder parsing, including labels with underscores.
- Compatibility with the existing broad placeholder detector.
- Bound-key metadata and item-binding consistency.
- Exact, deterministic and order-independent canonical digest fixture.
- Digest sensitivity to restoration-semantic changes.
- Complete eight-status matrix and six fail-closed statuses.
- Explicit difference between verified bound match and legacy unbound compatibility.
- Frozen pure-helper responsibilities and result fields.
- Current three-step UI/no-extra-gate contract.
- Synthetic-only and security-claim boundaries.

## Validation

- Canonical SHA-256 fixture independently recomputed: passed.
- Targeted contract/source tests: pending GitHub Actions.
- Full repository suite: pending PR validation.
- Hugging Face sync: not functionally applicable; no runtime/app code changed.
- App verification: not applicable; no visible behavior changed.

## Notes / risks

- The contract mitigates accidental mismatch/corruption after implementation, not malicious editing with recomputed unkeyed digest.
- Legacy v1.0 keys remain unbound.
- Export and reinsert behavior remain unchanged until later packages.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` after merge.
""",
    encoding="utf-8",
)
