# Scrub Key Warning UX Plan — WP27

Status: completed UX/security specification-only  
Date: 2026-06-10  
Repository: `solidprivacy-nl/scrub`

This plan converts the WP25 Scrub Key threat model and the WP26 lifecycle specification into user-facing warning and acknowledgement expectations. It does not implement UI, change Streamlit patch files, change helper logic, change Scrub Key schema, implement encryption, change import/export behavior, change reinsert behavior, add tests, store secrets or add real data.

---

## 1. Scope and UX principles

A Scrub Key is sensitive re-identification data. It maps placeholders back to original confidential values. As long as a Scrub Key exists, matching scrubbed output is pseudonymized, not fully anonymized.

The warning UX must make three things continuously clear:

1. The Scrub Key is not a normal export artifact; it restores sensitive values.
2. The scrubbed document and the Scrub Key must be handled separately.
3. Reinsert and restored downloads intentionally create confidential output again.

This plan is warning and acknowledgement design only. It must be implemented later in a dedicated UI workpackage.

---

## 2. Severity model

| Severity | Meaning | MVP use | Later policy use |
| --- | --- | --- | --- |
| Informational | Explains normal local workflow, limitations or next steps. | Yes. Use for context and non-dangerous reminders. | Yes. |
| Warning | User can continue, but must understand material risk. | Yes. Main level for Scrub Key export/import/reinsert warnings. | Yes. |
| Critical | High-risk action or state. User should make an explicit acknowledgement before continuing. | Yes, for export/download, import/reload, reinsert and restored output download. | Yes. May be backed by stronger controls. |
| Blocking candidate for later policy | Future policy may block until the user fixes a condition or confirms an allowed exception. | No automatic blocking in MVP unless already existing behavior blocks. | Candidate for encrypted/vault/local desktop versions after separate approval. |

MVP warning UX should be clear and repeated at the relevant moment, but must not silently block or change existing export/reinsert behavior unless a later workpackage explicitly approves that policy.

---

## 3. Acknowledgement model

### MVP acknowledgement

MVP should use lightweight acknowledgement at high-risk moments:

- checkbox before Scrub Key download/export;
- checkbox before import/reload if a key is pasted or uploaded;
- checkbox before reinsert mode execution;
- checkbox or explicit button text before restored output download.

Acknowledgement text should be short, concrete and written in Dutch.

Example MVP acknowledgement text:

```text
Ik begrijp dat deze Scrub Key originele vertrouwelijke waarden kan herstellen en dat ik deze sleutel lokaal, apart en beveiligd moet bewaren.
```

### Later professional/local desktop acknowledgement

Later secure/local desktop versions may add:

- persistent first-use education;
- matter/project-specific lifecycle prompts;
- shared-device warning detection;
- expiry/delete acknowledgement;
- encrypted-key/passphrase acknowledgement;
- organization policy acknowledgement;
- blocking gates for invalid, mismatched or tampered keys.

---

## 4. Touchpoint warning plan

### 4.1 Scrub Key creation

Moment:

The key is built from reviewed replacement rows before JSON download/export is offered.

Severity:

- MVP: warning.
- Later: critical if key contains many items or high-risk entity classes.

UX expectation:

- Explain that selected rows become a reversible mapping.
- Remind the user that unchecked/excluded rows are not part of the key under the current model.
- Do not show original values again in warning copy.

Proposed Dutch UI copy:

```text
Let op: u maakt nu een Scrub Key. Deze sleutel koppelt placeholders aan originele vertrouwelijke waarden. Zolang deze sleutel bestaat, is de opgeschoonde tekst pseudoniem en niet volledig anoniem.
```

MVP or later:

- MVP: yes.
- Later: add entity-count/risk summary without exposing values.

Acknowledgement expectation:

- Optional for creation preview.
- Required before download/export.

---

### 4.2 Scrub Key download/export

Moment:

Before the user clicks the Scrub Key download button and immediately after the download is offered.

Severity:

- MVP: critical.
- Later: critical, with possible blocking candidate if policy requires protected storage first.

UX expectation:

- Make clear that the JSON file enables re-identification.
- Tell the user not to upload it to AI or e-mail it with scrubbed output unless explicitly allowed.
- Tell the user to store it separately from scrubbed output.
- Explain that browser downloads may land in an unmanaged Downloads folder.

Proposed Dutch UI copy before download:

```text
Belangrijk: deze Scrub Key kan originele vertrouwelijke waarden herstellen. Download de sleutel alleen als u deze lokaal, apart en beveiligd kunt bewaren. Deel of upload de sleutel niet naar externe AI, e-mail of derden, tenzij dit bewust bedoeld en toegestaan is.
```

