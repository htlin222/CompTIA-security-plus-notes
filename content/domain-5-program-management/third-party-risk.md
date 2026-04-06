---
title: "Third-Party Risk"
description: "Third-party risk management addresses the security threats introduced by vendors, suppliers, and service providers."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/medium
aliases:
  - "Third-Party Risk Management"
  - "TPRM"
---

> [!eli5] ELI5: What is Third-Party Risk?
> Say you give your house key to a dog walker so they can come in while you're at school. You trust them, but what if they lose the key or leave the door unlocked? Third-party risk is the danger that comes from sharing your stuff (data, systems, or access) with outside helpers like vendors or partners. If their security is weak, bad guys could get to your data through them -- even if your own locks are strong.

## Overview

Third-party risk arises whenever an organization shares data, systems, or access with external entities such as vendors, contractors, cloud providers, or business partners. A compromise at a third party can directly impact your organization. Managing this risk requires due diligence before onboarding, continuous monitoring during the relationship, and secure offboarding at termination.

## Key Concepts

- **[[supply-chain-risk|Supply chain risk]]** — compromised hardware, software, or services introduced through the supply chain (e.g., SolarWinds)
- **[[vendor-assessment|Vendor assessment]]** — questionnaires, on-site audits, penetration test results, and SOC reports used to evaluate vendor security
- **[[service-level-agreements-slas|Service Level Agreements (SLAs)]]** — contractual terms defining uptime, response times, and security obligations
- **[[right-to-audit|Right to audit]]** — contractual clause allowing the organization to audit the vendor's security controls
- **[[data-ownership-and-processing-agreements|Data ownership and processing agreements]]** — clearly define who owns data and how it is handled, stored, and deleted
- **[[soc-reports|SOC reports]]** — SOC 2 Type I (point-in-time) and Type II (over a period) attest to a service provider's controls
- **[[vendor-lock-in|Vendor lock-in]]** — dependency risk when switching providers is costly or technically difficult
- **[[offboarding|Offboarding]]** — revoking access, retrieving data, and ensuring secure data destruction when a vendor relationship ends
- **[[fourth-party-risk|Fourth-party risk]]** — risk from your vendor's vendors; you may not have visibility into their supply chain
- **MOU (Memorandum of Understanding)** — less formal agreement outlining mutual intentions between parties
- **MSA (Master Service Agreement)** — overarching contract governing all future transactions between parties
- **BPA (Business Partners Agreement)** — defines responsibilities and profit/loss sharing between business partners

## Exam Tips

> [!tip] Remember
> SOC 2 Type II is more valuable than Type I because it covers a time period, not just a snapshot. The exam tests supply chain attacks and vendor assessment methods frequently.

## Connections

- Falls under the broader [[risk-management]] framework as a specific category of external risk
- Related to [[compliance]] because regulations often require organizations to ensure third-party data handling meets standards
- See also [[security-policies]] for acceptable use and vendor management policy requirements

## Practice Questions

> [!qbank]- Q-Bank: Third-Party Risk (4 Questions)
>
> **Q1.** A company discovers that its cloud storage provider was breached, exposing customer records that the company had uploaded. Investigation reveals the company never reviewed the provider's security controls before signing the contract. Which third-party risk management failure does this BEST illustrate?
>
> A. Lack of right-to-audit clause
> B. Failure to perform vendor assessment
> C. Vendor lock-in
> D. Inadequate offboarding procedures
>
> > [!answer]- Show Answer
> > **B. Failure to perform vendor assessment**
> >
> > [[vendor-assessment|Vendor assessment]] is the due diligence process of evaluating a vendor's security posture before onboarding, including reviewing questionnaires, SOC reports, and penetration test results. Not performing this is a fundamental TPRM failure. A right-to-audit clause (A) enables future audits but would not have prevented the initial lack of review. Vendor lock-in (C) is about dependency risk when switching providers. Offboarding (D) addresses end-of-relationship procedures, not pre-contract evaluation.
>
> **Q2.** During contract negotiations with a SaaS provider, the legal team insists on including a clause that allows the organization to inspect the provider's security controls annually. This clause is BEST known as a:
>
> A. Service Level Agreement
> B. Data processing agreement
> C. Right to audit
> D. Non-disclosure agreement
>
> > [!answer]- Show Answer
> > **C. Right to audit**
> >
> > The [[right-to-audit|right to audit]] is a contractual clause that grants the organization permission to audit or inspect the vendor's security controls. A Service Level Agreement (A) defines uptime and performance metrics, not inspection rights. A data processing agreement (B) defines how data is handled and stored. A non-disclosure agreement (D) protects confidential information shared between parties but does not grant audit rights.
>
> **Q3.** An organization's primary vendor uses a subcontractor to process sensitive data. The organization has no visibility into the subcontractor's security practices. This situation BEST describes which risk concept?
>
> A. Supply chain risk
> B. Vendor lock-in
> C. Fourth-party risk
> D. Contractual compliance failure
>
> > [!answer]- Show Answer
> > **C. Fourth-party risk**
> >
> > [[fourth-party-risk|Fourth-party risk]] is the risk from your vendor's vendors (subcontractors), where you may have no visibility or control over their security practices. Supply chain risk (A) is broader and includes hardware, software, and services in the entire chain, but the specific scenario of a vendor's subcontractor is fourth-party risk. Vendor lock-in (B) is about switching costs, not subcontractor visibility. Contractual compliance failure (D) would mean the vendor is violating contract terms, which may or may not be the case here.
>
> **Q4.** A company terminates its relationship with a managed security services provider. Which activity is MOST critical during the offboarding process?
>
> A. Negotiating a new SLA
> B. Revoking the provider's access and ensuring secure data destruction
> C. Conducting a phishing simulation on the provider's staff
> D. Purchasing cyber insurance to cover the transition period
>
> > [!answer]- Show Answer
> > **B. Revoking the provider's access and ensuring secure data destruction**
> >
> > [[offboarding|Offboarding]] requires revoking all access, retrieving or destroying data, and ensuring no residual access remains after the relationship ends. Negotiating a new SLA (A) applies to onboarding a new provider, not terminating an existing one. Conducting a phishing simulation (C) on the provider's staff is not part of offboarding and is outside the organization's authority. Purchasing cyber insurance (D) may be prudent generally but is not the most critical offboarding activity.

## Scenario

> See [[case-third-party-risk]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [5.3 – Third-party Risk Assessment](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=114)
