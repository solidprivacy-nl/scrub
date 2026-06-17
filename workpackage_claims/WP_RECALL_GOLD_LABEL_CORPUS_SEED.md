status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_GOLD_LABEL_CORPUS_SEED — Add synthetic gold-label corpus seed for recall/precision benchmarking
started timestamp: 2026-06-17 08:16 Europe/Amsterdam
completed timestamp: 2026-06-17 08:16 Europe/Amsterdam
scope: benchmark/data/documentation-only gold-label corpus seed
boundaries: no product-code, no recognizer, no pattern, no UI, no export, no Scrub Key, no reinsert changes

final commit SHA or PR link: f1d724f98635b2b7339fbd93cbb690190cf8371e
handover path: handover/workpackages/20260617_0816_recall_gold_label_corpus_seed.md

files added:
- corpus/README.md
- corpus/legal/legal_reference_seed_001.txt
- corpus/legal/legal_reference_seed_001.gold.json
- corpus/legal/legal_role_preservation_seed_001.txt
- corpus/legal/legal_role_preservation_seed_001.gold.json
- corpus/care/care_reference_seed_001.txt
- corpus/care/care_reference_seed_001.gold.json
- tests/test_recall_gold_label_corpus_seed.py
- workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md
- handover/workpackages/20260617_0816_recall_gold_label_corpus_seed.md

files changed:
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md

product-code changes: none

tests/checks:
- Local tests were not runnable because no local GitHub working tree is available in this environment.
- Python-assisted offset generation was used before committing sidecars.
- Added tests/test_recall_gold_label_corpus_seed.py for sidecar/schema/offset validation.
- GitHub Actions should be used as final execution proof.

GitHub Actions status: unknown through connector at closeout time.
Hugging Face sync status: unknown through connector at closeout time.
app verification status: not required; benchmark/data/documentation-only and no app behavior changed.

corpus summary:
- Legal reference seed text and gold sidecar.
- Legal role preservation seed text and gold sidecar.
- Care reference seed text and gold sidecar.
- Corpus README and sidecar-integrity test added.

remaining gaps:
- No benchmark runner exists yet.
- Corpus seed is intentionally small.
- No formal recall/precision thresholds.
- No production-blocking benchmark gate.

remaining risks:
- Quantitative recall/precision remains unavailable until a runner compares predictions with sidecars.
- More synthetic legal/care documents are needed before broad trust claims.
- No product claim that all legal numbers are always detected is supported.

next recommended step: do not automatically start another pattern-fix round. Consider WP_RECALL_BENCHMARK_RUNNER_MINIMAL, WP_RECALL_GOLD_LABEL_CORPUS_EXPAND or WP_DOCX_HYGIENE_RECALL_FOLLOWUP only after separate coordinator approval.
