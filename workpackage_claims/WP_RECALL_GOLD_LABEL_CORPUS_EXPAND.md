status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_GOLD_LABEL_CORPUS_EXPAND
started timestamp: 2026-06-17 09:06 Europe/Amsterdam
completed timestamp: 2026-06-17 09:06 Europe/Amsterdam
scope: benchmark/data/documentation-only gold-label corpus expansion
boundaries: no product-code, no recognizer, no pattern, no UI, no export, no Scrub Key, no reinsert changes

final commit SHA or PR link: ddd7cfb14fe4972462b38a83328a488391bcd621
handover path: handover/workpackages/20260617_0906_recall_gold_label_corpus_expand.md

files added:
- corpus/legal/legal_false_positive_traps_seed_001.txt
- corpus/legal/legal_false_positive_traps_seed_001.gold.json
- corpus/legal/legal_mixed_identifiers_seed_001.txt
- corpus/legal/legal_mixed_identifiers_seed_001.gold.json
- corpus/care/care_role_preservation_seed_001.txt
- corpus/care/care_role_preservation_seed_001.gold.json
- corpus/care/care_mixed_identifiers_seed_001.txt
- corpus/care/care_mixed_identifiers_seed_001.gold.json
- workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_EXPAND.md
- handover/workpackages/20260617_0906_recall_gold_label_corpus_expand.md

files changed:
- corpus/README.md
- tests/test_recall_gold_label_corpus_seed.py
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_EXPAND.md

product-code changes: none

tests/checks:
- Local tests were not runnable because no local GitHub working tree is available in this environment.
- Python-assisted offset generation was used before committing new sidecars.
- Updated tests/test_recall_gold_label_corpus_seed.py for expanded sidecar/schema/offset validation.
- GitHub Actions should be used as final execution proof.

GitHub Actions status: unknown through connector at closeout time.
Hugging Face sync status: unknown through connector at closeout time.
app verification status: not required; benchmark/data/documentation-only and no app behavior changed.

corpus summary:
- Added legal false-positive trap source and sidecar.
- Added legal mixed identifiers source and sidecar.
- Added care role-preservation source and sidecar.
- Added care mixed identifiers source and sidecar.
- Corpus now has 4 legal source documents and 3 care source documents with gold sidecars.

remaining gaps:
- No benchmark runner exists yet.
- No formal recall/precision thresholds.
- No production-blocking benchmark gate.
- Corpus coverage is improved but not exhaustive.

remaining risks:
- Quantitative recall/precision remains unavailable until a runner compares predictions with sidecars.
- More synthetic legal/care documents may still be needed before broad trust claims.

next recommended step: do not automatically start another pattern-fix round. Consider WP_RECALL_BENCHMARK_RUNNER_MINIMAL or WP_DOCX_HYGIENE_RECALL_FOLLOWUP only after separate coordinator approval.
