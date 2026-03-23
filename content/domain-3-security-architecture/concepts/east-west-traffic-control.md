---
title: "East-west traffic control"
description: "segmentation is essential for monitoring and controlling internal lateral movement"
draft: false
date: 2026-03-20
tags:
  - domain/3
  - type/sub-topic
---

> [!eli5] ELI5: What is East-west traffic control?
> Once someone is inside a building, you still want to make sure they cannot wander into every room. East-west traffic control is about watching and limiting movement between rooms (systems) that are already inside the same network.

## Definition

East-west traffic control refers to the security monitoring and restriction of traffic flowing laterally between systems within the same network, as opposed to north-south traffic that crosses the network perimeter. Once attackers breach the perimeter, they often move laterally between internal systems to expand access — proper east-west controls limit this lateral movement.

## Key Details

- Traditional perimeter firewalls focus on north-south traffic; east-west often flows freely internally
- Micro-segmentation creates internal boundaries that restrict lateral movement
- Zero trust principles require authentication and authorization even for internal east-west traffic
- Network monitoring of east-west traffic is often limited — many organizations have poor internal visibility
- Attackers rely on unrestricted east-west traffic for lateral movement and propagation

## Connections

- Parent: [[network-segmentation]] — east-west traffic control is a key goal of network segmentation
- See also: [[micro-segmentation]]
