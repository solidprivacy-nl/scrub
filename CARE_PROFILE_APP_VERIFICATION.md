# Zorgfilter v1 — deployed app verification

Status: completed and app-verified after technical deployment verification.

## Technical evidence

An independent GitHub Actions check compared the relevant GitHub `main` files with the files in Hugging Face Space `solidprivacy/scrub`.

```text
Files compared byte-for-byte: 12
Exact matches:               12/12
Correctly scoped markers:    all passed
Space health:                HTTP 200 / ok
Space root:                  HTTP 200
Technical deployment:        verified
```

Evidence:

```text
output/validation/care_profile_hf_sync_verification.json
```

The first verification attempt produced a false negative because two marker checks looked for labels in the wrong modules. The byte hashes were already equal. The corrected check moved those markers to `recognition_profiles.py` and `review_status.py` and passed all exact-file, marker and health gates.

## Coordinator/user verification

Open:

```text
https://solidprivacy-scrub.hf.space/
```

Use only the built-in synthetic examples.

### A. Profile selector

Confirm:

- four profile choices are visible;
- their order is:
  1. `Zorgcontrole — streng`;
  2. `Juridische controle — streng`;
  3. `Algemene Nederlandse controle`;
  4. `Algemene internationale controle`;
- `Juridische controle — streng` is selected initially;
- switching profiles never happens silently.

### B. Care profile content

Select `Zorgcontrole — streng` and confirm:

- the description mentions patient/client identifiers, EPD/ECD or dossier references, care providers, organizations, locations and exact care dates;
- the description says diagnosis, medication, dosage, laboratory values and observations should remain readable;
- an expander for a synthetic care example is visible;
- the example selector contains eight care examples.

### C. Review policy

Load a synthetic care example containing both patient identity and review-selected context. Confirm:

- patient/client identifiers are included for replacement;
- care-provider, organization, location, room/bed or exact care-date detections remain selected but show `Controle nodig`;
- labels and professional roles remain readable;
- diagnosis, medication, dosages, laboratory values and observations are not blindly replaced;
- possible unresolved administrative care-reference candidates are unchecked.

### D. Existing profiles and workflow

Confirm:

- Legal, General Dutch and International profiles remain selectable;
- the side-by-side review and replacement table remain available;
- export/download remains available;
- the Scrub Key flow remains available;
- `Originele waarden terugzetten` remains available;
- no Script execution error is visible.

## Verification result

Coordinator/user confirmation received at `2026-08-03 20:35 Europe/Amsterdam`:

```text
alles groen
```

Confirmed visible behavior:

- four profiles are visible in the approved order;
- Legal remains the initial default;
- the Care description and eight synthetic examples are present;
- patient/client identifiers are selected for replacement;
- review-selected care context remains selected and shows `Controle nodig`;
- unresolved care-reference candidates remain unchecked;
- clinical meaning remains readable;
- Legal, General, International, review, export, Scrub Key and reinsert remain present;
- no Script execution error is visible.

## Closeout rule

The coordinator/user confirmed all visible checks. The package is completed and app-verified. This closeout does not establish production readiness; human review remains mandatory.
