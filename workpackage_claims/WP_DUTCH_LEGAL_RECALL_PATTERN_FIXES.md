status: completed
repository: solidprivacy-nl/scrub
started: 2026-06-16 22:11 Europe/Amsterdam
completed: 2026-06-16 22:11 Europe/Amsterdam
scope: targeted Dutch legal reference candidate improvements
boundaries: no UI, export, reinsert, startup, Docker or dependency changes

final commit SHA or PR link: 63340d6938b578ad645ccf9be48610308845d832
handover path: handover/workpackages/20260616_2211_dutch_legal_recall_pattern_fixes.md

files added:
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.md
- handover/workpackages/20260616_2211_dutch_legal_recall_pattern_fixes.md

files changed:
- candidate_scanner.py
- tests/test_dutch_legal_recall_gap_baseline.py
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- RELEASE_NOTES.md
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.md

tests/checks:
- Local py_compile/pytest attempted, but not runnable because container cannot resolve github.com for local clone.
- Baseline tests were converted from xfail to direct helper-level assertions.
- GitHub Actions should be used as final execution proof.

improved cases:
- Case-number-shaped values with spaces are now surfaced by candidate scanner near Dutch legal/admin context.
- Context cues added for rolnummer, rolnr, client, cliënt, camera, incident and reparatie.
- Role-word preservation remains covered by normal baseline assertions.

remaining risks:
- Full automatic recognizer classification is not proven for all Dutch legal references.
- CI/HF verification remains required.
- Broader benchmark thresholds and gold sidecars remain future work.

GitHub Actions status: unknown through connector at closeout time.
Hugging Face sync status: unknown through connector at closeout time.
app verification status: not required; no UI behavior changed.

next recommended step: do not automatically continue. Suggested next package after separate approval is WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.
