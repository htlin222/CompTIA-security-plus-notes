---
title: "Failover"
description: "automatic switching to a standby system when the primary fails"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Failover?
> Failover is like having a spare tire that automatically puts itself on the car the moment the main tire goes flat. The system switches to a backup so fast that you barely notice anything went wrong.

## Definition

Failover is the automatic or manual process of switching from a failed primary system to a standby secondary system in order to maintain service continuity. Automatic failover detects failure via health monitoring and switches without human intervention; manual failover requires an administrator to initiate the switch. The speed and reliability of failover is a key component of high availability (HA) design.

## Key Details

- Automatic failover minimizes downtime by eliminating human response time
- Failover time (RTO) depends on detection time + failover execution time
- Active-passive clustering is the most common failover architecture
- Clustering software (Windows Server Failover Clustering, Pacemaker) manages automatic failover
- DNS failover and load balancer health checks can redirect traffic at the network level

## Connections

- Parent: [[resilience-and-redundancy]] — failover is the core mechanism for achieving high availability
- See also: [[active-active-vs-active-passive]]
