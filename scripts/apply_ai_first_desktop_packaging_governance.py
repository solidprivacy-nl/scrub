from pathlib import Path

root = Path(__file__).resolve().parents[1]
wp = "SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT"


def prepend(path: str, marker: str, block: str) -> None:
    target = root / path
    content = target.read_text(encoding="utf-8")
    if marker not in content:
        target.write_text(block.rstrip() + "\n\n" + content, encoding="utf-8")


def insert_after(path: str, anchor: str, marker: str, block: str) -> None:
    target = root / path
    content = target.read_text(encoding="utf-8")
    if marker in content:
        return
    if anchor not in content:
        raise RuntimeError(f"anchor missing in {path}")
    target.write_text(content.replace(anchor, anchor + "\n" + block.rstrip() + "\n", 1), encoding="utf-8")


prepend(
    "WORKPACKAGES.md",
    wp,
    """## 2026-08-03 14:47 Europe/Amsterdam — SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT

Status: completed; documentation/strategy alignment only.

Summary:
- Added an AI-first execution model for the final local Windows desktop/offline packaging phase.
- Preserved the existing gate: installer implementation remains deferred until Phase 6 quality closeout and explicit coordinator approval.
- Refined the eventual target to a signed Tauri shell, bundled PyInstaller onedir Python/Presidio sidecar, setup.exe and MSI.
- Recorded planning assumptions that 60–70% of first-cycle development/integration labor and 75–90% of later repetitive release work may be agent-executed.
- Kept publisher identity, signing, public release, security claims, real-user acceptance and safety-critical semantic changes under human control.
- Added no product code, installer, runtime, dependency or UI change.

Next recommended step:
- Continue the active Phase 6 queue. Open the Phase 9 desktop distribution contract only after quality-gate closeout and explicit approval.""",
)

prepend(
    "CHANGELOG.md",
    wp,
    """## 2026-08-03 14:47 Europe/Amsterdam — SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT

Status: completed; roadmap/decision documentation only.

Purpose:
- Incorporate an AI-first cost and authority model into the final local EXE/MSI roadmap while preserving security and release accountability.

Files added:
- `AI_FIRST_DESKTOP_PACKAGING_EXECUTION_MODEL.md`
- `handover/workpackages/20260803_1447_ai_first_desktop_packaging_roadmap_alignment.md`
- `workpackage_claims/scrub_wp_ai_first_desktop_packaging_roadmap_alignment.md`

Files changed:
- `ROADMAP.md`
- `DESKTOP_PACKAGING_DECISION.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:
- Phase 9 target refined to signed setup.exe/MSI distribution around a Tauri shell and bundled PyInstaller onedir local engine.
- AI-agent planning assumption recorded: 60–70% first-cycle labor substitution and 75–90% later repetitive release automation.
- Indicative post-agent development/integration budget recorded as EUR 8,000–24,000, excluding retained independent security review and authority costs.
- Human gates retained for signing, release, security claims, UX acceptance and safety-critical semantics.

Validation:
- Documentation markers and phase gates checked by the branch governance operator.
- No product tests required because no product code or runtime changed.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally relevant.
- App verification: not applicable.

Intentionally not changed:
- active Phase 6 execution order;
- installer implementation authorization;
- runtime, UI, dependencies, recognizers, export, Scrub Key or reinsert behavior;
- cloud processing or telemetry behavior.""",
)

prepend(
    "DECISION_LOG.md",
    "## 2026-08-03 — D038",
    """## 2026-08-03 — D038 — Use AI-first execution with human-controlled signing, security and release gates for Phase 9 desktop packaging

Status: accepted roadmap and execution-model decision; implementation remains gated

Decision:

```text
When the final local desktop/offline installer phase is explicitly opened, use scoped AI agents for deterministic packaging, CI, synthetic testing and release-candidate preparation. Target a signed Tauri Windows shell with a bundled PyInstaller onedir Python/Presidio sidecar, a low-friction setup.exe and a managed-deployment MSI. Retain human control over publisher identity, production signing, public release, security claims, real-user acceptance and safety-critical semantic changes.
```

Planning assumptions:
- 60–70% of first-cycle development/integration labor may be agent-executed;
- 75–90% of repetitive later release work may be automated;
- post-agent development/integration planning range: approximately EUR 8,000–24,000;
- independent security review, test hardware, signing and human release oversight remain retained costs.

Boundaries:
- Phase 9 remains gated by Phase 6 quality closeout and explicit coordinator approval.
- No installer, runtime, UI, dependency, export, Scrub Key, reinsert or cloud behavior changes in this decision package.
- Synthetic data only.
- No single agent receives unrestricted repository-write, signing-identity and public-release authority.
- Successful packaging alone does not justify a production-readiness or local-only security claim.""",
)

insert_after(
    "DESKTOP_PACKAGING_DECISION.md",
    "Repository: `solidprivacy-nl/scrub`\n",
    "## 1A. AI-first execution refinement — 2026-08-03",
    """## 1A. AI-first execution refinement — 2026-08-03

The phase-order decision remains unchanged: installer work stays at the end of the roadmap and requires explicit approval. When that line opens, the intended end-user target is refined to:

```text
signed Tauri Windows shell
+ bundled PyInstaller onedir Python/Presidio sidecar
+ one setup.exe for low-friction installation
+ one MSI for managed deployment
+ local/offline model assets
+ loopback-only same-PC communication
```

The portable Python folder remains an internal technical validation route rather than the premium end-user product.

Implementation should be AI-first for deterministic build, packaging, CI and evidence work. Approximately 60–70% of first-cycle development/integration labor and 75–90% of later repetitive release work may be agent-executed. Human authority remains mandatory for publisher identity, signing approval, public release, security claims, real Windows UX acceptance and changes to safety-critical product semantics.

No single agent may hold unrestricted repository-write, signing and public-release authority at the same time. This refinement changes no current runtime, product behavior or active phase gate.""",
)

for path, marker in [
    ("WORKPACKAGES.md", wp),
    ("CHANGELOG.md", wp),
    ("DECISION_LOG.md", "## 2026-08-03 — D038"),
    ("DESKTOP_PACKAGING_DECISION.md", "## 1A. AI-first execution refinement — 2026-08-03"),
]:
    if marker not in (root / path).read_text(encoding="utf-8"):
        raise RuntimeError(f"validation failed for {path}")

print("governance alignment applied")
