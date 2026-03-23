---
title: "Failback"
description: "returning to the primary system after it is restored"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Failback?
> When your main bike gets a flat tire, you ride your backup bike. Failback is when the flat tire is fixed and you switch back to riding your main bike again.

## Definition

Failback is the process of returning operations back to the primary system after it has been restored to normal functioning following a failure event that caused a failover to the secondary/standby system. Failback must be carefully planned and executed to minimize disruption, as moving traffic back to the primary involves another transition period and potential brief service interruption.

## Key Details

- Failback is the reverse of failover — it returns services to the original primary infrastructure
- Must be carefully planned: verify primary is fully functional before initiating failback
- May involve data synchronization from secondary back to primary (especially after extended failover)
- Should be scheduled during low-traffic periods to minimize user impact
- Some organizations choose to keep operating on secondary infrastructure until a maintenance window

## Connections

- Parent: [[resilience-and-redundancy]] — failback is the complement to failover in resilient system design
- See also: [[failover]]