Proposed Dutch acknowledgement:

```text
Ik begrijp dat deze Scrub Key herleidbaar is en dat ik deze niet samen met opgeschoonde uitvoer mag delen zonder geldige reden en toestemming.
```

Proposed Dutch UI copy after download offer:

```text
Bewaar de Scrub Key niet onnodig in Downloads. Verplaats de sleutel naar een beveiligde lokale map of verwijder deze zodra hij niet meer nodig is.
```

MVP or later:

- MVP: before-download warning and acknowledgement.
- Later: storage-location detection, protected folder guidance and policy-driven blocking candidate.

---

### 4.3 Scrub Key local storage

Moment:

After export/download guidance, in help text, and in future local desktop storage flows.

Severity:

- MVP: warning.
- Later: critical if unmanaged/shared storage is detected.

UX expectation:

- Explain that local storage is not automatically safe.
- Warn about Downloads, shared computers, cloud sync and backups.
- Encourage separate protected storage.

Proposed Dutch UI copy:

```text
Bewaar de Scrub Key lokaal, apart van de opgeschoonde tekst en bij voorkeur in een beveiligde map. Let op met Downloads, gedeelde computers, automatische cloudsync en back-ups.
```

MVP or later:

- MVP: guidance text only.
- Later: local runtime may detect risky storage paths or provide app-managed storage.

Acknowledgement expectation:

- MVP: no separate acknowledgement unless shown during export.
- Later: acknowledgement if storing in an unmanaged/shared path.

---

### 4.4 Scrub Key import/reload

Moment:

Before upload/paste validation and after validation results.

Severity:

- MVP: critical before loading; warning/critical on validation issues.
- Later: blocking candidate for invalid, mismatched or tampered keys.

UX expectation:

- Warn that the key can restore original values.
- Ask the user to verify that the key belongs to the current document/matter.
- Show validation problems clearly.
- Avoid implying that a valid JSON file automatically belongs to the current text.

Proposed Dutch UI copy before import:

```text
Laad alleen een Scrub Key die bij dit document of dossier hoort. Een geldige sleutel kan originele vertrouwelijke waarden herstellen. Gebruik geen sleutel uit een ander dossier of van een onbekende bron.
```

Proposed Dutch UI copy on validation errors:

```text
Deze Scrub Key kan niet veilig worden geladen. De structuur of verplichte velden kloppen niet. Controleer of dit het juiste bestand is en gebruik geen handmatig aangepaste sleutel zonder extra controle.
```

Proposed Dutch acknowledgement:

```text
Ik begrijp dat ik alleen een Scrub Key mag laden die bij dit document of dossier hoort.
```

MVP or later:

- MVP: warning and validation issue display.
- Later: mismatch detection, key/document fingerprinting and blocking candidate after separate schema/policy work.

---

### 4.5 Reinsert mode

Moment:

When entering `Originele waarden terugzetten` mode and before running reinsert on pasted text, TXT, DOCX or PDF-to-TXT flows.

Severity:

- MVP: critical.
- Later: critical with stronger local desktop controls.

UX expectation:

- Remind user that reinsert restores confidential values.
- Confirm no AI/cloud processing for deterministic reinsert.
- Remind user that output must be reviewed before sharing.
- Require a valid Scrub Key before file reinsert actions.

Proposed Dutch UI copy:

```text
Let op: terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens, dossierinformatie of andere vertrouwelijke gegevens bevatten. Controleer het resultaat zorgvuldig voordat u het opslaat of deelt.
```

Proposed Dutch local-only copy:

```text
Terugzetten gebeurt lokaal met de geladen Scrub Key. Gebruik de Scrub Key niet in externe AI-diensten.
```

Proposed Dutch acknowledgement:

```text
Ik begrijp dat de herstelde uitvoer weer vertrouwelijk is.
```

MVP or later:

- MVP: warning and acknowledgement before running reinsert.
- Later: matter-level policy, local runtime storage guidance, optional expiry prompts.

---

### 4.6 Restored output download

Moment:

Before downloading restored TXT/DOCX output or any future restored output.

Severity:

- MVP: critical.
- Later: blocking candidate if residual audit shows high-risk unresolved issues and policy requires blocking.

UX expectation:

- Make clear that restored output is confidential again.
- Encourage saving only in an appropriate local location.
- Warn not to upload restored output to AI or external parties unless intended and allowed.

Proposed Dutch UI copy:

```text
De herstelde download bevat mogelijk weer originele persoonsgegevens en vertrouwelijke waarden. Sla dit bestand alleen op in een passende beveiligde locatie en deel het niet extern zonder controle en toestemming.
```

