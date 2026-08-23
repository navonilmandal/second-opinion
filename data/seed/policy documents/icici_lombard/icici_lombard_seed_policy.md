# ICICI Lombard General Insurance — Comprehensive Health Insurance Policy

> **PROTOTYPE / SYNTHETIC DOCUMENT**
>
> This document is mock data created exclusively for development and demonstration of the Insurance Policy Review prototype.
>
> It is **not an actual ICICI Lombard General Insurance policy**, does not represent official policy wording, and must not be used for purchasing, underwriting, claims, legal, or financial decisions.
>
> Company-level metrics are seeded from the prototype dataset. All policy clauses, coverage terms, exclusions, waiting periods, limits, claim conditions, and wording below are synthetic.

---

# Policy Information

| Field | Value |
|---|---|
| Policy ID | `icici_lombard_seed` |
| Provider | ICICI Lombard General Insurance |
| Policy Type | Comprehensive Health Insurance |
| Document Type | Synthetic Policy Wording |
| Version | `PROTOTYPE-1.0` |
| Effective Date | 01 April 2026 |
| Jurisdiction | India |
| Currency | INR |
| Document Status | Synthetic / Prototype |

---

# 1. Policy Overview

This synthetic policy represents a prototype comprehensive health insurance product covering eligible medical expenses during the policy period, subject to the applicable sum insured, waiting periods, exclusions, sub-limits, deductibles, co-payments, and claim conditions.

A medical expense is not automatically payable merely because it was incurred during a hospitalization. Eligibility depends on the complete set of applicable policy conditions.

---

# 2. Key Policy Metrics

The following figures are **prototype dataset metrics** and are not presented as official current product pricing or performance information.

| Metric | Prototype Value |
|---|---:|
| Indicative Annual Premium | ₹12,095 |
| Hidden Charge Count | 0 |
| Claim Settlement Metric | 82.24% |
| Estimated Claim Volume | 59,973 |
| Prototype Complaint Rate | 0.73 |
| Sample Count | 1 |
| Data Granularity | company |
| Settlement Metric Status | REAL / SOURCE-REFERENCED |
| Other Metrics | PLACEHOLDER / SYNTHETIC |

### Data Quality Notice

The prototype dataset identifies the claim-settlement metric as sourced from the IRDAI FY24-25 Annual Report, while premium, hidden-charge count, complaint rate, and claim volume are marked as placeholder or estimated values.

The application must distinguish source-referenced metrics from synthetic prototype metrics.

---

# 3. Covered Hospitalization

Eligible hospitalization expenses may be covered where the treatment:

- Is medically necessary.
- Falls within the insured benefits.
- Satisfies applicable waiting-period requirements.
- Is not excluded.
- Falls within applicable limits and sub-limits.
- Is supported by required documentation.

The insurer may request medical records, bills, prescriptions, diagnostic reports, discharge summaries, and other evidence reasonably required for claim assessment.

---

# 4. Day-Care Procedures

Specified procedures that do not require a full overnight hospitalization may qualify for coverage where they satisfy the applicable policy conditions.

Eligibility remains subject to:

- Medical necessity.
- Applicable waiting periods.
- Coverage limits.
- Exclusions.
- Documentation requirements.

A procedure being performed in a hospital does not by itself establish coverage.

---

# 5. Pre-Hospitalization Expenses

Eligible expenses incurred before a covered hospitalization may be considered where they are directly related to the hospitalization and fall within the applicable period.

Expenses that cannot reasonably be connected to the covered hospitalization may not qualify.

The insured should retain prescriptions, consultation records, diagnostic reports, and receipts supporting such expenses.

---

# 6. Post-Hospitalization Expenses

Eligible expenses incurred after discharge may be considered when they:

- Relate directly to the covered hospitalization.
- Are medically necessary.
- Occur within the applicable post-hospitalization period.
- Are supported by documentation.

The applicable duration should be verified against the policy schedule.

---

# 7. Waiting Periods

Certain illnesses, procedures, or conditions may be subject to waiting periods.

Waiting periods may apply to:

- Pre-existing diseases.
- Specified diseases.
- Certain planned procedures.
- Other categories identified by the selected plan.

Claims relating to a condition that remains within an applicable waiting period may not be payable.

> **AI REVIEW FLAG — HIGH**
>
> Waiting-period clauses can materially affect whether a newly purchased policy provides immediate protection for a particular medical condition.

**Risk category:** `waiting_period`

---

# 8. Pre-Existing Diseases

A pre-existing disease refers to a medical condition existing before commencement of coverage, according to the applicable policy definition.

Coverage may be subject to a waiting period.

