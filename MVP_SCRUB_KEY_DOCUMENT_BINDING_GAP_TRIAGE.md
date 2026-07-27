# SolidPrivacy Scrub — MVP Scrub Key Document-Binding Gap Triage

Workpackage: `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`  
Status: completed triage; implementation not started  
Repository: `solidprivacy-nl/scrub`

## 1. Evidence being triaged

The Phase 6 roundtrip matrix proves two different wrong-key outcomes:

1. A wrong key with a different placeholder namespace is visible. The document placeholders remain unknown and the key placeholders are reported as not found.
2. A structurally valid wrong or edited key that uses exactly the same placeholder names can restore incorrect original values without a validation error, unknown-placeholder signal or missing-placeholder signal.

The second outcome is critical because the current document and Scrub Key have no independently verifiable common binding value.

Evidence source:

- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- case `wrong_key_same_placeholder_namespace`
- finding `scrub_key_document_binding_missing`

## 2. Threat classes

### A. Accidental wrong-document pairing

A user selects a valid Scrub Key from another document or dossier. This is the primary MVP problem. It should fail closed without adding repeated confirmation steps.

### B. Accidental key corruption

A key is edited, truncated or otherwise changed unintentionally. Structural validation already detects many changes, but a valid-looking edit to original values is not currently detectable.

### C. Deliberate malicious tampering

An attacker intentionally changes original values and also updates any unkeyed checksum or visible binding metadata. Robust protection requires authenticity, such as a digital signature or HMAC backed by protected local key material. The current web prototype has no trusted signing-key lifecycle and must not claim tamper-proof keys.

## 3. Current architecture constraints

- Automatic placeholders are currently generated as stable generic tokens such as `[PERSOON_01]` in `document_tools.placeholder_for_entity`.
- Manual placeholders use generic tokens such as `[PERSOON_HANDMATIG_01]` in `manual_mask_entry.build_manual_placeholder`.
- The Scrub Key records the placeholder-to-original mapping but has no required document-binding identifier.
- `document_label` is descriptive, optional and user-controlled. It is not a security binding.
- Reinsert validates key structure and placeholder correspondence but cannot distinguish two valid keys that use the same generic placeholder names.
- The supported workflow includes pasted text, TXT, DOCX and PDF-to-restored-TXT. A solution must work across all of them and survive normal AI text roundtrips when placeholders are preserved.
- The user-facing flow must remain document first, key second, download third. No new hidden checkbox/button sequence is acceptable.

## 4. Options assessed

### Option 1 — Match `document_label`

Decision: reject as a security control.

Reason:

- optional and editable;
- labels can be duplicated;
- no cryptographic or structural relation to the document;
- risks false confidence.

It may remain useful display metadata only.

### Option 2 — Hash the complete scrubbed document

Decision: reject as the primary roundtrip binding.

Reason:

- AI rewriting legitimately changes document content;
- whitespace, formatting and document conversion change the hash;
- would reject valid roundtrips even when placeholders are preserved.

A content hash can still be useful as optional exact-export evidence, not as the reinsert gate.

### Option 3 — Hash the placeholder list or order

Decision: reject as sufficient binding.

Reason:

- the critical evidence already uses the same placeholder namespace;
- wrong keys can have the same placeholder list and order;
- AI may remove or reorder sections.

### Option 4 — Put a binding ID only in a filename, metadata field or separate sidecar

Decision: reject as the primary mechanism.

Reason:

- filenames are easily changed;
- DOCX/PDF metadata may be stripped and is part of the document-hygiene risk surface;
- pasted text and TXT do not provide reliable hidden metadata;
- a third sidecar file would make the recently simplified workflow less intuitive.

### Option 5 — Add a document-specific binding token to every placeholder and to the Scrub Key

Decision: recommended for accidental wrong-document protection.

Illustrative form:

```text
[PERSOON_K7M4Q9X2_01]
[DOSSIERNUMMER_K7M4Q9X2_01]
[PERSOON_K7M4Q9X2_HANDMATIG_01]
```

Properties:

- the token is generated locally and contains no personal data;
- every placeholder in one document uses the same binding token;
- the Scrub Key records the same token and binding version;
- reinsert extracts the token from the document and compares it with the key;
- no match or mixed tokens cause fail-closed reinsert before any value is restored;
- the binding travels with pasted text, TXT, DOCX and PDF text because it is part of the placeholders;
- no extra upload, checkbox or action button is needed;
- existing placeholder-preservation instructions remain applicable.

Recommended token properties:

- random, locally generated, at least 80 bits of entropy;
- uppercase base32 or hexadecimal characters compatible with the current placeholder grammar;
- injected by a helper so tests can supply a deterministic token;
- non-secret but treated as document-specific correlation metadata.

### Option 6 — Add a canonical mapping digest to the Scrub Key

Decision: recommended as a complementary accidental-corruption control.

The digest should cover the canonical reviewed mapping and binding metadata. Import/reinsert recomputes it and rejects a mismatch.

Limits:

- detects accidental edits when the digest is not also updated;
- does not prove authenticity;
- a malicious editor can recompute an unkeyed digest;
- must not be described as a digital signature.

### Option 7 — Sign or HMAC the key

Decision: defer to a later local-runtime security package.

Reason:

