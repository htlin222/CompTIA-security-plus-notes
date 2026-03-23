---
title: "IP spoofing"
description: "Forging the source IP address of packets to impersonate another system or hide the attacker's identity"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

IP spoofing involves crafting network packets with a falsified (spoofed) source IP address to impersonate another system, hide the attacker's true location, or redirect responses to a victim's IP (as in amplification attacks). Because IP is a connectionless protocol that doesn't inherently verify source addresses, spoofing is technically straightforward—though it limits the attacker's ability to receive responses.

## Key Details

- Used extensively in **amplification/reflection DDoS attacks**—spoofed victim's IP receives all the amplified responses.
- Also used in **blind injection attacks** where the attacker doesn't need to see responses.
- **BCP38 (Network Ingress Filtering)**: ISPs filtering outbound traffic to block packets with spoofed source IPs that don't match their allocated address blocks—the primary mitigation.
- Legitimate TCP sessions are difficult to spoof because the 3-way handshake requires correct sequence numbers—responses go to the spoofed IP.
- **uRPF (Unicast Reverse Path Forwarding)**: Router mechanism that drops packets whose source IP wouldn't be routed back through the same interface.

## Connections

- Parent: [[network-attacks]] — a foundational network-layer attack technique
- See also: [[amplification-attack]], [[smurf-attack]]
