# Scrub Key Expiry/Delete Policy — WP28

Status: completed security/lifecycle-policy-only
Date: 2026-06-10
Repository: `solidprivacy-nl/scrub`

This policy follows `SCRUB_KEY_THREAT_MODEL.md`, `SCRUB_KEY_LIFECYCLE_SPEC.md` and `SCRUB_KEY_WARNING_UX_PLAN.md`. It defines expiry, retention and deletion expectations for Scrub Keys. It does not implement UI, automatic deletion, encryption, schema migration, import/export behavior changes, reinsert behavior changes, tests, secrets, real data or cloud processing.

---

## 1. Policy position

A Scrub Key is sensitive re-identification data. It maps placeholders back to original confidential values. As long as a matching Scrub Key exists, scrubbed output is pseudonymized, not fully anonymized.

The core expiry/delete policy is:

```text
Scrub Keys must be retained only as long as needed for a specific matter, project, AI roundtrip, review or reinsert purpose. Deletion must remain explicit and user-controlled. Scrub must not silently delete keys or keep hidden recovery copies.
```

This balances two risks:

- keeping a key too long increases re-identification and leakage risk;
- deleting or losing a key too early prevents deterministic reinsert.

---

## 2. Retention principles

Scrub Key retention should follow these principles:

1. **Purpose limitation** — keep a key only for the concrete matter, project, document, AI roundtrip, review or reinsert workflow that needs it.
2. **Separation** — store the Scrub Key separately from scrubbed output that may be sent to AI or external parties.
3. **Local control** — keep the key under the user's or organization's local control; do not upload it to external AI, e-mail, shared links or third parties unless re-identification is intentionally allowed.
4. **Shortest practical retention** — delete the key when reinsert and review are complete and dossier or organization policy allows deletion.
5. **No hidden recovery** — Scrub must not create hidden cloud, server or repository recovery copies.
6. **No silent destruction** — Scrub must not silently delete keys, mappings, restored output or audit context.
7. **Explicit accountability** — users must understand that retaining a key preserves re-identification capability and deleting a key removes deterministic restore capability.

Recommended Dutch user-facing copy:

```text
Bewaar een Scrub Key alleen zolang u deze nodig heeft voor dit dossier, project of deze AI-ronde. Zolang de sleutel bestaat, kan de opgeschoonde tekst weer herleidbaar worden gemaakt.
```

---

## 3. User-controlled deletion

Deletion is a user decision in MVP. Scrub may advise, warn and later provide tools, but the current product must not delete Scrub Keys automatically.

User-controlled deletion means:

- the user decides whether the key is still needed;
- the user chooses when to delete the exported key file;
- the user understands that deletion prevents deterministic reinsert;
- future app-managed deletion must require clear confirmation;
- future deletion tooling must distinguish app-managed key storage from files outside Scrub, such as browser Downloads, synced folders and backups.

MVP may provide deletion guidance only. It must not:

- search the user's disk for Scrub Key files;
- remove files from Downloads;
- remove external backups;
- remove synced cloud copies;
- remove e-mail attachments or chat uploads;
- remove keys from external systems;
- claim that deletion in Scrub deletes all copies everywhere.

Recommended Dutch user-facing copy:

```text
Verwijder de Scrub Key handmatig zodra terugzetten niet meer nodig is en uw dossier- of organisatiebeleid dat toestaat. Let op: Scrub kan geen kopieën verwijderen uit Downloads, e-mail, cloudsync of back-ups.
```

---

## 4. Matter/project retention guidance

Retention should be tied to the user's matter or project, not to a generic product default.

Recommended guidance by situation:

| Situation | Recommended handling |
| --- | --- |
| Short AI rewrite/summarization roundtrip | Keep the key only until AI output is reviewed and any needed reinsert is complete. |
| Active legal matter or care project | Keep the key only if reinsert, audit or controlled review is still realistically needed. |
| Shared internal review | Store the key only in an approved protected local or organization-controlled location, separate from scrubbed output. |
| External AI or third-party sharing | Do not share the key unless the recipient is explicitly allowed to re-identify the content. |
| Matter/project closed | Delete the key if no further reinsert, audit or policy requirement justifies retention. |
| Legal/organizational hold | Follow approved retention policy; do not delete solely because Scrub suggests cleanup. |

