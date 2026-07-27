from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION"
MARKER = f"## 2026-07-27 20:05 Europe/Amsterdam — {TITLE}"
HANDOVER = ROOT / "handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, block.rstrip() + "\n\n" + text)


workpackages_block = f"""{MARKER}

Status: implemented; targeted validation passed; PR verification pending.

Summary:
- Added `scrub_key_binding.py` as a pure, Streamlit-free binding model.
- Implemented local binding-ID generation using ten random bytes and uppercase base32.
- Implemented strict binding-ID validation and automatic/manual bound placeholder build/parse helpers.
- Implemented strict document binding-ID extraction from bound placeholders.
- Implemented canonical mapping-digest payload and SHA-256 digest helpers matching the frozen fixture.
- Implemented bound Scrub Key structural, policy, item-binding, duplicate and digest validation.
- Implemented all eight frozen document/key statuses, including explicit legacy-v1.0 unbound compatibility.
- Enforced six fail-closed statuses before any later replacement integration.
- Preserved immutable inputs and stable result fields.
- Integrated nothing into current placeholder generation, export, reinsert or UI paths.

Validation boundaries:
- Contract fixture digest matched exactly.
- Targeted model, contract, legacy import/export and roundtrip tests passed.
- No Streamlit, network, AI, cloud or file-write behavior exists in the model.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`.
"""
prepend_once("WORKPACKAGES.md", MARKER, workpackages_block)

changelog_block = f"""{MARKER}

Status: implemented; targeted validation passed; PR verification pending.

Purpose:
- Implement the frozen document/Scrub-Key binding contract as pure helpers before changing shared placeholder generation, export or reinsert behavior.

Files added:
- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `tests/test_scrub_key_binding_model_validation.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`
- `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_model_implementation.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Implementation result:
- Local document binding ID generation supports injected deterministic bytes and normal `secrets` randomness.
- Bound automatic/manual placeholder creation and parsing match the frozen grammar.
- Canonical digest output matches the fixed synthetic SHA-256 fixture.
- Bound key validation checks schema, policies, items, item bindings, duplicates and digest.
- Document/key validation implements `bound_match`, `legacy_unbound`, `binding_mismatch`, `mixed_document_bindings`, `missing_document_binding`, `invalid_mapping_digest`, `invalid_bound_key` and `legacy_key_for_bound_document`.
- Bound failures prohibit replacement; legacy compatibility remains explicitly unverified.
- Inputs remain unmodified.

Intentionally not changed:
- current generic automatic/manual placeholder generation;
- current Scrub Key builder, serializer, export or import integration;
- current reinsert execution helpers or UI;
- filenames or MIME types;
- legacy migration;
- signing/HMAC or secret storage;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after PR validation and merge.

---
"""
prepend_once("CHANGELOG.md", MARKER, changelog_block)

roadmap = read("ROADMAP.md")
roadmap = roadmap.replace(
    "Last roadmap strategy update: 2026-07-27 — the bound-placeholder and Scrub Key contract is frozen; pure binding-model implementation is now active before export or reinsert integration.",
    "Last roadmap strategy update: 2026-07-27 — the pure binding model is implemented and isolated; bound placeholder and Scrub Key export integration is now active before reinsert enforcement.",
)
roadmap = roadmap.replace(
    "8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — active\n9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION",
    "8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — completed\n9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — active",
)
status_anchor = "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed with frozen placeholder, digest, legacy and fail-closed model contracts."
if "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — implemented with" not in roadmap:
    roadmap = roadmap.replace(
        status_anchor,
        status_anchor
        + "\nSCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — implemented with pure binding-ID, placeholder, digest, bound-key and document/key validation helpers; not yet integrated into export or reinsert.",
    )
write("ROADMAP.md", roadmap)

plan = read("MVP_PHASE6_EXECUTION_PLAN.md")
anchor = "Contract status: frozen. Binding IDs use `B[A-Z2-7]{16}`; bound keys use an explicit new schema direction with canonical SHA-256 mapping digest, eight statuses and fail-closed mismatch rules. Pure model implementation is the active next package."
replacement = "Contract status: frozen. Binding IDs use `B[A-Z2-7]{16}`; bound keys use an explicit new schema direction with canonical SHA-256 mapping digest, eight statuses and fail-closed mismatch rules. Pure model implementation is complete and isolated; export integration is active next, followed by reinsert enforcement."
plan = plan.replace(anchor, replacement)
write("MVP_PHASE6_EXECUTION_PLAN.md", plan)

