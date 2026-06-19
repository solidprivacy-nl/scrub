# Review debug elements collapse plan

Workpackage: `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning/design-only.

## 1. Purpose

This is an interface-cleanup plan, not a new review/safeguard/benchmark loop.

Goal:

```text
Make the normal review flow calmer and less prototype-like by moving debug/technical/governance details to secondary UI layers, while keeping all review, audit and export controls available.
```

Non-goals:

```text
No product UI implementation in this package.
No new review layer.
No new benchmark or threshold gate.
No new export gate.
No Scrub Key, reinsert, recognizer or export semantics changes.
No removal of audit details.
```

## 2. Review-loop trap guardrail

The next implementation package must stay small.

Do:

```text
rename/collapse existing visible debug-like elements
keep existing controls available
verify with screenshot and existing tests
```

Do not do:

```text
create another planning package
create another diagnostic framework
create another benchmark gate
turn this into a review-of-review cycle
redesign the whole app in one pass
```

Definition of success for the next implementation:

```text
A normal user sees a calmer review flow.
The review table and audit controls are still reachable.
No export/reinsert/Scrub Key behavior changes.
```

## 3. Current UI inventory and classification

Classification:

```text
A. Primair zichtbaar houden
B. Inklappen onder bestaande of nieuwe expander
C. Hernoemen naar gebruikersvriendelijke tekst
D. Alleen tonen als technische details/audit
E. Niet wijzigen wegens privacy/review-risico
```

| Element | Current text / location | Problem | Risk if changed | Classification | Proposed treatment | Next WP allowed to execute | Test / verification requirement |
|---|---|---|---|---|---|---|---|
| Central review surface | `2. Controleer de tekst` plus side-by-side caption | Caption is slightly technical but the surface is the main user task. | Hiding it weakens document review. | A / E | Keep visible. Optional later copy polish only. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | App screenshot confirms side-by-side review still visible. |
| Marker toggle | `Markeringen tonen` | Useful and understandable. | Removing it weakens visual review support. | A / E | Keep visible unchanged in collapse implementation. | none in next WP | Existing visual toggle remains visible. |
| Found-data guidance | `3. Controleer gevonden gegevens` and guidance text | Necessary but there is some repeated wording about the table being leading. | Over-trimming can reduce safe review behavior. | A / C | Keep visible; reduce duplicate captions only in later copy polish. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | Review table/source-of-truth sentence remains somewhere visible. |
| Explanation expander | `Uitleg bij deze controle` | Good location for longer guidance; already collapsed. | Removing guidance weakens safe use. | B | Keep collapsed. Do not expand by default. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` may leave unchanged | Expander remains available. |
| Review status line | `Reviewstatus: ...` | Slightly internal but useful status signal. | Removing it may reduce review orientation. | A / C | Keep visible for now; optionally rename later if copy package needs it. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | Counts still visible or deliberately preserved. |
| Focus filter | `Focusfilter voor controle` | Useful review tool; not debug-only. | Hiding may make checking harder. | A | Keep visible. | none in next WP | Filter remains available. |
| Focus result dataframe | `x van y rij(en) zichtbaar...` and helper caption | Can feel technical but only appears after filter use. | Hiding context may confuse filtered view. | C | Keep, but simplify copy later. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | If filter used, filtered overview still explains it is read-only. |
| Candidate audit | `Mogelijke gemiste waarden` | Important safety layer, but audit-like wording. | Hiding candidate warnings weakens false-negative review. | A / C / E | Keep visible when candidates exist; rename to `Mogelijk extra te controleren waarden` in implementation if low-risk. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Candidate warning still expands automatically when candidates exist. |
| Candidate empty state | `Geen mogelijke gemiste referenties gevonden door de auditlaag.` | Mentions audit layer, but only appears in expander. | Low. | C | Later copy: `Geen extra te controleren referenties gevonden.` | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | No behavioral change. |
| Full replacement table | `Vervangtabel controleren — <items> items` | Still technical, but already collapsed and source of truth. | Renaming too aggressively may obscure fallback role. | B / E | Keep collapsed and available. Optional later rename to `Alle gevonden gegevens controleren — <items> items`. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION`, not next debug-collapse if scope grows | Existing `replacement_editor` remains available and collapsed. |
| Table source-of-truth caption | `De vervangtabel blijft leidend...` | Repeated in multiple places. | Removing all instances weakens safety. | A / C | Keep one clear instance; do not remove entirely. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` | At least one visible source-of-truth statement remains. |
| Technical table columns | `Technisch type`, `Technische score`, `Technische bron` | Technical, but hidden inside replacement table/advanced details. | Removing can weaken auditability. | D / E | Keep available. Do not make primary. | none in next WP | Technical columns remain in table or advanced details. |
| Technical details expander | `Technische details bij de vervangtabel` | Valid advanced content, but label is technical/prototype-like. | Removing weakens auditability. | B / C / D | Rename to `Geavanceerde details bij de vervangtabel`; keep collapsed. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Expander remains collapsed and still shows technical columns. |
| Serial review heading | `Serial review — experimentele reviewhulp` | Strong prototype signal; English/internal and says experimental. | Removing panel would remove optional review aid. | C | Rename to `Stap voor stap controleren`. Keep panel available. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Panel still renders and still does not mutate review rows. |
| Serial review info | `Alleen-lezen hulpweergave...` | Useful safety wording but long/prototype-like. | Removing all safety text weakens source-of-truth clarity. | C | Replace with `Controleer gevonden gegevens één voor één. De vervangtabel blijft leidend voor beslissingen en export.` | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Source-of-truth message remains visible. |
| Serial governance caption | `table-first baseline · non-destructive · report-only · no Scrub Key mutation · no export blocking · no reinsert behavior change` | Pure governance/debug text in primary UI. | Removing from UI is safe if behavior/tests preserve it. | D | Hide from primary flow. Preserve in docs/tests; optionally move to a technical expander only if needed. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Existing tests must still prove no mutation/export/reinsert side effects. |
| Serial filter label | `Serial review filter` | English/internal. | Low. | C | Rename to `Filter voor stap-voor-stap controle`. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Filter options remain unchanged. |
| Context fallback labels | `Context preview fallback`, `Prefix`, `Match`, `Suffix` | Technical labels; shown in serial panel. | Changing labels low risk if content remains. | C | Rename only if implementation remains small: `Context`, `Vooraf`, `Gevonden tekst`, `Daarna`. | `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` unless already touching serial panel | Serial context card still visible. |
| Memory section | `4. Onthoud herbruikbare vervangingen` and memory file path | Useful, but `Geheugenbestand: ...` is technical. | Removing file path may reduce transparency. | B / D | Keep section for now. Consider moving file path to technical details later. | not in next WP unless scope remains tiny | Memory save/clear behavior unchanged. |
| Export section | `5. Exporteer resultaat` groups | Verified improved interface. | Changing it risks export regressions. | A / E | Do not touch in this implementation. | none | Existing export labels/groups remain. |
| DOCX hygiene audit | report-only audit panel after DOCX export | Important but can dominate lower flow. | Hiding too much may weaken hidden-content awareness. | B / D / E | Keep available. Do not move in next WP unless only label/collapse is safe. Future option: compact summary + collapsed details. | separate later package or `WP_REVIEW_COPY_POLISH_IMPLEMENTATION` if copy-only | DOCX hygiene audit remains accessible. |
| Technical export info | `Technische informatie` under export | Already collapsed and secondary. | Removing weakens evidence of no semantic change. | B / D | Keep collapsed. No action in next WP. | none | Expander remains available. |
| Technical recognitions | `Technische herkenningen` at bottom | Technical and appears after main flow; label reinforces prototype feel. | Removing weakens audit/debug trace. | B / C / D | Rename to `Geavanceerde herkenningsdetails`; keep collapsed. | `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` | Recognition details remain collapsed and available. |
| Top-level app docstring/candidate language | Source code only, not visible UI | Not user-facing. | No UI risk. | D | Do not touch in UI package unless tests require. | none | No app verification needed. |