Scrub should not define legal retention periods. The product should help users apply their own professional, contractual and organizational policies.

Recommended Dutch user-facing copy:

```text
Koppel de bewaartermijn van de Scrub Key aan het dossier of project. Is terugzetten niet meer nodig en mag de sleutel volgens beleid weg? Verwijder de sleutel dan.
```

---

## 5. Download-folder risk

Browser Downloads is a high-risk temporary location for Scrub Keys.

Risks:

- keys accumulate across matters;
- users forget that the file exists;
- shared or unmanaged devices expose old keys;
- automatic cloud sync may copy Downloads;
- backup or indexing tools may retain the key;
- file names may reveal sensitive matter context.

Policy:

- MVP must warn that Downloads is not a safe long-term storage location.
- Users should move a key to an approved protected local location if it must be retained.
- Users should clean the Downloads copy after moving or after reinsert is complete.
- Scrub must not claim it can delete the Downloads copy unless a later local app implements explicit user-confirmed deletion.

Recommended Dutch user-facing copy:

```text
Laat de Scrub Key niet onnodig in Downloads staan. Verplaats de sleutel naar een beveiligde lokale map of verwijder hem zodra u hem niet meer nodig heeft.
```

---

## 6. Shared-computer risk

Shared devices, shared browser profiles, remote desktops, unmanaged laptops, school devices and care-location workstations are not safe places to leave Scrub Keys.

Risks:

- another user may open the key from Downloads or recent files;
- browser state may persist;
- local preview tools may cache file contents;
- restored output may remain in temporary folders;
- the user may not control backups, sync or endpoint monitoring.

Policy:

- MVP must warn against using real confidential documents and Scrub Keys on shared/unmanaged devices.
- If a user still works on a shared environment, they must remove downloaded keys and restored files from user-accessible locations before leaving.
- Later local desktop versions may add shared-device warnings, private workspace guidance or managed storage checks, but only after separate implementation approval.

Recommended Dutch user-facing copy:

```text
Gebruikt u een gedeelde computer of gedeeld browserprofiel? Laat geen Scrub Keys, originele documenten of herstelde bestanden achter in Downloads, recente bestanden of tijdelijke mappen.
```

---

## 7. Expiry guidance

Expiry means the key is no longer needed for its purpose. Expiry is not the same as automatic deletion.

MVP expiry model:

```text
guidance-only expiry
```

In MVP:

- a key may be described as "niet langer nodig" by the user;
- Scrub may advise cleanup after export, after reinsert and in help text;
- Scrub must not add expiry metadata to the current schema;
- Scrub must not block import of an old key solely because of age;
- Scrub must not automatically delete an old key.

Later versions may add:

- optional expiry dates;
- matter/project lifecycle prompts;
- reminders for old app-managed keys;
- policy-controlled use of expired keys;
- app-managed deletion workflow with explicit confirmation;
- enterprise retention policy integration.

Later expiry enforcement must be careful: a hard expiry can protect confidentiality, but it can also cause surprise loss of reinsert capability.

Recommended Dutch user-facing copy:

```text
Een Scrub Key verloopt niet automatisch. Controleer zelf of de sleutel nog nodig is. Is het doel afgerond? Verwijder de sleutel volgens uw beleid.
```

---

## 8. Manual deletion guidance

Manual deletion guidance should be concrete but honest about limits.

User guidance:

1. Confirm that reinsert, review and audit use are complete.
2. Confirm that the key is not needed under matter, project, legal hold or organization policy.
3. Delete the exported key file from the storage location where it was saved.
4. Check the browser Downloads folder if the key was downloaded there.
5. Check whether the file was copied to synced folders, e-mail, chat or shared drives.
6. If the key was shared externally, treat deletion as incomplete until external copies are handled through the relevant policy/process.

