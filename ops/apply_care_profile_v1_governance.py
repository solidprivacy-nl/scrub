from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 15:31 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, block.rstrip() + "\n\n" + current)


def append_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, current.rstrip() + "\n\n" + block.rstrip() + "\n")


def update_roadmap() -> None:
    path = "ROADMAP.md"
    current = read(path)
    old_update = (
        "Last roadmap strategy update: 2026-08-03 — Phase 9 local desktop packaging "
        "remains gated, with an AI-first implementation model and explicit human signing, "
        "release, security-claim and UX-acceptance gates."
    )
    new_update = (
        "Last roadmap strategy update: 2026-08-03 — Zorgfilter v1 is approved as an "
        "evidence-driven profile line; policy and synthetic corpus work may proceed while "
        "recognizer and UI integration remain sequential and test-gated."
    )
    if old_update in current:
        current = current.replace(old_update, new_update, 1)
        write(path, current)

    marker = "## 11. Zorgfilter v1 — evidence-driven care profile"
    block = f"""## 11. Zorgfilter v1 — evidence-driven care profile

Approved: {TIMESTAMP}

The first product wedge already identifies Legal and Zorg as the most relevant Dutch professional domains. Zorg now receives an explicit profile line rather than remaining an incidental subset of general and legal recognition.

### Approved policy

```text
Geboortedatum: vervangen
Overige exacte zorgdata: controleren en standaard geselecteerd
Patiënt- en cliëntidentificatie: vervangen
Zorgverleneridentificatie: controleren en standaard geselecteerd
Diagnose, medicatie, dosering, labwaarden en observaties: behouden
Zeldzame-casus-herleidbaarheid: auditwaarschuwing, niet blind maskeren
```

The core product rule is:

```text
Remove identity and patient-specific administrative references while preserving clinical meaning.
```

Zorgfilter v1 is not a generic medical-word filter. It must not make care records clinically unreadable.

### Initial document scope

- daily nursing/care reports;
- care plans and evaluations;
- nursing transfers;
- medical specialist discharge letters;
- GP referrals and consultation letters;
- medication overviews or administration lists;
- laboratory reports;
- MIC/MIM/VIM care-incident reports.

### Architecture and sequencing

The first packages are pure helper, policy, corpus and evidence work. They may proceed without reopening the shared Streamlit review/export flow. The future current-UI integration is permitted by explicit coordinator approval, but only after the corpus baseline, gap triage, recognizer contracts and recognizer implementation are green and no parallel worker is editing the same UI surface.

Preferred helper direction:

```text
care_profile_policy.py
care_test_examples.py
care_profile_baseline.py
care_reference_taxonomy.py
dutch_care_recognizers.py
recognition_profiles.py
```

The existing broad `NL_HEALTHCARE_REFERENCE` category must be assessed and split. Patient numbers, referral references, insurance identifiers and DBC/clinical codes do not share one safe default action.

### Current and final interface direction

Current prototype after test-gated integration:

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

Final desktop workspace:

```text
[ Algemeen NL ] [ Zorg ] [ Juridisch ] [ Internationaal ]
```

The active profile remains visible in the document toolbar and never changes silently.

### Sequential workpackages

```text
1. SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION
2. SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE
3. SCRUB-WP_CARE_PROFILE_GAP_TRIAGE
4. SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS
5. SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION
6. SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR
7. SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION
8. SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX
9. SCRUB-WP_CARE_PROFILE_APP_VERIFY
10. SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT
```

Safety boundaries:

- synthetic data only;
- no blind masking of clinical meaning;
- no change to Scrub Key, export or reinsert semantics without a separate package;
- human review remains required;
- corpus or benchmark success does not prove production readiness;
- no cloud document processing is introduced.
"""
    append_once(path, marker, block)


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: in_progress; helper/test-first implementation on dedicated branch.

Goal:
- Establish the approved Zorgfilter v1 policy and a fully synthetic, machine-readable care-document corpus before adding recognizers or UI.

Current package scope:
- roadmap, decision and risk alignment;
- pure care-profile action contract;
- eight synthetic care-document families;
- corpus contract tests;
- current custom-recognizer baseline helper and report generator.

Approved policy:
- date of birth and patient/client identity: replace;
- other exact care dates and provider identity: review, selected by default;
- diagnosis, medication, dosage, lab results and observations: preserve;
- rare-case re-identification: audit warning only.