## 4. Sharp implementation scope for next package

The next implementation should be one small pass only.

Allowed changes in `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION`:

```text
1. Rename Serial review heading to Stap voor stap controleren.
2. Replace Serial review info text with short Dutch user-facing copy.
3. Remove or hide the serial governance caption from the primary UI.
4. Rename Serial review filter to Filter voor stap-voor-stap controle.
5. Rename Technische details bij de vervangtabel to Geavanceerde details bij de vervangtabel.
6. Rename Technische herkenningen to Geavanceerde herkenningsdetails.
7. Optionally rename Mogelijke gemiste waarden to Mogelijk extra te controleren waarden, while preserving expanded behavior when candidates exist.
```

Explicitly not allowed in the next implementation:

```text
Do not alter export/download section.
Do not alter Scrub Key behavior or labels except if tests require no change.
Do not alter replacement table data model.
Do not move review table out of the flow.
Do not add new benchmark, gate, status artifact, dashboard or safety system.
Do not add a new review panel.
Do not change recognizers or thresholds.
Do not touch Dockerfile.
```

## 5. Minimal verification checklist for next implementation

Use existing tests where possible. Add only small string/source tests if needed.

Recommended checks:

```text
python -m pytest -q tests/test_replace_logic_ui_patch.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests/test_export_download_ux_contracts.py tests/test_export_download_ux_implementation.py
python -m py_compile presidio_streamlit.py serial_review_panel_ui.py
```

If changes touch only `serial_review_panel_ui.py` and labels, a focused test run is enough before full-suite check if Actions later runs all tests.

App verification after implementation must confirm:

```text
No Script execution error.
Side-by-side review remains visible.
Replacement table remains available and collapsed.
Step-by-step review remains available but no longer says experimental.
Technical/guidance details remain collapsed and available.
Export section still shows 5. Exporteer resultaat.
```

## 6. Decision

Proceed to `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` as a small interface cleanup package.

Do not create more review/planning packages before implementation unless a concrete blocker is found.

This plan intentionally avoids the review-loop trap: it narrows the next action to a small UI cleanup diff with existing safety controls preserved.