Scrub should not overpromise secure deletion. Normal file deletion may leave recoverable traces in backups, sync systems or storage media. Secure deletion is environment-specific and should be handled by the user's organization or endpoint policy.

Recommended Dutch user-facing copy:

```text
Controleer vóór verwijderen of u de Scrub Key niet meer nodig heeft. Zonder sleutel kan Scrub de originele waarden niet meer automatisch terugzetten. Verwijder daarna ook eventuele kopieën in Downloads, cloudsync, e-mail of gedeelde mappen.
```

---

## 9. Loss-of-key consequences

If a Scrub Key is deleted, lost or inaccessible, Scrub cannot deterministically restore original values from that key.

Consequences:

- pasted-text, TXT, DOCX and PDF-to-TXT reinsert cannot restore the original values for that key;
- scrubbed output may remain useful for AI or external processing, but cannot be safely rehydrated by Scrub;
- manual reconstruction can introduce errors and confidentiality risks;
- if encryption is added later, losing the passphrase has the same practical effect as losing the key;
- Scrub must not promise cloud/server recovery in a local-first model.

Policy:

- warn before future deletion actions;
- warn in export and retention guidance;
- do not create hidden recovery copies;
- do not log original values to support recovery;
- later recovery/escrow models require explicit organizational/legal approval.

Recommended Dutch user-facing copy:

```text
Zonder Scrub Key kan Scrub de originele waarden niet meer deterministisch terugzetten. Bewaar de sleutel zolang terugzetten nog nodig is, maar verwijder hem daarna bewust volgens beleid.
```

---

## 10. Tampering/mismatch consequences

A retained key is only useful if it still matches the intended scrubbed output and has not been altered.

Risks:

- a wrong key may restore values into the wrong document;
- a hand-edited key may restore incorrect people, matter numbers or care references;
- missing mappings may create partial restoration;
- duplicate placeholders may make reinsert ambiguous;
- altered item counts or schema fields may weaken audit trust.

Policy:

- current import validation must remain conservative;
- reinsert must not guess missing mappings;
- duplicate, unknown and not-found placeholders must remain visible in audit output;
- future tamper protection should fail closed or require explicit user review;
- later protected/encrypted key containers should include integrity protection before relying on expiry/deletion state.

Recommended Dutch user-facing copy:

```text
Gebruik alleen een Scrub Key die bij dit document of dossier hoort. Een aangepaste, beschadigde of verkeerde sleutel kan waarden onjuist of onvolledig terugzetten.
```

---

## 11. Audit/logging expectations

Audit and logging should support accountability without storing sensitive mappings.

MVP audit expectations:

- record or display that key export/download guidance was shown;
- record or display import validation results;
- record reinsert counts, unknown placeholders, duplicate placeholders and placeholders not found;
- record local-only/no-AI/no-cloud status where available;
- do not store original values in logs;
- do not store full placeholder-to-original mappings in logs;
- do not store passphrases, keys or future encryption material;
- avoid full local file paths if they reveal matter names or personal data.

Future app-managed lifecycle audit may record:

- key created;
- key exported/downloaded;
- key imported/reloaded;
- key marked no longer needed;
- key deletion warning shown;
- app-managed key deleted after explicit confirmation;
- expired-key warning shown;
- validation/tamper/mismatch category.

Deletion audit must not become a hidden recovery mechanism.

Recommended Dutch user-facing copy:

```text
Het controleverslag mag aantallen en waarschuwingen tonen, maar mag geen originele waarden of volledige sleutelinhoud opslaan.
```

---

## 12. What MVP should warn about

MVP should warn about:

1. A Scrub Key enables re-identification.
2. Output with an existing key is pseudonymized, not fully anonymized.
3. Downloads is not a safe long-term storage location.
4. Keys should be stored separately from scrubbed output.
5. Keys should not be uploaded to external AI.
6. Keys should not be e-mailed or shared with scrubbed output unless re-identification is intended and allowed.
7. Shared computers and shared browser profiles are risky.
8. Retain the key only while reinsert/review/audit still needs it.
9. Delete the key manually when no longer needed and policy allows deletion.
10. Losing or deleting the key prevents deterministic reinsert.
11. Wrong, tampered, duplicate or mismatched keys can restore incorrectly.
12. Restored output is confidential again.

