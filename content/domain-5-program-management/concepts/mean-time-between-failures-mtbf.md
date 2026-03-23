---
title: "Mean Time Between Failures (MTBF)"
description: "average time a system operates before failing"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
aliases:
  - MTBF
---

> [!eli5] ELI5: What is Mean Time Between Failures?
> Think of it as tracking how many days your bike goes before the chain falls off again. A bigger number means your bike is more reliable.

## Definition

Mean Time Between Failures (MTBF) is a reliability metric that represents the average time a repairable system or component operates between failures. A higher MTBF indicates a more reliable system. MTBF is used in BIA and DR planning to predict how frequently a system is likely to fail and to help justify redundancy investments for critical systems with low MTBF values.

## Key Details

- Formula: MTBF = Total Operating Time / Number of Failures
- MTBF applies to **repairable** systems (contrast with MTTF — Mean Time to Failure — used for non-repairable components like hard drives)
- High MTBF → high reliability → lower risk of unexpected downtime
- Low MTBF systems are candidates for redundancy (RAID, load balancing, clustering) to maintain availability
- Exam tip: MTBF measures reliability between failures; MTTR measures how long it takes to fix a failure; both are used together in availability calculations

## Connections

- Parent: [[business-impact-analysis]] — MTBF informs availability risk assessments during the BIA
- See also: [[mean-time-to-repair-mttr]]
- See also: [[single-point-of-failure-spof]]
