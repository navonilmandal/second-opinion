# National Insurance — Comprehensive Health Insurance Policy

> **PROTOTYPE / SYNTHETIC DOCUMENT**
>
> This document is mock data created exclusively for development and demonstration of the Insurance Policy Review prototype.
>
> It is **not an actual National Insurance policy**, does not represent official policy wording, and must not be used for purchasing, underwriting, claims, legal, or financial decisions.
>
> Company-level metrics are seeded from the prototype dataset. All policy clauses, coverage terms, exclusions, waiting periods, limits, claim conditions, and other policy wording in this document are synthetic.

---

# Policy Information

| Field | Value |
|---|---|
| Policy ID | `national_insurance_seed` |
| Provider | National Insurance |
| Policy Type | Comprehensive Health Insurance |
| Document Type | Synthetic Policy Wording |
| Version | `PROTOTYPE-1.0` |
| Effective Date | 01 April 2026 |
| Jurisdiction | India |
| Currency | INR |
| Document Status | Synthetic / Prototype |

---

# 1. Policy Overview

This synthetic policy represents a prototype comprehensive health insurance product covering eligible medical expenses incurred during the policy period.

Coverage is subject to the applicable sum insured, waiting periods, exclusions, sub-limits, deductibles, co-payments, claim procedures, and other conditions described in this document.

The insurer may request medical, financial, and other supporting documentation reasonably required to assess a claim.

---

# 2. Key Policy Metrics

The following figures are **prototype dataset metrics** and are not presented as official current product pricing or performance information.

| Metric | Prototype Value |
|---|---:|
| Indicative Annual Premium | ₹7,938 |
| Hidden Charge Count | 0 |
| Claim Settlement Metric | 96.05% |
| Estimated Claim Volume | 316,634 |
| Prototype Complaint Rate | 1.87 |
| Sample Count | 1 |
| Data Granularity | company |
| Settlement Metric Status | REAL / SOURCE-REFERENCED |
| Other Metrics | PLACEHOLDER / SYNTHETIC |

### Data Quality Notice

The dataset marks the claim-settlement metric as real/source-referenced from the IRDAI FY24-25 Annual Report. Premium, hidden-charge count, complaint rate, and claim volume are marked as placeholder or estimated values.

The application should expose these statuses rather than treating every metric as equally verified.

---

# 3. Coverage

Subject to the policy conditions, eligible benefits may include:

- In-patient hospitalization.
- Day-care procedures.
- Medically necessary treatment.
- Eligible diagnostic investigations.
- Pre-hospitalization expenses.
- Post-hospitalization expenses.
- Emergency medical treatment.
- Eligible surgical procedures.
- Other benefits specifically listed in the applicable policy schedule.

Coverage remains subject to applicable limits and exclusions.

---

# 4. Hospitalization

Hospitalization expenses may be covered where treatment is medically necessary and otherwise eligible under the policy.

The insured may be required to provide:

- Admission records.
- Discharge summary.
- Medical reports.
- Prescriptions.
- Diagnostic reports.
- Itemized hospital bills.
- Payment receipts.
- Other documents reasonably required for claim assessment.

The total hospital bill does not automatically determine the amount payable by the insurer.

> **AI REVIEW FLAG — MEDIUM**
>
> Users should distinguish between the total amount billed and the amount that qualifies under the policy.

**Risk category:** `claim_expectation`

---

# 5. Room and Accommodation Limits

The policy may specify an eligible room category or accommodation limit.

Selecting accommodation above the applicable limit may result in deductions under the policy terms. Where proportionate deductions apply, associated medical expenses may also be affected.

The exact room limit must be verified against the applicable policy schedule.

> **AI REVIEW FLAG — HIGH**
>
> A room-category restriction can potentially increase out-of-pocket exposure beyond the difference in room price.

**Risk category:** `coverage_limit`

---

# 6. Waiting Periods

Certain conditions, treatments, or procedures may be subject to waiting periods.

Waiting periods may apply to:

- Pre-existing diseases.
- Specified illnesses.
- Certain planned procedures.
- Other benefits identified in the policy schedule.

A claim submitted during an applicable waiting period may not be payable.

The exact duration must be verified against the applicable policy schedule.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `waiting_period`

---

# 7. Pre-Existing Diseases

A pre-existing disease refers to a medical condition existing before commencement of coverage, subject to the applicable policy definition.

Coverage for such conditions may be subject to a waiting period.

The insured should disclose relevant medical history accurately during proposal and underwriting.

