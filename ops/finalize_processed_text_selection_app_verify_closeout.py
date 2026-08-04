from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-04 22:22 Europe/Amsterdam"


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


workpackage_section = f"""## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Goal:
- Record the coordinator/user confirmation that direct masking from `Verwerkte tekst` works in the deployed app.

Verification evidence:
```text
Integration PR: #63
Merge commit: 53fad202ae88a97b1ea476a9c3ba787932cd62ae
Final merge-candidate run: #2051 — 1146 passed in 11.59s
Independent deployment run: #2064
Runtime/component files exact on Hugging Face: 11/11
Space health: HTTP 200 / ok
Frontend component tests: passed
Post-deployment Python regression: 1146 passed in 11.47s
App verification: confirmed — "Het werkt."
```

Confirmed behavior:
- selection, safe inspection, type choice and exact-occurrence masking work;
- one normal `Handmatig uit tekst` row is created;
- one-step undo works;
- review table, manual fallback, export, Scrub Key and reinsert remain available;
- no Script execution error was reported.

New evidence finding:
- the repeated 80-bit document-binding segment makes bound placeholders visually long;
- shortening the underlying binding to four characters is not authorized because it would weaken wrong-key protection;
- next narrow package: `SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION`.

Boundaries:
- closeout-only; no product code or placeholder grammar changed;
- human review remains mandatory;
- no production-readiness claim.
"""
prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT",
    workpackage_section,
)

changelog_section = f"""## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Purpose:
- Close the processed-text selection integration after independent deployment checks and coordinator/user browser verification.

Validation:
- PR #63 merged as `53fad202ae88a97b1ea476a9c3ba787932cd62ae`;
- final merge-candidate run #2051: 1146 tests passed in 11.59s;
- independent deployment run #2064: 11/11 runtime/component files matched Hugging Face, Space health was `ok`, root returned HTTP 200, frontend tests passed, and 1146 Python tests passed in 11.47s;
- coordinator/user confirmed `Het werkt.` with a deployed-app screenshot.

Observed follow-up:
- bound placeholders remain safe but visually noisy because the same 80-bit binding ID is repeated;
- four-character binding IDs are rejected as an unsafe weakening;
- display-only compaction is routed to `SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION`.

Intentionally not changed:
- product code, placeholder grammar and binding entropy;
- export, Scrub Key, reinsert, recognizers, profiles or dependencies;
- production-readiness and human-review boundaries.
"""
prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT",
    changelog_section,
)

release_section = f"""## {TIMESTAMP} — Direct maskeren vanuit de verwerkte tekst geverifieerd

De nieuwe correctieroute is live gecontroleerd: een gemiste waarde kan direct in de verwerkte tekst worden geselecteerd, veilig worden geïnspecteerd, als type worden toegevoegd en daarna weer ongedaan worden gemaakt. De vervangtabel, handmatige invoer, downloads, Scrub Key en herstelroute blijven beschikbaar.

De lange documentbinding in placeholders blijft technisch intact. Een afzonderlijke verbetering gaat de weergave compacter maken zonder de beveiliging te verkorten.
"""
prepend_once(
    "RELEASE_NOTES.md",
    "Direct maskeren vanuit de verwerkte tekst geverifieerd",
    release_section,
)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — the all-exact contract, action model, local component and production review-table integration are complete; the active gate is GitHub-to-Hugging-Face synchronization and live app verification before cross-flow regression.",
    "Last roadmap strategy update: 2026-08-04 — processed-text selection masking is merged, synchronized and live-app verified; a narrow display-compaction package now addresses placeholder readability without changing the 80-bit document binding, before cross-flow regression continues.",
)
replace_once(
    "ROADMAP.md",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. The integration adds one normal bound manual row, reruns before exports, keeps the review table authoritative, retains the manual/static rollback path and changes no export/Scrub Key/reinsert semantics. The next gate is synchronization and live app verification; only then may the cross-flow regression package start. This line remains sequential and does not displace the active Phase 6 queue.",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. The integration adds one normal bound manual row, reruns before exports, keeps the review table authoritative, retains the manual/static rollback path and changes no export/Scrub Key/reinsert semantics. GitHub-to-Hugging-Face synchronization and live app verification are green. App evidence also exposed placeholder readability noise from the repeated 80-bit binding segment. A narrow display-only compaction package is permitted before cross-flow regression; the binding grammar, entropy, export, Scrub Key and reinsert semantics remain frozen. This line remains sequential and does not displace the active Phase 6 queue.",
)