- needs protected signing-key creation, storage, backup, rotation and recovery policy;
- the Hugging Face prototype is not a trusted secret-storage environment;
- introducing a hidden server secret would conflict with the local-first direction;
- a signature alone still needs document binding to prove which document the key belongs to.

## 5. Recommended binding contract

### New bound-key contract

A future bound Scrub Key should include at least:

```json
{
  "schema": "solidprivacy.scrub_key",
  "schema_version": "1.1",
  "binding_version": "1",
  "document_binding_id": "K7M4Q9X2...",
  "mapping_digest_algorithm": "sha256",
  "mapping_digest": "...",
  "items": []
}
```

The exact schema version remains an implementation decision, but the contract must not silently reinterpret an existing v1.0 key.

### Placeholder contract

- all generated automatic and manual placeholders for one document carry exactly one binding ID;
- all key items use placeholders carrying that same ID;
- mixed or missing IDs in a bound document are an error;
- the placeholder index and entity label remain readable;
- the binding ID contains no original value, dossier label or source-document hash.

### Reinsert contract

For bound keys:

1. validate the key structure;
2. validate the mapping digest;
3. extract binding IDs from document placeholders;
4. require exactly one document binding ID;
5. require equality with the key binding ID;
6. only then perform deterministic reinsert;
7. preserve unknown, duplicate and not-found audit reporting.

A binding mismatch, mixed binding IDs or invalid digest must produce zero replacements and a clear audit issue.

### Legacy v1.0 contract

- existing unbound keys must not be silently treated as bound;
- dual-read compatibility may remain available during migration;
- legacy reinsert must be visibly labelled `legacy_unbound` or equivalent;
- the interface should warn that document/key matching cannot be verified;
- do not reintroduce repeated source/key confirmation buttons;
- new exports should use the bound format after implementation is app-verified;
- the Phase 6 quality gate must retain the legacy limitation.

## 6. What this does and does not mitigate

| Threat | Binding ID in placeholders | Mapping digest | Signature/HMAC |
| --- | --- | --- | --- |
| Accidental wrong document/key pair | Strong MVP mitigation | No | Can complement |
| Accidental edit of key values | No | Detects | Detects |
| Placeholder removed or translated | Existing audit still needed | No | No |
| Deliberate key edit with digest recomputed | No | No | Detects if signing key is protected |
| Stolen correct Scrub Key | No | No | No |
| Key recovery after loss | No | No | No |

The MVP recommendation reduces accidental mismatch and accidental corruption. It does not solve key leakage, key loss or fully malicious document-and-key manipulation.

## 7. Impacted implementation surfaces

Expected sequential impact includes:

- `document_tools.placeholder_for_entity` and `build_placeholder_replacements`;
- `manual_mask_entry.build_manual_placeholder`;
- candidate/remembered replacement paths that create or preserve placeholders;
- `scrub_key.py` schema/build/validation/serialization;
- Scrub Key export construction in the main app;
- `scrub_key_import.py` compatibility and status reporting;
- `scrub_key_reinsert.py` binding and digest validation;
- TXT/DOCX/PDF-to-TXT reinsert tests;
- review/export copy where bound versus legacy status must be visible;
- fixture manifests and the Phase 6 roundtrip matrix.

These surfaces must be changed sequentially because placeholder generation, export and reinsert semantics are shared.

## 8. Approved next implementation sequence

### 1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`

Test/spec only. Lock:

- bound placeholder grammar;
- one binding ID per document;
- automatic and manual placeholder compatibility;
- schema 1.1 and explicit legacy v1.0 behavior;
- mapping digest canonicalization;
- fail-closed mismatch, mixed-ID and digest-error behavior;
- no additional confirmation gates;
- no cloud, AI or secret storage.

### 2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`

Implement pure helpers only:

- injected local binding-ID generation;
- bound placeholder parsing/building;
- canonical mapping digest;
- dual-version key validation;
- binding validation result model.

No Streamlit integration in this package.

### 3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`

Integrate bound placeholders into automatic/manual replacement creation and Scrub Key export. Preserve review-table authority, legal meaning, output filenames and MIME types. New exports become bound; legacy import remains explicit.

### 4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`

Require binding and digest validation before restoring any value for bound keys. Keep the existing three-step document-first UI and show status without adding redundant buttons or checkboxes.

### 5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Live-test:

- correct bound key succeeds;
- wrong bound key fails before replacement;
- mixed placeholders fail;
- altered digest fails;
- legacy key behavior is explicit;
- TXT, DOCX and PDF-to-TXT boundaries remain intact.

### Optional follow-up

`SCRUB-WP_MVP_MALFORMED_PLACEHOLDER_DIAGNOSTIC_HARDENING` may add a broader bracket-token scanner so malformed near-placeholders are reported directly. It must not guess or repair original values.

## 9. Triage conclusion

The critical finding is valid and cannot be fixed reliably with labels, filenames or content hashes. The smallest cross-format solution that survives normal AI roundtrips is a non-sensitive document binding ID carried inside every placeholder and the corresponding Scrub Key. A canonical mapping digest should complement it for accidental key corruption. Strong malicious-tampering protection requires later signed-key infrastructure and is outside the current web-prototype scope.

No implementation is authorized until the contract-test workpackage is merged and green.
