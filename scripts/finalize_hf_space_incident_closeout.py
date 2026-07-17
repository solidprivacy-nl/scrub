from __future__ import annotations

from pathlib import Path


CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
SELF = Path(__file__)

CHANGELOG_MARKER = (
    "## 2026-07-17 — Hugging Face Space runtime incident recovery and sync-churn guard"
)
CHANGELOG_ENTRY = '''## 2026-07-17 — Hugging Face Space runtime incident recovery and sync-churn guard

Status: completed and app-verified.

Purpose:

- Restore the Hugging Face Space after it entered an error/rebuild state.
- Diagnose the incident without exposing secrets or changing product behavior.
- Prevent clearly non-runtime-only commits from repeatedly rebuilding the live Space.

Result:

- Sanitized runtime evidence observed the Space first at `BUILDING` and subsequently at `RUNNING`.
- Streamlit started on port 7860 and the Flair model loaded.
- The coordinator confirmed that the application opens again.
- PR #35 added a conservative deployment `paths-ignore` guard while preserving runtime-relevant deployments and manual dispatch.
- Temporary incident recovery/probe workflows and triggers were removed after verification.

Intentionally not changed:

- product code or UI;
- recognizers, thresholds or replacement semantics;
- export, Scrub Key or reinsert semantics;
- dependencies, Dockerfile, hardware or Hugging Face configuration;
- privacy and human-review controls.

Next recommended step:

- Resume PR #33 and the Phase 6 document-fidelity sequence.

---

'''

WORKPACKAGES_MARKER = (
    "## 2026-07-17 11:45 Europe/Amsterdam — HF Space runtime incident closeout"
)
WORKPACKAGES_ENTRY = '''## 2026-07-17 11:45 Europe/Amsterdam — HF Space runtime incident closeout

Status: completed and app-verified.

Summary:
- Restored the Hugging Face Space and confirmed runtime stage `RUNNING`.
- Coordinator confirmed that the application opens again.
- Merged a conservative sync-churn guard so clearly non-runtime-only commits no longer rebuild the Space.
- Removed temporary recovery and probe workflows/triggers.
- No product behavior or privacy controls changed.

Active next package:
- Resume `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING` in PR #33.

'''


def prepend_once(path: Path, marker: str, entry: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker not in current:
        path.write_text(entry + current, encoding="utf-8")


def main() -> None:
    prepend_once(CHANGELOG, CHANGELOG_MARKER, CHANGELOG_ENTRY)
    prepend_once(WORKPACKAGES, WORKPACKAGES_MARKER, WORKPACKAGES_ENTRY)
    SELF.unlink()


if __name__ == "__main__":
    main()