Sequential follow-up:
1. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`
2. `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`
3. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`
4. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`
5. `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`
6. `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`
7. `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`
8. `SCRUB-WP_CARE_PROFILE_APP_VERIFY`
9. `SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT`

Boundaries:
- no Streamlit change in this package;
- no recognizer behavior change yet;
- no export, Scrub Key, reinsert, cloud or dependency change;
- synthetic data only;
- current Phase 6 binding verification remains an independent active gate.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: in progress; policy/corpus foundation implemented on a dedicated branch.

Purpose:
- Create the evidence base for an explicit Dutch Zorg profile without prematurely changing recognizers or the UI.

Files added:
- `CARE_PROFILE_V1_PLAN.md`
- `care_profile_policy.py`
- `care_test_examples.py`
- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_policy_contract.py`
- `tests/test_care_profile_corpus_contracts.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `workpackage_claims/scrub_wp_care_profile_v1_policy_and_corpus_foundation.md`

Main changes:
- froze replace/review/preserve/audit-only care policy actions;
- added eight fully synthetic document families;
- separated patient identifiers from provider/location review and clinical content preservation;
- added a deterministic baseline helper for current Dutch custom recognizers;
- made no recognizer or product-UI behavior change.

Validation:
- GitHub Actions pending on the branch;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- current three profile choices;
- recognizer registration or thresholds;
- review table, export, Scrub Key and reinsert semantics;
- runtime, dependencies or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_decision_log() -> None:
    marker = "## 2026-08-03 — D039 — Add Zorgfilter v1 with clinical-context preservation"
    block = """## 2026-08-03 — D039 — Add Zorgfilter v1 with clinical-context preservation

Status: accepted product and implementation-sequence decision

Decision:

```text
Add an explicit Dutch Zorg profile. Replace date of birth and patient/client identity by default. Show other exact care dates, provider identity, BIG/AGB, organizations and locations for review and select them by default. Preserve diagnosis, medication, dosage, laboratory results and observations. Surface rare-case indirect re-identification as residual-risk evidence rather than blindly masking clinical meaning.
```

Implementation sequence:
- policy and fully synthetic corpus first;
- current-engine baseline and gap triage second;
- recognizer contracts and pure recognizer implementation before UI;
- central profile configuration before adding the fourth Streamlit profile;
- cross-profile regression and live app verification before closeout.

Reason:
- Care documents contain both direct identifiers and essential clinical meaning.
- A broad medical-word filter would destroy usability and potentially clinical/legal context.
- The current `NL_HEALTHCARE_REFERENCE` category combines values with different privacy policies and must be split through evidence-driven work.
- A fourth UI label without dedicated detection evidence would be cosmetic and unsafe.

Boundaries:
- synthetic data only;
- human review remains required;
- no production-readiness claim from corpus or benchmark results;
- no silent profile switching;
- no cloud document processing;
- no export, Scrub Key or reinsert semantic change in the foundation package.
"""
    prepend_once("DECISION_LOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    marker = "## R10 — Care-profile under-detection and clinical over-masking"
    block = """## R10 — Care-profile under-detection and clinical over-masking

Status: mitigating  
Impact: critical

Risk:

```text
A care document retains patient or trajectory identifiers, or Scrub removes diagnosis, medication, laboratory values, observations or care context and makes the document misleading or unusable.
```

Mitigation direction:

- explicit Zorgfilter v1 policy contract;
- fully synthetic corpus across eight care-document families;
- exact replace, review and preserve expectations;
- current-engine baseline before recognizer changes;
- separate care taxonomy and recognizers;
- negative tests for medical numbers, dosages, times, vital signs and laboratory values;
- cross-profile regression before UI promotion;
- human review and residual-risk evidence remain mandatory.

Approved policy boundary:

```text
Patient identity and date of birth: replace.
Other exact care dates and provider identity: review, selected by default.
Clinical meaning: preserve.
Rare-case indirect identification: audit warning, not blind masking.
```

The current broad `NL_HEALTHCARE_REFERENCE` category is insufficient because it combines patient numbers, referral references, insurance identifiers and DBC/clinical codes under one behavior.

---
"""
    current = read(path)
    if marker not in current:
        anchor = "## Product-claim boundary"
        if anchor not in current:
            raise RuntimeError("RISK_REGISTER.md anchor not found")
        current = current.replace(anchor, block + "\n" + anchor, 1)
        write(path, current)


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_decision_log()
    update_risk_register()

    Path("ops/apply_care_profile_v1_governance.py").unlink(missing_ok=True)
    Path(".github/workflows/apply-care-profile-v1-governance.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
