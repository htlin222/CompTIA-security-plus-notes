---
title: "Maximum Tolerable Downtime (MTD)"
description: "the longest period a function can be unavailable before causing irreversible damage"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Maximum Tolerable Downtime (MTD), sometimes called Maximum Tolerable Period of Disruption (MTPD), is the longest period of time a critical business function can be unavailable before the organization suffers irreversible harm — such as bankruptcy, regulatory action, permanent customer loss, or safety emergencies. MTD establishes the absolute outer boundary for recovery; the RTO must always be less than the MTD.

## Key Details

- MTD > RTO: the RTO is the target recovery time; MTD is the absolute deadline — exceeding MTD means catastrophic consequences
- Different functions have different MTDs: e-commerce payment processing might be 4 hours; email might be 24 hours; physical document archiving might be 30 days
- MTD is determined during the BIA by interviewing business unit owners about the consequences of extended downtime
- If RTO equals or exceeds MTD, the DR plan is inadequate and must be improved
- Exam tip: know the relationship: MTD ≥ RTO ≥ WRT (Work Recovery Time); this hierarchy is testable

## Connections

- Parent: [[business-impact-analysis]] — MTD is a key BIA metric defining the outer boundary for recovery
- See also: [[recovery-time-objective-rto]]
- See also: [[recovery-point-objective-rpo]]
