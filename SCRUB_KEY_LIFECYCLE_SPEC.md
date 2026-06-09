# Scrub Key Lifecycle Specification — WP26

Status: completed security/lifecycle-specification-only  
Date: 2026-06-10  
Repository: `solidprivacy-nl/scrub`

This specification follows `SCRUB_KEY_THREAT_MODEL.md` and treats the Scrub Key as sensitive re-identification data. It defines lifecycle states, retention/deletion expectations and protection options. It does not implement encryption, change the Scrub Key JSON schema, change import/export behavior, change reinsert behavior, change UI behavior, add dependencies, store secrets or add real data.

---

## 1. Security position

A Scrub Key maps placeholders back to original sensitive values. As long as the key exists, Scrub Key-based output is pseudonymized, not fully anonymized.

The Scrub Key must be handled as a separate sensitive security object from:

- the original document;
- the scrubbed/pseudonymized document;
- AI output containing placeholders;
- the restored/reinserted document;
- audit or residual-risk reports.

The MVP may use the existing plain JSON key format with strong warnings and explicit lifecycle guidance. Professional/local desktop versions should move toward protected or encrypted key handling after separate implementation workpackages.

---

## 2. Lifecycle states

### 2.1 Created

Definition:

The key is generated from reviewed replacement rows. It contains the mapping between original values and placeholders.

Risks:

- the key immediately becomes concentrated sensitive data;
- included rows may contain names, case numbers, client numbers, healthcare references, addresses or other confidential values;
- the user may not yet understand that the key makes the output reversible.

Required expectations:

- classify the key as sensitive re-identification data at creation time;
- show or record that the output is pseudonymized, not fully anonymized;
- do not create hidden server-side recovery copies;
- do not store the key automatically outside the user's explicit workflow.

### 2.2 Download/export

Definition:

The user downloads or exports the key as a file.

Risks:

- the key lands in the browser Downloads folder;
- the key may be shared together with the scrubbed document;
- the key may be added to e-mail, Teams, cloud drives or external AI prompts;
- export creates a durable sensitive artifact.

Required expectations:

- warn before and after key export;
- file naming should make sensitivity visible;
- the key must not be silently bundled into external export packages;
- the user should be told to store the key separately from scrubbed output intended for external AI or external sharing.

### 2.3 Local storage

Definition:

The exported key is stored on local disk, network disk, local app storage, browser Downloads, an encrypted container or a future vault.

Risks:

- default Downloads retention;
- local user-account compromise;
- shared-computer access;
- automatic cloud sync;
- endpoint backups;
- file indexing and search previews;
- unmanaged copies across matters.

Required expectations:

- MVP: provide clear guidance to store the key in a protected local location and delete it when no longer needed;
- professional/local desktop: define an explicit protected storage model before implementation;
- do not imply that local storage is automatically safe on shared or unmanaged devices.

### 2.4 Import/reload

Definition:

A previously exported key is loaded back into Scrub to support review, audit or deterministic reinsert.

Risks:

- malformed JSON;
- wrong key for the wrong document;
- old key with stale mappings;
- key altered manually or maliciously;
- user assumes successful import means safe/complete restoration.

Required expectations:

- validate schema, reversible flag, privacy model, item count and required item fields;
- fail closed on invalid structure;
- report validation issues clearly;
- future versions should consider document/key fingerprinting or user-visible matter labels, but not by silently changing schema.

### 2.5 Active use

Definition:

The key is used to restore original values into scrubbed or AI-processed text/document output.

Risks:

- sensitive values are intentionally brought back;
- restored content may be saved or shared accidentally;
- AI-modified placeholders may cause partial restoration;
- wrong key or tampered key may restore wrong values.

Required expectations:

- reinsert must remain local and deterministic;
- audit should show replacement count, unknown placeholders, duplicate placeholders, placeholders not found and validation issues;
- the user should understand that reinserted output is confidential again;
- active-use logs must not contain original sensitive values.

### 2.6 Sharing risk state

Definition:

The key is outside the controlled local user context, for example in e-mail, external AI, cloud storage, shared drives, Teams/Slack chats, support tickets or browser uploads.

Risks:

- any holder of the key plus matching scrubbed output can re-identify the document;
- external services may retain or process the key;
- professional secrecy, care confidentiality, client instructions or policy may be violated.

Required expectations:

- warn that sharing the key is equivalent to sharing re-identification capability;
- do not encourage key upload to AI services;
- future UX should separate "share scrubbed output" from "share re-identification key".

### 2.7 Expired

Definition:

The key is no longer needed for the current matter, project, AI roundtrip, review or reinsert workflow, but may still exist.

Risks:

- stale keys remain useful for re-identification;
- old keys accumulate across clients or dossiers;
- users may not know which key belongs to which output.

Required expectations:

- MVP: provide policy guidance that keys should be deleted when no longer needed;
- later versions: provide expiry metadata, reminders or managed lifecycle states only after schema/lifecycle decisions;
- expiry must not silently destroy a key without explicit user understanding because loss of key prevents deterministic reinsert.

### 2.8 Deleted

Definition:

The key is removed by the user or future local lifecycle tooling.

Risks:

- deterministic reinsert is no longer possible;
- old backups may still contain the key;
- users may assume deletion from the app also deletes browser Downloads or cloud copies.

Required expectations:

- explain that deletion prevents Scrub from restoring values from that key;
- do not keep hidden recovery copies;
- future tooling should distinguish app-managed deletion from external file deletion;
- deletion audit must not store original values.

---

## 3. Loss-of-key consequences

If the Scrub Key is lost, Scrub cannot deterministically restore the original values.

Consequences:

- reinsert cannot be completed through the normal local deterministic workflow;
- the scrubbed document may remain useful for AI/external processing, but cannot be safely rehydrated through Scrub;
- manual reconstruction may create errors or confidentiality risks;
- if the key is encrypted later, losing the passphrase has the same practical effect as losing the key.

Policy direction:

- do not create hidden cloud/server recovery copies;
- warn before deletion;
- clearly separate deletion from secure backup decisions;
- for professional versions, define organization-controlled recovery only if explicitly approved and legally/policy compatible.

---

## 4. Tampering consequences

If the Scrub Key is changed, corrupted or maliciously edited, reinsert may restore wrong values.

Consequences:

- a person may be restored into the wrong role or matter;
- a legal or care document may become semantically wrong;
- case numbers, client numbers or healthcare references may be swapped;
- audit trust is weakened;
- partial restoration may be mistaken for complete restoration.

Policy direction:

- current structural validation remains necessary;
- future protected/encrypted formats should include integrity protection;
- manual edits should be treated as unsafe unless validated;
- tamper detection should fail closed or force explicit user review.

---

## 5. Protection option comparison

| Option | Description | Advantages | Main risks / limitations | MVP recommendation | Later professional/local desktop recommendation |
| --- | --- | --- | --- | --- | --- |
| Warning-only | Keep the current plain JSON key and rely on strong warnings, file naming, user guidance and audit text. | Simple; compatible with current helpers; no schema migration; low implementation risk. | Does not protect a leaked key; depends heavily on user behavior; weak on shared devices and synced Downloads. | Acceptable as MVP baseline if warnings are explicit and lifecycle guidance is clear. | Not sufficient as final professional model. |
| Protected local file | Keep file-based handling but guide or enforce storage in protected local folders; rely on OS account controls, disk encryption or managed device policy. | Low schema impact; works with local-first direction; can be improved by installer/runtime guidance. | Protection varies by device; weak on unmanaged/shared devices; automatic cloud sync/backups may still expose keys. | Good near-term improvement after warning UX; no crypto implementation required if guidance-only. | Useful as baseline for managed environments, but should be paired with integrity checks or encryption for high-trust use. |
| Encrypted local file | Store the Scrub Key in an encrypted file, likely passphrase-protected or protected by an app-managed local key. | Protects leaked files better; can include authenticated encryption/tamper detection; supports portable key files. | Requires cryptographic design, dependency review, UX design, passphrase-loss handling, versioning and migration plan. | Not for immediate MVP unless separately specified and implemented. | Recommended candidate for professional local desktop, especially for portable keys. |
| Local vault / managed key store | Store keys in a local app vault or OS managed key store such as Windows DPAPI, macOS Keychain or Linux Secret Service. | Best user experience when integrated well; can reduce exposed files; aligns with local desktop direction. | More complex cross-platform behavior; backup/recovery is hard; may lock keys to device/user profile; packaging implications. | Out of MVP scope. | Strong candidate for later professional desktop version, possibly combined with encrypted export for portability. |

