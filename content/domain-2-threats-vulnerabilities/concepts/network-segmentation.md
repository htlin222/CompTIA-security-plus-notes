---
title: "Network segmentation"
description: "Dividing the network into isolated zones to limit lateral movement and blast radius"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is Network Segmentation?
> It's like dividing a ship into watertight sections. If one section floods, the water stays there and doesn't sink the whole ship. Segmentation keeps a hacked part of the network from spreading to everything else.

## Definition

Network segmentation divides a network into isolated zones or segments—separated by firewalls, VLANs, or other controls—to contain the spread of threats and limit an attacker's ability to move laterally between systems. Even if one segment is compromised, segmentation prevents the attacker from freely accessing other parts of the network, reducing the blast radius of a security incident.

## Key Details

- **VLANs**: Software-defined network segments that isolate broadcast domains at Layer 2—efficient and flexible.
- **DMZ (Demilitarized Zone)**: An intermediate zone for internet-facing servers, separated from both the internet and the internal network.
- **Microsegmentation**: Fine-grained segmentation at the workload or individual host level—often implemented in software-defined networking (SDN) or cloud environments.
- **Zero Trust microsegmentation**: All inter-zone traffic requires explicit authorization, regardless of which zone it originates from.
- Ransomware containment: segmented networks prevent ransomware from spreading from one VLAN to encrypt network shares in another.

## Connections

- Parent: [[mitigation-techniques]] — a network architecture mitigation technique
- See also: [[access-control-lists-acls]]