risk = read("RISK_REGISTER.md")
r2_anchor = "Contract tests now freeze legacy v1.0 unbound behavior, a document-specific base32 binding ID, canonical SHA-256 mapping digest and fail-closed mismatch/mixed-ID/digest-error statuses before model implementation."
r2_replacement = r2_anchor + " The pure model now implements those contracts without changing current export or reinsert behavior. Risk remains open until bound placeholders and keys are created during export and binding validation gates replacement during reinsert."
risk = risk.replace(r2_anchor, r2_replacement)
write("RISK_REGISTER.md", risk)

decision = read("DECISION_LOG.md")
decision_marker = "## 2026-07-27 — D035 — Keep binding-model implementation pure until sequential export and reinsert integration"
if decision_marker not in decision:
    insertion = f"""{decision_marker}

Status: accepted implementation decision

Decision:

```text
Implement document/Scrub-Key binding as a new pure helper module first. Do not alter current placeholder creation, Scrub Key export/import, deterministic replacement or Streamlit behavior in the model package. Export integration creates bound artifacts in the next package; reinsert integration enforces binding only after bound export is proven.
```

Reason:

- Placeholder generation, key export and reinsert are shared safety-critical surfaces.
- Pure helpers can be validated completely against the frozen contract without silently changing current output semantics.
- Sequential integration preserves explicit migration and rollback boundaries.

Implemented model boundaries:

- local random/injected binding-ID generation;
- strict bound placeholder build/parse and document-ID extraction;
- canonical SHA-256 mapping digest;
- bound key validation;
- eight stable document/key statuses and six fail-closed statuses;
- explicit legacy-v1.0 unbound compatibility;
- no UI, export or reinsert integration;
- no cloud, AI, file persistence, signing or secret storage.

Evidence:

- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`

---

"""
    decision = decision.replace("---\n\n## 2026-07-27 — D034", "---\n\n" + insertion + "## 2026-07-27 — D034", 1)
write("DECISION_LOG.md", decision)

claim_path = "workpackage_claims/scrub_wp_mvp_scrub_key_binding_model_implementation.md"
claim = read(claim_path)
claim = claim.replace("Status: in_progress", "Status: implemented; targeted validation passed; PR verification pending")
claim = claim.replace(
    "- Add the pure binding model and implementation tests against the frozen contract, then hand over to `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after green validation.",
    "- Merge after GitHub Actions pass, then start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`.",
)
if "Implementation result:" not in claim:
    claim += """

Implementation result:
- Pure module: `scrub_key_binding.py`.
- Frozen binding ID, placeholder, digest and status contracts implemented.
- Eight statuses and six fail-closed paths implemented.
- Explicit legacy-v1.0 unbound compatibility implemented.
- Targeted model/contract/legacy/roundtrip validation passed.
- Current export integrated: false.
- Current reinsert integrated: false.
- Product UI changed: false.
- Production ready: false; human review required: true.
- Evidence: `output/validation/mvp_scrub_key_binding_model_validation.json`.
- Handover: `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`.
"""
write(claim_path, claim)

HANDOVER.parent.mkdir(parents=True, exist_ok=True)
HANDOVER.write_text(
    f"""# Handover — {TITLE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{TITLE}

## Status

Implemented; targeted validation passed; PR verification pending.

## Summary

The frozen binding contract is implemented as a pure helper module. Binding IDs, bound placeholders, canonical mapping digests, bound-key validation and all eight document/key statuses are available without integrating current export, reinsert or UI paths.

## Files added

- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `tests/test_scrub_key_binding_model_validation.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`
- `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_model_implementation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## Tests

- Deterministic injected and normal local binding-ID generation.
- Binding-ID validation.
- Automatic/manual bound placeholder build/parse and strict rejection.
- Document binding-ID extraction.
- Exact canonical payload/digest, metadata exclusions and semantic sensitivity.
- Bound-key schema/policy/item/duplicate/digest validation.
- All eight frozen document/key status cases.
- Six fail-closed paths and explicit legacy-unbound compatibility.
- Input immutability.
- No Streamlit, network, AI, file-writing or integration side effects.
- Existing contract, secure import/export and roundtrip tests included in targeted validation.

## Validation

- Targeted model/contract/legacy/roundtrip tests: passed.
- Contract fixture digest: matched exactly.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally applicable; no runtime/app code changed.
- App verification: not applicable; no visible behavior changed.

## Notes / risks

- Current exports remain legacy/unbound until the next package.
- Current reinsert does not yet enforce binding.
- Mapping digest is not cryptographic authenticity.
- Legacy keys remain explicitly unbound.
- Human review remains mandatory; production readiness remains false.

## Next recommended step

- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after merge.
""",
    encoding="utf-8",
)
