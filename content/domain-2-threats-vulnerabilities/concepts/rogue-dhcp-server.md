---
title: "Rogue DHCP server"
description: "Unauthorized DHCP server providing malicious gateway or DNS settings to clients"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Rogue DHCP Server?
> When your computer joins a network, it asks for directions. A rogue DHCP server is like a fake information desk that gives you wrong directions, sending all your traffic through the attacker instead.

## Definition

A rogue DHCP server is an unauthorized DHCP server on a network segment that races to respond to client DHCP requests before the legitimate server. When a client receives a response from the rogue server, it is assigned malicious network configuration—particularly a rogue default gateway (enabling traffic interception) and rogue DNS servers (enabling DNS spoofing). This enables a network-level man-in-the-middle attack.

## Key Details

- Wins the DHCP race by responding faster than the legitimate server—clients accept the first valid DHCP offer they receive.
- By providing a **malicious default gateway**: all client traffic is routed through the attacker's machine—full traffic interception.
- By providing **malicious DNS servers**: DNS responses can be spoofed, redirecting all name resolution to attacker-controlled IPs.
- **Mitigation**: **DHCP snooping** on managed switches—only allows DHCP server responses from trusted ports; client-facing ports are marked as untrusted and DHCP server traffic from them is dropped.
- Can be set up very easily—a laptop running DHCP server software can become a rogue DHCP server.

## Connections

- Parent: [[network-attacks]] — a network configuration attack enabling MitM
- See also: [[arp-spoofingpoisoning]]