---

## 6. Recommended MVP versus later versions

### MVP recommendation

The MVP should use:

```text
warning-only + explicit lifecycle guidance + protected-local-file guidance
```

MVP must include:

- strong warning language at export/import/reinsert touchpoints;
- clear statement that the key enables re-identification;
- guidance to keep the key local, separate and protected;
- guidance to avoid external AI, e-mail and shared folders;
- deletion guidance after the key is no longer needed;
- audit logging that records events without original values;
- no hidden recovery copies;
- no encryption claims.

Rationale:

This preserves current schema and behavior, avoids fragile ad-hoc crypto and makes the immediate risk visible without changing import/export semantics.

### Later professional/local desktop recommendation

A professional/local desktop version should evaluate:

```text
encrypted local file + local vault / managed key store + integrity protection
```

Professional version should consider:

- authenticated encryption for portable key files;
- OS keychain/DPAPI-backed storage for app-managed keys;
- explicit backup and recovery policy;
- tamper detection;
- versioned key containers;
- enterprise/device-management compatibility;
- audit events without sensitive values;
- local-only operation and no cloud recovery by default.

Rationale:

Professionals handling legal or care documents need stronger protection than warnings alone. However, protection must not create surprise data loss or silent schema incompatibility.

---

## 7. Password and passphrase considerations

If passphrase-protected encryption is implemented later:

- the passphrase must not be stored in the repository, logs, audit files or Scrub Key metadata;
- loss of the passphrase means loss of access to the Scrub Key unless an approved recovery model exists;
- weak passphrases reduce the benefit of encryption;
- copy-paste mistakes and keyboard-layout differences can cause permanent lockout;
- UX must explain that Scrub cannot recover a forgotten passphrase by default;
- passphrase prompts must not reveal original values;
- automated tests must use synthetic dummy passphrases only;
- the implementation must use reviewed cryptographic libraries and authenticated encryption, not custom cryptography.

MVP decision:

No passphrase workflow should be added in WP26. It requires separate implementation approval.

---

## 8. Key recovery considerations

Recovery is a product and legal-policy decision, not only a technical feature.

Recovery options to evaluate later:

- no recovery: safest against hidden copies, but users lose reinsert if the key/passphrase is lost;
- user-managed backup: user stores a protected backup, with clear risk ownership;
- organization-managed escrow: possible for enterprise deployments, but requires governance, access controls and audit;
- device-bound recovery: possible with local OS vaults, but may fail after device replacement or profile loss;
- cloud recovery: not aligned with local-first confidential processing unless explicitly approved.

WP26 recommendation:

For MVP, use no hidden recovery. For later professional versions, evaluate recovery only as part of a separate approved lifecycle/security implementation plan.

---

## 9. Metadata risks

Scrub Key metadata can be sensitive even when it does not directly contain original values.

Risky metadata examples:

- document labels that reveal client, matter, patient, case or project context;
- timestamps that reveal when a matter was processed;
- source/review status that reveals workflow decisions;
- entity types and item counts that reveal document sensitivity;
- filenames that include client or matter details;
- audit events that identify users, paths or devices.

Policy direction:

- do not store original values in audit logs;
- keep document labels optional and synthetic in tests;
- avoid sensitive filename defaults;
- treat metadata as sensitive operational data;
- future logs should record event types and counts, not mapped values.

---

## 10. Audit and logging expectations

Audit should support user control and incident review without becoming a new leakage source.

Recommended audit events:

- key created;
- key exported/downloaded;
- key imported/reloaded;
- key validation failed;
- key used for reinsert;
- key expired or marked no longer needed;
- key deletion guidance shown;
- key deleted by app-managed storage, if future app-managed storage exists.

Audit must not contain:

- `original_value` contents;
- full placeholder-to-original mappings;
- passphrases;
- encryption keys;
- real customer/client/care data;
- full local file paths if they reveal sensitive matter names, unless explicitly approved.

Audit may contain:

- timestamps;
- event type;
- item count;
- validation issue categories;
- unknown/duplicate/not-found placeholder counts;
- whether processing was local-only/no-AI/no-cloud;
- document label only if the user supplied it and it is considered acceptable.

---

## 11. Minimum UI warning requirements

WP26 does not implement UI changes, but future WP27 warning UX should cover these touchpoints:

1. Before Scrub Key export/download.
2. Immediately after Scrub Key export/download.
3. Before import/reload.
4. Before reinsert.
5. After reinsert, when output is confidential again.
6. When the key appears to be stored in or downloaded to an unmanaged location, if detectable in a future local app.
7. Before key deletion or expiry action.

Minimum warning content:

- a Scrub Key makes scrubbed output reversible;
- this is pseudonymization, not full anonymization;
- anyone with the key and matching scrubbed output can restore original values;
- keep the key local, separate and protected;
- do not upload the key to external AI;
- do not e-mail or share the key unless the recipient is allowed to re-identify the document;
- deleting or losing the key prevents deterministic reinsert;
- reinserted output is confidential again.

Suggested Dutch baseline:

```text
Een Scrub Key maakt deze tekst omkeerbaar. Dit is pseudonimisering, geen volledige anonimisering. Bewaar de sleutel lokaal, apart en beveiligd. Deel of upload de Scrub Key niet naar externe AI, e-mail of derden, tenzij dit bewust bedoeld en toegestaan is. Als u de sleutel verliest of verwijdert, kan Scrub de originele waarden niet meer deterministisch terugzetten.
```

---

## 12. Implementation phases

### Phase 0 — Current baseline

Current state:

- plain JSON Scrub Key;
- import validation;
- deterministic local reinsert;
- audit fields around reinsert;
- warnings around key sensitivity.

No WP26 implementation change.

### Phase 1 — MVP lifecycle and warning hardening

Future workpackages:

- WP27 warning UX plan;
- WP28 expiry/delete policy;
- WP29 secure import/export tests.

Allowed direction:

- warning copy and UX placement;
- lifecycle guidance;
- deletion guidance;
- tests for import/export safety expectations;
- no encryption or schema migration unless separately approved.

### Phase 2 — Protected local file handling

Future workpackages should define:

- safer default filenames;
- local storage guidance;
- app-managed local folder strategy, if local runtime exists;
- browser Downloads limitations;
- backup/sync warnings;
- audit events without sensitive values.

### Phase 3 — Encrypted file container specification and implementation

Only after explicit approval:

- define encrypted container format;
- define versioning and migration;
- define authenticated encryption and tamper detection;
- define passphrase loss behavior;
- define compatibility with existing JSON keys;
- add tests with synthetic keys only.

### Phase 4 — Local vault / managed key store

Only for professional/local desktop versions:

- define OS keychain/DPAPI/Secret Service strategy;
- define device/user-profile binding consequences;
- define enterprise policy options;
- define local backup and recovery model;
- define migration between vault and encrypted export.

---

## 13. Recommended next workpackages

Immediate next step:

```text
WP27 — Scrub Key warning UX plan
```

Reason:

The MVP recommendation is warning-only plus explicit lifecycle guidance. Warning UX must therefore be specified before changing user-facing flows.

Alternative/parallel next step after WP27 is defined:

```text
WP29 — Scrub Key secure import/export tests
```

Reason:

Secure import/export tests can verify that invalid, malformed, wrong-policy or risky key cases are reported safely without changing behavior.

Follow-up work:

- WP28 — Scrub Key expiry/delete policy.
- Later implementation package — protected local file handling.
- Later implementation package — encrypted key container.
- Later implementation package — local vault / managed key store.

---

## 14. Intentionally not changed by WP26

WP26 intentionally does not change:

- helper logic;
- Scrub Key JSON schema;
- import behavior;
- export behavior;
- reinsert behavior;
- UI behavior;
- encryption implementation;
- dependency list;
- tests;
- storage of secrets;
- storage of real data.
