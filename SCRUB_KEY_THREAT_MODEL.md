# Scrub Key Threat Model — WP25

Status: completed security/specification-only  
Date: 2026-06-09  
Repository: `solidprivacy-nl/scrub`

This document treats the Scrub Key as sensitive re-identification data. It is a security and lifecycle specification only. It does not implement encryption, change the Scrub Key JSON format, change UI behavior, change import/export behavior, or store secrets.

---

## 1. Scope and security position

The Scrub Key is the artifact that makes reviewed scrubbed output reversible. It maps placeholders back to real values.

The key product rule is:

```text
Scrub Key-based output is pseudonymized, not fully anonymized, as long as the Scrub Key exists.
```

The Scrub Key and the scrubbed document must be treated as separate security objects:

- the scrubbed document may be suitable for AI use or external processing only after human review and residual-risk acceptance;
- the Scrub Key contains the mapping needed to restore sensitive values;
- the Scrub Key must stay local, protected and under user control;
- the Scrub Key must not be uploaded to external AI, email, shared drives or third parties unless this is explicit, intended and allowed by policy, client instruction and legal basis.

---

## 2. Terminology: anonymization, pseudonymization, redaction and reinsert

### Anonymization

Anonymization means the document can no longer reasonably be linked back to the original person, matter, client, patient, employee or organization. There is no usable key that can restore the original values.

True anonymization is hard. Scrub should not claim full anonymization when a Scrub Key exists.

### Pseudonymization

Pseudonymization means sensitive values are replaced by placeholders while a separate mapping still exists. The data is safer than the original document, but it remains reversible.

Scrub Key-based output is pseudonymized because placeholders such as `[PERSOON_1]` can be restored with the Scrub Key.

### Redaction

Redaction means sensitive values are removed, blacked out or irreversibly replaced, with no expected reinsert path. Redaction is not the same as Scrub Key-based reversible replacement.

### Reinsert

Reinsert means restoring original values from the Scrub Key into scrubbed text or a supported document flow. Reinsert intentionally brings sensitive values back and must be treated as a high-risk action.

---

## 3. What a Scrub Key contains

A Scrub Key contains metadata and an item list.

Expected metadata includes:

- schema and schema version;
- workflow marker: `Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit`;
- privacy model marker: `pseudonymization_not_full_anonymization`;
- reversible marker;
- storage policy marker;
- external AI policy marker;
- excluded-row policy;
- document or dossier label when supplied;
- item count.

Each mapping item can contain:

- `original_value`: the real sensitive value before replacement;
- `placeholder`: the placeholder used in scrubbed output;
- `entity_type`: the stable technical entity type;
- `type_label`: the user-facing label shown during review;
- `source`: detected, candidate, manual, remembered or similar;
- `review_status`: review state at key creation time;
- `include_state`: whether the row is active in the reversible mapping;
- `timestamp`: timestamp supplied by the reviewed row;
- `document_label`: optional matter, dossier, project or document context.

This means the key can contain names, addresses, e-mail addresses, phone numbers, client numbers, matter numbers, case references, claim numbers, healthcare references, employee identifiers or other confidential values.

---

## 4. Why the Scrub Key is sensitive

The Scrub Key is sensitive because it concentrates the link between safe-looking placeholders and original confidential values.

Security consequences:

- a small JSON file may re-identify a whole document;
- one key may expose many entity classes at once;
- a key can reveal relationships between people, legal matters, care cases, incidents and organizations;
- the key may be more sensitive than the scrubbed document by itself;
- the key may remain dangerous long after the scrubbed document has been shared;
- losing control of the key can turn pseudonymized output back into identifiable confidential content.

---

## 5. Threats and risks

### 5.1 Accidental sharing risks

Scenario:

A user shares both the scrubbed document and the Scrub Key in the same folder, e-mail, chat, AI prompt, Teams channel or export bundle.

Impact:

- the recipient can restore original values;
- the user may believe the document was anonymized while it was only pseudonymized;
- confidentiality, client privilege, healthcare secrecy or internal policy may be breached.

Minimum direction:

- Scrub Key download/export must clearly warn that the key enables re-identification;
- Scrub must discourage storing the key next to externally shared scrubbed output;
- future export bundles must not silently include the key unless explicitly requested.

### 5.2 Local storage risks

Scenario:

The key is saved on a local disk without protection. Other local users, malware, backup software, indexing tools or file sync tools can access it.

Impact:

- local compromise exposes all mapped values;
- automatic cloud sync can turn a local-only workflow into cloud storage;
- endpoint backups may retain the key longer than the user expects.

