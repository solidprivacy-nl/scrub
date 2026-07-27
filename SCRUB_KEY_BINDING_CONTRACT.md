# SolidPrivacy Scrub — Scrub Key Binding Contract v1

Workpackage: `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`  
Status: contract frozen for model implementation  
Implementation: not included in this package

## Purpose

This contract prevents a structurally valid Scrub Key from being silently applied to the wrong scrubbed document when both use the same generic placeholder names.

The contract covers:

- a non-sensitive document binding ID;
- bound automatic and manual placeholders;
- bound Scrub Key metadata;
- a deterministic mapping digest for accidental corruption;
- explicit legacy-v1.0 behavior;
- fail-closed document/key validation before replacement;
- preservation of the current three-step reinsert UX.

It does not provide encrypted key storage, key recovery or cryptographic authenticity against a malicious editor with control of both document and key.

## 1. Binding ID

### Grammar

```text
B[A-Z2-7]{16}
```

Example:

```text
BK7M4Q2XR5TD3W6YZ
```

Rules:

- the initial `B` identifies a SolidPrivacy binding token;
- the remaining 16 symbols use uppercase RFC 4648 base32 characters `A-Z` and `2-7`;
- the random payload provides at least 80 bits of entropy;
- the ID is generated locally;
- the ID contains no original value, document label, filename or source-document hash;
- the ID is not secret, but is document-specific correlation metadata;
- pure helpers must accept an injected ID so tests remain deterministic.

Invalid examples include lowercase characters, `0`, `1`, `8`, `9`, punctuation, whitespace and the wrong length.

## 2. Bound placeholder grammar

### Automatic placeholder

```text
[<ENTITY_LABEL>_<BINDING_ID>_<INDEX>]
```

Examples:

```text
[PERSOON_BK7M4Q2XR5TD3W6YZ_01]
[DOSSIERNUMMER_BK7M4Q2XR5TD3W6YZ_01]
[IP_ADRES_BK7M4Q2XR5TD3W6YZ_02]
```

### Manual placeholder

```text
[<ENTITY_LABEL>_<BINDING_ID>_HANDMATIG_<INDEX>]
```

Example:

```text
[PERSOON_BK7M4Q2XR5TD3W6YZ_HANDMATIG_01]
```

### Parsing expression

```regex
^\[(?P<label>[A-Z][A-Z0-9_]*?)_(?P<binding_id>B[A-Z2-7]{16})(?:_(?P<manual>HANDMATIG))?_(?P<index>\d{2,})\]$
```

Rules:

- entity labels remain readable and may contain underscores;
- the index is decimal and at least two digits;
- one document uses one binding ID across every automatic and manual placeholder;
- a bound Scrub Key item placeholder must carry the key's top-level binding ID;
- a document containing two or more binding IDs is mixed and must fail closed;
- a bound key applied to a document with only legacy unbound placeholders must fail closed as `missing_document_binding`;
- no parser may guess or repair malformed placeholders.

The existing broad placeholder detector may continue to discover bound tokens, but binding parsing requires the stricter expression above.

## 3. Bound Scrub Key metadata

A bound key uses an explicit new contract. The model implementation should use schema version `1.1`, while retaining explicit dual-read support for structurally valid legacy `1.0` keys.

Required bound fields:

```json
{
  "schema": "solidprivacy.scrub_key",
  "schema_version": "1.1",
  "binding_version": "1",
  "document_binding_id": "BK7M4Q2XR5TD3W6YZ",
  "mapping_digest_algorithm": "sha256",
  "mapping_digest": "516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3",
  "items": []
}
```

Rules:

- `binding_version` is exactly `1`;
- `document_binding_id` matches the binding-ID grammar;
- `mapping_digest_algorithm` is exactly `sha256`;
- `mapping_digest` is 64 lowercase hexadecimal characters;
- every included item placeholder contains the same binding ID;
- `item_count` matches the number of items;
- existing privacy, reversibility, storage, external-AI and excluded-row policies remain required;
- descriptive `document_label` remains optional and is never a security decision input.

## 4. Canonical mapping digest

The digest detects accidental key changes. It is not a signature or authenticity proof.

### Canonical payload

