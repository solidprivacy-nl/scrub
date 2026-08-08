from pathlib import Path


CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
RELEASE_NOTES = Path("RELEASE_NOTES.md")
CLAIM = Path("workpackage_claims/scrub_wp_premium_app_shell_implementation.md")
HANDOVER = Path("handover/workpackages/20260808_1655_premium_app_shell_state_preservation_repair.md")

changelog = CHANGELOG.read_text(encoding="utf-8")
entry = """## 2026-08-08 16:55 Europe/Amsterdam — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repair after blind-assurance FAIL

Status: `RELEASE_CANDIDATE_READY` only after a fresh exact-head full-suite run; fresh independent assurance remains mandatory.

Independent assurance on prior head `2b04ca6260bddee07fbcf901239cee2955bd6dc7` returned `FAIL` because switching `Standaard → Expert` could silently reset an explicitly selected Zorg profile to the hard-coded Expert default Juridisch. The same repair cycle reviewed operator, threshold, entity selection, allow/deny lists and analyzer configuration as processing-affecting state.

Repair:
- Standard and Expert now hydrate the same persisted processing settings;
- entering Expert no longer uses a hard-coded recognition-profile or operator default when a valid current choice exists;
- returning to Standard rehydrates the Standard profile widget from the shared processing state;
- threshold, entity selection, allow/deny lists and analyzer/model settings are preserved across presentation-only switches;
- deterministic processing-generation synchronization now runs in both presentation modes;
- presentation-only switching with unchanged settings preserves valid downstream lineage;
- a real processing-affecting Expert change invalidates processed/review/export lineage fail-closed;
- Standard still refuses unsupported Expert-only operators without silently rewriting them.

Regression evidence before administrative finalization:
- GitHub Actions Tests run #2229 / ID `31263099583`, job `93116829430`;
- PR merge candidate `bd3c404f7075d86620272bf28c9a5192006e8209`;
- `python -m pytest -q tests` → `1235 passed in 14.48s`;
- new coverage explicitly includes Standard Zorg → Expert → Standard state preservation and real-change invalidation.

Protected semantics unchanged:
- recognizers/profile rules and threshold meaning;
- review-table/include authority and direct masking;
- export bytes, filenames and MIME types;
- Scrub Key, reinsert and audit semantics;
- dependencies and local/cloud processing boundary;
- mandatory human review.

A fresh exact-head regression is required after this administrative closeout, followed by a new blind `governance_release_assurance` review. The later Premium Input Stage package remains blocked.

---

"""
if not changelog.startswith(entry):
    CHANGELOG.write_text(entry + changelog, encoding="utf-8")

release_notes = RELEASE_NOTES.read_text(encoding="utf-8")
release_entry = """## 2026-08-08 — Standaard en Expert behouden dezelfde verwerkingskeuzes

- Wisselen tussen `Standaard` en `Expert` verandert niet langer ongemerkt de gekozen controlemodus of andere verwerkingsinstellingen.
- Een gekozen Zorg-, Juridisch- of ander profiel blijft behouden wanneer alleen de weergave verandert.
- Ook gevoeligheid, gegevenstypen, woordenlijsten en technische herkenningsinstellingen worden over beide weergaven heen consistent gehouden.
- Alleen een echte wijziging aan een verwerkingsinstelling maakt eerdere controle- en downloadstatus ongeldig; alleen wisselen van weergave doet dat niet.
- Herkenning, vervangingslogica, exportbestanden, Scrub Key, terugzetten en verplichte menselijke controle zijn inhoudelijk niet gewijzigd.

---

"""
if not release_notes.startswith(release_entry):
    RELEASE_NOTES.write_text(release_entry + release_notes, encoding="utf-8")

workpackages = WORKPACKAGES.read_text(encoding="utf-8")
workpackages = workpackages.replace(
    "### 2. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — active draft PR #85, amended",
    "### 2. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repaired candidate pending fresh assurance",
    1,
)
workpackages = workpackages.replace(
    "Status: active draft; **production integration gated by package 1**.  ",
    "Status: `RELEASE_CANDIDATE_READY` after repair of the prior assurance FAIL; fresh exact-head CI + fresh blind assurance required before merge.  ",
    1,
)
repair_note = """
Repair gate — 2026-08-08:
- prior exact head `2b04ca6260bddee07fbcf901239cee2955bd6dc7` received independent `FAIL` because Standard → Expert could silently reset Zorg to Juridisch;
- repaired candidate must preserve profile, operator, threshold, entity selection, allow/deny lists and analyzer configuration across presentation-only switching;
- presentation-only Standard ↔ Expert must keep deterministic processing generation and valid downstream lineage unchanged;
- a real processing-setting change must invalidate downstream lineage fail-closed;
- dedicated Standard Zorg → Expert → Standard regression coverage is mandatory;
- the repaired head requires a completely fresh blind reviewer; prior issue #90 cannot authorize the repair.

"""
anchor = "Existing reusable work:\n"
if repair_note not in workpackages:
    workpackages = workpackages.replace(anchor, repair_note + anchor, 1)
