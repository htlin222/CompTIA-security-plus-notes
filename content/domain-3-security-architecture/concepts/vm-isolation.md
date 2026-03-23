---
title: "VM isolation"
description: "ensuring one VM cannot access another VM's memory, storage, or network traffic on the same host"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

## Definition

VM isolation is the security property that ensures virtual machines running on the same physical host cannot access each other's memory, storage, CPU state, or network traffic without explicit authorization. Proper isolation is enforced by the hypervisor and hardware virtualization extensions. It is fundamental to multi-tenant cloud security — a breach of VM isolation allows one customer's workload to access another's data.

## Key Details

- Enforced by the hypervisor using hardware extensions (Intel VT-x/VT-d, AMD-V/IOMMU)
- Memory isolation prevents VMs from reading or writing each other's RAM
- Network isolation achieved through virtual switches, VLANs, and separate virtual NICs
- Storage isolation ensures VMs cannot access each other's virtual disks
- Side-channel attacks (e.g., Spectre, Meltdown) can partially break isolation at the CPU cache level

## Connections

- Parent: [[virtualization-security]] — VM isolation is the core security guarantee of virtualization environments
- See also: [[vm-escape]], [[hardening-the-hypervisor]], [[multitenancy-risks]]
