from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_NUMBER = os.environ.get("GITHUB_RUN_NUMBER", "current")
TIMESTAMP = "2026-08-04 01:34 Europe/Amsterdam"


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_once(path: str, marker: str, entry: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        raise RuntimeError(f"Entry already present in {path}: {marker}")
    target.write_text(entry.rstrip() + "\n\n" + text, encoding="utf-8")


replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md",
    "Status: approved contract; action model and non-mutating component spike implemented and test-gated",
    "Status: approved contract; action model, component and authoritative table integration implemented and test-gated",
)
replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md",
    "The action model is implemented in `selection_mask_action.py`, and the isolated Streamlit v1 component spike proves UTF-16 selection transport, accessible menu behavior and bidirectional inspect/commit intents without product mutation. The next permitted package is sequential table integration; the review table, manual fallback and unchanged export/Scrub Key/reinsert semantics remain mandatory.",
    "The action model, local Streamlit v1 component and production integration now implement the approved all-exact route through the existing document-scoped manual rows and authoritative review table. The static renderer and manual form remain fallbacks, while export, Scrub Key and reinsert semantics remain unchanged. Deployment synchronization and live app verification are required before cross-flow promotion.",
)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — the all-exact contract, pure action model and isolated non-mutating Streamlit component spike are complete; the next gated step is sequential production table integration with rollback, synchronization and live app verification requirements.",
    "Last roadmap strategy update: 2026-08-04 — the all-exact contract, action model, local component and production review-table integration are complete; the active gate is GitHub-to-Hugging-Face synchronization and live app verification before cross-flow regression.",
)
replace_once(
    "ROADMAP.md",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, Streamlit-free action model and isolated non-mutating component spike are complete. The next permitted package is sequential production integration with the existing document-scoped manual-row state and authoritative review table. It must preserve the static/manual rollback path, export/Scrub Key/reinsert semantics, and require GitHub Actions, Hugging Face synchronization and live app verification. This line remains sequential and does not displace the active Phase 6 queue.",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. The integration adds one normal bound manual row, reruns before exports, keeps the review table authoritative, retains the manual/static rollback path and changes no export/Scrub Key/reinsert semantics. The next gate is synchronization and live app verification; only then may the cross-flow regression package start. This line remains sequential and does not displace the active Phase 6 queue.",
)

prepend_once(
    "WORKPACKAGES.md",
    "## 2026-08-04 01:34 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Status: completed in GitHub; deployment synchronization and app verification pending.

Goal:
- Integrate direct selection masking with the existing document-scoped manual rows and authoritative review table.

Implementation result:

```text
Interactive component in production review: implemented
Static renderer environment/exception fallback: retained
Manual Gemiste waarde toevoegen fallback: retained
Inspect after current editable table state: implemented
Commit exactly one bound manual row: implemented
Immediate rerun before serial review/export: implemented
Protected spans when visual markers hidden: implemented
Replay/stale/collision guards: retained
Undo latest unchanged selection row: implemented
Undo after visible table edit: blocked
Export/Scrub Key/reinsert semantics changed: false
```

Files added:
- `processed_text_selection_integration.py`
- `tests/test_processed_text_selection_integration.py`
- `tests/test_processed_text_selection_table_integration_contract.py`
- `PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_table_integration.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

Files changed:
- `processed_text_selection_component.py`
- `side_by_side_review_panel_ui.py`
- `presidio_streamlit.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Validation:
- exact finalized tree validated in GitHub Actions run #{RUN_NUMBER};
- frontend component tests and full Python regression required green before merge;
- Hugging Face sync and app verification pending after merge.

Next gate:
- synchronization plus focused live app verification;
- then `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`.
''',
)

prepend_once(
    "CHANGELOG.md",
    "## 2026-08-04 01:34 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Status: completed in GitHub; deployment and app verification pending.

Purpose:
- Make direct selection in `Verwerkte tekst` a safe input route into the existing manual replacement-table path.

Files added:
- `processed_text_selection_integration.py`
- `tests/test_processed_text_selection_integration.py`
- `tests/test_processed_text_selection_table_integration_contract.py`
- `PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_table_integration.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

Files changed:
- `processed_text_selection_component.py`
- `side_by_side_review_panel_ui.py`
- `presidio_streamlit.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation:
- promoted the local component wrapper while retaining the isolated spike alias;
- added interactive review with environment-controlled and exception-safe static fallback;
- added server-protected spans independent of marker visibility;
- processed inspect/commit only after the editable table and before serial review/export;
- appended one bound normal manual row through document-scoped `manual_mask_rows`;
- added immediate reruns, feedback and safe one-step undo;
- blocked undo when the visible table row was subsequently edited;
- retained the full review table and existing manual form.

Validation:
- exact finalized tree validated in GitHub Actions run #{RUN_NUMBER};
- automated merge is permitted only after frontend and full Python regressions succeed;
- Hugging Face sync and live app verification pending.

Intentionally not changed:
- all-exact version-one scope;
- export formats, filenames, MIME or download behavior;
- Scrub Key schema, binding, digest, warning or lifecycle;
- reinsert semantics;
- recognizers, profiles, thresholds or dependencies;
- external network, telemetry, browser persistence or cloud processing.
''',
)

