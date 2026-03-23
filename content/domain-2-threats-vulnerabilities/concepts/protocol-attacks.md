---
title: "Protocol attacks"
description: "Exploiting protocol weaknesses to consume server resources (SYN flood, Ping of Death, Smurf attack)"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What are Protocol Attacks?
> Computers follow rules (protocols) to talk to each other. These attacks abuse those rules -- like starting a handshake but never finishing, leaving the other person standing there with their hand out until they run out of patience.

## Definition

Protocol attacks (also called state exhaustion attacks) exploit weaknesses in network protocols to consume server or network device resources such as connection state tables, CPU, and memory. Unlike volumetric attacks (which saturate bandwidth), protocol attacks target the finite capacity of the target's protocol handling infrastructure—particularly stateful connection tracking in firewalls and load balancers.

## Key Details

- **SYN flood**: Sends many SYN packets without completing the handshake—fills the server's TCP connection table with half-open connections.
- **Ping of Death**: Sends malformed or oversized ICMP packets that crash the target (largely patched in modern systems).
- **Smurf attack**: Sends ICMP echo requests with spoofed source (victim's IP) to a broadcast address—all hosts reply to the victim.
- **Mitigation for SYN flood**: **SYN cookies**—allows the server to track connection state without allocating resources until the handshake is complete.
- Often combined with other attack types in large-scale DDoS campaigns.

## Connections

- Parent: [[denial-of-service]] — a category of DoS attack exploiting protocol weaknesses
- See also: [[syn-flood]], [[smurf-attack]]
