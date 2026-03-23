---
title: "Logical segmentation"
description: "VLANs, subnets, and software-defined boundaries on shared infrastructure"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is Logical segmentation?
> Instead of building actual walls, you use invisible lines on the floor to divide a room into sections. Logical segmentation uses software rules to split one network into separate zones without needing different physical cables.

## Definition

Logical segmentation creates network boundaries using software-defined mechanisms rather than separate physical hardware. Technologies like VLANs, subnets, and software-defined networking (SDN) enable the creation of isolated network segments on shared physical infrastructure. Logical segmentation is more cost-effective and flexible than physical segmentation while providing meaningful security boundaries.

## Key Details

- **VLANs**: tag-based isolation at Layer 2; same physical switch can host multiple isolated VLANs
- **Subnets**: Layer 3 boundaries that require routing between them; can enforce access control via ACLs
- **Software-defined networking (SDN)**: programmatic creation and management of network segments
- Traffic between logical segments can be inspected and filtered by routers and firewalls
- VLAN hopping attacks are a risk if VLAN configurations are not properly hardened

## Connections

- Parent: [[network-segmentation]] — logical segmentation is the primary segmentation approach in modern networks
- See also: [[vlans-virtual-lans]]
