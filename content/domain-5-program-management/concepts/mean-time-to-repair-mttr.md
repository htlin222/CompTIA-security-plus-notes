---
title: "Mean Time to Repair (MTTR)"
description: "average time to fix a failed component"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
aliases:
  - MTTR
---

> [!eli5] ELI5: What is Mean Time to Repair?
> This measures how fast you can fix your bike after it breaks. The quicker you patch the tire and get riding again, the better your repair time.

## Definition

Mean Time to Repair (MTTR) is the average time required to repair or restore a failed component or system to full operational status, measured from the time of failure to the time of restoration. MTTR includes diagnosis time, repair or replacement time, and any testing needed to confirm restoration. A lower MTTR indicates a faster recovery capability. MTTR is used alongside MTBF to calculate system availability and to validate that recovery capabilities align with RTO targets.

## Key Details

- Formula: MTTR = Total Repair Time / Number of Repairs
- System Availability = MTBF / (MTBF + MTTR); higher MTBF and lower MTTR both improve availability
- MTTR informs DR planning: if MTTR exceeds RTO for a critical system, additional resilience measures (redundancy, hot standby) are needed
- Reducing MTTR: pre-positioned spare parts, trained on-call staff, runbooks, automated failover mechanisms
- Exam tip: MTTR is the repair/restore time; MTBF is the time between failures; both appear in BIA/DR calculations

## Connections

- Parent: [[business-impact-analysis]] — MTTR is a key availability metric used in BIA and DR planning
- See also: [[mean-time-between-failures-mtbf]]
- See also: [[recovery-time-objective-rto]]
