from __future__ import annotations

from pathlib import Path


ROADMAP = Path("ROADMAP.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
CHANGELOG = Path("CHANGELOG.md")
DECISION_LOG = Path("DECISION_LOG.md")
RISK_REGISTER = Path("RISK_REGISTER.md")
CLAIM = Path("workpackage_claims/scrub_wp_mvp_phase6_roadmap_realignment.md")
PLAN = Path("MVP_PHASE6_EXECUTION_PLAN.md")
HANDOVER = Path("handover/workpackages/20260717_2012_mvp_phase6_roadmap_realignment.md")

STAMP = "2026-07-17 20:12 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def prepend_once(path: Path, marker: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(entry + text, encoding="utf-8")


def update_roadmap() -> None:
    text = ROADMAP.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Last roadmap strategy update: 2026-06-18 — active next direction refocused on MVP UI cleanup and export/download flow.",
        "Last roadmap strategy update: 2026-07-17 — verified MVP UI simplification line closed; Phase 6 workflow validation and trust hardening is now active.",
        "roadmap strategy date",
    )
    text = replace_once(
        text,
        "WP_RECALL_PERSON_NAME_* — diagnostic, contract and helper-level PERSON-name work completed; benchmark follow-up temporarily parked unless a concrete blocker appears.\n```",
        "WP_RECALL_PERSON_NAME_* — diagnostic, contract and helper-level PERSON-name work completed; benchmark follow-up temporarily parked unless a concrete blocker appears.\nSCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_* through SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_* — the current MVP UI simplification line is completed, synchronized and live-app verified.\n```",
        "roadmap completed status",
    )
    text = replace_once(
        text,
        """Important UX status:

```text
The review table remains source of truth and fallback.
The old replacement decision helper panel must not return as normal user-facing UI.
The long-term review target is one unified side-by-side main review surface, not more separate helper panels.
The export/download flow is functional but not yet product-finished.
```""",
        """Important UX status:

```text
The review table remains source of truth and fallback.
The old replacement decision helper panel must not return as normal user-facing UI.
The unified side-by-side review, manual missed-value entry and compact export flow form the verified MVP UI baseline.
Further UI work is not the default next line and requires a separately approved package tied to evidence from Phase 6 validation.
```""",
        "roadmap UX status",
    )
    old_active = """## 7. Active next work direction

Current active priorities:

```text
1. Clean up the MVP interface and export/download flow.
2. Move debug/audit details out of the primary user path without removing safety controls.
3. Then continue benchmark/recalibration work where it directly supports user-visible trust.
```

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

Do not implement UI directly from this roadmap step. Use the workpackage queue in `WORKPACKAGES.md`: first export/download UX contract tests, then implementation, then review debug/copy cleanup.

Do not start local packaging next steps such as `WP48B` or `WP49B` by default. They require explicit coordinator approval.

Do not start pilot follow-up such as `WP52` by default. It requires the MVP quality gate to pass first."""
    new_active = """## 7. Active next work direction

The verified MVP UI baseline is now stable enough to move the active line into Phase 6 validation and trust hardening.

Current execution queue:

```text
1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX
2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE
3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING
4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION
5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE
6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT
```

Execution principles:

- use synthetic data only;
- validate the full supported workflow before adding new features;
- create recognizer or document-processing fixes only from reproducible evidence;
- preserve legal meaning and keep human review mandatory;
- do not reopen broad UI work unless validation reveals a concrete usability or safety blocker;
- do not make production-readiness claims from prototype evidence.

Recall/benchmark work is reopened only where the synthetic validation matrix exposes a concrete false-negative, misclassification or over-masking gap.

Do not start local packaging next steps such as `WP48B` or `WP49B` by default. They require explicit coordinator approval.

Do not start pilot follow-up such as `WP52` by default. It remains gated by `SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT` and explicit coordinator approval."""
    text = replace_once(text, old_active, new_active, "roadmap active direction")
    ROADMAP.write_text(text, encoding="utf-8")


