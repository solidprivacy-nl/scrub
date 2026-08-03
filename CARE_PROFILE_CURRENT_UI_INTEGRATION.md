# Zorgfilter v1 — current Streamlit integration

Status: implemented and regression-tested; merge, deployment sync and live app verification pending.

## User-visible result

The current Streamlit prototype gains a fourth recognition profile:

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

The existing three labels keep their relative order. `Juridische controle — streng` remains the initial default selection; the Care profile never activates silently.

The Care profile:

- registers sixteen dedicated, context-bound care recognizers;
- combines general Dutch identity recognition with care-specific entities;
- excludes legal-only entities from the default Care selection;
- applies exact-span precedence such as AGB over BSN and dedicated care entities over broad legacy categories;
- offers eight fully synthetic care examples;
- shows unresolved, strongly labelled administrative care references as unchecked review candidates;
- marks provider, organization, location, room/bed and exact care-date detections as `Controle nodig` while leaving them selected by default;
- keeps patient/client identity and patient-specific administrative references selected for replacement.

## Clinical-context boundary

Zorgfilter v1 is not a generic medical-word filter. Its dedicated rules and candidate layer do not scan diagnosis, medication, dosage, laboratory values, vital signs or free clinical observations as identifiers.

Rare-case indirect identification remains a residual-risk/audit concern. It is not blindly masked.

## Unchanged workflow semantics

This integration does not change:

- replacement-table source-of-truth behavior;
- export filenames, MIME types or document formats;
- Scrub Key schema, binding or warning semantics;
- TXT, DOCX or PDF-to-TXT reinsert behavior;
- DOCX document-processing scope;
- cloud-processing boundaries or dependencies.

Human review remains mandatory. Synthetic tests and prototype verification do not establish production readiness.

## Validation

GitHub Actions run `#1877` passed with `983 tests` after isolating the analyzer-registration test from optional Streamlit/OpenAI UI dependencies.

The next gates are:

1. final clean regression run after governance finalization;
2. merge and GitHub-to-Hugging-Face sync;
3. cross-profile regression matrix;
4. deployed app verification.
