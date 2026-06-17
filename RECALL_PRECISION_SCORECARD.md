# Recall / Precision Scorecard — Dutch legal and care corpus refresh

Status: refreshed after Dutch legal pattern fixes, scorecard refresh, gold-label corpus seed and corpus expansion.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/documentation-only. No product code, recognizer code, UI, export, Scrub Key or reinsert behavior is changed by this document.

---

## 1. Current evidence status

This scorecard records the current evidence after:

```text
WP_DUTCH_LEGAL_RECALL_GAP_TESTS
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
WP_RECALL_SCORECARD_REFRESH
WP_RECALL_GOLD_LABEL_CORPUS_SEED
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND
```

Current evidence:

- Dutch legal recall gap tests exist and cover documented legal reference values and role-word preservation.
- The first pattern-fix round improved `candidate_scanner.py` only.
- Coordinator evidence confirmed GitHub Actions `Tests #1115`, `Sync to Hugging Face Space #1116` and live Hugging Face smoke check for the pattern-fix verify closeout.
- A synthetic gold-label corpus seed was added.
- The gold-label corpus is now expanded with additional legal/care documents and sidecars.
- Quantitative recall/precision is still pending a runner and accepted thresholds.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label corpus != quantitative score until a runner compares predictions with sidecars.
```

---

## 2. Corpus inventory

Current corpus inventory:

```text
Legal documents: 4
Care documents: 3
Gold sidecars: 7
Validator: tests/test_recall_gold_label_corpus_seed.py
```

Corpus files:

```text
corpus/legal/legal_reference_seed_001.txt
corpus/legal/legal_reference_seed_001.gold.json
corpus/legal/legal_role_preservation_seed_001.txt
corpus/legal/legal_role_preservation_seed_001.gold.json
corpus/legal/legal_false_positive_traps_seed_001.txt
corpus/legal/legal_false_positive_traps_seed_001.gold.json
corpus/legal/legal_mixed_identifiers_seed_001.txt
corpus/legal/legal_mixed_identifiers_seed_001.gold.json
corpus/care/care_reference_seed_001.txt
corpus/care/care_reference_seed_001.gold.json
corpus/care/care_role_preservation_seed_001.txt
corpus/care/care_role_preservation_seed_001.gold.json
corpus/care/care_mixed_identifiers_seed_001.txt
corpus/care/care_mixed_identifiers_seed_001.gold.json
```

Sidecars provide:

- `labels` with exact zero-based offsets;
- `preserve_terms` for legal/care role and context terms;
- `known_traps` for legal articles, dates, times, money amounts, role words, attachment/page labels and care-location ambiguity;
- `synthetic: true` for every document;
- `.example.test` email domains only.

---

## 3. Dutch legal reference coverage

| Value/risk group | Coverage status | Evidence | Scorecard interpretation |
|---|---|---|---|
| `10598721 / UE VERZ 26-441` | baseline + gold sidecar | `test_rechtspraak_like_rolnummers_are_detectable`; `legal_reference_seed_001.gold.json` | Reduced known rolnummer gap; ready for runner measurement. |
| `ARN 26/4412` | baseline + gold sidecar | `test_rechtspraak_like_rolnummers_are_detectable`; `legal_reference_seed_001.gold.json` | Reduced Rechtspraak-like reference gap; broader variants now partly expanded. |
| `ZK-WOON-55091`, `ZK-ARBEID-2026-0007`, `ZK-HUUR-2026-8831` | baseline + expanded corpus | legal reference, false-positive and mixed identifier sidecars | Better measurable case-number coverage. |
| dossier references | baseline + expanded corpus | `DOS-2026-778899`, `DOS-ARBEID-2026-9911`, `DOS-HUUR-2026-1200` | Better measurable dossier-number coverage. |
| client references | baseline + expanded corpus | `CL-FAM-55201`, `CLNT-2026-0042`, `CL-HUUR-2026-0009` | Better measurable client-reference coverage. |
| claim references | baseline + expanded corpus | `CLM-2026-112233`, `CLM-2026-778899` | Specific CLM/phone confusion risk can now be measured across more than one sample. |
| ECLI values | expanded corpus | `ECLI:NL:RBAMS:2026:1234`, `ECLI:NL:RBROT:2026:4455`, `ECLI:NL:RBDHA:2026:8821` | Better measurable ECLI coverage. |
| legal false-positive traps | expanded corpus | articles, page, attachment, production, date, time, money amount | Better precision trap measurability. |

---

## 4. CLM / phone-number risk

The baseline explicitly checks that `CLM-2026-112233` is not treated as a phone entity. The expanded corpus now also includes `CLM-2026-778899`.

Risk update:

- Known CLM/phone confusion risk is reduced for documented samples.
- Multiple CLM-style examples are now available for a future runner.
- This still does not prove that every future legal reference resembling a phone number will always be classified correctly.

---

## 5. Role words / over-masking

The baseline protects these role/context words from being treated as person values on their own:

```text
slachtoffer
arts
getuige
eiser
verweerder
minderjarige
```

The expanded corpus adds or reinforces:

```text
cliënt
zorgmedewerker
verpleegkundige
behandelaar
mantelzorger
kamer
afdeling
```

Role/name combinations now represented include:

```text
arts Jansen
getuige Fatima El Amrani
de minderjarige Sami El Amrani
arts Bakker
verpleegkundige Sara El Idrissi
cliënt Youssef Ait Ben
mantelzorger Fatima Zahra
```

Risk update:

- Role-word over-masking measurability is improved.
- Legal/care meaning must remain readable.
- Names next to role words should be detected as `PERSON`, while role words remain context.

---

## 6. Care coverage

The expanded care corpus improves measurability for:

- care client numbers;
- zorgdossier references;
- MIC incident references;
- room and department context;
- medication/admin codes;
- device references;
- BIG-like numbers;
- care role words;
- care role/name combinations;
- person, phone and email direct identifiers.

Examples now in sidecars:

```text
ZORG-CL-2026-00441
ZORG-CL-2026-77881
ZORG-CL-2026-88990
ZD-2026-99121
ZD-2026-11220
ZD-2026-55661
MIC-2026-0188
MIC-2026-6612
MIC-2026-7720
MED-2026-AX91
VOS-UNIT-2026-441
```

---

## 7. Review/export regression boundaries

The corpus expansion does not execute or change the app, analyzer, review table, export, Scrub Key or reinsert behavior.

Existing boundary tests remain relevant:

```text
tests/test_review_table_collapsible_contract.py
tests/test_side_by_side_review_ui_patch.py
tests/test_side_by_side_review_consolidation_dutch_sample.py
```

Coverage summary:

- `replacement_editor` remains the review table source of truth and fallback.
- Download labels and export/download surfaces remain contract-tested.
- Side-by-side review remains report/visual only.
- No Scrub Key writes are introduced.
- No reinsert behavior change is introduced.
- Corpus tests do not run Presidio, Streamlit or anonymization output.

---

## 8. Open scorecard risks

Open risks:

- No benchmark runner exists yet.
- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still not exhaustive.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.
- The app must not claim: `alle juridische nummers worden altijd herkend`.

Allowed wording:

```text
Nederlandse juridische referenties worden beter als review-kandidaat zichtbaar gemaakt wanneer automatische herkenning ze mist.
```

Disallowed wording:

```text
Alle juridische nummers worden altijd herkend.
```

---

## 9. Recommendation

No immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` should start unless new concrete misses are demonstrated.