Minimum direction:

- document local storage locations clearly;
- treat the key as a secret-like sensitive document artifact;
- future lifecycle design should support encrypted/protected key storage.

### 5.3 Download folder risks

Scenario:

The browser downloads the Scrub Key to the default Downloads folder. The user forgets it there.

Impact:

- keys accumulate across matters and clients;
- shared or unmanaged devices expose old keys;
- later cleanup becomes difficult because file names may not explain sensitivity strongly enough.

Minimum direction:

- key filenames and UI warnings should make sensitivity visible;
- future UX should explain that Downloads is temporary and should be cleaned;
- future lifecycle policy should provide deletion reminders or direct delete guidance.

### 5.4 Email and AI upload risks

Scenario:

The user uploads the Scrub Key to a cloud AI service or attaches it to an e-mail together with scrubbed output.

Impact:

- the receiving system can reconstruct sensitive values;
- the key may be retained by external systems;
- the user may violate client, care, contractual, legal or organizational rules.

Minimum direction:

- Scrub must explicitly say: do not upload the Scrub Key to external AI unless this is intentional and allowed;
- AI workflows should use scrubbed content only, not the key;
- reinsert should remain local and deterministic.

### 5.5 Multi-user and shared-computer risks

Scenario:

A user works on a shared device, shared browser profile, remote desktop, unmanaged laptop, school device or care-location workstation.

Impact:

- another user may open the key from downloads or recent files;
- browser state may persist across sessions;
- local temp files or preview tools may retain key contents.

Minimum direction:

- future warning UX should mention shared-computer risk;
- future local runtime should define private storage and cleanup behavior;
- browser-based demo usage must not be positioned as safe for real confidential files.

### 5.6 Retention risks

Scenario:

Keys are kept indefinitely because the user may want to restore values later.

Impact:

- long-term key retention increases breach impact;
- old keys can re-identify old outputs even after the original processing purpose is finished;
- unmanaged retention conflicts with data minimization.

Minimum direction:

- define an expiry/delete policy before adding advanced key management;
- default guidance should prefer short retention and matter-specific deletion decisions;
- retention should be auditable and user-controlled.

### 5.7 Loss-of-key risks

Scenario:

The user deletes or loses the Scrub Key before reinsert is complete.

Impact:

- deterministic reinsert cannot restore original values;
- the scrubbed document may remain usable for AI/external use but cannot be safely rehydrated by Scrub;
- users may try unsafe manual reconstruction.

Minimum direction:

- warn that Scrub cannot restore values without the key;
- future lifecycle design should balance deletion with explicit backup/retention choices;
- do not create hidden server-side recovery copies.

### 5.8 Tampering risks

Scenario:

A Scrub Key is edited manually or maliciously. Placeholders are mapped to wrong original values, duplicated, removed or swapped.

Impact:

- reinsert may restore the wrong person, case number or confidential value;
- legal or care meaning may be corrupted;
- auditability and trust are weakened.

Minimum direction:

- preserve strict validation before import/reinsert;
- report duplicate, missing, unknown or invalid placeholders;
- future protection options should include integrity checks or signatures.

### 5.9 Malformed key risks

Scenario:

The user imports invalid JSON, an incomplete key, a key from another tool, a key from another document, or a key with unexpected fields.

Impact:

- reinsert may fail;
- wrong mappings may be applied if validation is too permissive;
- the user may misinterpret partial restoration as complete restoration.

Minimum direction:

- fail closed on invalid schema or missing required fields;
- show validation issues clearly;
- do not silently ignore structural problems that affect mapping safety.

### 5.10 Import/export risks

Scenario:

Export creates a key that is easier to leak; import loads a key that may not match the current document; reinsert applies mappings to AI-modified text.

Impact:

- export creates a durable sensitive artifact;
- import may revive sensitive data into the wrong document;
- changed placeholders may cause partial or incorrect restoration.

Minimum direction:

- export must warn before and after creating the key;
- import must validate schema, reversible flag, privacy model and item structure;
- reinsert audit must report unknown placeholders, placeholders not found and duplicates;
- no import/export behavior should be changed silently without a separate approved workpackage.

---

## 6. Minimum warning requirements

Any future warning UX must communicate at least:

