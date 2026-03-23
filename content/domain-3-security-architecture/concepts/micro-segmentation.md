---
title: "Micro-segmentation"
description: "granular segmentation within a network, often at the workload level"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Micro-segmentation?
> Regular segmentation divides a building into floors. Micro-segmentation goes further and puts a locked door on every single room. Each individual program or service gets its own tiny protected space.

## Definition

Micro-segmentation is a highly granular network security approach that creates individual security perimeters around specific workloads, applications, or even individual virtual machines — far more granular than traditional VLAN-based segmentation. Implemented primarily through software-defined networking and virtualization platforms, micro-segmentation limits lateral movement by applying zero-trust principles within the network interior.

## Key Details

- Creates per-workload firewall policies rather than per-segment policies
- Implemented using SDN controllers, hypervisor-level firewalls (VMware NSX, Hyper-V), or container network policies
- Enables zero-trust network access at a granular level within the data center
- A compromised workload cannot communicate with other workloads unless explicitly allowed
- Particularly valuable in cloud environments where traditional perimeter controls are limited

## Connections

- Parent: [[network-security-architecture]] — micro-segmentation is an advanced network security architecture pattern
- Parent: [[network-segmentation]] — micro-segmentation is the most granular form of network segmentation
- See also: [[zero-trust-architecture]]
