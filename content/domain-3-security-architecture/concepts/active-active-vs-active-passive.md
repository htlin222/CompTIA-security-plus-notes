---
title: "Active-active vs. active-passive"
description: "active-active uses all nodes; active-passive has standby nodes for failover"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Active-active vs. active-passive?
> Active-active is like having two cashiers both ringing up customers at the same time. Active-passive is like having one cashier working while a second one sits nearby, ready to jump in only if the first one needs a break.

## Definition

In load balancing and high availability clustering, active-active configurations distribute traffic across all nodes simultaneously so every node is handling requests at all times. Active-passive configurations keep one or more nodes on standby that only take over if the primary node fails. The choice between them involves trade-offs between resource utilization and simplicity of failover.

## Key Details

- Active-active: better resource utilization, all nodes process traffic, more complex to configure
- Active-passive: standby nodes sit idle until failover, simpler but wastes capacity
- Active-active provides higher throughput; active-passive provides simpler failover logic
- Both configurations eliminate single points of failure
- Failover time is typically faster in active-active since no node needs to "wake up"

## Connections

- Parent: [[load-balancers-and-proxies]] — load balancer clustering uses these deployment modes
- See also: [[failover]]
