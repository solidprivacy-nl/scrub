from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-04 23:15 Europe/Amsterdam"
WP = "SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        raise RuntimeError(f"Required anchor missing in {path}: {old!r}")
    write(path, text.replace(old, new, 1))


def prepend_once(path: str, marker: str, section: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, section.rstrip() + "\n\n" + text)


workpackages = f"""## {TIMESTAMP} — {WP}

Status: completed in GitHub; deployment synchronization and live app verification pending.

Goal:
- Make document-bound placeholders easier to scan in the review UI without shortening or changing their security binding.

Implementation result:
```text
Full source/internal placeholder changed: false
Binding grammar changed: false
Binding entropy changed: false
Exported placeholder changed: false
Scrub Key mapping changed: false
Reinsert token changed: false
Automatic review alias: [LABEL_INDEX]
Manual review alias: [LABEL_H_INDEX]
Static fallback parity: implemented
Interactive UTF-16 source mapping: implemented
Compact placeholders protected with markers hidden: implemented
Legacy/malformed/free replacement text compacted: false
```

Examples:
```text
[LOCATIE_BSK732WYQ424ZIEQ6_02]          -> visible [LOCATIE_02]
[EMAIL_BSK732WYQ424ZIEQ6_HANDMATIG_03] -> visible [EMAIL_H_03]
```

Files added:
- `BOUND_PLACEHOLDER_DISPLAY_COMPACTION.md`
- `bound_placeholder_display.py`
- `tests/test_bound_placeholder_display.py`
- `tests/test_bound_placeholder_display_ui_integration.py`
- `tests/frontend/bound_placeholder_display.test.js`
- `workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md`
- `handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md`

Files changed:
- `frontend/processed_text_selection_component/component_core.js`
- `frontend/processed_text_selection_component/component.js`
- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Validation:
- dedicated frontend display contracts passed;
- existing frontend component contracts passed;
- standard PR run #2076: 1155 Python tests passed in 11.62s;
- final merge-candidate frontend and Python regression required after governance finalization.

Next gate:
- merge after the exact finalized tree is green;
- verify GitHub-to-Hugging-Face byte equality and Space health;
- request focused app verification of compact review aliases, offset-safe direct selection, full-token exports and reinsert;
- then continue `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`.
"""
prepend_once("WORKPACKAGES.md", WP, workpackages)

changelog = f"""## {TIMESTAMP} — {WP}

Status: completed in GitHub; deployment and app verification pending.

Purpose:
- Reduce placeholder noise in the review panes without weakening document binding or changing roundtrip semantics.

Implementation:
- added a strict display-only parser for schema-1.1 automatic and manual bound placeholders;
- automatic tokens display as `[LABEL_INDEX]` and manual tokens as `[LABEL_H_INDEX]`;
- retained full source tokens and exact UTF-16 source offsets behind every compact segment;
- mapped browser selection positions back to the unchanged source text;
- treated compact placeholders as protected spans even when visual yellow markers are hidden;
- applied the same compact rendering to the static fallback;
- kept malformed, legacy and free replacement values unchanged;
- exposed the full token only as non-mutating hover/accessibility metadata.

Validation:
- new Python and frontend contracts cover strict aliasing, lossless source reconstruction, UTF-16 offsets, hidden-marker protection and static fallback escaping;
- existing frontend component tests passed;
- standard PR run #2076: 1155 tests passed in 11.62s;
- final exact-tree validation follows this governance update.

Intentionally not changed:
- the 80-bit binding ID, placeholder grammar or mapping digest;
- processed document text, replacement-table values or component payload hashes;
- exports, filenames, MIME, Scrub Key schema/lifecycle or reinsert;
- recognizers, profiles, thresholds, dependencies, telemetry, network or cloud processing.
"""
prepend_once("CHANGELOG.md", WP, changelog)

release = f"""## {TIMESTAMP} — Kortere placeholders in de controleweergave

- Lange documentgebonden placeholders worden in de controleweergave compacter getoond. Zo wordt bijvoorbeeld `[LOCATIE_BSK732WYQ424ZIEQ6_02]` zichtbaar als `[LOCATIE_02]`.
- Handmatig toegevoegde waarden krijgen in de weergave een korte `H`, bijvoorbeeld `[EMAIL_H_03]`.
- Dit is uitsluitend een leesbaarheidsverbetering: de volledige beveiligde placeholder blijft intern en in gedownloade documenten intact.
- Scrub Key, documentbinding, controlewaarde en originele waarden terugzetten zijn niet gewijzigd.
- Vrij aangepaste vervangtekst en oudere of afwijkende placeholders worden niet stilzwijgend herschreven.
- Direct selecteren van een gemiste waarde blijft op de volledige onderliggende tekst werken, ook na een compact weergegeven placeholder.
- Menselijke controle blijft noodzakelijk.
"""
prepend_once("RELEASE_NOTES.md", "Kortere placeholders in de controleweergave", release)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — processed-text selection masking is merged, synchronized and live-app verified; a narrow display-compaction package now addresses placeholder readability without changing the 80-bit document binding, before cross-flow regression continues.",
    "Last roadmap strategy update: 2026-08-04 — processed-text selection masking is live verified and display-only placeholder compaction is implemented without changing the 80-bit binding; deployment and app verification of the compact view gate the subsequent cross-flow regression.",
)

