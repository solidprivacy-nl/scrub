from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Missing expected anchor in {path}: {old[:120]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend(path: str, addition: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    if addition.strip() in text:
        return
    file_path.write_text(addition.rstrip() + "\n\n" + text, encoding="utf-8")


replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — processed-text selection masking is live verified and display-only placeholder compaction is implemented without changing the 80-bit binding; deployment and app verification of the compact view gate the subsequent cross-flow regression.",
    "Last roadmap strategy update: 2026-08-05 — compact bound-placeholder display is deployed and live verified; direct user evidence confirms that local decluttering has not yet removed the long-form, form-like application structure, so a premium single-task app-shell line is now sequenced after the existing cross-flow safety regression.",
)

replace_once(
    "ROADMAP.md",
    """Important UX status:\n\n```text\nThe review table remains source of truth and fallback.\nThe old replacement decision helper panel must not return as normal user-facing UI.\nThe unified side-by-side review, manual missed-value entry and compact export flow form the verified MVP UI baseline.\nFurther UI work is not the default next line and requires a separately approved package tied to evidence from Phase 6 validation.\n```""",
    """Important UX status:\n\n```text\nThe review table remains source of truth and fallback.\nThe old replacement decision helper panel must not return as normal user-facing UI.\nThe unified side-by-side review, manual missed-value entry, compact placeholder display and grouped export flow form the verified functional baseline.\nDirect live-app evidence now confirms that this baseline still presents too much of the workflow as one long form.\nThe next approved UI direction is a global Standard/Expert presentation model and a one-active-stage document workspace, not another isolated expander-cleanup pass.\n```""",
)

replace_once(
    "ROADMAP.md",
    """- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`.\n\nUX principles:""",
    """- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`;\n- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`.\n\nUX principles:""",
)

premium_section = """
### Premium core-flow UI realignment

Direct coordinator/user evidence on 2026-08-05 establishes that the remaining interface problem is structural:

```text
The app still behaves visually as one long Streamlit form.
Input, settings, review, corrections, downloads, Scrub Key and audit controls compete on the same page.
```

The approved target is:

```text
Top-level workflow: Anonimiseren | Terugzetten
Global presentation: Standaard | Expert
One active stage: Toevoegen → Controleren → Downloaden
One primary action per active stage
Progressive and conditional disclosure for settings, other formats, Scrub Key and audit evidence
```

`Standaard` is lower cognitive load, not lower safety. `Expert` preserves full inspection, tuning, audit and troubleshooting. The current permanent settings sidebar is not part of the Standard target. Completed stages collapse into compact summaries rather than remaining open above the current task.

The implementation remains within Streamlit first, but must approximate a single-task application shell. It must not change recognizers, replacement decisions, export bytes, filenames, MIME types, Scrub Key semantics, reinsert behavior, audit evidence or the human-review requirement.

Sequential execution:

```text
0. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
1. SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT
2. SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL
3. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION
4. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
5. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
6. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
7. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
8. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

Do not combine the input, review and export restructuring into one patch. Do not run shared Streamlit UI packages in parallel.

"""
replace_once(
    "ROADMAP.md",
    "### Phase 6 — MVP workflow validation and trust hardening\n",
    premium_section + "### Phase 6 — MVP workflow validation and trust hardening\n",
)

replace_once(
    "ROADMAP.md",
    "- do not reopen broad UI work unless validation reveals a concrete usability or safety blocker;",
    "- direct live-app evidence on 2026-08-05 establishes a concrete usability blocker: the functional baseline remains a long, form-like page; reopen UI work only through the approved premium core-flow sequence;",
)

replace_once(
    "ROADMAP.md",
    """The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. The integration adds one normal bound manual row, reruns before exports, keeps the review table authoritative, retains the manual/static rollback path and changes no export/Scrub Key/reinsert semantics. GitHub-to-Hugging-Face synchronization and live app verification are green. App evidence also exposed placeholder readability noise from the repeated 80-bit binding segment. A narrow display-only compaction package is permitted before cross-flow regression; the binding grammar, entropy, export, Scrub Key and reinsert semantics remain frozen. This line remains sequential and does not displace the active Phase 6 queue.""",
    """The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. The integration adds one normal bound manual row, reruns before exports, keeps the review table authoritative, retains the manual/static rollback path and changes no export/Scrub Key/reinsert semantics. GitHub-to-Hugging-Face synchronization and live app verification are green. The display-only placeholder compaction is also deployed and app-verified without changing binding grammar, entropy, export, Scrub Key or reinsert semantics. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION` is now the final safety baseline before the premium core-flow UI contract line starts.""",
)

replace_once(
    "ROADMAP.md",
    """MVP architecture target:\n\n```text\nThin Streamlit UI, helper-driven behavior, tested safety boundaries, local-first direction, and clear export/audit workflow.\n```""",
    """MVP architecture target:\n\n```text\nThin helper-driven Streamlit application shell; one active document stage at a time; global Standard/Expert presentation; tested safety boundaries; local-first direction; and a clear primary export with secondary restore/audit layers.\n```""",
)

wp_entry = """## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Status: completed planning/design-only; implementation not started.

Goal:
- Reassess the current interface after direct live-app evidence and replace incremental form decluttering with a coherent premium single-task app-shell direction.

Decision result:
```text
Top-level workflows: Anonimiseren | Terugzetten
Global presentation: Standaard | Expert
Standard stages: Toevoegen → Controleren → Downloaden
Only one active stage expanded
One primary action per stage
No permanent configuration sidebar in Standard
One recommended document download; other formats, Scrub Key and audit remain secondary
```

Safety boundary:
- visibility and grouping only unless a later package explicitly freezes state behavior;
- no recognizer, replacement, export, Scrub Key, reinsert, audit, runtime or dependency semantic change;
- human review remains mandatory.

Execution gate:
```text
1. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
2. SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT
3. SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL
4. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION
5. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
6. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
7. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
8. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
9. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

Parallelization:
- do not run the shared Streamlit UI packages in parallel;
- contract and pure state helpers precede UI integration;
- input, review and export are separate sequential patches.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Evidence:
- PR #66 merged as `74b7a15ee74f6330f7fc37892b65246c1a61afaf`;
- final run #2080: 1155 tests passed in 12.44s;
- independent deployment run #2082: 4/4 runtime files exact, health `ok`, root HTTP 200, frontend tests passed, 1155 tests passed in 11.49s;
- coordinator/user confirmation: `Aanpassing is geslaagd. Ik zie nu inderdaad kortere vervangingscodes.`

Confirmed boundary:
- compact aliases are display-only;
- full 80-bit-bound tokens remain internal and in exports;
- export, Scrub Key and reinsert semantics remain unchanged.
"""
prepend("WORKPACKAGES.md", wp_entry)

changelog_entry = """## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Status: completed planning/design-only.

Purpose:
- Convert new live-app UX evidence into a structural interface strategy rather than another isolated decluttering patch.

Result:
- added `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- documented the gap between the implemented review-local Basic/Expert split and an application-wide presentation model;
- defined top-level Anonymize/Reinsert workflows;
- defined global Standard/Expert visibility and grouping;
- defined one-active-stage `Toevoegen → Controleren → Downloaden` behavior;
- defined no permanent settings sidebar in Standard;
- defined one recommended document download with other formats, Scrub Key and audit evidence secondary;
- sequenced contract, pure state model, app shell, input, review, export, Expert parity and app verification packages;
- added planning contract tests;
- changed no runtime product behavior.

Intentionally not changed:
- Streamlit product code;
- recognizers, profiles, replacement logic or review decisions;
- export payloads, filenames or MIME types;
- Scrub Key or reinsert semantics;
- runtime, dependencies or cloud-processing boundaries.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Validation:
- PR #66 merged as `74b7a15ee74f6330f7fc37892b65246c1a61afaf`;
- final run #2080: 1155 tests passed in 12.44s;
- deployment run #2082: 4/4 files exact, Space health `ok`, root HTTP 200, frontend tests passed and 1155 tests passed in 11.49s;
- coordinator/user confirmed shorter replacement codes are visible and working.

Intentionally not changed:
- full bound tokens in exports;
- 80-bit binding entropy;
- Scrub Key, reinsert or export semantics;
- human-review and production-readiness boundaries.
"""
prepend("CHANGELOG.md", changelog_entry)

decision_entry = """## 2026-08-05 — D041 — Move from review-local decluttering to an application-wide premium core-flow shell

Status: accepted product, UX and implementation-sequence decision

Decision:

```text
Adopt an application-wide Standard/Expert presentation model and a one-active-stage document workspace. Separate Anonymize and Reinsert as top-level workflows. In Standard, present Toevoegen → Controleren → Downloaden with one primary action per stage and progressive disclosure of settings, alternative formats, Scrub Key and audit evidence.
```

Reason:

- live app evidence confirms that earlier Basic/Expert and decluttering work improved individual sections but left the whole product as a long form;
- premium and enterprise credibility require a coherent task hierarchy, not merely fewer open expanders;
- input alternatives, profile settings, review machinery, normal downloads, restore material and audit evidence serve different user goals and should not have equal visual weight;
- one active stage at a time reduces cognitive load and makes the current task explicit.

Presentation boundary:

- recommended global labels are `Standaard` and `Expert`, subject to contract freeze;
- Standard has no permanent configuration sidebar;
- Expert preserves full inspection, tuning, audit and troubleshooting;
- switching presentation changes visibility and grouping only and must preserve input, replacement decisions and session state.

Safety boundary:

- human review remains mandatory;
- the review table remains source of truth and fallback;
- no silent profile or recognizer changes;
- no export-byte, filename, MIME, Scrub Key, reinsert or audit semantic changes;
- no cloud document processing, telemetry or browser persistence;
- an explicit processing action requires a pure stale-state and transition model before UI integration.

Approved sequence:

1. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`
2. `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`
3. `SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL`
4. `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION`
5. `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`
6. `SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION`
7. `SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION`
8. `SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION`
9. `SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT`

Evidence:

- coordinator/user feedback at 2026-08-05 10:49 Europe/Amsterdam;
- `BASIC_EXPERT_REVIEW_MODE_PLAN.md`;
- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`.

"""
prepend("DECISION_LOG.md", decision_entry)

replace_once(
    "RISK_REGISTER.md",
    """- The contract, action model and component spike are now connected through `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`. The review table remains source of truth; the component is only an input route into normal bound manual rows.\n\nGaps:""",
    """- The contract, action model and component spike are now connected through `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`. The review table remains source of truth; the component is only an input route into normal bound manual rows.\n- Live app evidence on 2026-08-05 confirms that local decluttering is not sufficient: the application still exposes input, settings, review, downloads, Scrub Key and audit as one long form. `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md` mitigates this through a global Standard/Expert model, top-level workflow navigation, one active stage and progressive disclosure.\n\nGaps:""",
)

replace_once(
    "workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
    "Status: completed; deployment synchronization and live app verification green",
)

replace_once(
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
    "Status: completed in GitHub; deployment synchronization and app verification pending",
    "Status: completed; deployment synchronization and live app verification green",
)
replace_once(
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
    "- Final exact-tree frontend and Python regression pending this governance-only finalization.",
    "- Finalization workflow: both frontend suites passed and 1155 tests passed in 10.73s.\n- Final standard merge-candidate run #2080: 1155 tests passed in 12.44s.\n- Independent deployment run #2082: 4/4 runtime files exact, health `ok`, root HTTP 200, frontend tests passed and 1155 tests passed in 11.49s.\n- Coordinator/user app verification confirmed shorter replacement codes are visible and working.",
)
replace_once(
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
    "Green through run #2076; final merge-candidate run pending.",
    "Green through final merge-candidate run #2080 and independent deployment run #2082.",
)
replace_once(
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
    "Pending merge.",
    "Green; 4/4 changed runtime files matched Hugging Face byte-for-byte in run #2082.",
)
replace_once(
    "handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md",
    "Pending. Required because the visible review representation and browser offset mapping changed.",
    "Confirmed by coordinator/user at 2026-08-05 10:49 Europe/Amsterdam.",
)

# Self-clean temporary operator files before committing the finalized tree.
(ROOT / ".github/workflows/finalize_premium_core_flow_ui_realignment.yml").unlink()
Path(__file__).unlink()
