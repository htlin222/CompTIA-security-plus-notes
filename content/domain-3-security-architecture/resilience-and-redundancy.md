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

## Exam Tips

> [!tip] Remember
> RAID 0 = no redundancy (just performance). RAID 1 = mirror. RAID 5 = minimum 3 disks, survives 1 failure. RAID 10 = best of both. UPS provides short-term power; generators provide long-term. Active-active = both nodes serve traffic.

## Connections

- Provides the architectural foundation for [[disaster-recovery]] and [[business-continuity]] plans
- [[load-balancers-and-proxies]] implement server redundancy and failover at the network level
- See also [[cloud-security]] where resilience is achieved through multi-region and multi-AZ deployments

## Scenario

> See [[case-resilience-and-redundancy]] for a practical DevOps scenario applying these concepts.
