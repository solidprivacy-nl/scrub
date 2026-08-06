from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def prepend_once(path: str, marker: str, block: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        return
    target.write_text(block.rstrip() + "\n\n" + text, encoding="utf-8")


def insert_before_once(path: str, marker: str, anchor: str, block: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        return
    if anchor not in text:
        raise RuntimeError(f"Anchor not found in {path}: {anchor!r}")
    target.write_text(text.replace(anchor, block.rstrip() + "\n\n" + anchor, 1), encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


GOVERNANCE_SECTION = """## Implementation-versus-assurance separation

Consequential work uses the canonical two-role model linked from `control/PROJECT_GOVERNANCE_BOOTSTRAP.md` and the project contract in `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`.

```text
implementation_operations
governance_release_assurance
```

The user gives one instruction and receives one consolidated status. Implementation prepares an identifiable release candidate but may not certify its own completion. Governance independently reconstructs the candidate and issues `PASS`, `FAIL` or `INDETERMINATE`; it may not silently repair what it reviews.

Before its initial decision, the assurance worker must not read the implementation handover, self-assessment or conclusions. It works from the requested outcome, authoritative project files, candidate source/diff, acceptance criteria and raw machine/deployment evidence. Only after recording the initial decision may it open the implementation handover for disclosure and administrative closeout checks.

A candidate requiring repair returns to implementation and receives a fresh assurance pass. Consequential implementation and verification must be separate workpackages and separate workers/sessions.

For consequential work, read after the mandatory start sequence:

1. `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
2. `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
"""

SHORT_GOVERNANCE_SECTION = """Apply the project's implementation-versus-release-assurance separation and blind-review boundary for consequential work. Read:

1. `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
2. `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`

Implementation may only prepare a release candidate. A separate `governance_release_assurance` worker/session independently reconstructs and verifies it without reading the implementation handover or conclusions before its initial `PASS`, `FAIL` or `INDETERMINATE`. Governance may not silently repair the candidate it reviews.
"""

WORKPACKAGES_ENTRY = """## 2026-08-06 11:37 Europe/Amsterdam — Two-role governance adoption and processed-text cross-flow regression

### SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION

Status: `RELEASE_CANDIDATE_READY`; independent governance verification pending.

Goal:
- Adopt the canonical cross-project implementation-versus-release-assurance model used by Weekly ETF, strengthened for Scrub with a blind-review boundary.

Candidate files:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- project prompt, roadmap and decision-log invocation records;
- separate implementation and verification workpackages.

Verification gate:
- `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY` must be claimed by `governance_release_assurance` in a separate worker/session;
- before its initial decision, that worker must not read implementation handovers or implementation conclusions;
- governance may issue only `PASS`, `FAIL` or `INDETERMINATE` and may not silently repair the candidate.

### SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: `RELEASE_CANDIDATE_READY`; GitHub Actions and independent governance verification pending.

Goal:
- Prove with synthetic chain tests that a processed-text selection row remains one normal authoritative review-table row across document export, Scrub Key, TXT/DOCX reinsert and audit evidence.

Candidate evidence:
- `tests/test_processed_text_selection_cross_flow_regression.py`;
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`;
- no production product-code or UI changes.

Required independent follow-up:
1. `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY`;
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY`;
3. only after both governance passes may `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT` start.

Safety boundary:
- synthetic data only;
- no recognizer, replacement, export, filename, MIME, Scrub Key, reinsert, audit, runtime or UI semantic changes;
- review-table include state and human review remain authoritative;
- custom replacement text remains document-exportable but verified bound-key generation must fail closed.
"""

CHANGELOG_ENTRY = """## 2026-08-06 11:37 Europe/Amsterdam — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION / SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: implementation `RELEASE_CANDIDATE_READY`; GitHub Actions and independent governance assurance pending.

Purpose:
- adopt the Weekly ETF donor's canonical implementation-versus-release-assurance model for Scrub;
- strengthen it with a blind-review boundary so the assurance worker does not read implementation conclusions before its initial decision;
- add end-to-end synthetic regression evidence from processed-text selection commit through exports, bound Scrub Key, TXT/DOCX reinsert and audit outputs.

Files added:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`;
- `tests/test_processed_text_selection_cross_flow_regression.py`;
- implementation claim and handover files.

Files changed:
- `PROJECT_PROMPT.md`;
- `PROJECT_PROMPT_SHORT.md`;
- `ROADMAP.md`;
- `WORKPACKAGES.md`;
- `DECISION_LOG.md`;
- `CHANGELOG.md`.

Regression coverage:
- selection-created row provenance, binding, all-exact occurrence count and authoritative include state;
- processed text/TXT export;
- original-DOCX replacement path;
- schema-1.1 bound Scrub Key generation and fail-closed custom-text behavior;
- verified TXT and DOCX reinsert;
- replacement CSV and scrub-report audit evidence;
- local-only/no-AI/no-cloud metadata.

Validation:
- local execution unavailable in this connector-only session;
- GitHub Actions pending on the candidate PR;
- independent governance decisions deliberately not issued by implementation.

Intentionally not changed:
- production Python/Streamlit behavior;
- recognizers, profiles, thresholds or review decisions;
- export bytes, filenames or MIME types;
- Scrub Key schema/binding or reinsert semantics;
- audit semantics, dependencies, runtime or Hugging Face app behavior.
"""

DECISION_ENTRY = """## 2026-08-06 — D042 — Separate implementation from blind independent release assurance

Status: accepted project-governance and release-control decision

Decision:

```text
Adopt CROSS_PROJECT_TWO_ROLE_GOVERNANCE_V1 for consequential Scrub work. Use one coordinator and two separated roles: implementation_operations and governance_release_assurance. Implementation prepares an identifiable candidate but cannot certify it. Governance reconstructs it independently and cannot silently repair it.
```

Scrub-specific strengthening:

```text
Before its initial PASS / FAIL / INDETERMINATE, governance may inspect the requested outcome, authoritative control files, candidate source/diff, acceptance criteria and raw machine/deployment evidence, but may not read the implementation handover, implementation self-assessment or implementation conclusions.
```

Reason:
- Scrub processes privacy-sensitive professional documents and creates re-identification-sensitive Scrub Keys;
- builder self-certification creates avoidable confirmation bias and weakens release confidence;
- the Weekly ETF donor architecture already establishes a mature coordinator/implementation/assurance split;
- the user's explicit requirement is stronger than ordinary review and requires conclusion isolation before the initial assurance decision.

Operating consequences:
- consequential implementation and verification are separate workpackages and separate workers/sessions;
- the user continues to give one instruction and receives one consolidated status;
- a failed or indeterminate candidate returns to implementation and requires a fresh assurance pass;
- implementation statuses are limited to `IMPLEMENTATION_IN_PROGRESS`, `IMPLEMENTATION_BLOCKED` and `RELEASE_CANDIDATE_READY`;
- assurance decisions are `PASS`, `FAIL` or `INDETERMINATE`;
- merge/deployment execution and independently confirmed outcome remain distinct statuses.

Initial maturity:
- `LEVEL_1_CHECKLIST`;
- target `LEVEL_2_MACHINE_EVIDENCE` through a later structured assurance-record package;
- no claim that documentation alone provides hard CI or post-action enforcement.

Authority:
- canonical standard: `market-predictions/control-plane/control/CROSS_PROJECT_TWO_ROLE_GOVERNANCE_STANDARD_V1.md`;
- project bootstrap: `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- project contract: `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`.
"""

ROADMAP_SECTION = """## Operational governance — implementation and blind release assurance

Consequential Scrub work now follows the canonical cross-project two-role standard used by the Weekly ETF donor architecture:

```text
implementation_operations
→ identifiable release candidate
→ governance_release_assurance blind reconstruction
→ PASS / FAIL / INDETERMINATE
→ authorized action
→ independent post-action confirmation
```

The user remains the single coordinator-facing principal. Implementation cannot certify its own candidate, and governance cannot silently repair it. Scrub adds a blind-review boundary: before its initial decision, governance may inspect source, criteria and raw machine evidence but not implementation handovers, self-assessments or conclusions.

The current maturity is `LEVEL_1_CHECKLIST`, with a later target of `LEVEL_2_MACHINE_EVIDENCE`. This adoption does not claim a hard CI gate. The next premium UI package remains blocked until independent assurance passes both the governance-adoption candidate and the processed-text cross-flow regression candidate.

Governed by:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `DECISION_LOG.md` D042.
"""


insert_before_once(
    "PROJECT_PROMPT.md",
    "## Implementation-versus-assurance separation",
    "## Current way of working",
    GOVERNANCE_SECTION,
)
insert_before_once(
    "PROJECT_PROMPT_SHORT.md",
    "Apply the project's implementation-versus-release-assurance separation",
    "Follow the current workpackage plan",
    SHORT_GOVERNANCE_SECTION,
)
prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION",
    WORKPACKAGES_ENTRY,
)
prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION / SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION",
    CHANGELOG_ENTRY,
)
prepend_once(
    "DECISION_LOG.md",
    "D042 — Separate implementation from blind independent release assurance",
    DECISION_ENTRY,
)
insert_before_once(
    "ROADMAP.md",
    "## Operational governance — implementation and blind release assurance",
    "## 1. Product vision",
    ROADMAP_SECTION,
)
replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-05 — compact bound-placeholder display is deployed and live verified; direct user evidence confirms that local decluttering has not yet removed the long-form, form-like application structure, so a premium single-task app-shell line is now sequenced after the existing cross-flow safety regression.",
    "Last roadmap strategy update: 2026-08-06 — the Weekly ETF donor's canonical implementation-versus-release-assurance model is adopted for consequential Scrub work, strengthened with blind review before the initial assurance decision; the premium single-task app-shell line remains gated by independent governance passes after the cross-flow safety regression.",
)
