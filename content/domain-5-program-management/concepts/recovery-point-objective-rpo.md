---
title: "Recovery Point Objective (RPO)"
description: "the maximum acceptable data loss measured in time (e.g., 4 hours of transactions)"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

## Definition

Recovery Point Objective (RPO) is the maximum amount of data loss an organization can tolerate, expressed as a time period. It answers the question: "How much data can we afford to lose?" For example, an RPO of 4 hours means the organization can tolerate losing up to 4 hours of transactions or updates. RPO directly determines how frequently backups or replication must occur — a 4-hour RPO requires backups or synchronization at least every 4 hours.

## Key Details

- RPO is set during the BIA for each critical business function
- Shorter RPO → more frequent backups → higher cost; organizations must balance RPO with backup infrastructure investment
- Real-time replication achieves near-zero RPO; daily backups support RPO of ~24 hours
- RPO ≠ RTO: RPO is about data loss; RTO is about system downtime
- Exam tip: RPO determines *backup frequency*; a 1-hour RPO means backups or replication must occur at least hourly

## Connections

- Parent: [[business-impact-analysis]] — RPO is a key BIA metric that drives backup strategy design
- See also: [[recovery-time-objective-rto]]
- See also: [[replication]]
