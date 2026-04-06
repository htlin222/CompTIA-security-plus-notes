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

## Practice Questions

> [!qbank]- Q-Bank: Disaster Recovery (4 Questions)
>
> **Q1.** An organization performs a full backup every Sunday night and incremental backups every other night. A server fails on Thursday morning. Which backups are needed to restore the system?
>
> A. Sunday's full backup only
> B. Sunday's full backup and Wednesday's incremental backup only
> C. Sunday's full backup and Monday through Wednesday's incremental backups
> D. The most recent incremental backup only
>
> > [!answer]- Show Answer
> > **C. Sunday's full backup and Monday through Wednesday's incremental backups**
> >
> > [[disaster-recovery|Incremental backups]] capture only data changed since the last backup of any type, so restoring requires the last full backup plus every subsequent incremental. Only using Sunday's full (A) would lose Monday through Wednesday's data. Using only the full plus Wednesday's incremental (B) describes how differential backups work, not incremental. Using only the last incremental (D) would contain only Wednesday's changes and miss all prior data.
>
> **Q2.** A startup needs a disaster recovery site but has a very limited budget and can tolerate a recovery time of several days. Which site type BEST fits these constraints?
>
> A. Hot site
> B. Warm site
> C. Cold site
> D. Cloud site with real-time replication
>
> > [!answer]- Show Answer
> > **C. Cold site**
> >
> > A [[disaster-recovery|cold site]] provides only basic facilities (power, connectivity, space) at the lowest cost, making it appropriate when budget is tight and longer recovery times are acceptable. A hot site (A) is the most expensive option with near-zero RTO. A warm site (B) is moderately priced but still more costly than a cold site. A cloud site with real-time replication (D) would also be expensive and exceeds the startup's needs.
>
> **Q3.** A security architect is designing a backup strategy for a financial trading platform. The business requires that no more than one copy be stored off-site and that at least two different media types be used. Which backup principle are they implementing?
>
> A. Incremental backup strategy
> B. Geographic redundancy
> C. 3-2-1 backup rule
> D. Real-time replication
>
> > [!answer]- Show Answer
> > **C. 3-2-1 backup rule**
> >
> > The [[3-2-1-backup-rule|3-2-1 backup rule]] specifies 3 copies of data, on 2 different media types, with 1 copy off-site -- matching the described requirements. Incremental backup strategy (A) defines how backups are taken, not storage diversity. Geographic redundancy (B) addresses location but not media diversity. Real-time replication (D) provides continuous data protection but does not describe the overall backup architecture with media and location requirements.
>
> **Q4.** After restoring systems at a warm site following a flood, the disaster recovery team wants to verify that the DRP worked correctly and identify areas for improvement. What should they do FIRST?
>
> A. Immediately fail back to the primary site
> B. Conduct a full interruption test at the warm site
> C. Document lessons learned and conduct an after-action review
> D. Switch to a hot site for better protection
>
> > [!answer]- Show Answer
> > **C. Document lessons learned and conduct an after-action review**
> >
> > [[testing-the-drp|Testing the DRP]] includes post-event review. Documenting lessons learned while experience is fresh ensures the plan improves for next time. Immediately failing back (A) is premature before validating the primary site is safe and captures no lessons. Conducting a full interruption test (B) at the warm site adds unnecessary risk during recovery. Switching to a hot site (D) changes the recovery strategy without first understanding what worked and what did not.

## Scenario

> See [[case-disaster-recovery]] for a practical DevOps scenario applying these concepts.

## Resources

- **Professor Messer's SY0-701 Security+ Course**
  - [3.4 – Recovery Testing](https://www.youtube.com/watch?v=IhT7Odu4xHc)
