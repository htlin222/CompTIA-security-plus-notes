---
title: "Ad hoc vs. recurring vs. continuous"
description: "assessments may be triggered by events, scheduled, or ongoing"
draft: false
date: 2026-03-20
tags:
  - domain/5
  - type/sub-topic
---

> [!eli5] ELI5: What is Ad Hoc vs. Recurring vs. Continuous?
> Ad hoc is checking your bike after you crash. Recurring is checking it every Saturday. Continuous is having a sensor that beeps the moment something goes wrong. Companies check their security the same three ways.

## Definition

Risk and security assessments can be performed on three schedules: ad hoc assessments are triggered by a specific event (e.g., a breach, new system deployment, or regulatory change); recurring assessments happen on a defined schedule (e.g., annual penetration tests or quarterly vulnerability scans); and continuous assessments use automated tooling to monitor the environment in real time. Each approach has trade-offs in cost, depth, and timeliness.

## Key Details

- **Ad hoc**: triggered by events such as mergers, incidents, or new threat intelligence — unplanned but necessary
- **Recurring**: scheduled at regular intervals (annual, quarterly, monthly); required by many compliance frameworks (PCI DSS, HIPAA)
- **Continuous**: automated monitoring tools (SIEM, vulnerability scanners) provide real-time visibility; closest to true situational awareness
- Continuous assessments do not replace periodic deep assessments; they complement them
- Exam tip: compliance frameworks often mandate *at least* recurring assessments; continuous is considered a maturity best practice

## Connections

- Parent: [[risk-assessment]] — describes the scheduling dimension of risk assessment activities
- See also: [[compliance-monitoring]]
- See also: [[vulnerability-assessment]]
