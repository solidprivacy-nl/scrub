from __future__ import annotations

from pathlib import Path


CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
IMPLEMENTATION_CLAIM = Path(
    "workpackage_claims/"
    "scrub_wp_manual_correction_panel_density_simplification_implementation.md"
)
CLOSEOUT_CLAIM = Path(
    "workpackage_claims/"
    "scrub_wp_manual_correction_panel_density_simplification_app_verify_closeout.md"
)
IMPLEMENTATION_HANDOVER = Path(
    "handover/workpackages/"
    "20260716_2040_manual_correction_panel_density_implementation.md"
)
CLOSEOUT_HANDOVER = Path(
    "handover/workpackages/"
    "20260716_2343_manual_correction_panel_density_app_verify_closeout.md"
)

STAMP = "2026-07-16 23:43 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT"

CHANGELOG_ENTRY = f'''## 2026-07-16 — {PACKAGE}

Status: completed and app-verified.

Purpose:

- Record live Hugging Face app verification after PR #28 merged.
- Close the manual correction panel density simplification line.
- Confirm the compact layout preserves the existing manual correction workflow.

Verification evidence:

- Coordinator live app screenshot reviewed at {STAMP}.
- `Gemiste waarde toevoegen` remains collapsed by default and opens without a duplicate internal heading.
- The value, type and replacement controls appear in one compact row.
- The full-width `Toevoegen aan vervangtabel` action remains visible.
- Synthetic value `lantaarnbloem` was added successfully.
- The replacement table shows `lantaarnbloem` with `[WAARDE_HANDMATIG_01]` and status `Handmatig toegevoegd`.
- No Script execution error is visible.
- The live screenshot confirms GitHub-to-Hugging-Face deployment of the merged UI.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Files added:

- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260716_2343_manual_correction_panel_density_app_verify_closeout.md`

Intentionally not changed:

- product code or tests;
- recognizer or replacement semantics;
- validation or session-state behavior;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, startup/runtime or dependencies.

Next recommended step:

- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

---

'''

WORKPACKAGES_ENTRY = f'''## {STAMP} — {PACKAGE}

Status: completed and app-verified.

Summary:
- Live Hugging Face app verification passed after PR #28 merge.
- The manual correction panel opens with one concise caption, a compact three-column input row and one full-width submit action.
- The duplicate internal heading is absent.
- Synthetic value `lantaarnbloem` was successfully added and is visible in the replacement table as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.
- The screenshot confirms the merged UI reached the Hugging Face Space and no Script execution error is visible.
- No product code or behavioral semantics changed in this docs-only closeout.

Validation:
- PR #28 final GitHub Actions test run passed before merge.
- Hugging Face sync confirmed by live deployed UI.
- App verification passed.

Related package status:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

Next recommended step:
- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

'''

CLOSEOUT_CLAIM_CONTENT = f'''# Workpackage claim — {PACKAGE}

Repository: solidprivacy-nl/scrub

Workpackage title: {PACKAGE}

Status: completed and app-verified

Claimed by: ChatGPT GitHub worker

Claimed at: {STAMP}

Completed at: {STAMP}

Branch: scrub-manual-correction-density-app-verify-closeout

Scope:
- Administrative closeout for live app verification of the compact manual correction panel.
- Docs-only update; no product code or tests changed.

Validation:
- PR #28 GitHub Actions passed before merge.
- Live Hugging Face screenshot confirms deployment.
- `lantaarnbloem` was added and appears in the replacement table as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.
- Compact input row, concise caption and full-width submit action are visible.
- No duplicate internal heading or Script execution error is visible.

Handover:
- `{CLOSEOUT_HANDOVER}`

Next recommended step:
- Use representative synthetic legal documents before approving another UI simplification package.
'''

