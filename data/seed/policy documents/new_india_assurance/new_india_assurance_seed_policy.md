# New India Assurance — Comprehensive Health Insurance Policy

> **PROTOTYPE / SYNTHETIC DOCUMENT**
>
> This document is mock data created exclusively for development and demonstration of the Insurance Policy Review prototype.
>
> It is **not an actual New India Assurance policy**, does not represent official policy wording, and must not be used for purchasing, underwriting, claims, legal, or financial decisions.
>
> Company-level metrics are seeded from the prototype dataset. All policy clauses, coverage terms, exclusions, waiting periods, limits, claim conditions, and other policy wording in this document are synthetic.

---

# Policy Information

| Field | Value |
|---|---|
| Policy ID | `new_india_assurance_seed` |
| Provider | New India Assurance |
| Policy Type | Comprehensive Health Insurance |
| Document Type | Synthetic Policy Wording |
| Version | `PROTOTYPE-1.0` |
| Effective Date | 01 April 2026 |
| Jurisdiction | India |
| Currency | INR |
| Document Status | Synthetic / Prototype |

---

# 1. Policy Overview

This synthetic policy represents a prototype comprehensive health insurance product intended to cover eligible medical expenses incurred during the policy period.

Coverage is subject to the applicable sum insured, waiting periods, exclusions, sub-limits, deductibles, co-payments, claim procedures, and other conditions contained in this document.

The insurer may request reasonable medical and financial documentation to determine claim eligibility and the amount payable.

---

# 2. Key Policy Metrics

The following figures are **prototype dataset metrics** and are not presented as official current product pricing or performance information.

| Metric | Prototype Value |
|---|---:|
| Indicative Annual Premium | ₹12,374 |
| Hidden Charge Count | 1 |
| Claim Settlement Metric | 100.98% |
| Estimated Claim Volume | 304,456 |
| Prototype Complaint Rate | 1.89 |
| Sample Count | 1 |
| Data Granularity | company |
| Settlement Metric Status | REAL / SOURCE-REFERENCED |
| Other Metrics | PLACEHOLDER / SYNTHETIC |

### Data Quality Notice

The prototype dataset marks the claim-settlement metric as real/source-referenced from the IRDAI FY24-25 Annual Report. Premium, hidden-charge count, complaint rate, and claim volume are explicitly marked as placeholder or estimated in the source dataset.

The application must therefore display confidence/status information rather than treating every metric as equally verified.

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
- Other benefits specifically stated in the applicable policy schedule.

Coverage remains subject to applicable limits and exclusions.

---

# 4. Hospitalization

Hospitalization expenses may be covered where the treatment is medically necessary and otherwise eligible under the policy.

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
> The application should distinguish the amount billed by the provider from the amount that qualifies for reimbursement under the policy.

**Risk category:** `claim_expectation`

---

# 5. Room and Accommodation Limits

The policy may specify an eligible room category or accommodation limit.

If the insured chooses a room above the eligible category, the insurer may apply deductions according to the applicable policy terms. Where proportionate deductions apply, associated medical expenses may also be affected.

The exact room limit must be verified against the applicable policy schedule.

> **AI REVIEW FLAG — HIGH**
>
> A room-category restriction can potentially increase out-of-pocket exposure beyond the difference between the selected room and the eligible room.

**Risk category:** `coverage_limit`

---

# 6. Waiting Periods

Certain illnesses, treatments, procedures, and pre-existing conditions may be subject to waiting periods.

Waiting periods may apply to:

- Pre-existing diseases.
- Specified illnesses.
- Certain planned procedures.
- Other benefits identified in the policy schedule.

A claim submitted during an applicable waiting period may not be payable.

The exact duration must be verified from the applicable policy schedule.

> **AI REVIEW FLAG — MEDIUM**
>
> Users should not assume that every medical condition is covered immediately after policy commencement.

**Risk category:** `waiting_period`

---

# 7. Pre-Existing Diseases

A pre-existing disease refers to a medical condition existing before commencement of coverage, subject to the applicable policy definition.

Coverage for pre-existing diseases may be subject to a waiting period.

The insured should disclose relevant medical history accurately during proposal and underwriting.

