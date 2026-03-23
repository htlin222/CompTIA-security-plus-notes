---
title: "Multitenancy risks"
description: "data isolation between tenants; side-channel attacks; resource contention"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What are Multitenancy risks?
> Sharing a cloud computer is like sharing an apartment building. If the walls are thin, your neighbor might hear your conversations or use up all the hot water. Multitenancy risks are the dangers that come from multiple customers sharing the same physical hardware.

## Definition

Multitenancy risks arise in cloud environments where multiple customers (tenants) share the same underlying physical infrastructure, hypervisors, or application platforms. While cloud providers implement strong isolation controls, sharing physical resources creates theoretical risks that do not exist in dedicated private infrastructure, including data leakage between tenants and side-channel attacks.

## Key Details

- **Data isolation**: data from one tenant must never be accessible by another tenant; virtualization and encryption enforce this
- **Side-channel attacks**: exploiting shared resources (CPU caches, shared memory) to extract information from co-tenant processes (Spectre, Meltdown)
- **Resource contention**: "noisy neighbor" problem where one tenant's high resource usage degrades performance for others
- Cloud providers use hardware isolation, hypervisor hardening, and memory encryption to mitigate these risks
- Highly sensitive workloads may require dedicated hosts or private cloud deployments to eliminate shared-resource risk

## Connections

- Parent: [[cloud-security]] — multitenancy risks are inherent to shared cloud infrastructure
- See also: [[shared-responsibility-model]]
