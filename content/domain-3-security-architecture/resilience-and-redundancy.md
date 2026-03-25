---
title: "Resilience and Redundancy"
description: "Resilience and redundancy ensure systems remain available and operational through fault tolerance, high availability, and recovery mechanisms."
draft: false
date: 2026-03-20
tags:
  - domain/3
  - concept/network
  - weight/high
aliases:
  - "Resilience"
  - "Redundancy"
  - "High Availability"
---

> [!eli5] ELI5: What are Resilience and Redundancy?
> Have you ever noticed that airplanes have two engines when they really only need one to fly? That extra engine is redundancy -- a backup in case the first one fails. Resilience is the plane's ability to keep flying safely even when something goes wrong. In the computer world, this means having backup systems, extra copies of important data, and plans that kick in automatically so everything keeps working even during problems.

## Overview

Resilience is the ability of a system to continue operating during adverse conditions, while redundancy eliminates single points of failure by duplicating critical components. Together, they ensure high availability and minimize downtime. Resilient architectures combine redundant hardware, diverse network paths, automated failover, and geographic distribution to withstand failures, attacks, and disasters.

## Key Concepts

- **[[high-availability-ha|High availability (HA)]]** — measured in "nines" (99.9% = 8.76 hours downtime/year; 99.999% = 5.26 minutes/year)
- **Redundancy types:**
  - **Server redundancy** — clustering, load balancing, active-active or active-passive configurations
  - **Storage redundancy — RAID levels:**
    - **RAID 0** — striping, no redundancy; performance only
    - **RAID 1** — mirroring; full duplicate on second disk
    - **RAID 5** — striping with parity; can survive one disk failure; minimum 3 disks
    - **RAID 6** — striping with double parity; can survive two disk failures
    - **RAID 10 (1+0)** — mirroring + striping; high performance and redundancy
  - **Network redundancy** — dual ISPs, redundant switches/routers, link aggregation, diverse paths
  - **Power redundancy** — UPS (Uninterruptible Power Supply), generators, dual power supplies, PDUs
  - **Geographic redundancy** — multiple data centers in different locations
- **[[failover|Failover]]** — automatic switching to a standby system when the primary fails
- **[[failback|Failback]]** — returning to the primary system after it is restored
- **[[diversity|Diversity]]** — using different vendors, technologies, or paths to avoid common-mode failures
- **[[capacity-planning|Capacity planning]]** — ensuring sufficient resources to handle peak loads and growth
- **[[scalability|Scalability]]** — vertical (scale up: more resources) vs. horizontal (scale out: more instances)
- **[[non-persistence|Non-persistence]]** — systems rebuilt from known-good images; live boot media, revert to snapshot
- **NIC teaming** — combining multiple network interfaces for redundancy and increased throughput
- **SAN replication** — copying storage area network data between sites for disaster recovery
- **Backup types** — full (all data), incremental (changes since last backup), differential (changes since last full backup)

## Exam Tips

> [!tip] Remember
> RAID 0 = no redundancy (just performance). RAID 1 = mirror. RAID 5 = minimum 3 disks, survives 1 failure. RAID 10 = best of both. UPS provides short-term power; generators provide long-term. Active-active = both nodes serve traffic.

## Connections

- Provides the architectural foundation for [[disaster-recovery]] and [[business-continuity]] plans
- [[load-balancers-and-proxies]] implement server redundancy and failover at the network level
- See also [[cloud-security]] where resilience is achieved through multi-region and multi-AZ deployments

## Practice Questions

> [!qbank]- Q-Bank: Resilience and Redundancy (4 Questions)
>
> **Q1.** A database administrator needs a RAID configuration that can survive the failure of one disk while providing storage efficiency across a minimum of three disks. Which RAID level BEST meets this requirement?
>
> A. RAID 0
> B. RAID 1
> C. RAID 5
> D. RAID 10
>
> > [!answer]- Show Answer
> > **C. RAID 5**
> >
> > [[resilience-and-redundancy|RAID 5]] uses striping with distributed parity across a minimum of three disks and can survive one disk failure while providing good storage efficiency. RAID 0 (A) provides striping with no redundancy — any disk failure causes total data loss. RAID 1 (B) mirrors between two disks but does not provide storage efficiency. RAID 10 (D) requires a minimum of four disks and uses mirroring plus striping, offering less storage efficiency.
>
> **Q2.** A company's primary data center experiences a power outage. The UPS systems keep servers running for 15 minutes while diesel generators start up and provide long-term power. Which resilience concept does this demonstrate?
>
> A. Geographic redundancy
> B. Power redundancy with layered backup systems
> C. Network link aggregation
> D. Non-persistence through revert to snapshot
>
> > [!answer]- Show Answer
> > **B. Power redundancy with layered backup systems**
> >
> > [[resilience-and-redundancy|Power redundancy]] uses UPS for short-term battery backup and generators for long-term power, providing layered protection against outages. Geographic redundancy (A) involves multiple data center locations. Link aggregation (C) combines network connections for bandwidth and redundancy. Non-persistence (D) relates to rebuilding systems from known-good images, not power backup.
>
> **Q3.** An organization deploys two identical web server clusters — both actively serving traffic simultaneously. If one cluster fails, the other handles all requests. Which high availability configuration is this?
>
> A. Active-passive
> B. Active-active
> C. Cold standby
> D. Manual failover
>
> > [!answer]- Show Answer
> > **B. Active-active**
> >
> > [[active-active-vs-active-passive|Active-active]] means both nodes are actively serving traffic simultaneously, with either capable of handling the full load if the other fails. Active-passive (A) has a standby node that only activates when the primary fails. Cold standby (C) requires manual startup of the backup system. Manual failover (D) requires human intervention, which is not described in this scenario.
>
> **Q4.** A security architect recommends using different firewall vendors at the network perimeter and internal boundaries to reduce the risk of a single vulnerability affecting all firewalls. Which resilience concept does this represent?
>
> A. Scalability
> B. Non-persistence
> C. Diversity
> D. Capacity planning
>
> > [!answer]- Show Answer
> > **C. Diversity**
> >
> > [[diversity|Diversity]] means using different vendors, technologies, or paths to avoid common-mode failures — a vulnerability in one vendor's product will not affect the other. Scalability (A) refers to adding resources to handle growth. Non-persistence (B) involves rebuilding systems from known-good images. Capacity planning (D) ensures sufficient resources for current and future demands but does not address vendor diversification.

## Scenario

> See [[case-resilience-and-redundancy]] for a practical DevOps scenario applying these concepts.
