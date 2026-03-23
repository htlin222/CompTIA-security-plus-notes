---
title: "Recovery Time Objective (RTO)"
description: "the target time to restore a function after disruption; must be less than MTD"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Recovery Time Objective (RTO) is the maximum acceptable length of time that a business function, application, or system can be offline after a disruption before causing unacceptable business impact. It is set during the Business Impact Analysis (BIA) and must always be less than the Maximum Tolerable Downtime (MTD). RTO drives the design of recovery capabilities — the tighter the RTO, the more investment in hot standby systems, failover automation, and recovery staff.

## Key Details

- RTO must always be less than MTD: if RTO ≥ MTD, the recovery plan is inadequate
- Short RTO (minutes to hours) requires hot sites, automated failover, and active-active clustering
- Longer RTO (days) may allow warm or cold site recovery approaches
- Different systems within an organization will have different RTOs based on their criticality
- Exam tip: RTO = maximum downtime; RPO = maximum data loss; MTD = absolute outer limit; know all three relationships

## Connections

- Parent: [[business-impact-analysis]] — RTO is the primary time constraint that drives DR architecture decisions
- See also: [[recovery-point-objective-rpo]]
- See also: [[maximum-tolerable-downtime-mtd]]
