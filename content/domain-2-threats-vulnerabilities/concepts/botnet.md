---
title: "Botnet"
description: "Network of compromised devices controlled by an attacker to generate DDoS traffic"
draft: false
date: 2026-03-20
tags:
  - domain/2
  - type/sub-topic
---

> [!eli5] ELI5: What is a Botnet?
> Picture a villain who secretly takes control of thousands of toy robots and commands them all to attack at once. A botnet is a big group of hacked computers that one bad person controls like an army.

## Definition

A botnet is a network of internet-connected devices that have been compromised by malware and are remotely controlled by a threat actor (the "bot herder") without the device owners' knowledge. Botnets are used to launch DDoS attacks, send spam, distribute malware, conduct credential stuffing, and perform cryptocurrency mining. IoT devices are increasingly recruited into botnets due to their poor security defaults.

## Key Details

- Individual compromised devices in a botnet are called **bots** or **zombies**.
- Controlled via **Command and Control (C2 or C&C)** infrastructure—can be centralized servers or peer-to-peer.
- **Mirai botnet** (2016) famously weaponized IoT devices (cameras, DVRs) to launch record-breaking DDoS attacks.
- **DNS sinkholes** can disrupt botnet C2 communications by redirecting malicious domain lookups.
- Indicators of botnet infection: unusual outbound traffic, high bandwidth usage, connections to known C2 IPs.

## Connections

- Parent: [[denial-of-service]] — primary tool used in large-scale DDoS attacks
- See also: [[amplificationreflection]]