1. A Scrub Key makes scrubbed output reversible.
2. This is pseudonymization, not full anonymization.
3. The key contains or enables access to real confidential values.
4. Store the key locally and protected.
5. Do not upload the key to external AI services unless explicitly intended and allowed.
6. Do not e-mail or share the key with scrubbed output unless the recipient is allowed to re-identify it.
7. Anyone with the key and matching scrubbed output can restore original values.
8. Losing the key means Scrub cannot deterministically restore the original values.
9. Delete the key when it is no longer needed under the applicable matter, client, care or organizational policy.
10. Reinsert restores sensitive/confidential values and should be done only in a controlled local context.

Suggested Dutch baseline text for future UX planning:

```text
Een Scrub Key maakt deze tekst omkeerbaar. Dit is pseudonimisering, geen volledige anonimisering. De sleutel kan originele vertrouwelijke waarden herstellen. Bewaar de Scrub Key lokaal en beveiligd. Deel of upload de Scrub Key niet naar externe AI, e-mail of derden, tenzij dit bewust bedoeld en toegestaan is.
```

---

## 7. Expiry/delete policy direction

WP25 does not implement a lifecycle policy, but recommends this direction for WP26/WP28:

- classify the Scrub Key as sensitive re-identification data;
- separate key retention from scrubbed document retention;
- prefer shortest practical retention;
- support matter/project-level user decisions;
- provide clear deletion guidance after reinsert/export is finished;
- avoid hidden recovery copies;
- warn when a key is kept in Downloads or another unmanaged location;
- support audit text that records whether a key was created/imported/reinserted, without storing real values in logs;
- define how users handle backups before implementing automatic deletion.

---

## 8. Encryption and protection options

WP25 does not implement encryption. The following options should be evaluated in WP26 before implementation:

### Option A — Warning-only baseline

- Keep current JSON format.
- Add strong warnings and handling guidance.
- Lowest implementation complexity.
- Does not materially protect a leaked file.

### Option B — OS-level file protection guidance

- Keep JSON format.
- Explain storage in protected user folders.
- Rely on local device encryption and access control.
- Useful as interim guidance, but not sufficient for shared or unmanaged devices.

### Option C — Passphrase-protected encrypted Scrub Key file

- Encrypt the key file with a user-supplied passphrase.
- Requires careful UX, recovery messaging and secure cryptographic implementation.
- Loss of passphrase means loss of reinsert ability.
- Must be specified before changing format.

### Option D — Local OS keychain or protected vault

- Use Windows DPAPI, macOS Keychain, Linux Secret Service or equivalent where available.
- Better local integration.
- More complex cross-platform behavior and packaging implications.

### Option E — Integrity protection / tamper detection

- Add checksum, signature or authenticated encryption.
- Detect manual or malicious modifications.
- Helps prevent wrong reinsert mappings.
- Requires clear schema/version planning.

Recommended direction:

WP26 should specify a lifecycle and protection model before any implementation. Encryption must not be added as an ad-hoc patch to the current JSON import/export flow.

---

## 9. Current control boundaries

The current helper design already provides important boundaries:

- pure helpers avoid cloud processing;
- import/reinsert helpers are deterministic and side-effect free;
- validation checks schema, version markers, reversible marker, privacy model and required item fields;
- duplicate placeholders are reported and excluded from mapping in reinsert;
- reinsert returns audit fields such as unknown placeholders and placeholders not found.

Remaining gaps:

- no encrypted storage;
- no expiry/delete enforcement;
- no key vault;
- no tamper-proof key format;
- no user-facing lifecycle workflow beyond current warnings;
- no secure import/export regression test package focused on key safety.

---

## 10. Recommended next workpackages

Recommended next step:

```text
WP26 — Scrub Key encryption/lifecycle specification
```

Recommended WP26 scope:

- define key classification;
- choose lifecycle states: created, downloaded, imported, used for reinsert, expired, deleted;
- define storage and deletion UX requirements;
- compare warning-only, protected file, encrypted file and local vault options;
- define passphrase/key-loss behavior before encryption implementation;
- define integrity/tamper detection requirements;
- preserve backward compatibility or explicitly define migration boundaries.

Follow-up workpackages:

- WP27 — Scrub Key warning UX plan.
- WP28 — Scrub Key expiry/delete policy.
- WP29 — Scrub Key secure import/export tests.
- WP30 — Placeholder robustness review.
- WP35 — DOCX hidden content risk review, because hidden content may still contain sensitive values even if the visible document is pseudonymized.

---

## 11. Intentionally not changed by WP25

WP25 intentionally does not change:

- helper logic;
- Scrub Key JSON schema;
- import behavior;
- export behavior;
- reinsert behavior;
- UI behavior;
- encryption implementation;
- dependencies;
- tests;
- storage of secrets;
- storage of real data.
