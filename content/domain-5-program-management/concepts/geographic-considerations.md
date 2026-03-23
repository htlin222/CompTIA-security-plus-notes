---
title: "Geographic considerations"
description: "different jurisdictions have different requirements; data sovereignty matters"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What are Geographic Considerations?
> Different countries have different rules, just like different schools have different dress codes. Where your data is stored matters because it has to follow the laws of that place, and your backup should be far enough away that the same flood can't hit both copies.

## Definition

Geographic considerations in compliance and disaster recovery recognize that different countries, states, and regions impose different legal and regulatory requirements on how data is handled, stored, and transferred. Data sovereignty refers to the principle that data is subject to the laws of the country in which it resides. Additionally, geographic considerations in DR include selecting off-site backup and recovery locations that are far enough to avoid regional disasters but close enough for practical access.

## Key Details

- **Data sovereignty**: data stored in the EU is subject to GDPR; data stored in China may be subject to the Cybersecurity Law of China
- **Data residency requirements**: some regulations (e.g., GDPR) restrict cross-border data transfers; mechanisms like SCCs (Standard Contractual Clauses) and adequacy decisions govern transfers
- **DR geography**: backup sites should be far enough to avoid the same natural disaster (hurricane, earthquake) but not so far that network latency impairs replication
- Multi-national organizations must navigate overlapping and sometimes conflicting regulatory requirements
- Exam tip: geographic considerations appear in both compliance (data sovereignty) and DR (site selection) contexts on Security+

## Connections

- Parent: [[compliance]] — geographic factors affect which regulations apply and how data must be handled
- Parent: [[disaster-recovery]] — site selection in DR requires careful geographic planning
- See also: [[gdpr]]
- See also: [[replication]]
