# Handover — WP_RECALL_GOLD_LABEL_CORPUS_EXPAND

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — Expand synthetic gold-label corpus for recall/precision benchmarking`

Status: completed as benchmark/data/documentation-only.

## Summary

Expanded the synthetic gold-label corpus for future recall/precision benchmarking. Added four new synthetic source documents and four `.gold.json` sidecars, updated the corpus README, extended the tests-only sidecar validator, and refreshed scorecard/risk/workpackage documentation.

No product code, recognizer code, pattern code, UI, export/download, Scrub Key, reinsert, DOCX/PDF flow, Docker/startup or dependency behavior was changed.

## Files added

- `corpus/legal/legal_false_positive_traps_seed_001.txt`
- `corpus/legal/legal_false_positive_traps_seed_001.gold.json`
- `corpus/legal/legal_mixed_identifiers_seed_001.txt`
- `corpus/legal/legal_mixed_identifiers_seed_001.gold.json`
- `corpus/care/care_role_preservation_seed_001.txt`
- `corpus/care/care_role_preservation_seed_001.gold.json`
- `corpus/care/care_mixed_identifiers_seed_001.txt`
- `corpus/care/care_mixed_identifiers_seed_001.gold.json`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_EXPAND.md`
- `handover/workpackages/20260617_0906_recall_gold_label_corpus_expand.md`

## Files changed

- `corpus/README.md`
- `tests/test_recall_gold_label_corpus_seed.py`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_GOLD_LABEL_CORPUS_EXPAND.md` pending final closeout update after this handover file

## Product-code changes

None.

## Corpus expansion summary

Added four synthetic source documents:

1. `legal_false_positive_traps_seed_001.txt`
   - Legal false-positive trap sample.
   - Includes legal articles, legal subsection, page, attachment, exhibit, money, date and time traps.
   - Includes true sensitive values for case, dossier, ECLI, person, email and phone.

2. `legal_mixed_identifiers_seed_001.txt`
   - Legal mixed identifier sample.
   - Includes case, rolnummer-like court reference, dossier, client, claim, invoice, IBAN, BSN, ECLI, names, email, phone, address and postcode.

3. `care_role_preservation_seed_001.txt`
   - Care role-preservation sample.
   - Includes standalone care role words and care role/name combinations such as `arts Bakker`, `verpleegkundige Sara El Idrissi`, `cliënt Youssef Ait Ben` and `mantelzorger Fatima Zahra`.

4. `care_mixed_identifiers_seed_001.txt`
   - Care mixed identifier sample.
   - Includes room, department, incident, client number, zorgdossier, medication code, device reference, BIG-like number, names, email, phone and care role words.

## Sidecar/schema summary

Each new `.gold.json` sidecar includes:

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

- Confirmed no prior `WP_RECALL_GOLD_LABEL_CORPUS_EXPAND` claim existed before starting.
- Created claim file before corpus changes.
- Read required control files and relevant recall/scorecard/corpus/risk/decision/claim/handover files.
- Used `corpus/` as existing corpus location.
- Python-assisted offset generation was used before committing new sidecars.
- Extended tests-only validator `tests/test_recall_gold_label_corpus_seed.py` to expect the expanded sidecars and additional preserve-context terms.

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

The expanded corpus reduces the measurability gap but does not close the recall/precision risk because no runner or thresholds exist yet.

## Remaining gaps

- No benchmark runner exists yet.
- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Corpus coverage is improved but still synthetic and not exhaustive.

## Remaining risks

- Quantitative recall/precision remains unavailable until a runner compares analyzer/helper output with the sidecars.
- More synthetic legal/care documents may still be needed before broad trust claims.
- No product claim such as `alle juridische nummers worden altijd herkend` is supported.

## Next recommended step

Do not automatically start a pattern-fix round.

Likely next option after separate coordinator approval:

```text
WP_RECALL_BENCHMARK_RUNNER_MINIMAL
```

Alternative after separate coordinator approval:

```text
WP_DOCX_HYGIENE_RECALL_FOLLOWUP
```
