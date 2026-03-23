---
title: "Business Impact Analysis"
description: "BIA identifies critical business functions and quantifies the impact of their disruption to prioritize recovery efforts."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/high
aliases:
  - "BIA"
---

## Overview

A Business Impact Analysis (BIA) is a systematic process for determining the potential effects of an interruption to critical business operations. It identifies which processes are most vital, quantifies the financial and operational impact of downtime, and establishes recovery priorities. The BIA is a foundational input to both business continuity and disaster recovery planning.

## Key Concepts

- **[[critical-business-functions|Critical business functions]]** — processes that, if disrupted, would cause significant harm to the organization
- **[[maximum-tolerable-downtime-mtd|Maximum Tolerable Downtime (MTD)]]** — the longest period a function can be unavailable before causing irreversible damage
- **[[recovery-time-objective-rto|Recovery Time Objective (RTO)]]** — the target time to restore a function after disruption; must be less than MTD
- **[[recovery-point-objective-rpo|Recovery Point Objective (RPO)]]** — the maximum acceptable data loss measured in time (e.g., 4 hours of transactions)
- **[[mean-time-to-repair-mttr|Mean Time to Repair (MTTR)]]** — average time to fix a failed component
- **[[mean-time-between-failures-mtbf|Mean Time Between Failures (MTBF)]]** — average time a system operates before failing
- **[[single-point-of-failure-spof|Single point of failure (SPOF)]]** — any component whose failure would bring down an entire system
- **[[impact-categories|Impact categories]]** — financial loss, reputational damage, regulatory penalties, safety, operational disruption
- **[[dependencies|Dependencies]]** — upstream and downstream systems that a critical function relies on

## Exam Tips

> [!tip] Remember
> RTO < MTD always. RPO is about data loss, RTO is about downtime. If RPO = 0, you need real-time replication. The exam frequently tests the relationship between these metrics.

## Connections

- Directly informs [[business-continuity]] by setting recovery priorities and acceptable downtime thresholds
- Feeds into [[disaster-recovery]] to determine which systems need the fastest recovery and what replication strategy to use
- Supports [[risk-management]] by quantifying the financial impact of threats in dollar terms

## Scenario

> See [[case-business-impact-analysis]] for a practical DevOps scenario applying these concepts.