Material non-disclosure or inaccurate information may affect claim assessment where permitted by the policy terms and applicable law.

---

# 8. Treatment-Specific Sub-Limits

Certain treatments or benefits may have separate monetary limits.

A sub-limit may apply even when the overall sum insured remains available.

Users should review treatment-specific, procedure-specific, accommodation, diagnostic, and other benefit limits in the applicable schedule.

> **AI REVIEW FLAG — HIGH**
>
> A large overall sum insured does not necessarily mean unlimited reimbursement for every individual treatment.

**Risk category:** `coverage_limit`

---

# 9. Co-Payment

A co-payment may apply to specified treatments, benefits, policy configurations, or insured categories.

Where a co-payment applies, the insured must bear the specified portion of an otherwise eligible claim.

For illustration only, on a ₹100,000 eligible claim with a 20% co-payment:

- Insurer portion: ₹80,000
- Insured portion: ₹20,000

The actual co-payment must be verified from the applicable policy schedule.

---

# 10. Deductibles

A deductible may apply depending on the selected policy configuration.

The insured must bear the deductible amount before the insurer becomes liable for the remaining eligible expenses, subject to the applicable terms.

The deductible structure may be defined per claim, per policy period, or under another applicable arrangement.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `out_of_pocket_cost`

---

# 11. Non-Medical Expenses

Certain hospitalization-related expenses may not qualify as covered medical expenses.

Potential examples include:

- Personal-use items.
- Administrative charges.
- Convenience items.
- Certain consumables.
- Other expenses specifically excluded by the policy.

These amounts may remain payable by the insured.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `out_of_pocket_cost`

---

# 12. Cashless Treatment

Cashless treatment may be available at eligible network hospitals subject to authorization.

Cashless authorization does not necessarily mean every expense incurred during hospitalization will be paid.

Final claim liability remains subject to coverage, exclusions, waiting periods, sub-limits, deductibles, co-payments, medical necessity, and supporting documentation.

> **AI REVIEW FLAG — HIGH**
>
> "Cashless" should not be interpreted as "fully covered."

**Risk category:** `claim_expectation`

---

# 13. Pre-Authorization

For planned hospitalization, prior authorization may be required where applicable.

Authorization may be based on information available at the time of request and does not necessarily constitute final approval of every expense.

The final claim may be assessed after complete documentation is received.

---

# 14. Emergency Hospitalization

In an emergency, the insured should notify the insurer or applicable claims administrator as soon as reasonably practicable.

The insurer may request information relating to the emergency, diagnosis, treatment, admission, medical necessity, and expenses incurred.

---

# 15. Reimbursement Claims

Where cashless treatment is not used, the insured may submit a reimbursement claim.

Supporting documents may include:

1. Claim form.
2. Hospital bills.
3. Discharge summary.
4. Medical reports.
5. Prescriptions.
6. Diagnostic reports.
7. Payment receipts.
8. Other supporting documentation.

Additional information may be requested where reasonably necessary.

---

# 16. Claim Documentation

The insured should retain relevant documentation supporting treatment and expenses.

Incomplete documentation may require additional verification.

The insured may be asked to clarify diagnosis, treatment, expenses, medical necessity, payment, or relevant medical history.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `claim_procedure`

---

# 17. Medical Necessity

Treatment may need to satisfy the applicable definition of medical necessity to qualify for coverage.

The insurer may assess whether treatment was appropriate, clinically required, provided at an appropriate level of care, and within covered benefits.

A medical invoice alone does not establish that the entire amount is payable.

---

# 18. Exclusions

Potential exclusions may include:

- Treatment during an applicable waiting period.
- Certain pre-existing conditions during their applicable waiting period.
- Cosmetic treatment not medically necessary.
- Experimental or unproven treatment.
- Non-medical expenses.
- Expenses exceeding applicable sub-limits.
- Treatment outside insured benefits.
- Other exclusions specifically stated in the policy schedule.

The complete exclusion section should be reviewed for any particular treatment.

---

# 19. Cosmetic Treatment

Treatment primarily undertaken for aesthetic purposes may not be covered.

An exception may apply where treatment is medically necessary due to a covered condition or accidental injury and otherwise eligible.

Supporting medical evidence may be required.

---

# 20. Experimental or Unproven Treatment

Experimental, investigational, or unproven treatments may be excluded unless specifically recognized as covered.

The insurer may request clinical or medical documentation supporting the treatment.

The existence of a medical expense does not automatically establish coverage.

