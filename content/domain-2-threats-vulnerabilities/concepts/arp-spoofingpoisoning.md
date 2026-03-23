---
title: "ARP spoofing/poisoning"
description: "Sending fake ARP messages to associate the attacker's MAC address with a legitimate IP"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

ARP spoofing (also called ARP poisoning) is an attack on local network communication where an attacker sends forged ARP (Address Resolution Protocol) reply messages to associate their own MAC address with the IP address of another host (such as the default gateway). This causes network traffic intended for that host to be redirected through the attacker's machine, enabling man-in-the-middle interception, sniffing, or modification.

## Key Details

- ARP is a **stateless** protocol—hosts accept ARP replies even without sending a request, making it easy to spoof.
- Most commonly used on **local Ethernet segments** (Layer 2); cannot cross routers without additional techniques.
- Enables **man-in-the-middle attacks**: attacker intercepts traffic between victim and gateway.
- **Defenses**: Dynamic ARP Inspection (DAI) on managed switches, static ARP entries for critical hosts, and network monitoring tools (e.g., ArpWatch).
- Often used as a precursor to SSL/TLS stripping or credential harvesting.

## Connections

- Parent: [[network-attacks]] — a fundamental LAN-based network attack
- Parent: [[on-path-attacks]] — the primary technique for executing on-path attacks on local networks
- See also: [[mac-flooding]]
