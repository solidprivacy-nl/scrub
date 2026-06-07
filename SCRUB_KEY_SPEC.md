# Scrub Key Specification — v13.0 pure model

## Purpose

A Scrub Key is a local mapping file that records which original values were replaced by which placeholders during the Scrub review workflow.

It prepares the future workflow:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The v13.0 scope is specification and pure model only. It does not add UI controls, export buttons, reinsert UI, cloud processing, or persistent storage.

## Core concept

A Scrub Key makes scrubbed text reversible when the key is available. This means the Scrub Key supports pseudonymization, not full anonymization.

The scrubbed document and the Scrub Key must be treated as separate security objects:

- the scrubbed document may be suitable for external processing after human review;
- the Scrub Key contains the mapping needed to restore sensitive values;
- the Scrub Key must stay local and protected;
- users should not share the key with external AI services unless explicitly intended and allowed by their policy, client instruction, and legal basis.

## Safety position

A Scrub Key is powerful because it can restore original terms. That also makes it sensitive.

Required user-facing safety language for future UI work:

```text
Een Scrub Key maakt deze tekst omkeerbaar. Dit is pseudonimisering, geen volledige anonimisering. Bewaar de sleutel lokaal en beveiligd. Deel de Scrub Key niet met externe AI-diensten, tenzij dit bewust is bedoeld en toegestaan.
```

Scrub Key export/import must not silently change document meaning. Future import and reinsert steps must preserve the exact reviewed mapping and should warn if a placeholder is missing, duplicated, ambiguous, or changed in the AI output.

## Mapping item fields

Each mapping item supports these fields:

| Field | Required | Meaning |
| --- | --- | --- |
| `original_value` | yes | The original sensitive value before replacement. |
| `placeholder` | yes | The placeholder that replaced the original value. |
| `entity_type` | yes | The stable technical entity type. |
| `type_label` | yes | The user-facing type label shown to the reviewer. |
| `source` | yes | Source of the row, for example detected, candidate, manual, or remembered. |
| `review_status` | yes | Review status at key-build time. |
| `include_state` | yes | Whether this item is included in the key. v13.0 emits included rows only. |
| `timestamp` | yes | Timestamp supplied by the reviewed row. The pure model does not create time itself. |
| `document_label` | optional | Optional document, project, dossier, or matter label. |

## v13.0 excluded-row policy

The v13.0 pure model uses this policy:

```text
excluded_rows_policy = omitted
```

Only rows explicitly selected for inclusion are written into the Scrub Key. Excluded rows are omitted rather than exported as inactive mappings. This keeps the first model aligned with current export semantics: unchecked rows are not part of the output mapping.

A later version may add an explicit audit mode that records excluded rows separately, but that is outside this workpackage.

## Determinism and timestamp rule

The pure model is deterministic. It does not call the system clock.

If a timestamp is needed, it must be supplied by the caller in the reviewed row. Validation reports an empty or missing timestamp as an issue. This avoids hidden side effects and makes tests stable.

## JSON shape

A Scrub Key is a JSON object with metadata and an `items` list.

Example using synthetic Dutch legal values only:

```json
{
  "schema": "solidprivacy.scrub_key",
  "schema_version": "1.0",
  "workflow": "Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit",
  "privacy_model": "pseudonymization_not_full_anonymization",
  "reversible": true,
  "storage_policy": "local_only_protect_key",
  "external_ai_policy": "do_not_share_key_unless_explicitly_intended_and_allowed",
  "excluded_rows_policy": "omitted",
  "document_label": "Dossier voorbeeld",
  "item_count": 1,
  "items": [
    {
      "original_value": "BETROKKENE-TEST-A",
      "placeholder": "[PERSOON_1]",
      "entity_type": "PERSON",
      "type_label": "Naam",
      "source": "detected",
      "review_status": "auto_detected",
      "include_state": "included",
      "timestamp": "2026-06-07T10:00:00Z",
      "document_label": "Dossier voorbeeld"
    }
  ]
}
```

## Pure helper API

The initial pure helper module is `scrub_key.py`.

Supported functions:

```python
build_scrub_key(rows, document_label=None) -> dict
scrub_key_to_json(scrub_key) -> str
scrub_key_from_json(text) -> dict
validate_scrub_key(scrub_key) -> list[str]
```

The helpers accept dictionaries, lists of dictionaries, and DataFrame-like objects with `to_dict(orient="records")`. They do not import Streamlit or pandas.

## Non-goals for v13.0

This specification/model does not add:

- Streamlit UI integration;
- export/download buttons;
- reinsert UI;
- cloud processing;
- secret storage;
- real personal data examples;
- encrypted vault/storage;
- document-meaning transformation;
- AI output parsing.

## Future phases

Planned follow-up work can build on this model:

1. Scrub Key JSON export UI.
2. Scrub Key import/reload.
3. Local reinsert of AI output.
4. Pseudonymization warnings in the UI.
5. Audit logging around export/import and reinsertion.