def update_workpackages() -> None:
    entry = f'''## {STAMP} — {PACKAGE}

Status: completed / ready for PR verification.

Summary:
- Closed the verified MVP UI simplification line as the default development focus.
- Made Phase 6 end-to-end workflow validation and trust hardening the active execution line.
- Added `MVP_PHASE6_EXECUTION_PLAN.md` with the ordered validation, triage, hardening, evidence and quality-gate packages.
- Preserved the Phase 7 pilot, local packaging and production-readiness gates.
- No product code, tests, UI, recognizers, replacement semantics, export, Scrub Key, reinsert, document processing, runtime or dependencies changed.

Validation:
- Documentation consistency checks required through PR review and GitHub Actions.
- Hugging Face sync not functionally relevant because no app code changed.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX`.

'''
    prepend_once(WORKPACKAGES, f"{STAMP} — {PACKAGE}", entry)
    text = WORKPACKAGES.read_text(encoding="utf-8")
    old_queue = """## Active / next recommended execution queue

```text
1. Complete PR validation for SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION.
2. If validation passes, merge and verify GitHub to Hugging Face sync.
3. Ask coordinator for live app verification because visible UI copy changed.
4. If app verification passes, close out. If it fails, create a narrow FIX package.
```"""
    new_queue = """## Active / next recommended execution queue

```text
1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX
2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — only for reproducible gaps found by the matrix
3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING
4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION
5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE
6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT
```

The UI simplification baseline is completed and app-verified. Do not start another UI package by default; use evidence from Phase 6 validation to justify any future UI change."""
    text = replace_once(text, old_queue, new_queue, "workpackage active queue")
    WORKPACKAGES.write_text(text, encoding="utf-8")


def update_changelog() -> None:
    entry = f'''## 2026-07-17 — {PACKAGE}

Status: completed / ready for PR verification.

Purpose:

- Realign the central roadmap after completion and live verification of the MVP UI simplification line.
- Make Phase 6 end-to-end workflow validation and trust hardening the active development line.
- Define an ordered evidence-driven workpackage queue before pilot or packaging work resumes.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_phase6_roadmap_realignment.md`

Files added:

- `MVP_PHASE6_EXECUTION_PLAN.md`
- `handover/workpackages/20260717_2012_mvp_phase6_roadmap_realignment.md`

Main changes:

- The verified UI baseline is no longer the active development focus.
- Phase 6 starts with a synthetic end-to-end validation matrix.
- False-negative, document-hygiene, Scrub Key/roundtrip and audit work must be driven by reproducible evidence.
- Phase 7 pilots and local packaging remain gated.

Validation status:

- Documentation-only package.
- GitHub Actions pending after PR.
- Hugging Face functional sync not applicable.
- App verification not applicable.

Intentionally not changed:

- product code or tests;
- UI behavior;
- recognizers or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX` after this realignment is merged.

---

'''
    prepend_once(CHANGELOG, PACKAGE, entry)


def update_decision_log() -> None:
    entry = '''## 2026-07-17 — D028 — Phase 6 workflow validation becomes the active development line

Status: accepted product-direction decision

Decision:

```text
Close the verified MVP UI simplification line as the default development focus and activate Phase 6 end-to-end workflow validation and trust hardening.
```

Reason:

```text
The current import, review, manual correction and export interface has been live-app verified and works as expected. The next material risk reduction comes from proving the supported workflow with synthetic evidence, then fixing only reproducible trust gaps.
```

Consequences:

- Start with `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX`.
- Open recognizer, document-hygiene, Scrub Key/roundtrip or audit fixes only from reproducible evidence.
- Do not start another broad UI package by default.
- Phase 7 pilots remain parked until the Phase 6 quality gate is explicitly approved.
- Local installer/packaging work remains deferred.
- Human review remains mandatory; no production-readiness claim is created by this decision.

---

'''
    text = DECISION_LOG.read_text(encoding="utf-8")
    marker = "## 2026-07-17 — D028"
    if marker not in text:
        anchor = "# SolidPrivacy Scrub — Decision Log\n\nThis file records accepted strategic, product and architecture decisions.\n\n---\n\n"
        text = replace_once(text, anchor, anchor + entry, "decision log anchor")
        DECISION_LOG.write_text(text, encoding="utf-8")


def update_risk_register() -> None:
    text = RISK_REGISTER.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table.",
        "Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table. Phase 6 now starts with a synthetic end-to-end validation matrix so new fixes are driven by reproducible false-negative, misclassification and over-masking evidence.",
        "risk R1 mitigation",
    )
    text = replace_once(
        text,
        "- Do not start a new feature automatically; consider `WP_MVP_UI_APP_VERIFICATION_CLOSEOUT` or a very small UI simplification package only with coordinator approval.",
        "- The current UI baseline is completed and app-verified. Do not start another UI feature automatically; open a narrowly scoped UI package only when Phase 6 validation exposes a concrete safety or workflow blocker.",
        "risk R6 recommendation",
    )
    text = replace_once(
        text,
        "- No generalized automated status artifact exists yet.",
        "- No generalized automated status artifact exists yet. `SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE` is scheduled after the synthetic validation, gap-triage and roundtrip packages.",
        "risk R8 gap",
    )
    RISK_REGISTER.write_text(text, encoding="utf-8")


