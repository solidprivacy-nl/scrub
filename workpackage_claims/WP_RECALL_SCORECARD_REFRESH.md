status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_SCORECARD_REFRESH — Refresh recall/precision scorecard after Dutch legal recall fixes
started timestamp: 2026-06-17 01:12 Europe/Amsterdam
completed timestamp: 2026-06-17 01:12 Europe/Amsterdam
scope: benchmark/documentation-only recall scorecard refresh
boundaries: no product-code, no recognizer, no UI, no export, no Scrub Key, no reinsert changes

final commit SHA or PR link: c049792476de119a2d1439e8444499adf671defa
handover path: handover/workpackages/20260617_0112_recall_scorecard_refresh.md

files added:
- RECALL_PRECISION_SCORECARD.md
- workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md
- handover/workpackages/20260617_0112_recall_scorecard_refresh.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_SCORECARD_REFRESH.md

product-code changes: none

tests/checks:
- Local tests were not runnable because the container cannot clone/access GitHub for a local working tree.
- Static GitHub connector checks completed for required control files, benchmark spec, baseline tests, candidate scanner, risks, release notes, decisions, claims and handovers.
- RECALL_PRECISION_SCORECARD.md was not present at repo root before this package and was added.
- GitHub Actions should be used as final execution proof for documentation commits.

GitHub Actions status: unknown through connector at closeout time.
Hugging Face sync status: unknown through connector at closeout time.
app verification status: not required; benchmark/documentation-only and no app behavior changed.

scorecard summary:
- Dutch legal recall status refreshed after gap tests, pattern fixes and verify closeout.
- Legal reference coverage table added for documented samples.
- CLM/phone-number risk reduction recorded.
- Role-word and over-masking protection recorded.
- Review/export regression boundaries recorded.
- No immediate Round2 recommended unless concrete new gaps appear.

remaining gaps:
- No complete gold-label corpus sidecars.
- No formal recall/precision thresholds.
- No production-blocking benchmark gate.
- Helper-level candidate surfacing is not automatic recognition.
- DOCX metadata/comments/tracked changes remain a separate risk.

remaining risks:
- Future app/user testing may reveal new Dutch legal reference variants.
- Role/name combinations such as arts Jansen need broader benchmark coverage.
- Quantitative scorecard remains future work until gold labels and a runner exist.

next recommended step: do not automatically start another pattern-fix round. Consider WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2 only after concrete new misses and separate coordinator approval. Alternative approved options: benchmark/gold-label corpus package or WP_DOCX_HYGIENE_RECALL_FOLLOWUP.
