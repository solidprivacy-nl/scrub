# Handover — WP_RECALL_GOLD_LABEL_CORPUS_SEED

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_GOLD_LABEL_CORPUS_SEED — Add synthetic gold-label corpus seed for recall/precision benchmarking`

Status: completed as benchmark/data/documentation-only.

## Summary

Added a first small synthetic gold-label corpus seed for future recall/precision benchmarking. The package adds plain-text synthetic source files, `.gold.json` sidecars with exact offsets, corpus documentation and a tests-only validator for sidecar integrity.

No product code, recognizer code, pattern code, UI, export/download, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup or dependency behavior was changed.

## Files added

- `corpus/README.md`
- `corpus/legal/legal_reference_seed_001.txt`
- `corpus/legal/legal_reference_seed_001.gold.json`
- `corpus/legal/legal_role_preservation_seed_001.txt`
- `corpus/legal/legal_role_preservation_seed_001.gold.json`
- `corpus/care/care_reference_seed_001.txt`
- `corpus/care/care_reference_seed_001.gold.json`
- `tests/test_recall_gold_label_corpus_seed.py`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md`
- `handover/workpackages/20260617_0816_recall_gold_label_corpus_seed.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_SEED.md` pending final closeout update after this handover file

## Product-code changes

None.

## Corpus summary

Added three synthetic source documents:

1. `legal_reference_seed_001.txt`
   - Dutch legal reference sample with case/reference/client/dossier/claim/ECLI/person/phone/email/address values.
   - Includes traps for `7:669 BW` and `EUR 250,00`.

2. `legal_role_preservation_seed_001.txt`
   - Legal role-word preservation sample.
   - Includes standalone role words and role/name combinations such as `arts Jansen`, `getuige Fatima El Amrani` and `de minderjarige Sami El Amrani`.

3. `care_reference_seed_001.txt`
   - Care reference sample with client/care dossier/incident/room/department/BIG/person/phone/email values.
   - Includes preserve terms such as `cliënt`, `arts`, `zorgmedewerker` and `verpleegkundige`.

## Sidecar/schema summary

Each `.gold.json` sidecar includes:

- `document_id`
- `domain`
- `document_type`
- `language`
- `source_file`
- `synthetic: true`
- `labels`
- `preserve_terms`
- `known_traps`

Gold label offsets are zero-based and end-exclusive. During construction, offsets were generated and checked so that:

```text
source_text[start:end] == label.text
source_text[start:end] == preserve_terms.term
```

## Tests/checks run

Required local commands:

```text
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

Result: not runnable locally in this environment because no local GitHub working tree is available for pytest/py_compile execution.

Static/generation checks completed:

- Confirmed no prior `WP_RECALL_GOLD_LABEL_CORPUS_SEED` claim existed before starting.
- Read required control files and relevant recall/scorecard/risk/decision/claim/handover files.
- GitHub code search for broad corpus/benchmark terms returned no useful existing corpus location, so `corpus/` was used as instructed.
- Python-assisted offset generation was used before committing the sidecars.
- Added tests-only validator `tests/test_recall_gold_label_corpus_seed.py` to check JSON validity, source existence, offsets, required label fields, preserve-term offsets and `.example.test` email domains.

## GitHub Actions status

Unknown at handover time. Connector status visibility for direct-push commits has been incomplete in this repo.

## Hugging Face sync status

Unknown at handover time. This package is benchmark/data/documentation-only.

## App verification status

Not required. No app behavior changed.

## Updated risks

Updated `RISK_REGISTER.md` for:

- false negatives / missed sensitive data;
- Dutch legal reference under-detection;
- role-word over-masking;
- corpus/threshold gap.

The gold-label seed reduces the measurability gap but does not close the recall/precision risk because no runner or thresholds exist yet.

## Remaining gaps

- The corpus seed is intentionally small.
- No benchmark runner exists yet.
- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Broader legal/care corpus coverage is still needed.

## Remaining risks

- Quantitative recall/precision remains unavailable until a runner compares analyzer/helper output with the sidecars.
- More synthetic legal/care documents are needed before broad trust claims.
- No product claim such as `alle juridische nummers worden altijd herkend` is supported.

## Next recommended step

Do not automatically start a pattern-fix round.

Likely next options after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_RUNNER_MINIMAL
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