Recommended next options:

```text
WP_RECALL_BENCHMARK_RUNNER_MINIMAL — compare sidecars with analyzer/helper output.
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — add more synthetic legal/care documents if coverage is still too thin.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2 — only if concrete new recall gaps are found.
WP_DOCX_HYGIENE_RECALL_FOLLOWUP — if document/export risks now dominate.
```

Most useful next benchmark step:

```text
Build a minimal diagnostic runner before adding more pattern work.
```

---

## 10. Current scorecard status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Baseline assertion plus multiple gold sidecar labels | Reduced for documented samples |
| Role-word preservation | Baseline assertions plus legal/care preserve terms | Reduced for documented samples |
| Over-masking role structure | Baseline assertion and expanded role seeds | Reduced for documented samples |
| Legal false-positive traps | Expanded corpus includes legal articles, dates, times, money, page/attachment labels | Improved precision measurability |
| Care references | Expanded corpus includes client, dossier, incident, BIG-like, room/department, medication and device examples | Improved measurability |
| Review/export regression | Covered by existing contract tests | Guarded, CI remains source of truth |
| Gold-label corpus sidecars | 7 synthetic sidecars present | Improved measurability |
| Quantitative recall | Not available until runner exists | Open |
| Quantitative precision | Not available until runner exists | Open |
| Production safety claim | Not supported | Must remain blocked |
