# HDFC ERGO General Insurance — Comprehensive Health Insurance Policy

> **PROTOTYPE / SYNTHETIC DOCUMENT**
>
> This document is mock data created exclusively for development and demonstration of the Insurance Policy Review prototype.
>
> It is **not an actual HDFC ERGO General Insurance policy**, does not represent official policy wording, and must not be used for purchasing, underwriting, claims, legal, or financial decisions.
>
> Company-level metrics in this document are seeded from the prototype dataset. Policy clauses, coverage terms, exclusions, waiting periods, limits, claim conditions, and other policy wording are synthetic.

---

# Policy Information

| Field | Value |
|---|---|
| Policy ID | `hdfc_ergo_seed` |
| Provider | HDFC Ergo General Insurance |
| Policy Type | Comprehensive Health Insurance |
| Document Type | Synthetic Policy Wording |
| Version | `PROTOTYPE-1.0` |
| Effective Date | 01 April 2026 |
| Jurisdiction | India |
| Currency | INR |
| Document Status | Synthetic / Prototype |

---

# 1. Policy Overview

This synthetic policy provides a prototype representation of comprehensive health insurance coverage for eligible medical expenses incurred during the policy period.

Coverage is subject to the applicable sum insured, waiting periods, exclusions, sub-limits, deductibles, co-payments, claim procedures, and other conditions described in this document.

The insurer may request documentation reasonably required to determine whether a claim is covered and the amount payable.

---

# 2. Key Policy Metrics

The following figures are **prototype dataset metrics** and are not presented as official current product pricing or performance information.

| Metric | Prototype Value |
|---|---:|
| Indicative Annual Premium | ₹16,594 |
| Hidden Charge Count | 2 |
| Claim Settlement Metric | 84.85% |
| Estimated Claim Volume | 60,985 |
| Prototype Complaint Rate | 7.01 |
| Sample Count | 1 |
| Data Granularity | company |
| Settlement Metric Status | REAL / SOURCE-REFERENCED |
| Other Metrics | PLACEHOLDER / SYNTHETIC |

### Data Quality Notice

The prototype dataset identifies the claim-settlement metric as sourced from the IRDAI FY24-25 Annual Report, while premium, hidden-charge count, complaint rate, and claim volume are marked as placeholder or estimated values.

The application must therefore distinguish verified/source-referenced metrics from synthetic prototype metrics.

---

# 3. Coverage

Subject to the policy conditions, eligible coverage may include:

- In-patient hospitalization.
- Day-care procedures.
- Medically necessary treatment.
- Eligible diagnostic investigations.
- Pre-hospitalization expenses.
- Post-hospitalization expenses.
- Emergency medical treatment.
- Eligible surgical procedures.
- Other benefits specifically listed in the applicable policy schedule.

Coverage is subject to the sum insured and any applicable limits.

---

# 4. Hospitalization

Hospitalization expenses may be covered when the treatment is medically necessary and falls within the scope of the policy.

The insured may be required to provide:

- Hospital admission records.
- Discharge summary.
- Medical reports.
- Prescriptions.
- Diagnostic reports.
- Itemized bills.
- Payment receipts.
- Other documents reasonably required for claim assessment.

The presence of a hospital bill does not by itself establish that every billed item is covered.

> **AI REVIEW FLAG — MEDIUM**
>
> Users should distinguish between the total amount billed by a hospital and the amount that is actually payable under the insurance policy.

---

# 5. Room Category and Accommodation Limits

The policy may define an eligible room category or accommodation limit.

If the insured selects accommodation above the eligible limit, the insurer may apply applicable deductions to room-related expenses and, where the policy provides for it, proportionate deductions to associated medical expenses.

The precise room category limit must be verified against the applicable policy schedule.

> **AI REVIEW FLAG — HIGH**
>
> This is an important prototype risk signal because a room-category restriction can potentially affect the final payable claim beyond the difference in room price.

**Risk category:** `coverage_limit`

---

# 6. Waiting Periods

Certain conditions, treatments, or procedures may be subject to waiting periods.

Waiting periods may apply to:

- Pre-existing diseases.
- Specified illnesses.
- Certain planned procedures.
- Other treatments identified by the applicable plan.

A claim submitted before completion of an applicable waiting period may not be payable.

The exact duration of each waiting period must be checked against the applicable policy schedule.

> **AI REVIEW FLAG — MEDIUM**
>
> Users may assume that coverage begins immediately for all medical conditions. Waiting-period provisions can materially affect whether a treatment is covered.

**Risk category:** `waiting_period`

---

# 7. Pre-Existing Diseases

A pre-existing disease is a medical condition that existed before the commencement of coverage, subject to the definition applicable to the policy.

Coverage for such conditions may be subject to an applicable waiting period.

