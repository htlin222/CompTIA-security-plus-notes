---
title: "Honeynets"
description: "Networks of honeypots simulating an entire environment to study attacker behavior"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

## Definition

A honeynet is a network of interconnected honeypot systems designed to simulate a realistic network environment. Unlike a single honeypot, a honeynet provides attackers with multiple services to interact with (web servers, file servers, workstations, routers), creating a convincing trap that encourages deeper investigation. This allows defenders to observe complete attack chains, TTPs (Tactics, Techniques, and Procedures), and lateral movement behavior.

## Key Details

- Honeynets are **research-grade deception** infrastructure—much more complex to deploy and manage than individual honeypots.
- All traffic entering the honeynet is suspicious; all traffic leaving must be controlled to prevent attackers from using honeynets to attack others.
- **Honeywall**: A gateway device that monitors, captures, and controls all honeynet traffic.
- Provides insight into attacker TTPs—valuable for updating detection rules, training staff, and contributing to threat intelligence.
- The **Honeynet Project** is a non-profit organization that pioneered honeynet research and shares threat data.

## Connections

- Parent: [[deception-technologies]] — a network-scale deception deployment
- See also: [[honeypots]], [[deception-platforms]]