def create_plan() -> None:
    PLAN.write_text(
        '''# SolidPrivacy Scrub — MVP Phase 6 Execution Plan

Status: active after `SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT` merges.

## Objective

Validate the supported MVP workflow with synthetic evidence before pilot expansion, local packaging or stronger trust claims.

```text
Import -> Scrub -> Review -> Handmatig aanvullen -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Package order

### 1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Create a versioned synthetic corpus, a machine-readable case manifest and automated tests covering supported TXT, DOCX and text-based PDF paths. Record expected detections, preserved role/context terms, manual additions, exports, Scrub Key, reinsert and audit outcomes.

### 2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Review only reproducible gaps from the matrix. Classify each as recognizer gap, misclassification, over-masking, document-extraction gap, expected limitation or manual-review dependency. Do not implement broad recognizer changes in the triage package.

### 3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Test and, through separately scoped fixes, harden headers, footers, tables, comments, tracked changes, hidden content, metadata, text order, residual placeholders and export readability. Preserve the report-only boundary until a clean-DOCX policy change is explicitly approved.

### 4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Test correct, missing, duplicate, altered, translated, merged and malformed placeholders; wrong or incomplete Scrub Keys; repeated values; partial restoration; and deterministic recovery reporting.

### 5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE

Produce a consistent machine-readable and human-readable evidence summary covering automatic findings, manual additions, unresolved candidates, document-hygiene warnings, exports, reinsert completeness and known limitations.

### 6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT

Decide whether the prototype is ready for controlled pilot validation. This gate does not establish production readiness and cannot remove the human-review requirement.

## Validation matrix minimum scope

- synthetic TXT, DOCX and text-based PDF;
- paragraphs, tables, headers and footers;
- names, addresses, email, telephone and dates;
- Dutch legal dossier, case, client, claim and administrative references;
- legal and care role words that must retain meaning;
- manual missed-value addition through the replacement table;
- normal TXT/DOCX/PDF exports within existing semantics;
- Scrub Key export/import and warning boundaries;
- pasted-text, TXT and DOCX reinsert plus PDF-to-TXT limitation;
- DOCX hygiene audit and residual-risk visibility;
- placeholder mutation simulations without external AI or cloud processing.

## Evidence rules

- synthetic data only;
- deterministic fixtures where possible;
- machine-readable case manifest;
- explicit expected and observed outcomes;
- failures become narrow workpackages, not silent test weakening;
- preserve legal meaning;
- no claim that all sensitive data is detected;
- no production-readiness claim;
- no Phase 7 pilot start without explicit quality-gate approval.

## Parallelization

Safe in parallel only when files and flows do not overlap:

- corpus/fixture design;
- helper-level validation utilities;
- audit evidence schema;
- documentation and risk review.

Keep sequential:

- recognizer changes;
- `presidio_streamlit.py` changes;
- document extraction/export changes;
- Scrub Key/reinsert semantics;
- quality-gate decisions.
''',
        encoding="utf-8",
    )


def finalize_claim_and_handover() -> None:
    claim = CLAIM.read_text(encoding="utf-8")
    claim = claim.replace("Status: in_progress", "Status: completed / ready for PR verification", 1)
    if "Implementation result:" not in claim:
        claim += f'''\n\nImplementation result:\n- Completed at: {STAMP}\n- Phase 6 roadmap and execution queue realigned.\n- Product code/tests/UI unchanged.\n- Handover: `{HANDOVER}`\n'''
    CLAIM.write_text(claim, encoding="utf-8")

    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(
        f'''# Handover — {PACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{PACKAGE}

## Status

Completed / ready for PR verification.

## Files added

- `MVP_PHASE6_EXECUTION_PLAN.md`
- `{HANDOVER}`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

## Tests

No product tests required. Documentation consistency and `git diff --check` are required in CI.

## Validation status

Documentation-only realignment completed.

## GitHub Actions status

Pending PR validation.

## Hugging Face sync status

Not functionally relevant; no app code changed.

## App verification status

Not applicable.

## Remaining risks

- The synthetic validation matrix must avoid implying production readiness.
- Any recognizer or document-processing fixes must be opened as separate evidence-driven packages.
- Phase 7 and local packaging remain gated.

## Next recommended step

Start `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX` after merge.
''',
        encoding="utf-8",
    )


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_decision_log()
    update_risk_register()
    create_plan()
    finalize_claim_and_handover()
    print("Phase 6 roadmap realignment applied.")


if __name__ == "__main__":
    main()
