---
title: "Security Policies"
description: "Security policies are formal documents that define an organization's rules, expectations, and requirements for protecting information assets."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/medium
aliases:
  - "Security Policies"
---

> [!eli5] ELI5: What are Security Policies?
> A security policy is like the student handbook your school gives out at the start of the year. It lists the rules everyone needs to follow -- no cheating, be respectful, wear your uniform. For a company, security policies are the official written rules about how to protect computers and data. They cover things like who can access what, how strong your password must be, and what happens if you break a rule. Everyone in the company has to know and follow them.

## Overview

Security policies are high-level, management-approved documents that establish the rules and expectations for how an organization protects its information assets. They serve as the foundation for all security decisions and are enforced through standards, procedures, and guidelines. Policies must be living documents that are regularly reviewed, updated, and communicated to all personnel.

## Key Concepts

- **Policy hierarchy:**
  - **Policies** — mandatory, broad, management-approved ("what" must be done)
  - **Standards** — mandatory, specific technical requirements ("how" it must be done)
  - **Baselines** — minimum security configurations for systems
  - **Guidelines** — recommended but not mandatory best practices
  - **Procedures** — step-by-step instructions for tasks
- **Common security policies:**
  - **Acceptable Use Policy (AUP)** — defines permitted use of organizational resources
  - **Information security policy** — overarching security program direction
  - **Password / credential policy** — complexity, length, rotation, MFA requirements
  - **Data handling / classification policy** — rules for managing data at each classification level
  - **Change management policy** — process for approving and documenting changes
  - **Incident response policy** — defines roles, authority, and procedures for handling incidents
  - **BYOD policy** — rules for personal devices accessing corporate resources
- **[[policy-lifecycle|Policy lifecycle]]** — create, approve, distribute, enforce, review, revise, retire
- **[[exception-process|Exception process]]** — formal mechanism for requesting and approving deviations from policy
- **Job rotation** — periodically rotating personnel through different roles to detect fraud and reduce single points of failure
- **Mandatory vacations** — requiring employees to take time off so others perform their duties, exposing potential fraud
- **Clean desk policy** — requiring employees to secure all sensitive materials when leaving their workspace
- **NDA (Non-Disclosure Agreement)** — legal contract prohibiting sharing of confidential information
- **Background checks** — pre-employment screening including criminal history, credit checks, and reference verification
- **EOL (End of Life)** — vendor no longer sells the product but may still provide support
- **EOSL (End of Service Life)** — vendor no longer provides patches, updates, or support; critical security risk

## Exam Tips

> [!tip] Remember
> Policies are mandatory and set by management. Guidelines are optional recommendations. Standards define specific requirements. The AUP is the most commonly referenced policy on the exam.

## Connections

- Derived from [[governance]] decisions and organizational risk appetite
- Must align with external [[regulations-and-frameworks]] to ensure compliance
- See also [[security-awareness-training]] for how policies are communicated to employees

## Practice Questions

> [!qbank]- Q-Bank: Security Policies (4 Questions)
>
> **Q1.** A new employee asks their manager what is and is not allowed when using the company laptop for personal activities during lunch breaks. Which policy document should the manager direct them to?
>
> A. Incident response policy
> B. Change management policy
> C. Acceptable Use Policy (AUP)
> D. Data handling policy
>
> > [!answer]- Show Answer
> > **C. Acceptable Use Policy (AUP)**
> >
> > The [[security-policies|Acceptable Use Policy (AUP)]] defines permitted and prohibited uses of organizational resources, including personal use of company equipment. The incident response policy (A) covers procedures for handling security incidents. The change management policy (B) governs how changes to systems are approved and documented. The data handling policy (D) addresses how data at each classification level should be managed.
>
> **Q2.** A security architect creates a document specifying that all Windows servers must use AES-256 encryption for data at rest, enforce TLS 1.3 for data in transit, and disable SMBv1. This document is BEST classified as a:
>
> A. Policy
> B. Standard
> C. Guideline
> D. Procedure
>
> > [!answer]- Show Answer
> > **B. Standard**
> >
> > A [[security-policies|standard]] defines mandatory, specific technical requirements -- the "how" of implementation. Specifying exact encryption algorithms and protocols is a standard. A policy (A) is a high-level statement of what must be done, not specific technical details. A guideline (C) is recommended but not mandatory. A procedure (D) provides step-by-step instructions for completing a task, not configuration specifications.
>
> **Q3.** A department head needs to use an older application that does not support the organization's required multi-factor authentication standard. The department head submits a formal request documenting the business justification and compensating controls. This process is BEST described as a:
>
> A. Policy violation
> B. Change management request
> C. Exception process
> D. Baseline deviation
>
> > [!answer]- Show Answer
> > **C. Exception process**
> >
> > The [[exception-process|exception process]] is the formal mechanism for requesting and approving deviations from policy when business needs require it. A policy violation (A) would be an unauthorized deviation without approval. A change management request (B) is for modifying systems or configurations, not for requesting policy exceptions. A baseline deviation (C) describes a system not meeting minimum configuration, but the formal request process to permit this is the exception process.
>
> **Q4.** An organization publishes a document recommending that employees use password managers but does not require it. This document is BEST classified as a:
>
> A. Policy
> B. Standard
> C. Guideline
> D. Procedure
>
> > [!answer]- Show Answer
> > **C. Guideline**
> >
> > A [[security-policies|guideline]] provides recommended best practices that are not mandatory. The key word "recommending" without a requirement indicates this is advisory, not compulsory. A policy (A) would mandate the use of password managers. A standard (B) would specify exact technical requirements for password management. A procedure (D) would provide step-by-step instructions on how to set up and use a password manager.

## Scenario

> See [[case-security-policies]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [5.1 – Security Policies](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv&index=105)