Proposed Dutch acknowledgement:

```text
Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten.
```

MVP or later:

- MVP: warning before/near download.
- Later: policy-driven block if validation issues, unknown placeholders or mismatch risk remain unresolved.

---

### 4.7 Deletion/expiry guidance

Moment:

After export, after successful reinsert, in help text, and before any future key deletion/expiry action.

Severity:

- MVP: warning.
- Later: critical before deletion; blocking candidate for expired key use depending on policy.

UX expectation:

- Explain that keeping keys too long increases breach impact.
- Explain that deleting/losing the key prevents deterministic reinsert.
- Do not silently delete keys.
- No hidden recovery copies.

Proposed Dutch UI copy:

```text
Bewaar de Scrub Key niet langer dan nodig. Verwijder de sleutel zodra het doel is afgerond en uw dossier- of organisatiebeleid dat toestaat. Let op: zonder Scrub Key kan Scrub originele waarden niet meer deterministisch terugzetten.
```

Proposed Dutch acknowledgement before future deletion:

```text
Ik begrijp dat verwijderen of verliezen van de Scrub Key betekent dat Scrub deze waarden niet meer automatisch kan terugzetten.
```

MVP or later:

- MVP: guidance only.
- Later: expiry metadata, deletion reminders, app-managed deletion and policy acknowledgements after WP28.

---

### 4.8 Shared-computer risk

Moment:

In warning/help text for Hugging Face demo use, local storage, download guidance and future local desktop first-run checks.

Severity:

- MVP: warning.
- Later: critical or blocking candidate on shared/unmanaged devices if detectable.

UX expectation:

- Warn users that Downloads, browser history, recent files and local previews may expose keys or restored output.
- Do not position the browser/cloud demo as the safe trust environment for real confidential files.

Proposed Dutch UI copy:

```text
Gebruikt u een gedeelde computer, gedeeld browserprofiel of onbeheerde werkplek? Verwerk dan geen echte vertrouwelijke documenten en laat geen Scrub Keys of herstelde bestanden achter in Downloads, recente bestanden of tijdelijke mappen.
```

MVP or later:

- MVP: warning/help text.
- Later: local desktop may add shared-device checks or private workspace guidance.

Acknowledgement expectation:

- MVP: optional.
- Later: required for shared/unmanaged workspace warnings.

---

### 4.9 Email/AI upload risk

Moment:

Scrub Key export, local storage guidance, AI handoff guidance and reinsert mode.

Severity:

- MVP: critical for key export/import; warning for scrubbed-output AI guidance.
- Later: blocking candidate if app detects key file selected for external AI workflow.

UX expectation:

- Distinguish scrubbed output from Scrub Key.
- Explicitly say that the key should not be uploaded to external AI.
- Warn against e-mailing the key together with scrubbed output.

Proposed Dutch UI copy:

```text
Upload de Scrub Key niet naar externe AI. Voor AI gebruikt u alleen de gecontroleerde opgeschoonde tekst, niet de sleutel. Mail de Scrub Key ook niet mee met de opgeschoonde tekst, tenzij de ontvanger de inhoud bewust mag herleiden.
```

MVP or later:

- MVP: critical copy at export/import and AI guidance.
- Later: stronger workflow separation and policy-controlled export bundles.

Acknowledgement expectation:

- MVP: include in export acknowledgement.
- Later: explicit AI workflow acknowledgement.

---

### 4.10 Loss-of-key warning

Moment:

Before download/export, in deletion/expiry guidance and before future deletion action.

Severity:

- MVP: warning.
- Later: critical before deletion or encrypted/passphrase workflows.

UX expectation:

- Explain that Scrub cannot restore without the key.
- Avoid hidden server/cloud recovery promises.
- In later encrypted versions, explain that losing a passphrase has the same practical effect.

Proposed Dutch UI copy:

```text
Zonder Scrub Key kan Scrub originele waarden niet meer deterministisch terugzetten. Bewaar de sleutel zolang terugzetten nog nodig is, maar verwijder hem daarna volgens uw dossier- of organisatiebeleid.
```

MVP or later:

- MVP: guidance in export and deletion/expiry text.
- Later: required acknowledgement for deletion and passphrase-protected key flows.

---

### 4.11 Tampering/mismatch warning

Moment:

Import/reload validation, reinsert audit, unknown placeholders, duplicate placeholders, placeholders not found and future mismatch checks.

Severity:

- MVP: warning or critical depending on validation outcome.
- Later: blocking candidate for tamper detection, failed integrity checks or confirmed document/key mismatch.

