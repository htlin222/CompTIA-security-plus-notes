---
title: "Business Continuity"
description: "Business continuity planning ensures that critical operations can continue during and after a disruption."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/high
aliases:
  - "BCP"
  - "BC"
---

> [!eli5] ELI5: What is Business Continuity?
> You know how your school has a plan for snow days -- maybe you switch to online classes so learning doesn't stop? Business continuity is the same idea for companies. It's the plan for keeping the important stuff running even when something goes wrong, like a power outage, a big storm, or a computer crash. The goal is to never have to say "sorry, we're closed" when people are counting on you.

## Overview

Business Continuity Planning (BCP) is the proactive process of creating systems and procedures that enable an organization to maintain essential functions during and after a disaster or significant disruption. BCP goes beyond IT recovery to encompass people, processes, facilities, and communications. A well-tested BCP minimizes downtime, protects revenue, and ensures stakeholder confidence.

## Key Concepts

- **[[business-continuity-vs-disaster-recovery|Business continuity vs. disaster recovery]]** — BCP keeps the business running during disruption; DR restores IT systems after disruption
- **[[bia-as-the-foundation|BIA as the foundation]]** — the Business Impact Analysis identifies critical functions and sets recovery priorities
- **Continuity strategies:**
  - **Alternate site types:** hot site (ready immediately), warm site (partially equipped), cold site (empty facility)
  - **Cloud-based recovery** — DRaaS and cloud failover for rapid recovery
  - **Redundant systems** — eliminating single points of failure
- **[[succession-planning|Succession planning]]** — ensuring leadership continuity if key personnel are unavailable
- **[[communication-plan|Communication plan]]** — pre-defined channels and contacts for internal and external stakeholders during a crisis
- **[[order-of-restoration|Order of restoration]]** — critical systems first, based on BIA priorities and RTO requirements
- **Testing types:**
  - **Tabletop exercise** — discussion-based walkthrough of scenarios
  - **Simulation** — role-playing a specific disaster scenario
  - **Parallel test** — recovery systems run alongside production
  - **Full interruption test** — production systems are shut down; most thorough but riskiest
- **[[after-action-review|After-action review]]** — lessons learned documented after each test or actual incident
- **COOP (Continuity of Operations Plan)** — government term for maintaining essential functions during emergencies
- **DRP (Disaster Recovery Plan)** — specific procedures for recovering IT systems after a disaster

## Exam Tips

> [!tip] Remember
> Hot site = most expensive, fastest recovery. Cold site = cheapest, slowest recovery. Tabletop exercises are discussion-only and low-risk. Full interruption tests are the most realistic but carry the highest risk of disruption.

## Connections

- Depends on [[business-impact-analysis]] to identify critical functions and set recovery priorities
- Works in tandem with [[disaster-recovery]] which focuses specifically on restoring IT systems and data
- Related to [[risk-management]] because BCP is a form of risk mitigation for operational disruptions
- See also [[encryption]] for protecting data during backup and recovery processes

## Practice Questions

> [!qbank]- Q-Bank: Business Continuity (4 Questions)
>
> **Q1.** A regional bank wants to validate its business continuity plan without risking any impact to production systems. Stakeholders from multiple departments are available for a half-day session. Which testing method is MOST appropriate?
>
> A. Full interruption test
> B. Parallel test
> C. Tabletop exercise
> D. Simulation test
>
> > [!answer]- Show Answer
> > **C. Tabletop exercise**
> >
> > A [[business-continuity|tabletop exercise]] is a discussion-based walkthrough that carries zero risk to production systems and is ideal for multi-department validation. A full interruption test (A) shuts down production and carries the highest risk. A parallel test (B) runs recovery systems alongside production, which still requires technical effort and some risk. A simulation (D) involves role-playing a scenario with more active participation than a discussion and may involve limited system interaction.
>
> **Q2.** After a major hurricane, a company activates its continuity plan. The CEO is unreachable, and the VP of Operations is also unavailable. The recovery team is unsure who has authority to make decisions. Which BCP element was MOST likely missing?
>
> A. Communication plan
> B. Order of restoration
> C. Succession planning
> D. After-action review
>
> > [!answer]- Show Answer
> > **C. Succession planning**
> >
> > [[succession-planning|Succession planning]] ensures a defined chain of command so that leadership decisions can continue when key personnel are unavailable. A communication plan (A) defines channels and contacts but does not establish decision-making authority. Order of restoration (B) addresses which systems to recover first, not who leads. An after-action review (D) is conducted after an event, not during.
>
> **Q3.** An e-commerce company requires near-zero downtime for its storefront during the holiday shopping season. Budget is not a primary concern. Which continuity strategy BEST meets this requirement?
>
> A. Cold site
> B. Warm site
> C. Hot site
> D. Reciprocal agreement with a partner company
>
> > [!answer]- Show Answer
> > **C. Hot site**
> >
> > A [[business-continuity|hot site]] is a fully operational duplicate facility that enables near-zero RTO, making it ideal when downtime is unacceptable and budget is flexible. A cold site (A) has the longest recovery time and is cheapest. A warm site (B) requires additional setup time for data and configuration. A reciprocal agreement (D) depends on another organization's capacity and offers no guarantee of immediate availability.
>
> **Q4.** Following a successful recovery from a data center fire, the IT director wants to capture what went well and what needs improvement. Which BCP activity should be performed FIRST?
>
> A. Update the risk register
> B. Conduct an after-action review
> C. Schedule a full interruption test
> D. Revise the communication plan
>
> > [!answer]- Show Answer
> > **B. Conduct an after-action review**
> >
> > An [[after-action-review|after-action review]] captures lessons learned while the experience is fresh, documenting successes and gaps to improve the plan. Updating the risk register (A) may follow the review but should not come first. Scheduling a full interruption test (C) is a future activity unrelated to capturing current lessons. Revising the communication plan (D) may be one outcome of the review but should not precede the review itself.

## Scenario

> See [[case-business-continuity]] for a practical DevOps scenario applying these concepts.