WORKPACKAGES.write_text(workpackages, encoding="utf-8")

claim = CLAIM.read_text(encoding="utf-8")
claim = claim.replace("Status: `IMPLEMENTATION_IN_PROGRESS`", "Status: `RELEASE_CANDIDATE_READY`", 1)
claim += """

## Repair validation result — 2026-08-08 16:55 Europe/Amsterdam

The functional repair and new regression contracts are green before final administrative identity:

```text
Tests run #2229 / ID 31263099583
job 93116829430
branch head under test: f6dd1fede240f9cacf29bd5323dec9f182052828
PR merge candidate: bd3c404f7075d86620272bf28c9a5192006e8209
base main in tested merge candidate: 2831da154e6c299b3616d62a37f151ebfa9c45f1
command: python -m pytest -q tests
result: 1235 passed in 14.48s
conclusion: success
```

The final administrative commit changes candidate identity but not runtime behavior. Therefore this claim is not sufficient release evidence by itself: a fresh full exact-head GitHub Actions run on the final candidate is mandatory before handoff to a new blind reviewer.
"""
CLAIM.write_text(claim, encoding="utf-8")

HANDOVER.parent.mkdir(parents=True, exist_ok=True)
HANDOVER.write_text("""# Handover — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION state-preservation repair

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repair Standard/Expert processing-state preservation`  
Status: `RELEASE_CANDIDATE_READY` subject to final exact-head CI and fresh blind assurance.

## Files added/changed in this repair cycle

Added:
- `tests/test_premium_presentation_state_preservation.py`
- this repair handover.

Changed:
- `premium_streamlit_state.py`
- `presidio_streamlit.py`
- `tests/test_premium_streamlit_state.py`
- `tests/test_care_profile_current_ui_integration_snapshot.py`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_premium_app_shell_implementation.md`

Temporary repair executor/workflow self-deleted and are not intended to be part of the persistent candidate diff.

## Repair implemented

- Hydrate Expert profile from the shared persisted profile instead of hard-coded index 1.
- Hydrate operator, threshold, entity selection, allow/deny lists and analyzer/model settings across Standard/Expert.
- Rehydrate the Standard profile widget when returning from Expert.
- Synchronize deterministic processing generation in both presentation modes.
- Preserve downstream lineage when only presentation changes.
- Invalidate downstream lineage fail-closed when processing-affecting settings actually change.
- Preserve the existing block against silently coercing Expert-only operators in Standard.

## Tests

Pre-administration full regression:

```text
GitHub Actions Tests #2229 / run 31263099583
job 93116829430
python -m pytest -q tests
1235 passed in 14.48s
conclusion: success
```

Focused new contracts include Standard Zorg → Expert → Standard preservation, operator/threshold/entity generation sensitivity and source-level hydration/synchronization assertions.

## Validation status

Functional repair validation: green before final administration.  
Final exact-head validation: required after this handover/administration commit.

## GitHub Actions status

Pre-administration candidate: `success` as above.  
Final candidate: pending a fresh exact-head full-suite run.

## Hugging Face sync status

Not run pre-merge. Runtime source changed, so exact GitHub → Hugging Face synchronization must be verified after an independently authorized merge.

## App verification status

Pending. UI behavior changed; coordinator live-app verification is mandatory after merge and successful synchronization/runtime health confirmation.

## Remaining risks

- Streamlit widget/session-state behavior must still receive independent source review and later live app verification.
- A fresh assurance worker must independently verify that presentation switching cannot alter processing settings or stale lineage.
- No later Premium Input/Review/Export package may start until this App Shell gate is passed, merged and post-merge/app-verified.

## Next recommended step

1. Run the complete regression suite on the final exact PR head after administration.
2. Freeze that head and record raw run/job/merge-candidate evidence in PR #85 and issue #84 metadata.
3. Open a new blind assurance issue for a fresh `governance_release_assurance` worker; do not reuse prior issue #90.
4. Merge only after independent PASS, then verify exact-main Actions, GitHub→Hugging Face sync/runtime health and live app behavior.
""", encoding="utf-8")

print("repair administration finalized")
