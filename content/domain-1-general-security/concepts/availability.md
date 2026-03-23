---
title: "Availability"
description: "Ensuring systems and data are accessible to authorized users when needed"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

Availability is the third pillar of the CIA Triad, ensuring that systems, services, and data are accessible and functional for authorized users when they are needed. Threats to availability include DoS/DDoS attacks, hardware failures, ransomware, and natural disasters. Controls that protect availability include redundancy, backups, failover systems, and business continuity planning.

## Key Details

- Measured by **uptime** and **SLA (Service Level Agreement)** targets (e.g., 99.9% = ~8.7 hours downtime/year).
- Primary threats: **DoS/DDoS attacks**, **ransomware**, **hardware failure**, **power outages**, **natural disasters**.
- Key controls: **RAID**, **clustering/failover**, **UPS (Uninterruptible Power Supply)**, **geographic redundancy**, **backups**.
- **RTO (Recovery Time Objective)** and **RPO (Recovery Point Objective)** are key availability metrics in BCPs.
- Balancing availability with confidentiality is a common security challenge—overly strict controls can reduce availability.

## Connections

- Parent: [[cia-triad]] — the "A" in CIA Triad
- See also: [[confidentiality]], [[integrity]]
