---
title: "Disaster Recovery"
description: "Disaster recovery focuses on restoring IT systems, data, and infrastructure after a disruption to resume normal operations."
draft: false
date: 2026-03-20
tags:
  - domain/5
  - concept/risk
  - weight/high
aliases:
  - "DR"
  - "DRP"
---

> [!eli5] ELI5: What is Disaster Recovery?
> Remember when your phone died and you were relieved your photos were backed up to the cloud? Disaster recovery is a company's plan to get its computers, files, and systems back up and running after something really bad happens -- like a flood, a fire, or a big cyberattack. It spells out exactly what to do, who does it, and in what order, so the company can get back to normal as fast as possible.

## Overview

Disaster Recovery (DR) is the subset of business continuity that specifically addresses restoring IT infrastructure, systems, and data after a catastrophic event. A Disaster Recovery Plan (DRP) defines the procedures, responsibilities, and technologies needed to recover from outages caused by natural disasters, cyberattacks, hardware failures, or human error. The DRP must be regularly tested and updated.

## Key Concepts

- **Recovery sites:**
  - **Hot site** — fully operational duplicate; near-zero RTO; highest cost
  - **Warm site** — hardware in place but needs data and configuration; moderate RTO and cost
  - **Cold site** — facility with power and connectivity only; longest RTO; lowest cost
  - **Cloud site** — on-demand recovery infrastructure via IaaS or DRaaS
- **Backup strategies:**
  - **Full backup** — complete copy of all data; longest time, most storage, fastest restore
  - **Incremental backup** — only data changed since last backup of any type; fastest backup, slowest restore
  - **Differential backup** — data changed since last full backup; moderate backup and restore times
  - **Snapshot** — point-in-time image of a system or volume
- **[[replication|Replication]]** — real-time or near-real-time copying of data to a secondary location
- **[[geographic-considerations|Geographic considerations]]** — off-site backups protect against regional disasters; consider distance and latency
- **[[3-2-1-backup-rule|3-2-1 backup rule]]** — 3 copies of data, on 2 different media types, with 1 copy off-site
- **[[testing-the-drp|Testing the DRP]]** — same test types as BCP (tabletop, simulation, parallel, full interruption)
- **[[documentation|Documentation]]** — recovery procedures, contact lists, system dependencies, vendor information

## Exam Tips

> [!tip] Remember
> Incremental = fastest to back up, slowest to restore (needs all incrementals + last full). Differential = moderate both ways (needs last full + last differential only). The 3-2-1 rule is a favorite exam topic.

## Connections

- Complements [[business-continuity]] by handling the technical recovery of IT systems
- Uses metrics from [[business-impact-analysis]] (RTO, RPO, MTD) to define recovery requirements
- See also [[resilience-and-redundancy]] for the architectural controls that minimize the need for disaster recovery

## Scenario

> See [[case-disaster-recovery]] for a practical DevOps scenario applying these concepts.