---

# 21. Fraud and Misrepresentation

A claim containing materially false information, fabricated documents, or fraudulent representations may be rejected in accordance with applicable policy terms and law.

The insurer may investigate circumstances where fraud or material misrepresentation is suspected.

---

# 22. Policy Renewal

The policy may be renewed subject to applicable renewal terms.

At renewal, the policyholder should review premium, sum insured, benefits, waiting periods, exclusions, sub-limits, co-payment, deductibles, network hospital availability, and other policy conditions.

A renewed policy should not automatically be assumed to have identical terms to the previous version.

---

# 23. Cancellation

Cancellation is subject to applicable policy terms.

Any refund may depend on time elapsed, claims already made, cancellation provisions, regulatory requirements, and other applicable conditions.

---

# 24. Consumer Review Checklist

Before purchasing or relying on this policy, a user should review:

- Total premium.
- Sum insured.
- Waiting periods.
- Pre-existing disease conditions.
- Room-category limits.
- Treatment-specific sub-limits.
- Co-payment.
- Deductibles.
- Exclusions.
- Non-medical expenses.
- Cashless network.
- Claim notification requirements.
- Reimbursement documentation.
- Renewal conditions.
- Cancellation and refund conditions.

---

# 25. Prototype Risk Signals

## Risk Signal 1 — Room Category / Proportionate Deduction

**Risk Level:** High

A room-category restriction may affect associated medical expenses if proportionate deductions apply.

**Category:** `coverage_limit`

## Risk Signal 2 — Waiting Period

**Risk Level:** Medium

Certain conditions may not be covered until an applicable waiting period has been completed.

**Category:** `waiting_period`

## Risk Signal 3 — Treatment-Specific Sub-Limits

**Risk Level:** High

Individual treatments may have limits separate from the overall sum insured.

**Category:** `coverage_limit`

## Risk Signal 4 — Cashless Does Not Mean Fully Covered

**Risk Level:** High

Cashless authorization does not guarantee payment of every expense.

**Category:** `claim_expectation`

## Risk Signal 5 — Out-of-Pocket Exposure

**Risk Level:** Medium

Co-payments, deductibles, non-medical expenses, and sub-limits may increase the insured's financial contribution.

**Category:** `out_of_pocket_cost`

## Risk Signal 6 — Claim Documentation

**Risk Level:** Medium

Reimbursement claims may require multiple supporting documents.

**Category:** `claim_procedure`

---

# 26. Prototype Policy Score Inputs

```yaml
policy_id: national_insurance_seed
provider: National Insurance

metrics:
  premium:
    value: 7938
    currency: INR
    status: PLACEHOLDER

  hidden_charges_count:
    value: 0
    status: PLACEHOLDER

  claim_settlement_pct:
    value: 96.05
    status: REAL_SOURCE_REFERENCED

  claim_volume:
    value: 316634
    status: ESTIMATED_TIER

  complaint_rate:
    value: 1.87
    status: PLACEHOLDER

  n_samples:
    value: 1

data_source:
  claim_settlement_pct: "IRDAI Annual Report 2024-25, company-wise Incurred Claim Ratio (health segment)"

granularity: company
```

---

# 27. AI Analysis Metadata

```yaml
document_id: national_insurance_seed_policy_v1
policy_id: national_insurance_seed
provider: National Insurance
policy_category: health
document_type: synthetic_policy
document_version: PROTOTYPE-1.0
jurisdiction: IN
language: en
synthetic: true
source_type: prototype_generated
source_authority: none

analysis_categories:
  - exclusions
  - waiting_periods
  - coverage_limits
  - room_rent
  - sub_limits
  - co_payment
  - deductibles
  - claim_procedure
  - out_of_pocket_cost
  - cashless_claims
  - reimbursement
  - renewal
  - cancellation

risk_categories:
  - high
  - medium
  - low
```

---

# 28. Prototype Disclaimer

This document is synthetic mock data created for demonstrating:

- Full-document ingestion.
- PDF/DOCX-to-text extraction.
- Clause segmentation.
- Vector embedding.
- Retrieval-augmented generation.
- Clause-level risk detection.
- Evidence mapping.
- Policy-level scoring.
- Document highlighting.
- Browser-extension analysis.

It must not be interpreted as an actual insurance contract or as a representation of the terms offered by National Insurance.

For production deployment, this synthetic document must be replaced or supplemented with verified policy documents and authoritative sources.

---

# End of Synthetic Policy Document