replace_once(
    "RISK_REGISTER.md",
    "The static renderer and manual form remain fallbacks until deployment and live verification are green.",
    "The static renderer and manual form remain fallbacks. Deployment synchronization and live browser verification are green, including selection, exact-occurrence masking, normal table-row creation and one-step undo.",
)
replace_once(
    "RISK_REGISTER.md",
    "- Production table integration now preserves collision/replay/stale guards, hidden-marker protection, immediate rerun and edit-aware undo. The remaining high-risk gates are deployment synchronization, live browser/app verification and full export/Scrub Key/reinsert cross-flow regression.",
    "- Production table integration preserves collision/replay/stale guards, hidden-marker protection, immediate rerun and edit-aware undo. Deployment synchronization and live browser/app verification are green. The remaining high-risk gate is full export/Scrub Key/reinsert cross-flow regression. A narrow display-only placeholder compaction may proceed first because app evidence showed readability noise; the underlying 80-bit binding must not be shortened.",
)

replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
    "Status: completed, synchronized and live-app verified",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "- Hugging Face sync pending merge.\n- App verification pending merge and synchronization.",
    "- Independent deployment run #2064 matched 11/11 runtime/component files, returned Space health `ok` and HTTP 200, passed frontend tests, and passed 1146 Python tests in 11.47s.\n- Coordinator/user live app verification confirmed `Het werkt.` at 2026-08-04 22:22 Europe/Amsterdam.",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Pending.\n\n## App verification status\n\nPending. Required because this is a user-visible production review-flow change.",
    "Green through independent run #2064: 11/11 files exact, health `ok`, root HTTP 200.\n\n## App verification status\n\nConfirmed by the coordinator/user: selection masking and undo work in the deployed app; existing review/export/Scrub Key/reinsert surfaces remain present.",
)
replace_once(
    "handover/workpackages/20260804_0134_processed_text_selection_table_integration.md",
    "Merge after the final documentation-only PR run is green. Then verify GitHub-to-Hugging-Face synchronization and request focused live app verification before starting cross-flow regression.",
    "Implement the separately scoped display-only bound-placeholder compaction without changing binding entropy or export/Scrub Key/reinsert semantics, then continue with cross-flow regression.",
)

replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_app_verify_closeout.md",
    "Status: in_progress",
    "Status: completed",
)

handover = f"""# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Close out deployed processed-text selection app verification  
Status: completed

## Summary

Recorded independent deployment synchronization and the coordinator/user confirmation that direct masking from the processed-text pane works. The verification confirms the normal review-table route, exact-occurrence masking and one-step undo without changing export, Scrub Key or reinsert semantics.

The screenshot also exposed a concrete readability issue: the same 80-bit document-binding segment is repeated inside every placeholder. This is routed to a separate display-only compaction package. Reducing the actual binding to four characters is explicitly excluded because it would weaken wrong-key protection.

## Files added

- `workpackage_claims/scrub_wp_processed_text_selection_app_verify_closeout.md`
- `handover/workpackages/20260804_2222_processed_text_selection_app_verify_closeout.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

## Tests

- No product-code tests added; this is verification/closeout-only.
- Final repository regression is required on the closeout PR.

## Validation status

- Merge commit: `53fad202ae88a97b1ea476a9c3ba787932cd62ae`.
- Final merge-candidate run #2051: 1146 passed in 11.59s.
- Independent deployment run #2064: 11/11 files exact, health `ok`, root HTTP 200, frontend tests passed, 1146 Python tests passed in 11.47s.
- Coordinator/user app verification: confirmed — `Het werkt.`

## GitHub Actions status

Pending the closeout-only PR run.

## Hugging Face sync status

Green through independent run #2064.

## App verification status

Confirmed at {TIMESTAMP}.

## Remaining risks

- Full export/Scrub Key/reinsert cross-flow regression remains required.
- Long repeated binding segments reduce readability but do not indicate a binding defect.
- The actual 80-bit binding must remain intact unless a separately approved security architecture replaces it.

## Next recommended step

- `SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION`: compact only the review presentation, preserve the exact full tokens internally and in export/Scrub Key/reinsert, then run app verification before cross-flow regression.
"""
write(
    "handover/workpackages/20260804_2222_processed_text_selection_app_verify_closeout.md",
    handover,
)

# Self-clean after the closeout commit is prepared.
(ROOT / "ops/finalize_processed_text_selection_app_verify_closeout.py").unlink()
(ROOT / ".github/workflows/processed_text_selection_app_verify_closeout.yml").unlink()
