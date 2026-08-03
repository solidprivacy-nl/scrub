# Zorgfilter — long-form synthetic care corpus

Workpackage: `SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS`

## Goal

Give testers enough realistic care context to assess readability, recognition, review status and preservation of clinical meaning. The eight existing synthetic examples remain the stable corpus, but their visible document bodies become substantially longer and more structured.

## Stable document families

1. VVT daily nursing report.
2. Disability-care plan and evaluation.
3. Hospital-to-community nursing transfer.
4. Medical-specialist discharge letter.
5. General-practice referral to cardiology.
6. Pharmacy medication overview.
7. Clinical chemistry laboratory report.
8. VVT medication-incident report.

## Long-form contract

Each visible example must:

- retain its current stable ID, name, sector and document type;
- retain every existing replace, review-selected, preserve, audit-only and ambiguity-trap value;
- contain at least 250 words in total;
- add five document-type-specific section headings;
- provide realistic observations, assessment, care actions and follow-up context;
- expose the same expanded text through the existing Zorgfilter example selector.

## Privacy boundary

The added narrative contains no new:

- personal names;
- patient, client, dossier, referral, insurance, laboratory or incident numbers;
- dates or clock times;
- addresses or postcodes;
- telephone numbers or e-mail addresses;
- named providers, organizations, departments, rooms or locations.

The additions contain no digits. This keeps the current exact identifier and recognizer contracts stable while making the documents more useful for testing.

## Product boundaries

This package changes example content only. It does not change:

- recognition patterns or profile composition;
- confidence thresholds or collision precedence;
- review-selection policy;
- replacement-table behavior;
- export filenames, formats or MIME types;
- Scrub Key schema, binding or warnings;
- reinsert behavior;
- cloud processing, runtime dependencies or production-readiness claims.

Human review remains mandatory.

## Verification

Required gates:

1. Long-form corpus contract tests.
2. Existing care corpus, recognizer and cross-profile tests.
3. Full GitHub Actions regression.
4. GitHub-to-Hugging-Face synchronization.
5. Coordinator/user app verification that the eight visible care examples are materially longer, structured and readable without a Script execution error.
