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

## Exam Tips

> [!tip] Remember
> Hot site = most expensive, fastest recovery. Cold site = cheapest, slowest recovery. Tabletop exercises are discussion-only and low-risk. Full interruption tests are the most realistic but carry the highest risk of disruption.

## Connections

- Depends on [[business-impact-analysis]] to identify critical functions and set recovery priorities
- Works in tandem with [[disaster-recovery]] which focuses specifically on restoring IT systems and data
- Related to [[risk-management]] because BCP is a form of risk mitigation for operational disruptions
- See also [[encryption]] for protecting data during backup and recovery processes

## Scenario

> See [[case-business-continuity]] for a practical DevOps scenario applying these concepts.