prepend_once(
    "RELEASE_NOTES.md",
    "## 2026-08-04 — Gemiste waarden direct vanuit de tekst maskeren",
    '''## 2026-08-04 — Gemiste waarden direct vanuit de tekst maskeren

- In `Verwerkte tekst` kan een gebruiker een nog zichtbare gevoelige waarde selecteren en via rechtermuisknop, toetsenbord of `Masker selectie` toevoegen.
- Scrub controleert de selectie eerst op de server en toont hoeveel exacte voorkomens in het document worden geraakt.
- De gebruiker kiest zelf een algemeen type, zoals persoon, organisatie, locatie, e-mailadres, telefoonnummer, datum/tijd of referentie.
- De eerste versie maskeert alle veilige exacte voorkomens van de gekozen waarde; alleen één specifieke tekstpositie maskeren is nog niet ondersteund.
- Korte of botsende selecties die onderdeel zijn van een langere waarde worden geblokkeerd en verwezen naar de bestaande gedetailleerde invoer.
- Een bevestigde selectie wordt als normale handmatige rij zichtbaar in de bestaande vervangtabel.
- De meest recente ongewijzigde selectieactie kan één stap ongedaan worden gemaakt.
- `Gemiste waarde toevoegen`, de volledige vervangtabel en de statische reviewweergave blijven als fallback beschikbaar.
- Exportformaten, Scrub Key, terugzetten, herkenningsprofielen en documentverwerking zijn niet gewijzigd.
- Menselijke controle blijft verplicht; de functie versnelt correctie maar geeft geen garantie dat alle gevoelige gegevens zijn gevonden.

---''',
)

replace_once(
    "RISK_REGISTER.md",
    "Its frozen contract, pure action model and isolated component spike require a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table. The model proves UTF-16 selection validation, impact bands, collision/replay/stale protection and safe row construction; the spike proves local bidirectional event transport, accessible menu behavior and correct offsets around marked nodes without product mutation.",
    "Its frozen contract, action model, local component and production integration enforce a two-stage server-authoritative inspect/commit protocol. Accepted commits append one normal document-scoped row, rerun before export and remain visible in the authoritative review table. The static renderer and manual form remain fallbacks until deployment and live verification are green.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The contract freezes the route, the action model implements server-authoritative validation/row construction, and `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE` proves the isolated browser transport. The review table remains source of truth and production integration remains sequentially gated.",
    "- The contract, action model and component spike are now connected through `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`. The review table remains source of truth; the component is only an input route into normal bound manual rows.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The action model and component spike now prove exact-occurrence bands, Unicode collision guards, replay/stale protection, safe undo, text-node offsets and accessible bidirectional transport. The remaining high-risk gate is production table integration with rollback plus cross-flow and live app verification.",
    "- Production table integration now preserves collision/replay/stale guards, hidden-marker protection, immediate rerun and edit-aware undo. The remaining high-risk gates are deployment synchronization, live browser/app verification and full export/Scrub Key/reinsert cross-flow regression.",
)

replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_table_integration.md",
    "Status: in_progress",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
)
replace_once(
    "PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md",
    "Status: implementation under validation  ",
    "Status: implemented and GitHub test-gated; deployment verification pending  ",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Status: implementation under validation",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "- Controlled production patch applied through GitHub Actions.\n- Exact final governance and regression validation pending.\n- Hugging Face sync pending merge.\n- App verification pending merge and synchronization.",
    f"- Controlled production patch and exact final governance validated in GitHub Actions run #{RUN_NUMBER}.\n- Frontend component tests and the complete Python regression must succeed before merge.\n- Hugging Face sync pending merge.\n- App verification pending merge and synchronization.",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Pending exact merge-candidate validation.",
    f"Exact finalized tree is validated in run #{RUN_NUMBER}; merge remains conditional on frontend and full Python regression success.",
)