CLOSEOUT_HANDOVER_CONTENT = f'''# Handover — {PACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{PACKAGE}

## Status

Completed and app-verified.

## Files added

- `{CLOSEOUT_CLAIM}`
- `{CLOSEOUT_HANDOVER}`

## Files changed

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `{IMPLEMENTATION_CLAIM}`
- `{IMPLEMENTATION_HANDOVER}`

## Tests

No new pytest run required for this docs-only closeout. PR #28 final GitHub Actions validation passed before merge.

## Validation status

Passed.

## GitHub Actions status

PR #28 final test run passed before merge.

## Hugging Face sync status

Passed; confirmed by the live deployed UI screenshot.

## App verification status

Passed at {STAMP}.

Confirmed:
- `Gemiste waarde toevoegen` opens without a duplicate internal heading.
- One concise caption is visible.
- Value, type and replacement controls are arranged in one compact row.
- The full-width submit action remains visible.
- Synthetic value `lantaarnbloem` was added successfully.
- The replacement table shows `lantaarnbloem` mapped to `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.
- No Script execution error is visible.

## Remaining risks

- This screenshot verifies the successful-add path and deployed layout. Broader document-level regression coverage remains provided by the existing automated suites.
- Further UI changes should remain separately scoped because review and replacement controls are safety-sensitive.

## Next recommended step

Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.
'''


def prepend_once(path: Path, marker: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(entry + text, encoding="utf-8")


def main() -> None:
    prepend_once(CHANGELOG, PACKAGE, CHANGELOG_ENTRY)
    prepend_once(WORKPACKAGES, PACKAGE, WORKPACKAGES_ENTRY)

    implementation_claim = IMPLEMENTATION_CLAIM.read_text(encoding="utf-8")
    implementation_claim = implementation_claim.replace(
        "Status: completed / ready for app verification",
        "Status: completed and app-verified",
        1,
    )
    if "App verification passed:" not in implementation_claim:
        implementation_claim += f'''\n\nApp verification passed:\n- Verified at: {STAMP}\n- Live Hugging Face screenshot confirms deployment.\n- Compact input row and full-width submit action are visible without a duplicate internal heading.\n- Synthetic value `lantaarnbloem` appears in the replacement table as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.\n- No Script execution error is visible.\n'''
    IMPLEMENTATION_CLAIM.write_text(implementation_claim, encoding="utf-8")

    implementation_handover = IMPLEMENTATION_HANDOVER.read_text(encoding="utf-8")
    implementation_handover = implementation_handover.replace(
        "Completed / ready for app verification.",
        "Completed and app-verified.",
        1,
    )
    implementation_handover = implementation_handover.replace(
        "## GitHub Actions status\n\nPending PR validation after implementation commit.",
        "## GitHub Actions status\n\nPR #28 final test run passed before merge.",
        1,
    )
    implementation_handover = implementation_handover.replace(
        "## Hugging Face sync status\n\nPending after merge.",
        "## Hugging Face sync status\n\nPassed; confirmed by the live deployed UI screenshot.",
        1,
    )
    implementation_handover = implementation_handover.replace(
        "## App verification status\n\nRequired after Actions and sync because visible UI behavior changed.",
        f"## App verification status\n\nPassed at {STAMP}.",
        1,
    )
    if "## App verification evidence" not in implementation_handover:
        implementation_handover += f'''\n\n## App verification evidence\n\n- Live Hugging Face screenshot reviewed at {STAMP}.\n- Compact value/type/replacement row is visible.\n- Duplicate internal heading is absent.\n- `lantaarnbloem` was added as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.\n- No Script execution error is visible.\n'''
    IMPLEMENTATION_HANDOVER.write_text(implementation_handover, encoding="utf-8")

    CLOSEOUT_CLAIM.write_text(CLOSEOUT_CLAIM_CONTENT, encoding="utf-8")
    CLOSEOUT_HANDOVER.write_text(CLOSEOUT_HANDOVER_CONTENT, encoding="utf-8")


if __name__ == "__main__":
    main()