UX expectation:

- Warn that hand-edited or wrong keys can restore wrong values.
- Explain that validation problems mean reinsert may not be reliable.
- Make partial restoration visible.
- Do not silently repair or guess mappings.

Proposed Dutch UI copy for mismatch/tampering risk:

```text
Deze Scrub Key lijkt mogelijk niet volledig bij deze tekst te passen, of bevat dubbele/ongeldige mappings. Terugzetten kan daardoor onvolledig of onjuist zijn. Controleer het controleverslag en gebruik bij twijfel de juiste sleutel opnieuw.
```

Proposed Dutch UI copy for unknown placeholders:

```text
De tekst bevat placeholders die niet in de geladen Scrub Key staan. Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel.
```

Proposed Dutch UI copy for duplicate placeholders:

```text
De Scrub Key bevat dubbele placeholders. Deze mappings worden niet automatisch teruggezet om verkeerde herleiding te voorkomen.
```

MVP or later:

- MVP: warning/critical based on existing audit fields.
- Later: blocking candidate after integrity/mismatch policy and tests.

---

## 5. MVP warning set

MVP warning UX should include these warnings and acknowledgements:

1. Scrub Key creation warning.
2. Critical export/download warning with acknowledgement.
3. Local storage / Downloads guidance.
4. Critical import/reload warning with acknowledgement.
5. Critical reinsert warning with acknowledgement.
6. Restored output download warning.
7. Loss-of-key guidance.
8. Email/AI upload risk warning.
9. Tampering/mismatch warnings using current validation and audit fields.

MVP must not include:

- encryption claims;
- automatic deletion;
- schema migration;
- hidden recovery;
- app-managed vault claims;
- blocking export/download changes unless separately approved.

---

## 6. Later secure/local desktop warning set

Later secure/local desktop versions may add:

- detected risky storage warnings;
- app-managed protected local storage warnings;
- encrypted file/passphrase warnings;
- key-vault/device-bound key warnings;
- key recovery/escrow warnings;
- expiry/reminder warnings;
- policy-driven blocking candidates;
- organization-managed acknowledgement logging;
- local runtime shared-device warnings;
- key/document mismatch warnings after fingerprinting or integrity work.

These require separate workpackages because they may affect storage, schema, import/export behavior, encryption, local runtime behavior or organizational policy.

---

## 7. Blocking candidates for later policy

The following should not be silently blocked in MVP, but are candidates for later policy once approved:

| Candidate condition | Reason | Required prior work |
| --- | --- | --- |
| Invalid Scrub Key schema | Reinsert cannot be trusted. | WP29 secure import/export tests. |
| Failed integrity/tamper check | Wrong values may be restored. | Future encrypted/integrity container. |
| Confirmed key/document mismatch | Wrong document may be re-identified. | Future fingerprint/matching spec. |
| Attempt to bundle Scrub Key with scrubbed output for external sharing | Re-identification risk. | Export policy workpackage. |
| Expired key used after policy deadline | Retention/data minimization risk. | WP28 expiry/delete policy. |
| Shared/unmanaged device for real confidential files | Local leakage risk. | WP45/WP46/WP47 local runtime and file-handling checks. |
| External AI upload flow includes Scrub Key | Direct re-identification exposure. | AI handoff policy and workflow controls. |

---

## 8. Audit and logging expectations for warning UX

Future implementation may record warning/acknowledgement events, but must not log original values or full mappings.

Allowed audit fields:

- event type;
- warning severity;
- acknowledgement given true/false;
- timestamp;
- item count;
- validation issue categories;
- unknown/duplicate/not-found placeholder counts;
- local-only/no-AI/no-cloud flags.

Not allowed:

- original values;
- full placeholder-to-original mappings;
- Scrub Key JSON body;
- passphrases;
- encryption keys;
- real customer/client/care data;
- full sensitive file paths.

---

## 9. Implementation sequencing

Recommended sequence after WP27:

1. `WP28 — Scrub Key expiry/delete policy`.
2. `WP29 — Scrub Key secure import/export tests`.
3. Later UI implementation package for MVP warning/acknowledgement copy.
4. Later protected local file handling package.
5. Later encrypted key container specification/implementation package.
6. Later local vault / managed key store package.

---

## 10. Intentionally not changed by WP27

WP27 intentionally does not change:

- UI files;
- Streamlit patch logic;
- helper logic;
- Scrub Key JSON schema;
- import behavior;
- export behavior;
- reinsert behavior;
- encryption implementation;
- tests;
- dependencies;
- secrets;
- real data.