Build exactly this object:

```text
schema
schema_version
privacy_model
reversible
storage_policy
external_ai_policy
excluded_rows_policy
binding_version
document_binding_id
item_count
items
```

For every item, include exactly:

```text
placeholder
original_value
entity_type
include_state
```

Sort items lexicographically by:

```text
placeholder, original_value, entity_type
```

Serialize using UTF-8 JSON with:

```python
json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
```

Then compute:

```python
sha256(serialized_payload.encode("utf-8")).hexdigest()
```

Excluded from the digest:

- `mapping_digest` itself;
- `mapping_digest_algorithm`;
- `workflow`;
- `document_label`;
- `type_label`;
- `source`;
- `review_status`;
- `timestamp`.

These exclusions keep the digest focused on binding and restoration semantics rather than display/audit metadata.

The canonical synthetic fixture digest is:

```text
516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3
```

## 5. Binding validation result

The future pure model helper returns a stable result shape containing at least:

```text
ok
binding_status
replacement_allowed
verified_document_match
legacy_unbound
errors
warnings
document_binding_ids
key_binding_id
mapping_digest_valid
```

Required statuses:

| Status | Replacement allowed | Verified document match | Meaning |
| --- | ---: | ---: | --- |
| `bound_match` | yes | yes | One document ID matches the valid key ID and digest. |
| `legacy_unbound` | yes | no | Valid v1.0 key/document; compatibility only, with warning. |
| `binding_mismatch` | no | no | One document binding ID differs from the key. |
| `mixed_document_bindings` | no | no | More than one binding ID is present. |
| `missing_document_binding` | no | no | Bound key, but no bound placeholder is present. |
| `invalid_mapping_digest` | no | no | Recomputed digest differs from key. |
| `invalid_bound_key` | no | no | Bound-key metadata or item binding is invalid. |
| `legacy_key_for_bound_document` | no | no | A legacy key is supplied for a bound document. |

Fail-closed statuses must produce zero replacements. No partial restoration may occur before binding validation succeeds.

## 6. Legacy v1.0 contract

A structurally valid v1.0 key remains readable during migration, but is explicitly unbound.

Rules:

- status is `legacy_unbound`;
- `verified_document_match` is false;
- a clear warning states that document/key matching cannot be verified;
- no new hidden confirmation button or checkbox is introduced;
- the existing final confidential-download acknowledgement remains;
- a legacy key must not be applied to bound placeholders;
- a v1.0 key is not silently upgraded or assigned a fabricated binding ID;
- new bound exports will use the new contract after implementation and app verification.

## 7. UX contract

The visible workflow remains:

```text
1. Upload source document or paste text
2. Upload the corresponding Scrub Key
3. Download the restored result
```

Binding validation happens automatically after step 2.

Requirements:

- no additional source/key execution button;
- no additional source/key acknowledgement checkbox;
- binding status and errors remain visible;
- bound mismatch prevents output generation;
- one final confidentiality acknowledgement remains immediately before download;
- existing TXT, DOCX and PDF-to-TXT boundaries remain visible;
- filenames and MIME types are not changed by the model package.

## 8. Pure helper API expected from the model package

The next implementation package should provide pure, Streamlit-free helpers with these responsibilities. Exact internal decomposition may vary, but the public behavior and result fields are fixed by this contract.

```python
validate_document_binding_id(value) -> list[str]
build_bound_placeholder(entity_label, index, document_binding_id, manual=False) -> str
parse_bound_placeholder(token) -> dict | None
canonical_mapping_digest_payload(scrub_key) -> dict
compute_mapping_digest(scrub_key) -> str
validate_bound_scrub_key(scrub_key) -> dict
validate_document_key_binding(text, scrub_key) -> dict
```

The helpers must not:

- call Streamlit;
- access the network;
- call AI services;
- write files;
- persist secrets;
- derive IDs from personal data;
- guess or repair malformed placeholders.

## 9. Implementation gate

Model implementation may start only when the contract fixture and contract tests are green.

This contract does not authorize:

- export integration;
- reinsert integration;
- UI changes;
- automatic migration of legacy keys;
- signing/HMAC infrastructure;
- production-readiness claims.
