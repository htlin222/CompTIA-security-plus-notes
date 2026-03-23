---
title: "Fake telemetry"
description: "Generating false network data to confuse attackers performing reconnaissance"
draft: false
date: 2026-03-20
tags:
  - domain/1
  - type/sub-topic
---

> [!eli5] ELI5: What is Fake Telemetry?
> It's like putting up fake street signs to confuse a burglar who's trying to map out your neighborhood. The bad guy gets a totally wrong picture of where everything is.

## Definition

Fake telemetry is a deception technique that generates fictitious network traffic, system events, or data flows to mislead attackers who are conducting reconnaissance. By polluting the attacker's information gathering with false data—fake open ports, phantom hosts, fictitious network topology—defenders make it significantly harder for attackers to accurately map the environment and plan their attack.

## Key Details

- Creates **information asymmetry**—defenders know what's real, attackers must sift through false signals.
- Can include: fake **open ports** (responding to scans), phantom **ARP entries**, false **routing tables**, fake **user accounts**.
- Works alongside **honeypots** and **honeynets** to create a comprehensive deceptive environment.
- Increases **attacker dwell time** wasted on false leads—allowing defenders more time to detect and respond.
- Used in enterprise deception platforms that automate the generation and management of fake telemetry.

## Connections

- Parent: [[deception-technologies]] — a deception technique targeting attacker reconnaissance
- See also: [[honeypots]], [[deception-platforms]]