The insured is expected to provide accurate and complete information during proposal and underwriting.

Material non-disclosure may affect claim assessment where permitted by applicable terms and law.

---

# 9. Room-Rent and Accommodation Limits

The policy may specify an eligible room category or monetary accommodation limit.

Where the insured chooses accommodation above the applicable eligibility limit, the policy may apply deductions to room-related expenses and, where specified, proportionate deductions to associated medical expenses.

The actual room limit must be checked against the applicable policy schedule.

> **AI REVIEW FLAG — HIGH**
>
> This clause is important because a room restriction may affect the final claim beyond the room-price difference.

**Risk category:** `coverage_limit`

---

# 10. Co-Payment

A co-payment may apply to specified treatments, policy configurations, or insured categories.

Where applicable, the insured must bear the stated percentage of eligible expenses.

For illustration only, if an eligible claim is ₹100,000 and a 20% co-payment applies:

- Insurer portion: ₹80,000
- Insured portion: ₹20,000

The actual co-payment must be verified from the applicable policy schedule.

---

# 11. Deductible

A deductible may apply depending on the selected plan.

The insured must bear the deductible before the insurer becomes liable for the remaining eligible expenses, subject to the terms governing how the deductible operates.

A deductible may materially change the effective out-of-pocket cost of a policy.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `out_of_pocket_cost`

---

# 12. Disease and Treatment Sub-Limits

Specific illnesses, procedures, or benefits may have separate monetary limits.

A sub-limit can restrict the maximum amount payable for a particular category even when the overall sum insured remains available.

Users should therefore review both:

- The headline sum insured.
- Individual benefit-level limits.

> **AI REVIEW FLAG — HIGH**
>
> A large sum insured should not automatically be interpreted as unlimited coverage for every treatment.

**Risk category:** `coverage_limit`

---

# 13. Non-Medical Expenses

Certain expenses associated with hospitalization may be excluded from reimbursement.

Potential examples include:

- Personal-use items.
- Convenience items.
- Administrative charges.
- Certain consumables.
- Other specifically excluded items.

These expenses may remain payable by the insured.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `out_of_pocket_cost`

---

# 14. Cashless Hospitalization

Cashless treatment may be available at eligible network hospitals subject to authorization.

Cashless authorization does not guarantee that every expense will ultimately be paid.

Final liability remains subject to:

- Coverage.
- Exclusions.
- Waiting periods.
- Sub-limits.
- Deductibles.
- Co-payments.
- Medical necessity.
- Documentation.

> **AI REVIEW FLAG — HIGH**
>
> "Cashless" should not be interpreted as "all expenses are covered."

**Risk category:** `claim_expectation`

---

# 15. Pre-Authorization

For planned hospitalization, prior authorization may be required where applicable.

Authorization is based on information available at the time of review and does not necessarily constitute final approval of every expense.

The final claim may be assessed after complete treatment records and bills are submitted.

---

# 16. Emergency Hospitalization

In an emergency, the insured should notify the insurer or claims administrator as soon as reasonably practicable.

The insurer may require information concerning:

- Emergency circumstances.
- Diagnosis.
- Treatment.
- Admission.
- Medical necessity.
- Expenses incurred.

Failure to comply with applicable notification requirements may lead to additional claim review.

---

# 17. Reimbursement Claims

Where cashless treatment is not used, reimbursement may be requested subject to policy requirements.

Supporting documents may include:

1. Claim form.
2. Hospital bills.
3. Discharge summary.
4. Medical reports.
5. Prescriptions.
6. Diagnostic reports.
7. Payment receipts.
8. Other documents reasonably requested for assessment.

---

# 18. Claim Assessment

A claim may be assessed using:

1. Policy eligibility.
2. Medical necessity.
3. Waiting periods.
4. Exclusions.
5. Coverage limits.
6. Sub-limits.
7. Deductibles.
8. Co-payments.
9. Documentation.

The amount claimed and the amount ultimately payable may therefore differ.

---

# 19. Medical Necessity

Treatment must satisfy the applicable medical-necessity requirements.

The insurer may consider:

- Diagnosis.
- Clinical justification.
- Treatment appropriateness.
- Level of care.
- Supporting medical records.

A hospital invoice alone does not establish that every expense is covered.

---

# 20. Exclusions

The policy may exclude:

- Treatment during an applicable waiting period.
- Certain pre-existing conditions during their waiting period.
- Cosmetic treatment not medically necessary.
- Experimental or unproven treatment.
- Non-medical expenses.
- Expenses above applicable limits.
- Specifically excluded procedures or circumstances.
- Expenses otherwise outside the insured benefits.

