---
title: "East-west vs. north-south traffic"
description: "east-west is internal lateral; north-south crosses the network boundary"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is East-west vs. north-south traffic?
> North-south traffic is like people walking in and out of a building's front door. East-west traffic is people walking between rooms inside the building. Both need to be watched, but they require different kinds of security checks.

## Definition

East-west traffic refers to data flowing laterally between systems within the same internal network or data center, while north-south traffic refers to data flowing vertically between internal systems and external networks (the internet or remote users). Security architectures must address both traffic flows, as they present different threat profiles and control requirements.

## Key Details

- **North-south**: traffic crossing the network perimeter (internet → internal, or internal → internet)
- **East-west**: traffic flowing between servers, microservices, or systems within the internal network
- Traditional firewall-centric security focused almost exclusively on north-south traffic
- As cloud and microservices architectures grew, east-west traffic volumes now often exceed north-south
- Zero trust and micro-segmentation strategies address the security of east-west traffic

## Connections

- Parent: [[network-security-architecture]] — understanding traffic directions is fundamental to security architecture
- See also: [[east-west-traffic-control]]