The insured is expected to provide accurate information during proposal and underwriting.

Material non-disclosure or inaccurate information may affect claim assessment where permitted under the applicable terms and law.

---

# 8. Co-Payment

A co-payment may apply to specified benefits, treatments, policy configurations, or insured categories.

Where a co-payment applies, the insured must bear the specified portion of an otherwise eligible claim.

For illustration only:

If an eligible claim is ₹100,000 and the applicable co-payment is 20%:

- Insurer portion: ₹80,000
- Insured portion: ₹20,000

The actual co-payment applicable to a policy must be verified from its schedule.

---

# 9. Deductibles

A deductible may apply depending on the selected policy configuration.

A deductible represents an amount that the insured must bear before the insurer becomes liable for the remaining eligible expenses.

The deductible may operate per claim, per policy period, or according to the applicable product terms.

> **AI REVIEW FLAG — MEDIUM**
>
> A deductible can materially reduce the amount payable by the insurer even where the underlying treatment is otherwise covered.

**Risk category:** `out_of_pocket_cost`

---

# 10. Sub-Limits

Certain treatments or benefits may have monetary sub-limits.

A sub-limit may restrict the maximum amount payable for a particular category of treatment even when the overall sum insured has not been exhausted.

Examples of categories that may have separate limits include:

- Specific procedures.
- Certain diagnostic treatments.
- Accommodation.
- Particular medical benefits.
- Other categories identified in the policy schedule.

The existence of a large overall sum insured should therefore not automatically be interpreted as unlimited coverage for every individual treatment.

> **AI REVIEW FLAG — HIGH**

**Risk category:** `coverage_limit`

---

# 11. Non-Medical Expenses

Certain expenses incurred during hospitalization may not qualify as covered medical expenses.

Potential examples include:

- Personal-use items.
- Administrative charges.
- Convenience items.
- Certain consumables.
- Other expenses specifically excluded by the policy.

Such amounts may remain payable by the insured.

> **AI REVIEW FLAG — MEDIUM**
>
> Small excluded expenses can accumulate and increase the insured's final out-of-pocket amount.

**Risk category:** `out_of_pocket_cost`

---

# 12. Cashless Treatment

Cashless treatment may be available at eligible network hospitals subject to authorization.

Cashless authorization does not necessarily mean that every expense incurred during hospitalization will be paid.

Final claim liability remains subject to:

- Policy coverage.
- Exclusions.
- Waiting periods.
- Sub-limits.
- Deductibles.
- Co-payments.
- Medical necessity.
- Supporting documentation.

> **AI REVIEW FLAG — HIGH**
>
> "Cashless" should not be interpreted as "fully covered."

**Risk category:** `claim_expectation`

---

# 13. Pre-Authorization

For planned hospitalization, the insured may be required to obtain prior authorization where applicable.

Authorization may be based on information available at the time of the request.

Approval for cashless treatment does not necessarily constitute final approval of every expense incurred during treatment.

The final claim may be assessed after submission of complete documentation.

---

# 14. Emergency Hospitalization

In an emergency, the insured should notify the insurer or applicable claims administrator as soon as reasonably practicable.

The insurer may request supporting information concerning:

- The emergency.
- Diagnosis.
- Treatment.
- Admission.
- Medical necessity.
- Expenses incurred.

Failure to follow applicable notification requirements may result in additional claim review.

---

# 15. Reimbursement Claims

Where cashless treatment is not used, the insured may submit a reimbursement claim subject to the policy requirements.

Supporting documents may include:

1. Claim form.
2. Hospital bills.
3. Discharge summary.
4. Medical reports.
5. Prescriptions.
6. Diagnostic reports.
7. Payment receipts.
8. Other supporting documents.

The insurer may request additional information when reasonably necessary to assess the claim.

---

# 16. Claim Documentation

The insured should retain relevant documentation for the duration necessary to support the claim.

Incomplete documentation may require additional verification.

Where requested documents are unavailable, the claim may require additional assessment before a final decision can be made.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `claim_procedure`

---

# 17. Medical Necessity

Treatment must satisfy the applicable definition of medical necessity to qualify for coverage.

The insurer may review whether:

- The treatment was appropriate for the diagnosed condition.
- The treatment was clinically required.
- The level of care was appropriate.
- The treatment falls within the policy's covered benefits.

The total amount charged by a healthcare provider does not automatically determine the amount payable.

---

# 18. Exclusions

The following categories may be excluded unless specifically covered:

- Treatment during an applicable waiting period.
- Certain pre-existing conditions during their applicable waiting period.
- Cosmetic treatment not medically necessary.
- Experimental or unproven treatment.
- Expenses specifically excluded under the policy.
- Expenses exceeding applicable sub-limits.
- Non-medical expenses.
- Treatment or circumstances falling outside the insured benefits.

