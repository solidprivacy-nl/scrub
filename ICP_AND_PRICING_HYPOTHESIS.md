# WP51 — ICP and pricing hypothesis

Status: business/design/documentation-only.

Repository: `solidprivacy-nl/scrub`

## 1. Short summary

This document defines a first ICP and pricing hypothesis for SolidPrivacy Scrub after WP50.

The hypothesis compares two early validation tracks:

```text
Scrub Legal — legal teams and legal document workflows.
Scrub Zorg  — care-organization teams and operational document workflows.
```

This is not a sales plan and not a production offer. It is a working hypothesis for interviews, controlled pilots and positioning decisions.

## 2. Assumptions and limits

Current assumptions:

- Scrub is still a risk-driven MVP, not a certified production platform.
- The Hugging Face app is a demo and development surface.
- The intended confidential route is local processing.
- Scrub output requires human review.
- Scrub Key output is pseudonymized and reversible with the key.
- DOCX comments, metadata and hidden parts remain a known product-risk area until the DOCX hygiene line is further integrated.
- PDF support remains text/TXT-only; no OCR and no restored PDF output.
- Residual-risk reports are support tools, not guarantees.

Commercial boundary:

```text
Do not sell full automation, production certification, legal compliance guarantees, medical compliance guarantees, or complete anonymization as current capabilities.
```

## 3. ICP Legal

### Best-fit organization type

The strongest first Legal ICP is likely:

```text
Small to mid-sized Dutch legal teams that frequently prepare confidential documents for AI-assisted review, summarization, drafting or sharing.
```

Potential segments:

- small and mid-sized law firms;
- legal departments;
- legal operations teams;
- privacy/compliance teams with legal document flows.

### User

Likely users:

- lawyer;
- legal assistant;
- paralegal;
- legal operations employee;
- privacy/compliance reviewer.

### Buyer

Likely buyer:

- managing partner;
- legal operations lead;
- head of legal;
- privacy/compliance lead;
- innovation lead.

### Approver or blocker

Likely approver/blocker:

- privacy officer;
- security officer;
- IT lead;
- records/information governance lead;
- professional-risk owner.

### Suitable workflows

Best first workflows:

- preparing legal text for AI support;
- sharing a scrubbed version for review;
- creating safer examples for internal analysis;
- controlled reinsert after AI or review;
- residual-risk discussion before external use.

Avoid as first workflows:

- high-volume batch processing;
- direct production publishing;
- scanned PDF workflows;
- workflows that depend on perfect DOCX hidden-content cleanup.

### Main pain

Legal users need to preserve meaning while reducing exposure of sensitive values. Generic redaction or manual replacement is slow, inconsistent and hard to audit.

### Why they may pay

Willingness-to-pay drivers:

- lower manual review burden;
- safer AI preparation;
- clearer audit trail;
- reversible pseudonymization through Scrub Key;
- better context preservation than blunt redaction;
- local-first direction.

### Sales risks

Hard parts:

- high trust bar;
- fear of missed sensitive values;
- need for local deployment;
- unclear liability expectations;
- current DOCX/PDF limitations;
- buyers may expect full automation too early.

### What a pilot must prove

A Legal pilot must prove:

- user understands the workflow;
- review effort is acceptable;
- output stays readable;
- residual-risk reporting is useful;
- Scrub Key risk is understood;
- current limitations are clear enough.

## 4. ICP Zorg

### Best-fit organization type

The strongest first Zorg ICP is likely:

```text
Dutch care organizations with project, quality, privacy, IT or innovation teams that prepare operational documents for internal analysis, training, supplier conversations or AI support.
```

Potential segments:

- care organizations with privacy/quality teams;
- care-technology project teams;
- functional application management;
- innovation and information-management teams;
- digital transformation teams.

### User

Likely users:

- project manager;
- privacy or quality officer;
- functional application manager;
- policy or support staff;
- innovation staff;
- information-management staff.

### Buyer

Likely buyer:

- manager ICT;
- privacy officer or DPO-adjacent owner;
- quality manager;
- innovation manager;
- operations or transformation lead.

### Approver or blocker

Likely approver/blocker:

- privacy officer;
- security officer;
- ICT management;
- information governance;
- legal/procurement for later production use.

### Suitable workflows

Best first workflows:

- preparing operational documents for internal learning;
- safer AI-assisted summarization of project notes;
- creating controlled training examples;
- sharing scrubbed versions with internal project teams;
- discussing residual-risk reports with privacy/quality staff.

Avoid as first workflows:

- direct processing of production care records;
- unmanaged cloud-demo usage for confidential material;
- high-risk clinical decision workflows;
- large batch processing.

### Main pain

Care organizations have many operational documents with sensitive context. Teams want to use AI and share examples, but privacy review is slow and risk-sensitive.

### Why they may pay

Willingness-to-pay drivers:

- safer internal AI experimentation;
- less manual preparation work;
- better privacy-office confidence;
- local-first route;
- audit and residual-risk language for governance;
- support for training/project examples.

### Sales risks

Hard parts:

- strong need for privacy approval;
- local deployment expectations;
- unclear ownership between ICT, privacy, quality and operations;
- low tolerance for confusing limitations;
- current DOCX hidden-content risk must be explained clearly.

### What a pilot must prove

A Zorg pilot must prove:

- the workflow is understandable for non-legal users;
- local-first direction is credible;
- review effort is acceptable;
- residual-risk reporting helps governance;
- current limitations do not create false confidence.

## 5. Legal vs Zorg comparison

