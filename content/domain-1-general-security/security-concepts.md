---
title: "Security Concepts"
description: "Foundational security principles and terminology for the SY0-701 exam"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - concept/risk
  - weight/high
aliases:
  - "Security Fundamentals"
---

> [!eli5] ELI5: What are Security Concepts?
> Security concepts are the basic rules everyone follows to keep information safe -- kind of like the safety rules you learn on the first day of school. They include ideas like "only share secrets with people who need to know," "don't give anyone more power than they need," and "keep records of who did what." These simple ideas guide every decision about protecting computers and data, no matter how big or complicated the system gets.

## Overview

Security concepts form the bedrock of the CompTIA Security+ exam, encompassing the principles, terminology, and frameworks that guide all cybersecurity practices. Understanding these foundational ideas is essential for grasping how threats are identified, risks are managed, and systems are protected across an organization.

## Key Concepts

- **Confidentiality, Integrity, Availability (CIA)** — the three pillars of information security; every control maps back to at least one of these (see [[cia-triad]])
- **[[non-repudiation|Non-repudiation]]** — ensures that a party cannot deny having performed an action; achieved through digital signatures, logging, and audit trails
- **[[least-privilege|Least privilege]]** — users and processes should only have the minimum permissions necessary to perform their function
- **[[separation-of-duties|Separation of duties]]** — no single person should control all aspects of a critical transaction, reducing fraud and error risk
- **[[need-to-know|Need to know]]** — access to information is restricted to those who require it for their role
- **[[due-diligence-vs-due-care|Due diligence vs. due care]]** — due diligence is researching and understanding risks; due care is acting responsibly to mitigate them
- **[[security-through-obscurity|Security through obscurity]]** — relying on secrecy of design rather than robust controls; considered insufficient on its own
- **[[open-design-principle|Open design principle]]** — security mechanisms should not depend on secrecy of implementation

## Exam Tips

> [!tip] Remember
> The CIA triad appears in nearly every domain. When evaluating a scenario question, ask: "Which element of CIA is being threatened?" This frames the correct answer quickly.

> [!tip] Least Privilege vs. Need to Know
> Least privilege limits _permissions_; need to know limits _information access_. Both reduce attack surface but operate at different levels.

## Connections

- Built upon [[cia-triad]] as the core framework for evaluating security posture
- Implemented through [[defense-in-depth]] to create layered security controls
- Enforced by [[access-control-models]] which define how least privilege and separation of duties are applied
- Directly informs [[risk-management]] decisions about which controls to implement

## Practice Questions

> [!qbank]- Q-Bank: Security Concepts (4 Questions)
>
> **Q1.** A company grants its help desk staff the ability to reset passwords but not to create new accounts or modify group memberships. Which foundational security principle does this restriction BEST enforce?
>
> A. Separation of duties
> B. Least privilege
> C. Need to know
> D. Due care
>
> > [!answer]- Show Answer
> > **B. Least privilege**
> >
> > [[least-privilege|Least privilege]] dictates that users and processes should only have the minimum permissions necessary to perform their function — help desk staff need password reset capability but nothing more. [[separation-of-duties|Separation of duties]] divides critical tasks among multiple people to prevent fraud, but the scenario is about limiting permissions, not splitting responsibilities. [[need-to-know|Need to know]] restricts access to information rather than system permissions. Due care is about acting responsibly to mitigate risks, which is a broader governance concept.
>
> **Q2.** An employee signs a contract with a digital signature, but later claims they never authorized the agreement. The company produces the digitally signed document with a verified certificate chain and timestamp. Which security concept allows the company to prove the employee did sign the document?
>
> A. Integrity
> B. Confidentiality
> C. Non-repudiation
> D. Availability
>
> > [!answer]- Show Answer
> > **C. Non-repudiation**
> >
> > [[non-repudiation|Non-repudiation]] ensures that a party cannot deny having performed an action — digital signatures with verified certificate chains and timestamps provide this proof. Integrity verifies that data has not been altered, which supports non-repudiation but is not the concept of proving who performed an action. Confidentiality prevents unauthorized disclosure and is unrelated to proving authorship. Availability ensures systems are accessible when needed and has nothing to do with proving actions were performed.
>
> **Q3.** Before acquiring a new cloud vendor, a company researches the vendor's security certifications, reviews their SOC 2 reports, and evaluates their incident history. Which governance concept does this activity BEST represent?
>
> A. Due care
> B. Due diligence
> C. Separation of duties
> D. Security through obscurity
>
> > [!answer]- Show Answer
> > **B. Due diligence**
> >
> > [[due-diligence-vs-due-care|Due diligence]] is the process of researching, investigating, and understanding risks before making decisions — reviewing certifications, SOC 2 reports, and incident history is classic due diligence. Due care is acting responsibly to mitigate known risks (implementing controls), which comes after due diligence. Separation of duties divides responsibilities among multiple people and is unrelated to vendor evaluation. Security through obscurity relies on secrecy of design, which is the opposite of transparent vendor review.
>
> **Q4.** A software company publishes the complete source code of its encryption algorithm, arguing that public scrutiny makes the algorithm more secure than keeping it secret. Which security principle does this approach align with?
>
> A. Security through obscurity
> B. Open design principle
> C. Need to know
> D. Least privilege
>
> > [!answer]- Show Answer
> > **B. Open design principle**
> >
> > The [[open-design-principle|open design principle]] states that security mechanisms should not depend on secrecy of implementation — public scrutiny strengthens security by allowing experts to identify flaws. [[security-through-obscurity|Security through obscurity]] is the opposite approach, relying on secrecy of design, which is considered insufficient on its own. Need to know restricts access to information based on role requirements and is unrelated to algorithm transparency. Least privilege limits permissions to the minimum necessary and does not apply to publishing source code.

## Scenario

> See [[case-security-concepts]] for a practical DevOps scenario applying these concepts.
