---
title: "MAC flooding"
description: "Overwhelming a switch's CAM table to force it into hub mode, broadcasting traffic to all ports"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

MAC flooding is an attack against network switches that overwhelms the switch's Content Addressable Memory (CAM) table—which maps MAC addresses to switch ports—by flooding it with many fake MAC addresses. When the CAM table is full, the switch fails open into hub mode, broadcasting all traffic out all ports instead of only the intended destination port, allowing the attacker to capture traffic from the entire network segment.

## Key Details

- Switches normally **unicast** traffic directly to the correct port based on the CAM table—MAC flooding breaks this.
- When the CAM table overflows, the switch broadcasts frames out all ports (called **unicast flooding**)—attackers on any port can capture all traffic.
- Enables sniffing of traffic not intended for the attacker's port—similar to being on a shared hub network.
- **Defense**: **Port security** on managed switches—limits the number of MAC addresses learned per port; excess triggers an alert or shutdown.
- Also defeated by **Private VLANs** and **dynamic ARP inspection**.

## Connections

- Parent: [[network-attacks]] — a Layer 2 switch attack enabling traffic capture
- See also: [[arp-spoofingpoisoning]]
