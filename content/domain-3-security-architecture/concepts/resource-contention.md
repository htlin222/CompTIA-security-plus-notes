---
title: "Resource contention"
description: "VMs competing for shared CPU, memory, storage, and network resources"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

Resource contention in virtualized environments occurs when multiple virtual machines compete for the same underlying physical resources (CPU, memory, disk I/O, network bandwidth) on a shared host. Severe contention can degrade performance, cause availability issues, and potentially enable side-channel attacks where information about one VM's activity leaks through shared resource usage patterns.

## Key Details

- CPU contention: multiple VMs competing for physical CPU cores; managed with CPU scheduling and reservation policies
- Memory contention: hypervisor may use memory ballooning, transparent page sharing, or swapping under pressure
- Storage I/O contention: multiple VMs sharing the same storage array can create I/O bottlenecks
- "Noisy neighbor" effect: a high-load VM degrades performance for co-located VMs
- Resource pools, reservations, limits, and shares in hypervisors manage resource allocation priorities

## Connections

- Parent: [[virtualization-security]] — resource contention is a key operational risk in virtualized environments
- See also: [[multitenancy-risks]]