Material non-disclosure or inaccurate information may affect claim assessment where permitted by the policy terms and applicable law.

---

# 8. Disease-Specific Limits

Certain illnesses or treatments may have specific monetary limits or sub-limits.

A sub-limit can apply even when the overall sum insured remains available.

The insured should therefore review:

- Treatment-specific limits.
- Procedure-specific limits.
- Accommodation limits.
- Diagnostic limits.
- Other benefit-specific restrictions.

> **AI REVIEW FLAG — HIGH**
>
> A large overall sum insured does not necessarily mean unlimited reimbursement for every medical treatment.

**Risk category:** `coverage_limit`

---

# 9. Co-Payment

A co-payment may apply to specified treatments, benefits, policy configurations, or categories of insured persons.

Where a co-payment applies, the insured must bear the applicable percentage of an otherwise eligible claim.

For illustration only, if an eligible claim is ₹100,000 and a 20% co-payment applies:

- Insurer portion: ₹80,000
- Insured portion: ₹20,000

The actual co-payment must be verified from the applicable policy schedule.

---

# 10. Deductibles

A deductible may apply depending on the selected policy configuration.

The insured must bear the deductible amount before the insurer becomes liable for the remaining eligible expenses, subject to the applicable terms.

The operation of a deductible may depend on whether it is defined per claim, per policy period, or under another applicable structure.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `out_of_pocket_cost`

---

# 11. Non-Medical Expenses

Certain hospitalization-related expenses may not qualify as covered medical expenses.

Examples may include:

- Personal-use items.
- Administrative charges.
- Convenience items.
- Certain consumables.
- Other expenses specifically excluded by the policy.

Such expenses may remain payable by the insured.

> **AI REVIEW FLAG — MEDIUM**
>
> Individual excluded items may appear minor but can collectively increase the final amount paid by the insured.

**Risk category:** `out_of_pocket_cost`

---

# 12. Cashless Treatment

Cashless treatment may be available at eligible network hospitals subject to authorization.

Cashless authorization does not necessarily mean that every expense incurred during hospitalization will be paid.

Final claim liability remains subject to:

- Coverage.
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

For planned hospitalization, prior authorization may be required where applicable.

Authorization may be based on information available at the time of the request.

Approval does not necessarily constitute final approval of every expense incurred during treatment.

The final claim may be assessed after complete documentation is submitted.

---

# 14. Emergency Hospitalization

In an emergency, the insured should notify the insurer or applicable claims administrator as soon as reasonably practicable.

The insurer may request information relating to:

- The emergency.
- Diagnosis.
- Treatment.
- Admission.
- Medical necessity.
- Expenses incurred.

Applicable notification requirements should be reviewed before submitting a claim.

---

# 15. Reimbursement Claims

Where cashless treatment is unavailable or not used, the insured may submit a reimbursement claim.

Supporting documents may include:

1. Claim form.
2. Hospital bills.
3. Discharge summary.
4. Medical reports.
5. Prescriptions.
6. Diagnostic reports.
7. Payment receipts.
8. Other documents reasonably required for assessment.

The insurer may request additional documentation where necessary.

---

# 16. Claim Documentation

The insured should retain documents supporting the medical treatment and expenses.

Incomplete documentation may require additional verification.

The insured may be asked to provide clarification regarding:

- Treatment.
- Diagnosis.
- Expenses.
- Medical necessity.
- Payment.
- Previous medical history.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `claim_procedure`

---

# 17. Medical Necessity

For an expense to be eligible, the treatment may need to satisfy the applicable definition of medical necessity.

The insurer may assess:

- Whether treatment was appropriate for the diagnosed condition.
- Whether treatment was clinically required.
- Whether the level of care was appropriate.
- Whether the treatment falls within covered benefits.

A medical bill alone does not establish that the entire amount is payable.

---

# 18. Exclusions

The policy does not automatically cover every medical expense.

Potential exclusions may include:

- Treatment during an applicable waiting period.
- Certain pre-existing conditions during their applicable waiting period.
- Cosmetic treatment not medically necessary.
- Experimental or unproven treatment.
- Non-medical expenses.
- Expenses exceeding applicable sub-limits.
- Treatment outside the insured benefits.
- Other exclusions specifically identified in the policy schedule.