MVP must keep warnings as guidance/acknowledgement only unless a later approved workpackage explicitly changes behavior.

---

## 13. Later secure/local desktop enforcement candidates

Later professional/local desktop versions may enforce or assist with:

- app-managed protected local key storage;
- explicit "mark no longer needed" lifecycle state;
- user-confirmed app-managed deletion;
- expiry reminders;
- protected-folder checks;
- shared-device warnings;
- cloud-sync/download-folder warnings;
- encrypted key containers;
- integrity/tamper detection;
- matter/project labels that help users choose the correct key;
- organization retention policy prompts;
- local vault / OS key-store integration;
- enterprise recovery/escrow only after explicit governance approval.

Later versions may block or require extra acknowledgement for:

- importing structurally invalid keys;
- importing keys with failed integrity checks;
- using a key that appears mismatched to the current document;
- using a key marked expired/no longer needed;
- saving app-managed keys to risky storage locations if policy requires protection.

These enforcement options require separate implementation workpackages, tests and migration decisions.

---

## 14. What must never be deleted silently

Scrub must never silently delete:

- exported Scrub Key files;
- Scrub Key mappings;
- original uploaded documents;
- scrubbed output;
- AI output containing placeholders;
- restored output;
- audit reports needed to understand reinsert results;
- user-created backups;
- files in browser Downloads;
- files in synced folders, shared drives, e-mail or chat;
- app-managed key vault entries, if implemented later;
- recovery/escrow records, if explicitly approved later.

Silent deletion is not acceptable because it can destroy deterministic reinsert capability, violate matter retention requirements and undermine user trust.

Allowed future behavior, only after separate approval:

- show cleanup reminders;
- provide a user-confirmed delete action for app-managed keys;
- mark keys as expired/no longer needed;
- warn that external copies may still exist;
- write non-sensitive deletion audit events.

---

## 15. Recommended implementation phases

### Phase 1 — MVP policy and warning implementation planning

Recommended package:

```text
WP28B — Scrub Key warning implementation planning
```

Scope:

- map WP27 and WP28 copy to exact UI locations;
- define which warnings need acknowledgement;
- keep behavior unchanged until implementation package is approved;
- no automatic deletion.

### Phase 2 — Secure import/export tests

Recommended package:

```text
WP29 — Scrub Key secure import/export tests
```

Scope:

- test malformed key import;
- test missing required policy markers;
- test privacy model/reversible validation;
- test duplicate/mismatch warning surfaces if currently available;
- test that warnings and validation do not expose original values;
- no schema migration and no encryption.

### Phase 3 — MVP warning/acknowledgement UI implementation

Scope:

- implement approved warning copy;
- add acknowledgements for key export/import/reinsert/restored output where approved;
- preserve current import/export and reinsert behavior;
- no automatic deletion.

### Phase 4 — Local runtime protected storage guidance

Scope:

- add local runtime storage guidance after WP46/WP47;
- document Downloads/cloud-sync/shared-device risks in local app context;
- consider app-managed key folder only after explicit design.

### Phase 5 — Professional key protection and lifecycle enforcement

Scope:

- encrypted key container;
- authenticated integrity checks;
- optional expiry metadata;
- user-confirmed app-managed deletion;
- local vault / managed key store;
- governance-approved recovery/escrow where relevant.

---

## 16. Intentionally not changed by WP28

WP28 intentionally does not change:

- UI implementation;
- Streamlit patch files;
- helper logic;
- Scrub Key JSON schema;
- import behavior;
- export/download behavior;
- reinsert behavior;
- automatic deletion;
- encryption;
- tests or CI gates;
- dependencies;
- secrets handling;
- real data handling;
- cloud processing.