replace_once(
    "RISK_REGISTER.md",
    "Signatures/HMAC remain deferred until protected local signing-key management exists.",
    "Signatures/HMAC remain deferred until protected local signing-key management exists. Display-only placeholder compaction does not shorten the binding ID, alter the mapping digest or change any key/export/reinsert token; full-token roundtrip verification remains required after deployment.",
)
replace_once(
    "RISK_REGISTER.md",
    "- Production table integration preserves collision/replay/stale guards, hidden-marker protection, immediate rerun and edit-aware undo. Deployment synchronization and live browser/app verification are green. The remaining high-risk gate is full export/Scrub Key/reinsert cross-flow regression. A narrow display-only placeholder compaction may proceed first because app evidence showed readability noise; the underlying 80-bit binding must not be shortened.",
    "- Production table integration preserves collision/replay/stale guards, hidden-marker protection, immediate rerun and edit-aware undo. Deployment synchronization and live browser/app verification are green. Display-only placeholder compaction is implemented with lossless source tokens, exact UTF-16 mapping and protected compact spans; the underlying 80-bit binding remains unchanged. Focused deployment/app verification of the compact view is required before the remaining high-risk export/Scrub Key/reinsert cross-flow regression.",
)

replace_once(
    "workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md",
    "Status: in_progress",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
)

handover = f"""# Handover — {WP}

Repository worked in: `solidprivacy-nl/scrub`
Workpackage title: Compact document-bound placeholders in review display
Status: completed in GitHub; deployment synchronization and app verification pending

## Summary

Implemented a display-only compaction layer for strict schema-1.1 bound placeholders. The review UI now presents short aliases while retaining the complete source token, 80-bit document binding and exact UTF-16 offsets. Automatic placeholders display as `[LABEL_INDEX]`; manual selection placeholders display as `[LABEL_H_INDEX]`.

The interactive component renders source-backed segments and maps browser selections back to the unchanged processed text. Compact placeholders remain protected even with visual markers hidden. The static fallback uses the same strict, escaped display contract. Legacy, malformed and free replacement text remain unchanged.

## Files added

- `BOUND_PLACEHOLDER_DISPLAY_COMPACTION.md`
- `bound_placeholder_display.py`
- `tests/test_bound_placeholder_display.py`
- `tests/test_bound_placeholder_display_ui_integration.py`
- `tests/frontend/bound_placeholder_display.test.js`
- `workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md`
- `handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md`

## Files changed

- `frontend/processed_text_selection_component/component_core.js`
- `frontend/processed_text_selection_component/component.js`
- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

## Tests

New and updated tests cover:

- strict automatic and manual compact aliases;
- no rewrite of legacy, malformed or free values;
- complete source reconstruction from display segments;
- exact UTF-16 source offsets, including text after compact tokens;
- selection mapping within and after compact tokens;
- protected placeholder spans when visual markers are hidden;
- complete source token and hash retained in component arguments;
- escaped static fallback parity and full-token hover/accessibility metadata;
- explicit no-change declarations for binding entropy and key semantics.

## Validation status

- Dedicated frontend display tests passed.
- Existing processed-text component frontend tests passed.
- Standard PR run #2076: 1155 Python tests passed in 11.62s.
- Final exact-tree frontend and Python regression pending this governance-only finalization.

## GitHub Actions status

Green through run #2076; final merge-candidate run pending.

## Hugging Face sync status

Pending merge.

## App verification status

Pending. Required because the visible review representation and browser offset mapping changed.

## Remaining risks

- Live browser behavior must confirm compact aliases render consistently and direct selection after them still targets the correct full source offsets.
- Downloaded scrubbed documents must be checked to contain full bound tokens rather than compact aliases.
- Scrub Key validation and reinsert must be checked against those full exported tokens.
- The full token is available in hover/accessibility metadata; this is non-sensitive but should not create visual clutter.
- Cross-browser Edge, Chrome and Firefox behavior remains part of later broader validation.
- Human review remains mandatory; no production-readiness claim is made.

## Next recommended step

Merge only after the finalized frontend and Python regressions are green. Then verify GitHub-to-Hugging-Face synchronization and perform focused app verification of compact aliases, marker-off behavior, direct selection after a compact token, full-token export and successful reinsert. Continue cross-flow regression only after that gate is green.
"""
write("handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md", handover)

# Normalize markdown trailing whitespace in files touched by this finalizer.
for relative in (
    "ROADMAP.md",
    "WORKPACKAGES.md",
    "CHANGELOG.md",
    "RELEASE_NOTES.md",
    "RISK_REGISTER.md",
    "workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md",
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
):
    path = ROOT / relative
    normalized = "\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()) + "\n"
    path.write_text(normalized, encoding="utf-8")

(ROOT / "ops/finalize_bound_placeholder_display_compaction.py").unlink()
(ROOT / ".github/workflows/finalize_bound_placeholder_display_compaction.yml").unlink()