| Dimension | Legal hypothesis | Zorg hypothesis |
|---|---|---|
| First value | AI/share preparation for legal documents | AI/share preparation for operational documents |
| Strongest buyer pain | Meaning-preserving confidentiality control | Privacy-safe internal analysis and learning |
| Trust bar | Very high | High, with governance focus |
| Access path | Harder, more trust-driven | Potentially faster through care-sector network |
| Best first offer | Guided controlled pilot | Guided controlled pilot / workshop |
| Main blocker | liability and professional trust | privacy/security approval and local deployment |
| Likely wedge | legal AI preparation | operational document preparation |

Initial commercial priority hypothesis:

```text
Scrub Zorg may be the fastest validation wedge because the project already has care-sector context and access. Scrub Legal remains a strong product story but may require more trust evidence before conversion.
```

## 6. First buyer personas

### Legal persona A — Managing lawyer / legal owner

- Wants safer AI use without losing legal context.
- Needs trust, control and auditability.
- May pay for risk reduction and workflow efficiency.
- Blocks if the tool sounds like unsupported automatic anonymization.

### Legal persona B — Legal operations / privacy lead

- Wants repeatable process and governance.
- Needs residual-risk language and review evidence.
- May prefer a controlled pilot before buying.

### Zorg persona A — Privacy/quality lead

- Wants safer internal sharing and AI preparation.
- Needs clear boundaries and local processing direction.
- May sponsor a guided pilot if governance is clear.

### Zorg persona B — ICT/project lead

- Wants practical tooling for project and support documents.
- Needs easy local run path and clear support model.
- May become buyer or internal champion.

## 7. Pricing model comparison

| Model | Advantage | Disadvantage | Risk | Best moment |
|---|---|---|---|---|
| Free demo/discovery | Low friction | No revenue signal | Attracts unqualified users | Before pilot |
| Paid pilot | Validates willingness to pay | Requires clear scope | May feel early if product limits are unclear | After demo interest |
| Consultancy-assisted pilot | High trust and learning | Time-intensive | Hard to scale | Best first paid offer |
| Per user per month | Simple SaaS logic | Less aligned with local desktop/security route | May underprice value | Later MVP |
| Per organization per month | Fits governance buyer | Needs support model | Needs mature local deployment | Later pilot/early production |
| Local desktop license | Fits local-first promise | Requires packaging/support | Premature before WP49B or later | After packaging proof |
| Enterprise/support model | Fits larger organizations | Complex sales | Too heavy early | Later only |

## 8. First pricing hypothesis

This is a cautious hypothesis, not a price list.

Suggested bands:

```text
Discovery/demo: free or very low threshold.
Paid controlled pilot: small fixed fee.
Consultancy-assisted pilot: higher fixed fee because guidance and review sessions are included.
Later subscription/license: only after product validation and local deployment proof.
```

Suggested initial direction:

```text
Start with a consultancy-assisted paid pilot rather than a self-serve subscription.
```

Reason:

- product trust is not yet fully proven;
- users need guidance on limitations;
- feedback quality matters more than scale;
- a guided pilot can validate willingness to pay and risk language.

## 9. Pilot offer vs production offer

### Pilot offer

Purpose:

- learn;
- validate workflow value;
- measure review burden;
- collect structured feedback;
- test messaging and trust.

Included:

- controlled document set;
- guided session;
- feedback interview;
- residual-risk discussion;
- no production claim.

### Production offer

Later only.

Requires before offering:

- local runtime confidence;
- document hygiene path;
- clearer support model;
- security/privacy approval material;
- packaging or deployment decision;
- pricing validation.

## 10. What must not be sold or claimed yet

Do not claim:

- production certification;
- full automation;
- full anonymization without review;
- complete DOCX hidden-content handling;
- OCR or restored PDF output;
- guaranteed detection of all sensitive values;
- encrypted Scrub Key container;
- enterprise deployment readiness;
- compliance approval.

Allowed positioning:

```text
A guided, local-first-oriented workflow for controlled document scrubbing validation, with human review, Scrub Key awareness and residual-risk visibility.
```

## 11. Validation questions

Use these in interviews or guided pilots:

1. What document workflow would you want to use Scrub for first?
2. What would make you trust or distrust the output?
3. How much review time is acceptable per document?
4. Which missed items would be unacceptable?
5. Which false positives are annoying but acceptable?
6. Is the Scrub Key concept clear?
7. Do the warnings make the workflow safer or more confusing?
8. Are DOCX/PDF limitations clear enough?
9. Would local processing change your willingness to test or buy?
10. Who would approve a pilot in your organization?
11. Who would block it?
12. What would make you pay for a controlled pilot?
13. What would make you refuse to buy?
14. Would you prefer a guided pilot, desktop license or subscription later?
15. What evidence would you need before production use?

## 12. Go / no-go criteria

The hypothesis gets stronger if:

- users understand the workflow;
- users accept human review;
- users see clear time or risk value;
- users understand limitations;
- users can explain Scrub Key risk back correctly;
- users consider a paid pilot reasonable;
- a clear buyer and approver path emerges.

Pause or revise if:

- users want only automatic anonymization;
- users require immediate production certification;
- users reject local install or controlled pilot constraints;
- DOCX/PDF limitations block the main use case;
- willingness to pay is absent;
- the buyer is unclear.

## 13. Recommended next step

Recommended next workpackage:

```text
WP52 — Pilot intake and NDA process
```

WP52 should define the practical intake and agreement process before any real external pilot activity is started.