The complete exclusion list must be reviewed before relying on coverage for a particular treatment.

---

# 19. Cosmetic Treatment

Treatment primarily undertaken for cosmetic or aesthetic purposes may not be covered.

An exception may apply where treatment is medically necessary because of a covered medical condition or accidental injury and is otherwise eligible under the policy.

The insurer may require supporting medical evidence.

---

# 20. Experimental Treatment

Experimental, investigational, or unproven treatment may be excluded unless specifically recognized as covered.

The insurer may request evidence regarding the treatment's medical basis and applicability.

The existence of a medical expense does not automatically make the expense eligible for reimbursement.

---

# 21. Fraud and Misrepresentation

Claims containing materially false information, fabricated documents, or fraudulent representations may be rejected in accordance with applicable policy terms and law.

The insurer may investigate circumstances surrounding a claim where fraud or material misrepresentation is suspected.

---

# 22. Policy Renewal

The policy may be renewed subject to applicable renewal terms.

At renewal, the policyholder should review:

- Premium.
- Sum insured.
- Benefits.
- Waiting-period treatment.
- Exclusions.
- Sub-limits.
- Co-payment.
- Deductibles.
- Network hospital availability.
- Changes to policy wording.

The renewed policy should not be assumed to be identical to the previous version.

---

# 23. Cancellation

Cancellation is subject to the applicable policy terms.

Any applicable refund may depend on:

- Time elapsed.
- Claims made.
- Cancellation provisions.
- Regulatory requirements.
- Other conditions.

The policyholder should review the cancellation and refund provisions before terminating coverage.

---

# 24. Consumer Review Checklist

Before purchasing or relying on this policy, a user should review:

- Total premium.
- Sum insured.
- Waiting periods.
- Pre-existing disease conditions.
- Room-category limits.
- Sub-limits.
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

The following synthetic clauses are intentionally included to test the AI review engine.

## Risk Signal 1 — Room Category / Proportionate Deduction

**Risk Level:** High

A room-category restriction may affect the amount payable for associated medical expenses.

**Why it should be flagged:**

A user may believe that selecting a more expensive room only increases the room bill, without realizing that applicable proportionate deductions may also affect other expenses.

**Category:** `coverage_limit`

---

## Risk Signal 2 — Waiting Period

**Risk Level:** Medium

Certain conditions and treatments may not be covered until an applicable waiting period has been completed.

**Why it should be flagged:**

Users may incorrectly assume that purchasing a policy immediately provides coverage for every existing or specified condition.

**Category:** `waiting_period`

---

## Risk Signal 3 — Sub-Limits

**Risk Level:** High

A policy can have a large overall sum insured while individual treatment categories remain subject to separate monetary limits.

**Why it should be flagged:**

A high headline sum insured can create an inaccurate expectation of unlimited coverage.

**Category:** `coverage_limit`

---

## Risk Signal 4 — Cashless Does Not Mean Fully Covered

**Risk Level:** High

Cashless authorization does not guarantee payment of every expense incurred during hospitalization.

**Why it should be flagged:**

Users may misunderstand the practical meaning of cashless treatment.

**Category:** `claim_expectation`

---

## Risk Signal 5 — Deductible / Out-of-Pocket Exposure

**Risk Level:** Medium

A deductible can reduce the amount payable by the insurer even when treatment is otherwise covered.

**Why it should be flagged:**

Users may compare policies using only premium and sum insured without accounting for deductible exposure.

**Category:** `out_of_pocket_cost`

---

## Risk Signal 6 — Claim Documentation

**Risk Level:** Medium

Reimbursement claims may require multiple supporting documents.

**Why it should be flagged:**

Incomplete records can result in additional verification requirements and potentially delay claim assessment.

**Category:** `claim_procedure`

---

# 26. Prototype Policy Score Inputs

The following company-level metrics are provided to the scoring engine from the prototype seed corpus.

```yaml
policy_id: hdfc_ergo_seed
provider: HDFC Ergo General Insurance

metrics:
  premium:
    value: 16594
    currency: INR
    status: PLACEHOLDER

  hidden_charges_count:
    value: 2
    status: PLACEHOLDER

  claim_settlement_pct:
    value: 84.85
    status: REAL_SOURCE_REFERENCED

  claim_volume:
    value: 60985
    status: ESTIMATED_TIER

  complaint_rate:
    value: 7.01
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
document_id: hdfc_ergo_seed_policy_v1
policy_id: hdfc_ergo_seed
provider: HDFC Ergo General Insurance
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

It must not be interpreted as an actual insurance contract or as a representation of the terms offered by HDFC ERGO General Insurance.

For production deployment, this synthetic document must be replaced or supplemented with verified policy documents and authoritative sources.

---

# End of Synthetic Policy Document
