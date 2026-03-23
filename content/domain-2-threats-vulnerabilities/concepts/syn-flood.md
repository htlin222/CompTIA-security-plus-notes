---
title: "SYN flood"
description: "Sending many TCP SYN packets without completing the handshake, filling the target's connection table"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

## Definition

A SYN flood is a denial-of-service attack that exploits the TCP three-way handshake by sending many SYN packets to a target server without completing the handshake (never sending the final ACK). The server allocates resources for each half-open connection and waits for the ACK, filling its connection table (the SYN backlog) until it can no longer accept new legitimate connections.

## Key Details

- TCP handshake: SYN → SYN-ACK → ACK. In a SYN flood, the attacker sends SYN packets but never sends the final ACK—leaving connections "half-open."
- The server's **SYN backlog queue** has a finite size—once filled, new connection requests are dropped.
- Typically uses **spoofed source IPs** so the SYN-ACK replies go to non-existent hosts and the attacker is harder to trace.
- **SYN cookies**: The primary mitigation—the server encodes connection state in the sequence number rather than allocating memory for each half-open connection; resources are only allocated when the ACK arrives with the correct cookie.
- **Firewalls** and **load balancers** can absorb SYN floods with SYN proxy functionality.

## Connections

- Parent: [[denial-of-service]] — a protocol attack targeting TCP handshake state
- See also: [[protocol-attacks]]