The complete exclusion section should be reviewed before relying on coverage for a particular treatment.

---

# 19. Cosmetic Treatment

Treatment primarily undertaken for aesthetic or cosmetic purposes may not be covered.

Treatment may be considered differently where medically necessary due to a covered condition or accidental injury and otherwise eligible under the policy.

The insurer may request supporting medical evidence.

---

# 20. Experimental or Unproven Treatment

Experimental, investigational, or unproven treatments may be excluded unless specifically recognized as covered.

The insurer may request clinical or medical documentation supporting the treatment.

The existence of a medical expense does not automatically make the expense eligible for reimbursement.

---

# 21. Fraud and Misrepresentation

A claim containing materially false information, fabricated documents, or fraudulent representations may be rejected in accordance with applicable policy terms and law.

The insurer may investigate circumstances surrounding a claim where fraud or material misrepresentation is suspected.

---

# 22. Policy Renewal

The policy may be renewed subject to applicable renewal terms.

The policyholder should review renewal documentation for changes to:

- Premium.
- Sum insured.
- Benefits.
- Waiting periods.
- Exclusions.
- Sub-limits.
- Co-payment.
- Deductibles.
- Network hospital availability.
- Other policy conditions.

A renewal should not automatically be assumed to have identical terms to the previous policy version.

---

# 23. Cancellation

Cancellation is subject to the applicable policy terms.

Any applicable refund may depend on:

- Time elapsed.
- Claims already made.
- Cancellation provisions.
- Regulatory requirements.
- Other applicable conditions.

The policyholder should review the cancellation section before terminating coverage.

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

**Why it should be flagged:**

Users may assume that choosing a higher-priced room only changes the room expense.

**Category:** `coverage_limit`

---

## Risk Signal 2 — Waiting Period

**Risk Level:** Medium

Certain conditions may not be covered until an applicable waiting period has been completed.

**Why it should be flagged:**

Immediate coverage should not be assumed for every medical condition.

**Category:** `waiting_period`

---

## Risk Signal 3 — Disease-Specific Sub-Limits

**Risk Level:** High

Individual treatments can have limits separate from the overall sum insured.

**Why it should be flagged:**

A high overall sum insured can create unrealistic expectations about reimbursement.

**Category:** `coverage_limit`

---

## Risk Signal 4 — Cashless Does Not Mean Fully Covered

**Risk Level:** High

Cashless authorization does not guarantee payment of every expense.

**Why it should be flagged:**

Users may misunderstand the practical meaning of cashless treatment.

**Category:** `claim_expectation`

---

## Risk Signal 5 — Out-of-Pocket Costs

**Risk Level:** Medium

Co-payments, deductibles, non-medical expenses, and sub-limits can increase the amount paid by the insured.

**Why it should be flagged:**

Premium alone is insufficient for evaluating the user's potential financial exposure.

**Category:** `out_of_pocket_cost`

---

## Risk Signal 6 — Claim Documentation

**Risk Level:** Medium

Reimbursement claims may require several supporting documents.

**Why it should be flagged:**

Missing records may create additional verification requirements.

**Category:** `claim_procedure`

---

# 26. Prototype Policy Score Inputs

The following company-level metrics are provided to the prototype scoring engine.

```yaml
policy_id: new_india_assurance_seed
provider: New India Assurance

metrics:
  premium:
    value: 12374
    currency: INR
    status: PLACEHOLDER

  hidden_charges_count:
    value: 1
    status: PLACEHOLDER

  claim_settlement_pct:
    value: 100.98
    status: REAL_SOURCE_REFERENCED

  claim_volume:
    value: 304456
    status: ESTIMATED_TIER

  complaint_rate:
    value: 1.89
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
document_id: new_india_assurance_seed_policy_v1
policy_id: new_india_assurance_seed
provider: New India Assurance
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

It must not be interpreted as an actual insurance contract or as a representation of the terms offered by New India Assurance.

For production deployment, this synthetic document must be replaced or supplemented with verified policy documents and authoritative sources.

---

# End of Synthetic Policy Document