The complete exclusion list should be reviewed before relying on coverage.

---

# 21. Cosmetic Treatment

Treatment primarily intended for cosmetic or aesthetic purposes may not be covered.

Treatment may receive different consideration where medically necessary because of a covered illness or accidental injury and otherwise eligible under the policy.

Medical evidence may be requested.

---

# 22. Experimental or Unproven Treatment

Experimental, investigational, or unproven treatments may be excluded unless specifically covered.

The insurer may request evidence regarding clinical justification and recognition of the treatment.

---

# 23. Claim Documentation

The insured should retain complete documentation supporting a claim.

Incomplete documentation may result in additional verification requirements.

Where required records cannot be provided, the insurer may seek alternative evidence or conduct additional assessment.

> **AI REVIEW FLAG — MEDIUM**

**Risk category:** `claim_procedure`

---

# 24. Fraudulent or Misrepresented Claims

Materially false information, fabricated documents, or fraudulent representations may result in rejection or other action according to the applicable policy terms and law.

The insurer may investigate circumstances where fraud or material misrepresentation is suspected.

---

# 25. Renewal

At renewal, the policyholder should review:

- Premium.
- Sum insured.
- Benefits.
- Exclusions.
- Waiting-period provisions.
- Sub-limits.
- Deductibles.
- Co-payments.
- Network hospital availability.
- Changes to policy wording.

A renewed policy should not automatically be assumed to have identical terms to the previous policy version.

---

# 26. Cancellation

Cancellation is subject to the applicable policy provisions.

Any refund may depend on:

- Time elapsed.
- Claims made.
- Applicable cancellation terms.
- Regulatory requirements.

The policyholder should review the cancellation and refund conditions before terminating coverage.

---

# 27. Consumer Review Checklist

A user reviewing this policy should pay particular attention to:

- Premium.
- Sum insured.
- Waiting periods.
- Pre-existing disease provisions.
- Room-rent limits.
- Sub-limits.
- Co-payment.
- Deductibles.
- Exclusions.
- Non-medical expenses.
- Cashless hospital network.
- Claim notification.
- Documentation requirements.
- Renewal conditions.
- Cancellation and refund provisions.

---

# 28. Prototype Risk Signals

## Risk Signal 1 — Waiting Period

**Risk Level:** High

Some medical conditions and treatments may not be covered immediately after policy commencement.

**Category:** `waiting_period`

---

## Risk Signal 2 — Room-Rent Restriction

**Risk Level:** High

Selecting accommodation above an eligible limit may increase out-of-pocket exposure through applicable deductions.

**Category:** `coverage_limit`

---

## Risk Signal 3 — Treatment Sub-Limits

**Risk Level:** High

Individual treatments may have limits lower than the overall sum insured.

**Category:** `coverage_limit`

---

## Risk Signal 4 — Cashless Does Not Mean Fully Covered

**Risk Level:** High

Cashless authorization does not guarantee payment of every expense.

**Category:** `claim_expectation`

---

## Risk Signal 5 — Deductible / Co-Payment

**Risk Level:** Medium

Deductibles and co-payments can materially increase the insured's share of eligible expenses.

**Category:** `out_of_pocket_cost`

---

## Risk Signal 6 — Claim Documentation

**Risk Level:** Medium

Reimbursement claims may require multiple supporting records.

**Category:** `claim_procedure`

---

# 29. Prototype Policy Score Inputs

```yaml
policy_id: icici_lombard_seed
provider: ICICI Lombard General Insurance

metrics:
  premium:
    value: 12095
    currency: INR
    status: PLACEHOLDER

  hidden_charges_count:
    value: 0
    status: PLACEHOLDER

  claim_settlement_pct:
    value: 82.24
    status: REAL_SOURCE_REFERENCED

  claim_volume:
    value: 59973
    status: ESTIMATED_TIER

  complaint_rate:
    value: 0.73
    status: PLACEHOLDER

  n_samples:
    value: 1

data_source:
  claim_settlement_pct: "IRDAI Annual Report 2024-25, company-wise Incurred Claim Ratio (health segment)"

granularity: company
```

---

# 30. AI Analysis Metadata

```yaml
document_id: icici_lombard_seed_policy_v1
policy_id: icici_lombard_seed
provider: ICICI Lombard General Insurance
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

# 31. Prototype Disclaimer

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

It must not be interpreted as an actual insurance contract or as a representation of the terms offered by ICICI Lombard General Insurance.

For production deployment, this synthetic document must be replaced or supplemented with verified policy documents and authoritative sources.

---

# End of Synthetic Policy Document
