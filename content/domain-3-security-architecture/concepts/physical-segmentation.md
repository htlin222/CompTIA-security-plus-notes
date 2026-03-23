---
title: "Physical segmentation"
description: "separate physical network infrastructure for different zones"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Physical segmentation?
> It's like having completely separate buildings instead of just separate rooms. Physical segmentation uses different cables, switches, and hardware to keep network sections truly apart -- no shared walls at all.

## Definition

Physical segmentation creates network boundaries using completely separate physical hardware — different switches, cabling, and network infrastructure — for each network zone, rather than using logical separation on shared hardware. Physical segmentation provides the strongest isolation guarantee but is the most expensive and inflexible approach.

## Key Details

- Separate physical switches, routers, and cabling for each network zone
- Traffic cannot cross between segments at Layer 2 — physical separation eliminates VLAN hopping risks
- Used for the most sensitive environments: classified government networks, payment processing, OT/ICS networks
- Very expensive: requires duplicate hardware and cabling for each segment
- Management complexity increases as the number of physically separate networks grows

## Connections

- Parent: [[network-segmentation]] — physical segmentation provides the strongest network isolation
- See also: [[air-gap]]
