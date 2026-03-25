---
title: "Governance"
description: "Security governance establishes the framework of policies, roles, and processes that guide an organization's security program."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/compliance
  - weight/high
aliases:
  - "Security Governance"
---

> [!eli5] ELI5: What is Governance?
> Every school has a principal who sets the rules, teachers who enforce them, and a student handbook that explains what's expected. Security governance works the same way for a company. The leaders at the top decide what the security rules should be, who's in charge of what, and how much risk the company is okay with. Without this structure, everyone would make up their own rules and things would get messy fast.

## Overview

Security governance is the set of responsibilities, policies, and procedures an organization follows to manage and oversee its information security strategy. It ensures that security efforts align with business objectives and that leadership is accountable for risk decisions. Governance provides the top-down structure from which all security policies, standards, and guidelines flow.

## Key Concepts

- **[[board-and-executive-involvement|Board and executive involvement]]** — governance starts at the top; senior leadership sets the tone and approves risk appetite
- **[[policies-standards-baselines-guidelines-procedures|Policies, standards, baselines, guidelines, procedures]]** — the governance hierarchy from most authoritative to most flexible
- **[[roles-and-responsibilities|Roles and responsibilities]]** — CISO, data owner, data custodian, data steward, data processor, data controller
- **[[governance-committees|Governance committees]]** — cross-functional groups that review security posture, approve policy changes, and allocate budgets
- **[[centralized-vs-decentralized-governance|Centralized vs. decentralized governance]]** — centralized offers consistency; decentralized gives business units flexibility
- **[[monitoring-and-reporting|Monitoring and reporting]]** — KPIs and KRIs measure governance effectiveness and communicate risk to leadership
- **[[due-diligence-vs-due-care|Due diligence vs. due care]]** — diligence is researching and understanding risks; care is acting on that knowledge
- **Control types by category** — managerial (policies, risk assessments), operational (training, procedures, guards), technical (firewalls, encryption, ACLs)
- **Control types by function** — preventive (block threats), detective (identify incidents), corrective (fix after incident), deterrent (discourage), compensating (alternative when primary control isn't feasible), physical (locks, fences, cameras)

## Exam Tips

> [!tip] Remember
> Governance = "who decides and how." Policies say what to do; standards say how; guidelines suggest; procedures give step-by-step. The exam loves asking about the hierarchy and who owns what.

## Connections

- Foundational to [[security-policies]] because governance defines the authority behind all policies
- Directly supports [[compliance]] by providing the structure that ensures regulatory requirements are met
- Works alongside [[risk-management]] to ensure risk decisions are made at the appropriate organizational level
- See also [[regulations-and-frameworks]] for the external drivers that shape governance requirements

## Practice Questions

> [!qbank]- Q-Bank: Governance (4 Questions)
>
> **Q1.** A company's board of directors approves a statement defining the maximum level of cybersecurity risk the organization is willing to accept in pursuit of its strategic objectives. This statement BEST represents which governance concept?
>
> A. Security policy
> B. Risk appetite
> C. Baseline configuration
> D. Due care
>
> > [!answer]- Show Answer
> > **B. Risk appetite**
> >
> > Risk appetite is set by senior leadership and defines the organization's overall willingness to take risk, which is a core [[governance]] responsibility. A security policy (A) defines rules for protecting assets but is not specifically about acceptable risk levels. A baseline configuration (C) is a minimum technical standard for systems. Due care (D) is acting responsibly on known risks, not defining acceptable risk thresholds.
>
> **Q2.** A CISO discovers that different business units have implemented conflicting password requirements. Some require 8 characters, others require 14, and one unit has no policy at all. This situation is MOST likely caused by which governance model?
>
> A. Centralized governance
> B. Decentralized governance
> C. Governance committees
> D. Board-level oversight
>
> > [!answer]- Show Answer
> > **B. Decentralized governance**
> >
> > [[centralized-vs-decentralized-governance|Decentralized governance]] gives business units flexibility to set their own requirements, which can lead to inconsistency like conflicting password policies. Centralized governance (A) enforces uniform standards across the organization. Governance committees (C) are cross-functional groups that review policies but do not inherently cause inconsistency. Board-level oversight (D) sets strategic direction but does not directly determine how individual policies are implemented.
>
> **Q3.** Before adopting a new cloud provider, an organization's security team researches the provider's certifications, reviews its SOC 2 report, and evaluates its security architecture. This activity BEST represents which concept?
>
> A. Due care
> B. Due diligence
> C. Compliance monitoring
> D. Attestation
>
> > [!answer]- Show Answer
> > **B. Due diligence**
> >
> > [[due-diligence-vs-due-care|Due diligence]] is the process of researching and understanding risks before making a decision. Investigating a provider's security posture before adoption is a classic example. Due care (A) is acting on knowledge to implement appropriate safeguards, which comes after due diligence. Compliance monitoring (C) is ongoing verification of control effectiveness, not pre-decision research. Attestation (D) is a formal auditor declaration about control effectiveness.
>
> **Q4.** An organization creates a cross-functional team that includes representatives from IT, legal, finance, and HR to review security posture quarterly and approve policy changes. This team is BEST described as a:
>
> A. Incident response team
> B. Governance committee
> C. Audit team
> D. Risk management office
>
> > [!answer]- Show Answer
> > **B. Governance committee**
> >
> > A [[governance-committees|governance committee]] is a cross-functional group that reviews security posture, approves policy changes, and allocates budgets -- exactly matching this description. An incident response team (A) handles active security incidents, not ongoing policy governance. An audit team (C) evaluates controls against standards but does not approve policy changes. A risk management office (D) focuses specifically on risk identification and response, not broad governance decisions.

## Scenario

> See [[case-governance]] for a practical DevOps scenario applying these concepts.
